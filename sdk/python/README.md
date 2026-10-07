# Apostra Python SDK

Typed synchronous and asynchronous calls to the public V3 HTTP API. Python 3.11+.

```bash
python -m pip install apostra
```

Start with the [SDK quickstart](https://docs.apostra.com/v3/sdk-quickstart).
It covers account discovery, a campaign launch preview and confirmation, and
delivery reporting. The [runnable synthetic-seller
example](https://github.com/apostra-public/apostra/blob/main/sdk/python/examples/first_value.py)
is in the SDK source checkout. It previews by default and only confirms a
launch when `APOSTRA_CONFIRM_LAUNCH=true` is set deliberately.

```python
from apostra import Apostra
api = Apostra()
try:
    status = api.get_status()
finally:
    api.close()
```

Models in `apostra.models` are typed wire dictionaries: keep the contract's
field names, including camelCase keys. Methods use snake_case and return the
envelope's `data`. Both mypy and pyright check inputs, results and recursive
JSON types. Runtime schema constraints remain enforced by the server.

Every generated method also has a `_with_response` variant, such as
`get_status_with_response`. It returns a successful response dictionary with
`data`, `request_id`, `headers` and `status`, so support tools can retain
`x-request-id` and response headers without dispatching by a wire
operation name.

The client reads `APOSTRA_API_KEY`, `APOSTRA_ACCOUNT_ID` and
`APOSTRA_BASE_URL` by default. Explicit constructor options override those
values. Use `access_token` for an existing REST/M2M bearer token or
`token_provider` for application-managed refresh. `m2m_token_provider` and
`m2m_token_provider_async` acquire and cache server-side client-credentials
tokens, refresh 60 seconds before expiry, and share a concurrent refresh. The
async client requires the async provider. Supply exactly one source. Never
expose keys or client secrets in browser code, URLs or logs. Credentials are
neither persisted nor included in exception strings. M2M token refreshes have a
30-second deadline by default; pass `timeout` to override it.

```python
import os

from apostra import Apostra, m2m_token_provider

api = Apostra(token_provider=m2m_token_provider(
    client_id=os.environ['APOSTRA_CLIENT_ID'],
    client_secret=os.environ['APOSTRA_CLIENT_SECRET'],
    scope='interchange:read',
))
```

`ApostraError` exposes `status`, `code`, `recovery`, `retry_after`, `retryable`,
`error` and `request_id`. Catch `RateLimitError`, `ValidationError`, or another
typed exception instead of parsing exception text. Read calls take
`account_id` and `timeout` overrides; write calls also require a caller-owned
`idempotency_key`, which the SDK sends as `Idempotency-Key` without creating or
replacing it. Account targeting must match the account resolved by
authentication. Default timeout: 30 seconds. Transient network, 429 and 5xx
failures retry twice by default with full-jitter backoff; set `max_retries=0`
to opt out. Reads retry automatically. Writes reuse only their caller-owned
idempotency key, and the server's `retry_after` is a minimum delay. HTTP
redirects are not followed. `AsyncApostra` supports asyncio task cancellation;
cancelling HTTP does not undo server-side work. Clients close only HTTP clients
they own; callers close injected clients.
Async timeouts include token acquisition and HTTP. A synchronous provider runs
behind the same caller deadline, so a blocked provider raises `TimeoutError`
without sending an HTTP request. Python cannot forcibly interrupt blocked work,
so at most one sync request can remain in flight per client.
An HTTP `202` raises `InFlightReceiptError`, not a completed operation value.
It exposes the request ID and numeric `Retry-After` while the V3 receipt schema
and its read-only endpoint are pending. Keep the original operation key. Use
`settle` (or `settle_async`) to replay that exact operation until it completes:

```python
from apostra import settle

key = 'preview-123'
result = settle(
    lambda: api.save_ask(input, idempotency_key=key),
    timeout=30,
)
```

```python
response = api.get_status_with_response()
data = response['data']
request_id = response['request_id']
correlation_id = response['headers']['x-request-id']
```

`paginate`, `paginate_async` and `poll` accept typed callbacks, leaving exact
cursor/status rules to the caller. `poll` requires a finite timeout.
Async helper cancellation propagates into the awaited read. A failed read
ends pagination or polling; neither helper retries it.
`verify_webhook` validates duplicate-preserving V3 webhook headers, the raw
body, the five-minute delivery window, and a rotating key map before you parse
JSON. Provide every raw occurrence of `signature`, `timestamp`, and
`deliveryId`; do not flatten duplicate headers or log secrets.

`open_handoff(url, opener=None)` returns the supplied HTTPS URL in headless
code. An explicit opener can display a URL actually returned by the API.
There is no inferred URL, embedded UI, login, wait/resume, or byte-upload helper.
Those need a public contract. `upload_creative_asset`
returns the current typed human task and fallback URL.
`get_handoff(result)` returns a supported human action with its `kind`, `url`,
`expiresAt` and `resume` instructions, or `None`. Pass it to
`open_handoff(handoff, opener=None)` to return the supplied HTTPS URL in
headless code or display it with an explicit opener. Opening or closing the
browser is not completion: follow `resume` and read the affected object before
continuing. The SDK never infers a URL or embeds a login flow.

Source and releases: https://github.com/apostra-public/apostra
