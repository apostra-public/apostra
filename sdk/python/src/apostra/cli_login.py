"""The credential store behind `apostra login`, shared with the CLI and the TypeScript SDK.

Login tokens live in the operating system credential store. Existing
``credentials.json`` entries migrate on first use. It never opens a browser:
sign-in stays in the CLI. Refresh tokens rotate, so a Python process and a
Node process take the same lock file before they refresh, and one of them
reuses the other's result.
"""

from __future__ import annotations

import asyncio
import importlib
import json
import math
import os
import random
import sys
import threading
import uuid
import warnings
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime, timedelta
from pathlib import Path
from time import monotonic, sleep, time
from typing import Any, TypedDict, cast
from urllib.parse import urlsplit

import httpx
import keyring

from ._version import BASE_URL
from .transport import AsyncTokenProvider, ConnectionError, TimeoutError, TokenProvider

_FRESH_MARGIN = timedelta(seconds=60)
_REQUEST_TIMEOUT = 15.0
_LOCK_STALE_S = 30.0
_LOCK_HEARTBEAT_S = 5.0
_LOCK_WAIT_S = 30.0
_LOOPBACK_HOSTS = {"localhost", "127.0.0.1", "::1"}
_DEFAULT_PORTS = {"https": 443, "http": 80}
_KEYRING_SERVICE = "Apostra CLI login"
_LINUX_SECRET_ATTRIBUTES = ("service", "username")
_LINUX_KEYTAR_ATTRIBUTES = ("service", "account")


class CliLoginEntry(TypedDict):
    """One stored sign-in. Field names are the file's, shared with the CLI."""

    issuer: str
    resource: str
    clientId: str
    accessToken: str
    refreshToken: str
    expiresAt: str
    accountId: str
    scopes: list[str]


def credentials_path() -> Path:
    """`${XDG_CONFIG_HOME:-~/.config}/apostra/credentials.json` (`%APPDATA%` on Windows)."""
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        base = (
            Path(appdata)
            if appdata is not None
            else Path.home() / "AppData" / "Roaming"
        )
    else:
        xdg = os.environ.get("XDG_CONFIG_HOME")
        base = Path(xdg) if xdg and os.path.isabs(xdg) else Path.home() / ".config"
    return base / "apostra" / "credentials.json"


def _secure_url(value: object, name: str) -> str:
    url = urlsplit(value if isinstance(value, str) else "")
    host = url.hostname
    if (
        not host
        or url.username
        or url.password
        or url.fragment
        or (
            url.scheme != "https"
            and not (url.scheme == "http" and host in _LOOPBACK_HOSTS)
        )
    ):
        raise ValueError(f"{name} must be an HTTPS URL (HTTP only on loopback)")
    port = url.port
    netloc = f"[{host}]" if ":" in host else host
    if port is not None and port != _DEFAULT_PORTS[url.scheme]:
        netloc += f":{port}"
    query = f"?{url.query}" if url.query else ""
    return f"{url.scheme}://{netloc}{url.path or '/'}{query}"


def normalize_base_url(raw: str) -> str:
    """The store key: the API base URL as the CLI writes it, without a trailing slash."""
    href = _secure_url(raw, "Base URL")
    if urlsplit(href).query:
        raise ValueError("Base URL must not have a query string")
    return href.removesuffix("/")


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)


