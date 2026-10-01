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
import os
from apostra import Apostra
api = Apostra(api_key=os.environ['APOSTRA_API_KEY'], account_id='123')
try:
    status = api.get_status({})
finally:
    api.close()
```

Models in `apostra.models` are typed wire dictionaries: keep the contract's
field names, including camelCase keys. Methods use snake_case and return the
envelope's `data`. Both mypy and pyright check inputs, results and recursive
JSON types. Runtime schema constraints remain enforced by the server.

Use `access_token` for an existing REST/M2M bearer token or `token_provider`
for application-managed refresh. The async client requires an async provider.
Supply exactly one source. Never expose keys in browser code, URLs or logs.
Credentials are neither persisted nor included in exception strings.

`ApostraError` exposes `status`, `error` and `request_id`. The `error` dictionary
contains the server code, message and recovery hints. Read calls take
`account_id` and `timeout` overrides; write calls also require a caller-owned
`idempotency_key`, which the SDK sends as `Idempotency-Key` without creating or
replacing it. Account targeting must match the account resolved by
authentication. Default timeout: 30 seconds. Automatic retries: zero. HTTP
redirects are not followed. Retain operation-specific idempotency keys if your
application chooses to retry. `AsyncApostra` supports asyncio task cancellation;
cancelling HTTP does not undo server-side work. Clients close only HTTP clients
they own; callers close injected clients.
Async timeouts include token acquisition and HTTP. A synchronous provider runs
behind the same caller deadline, so a blocked provider raises `TimeoutError`
without sending an HTTP request. Python cannot forcibly interrupt blocked work,
so at most one sync request can remain in flight per client.
An HTTP `202` raises `InFlightReceiptError`, not a completed operation value.
It exposes the request ID and numeric `Retry-After` while the V3 receipt schema
and its read-only endpoint are pending. Keep the original operation key: the
SDK neither replays the write nor makes a new key.

`paginate`, `paginate_async` and `poll` accept typed callbacks, leaving exact
cursor/status rules to the caller. `poll` requires a finite timeout.
Async helper cancellation propagates into the awaited read. A failed read
ends pagination or polling; neither helper retries it.
`open_handoff(url, opener=None)` returns the supplied HTTPS URL in headless
code. An explicit opener can display a URL actually returned by the API.
There is no inferred URL, embedded UI, login, wait/resume, byte-upload helper
or webhook verifier. Those need a public contract. `upload_creative_asset`
returns the current typed human task and fallback URL.

Source and releases: https://github.com/apostra-public/apostra
