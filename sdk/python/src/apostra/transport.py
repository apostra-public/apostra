"""HTTP mechanics only. Credentials, refresh policy and business state stay outside."""
from __future__ import annotations

import asyncio
import builtins
import json
import math
import re
from _thread import LockType
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
from importlib.resources import files
from os import environ
from threading import Event, Lock, Thread
from time import monotonic
from typing import Literal, NotRequired, Self, TypeVar, TypedDict, cast
from urllib.parse import quote, urlencode, urlsplit

import httpx

from ._version import BASE_URL, __version__
from .models import AdcpError, InFlightReceipt

T = TypeVar('T')
TokenProvider = Callable[[], str]
AsyncTokenProvider = Callable[[], Awaitable[str]]


class Parameter(TypedDict):
    name: str
    location: Literal['path', 'query']
    required: bool


class Operation(TypedDict):
    path: str
    method: str
    body: bool
    binary: bool
    idempotencyKey: bool
    bodyKeyField: NotRequired[str]
    parameters: list[Parameter]


OPERATIONS = cast(dict[str, Operation], json.loads(files('apostra').joinpath('operations.json').read_text()))


class ApostraError(Exception):
    def __init__(self, status: int, error: AdcpError, request_id: str | None) -> None:
        self.code = error['code']
        self.recovery = error.get('recovery', _recovery_for_status(status))
        self.retry_after = error.get('retry_after')
        self.retryable = self.recovery == 'transient'
        super().__init__(f"Apostra request failed ({status} {self.code}{f', request {request_id}' if request_id else ''})")
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
    code = 'CONNECTION_ERROR'
    recovery = 'transient'
    retry_after: float | None = None
    retryable = True
    request_id: str | None = None


class TimeoutError(builtins.TimeoutError):
    code = 'TIMEOUT'
    recovery = 'transient'
    retry_after: float | None = None
    retryable = True
    request_id: str | None = None


class ProtocolError(Exception):
    def __init__(self, status: int, request_id: str | None) -> None:
        super().__init__(f'Unexpected Apostra response ({status})')
        self.status = status
        self.request_id = request_id


class InFlightReceiptError(Exception):
    """A 202 receipt proves a write is not yet a completed result."""

    status = 202

    def __init__(self, request_id: str | None, retry_after: float | None, receipt: InFlightReceipt) -> None:
        super().__init__('Apostra write is still in flight')
        self.request_id = request_id
        self.retry_after = retry_after
        self.receipt = receipt


def _account(value: str | None) -> str | None:
    if value is not None and not re.fullmatch(r'[1-9][0-9]*', value):
        raise ValueError('account_id must be a positive integer string')
    return value


def _base_url(value: str) -> str:
    url = urlsplit(value)
    if not url.hostname or url.username or url.password or url.query or url.fragment or (
        url.scheme != 'https' and not (url.scheme == 'http' and url.hostname in {'localhost', '127.0.0.1', '::1'})
    ):
        raise ValueError('Use HTTPS (HTTP is allowed only on loopback)')
    return value.rstrip('/')


def _recovery_for_status(status: int) -> Literal['transient', 'correctable', 'terminal']:
    if status in {408, 429} or status >= 500:
        return 'transient'
    if status in {400, 401, 403, 404, 409, 422}:
        return 'correctable'
    return 'terminal'


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


def _prepare(operation: str, input: Mapping[str, object], token: str, account_id: str | None, idempotency_key: str | None) -> tuple[Operation, str, dict[str, str]]:
    if not token or '\r' in token or '\n' in token:
        raise ValueError('Credential source returned an empty or invalid token')
    meta = OPERATIONS[operation]
    path = meta['path']
    query: dict[str, str] = {}
    for param in meta['parameters']:
        value = input.get(param['name'])
        if value is None:
            if param['required']:
                raise ValueError(f"Missing {param['name']}")
            continue
        if param['location'] == 'path':
            path = path.replace('{' + param['name'] + '}', quote(str(value), safe=''))
        else:
            query[param['name']] = str(value).lower() if isinstance(value, bool) else str(value)
    if query:
        path += '?' + urlencode(query)
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': f'apostra-python/{__version__}', 'Accept': 'text/markdown' if meta['binary'] else 'application/json'}
    if _account(account_id):
        headers['X-SCOPE3-CUSTOMER-ID'] = cast(str, account_id)
    if meta['idempotencyKey']:
        if idempotency_key is None or not re.fullmatch(r'[\x21-\x7e]{1,255}', idempotency_key):
            raise ValueError('idempotency_key must be a non-empty printable string')
        headers['Idempotency-Key'] = idempotency_key
    return meta, path, headers