def _format_time(value: datetime) -> str:
    return value.astimezone(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _parse_entry(value: object) -> CliLoginEntry | None:
    if not isinstance(value, dict):
        return None
    fields = cast(dict[str, object], value)
    scopes = fields.get("scopes")
    expires_at = _parse_time(fields.get("expiresAt"))
    if (
        not all(
            isinstance(fields.get(k), str) and fields[k]
            for k in ("issuer", "resource", "clientId", "accessToken", "refreshToken")
        )
        or expires_at is None
        or not isinstance(fields.get("accountId"), str)
        or not isinstance(scopes, list)
        or not all(isinstance(s, str) for s in cast(list[object], scopes))
    ):
        return None
    # Credential stores round-trip text. Canonicalise at their boundary so a
    # value with sub-millisecond precision cannot oscillate between clients.
    return cast(CliLoginEntry, {**fields, "expiresAt": _format_time(expires_at)})


def _read_file_store() -> tuple[dict[str, object], set[str]]:
    try:
        file: object = json.loads(credentials_path().read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}, set()
    if not isinstance(file, dict):
        return {}, set()
    fields = cast(dict[str, object], file)
    logins = fields.get("logins")
    authoritative = fields.get("authoritativeFileLogins")
    authoritative_values = cast(list[object], authoritative) if isinstance(authoritative, list) else []
    return (
        cast(dict[str, object], logins) if isinstance(logins, dict) else {},
        {resource for resource in authoritative_values if isinstance(resource, str)},
    )


def _write_file_logins(
    logins: dict[str, object], authoritative: set[str] | None = None
) -> None:
    """Atomic (temp file + rename), directory 0700, file 0600."""
    path = credentials_path()
    path.parent.mkdir(parents=True, mode=0o700, exist_ok=True)
    os.chmod(path.parent, 0o700)
    if not logins:
        path.unlink(missing_ok=True)
        return
    temp = path.with_name(f"{path.name}.{os.getpid()}.{uuid.uuid4().hex[:8]}.tmp")
    fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "version": 1,
                        "logins": logins,
                        **(
                            {
                                "authoritativeFileLogins": sorted(
                                    authoritative & set(logins)
                                )
                            }
                            if authoritative
                            else {}
                        ),
                    },
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n"
            )
        os.replace(temp, path)
    except BaseException:
        temp.unlink(missing_ok=True)
        raise


def _secretstorage() -> Any:
    """Load SecretStorage only where the CLI uses Secret Service directly."""
    return importlib.import_module("secretstorage")


def _unlock_linux_secret(item: Any) -> None:
    if item.is_locked():
        item.unlock()
        if item.is_locked():
            raise RuntimeError("Secret Service item remained locked")


def _linux_secret_collection() -> tuple[Any, Any]:
    secretstorage = _secretstorage()
    connection = secretstorage.dbus_init()
    try:
        collection = secretstorage.get_default_collection(connection)
        _unlock_linux_secret(collection)
        return collection, connection
    except BaseException:
        connection.close()
        raise


def _linux_secret_items(collection: Any, resource: str) -> list[Any]:
    # @napi-rs/keyring 2.1.1 builds a Rust keyring Entry, whose Secret Service
    # implementation stores `service` and `username`. Some keytar-compatible
    # stores expose the same Entry's second argument as `account`, so read that
    # representation too without changing the CLI's current write contract.
    native = list(
        collection.search_items(
            dict(zip(_LINUX_SECRET_ATTRIBUTES, (_KEYRING_SERVICE, resource)))
        )
    )
    if native:
        return native
    return list(
        collection.search_items(
            dict(zip(_LINUX_KEYTAR_ATTRIBUTES, (_KEYRING_SERVICE, resource)))
        )
    )


def _read_linux_secure_password(resource: str) -> str | None:
    collection, connection = _linux_secret_collection()
    try:
        items = _linux_secret_items(collection, resource)
        if len(items) > 1:
            raise RuntimeError("Secret Service has ambiguous Apostra login entries")
        if not items:
            return None
        _unlock_linux_secret(items[0])
        return cast(bytes, items[0].get_secret()).decode("utf-8")
    finally:
        connection.close()


def _write_linux_secure_password(resource: str, password: str) -> None:
    collection, connection = _linux_secret_collection()
    try:
        items = _linux_secret_items(collection, resource)
        if len(items) > 1:
            raise RuntimeError("Secret Service has ambiguous Apostra login entries")
        encoded = password.encode("utf-8")
        if items:
            _unlock_linux_secret(items[0])
            items[0].set_secret(encoded, content_type="application/octet-stream")
            return
        collection.create_item(
            f"keyring:{resource}@{_KEYRING_SERVICE}",
            dict(zip(_LINUX_SECRET_ATTRIBUTES, (_KEYRING_SERVICE, resource))),
            encoded,
            replace=True,
            content_type="application/octet-stream",
        )
    finally:
        connection.close()


def _read_secure_login(resource: str) -> tuple[bool, CliLoginEntry | None]:
    try:
        password = (
            _read_linux_secure_password(resource)
            if sys.platform == "linux"
            else keyring.get_password(_KEYRING_SERVICE, resource)
        )
    except Exception:
        return False, None
    if password is None:
        return True, None
    try:
        return True, _parse_entry(json.loads(password))
    except ValueError:
        return True, None


