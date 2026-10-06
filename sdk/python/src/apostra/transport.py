"""HTTP mechanics only. Credentials, refresh policy and business state stay outside."""

from __future__ import annotations

import asyncio
import builtins
import hashlib
import hmac
import json
import math
import random
import re
from _thread import LockType
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
from importlib.resources import files
from os import environ
from threading import Event, Lock, Thread
from time import monotonic, time
from typing import Generic, Literal, NotRequired, Self, TypeVar, TypedDict, cast
from urllib.parse import quote, urlencode, urlsplit

import httpx

from ._version import BASE_URL, M2M_TOKEN_URL, __version__
from .models import AdcpError, InFlightReceipt, Resume

T = TypeVar("T")
TokenProvider = Callable[[], str]
AsyncTokenProvider = Callable[[], Awaitable[str]]


class WebhookSecret(TypedDict):
    secret: str
    acceptsUntil: NotRequired[int]


class WebhookHeaders(TypedDict):
    signature: list[str]
    timestamp: list[str]
    deliveryId: list[str]


WebhookVerification = dict[str, object]


def verify_webhook(
    *,
    raw_body: bytes | str,
    headers: WebhookHeaders,
    secrets: Mapping[str, str | WebhookSecret],
    now_unix_seconds: int | None = None,
) -> WebhookVerification:
    """Verify one duplicate-preserving V3 webhook before parsing its body."""
    now = int(time()) if now_unix_seconds is None else now_unix_seconds
    if type(now) is not int or now < 0:
        return {"status": "invalid_clock"}
    values = (
        headers.get("signature", []),
        headers.get("timestamp", []),
        headers.get("deliveryId", []),
    )
    if any(len(value) != 1 for value in values):
        return {"status": "malformed"}
    signature, timestamp_header, delivery_id = cast(
        tuple[str, str, str], tuple(value[0] for value in values)
    )
    parsed = re.fullmatch(
        r"v1,kid=([A-Za-z0-9_-]{1,128}),hmac-sha256=([a-f0-9]{64})", signature
    )
    if (
        not parsed
        or not re.fullmatch(r"[1-9][0-9]{9,12}", timestamp_header)
        or not re.fullmatch(r"[!-~]{1,128}", delivery_id)
    ):
        return {"status": "malformed"}
    timestamp = int(timestamp_header)
    configured = secrets.get(parsed.group(1))
    if configured is None:
        return {"status": "unknown_secret"}
    secret = configured if isinstance(configured, str) else configured["secret"]
    accepts_until = (
        None if isinstance(configured, str) else configured.get("acceptsUntil")
    )
    if not secret or (
        accepts_until is not None
        and (type(accepts_until) is not int or now > accepts_until)
    ):
        return {"status": "expired_secret"}
    body = raw_body.encode() if isinstance(raw_body, str) else raw_body
    expected = hmac.new(
        secret.encode(),
        f"v1.{timestamp_header}.{delivery_id}.".encode() + body,
        hashlib.sha256,
    ).hexdigest()
    if not hmac.compare_digest(parsed.group(2), expected):
        return {"status": "invalid_signature"}
    if abs(now - timestamp) > 300:
        return {"status": "stale"}
    return {
        "status": "verified",
        "deliveryId": delivery_id,
        "secretId": parsed.group(1),
        "timestamp": timestamp,
    }
class HumanHandoff(TypedDict):
    """A supported URL returned by a human-action-required operation."""

    kind: Literal['human_action_required']
    url: str
    expiresAt: str
    resume: Resume


def _credential_part(value: str, name: str) -> str:
    if not value or "\r" in value or "\n" in value:
        raise ValueError(f"{name} must be a non-empty single-line string")
    return value


def _m2m_scope(value: str | list[str]) -> str:
    scope = " ".join(value) if isinstance(value, list) else value
    if not scope.strip() or "\r" in scope or "\n" in scope:
        raise ValueError("scope must be a non-empty single-line string")
    return scope


def _m2m_timeout(value: float) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError("timeout must be positive")
    return value