def _decode(response: httpx.Response, binary: bool) -> object:
    request_id = response.headers.get('x-request-id')
    if response.status_code == 202:
        try:
            receipt_envelope: object = response.json()
        except ValueError:
            raise ProtocolError(response.status_code, request_id) from None
        if not isinstance(receipt_envelope, dict):
            raise ProtocolError(response.status_code, request_id)
        receipt_data = cast(dict[str, object], receipt_envelope).get('data')
        if not isinstance(receipt_data, dict) or cast(dict[str, object], receipt_envelope).get('error') is not None:
            raise ProtocolError(response.status_code, request_id)
        receipt = cast(dict[str, object], receipt_data).get('receipt')
        if not isinstance(receipt, dict):
            raise ProtocolError(response.status_code, request_id)
        receipt_fields = cast(dict[str, object], receipt)
        state_version = receipt_fields.get('stateVersion')
        if (
            not isinstance(receipt_fields.get('id'), str)
            or receipt_fields.get('state') not in {'claimed', 'running', 'uncertain'}
            or not isinstance(state_version, int)
            or isinstance(state_version, bool)
            or state_version < 1
            or not isinstance(receipt_fields.get('stateChangedAt'), str)
        ):
            raise ProtocolError(response.status_code, request_id)
        retry_after = response.headers.get('retry-after')
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
        return response.content
    try:
        envelope: object = response.json()
    except ValueError:
        raise ProtocolError(response.status_code, request_id) from None
    if not isinstance(envelope, dict):
        raise ProtocolError(response.status_code, request_id)
    data = cast(dict[str, object], envelope)
    if not response.is_success:
        error = data.get('error')
        if 'data' in data and data['data'] is None and isinstance(error, dict):
            fields = cast(dict[str, object], error)
            if isinstance(fields.get('code'), str) and isinstance(fields.get('message'), str):
                raise _typed_error(response.status_code, cast(AdcpError, fields), request_id)
        raise ProtocolError(response.status_code, request_id)
    if data.get('error') is not None or 'error' not in data or 'data' not in data:
        raise ProtocolError(response.status_code, request_id)
    return data['data']


def _run_sync_with_deadline(
    task: Callable[[], T], deadline: float, in_flight: LockType
) -> T:
    """Bound a sync request while retaining at most one uninterruptible worker."""
    remaining = deadline - monotonic()
    if remaining <= 0 or not in_flight.acquire(timeout=remaining):
        raise TimeoutError('Apostra request timed out')
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
        raise TimeoutError('Apostra request timed out')
    if failure:
        raise failure[0]
    return value[0]