def _write_secure_login(resource: str, entry: CliLoginEntry) -> bool:
    try:
        password = json.dumps(entry)
        if sys.platform == "linux":
            _write_linux_secure_password(resource, password)
        else:
            keyring.set_password(_KEYRING_SERVICE, resource, password)
        return True
    except Exception:
        return False


def _warn_file_fallback() -> None:
    path = credentials_path()
    marker = path.parent / ".file-store-warning"
    try:
        path.parent.mkdir(parents=True, mode=0o700, exist_ok=True)
        os.chmod(path.parent, 0o700)
        os.close(os.open(marker, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600))
    except FileExistsError:
        return
    except OSError:
        # If the marker cannot be written, warn for this process rather than
        # silently accepting plaintext storage.
        pass
    warnings.warn(
        "Apostra could not access your OS credential store. Login tokens are "
        f"stored in {path} with 0600 permissions. Use Keychain, Credential "
        "Manager, or Secret Service when available.",
        RuntimeWarning,
        stacklevel=3,
    )


def _migrate_file_logins(lock_held: bool = False) -> bool:
    """Move all valid legacy entries without overwriting a refreshed credential."""
    file_logins, authoritative = _read_file_store()
    entries = [
        (resource, entry)
        for resource, value in file_logins.items()
        if (entry := _parse_entry(value)) is not None
    ]
    if not entries:
        return False
    if not lock_held:
        try:
            with cli_login_lock():
                return _migrate_file_logins(lock_held=True)
        except TimeoutError:
            return False
    remaining = dict(file_logins)
    remaining_authoritative = set(authoritative)
    for resource, entry in entries:
        available, stored = _read_secure_login(resource)
        if resource not in authoritative and stored is not None:
            remaining.pop(resource, None)
            remaining_authoritative.discard(resource)
            continue
        if not available or not _write_secure_login(resource, entry):
            # Retain only entries that still need migration. Otherwise a
            # successfully migrated authoritative login could shadow its next
            # secure-store refresh while another login remains in the file.
            _write_file_logins(remaining, remaining_authoritative)
            return False
        remaining.pop(resource, None)
        remaining_authoritative.discard(resource)
    _write_file_logins(remaining, remaining_authoritative)
    return True


def _read_cli_login(base_url: str, *, lock_held: bool = False) -> CliLoginEntry | None:
    resource = normalize_base_url(base_url)
    file_logins, authoritative = _read_file_store()
    file_login = _parse_entry(file_logins.get(resource))
    # A refresh token can rotate before a credential store reports an update
    # failure. This marker makes its 0600 fallback authoritative over the now
    # invalid secure-store value until a later read can migrate it safely.
    if resource in authoritative and file_login is not None:
        return file_login
    available, secure = _read_secure_login(resource)
    if secure is not None:
        return secure
    if not file_logins:
        return None
    if _migrate_file_logins(lock_held=lock_held):
        _, secure = _read_secure_login(resource)
        return secure
    if not available:
        _warn_file_fallback()
    return file_login


def read_cli_login(base_url: str) -> CliLoginEntry | None:
    return _read_cli_login(base_url)


def stored_cli_login(base_url: str) -> CliLoginEntry | None:
    """Like `read_cli_login`, but never raises: for the SDK's default credential chain."""
    try:
        return read_cli_login(base_url)
    except Exception:
        return None


def is_fresh(entry: CliLoginEntry) -> bool:
    expires = _parse_time(entry["expiresAt"])
    return expires is not None and expires - _FRESH_MARGIN > datetime.now(UTC)


def break_stale_lock(lock: Path) -> bool:
    """Remove a lock whose heartbeat stopped, without ever removing a live one.

    Only the holder of the takeover guard checks and removes. Checking again
    under the guard means a lock another process took after the first check is
    fresh and is left alone. A guard a crashed process left behind goes stale
    like a lock does. Returns whether this call held the guard, so the caller
    retries at once; otherwise it waits like any other contender.
    """
    guard = Path(f"{lock}.takeover")
    try:
        os.close(os.open(guard, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600))
    except FileExistsError:
        try:
            if time() - guard.stat().st_mtime > _LOCK_STALE_S:
                guard.unlink(missing_ok=True)
        except OSError:
            pass
        return False
    try:
        if time() - lock.stat().st_mtime > _LOCK_STALE_S:
            lock.unlink(missing_ok=True)
    except OSError:
        pass
    finally:
        guard.unlink(missing_ok=True)
    return True


