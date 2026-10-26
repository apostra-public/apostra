"""The credential store behind `apostra login`, shared with the CLI and the TypeScript SDK.

The CLI writes `credentials.json`; this module reads it and refreshes the
access token in place. It never opens a browser: sign-in stays in the CLI.
Refresh tokens rotate, so a Python process and a Node process take the same
lock file before they refresh, and one of them reuses the other's result.
"""

from __future__ import annotations

import asyncio
import json
import math
import os
import random
import sys
import threading
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime, timedelta
from pathlib import Path
from time import monotonic, sleep, time
from typing import TypedDict, cast
from urllib.parse import urlsplit

import httpx

from ._version import BASE_URL
from .transport import AsyncTokenProvider, ConnectionError, TimeoutError, TokenProvider

_FRESH_MARGIN = timedelta(seconds=60)
_REQUEST_TIMEOUT = 15.0
_LOCK_STALE_S = 30.0
_LOCK_HEARTBEAT_S = 5.0
_LOCK_WAIT_S = 30.0
_LOOPBACK_HOSTS = {"localhost", "127.0.0.1", "::1"}
_DEFAULT_PORTS = {"https": 443, "http": 80}


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


def _parse_entry(value: object) -> CliLoginEntry | None:
    if not isinstance(value, dict):
        return None
    fields = cast(dict[str, object], value)
    scopes = fields.get("scopes")
    if (
        not all(
            isinstance(fields.get(k), str) and fields[k]
            for k in ("issuer", "resource", "clientId", "accessToken", "refreshToken")
        )
        or _parse_time(fields.get("expiresAt")) is None
        or not isinstance(fields.get("accountId"), str)
        or not isinstance(scopes, list)
        or not all(isinstance(s, str) for s in cast(list[object], scopes))
    ):
        return None
    return cast(CliLoginEntry, fields)


def _read_all() -> dict[str, object]:
    try:
        file: object = json.loads(credentials_path().read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    logins = (
        cast(dict[str, object], file).get("logins") if isinstance(file, dict) else None
    )
    return cast(dict[str, object], logins) if isinstance(logins, dict) else {}


def _write_all(logins: dict[str, object]) -> None:
    """Atomic (temp file + rename), directory 0700, file 0600."""
    path = credentials_path()
    path.parent.mkdir(parents=True, mode=0o700, exist_ok=True)
    os.chmod(path.parent, 0o700)
    temp = path.with_name(f"{path.name}.{os.getpid()}.{uuid.uuid4().hex[:8]}.tmp")
    fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {"version": 1, "logins": logins}, indent=2, ensure_ascii=False
                )
                + "\n"
            )
        os.replace(temp, path)
    except BaseException:
        temp.unlink(missing_ok=True)
        raise


def read_cli_login(base_url: str) -> CliLoginEntry | None:
    return _parse_entry(_read_all().get(normalize_base_url(base_url)))


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
    _write_all({**_read_all(), normalize_base_url(base_url): entry})


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
        entry = read_cli_login(key)
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