class SyncTransport:
    def __init__(self, *, api_key: str | None = None, access_token: str | None = None, token_provider: TokenProvider | None = None, account_id: str | None = None, base_url: str | None = None, timeout: float = 30, http_client: httpx.Client | None = None) -> None:
        if not any(value is not None for value in (api_key, access_token, token_provider)):
            api_key = environ.get('APOSTRA_API_KEY')
        account_id = account_id if account_id is not None else environ.get('APOSTRA_ACCOUNT_ID')
        base_url = base_url if base_url is not None else environ.get('APOSTRA_BASE_URL', BASE_URL)
        if sum(value is not None for value in (api_key, access_token, token_provider)) != 1:
            raise ValueError('Supply exactly one of api_key, access_token or token_provider')
        self.__token = api_key or access_token
        self.__provider = token_provider
        self.__provider_lock = Lock()
        self._account_id = _account(account_id)
        self._base_url = _base_url(base_url)
        self._timeout = timeout
        self.__owns_client = http_client is None
        self._http = http_client or httpx.Client()

    def _request(self, operation: str, input: Mapping[str, object], *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str | None = None) -> object:
        seconds = self._timeout if timeout is None else timeout
        if not math.isfinite(seconds) or seconds <= 0:
            raise ValueError('timeout must be positive')
        target = _account(account_id if account_id is not None else self._account_id)
        deadline = monotonic() + seconds

        def send() -> tuple[httpx.Response, bool]:
            token = self.__provider() if self.__provider else self.__token
            meta, path, headers = _prepare(operation, input, token or '', target, idempotency_key)
            payload = dict(input)
            body_key_field = meta.get('bodyKeyField')
            if body_key_field:
                supplied = payload.get(body_key_field)
                if supplied is not None and supplied != idempotency_key:
                    raise ValueError(f'{body_key_field} must match idempotency_key for {operation}')
                payload[body_key_field] = cast(str, idempotency_key)
            remaining = deadline - monotonic()
            if remaining <= 0:
                raise TimeoutError('Apostra request timed out before dispatch')
            try:
                response = self._http.request(meta['method'], self._base_url + path, headers=headers, json=payload if meta['body'] else None, timeout=remaining, follow_redirects=False)
            except httpx.TimeoutException as error:
                raise TimeoutError('Apostra request timed out') from error
            except httpx.HTTPError as error:
                raise ConnectionError('Apostra connection failed') from error
            return response, meta['binary']

        response, binary = _run_sync_with_deadline(send, deadline, self.__provider_lock)
        return _decode(response, binary)

    def close(self) -> None:
        if self.__owns_client:
            self._http.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncTransport:
    def __init__(self, *, api_key: str | None = None, access_token: str | None = None, token_provider: AsyncTokenProvider | None = None, account_id: str | None = None, base_url: str | None = None, timeout: float = 30, http_client: httpx.AsyncClient | None = None) -> None:
        if not any(value is not None for value in (api_key, access_token, token_provider)):
            api_key = environ.get('APOSTRA_API_KEY')
        account_id = account_id if account_id is not None else environ.get('APOSTRA_ACCOUNT_ID')
        base_url = base_url if base_url is not None else environ.get('APOSTRA_BASE_URL', BASE_URL)
        if sum(value is not None for value in (api_key, access_token, token_provider)) != 1:
            raise ValueError('Supply exactly one of api_key, access_token or token_provider')
        self.__token = api_key or access_token
        self.__provider = token_provider
        self._account_id = _account(account_id)
        self._base_url = _base_url(base_url)
        self._timeout = timeout
        self.__owns_client = http_client is None
        self._http = http_client or httpx.AsyncClient()

    async def _request(self, operation: str, input: Mapping[str, object], *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str | None = None) -> object:
        seconds = self._timeout if timeout is None else timeout
        if not math.isfinite(seconds) or seconds <= 0:
            raise ValueError('timeout must be positive')
        target = _account(account_id if account_id is not None else self._account_id)
        try:
            async with asyncio.timeout(seconds):
                token = await self.__provider() if self.__provider else self.__token
                meta, path, headers = _prepare(operation, input, token or '', target, idempotency_key)
                payload = dict(input)
                body_key_field = meta.get('bodyKeyField')
                if body_key_field:
                    supplied = payload.get(body_key_field)
                    if supplied is not None and supplied != idempotency_key:
                        raise ValueError(f'{body_key_field} must match idempotency_key for {operation}')
                    payload[body_key_field] = cast(str, idempotency_key)
                try:
                    response = await self._http.request(meta['method'], self._base_url + path, headers=headers, json=payload if meta['body'] else None, timeout=seconds, follow_redirects=False)
                except httpx.TimeoutException as error:
                    raise TimeoutError('Apostra request timed out') from error
                except httpx.HTTPError as error:
                    raise ConnectionError('Apostra connection failed') from error
                return _decode(response, meta['binary'])
        except builtins.TimeoutError as error:
            if isinstance(error, TimeoutError):
                raise
            raise TimeoutError('Apostra request timed out') from error

    async def aclose(self) -> None:
        if self.__owns_client:
            await self._http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.aclose()


def paginate(read: Callable[[str | None], T], next_cursor: Callable[[T], str | None]) -> Iterator[T]:
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


async def paginate_async(read: Callable[[str | None], Awaitable[T]], next_cursor: Callable[[T], str | None]) -> AsyncIterator[T]:
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


async def poll(read: Callable[[], Awaitable[T]], complete: Callable[[T], bool], *, timeout: float, interval: float = 1) -> T:
    if not math.isfinite(timeout) or not math.isfinite(interval) or timeout <= 0 or interval <= 0:
        raise ValueError('timeout and interval must be positive')
    async with asyncio.timeout(timeout):
        while True:
            result = await read()
            if complete(result):
                return result
            await asyncio.sleep(interval)


def open_handoff(url: str, opener: Callable[[str], object] | None = None) -> str:
    """Use only a URL returned by the operation. Headless calls just return it."""
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('Expected an HTTPS handoff URL')
    if opener:
        opener(url)
    return url