@contextmanager
def cli_login_lock() -> Iterator[None]:
    """Serialise every read-modify-write of the store, across processes.

    The lock file holds its owner's token, so a process only ever removes a
    lock it owns, and a heartbeat keeps a live lock fresh however long the
    refresh takes. Only a lock whose heartbeat stopped for 30 seconds is stale.
    """
    lock = Path(f"{credentials_path()}.lock")
    lock.parent.mkdir(parents=True, mode=0o700, exist_ok=True)
    owner = f"{os.getpid()}:{uuid.uuid4()}"

    def owner_of() -> str | None:
        try:
            return lock.read_text(encoding="utf-8")
        except OSError:
            return None

    deadline = monotonic() + _LOCK_WAIT_S
    while True:
        try:
            fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError:
            try:
                if time() - lock.stat().st_mtime > _LOCK_STALE_S:
                    if break_stale_lock(lock):
                        continue
            except OSError:
                continue
            if monotonic() > deadline:
                raise TimeoutError(
                    "Timed out waiting for another Apostra login process"
                )
            sleep(0.025 + random.random() * 0.05)
            continue
        try:
            os.write(fd, owner.encode())
        finally:
            os.close(fd)
        break

    stopped = threading.Event()

    def beat() -> None:
        while not stopped.wait(_LOCK_HEARTBEAT_S):
            try:
                if owner_of() == owner:
                    os.utime(lock)
            except OSError:
                pass  # A missed beat only shortens the lease; the owner check still holds.

    threading.Thread(target=beat, daemon=True).start()
    try:
        yield
    finally:
        stopped.set()
        if owner_of() == owner:
            lock.unlink(missing_ok=True)


def write_cli_login(base_url: str, entry: CliLoginEntry) -> None:
    """Save a login. Call inside `cli_login_lock`."""
    resource = normalize_base_url(base_url)
    normalized = _parse_entry(entry)
    if normalized is None:
        raise ValueError("Apostra login is invalid")
    entry = normalized
    _migrate_file_logins(lock_held=True)
    secure_store_available, existing_secure_login = _read_secure_login(resource)
    if _write_secure_login(resource, entry):
        return
    _warn_file_fallback()
    file_logins, authoritative = _read_file_store()
    if not secure_store_available or existing_secure_login is not None:
        # Refresh-token rotation invalidates the old secure credential. Keep
        # the replacement in the protected fallback file and mark it ahead of
        # a stale secure-store value until it can be migrated. An unavailable
        # read is also unsafe: the store may recover with the old credential
        # after this write has failed.
        authoritative.add(resource)
    _write_file_logins({**file_logins, resource: entry}, authoritative)


@contextmanager
def _client(http_client: httpx.Client | None) -> Iterator[httpx.Client]:
    if http_client is not None:
        yield http_client
    else:
        with httpx.Client() as client:
            yield client


def _send(
    client: httpx.Client, method: str, url: str, data: dict[str, str] | None = None
) -> httpx.Response:
    try:
        return client.request(
            method,
            url,
            data=data,
            headers={"Accept": "application/json"},
            follow_redirects=False,
            timeout=_REQUEST_TIMEOUT,
        )
    except httpx.TimeoutException as error:
        raise TimeoutError("Apostra sign-in request timed out") from error
    except httpx.HTTPError as error:
        raise ConnectionError("Apostra sign-in request failed") from error


def _json(response: httpx.Response) -> object:
    try:
        return cast(object, response.json())
    except ValueError:
        return None


def _token_endpoint(client: httpx.Client, issuer: str) -> str:
    """The token endpoint from the stored issuer's authorization-server metadata (RFC 8414)."""
    issuer = _secure_url(issuer, "Issuer").removesuffix("/")
    parts = urlsplit(issuer)
    path = "" if parts.path in ("", "/") else parts.path
    url = (
        f"{parts.scheme}://{parts.netloc}/.well-known/oauth-authorization-server{path}"
    )
    response = _send(client, "GET", url)
    if not response.is_success:
        raise ValueError(f"Could not read {url} (HTTP {response.status_code})")
    metadata = _json(response)
    if (
        not isinstance(metadata, dict)
        or cast(dict[str, object], metadata).get("issuer") != issuer
    ):
        raise ValueError(f"{issuer} published mismatched authorization-server metadata")
    return _secure_url(
        cast(dict[str, object], metadata).get("token_endpoint"), "token_endpoint"
    )