def _m2m_token(response: httpx.Response) -> tuple[str, float]:
    if not response.is_success:
        raise ValueError(f"M2M token request failed ({response.status_code})")
    try:
        payload: object = response.json()
    except ValueError:
        raise ValueError("M2M token response is invalid") from None
    if not isinstance(payload, dict):
        raise ValueError("M2M token response is invalid")
    fields = cast(dict[str, object], payload)
    token = fields.get("access_token")
    expires_in = fields.get("expires_in")
    if (
        not isinstance(token, str)
        or not token
        or "\r" in token
        or "\n" in token
        or not isinstance(expires_in, (int, float))
        or isinstance(expires_in, bool)
        or not math.isfinite(expires_in)
        or expires_in <= 0
    ):
        raise ValueError("M2M token response is invalid")
    return token, max(0, expires_in - 60)


def m2m_token_provider(
    *,
    client_id: str,
    client_secret: str,
    scope: str | list[str],
    http_client: httpx.Client | None = None,
    timeout: float = 30,
) -> TokenProvider:
    """Return a cached client-credentials provider for server-side use only."""
    client_id = _credential_part(client_id, "client_id")
    client_secret = _credential_part(client_secret, "client_secret")
    scope = _m2m_scope(scope)
    timeout = _m2m_timeout(timeout)
    token: str | None = None
    expires_at = 0.0
    lock = Lock()

    def provider() -> str:
        nonlocal token, expires_at
        if token and monotonic() < expires_at:
            return token
        with lock:
            if token and monotonic() < expires_at:
                return token
            client = http_client or httpx.Client()
            try:
                response = client.post(
                    M2M_TOKEN_URL,
                    data={
                        "client_id": client_id,
                        "client_secret": client_secret,
                        "grant_type": "client_credentials",
                        "scope": scope,
                    },
                    headers={"Accept": "application/json"},
                    follow_redirects=False,
                    timeout=timeout,
                )
            except httpx.HTTPError as error:
                raise ConnectionError("Apostra M2M token request failed") from error
            finally:
                if http_client is None:
                    client.close()
            token, ttl = _m2m_token(response)
            expires_at = monotonic() + ttl
            return token

    return provider


def m2m_token_provider_async(
    *,
    client_id: str,
    client_secret: str,
    scope: str | list[str],
    http_client: httpx.AsyncClient | None = None,
    timeout: float = 30,
) -> AsyncTokenProvider:
    """Async counterpart to m2m_token_provider with one in-flight refresh."""
    client_id = _credential_part(client_id, "client_id")
    client_secret = _credential_part(client_secret, "client_secret")
    scope = _m2m_scope(scope)
    timeout = _m2m_timeout(timeout)
    token: str | None = None
    expires_at = 0.0
    lock = asyncio.Lock()

    async def provider() -> str:
        nonlocal token, expires_at
        if token and monotonic() < expires_at:
            return token
        async with lock:
            if token and monotonic() < expires_at:
                return token
            try:
                if http_client is None:
                    async with httpx.AsyncClient() as client:
                        response = await client.post(
                            M2M_TOKEN_URL,
                            data={
                                "client_id": client_id,
                                "client_secret": client_secret,
                                "grant_type": "client_credentials",
                                "scope": scope,
                            },
                            headers={"Accept": "application/json"},
                            follow_redirects=False,
                            timeout=timeout,
                        )
                else:
                    response = await http_client.post(
                        M2M_TOKEN_URL,
                        data={
                            "client_id": client_id,
                            "client_secret": client_secret,
                            "grant_type": "client_credentials",
                            "scope": scope,
                        },
                        headers={"Accept": "application/json"},
                        follow_redirects=False,
                        timeout=timeout,
                    )
            except httpx.HTTPError as error:
                raise ConnectionError("Apostra M2M token request failed") from error
            token, ttl = _m2m_token(response)
            expires_at = monotonic() + ttl
            return token

    return provider


class Parameter(TypedDict):
    name: str
    location: Literal["path", "query"]
    required: bool


class Operation(TypedDict):
    path: str
    method: str
    body: bool
    binary: bool
    idempotencyKey: bool
    bodyKeyField: NotRequired[str]
    parameters: list[Parameter]


