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
reporting state behind the work. The first-party [developer docs](https://docs.interchange.io/v3/overview)
are the canonical product reference. Use the connected account's `tools/list`
schemas for its current capabilities and exact call shapes.

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

Read the [connection guide](references/connection.md) when installing, authenticating,
or changing account context. Complete read-only verification before any remote
write. For MCP, call `get_status`, inspect the current tools, and read the
intended account resource. For a REST-only integration, use the documented
authorized resource read. Report the observed account and any readiness blocker.

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
Prose gives sequencing and intent; it does not define a request shape. Take
field names, nesting, types, enum values, output optionality, nullability, and
response variants from the live schemas rather than from a sample or a similar
API.

Proving access and proving the contract are separate checks. `get_status`
proves authentication and reports readiness; authority still depends on the
scoped resource and permission check. A passing fixture test proves only the
shapes encoded in that fixture, so derive fixtures from schemas where the
project can.

## Build the requested workflow

Read only the reference needed for the task:

- [Agent workflows](references/agents.md): seller discovery, connecting a seller,
  durable buyer-agent loops, and independent agent identity.
- [Data pipelines](references/data-pipelines.md): event ingestion handoff,
  aggregate reporting, exports, and scheduled delivery to cloud storage.
- [Sales-agent testing](references/sales-agent-testing.md): owned-supply
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
response shapes came from live schemas and which remain assumptions. Never report OAuth,
account access, ingestion, delivery, or launch from an inferred outcome.
When collecting activation evidence, record bounded outcomes and timestamps;
exclude prompts, source code, credentials, payloads, and signed URLs. The
first-party [skill correlation contract](https://docs.interchange.io/v2/skill#correlate-a-skill-run)
defines supported correlation metadata; that metadata does not prove
completion.
