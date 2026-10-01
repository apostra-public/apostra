# Apostra TypeScript SDK

Typed calls to the public V3 HTTP API. Requires Node.js 22.18 or later.

```bash
npm install @apostra/sdk
```

Start with the [SDK quickstart](https://docs.apostra.com/v3/sdk-quickstart).
It covers account discovery, a campaign launch preview and confirmation, and
delivery reporting. The [runnable synthetic-seller
example](https://github.com/apostra-public/apostra/blob/main/sdk/typescript/examples/first-value.ts)
is in the SDK source checkout. It previews by default and only confirms a
launch when `APOSTRA_CONFIRM_LAUNCH=true` is set deliberately.

```ts
import { Apostra } from '@apostra/sdk'
const api = new Apostra()
const status = await api.getStatus()
```

The client reads `APOSTRA_API_KEY`, `APOSTRA_ACCOUNT_ID` and
`APOSTRA_BASE_URL` by default. Explicit constructor options override those
values. Use `accessToken` for an existing REST/M2M bearer token, or
`tokenProvider` for application-managed acquisition and refresh. Supply exactly
one credential source. `m2mTokenProvider` acquires and caches a server-side
client-credentials token with the published M2M endpoint; it refreshes 60
seconds before expiry and shares a concurrent refresh. Never put API keys or
client secrets in browser bundles, URLs, examples or logs. The package does not
persist credentials or replay 401 responses. M2M token refreshes have a
30-second deadline by default; pass `timeoutMs` to override it.

```ts
import { Apostra, m2mTokenProvider } from '@apostra/sdk'

const api = new Apostra({
  tokenProvider: m2mTokenProvider({
    clientId: process.env.APOSTRA_CLIENT_ID!,
    clientSecret: process.env.APOSTRA_CLIENT_SECRET!,
    scope: 'interchange:read',
  }),
})
```

Methods accept the generated wire input and return the envelope's `data`.
Every generated method also has a `WithResponse` variant, such as
`getStatusWithResponse`. It returns `{ data, requestId, headers, status }` for
successful calls, so support tools can retain `x-request-id` and response
headers without dispatching by a wire operation name.
`ApostraError` exposes `status`, `code`, `recovery`, `retryAfter`, `retryable`,
the typed `error`, and `requestId`. Catch `RateLimitError`, `ValidationError`,
or another typed subclass instead of parsing an exception string. The default
exception string excludes response text. Static types do not replace server
validation of patterns, lengths, conditional requirements or permissions.

Read calls accept `{ accountId, signal, timeoutMs }`; write calls require those
options to include a caller-owned `{ idempotencyKey }`. The SDK sends it as
`Idempotency-Key`, and never creates or replaces it. Account selection uses
`X-SCOPE3-CUSTOMER-ID`; it must match the account resolved by the credential.
Cancellation stops waiting for HTTP; it does not undo server work. Requests
have a 30-second timeout, do not follow redirects, and retry transient network,
429 and 5xx failures twice by default with full-jitter backoff. Set
`maxRetries: 0` to opt out. Reads retry automatically. Writes retry only with
the same caller-owned idempotency key, which generated write methods require.
The SDK never creates or replaces that key. Server `retry_after` is a minimum
retry delay.

```ts
const { data, requestId, headers } = await api.getStatusWithResponse()
const correlationId = headers.get('x-request-id')
```

A `202` raises `InFlightReceiptError` rather than returning a completed value.
Use `settle` to replay the same keyed operation until it completes; it honours
the receipt's `Retry-After`, deadline and cancellation signal:

```ts
const key = 'preview-123'
const result = await settle(
  (signal) => api.saveAsk(input, { idempotencyKey: key, signal }),
  { timeoutMs: 30_000 },
)
```

`paginate` and `poll` take typed callbacks. Preserve original query parameters,
revisions and keys; provide the operation's cursor/status accessor. No helper
assumes that a POST is safe to retry without its caller-owned key or that every
list has the same cursor.
Polling passes its signal to `read(signal)`; pagination passes it to
`read(cursor, signal)`. Forward that signal into the SDK call to cancel the
underlying HTTP request. Timeouts cover credentials, HTTP and response-body
consumption; an injected fetch/provider must cooperate with cancellation to
stop its own work. Cancellation still stops the SDK from waiting.

`openHandoff(url, opener?)` accepts an actual HTTPS URL returned by the API.
Without an opener it just returns the URL. Some UI operations currently return
only parameters. URL construction, login, wait/resume, byte uploads and webhook
verification are unsupported unless a future public contract defines them.
`uploadCreativeAsset` exposes the current typed human task and fallback URL.

`@apostra/sdk/metadata` exports generated operation names, paths, security and
parameter descriptions for CLI discovery. The SDK has no terminal, browser,
profile-store or MCP dependencies. Import wire models from `@apostra/sdk/models`.

Source and releases: https://github.com/apostra-public/apostra