class ResponseDetails(TypedDict, Generic[T]):
    """A successful API result together with its transport metadata."""

    data: T
    status: int
    headers: httpx.Headers
    request_id: str | None


OPERATIONS = cast(
    dict[str, Operation],
    json.loads(files("apostra").joinpath("operations.json").read_text()),
)


class ApostraError(Exception):
    def __init__(self, status: int, error: AdcpError, request_id: str | None) -> None:
        self.code = error["code"]
        self.recovery = error.get("recovery", _recovery_for_status(status))
        self.retry_after = error.get("retry_after")
        self.retryable = self.recovery == "transient"
        super().__init__(
            f"Apostra request failed ({status} {self.code}{f', request {request_id}' if request_id else ''})"
        )
        self.status = status
        self.error = error
        self.request_id = request_id


class AuthenticationError(ApostraError):
    pass


class PermissionError(ApostraError):
    pass


class NotFoundError(ApostraError):
    pass


class ConflictError(ApostraError):
    pass


class RateLimitError(ApostraError):
    pass


class ValidationError(ApostraError):
    pass


class UnsupportedCapabilityError(Exception):
    """Deprecated compatibility export; the transport never raises this error."""


class ConnectionError(Exception):
    code = "CONNECTION_ERROR"
    recovery = "transient"
    retry_after: float | None = None
    retryable = True
    request_id: str | None = None


class TimeoutError(builtins.TimeoutError):
    code = "TIMEOUT"
    recovery = "transient"
    retry_after: float | None = None
    retryable = True
    request_id: str | None = None


class ProtocolError(Exception):
    def __init__(self, status: int, request_id: str | None) -> None:
        super().__init__(f"Unexpected Apostra response ({status})")
        self.status = status
        self.request_id = request_id


class InFlightReceiptError(Exception):
    """A 202 receipt proves a write is not yet a completed result."""

    status = 202

    def __init__(
        self,
        request_id: str | None,
        retry_after: float | None,
        receipt: InFlightReceipt,
    ) -> None:
        super().__init__("Apostra write is still in flight")
        self.request_id = request_id
        self.retry_after = retry_after
        self.receipt = receipt


def _account(value: str | None) -> str | None:
    if value is not None and not re.fullmatch(r"[1-9][0-9]*", value):
        raise ValueError("account_id must be a positive integer string")
    return value


def _base_url(value: str) -> str:
    url = urlsplit(value)
    if (
        not url.hostname
        or url.username
        or url.password
        or url.query
        or url.fragment
        or (
            url.scheme != "https"
            and not (
                url.scheme == "http"
                and url.hostname in {"localhost", "127.0.0.1", "::1"}
            )
        )
    ):
        raise ValueError("Use HTTPS (HTTP is allowed only on loopback)")
    return value.rstrip("/")


def _recovery_for_status(
    status: int,
) -> Literal["transient", "correctable", "terminal"]:
    if status in {408, 429} or status >= 500:
        return "transient"
    if status in {400, 401, 403, 404, 409, 422}:
        return "correctable"
    return "terminal"


def _typed_error(status: int, error: AdcpError, request_id: str | None) -> ApostraError:
    error_type: type[ApostraError] = {
        401: AuthenticationError,
        403: PermissionError,
        404: NotFoundError,
        409: ConflictError,
        429: RateLimitError,
        400: ValidationError,
        422: ValidationError,
    }.get(status, ApostraError)
    return error_type(status, error, request_id)


def _max_retries(value: int) -> int:
    if type(value) is not int or value < 0:
        raise ValueError("max_retries must be a non-negative integer")
    return value


def _retryable(error: BaseException) -> bool:
    if isinstance(error, ConnectionError):
        return True
    if isinstance(error, ApostraError):
        return error.status == 429 or error.status >= 500
    return isinstance(error, ProtocolError) and (
        error.status == 429 or error.status >= 500
    )


