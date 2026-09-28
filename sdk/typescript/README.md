# Apostra TypeScript SDK

Typed calls to the public V3 HTTP API. Requires Node.js 22.18 or later.

```ts
import { Apostra } from '@apostra/sdk'
const api = new Apostra({ apiKey: process.env.APOSTRA_API_KEY!, accountId: '123' })
const status = await api.getStatus({})
```

Use `accessToken` for an existing REST/M2M bearer token, or `tokenProvider`
for application-managed acquisition and refresh. Supply exactly one credential
source. Never put API keys in browser bundles, URLs, examples or logs. The
package does not acquire tokens, persist credentials or replay 401 responses.

Methods accept the generated wire input and return the envelope's `data`.
`ApostraError` exposes `status`, the typed `error`, and `requestId`. The default
exception string excludes response text. Static types do not replace server
validation of patterns, lengths, conditional requirements or permissions.

Every call accepts `{ accountId, signal, timeoutMs }`. Account selection uses
`X-SCOPE3-CUSTOMER-ID`; it must match the account resolved by the credential.
Cancellation stops waiting for HTTP; it does not undo server work. Requests
have a 30-second timeout and no automatic retries or redirects. Transient
errors expose the server's recovery hint and `retry_after`; the application
decides whether replay is safe with the operation's original idempotency key.
A `202` raises `InFlightReceiptError` rather than returning a completed value.
It carries only the request ID and parsed `Retry-After` while the receipt schema
and read-only receipt endpoint are pending. Keep the original key; the SDK does
not replay the write or mint a replacement key.

`paginate` and `poll` take typed callbacks. Preserve original query parameters,
revisions and keys; provide the operation's cursor/status accessor. No helper
assumes that a POST is safe to retry or that every list has the same cursor.
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
