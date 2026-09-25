# Apostra TypeScript starter

This Node.js 20.18.1+ starter connects to Apostra's v3 MCP endpoint with a scoped
access token and makes one read-only `get_status` call. The 15-second deadline
covers connection, verification, and session teardown. The starter closes its
HTTP connections before returning. On timeout, check network access and the MCP
endpoint, then retry. For browser OAuth, use the
[direct MCP quickstart](https://docs.interchange.io/v3/quickstart).

```sh
npm install
APOSTRA_ACCESS_TOKEN='your-scoped-token' npm start
npm test
```

Keep the token in an environment variable or secret manager. Do not commit it.

## Generate types from the live schemas

```sh
APOSTRA_ACCESS_TOKEN='your-scoped-token' npm run types:generate
```

This writes `src/generated/tools.ts` — one input type per tool, built from the
schemas the server publishes. Import those types instead of hand-writing the
request shapes:

```ts
import type { SaveCampaignInput } from "./generated/tools.js";

const input = {
  // ...
} satisfies SaveCampaignInput;
```

The schemas are what every request is validated against. Generating from them
lets `tsc` surface incompatible type or enum changes and newly required fields
before a live call. Regenerate after the tool surface changes and review the
generated diff as well as the compiler output. An open schema must accept
unknown extension keys. Generated types do not detect a removed or renamed
optional field on such a schema because the old name remains assignable as an
extension key.

Generated types are static projections, not runtime validators. Closed named
objects omit an index signature, so `satisfies` and direct annotations reject
extra keys in object literals. TypeScript's structural assignment can still
carry extra keys from an existing variable, and constraints such as string
patterns, lengths, numeric ranges, property-name rules, and `oneOf` exclusivity
remain server-validated.

The generated file repeats that warning. Runtime-only rules can also include
dependencies, conditionals, exclusions, and tuple bounds. Supported structural
combinations are retained: `$ref`, `const`, enum, union, and `allOf` siblings
generate as intersections. Mixed named and typed dictionaries keep their named
fields and leave extension-value validation to the server because TypeScript
cannot represent the two key spaces separately.

Named objects that leave `additionalProperties` open keep an unknown-valued
index signature, so valid server-defined extension fields remain assignable.

Field names are easy to guess wrong and prose cannot correct you: a campaign's
flight is `startAt`/`endAt`, its budget is `total`, and its revision is a
number. Read the schema — or generate from it — before writing the call.

After verification works, follow the
[build-an-agent guide](https://docs.interchange.io/v3/build-an-agent) to add
durable checkpoints, confirmation gates, and retries.