def _retry_delay(error: BaseException, attempt: int) -> float:
    jitter = random.uniform(0, min(10, 0.25 * 2**attempt))
    retry_after = error.retry_after if isinstance(error, ApostraError) else None
    return max(jitter, retry_after if isinstance(retry_after, (int, float)) else 0)


def _wait(seconds: float, deadline: float, cancel: Event | None = None) -> None:
    remaining = deadline - monotonic()
    if remaining <= 0:
        raise TimeoutError("Apostra request timed out")
    if cancel and cancel.wait(min(seconds, remaining)):
        raise asyncio.CancelledError()
    if cancel is None:
        Event().wait(min(seconds, remaining))
    if seconds > remaining:
        raise TimeoutError("Apostra request timed out")


def _prepare(
    operation: str,
    input: Mapping[str, object],
    token: str,
    account_id: str | None,
    idempotency_key: str | None,
) -> tuple[Operation, str, dict[str, str]]:
    if not token or "\r" in token or "\n" in token:
        raise ValueError("Credential source returned an empty or invalid token")
    meta = OPERATIONS[operation]
    path = meta["path"]
    query: dict[str, str] = {}
    for param in meta["parameters"]:
        value = input.get(param["name"])
        if value is None:
            if param["required"]:
                raise ValueError(f"Missing {param['name']}")
            continue
        if param["location"] == "path":
            path = path.replace("{" + param["name"] + "}", quote(str(value), safe=""))
        else:
            query[param["name"]] = (
                str(value).lower() if isinstance(value, bool) else str(value)
            )
    if query:
        path += "?" + urlencode(query)
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": f"apostra-python/{__version__}",
        "Accept": "text/markdown" if meta["binary"] else "application/json",
    }
    if _account(account_id):
        headers["X-SCOPE3-CUSTOMER-ID"] = cast(str, account_id)
    if meta["idempotencyKey"]:
        if idempotency_key is None or not re.fullmatch(
            r"[\x21-\x7e]{1,255}", idempotency_key
        ):
            raise ValueError("idempotency_key must be a non-empty printable string")
        headers["Idempotency-Key"] = idempotency_key
    return meta, path, headers


def _decode(response: httpx.Response, binary: bool) -> ResponseDetails[object]:
    request_id = response.headers.get("x-request-id")
    if response.status_code == 202:
        try:
            receipt_envelope: object = response.json()
        except ValueError:
            raise ProtocolError(response.status_code, request_id) from None
        if not isinstance(receipt_envelope, dict):
            raise ProtocolError(response.status_code, request_id)
        receipt_data = cast(dict[str, object], receipt_envelope).get("data")
        if (
            not isinstance(receipt_data, dict)
            or cast(dict[str, object], receipt_envelope).get("error") is not None
        ):
            raise ProtocolError(response.status_code, request_id)
        receipt = cast(dict[str, object], receipt_data).get("receipt")
        if not isinstance(receipt, dict):
            raise ProtocolError(response.status_code, request_id)
        receipt_fields = cast(dict[str, object], receipt)
        state_version = receipt_fields.get("stateVersion")
        if (
            not isinstance(receipt_fields.get("id"), str)
            or receipt_fields.get("state") not in {"claimed", "running", "uncertain"}
            or not isinstance(state_version, int)
            or isinstance(state_version, bool)
            or state_version < 1
            or not isinstance(receipt_fields.get("stateChangedAt"), str)
        ):
            raise ProtocolError(response.status_code, request_id)
        retry_after = response.headers.get("retry-after")
        try:
            seconds = float(retry_after) if retry_after is not None else None
        except ValueError:
            seconds = None
        raise InFlightReceiptError(
            request_id,
            seconds if seconds is None or seconds >= 0 else None,
            cast(InFlightReceipt, receipt),
        )
    if response.is_success and binary:
        return {
            "data": response.content,
            "status": response.status_code,
            "headers": response.headers,
            "request_id": request_id,
        }
    try:
        envelope: object = response.json()
    except ValueError:
        raise ProtocolError(response.status_code, request_id) from None
    if not isinstance(envelope, dict):
        raise ProtocolError(response.status_code, request_id)
    data = cast(dict[str, object], envelope)
    if not response.is_success:
        error = data.get("error")
        if "data" in data and data["data"] is None and isinstance(error, dict):
            fields = cast(dict[str, object], error)
            if isinstance(fields.get("code"), str) and isinstance(
                fields.get("message"), str
            ):
                raise _typed_error(
                    response.status_code, cast(AdcpError, fields), request_id
                )
        raise ProtocolError(response.status_code, request_id)
    if data.get("error") is not None or "error" not in data or "data" not in data:
        raise ProtocolError(response.status_code, request_id)
    return {
        "data": data["data"],
        "status": response.status_code,
        "headers": response.headers,
        "request_id": request_id,
    }


