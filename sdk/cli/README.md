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
```

`apostra login` stores one login per API in your OS credential store (Keychain,
Credential Manager or Secret Service), and `@apostra/sdk` in Node.js uses it
when no other credential is set. Without an available credential store, it
falls back to `${XDG_CONFIG_HOME:-~/.config}/apostra/credentials.json`
(`%APPDATA%\apostra` on Windows) with a one-time warning and 0600 permissions.
It needs the server support for the V3 OAuth resource. See the [CLI
guide](https://docs.apostra.com/v3/cli).

API calls and human handoffs will follow their public V3 contracts.
