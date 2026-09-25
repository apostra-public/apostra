---
name: build-with-apostra
description: Use Apostra to plan or run ads, find places to advertise, automate campaign work, read results, or build those jobs into software. Use when a marketer or developer asks for advertising help, an Apostra integration, API or MCP setup, authentication, reporting, or an AdCP sales-agent test.
---

# Build with Apostra

Help the person reach a useful advertising outcome or a working, tested
integration. They may describe the job as running ads, finding publishers,
automating campaign work, or getting results into a report. Do not require them
to know terms such as advertising agent, seller discovery, orchestration, or
MCP.

Apostra provides the account, campaign, seller connection, execution, and
reporting state behind the work. Read the [developer docs](https://docs.interchange.io/v3/overview)
for the product model and the order of operations. Take every call shape from
the connected account's `tools/list` schemas: they are what the server
enforces, and they are specific to the account you are connected to.

## Start in the repository

Inspect the project's instructions, language, package manager, existing MCP
configuration, authentication approach, and test commands. Reuse its conventions.
Identify the requested outcome and choose the smallest working example that
demonstrates it. Do not create a new framework or replace a working integration
merely to match a starter.

Choose how much of the operating loop the developer wants to own:

- **Managed workflow:** work interactively through Apostra and its connected
  assistant; keep campaign and delivery state in Apostra. This does not promise
  a hosted runtime for arbitrary customer code.
- **Composable workflow:** the application owns decisions, scheduling, and
  recovery and calls Apostra for the required operations and data.
- **Hybrid workflow:** application code owns durable checkpoints and approvals;
  an agent handles judgment within those boundaries. Prefer this for a durable
  buyer agent unless the developer has chosen another architecture.

For agent-facing work in Codex or Claude Code, prefer the published native
`apostra-developer` plugin from
`https://github.com/apostra-public/apostra.git`. It installs this skill and the
MCP connection together. Use a direct MCP connection to
`https://api.interchange.io/mcp/v3` when the host does not support the native
plugin, or when instructions were installed separately with `npx skills`.
In either case, let the host complete OAuth and store the interactive
credential.
For deterministic server or ETL work that needs a REST contract or an
operation V3 does not expose, use the documented stable V2 REST API. Explain
that choice in terms of the requested job, not a version-selection exercise.

## Connect and prove access

Read [connection.md](references/connection.md) when installing, authenticating,
or changing account context. Complete read-only verification before any remote
write. For MCP, call `get_status`, inspect the current tools, and read the
intended account resource. For a REST-only integration, use the documented
authorized resource read. Report the observed account and any readiness blocker.

Treat missing authorization as an expected human handoff. If Apostra itself is
not authorized, surface the coding-agent host's OAuth link or login prompt and
wait for the person to complete it. If a requested provider such as Meta is not
connected, follow the applicable workflow to obtain Apostra's one-time browser
authorization URL, give that URL to the person, and wait. Never ask them to
paste an Apostra token, provider token, password, or API key into chat. Verify
the resulting connection with a fresh read before continuing.

A local skill installation is not an MCP connection. OAuth success is not
permission to buy. A passing fixture test is not a successful live API call.
Keep those outcomes separate throughout the work.

Interactive OAuth represents the person using the coding agent. It does not
create a runtime identity for finished software. Reuse an existing Apostra
Agent when the software already has one, create one only when deployed software
needs its own identity and credential, or use the available sandbox while
prototyping safely.

## Prove the contract before writing calls

Read a tool's schema before writing any call to it. The schema carries required
fields, their types, their nesting, and the enum values the account accepts.
Prose gives you sequencing and intent; it cannot give you a field name. Where
the two appear to disagree, the schema is what the request is validated against.

Take field names, nesting, types, and enum values from the schema rather than
from a sample, a similar API, or a field name that reads as obvious. Confirm
response shapes from the tool's output schema, including optional fields,
nullability, and response variants. Read a live object as additional evidence,
not as the contract for code that parses every valid response.

Proving access and proving the contract are different checks, and neither
substitutes for the other. `get_status` proves authentication and reports
account readiness; authority for an operation still requires its scoped
resource and permission check. It says nothing about whether a call's payload
will be accepted. A passing fixture test shows only that the code agrees with
the shapes its author assumed - if those came from prose, the fixtures encode
the same mistake and still pass.

## Build the requested workflow

Read only the reference needed for the task:

- [daily-campaign-review.md](references/daily-campaign-review.md): read-only
  campaign pacing and performance review across the current and prior period.
- [agents.md](references/agents.md): seller discovery, connecting a seller,
  durable buyer-agent loops, and independent agent identity.
- [data-pipelines.md](references/data-pipelines.md): event ingestion handoff,
  aggregate reporting, exports, and scheduled delivery to cloud storage.
- [sales-agent-testing.md](references/sales-agent-testing.md): owned-supply
  discovery and sandbox transaction tests with cleanup.

Before following a workflow that changes account state, retrieve it through
`get({ kind: "skill", id: "build-with-apostra" })` in the active account.
An installed copy does not establish account eligibility. Retrieve a more
specific workflow the same way before executing its mutations.

Use returned identifiers, revisions, continuation cursors, and documented
idempotency semantics. Preserve customer approvals and each tool's confirmation
boundary. A request to build an integration does not authorize launching a
campaign, accepting terms, granting cloud access, or publishing an app.

## Verify and hand off

Run the generated code's deterministic test before calling the local example
working. Exercise meaningful behavior such as account denial, tool errors,
pagination, or restart recovery. Use synthetic fixtures and keep live writes
out of the default test command. If authentication is blocked, continue the
local example and state that live verification remains incomplete.

Report the chosen architecture, files created, test command and observed
result, read-only live result, and the next runnable step. Say which request and
response shapes were taken from the live schemas and which are still assumed;
an assumed shape is an open risk even when every local test passes. Never report OAuth,
account access, ingestion, delivery, or launch from an inferred outcome.
When collecting activation evidence, record bounded outcomes and timestamps;
exclude prompts, source code, credentials, payloads, and signed URLs. Follow
the [skill correlation contract](https://docs.interchange.io/v2/skill#correlate-a-skill-run)
when the host supports it; correlation metadata does not prove completion.