def _run_sync_with_deadline(
    task: Callable[[], T], deadline: float, in_flight: LockType
) -> T:
    """Bound a sync request while retaining at most one uninterruptible worker."""
    remaining = deadline - monotonic()
    if remaining <= 0 or not in_flight.acquire(timeout=remaining):
        raise TimeoutError("Apostra request timed out")
    value: list[T] = []
    failure: list[BaseException] = []
    complete = Event()

    def run() -> None:
        try:
            value.append(task())
        except BaseException as error:
            failure.append(error)
        finally:
            complete.set()
            in_flight.release()

    try:
        Thread(target=run, daemon=True).start()
    except BaseException:
        in_flight.release()
        raise
    remaining = deadline - monotonic()
    if remaining <= 0 or not complete.wait(remaining):
        raise TimeoutError("Apostra request timed out")
    if failure:
        raise failure[0]
    return value[0]


class SyncTransport:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        access_token: str | None = None,
        token_provider: TokenProvider | None = None,
        account_id: str | None = None,
        base_url: str | None = None,
        timeout: float = 30,
        max_retries: int = 2,
        http_client: httpx.Client | None = None,
    ) -> None:
        if not any(
            value is not None for value in (api_key, access_token, token_provider)
        ):
            api_key = environ.get("APOSTRA_API_KEY")
        account_id = (
            account_id if account_id is not None else environ.get("APOSTRA_ACCOUNT_ID")
        )
        base_url = (
            base_url
            if base_url is not None
            else environ.get("APOSTRA_BASE_URL", BASE_URL)
        )
        if (
            sum(value is not None for value in (api_key, access_token, token_provider))
            != 1
        ):
            raise ValueError(
                "Supply exactly one of api_key, access_token or token_provider"
            )
        self.__token = api_key or access_token
        self.__provider = token_provider
        self.__provider_lock = Lock()
        self._account_id = _account(account_id)
        self._base_url = _base_url(base_url)
        self._timeout = timeout
        self._max_retries = _max_retries(max_retries)
        self.__owns_client = http_client is None
        self._http = http_client or httpx.Client()

    def _request(
        self,
        operation: str,
        input: Mapping[str, object],
        *,
        account_id: str | None = None,
        timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> object:
        return self._request_with_response(
            operation,
            input,
            account_id=account_id,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )["data"]

    def _request_with_response(
        self,
        operation: str,
        input: Mapping[str, object],
        *,
        account_id: str | None = None,
        timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> ResponseDetails[object]:
        seconds = self._timeout if timeout is None else timeout
        if not math.isfinite(seconds) or seconds <= 0:
            raise ValueError("timeout must be positive")
        target = _account(account_id if account_id is not None else self._account_id)
        deadline = monotonic() + seconds

        def send() -> tuple[httpx.Response, bool]:
            token = self.__provider() if self.__provider else self.__token
            meta, path, headers = _prepare(
                operation, input, token or "", target, idempotency_key
            )
            payload = dict(input)
            body_key_field = meta.get("bodyKeyField")
            if body_key_field:
                supplied = payload.get(body_key_field)
                if supplied is not None and supplied != idempotency_key:
                    raise ValueError(
                        f"{body_key_field} must match idempotency_key for {operation}"
                    )
                payload[body_key_field] = cast(str, idempotency_key)
            remaining = deadline - monotonic()
            if remaining <= 0:
                raise TimeoutError("Apostra request timed out before dispatch")
            try:
                response = self._http.request(
                    meta["method"],
                    self._base_url + path,
                    headers=headers,
                    json=payload if meta["body"] else None,
                    timeout=remaining,
                    follow_redirects=False,
                )
            except httpx.TimeoutException as error:
                raise TimeoutError("Apostra request timed out") from error
            except httpx.HTTPError as error:
                raise ConnectionError("Apostra connection failed") from error
            return response, meta["binary"]

        for attempt in range(self._max_retries + 1):
            try:
                response, binary = _run_sync_with_deadline(
                    send, deadline, self.__provider_lock
                )
                return _decode(response, binary)
            except (ApostraError, ConnectionError, ProtocolError) as error:
                if attempt >= self._max_retries or not _retryable(error):
                    raise
                _wait(_retry_delay(error, attempt), deadline)
        raise AssertionError("retry loop exhausted without a result")

    def close(self) -> None:
        if self.__owns_client:
            self._http.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncTransport:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        access_token: str | None = None,
        token_provider: AsyncTokenProvider | None = None,
        account_id: str | None = None,
        base_url: str | None = None,
        timeout: float = 30,
        max_retries: int = 2,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        if not any(
            value is not None for value in (api_key, access_token, token_provider)
        ):
            api_key = environ.get("APOSTRA_API_KEY")
        account_id = (
            account_id if account_id is not None else environ.get("APOSTRA_ACCOUNT_ID")
        )
        base_url = (
            base_url
            if base_url is not None
            else environ.get("APOSTRA_BASE_URL", BASE_URL)
        )
        if (
            sum(value is not None for value in (api_key, access_token, token_provider))
            != 1
        ):
            raise ValueError(
                "Supply exactly one of api_key, access_token or token_provider"
            )
        self.__token = api_key or access_token
        self.__provider = token_provider
        self._account_id = _account(account_id)
        self._base_url = _base_url(base_url)
        self._timeout = timeout
        self._max_retries = _max_retries(max_retries)
        self.__owns_client = http_client is None
        self._http = http_client or httpx.AsyncClient()

    async def _request(
        self,
        operation: str,
        input: Mapping[str, object],
        *,
        account_id: str | None = None,
        timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> object:
        return (
            await self._request_with_response(
                operation,
                input,
                account_id=account_id,
                timeout=timeout,
                idempotency_key=idempotency_key,
            )
        )["data"]

    async def _request_with_response(
        self,
        operation: str,
        input: Mapping[str, object],
        *,
        account_id: str | None = None,
        timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> ResponseDetails[object]:
        seconds = self._timeout if timeout is None else timeout
        if not math.isfinite(seconds) or seconds <= 0:
            raise ValueError("timeout must be positive")
        target = _account(account_id if account_id is not None else self._account_id)
        try:
            async with asyncio.timeout(seconds):
                for attempt in range(self._max_retries + 1):
                    try:
                        token = (
                            await self.__provider() if self.__provider else self.__token
                        )
                        meta, path, headers = _prepare(
                            operation, input, token or "", target, idempotency_key
                        )
                        payload = dict(input)
                        body_key_field = meta.get("bodyKeyField")
                        if body_key_field:
                            supplied = payload.get(body_key_field)
                            if supplied is not None and supplied != idempotency_key:
                                raise ValueError(
                                    f"{body_key_field} must match idempotency_key for {operation}"
                                )
                            payload[body_key_field] = cast(str, idempotency_key)
                        try:
                            response = await self._http.request(
                                meta["method"],
                                self._base_url + path,
                                headers=headers,
                                json=payload if meta["body"] else None,
                                timeout=seconds,
                                follow_redirects=False,
                            )
                        except httpx.TimeoutException as error:
                            raise TimeoutError("Apostra request timed out") from error
                        except httpx.HTTPError as error:
                            raise ConnectionError(
                                "Apostra connection failed"
                            ) from error
                        return _decode(response, meta["binary"])
                    except (ApostraError, ConnectionError, ProtocolError) as error:
                        if attempt >= self._max_retries or not _retryable(error):
                            raise
                        await asyncio.sleep(_retry_delay(error, attempt))
                raise AssertionError("retry loop exhausted without a result")
        except builtins.TimeoutError as error:
            if isinstance(error, TimeoutError):
                raise
            raise TimeoutError("Apostra request timed out") from error

    async def aclose(self) -> None:
        if self.__owns_client:
            await self._http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.aclose()


def paginate(
    read: Callable[[str | None], T], next_cursor: Callable[[T], str | None]
) -> Iterator[T]:
    cursor = None
    seen: set[str] = set()
    while True:
        page = read(cursor)
        next_value = next_cursor(page)
        if next_value and next_value in seen:
            raise ProtocolError(200, None)
        if not next_value:
            yield page
            return
        seen.add(next_value)
        yield page
        cursor = next_value


async def paginate_async(
    read: Callable[[str | None], Awaitable[T]], next_cursor: Callable[[T], str | None]
) -> AsyncIterator[T]:
    cursor = None
    seen: set[str] = set()
    while True:
        page = await read(cursor)
        next_value = next_cursor(page)
        if next_value and next_value in seen:
            raise ProtocolError(200, None)
        if not next_value:
            yield page
            return
        seen.add(next_value)
        yield page
        cursor = next_value


async def poll(
    read: Callable[[], Awaitable[T]],
    complete: Callable[[T], bool],
    *,
    timeout: float,
    interval: float = 1,
) -> T:
    if (
        not math.isfinite(timeout)
        or not math.isfinite(interval)
        or timeout <= 0
        or interval <= 0
    ):
        raise ValueError("timeout and interval must be positive")
    async with asyncio.timeout(timeout):
        while True:
            result = await read()
            if complete(result):
                return result
            await asyncio.sleep(interval)


def settle(
    run: Callable[[], T], *, timeout: float = 30, cancel: Event | None = None
) -> T:
    """Re-invoke a caller-owned keyed write until an in-flight receipt settles."""
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be positive")
    deadline = monotonic() + timeout
    while True:
        if cancel and cancel.is_set():
            raise asyncio.CancelledError()
        try:
            return run()
        except InFlightReceiptError as error:
            _wait(
                error.retry_after if error.retry_after is not None else 1,
                deadline,
                cancel,
            )


async def settle_async(run: Callable[[], Awaitable[T]], *, timeout: float = 30) -> T:
    """Async counterpart to settle; task cancellation stops its next retry."""
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be positive")
    async with asyncio.timeout(timeout):
        while True:
            try:
                return await run()
            except InFlightReceiptError as error:
                await asyncio.sleep(
                    error.retry_after if error.retry_after is not None else 1
                )


def get_handoff(result: Mapping[str, object] | None) -> HumanHandoff | None:
    """Return a supported human handoff, or None when the result has none."""
    if result is None:
        return None
    handoff = result.get('humanHandoff')
    if not isinstance(handoff, Mapping):
        return None
    fields = cast(Mapping[str, object], handoff)
    if fields.get('kind') != 'human_action_required':
        return None
    url = fields.get('url')
    expires_at = fields.get('expiresAt')
    resume = fields.get('resume')
    if (
        not isinstance(url, str)
        or not isinstance(expires_at, str)
        or not isinstance(resume, Mapping)
    ):
        return None
    resume_fields = cast(Mapping[str, object], resume)
    if (
        resume_fields.get('kind') != 'manual'
        or resume_fields.get('reason')
        != 'This Page has no durable completion receipt. Read the affected object before continuing; opening or closing the browser is not completion.'
    ):
        return None
    return {
        'kind': 'human_action_required',
        'url': url,
        'expiresAt': expires_at,
        'resume': cast(Resume, resume_fields),
    }


def open_handoff(handoff: HumanHandoff | str, opener: Callable[[str], object] | None = None) -> str:
    """Use only a handoff returned by get_handoff; headless calls return its URL."""
    url = handoff if isinstance(handoff, str) else handoff['url']
    parsed = urlsplit(url)
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username
        or parsed.password
    ):
        raise ValueError("Expected an HTTPS handoff URL")
    if opener:
        opener(url)
    return url
