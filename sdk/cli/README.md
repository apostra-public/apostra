# Apostra CLI

The official terminal client for the Apostra V3 API. Requires Node.js 22.18 or
later.

```bash
npx @apostra/cli login            # sign in with your browser
npx @apostra/cli status           # the stored login and its account
npx @apostra/cli token            # print a fresh access token
npx @apostra/cli logout           # revoke and delete the stored login
npx @apostra/cli operations list
npx @apostra/cli operations describe get_delivery --json
npx @apostra/cli call get_status --json
npx @apostra/cli call get_delivery --input @request.json --json
```

`apostra call <operation>` runs any public V3 operation through `@apostra/sdk`.
It names its account on stderr (`--account`, then `APOSTRA_ACCOUNT_ID`, then
your sign-in), takes input from `--input` (inline JSON, `@file.json` or `-` for
stdin) and `--set path=value`, requires `--idempotency-key` for writes, and
pages through reads with `--all`. Every command except `login` accepts `--json`:
stdout is one versioned envelope, `{schemaVersion, ok, data | error}`, and
diagnostics go to stderr. Exit codes: 0 success, 1 server failure, 2 invalid
input, 3 authentication, 4 permission, 5 conflict, 6 unavailable capability.

`apostra login` stores one login per API in your OS credential store (Keychain,
Credential Manager or Secret Service), and `@apostra/sdk` in Node.js uses it
when no other credential is set. Without an available credential store, it
falls back to `${XDG_CONFIG_HOME:-~/.config}/apostra/credentials.json`
(`%APPDATA%\apostra` on Windows) with a one-time warning and 0600 permissions.
It needs the server support for the V3 OAuth resource. See the [CLI
guide](https://docs.apostra.com/v3/cli).

Human handoffs will follow their public V3 contract.