def _refreshed(
    client: httpx.Client, entry: CliLoginEntry
) -> tuple[str, str, str, list[str] | None]:
    endpoint = _token_endpoint(client, entry["issuer"])
    response = _send(
        client,
        "POST",
        endpoint,
        {
            "grant_type": "refresh_token",
            "refresh_token": entry["refreshToken"],
            "client_id": entry["clientId"],
            "resource": entry["resource"],
        },
    )
    body = _json(response)
    fields = cast(dict[str, object], body) if isinstance(body, dict) else {}
    if not response.is_success:
        # Never echo the response body: it may carry reflected credentials.
        if fields.get("error") == "invalid_grant":
            raise ValueError(
                "Your Apostra login expired or was revoked. Run `apostra login` again."
            )
        raise ValueError(f"Apostra token request failed (HTTP {response.status_code})")
    access = fields.get("access_token")
    expires_in = fields.get("expires_in")
    if (
        not isinstance(access, str)
        or not access
        or not isinstance(expires_in, (int, float))
        or isinstance(expires_in, bool)
        or not math.isfinite(expires_in)
        or expires_in <= 0
    ):
        raise ValueError("Apostra token response is invalid")
    try:
        expires_at = (
            (datetime.now(UTC) + timedelta(seconds=expires_in))
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z")
        )
    except (OverflowError, ValueError):
        raise ValueError("Apostra token response is invalid") from None
    # Rotation: the old refresh token is spent; keep the new one. A refresh
    # that does not rotate keeps the old one.
    rotated = fields.get("refresh_token")
    refresh = rotated if isinstance(rotated, str) and rotated else entry["refreshToken"]
    scope = fields.get("scope")
    scopes = [s for s in scope.split(" ") if s] if isinstance(scope, str) else None
    return access, refresh, expires_at, scopes


def refresh_cli_login(
    base_url: str, *, http_client: httpx.Client | None = None
) -> CliLoginEntry:
    """Return a usable login for `base_url`, refreshing it if the access token is about to expire.

    After taking the lock the file is read again: if another process refreshed
    first, its token is used and no request is made.
    """
    key = normalize_base_url(base_url)

    def missing() -> ValueError:
        return ValueError(f"Not signed in to {key}. Run `apostra login`.")

    first = read_cli_login(key)
    if first is None:
        raise missing()
    if is_fresh(first):
        return first
    with cli_login_lock():
        entry = _read_cli_login(key, lock_held=True)
        if entry is None:
            raise missing()
        if is_fresh(entry):
            return entry
        with _client(http_client) as client:
            access, refresh, expires_at, scopes = _refreshed(client, entry)
        updated: CliLoginEntry = {
            **entry,
            "accessToken": access,
            "refreshToken": refresh,
            "expiresAt": expires_at,
            "scopes": scopes if scopes is not None else entry["scopes"],
        }
        write_cli_login(key, updated)
        return updated


def _resolved_key(base_url: str | None) -> str:
    return normalize_base_url(
        base_url
        if base_url is not None
        else os.environ.get("APOSTRA_BASE_URL", BASE_URL)
    )


def cli_login_token_provider(
    *, base_url: str | None = None, http_client: httpx.Client | None = None
) -> TokenProvider:
    """A token provider backed by `apostra login`, for `token_provider=`.

    The clients use it themselves when no explicit credential or
    `APOSTRA_API_KEY` is set and a login exists for the base URL.
    """
    key = _resolved_key(base_url)
    lock = threading.Lock()

    def provider() -> str:
        entry = read_cli_login(key)
        if entry is not None and is_fresh(entry):
            return entry["accessToken"]
        with lock:
            return refresh_cli_login(key, http_client=http_client)["accessToken"]

    return provider


def cli_login_token_provider_async(
    *, base_url: str | None = None
) -> AsyncTokenProvider:
    """Async counterpart to `cli_login_token_provider` with one in-flight refresh."""
    sync = cli_login_token_provider(base_url=base_url)
    lock = asyncio.Lock()

    async def provider() -> str:
        async with lock:
            return await asyncio.to_thread(sync)

    return provider
