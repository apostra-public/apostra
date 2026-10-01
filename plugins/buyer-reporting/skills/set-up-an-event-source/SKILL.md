---
name: set-up-an-event-source
description: Set up or reuse advertiser conversion tracking when a buyer needs a social-platform source, website or app events, a server feed, CRM data, or a measurement partner.
---

# Set Up an Event Source

Use this workflow when a buyer wants to measure a conversion, attach conversion tracking to a campaign, or connect event data from a social platform or measurement partner.

## Establish the measurement job

1. Identify the advertiser and the conversion outcome the buyer wants to observe. Do not create a source until the advertiser is explicit.
2. Call `search` with `kind: "event_source"` and `filter.advertiserId`. Use the buyer's provider or outcome words as `query` when useful.
3. Reuse a source only when its name, `eventSourceId`, event types, and `actionSource` or `surface` match the buyer's intent. Health is evidence, not an eligibility gate: a new source can be used before any event arrives, but say that no event has arrived yet.

## Choose the source path

### Native social-platform source

Use an ID returned by the connected platform, product, or account flow. Never invent a pixel, form, channel, profile, or dataset ID. If no authorized native source is returned, stop and ask the buyer to connect or select the provider account that owns it.

Do not register a native platform source as if Interchange hosted it. Some products expose a built-in event-source sentinel in their execution template; copy that exact value only when the product declares it.

### Buyer or measurement-partner feed

Call `save_event_source` with the `advertiserId`, a fresh `idempotencyKey`, and one entry in `eventSources` per source. Each entry is keyed by a stable buyer-assigned `eventSourceId`; a new ID creates the source, and an existing ID updates it.

- A new source needs a clear `name` and the exact supported `eventTypes`. Omit `eventTypes` only when the source should accept every event type.
- When the buyer will report monetary values, set `valueCurrencies` to the currencies the sender uses. Without it the source cannot support canonical ROAS.
- Set `actionSource` (or `surface` when a flat category is too coarse) to where the conversion happens.
- The sender owns its field mapping, a stable event ID, and its deduplication rule. Agree those with the buyer before sending production data; V3 does not store them on the source.

Each entry in the response reports its own `action`: `created`, `updated`, `unchanged`, `archived`, or `failed` with `errors`. A failed entry does not undo the others; fix and resend only that entry. Retry an interrupted save with the same `idempotencyKey` and the same entries; a response with `replayed: true` means the earlier save already completed. Use a new key for a different change.

Each saved entry's `setup` object is the installation handoff. Registration saves configuration; it does not install a tag, authorize a provider account, send historical data, or prove that events are flowing.

Billy Grace and other measurement partners follow this server-feed path unless connection discovery explicitly returns a native connector and its authorized source IDs. Do not claim a native connector from the provider name alone.

## Verify before claiming success

1. Read the exact source with `get`, passing `kind: "event_source"`, the source's `eventSourceId` as `id`, and `advertiserId`.
2. Report `health` plainly. `health.status` is the AdCP grade (`insufficient`, `minimum`, `good`, or `excellent`), and `health.issues` names what needs attention:
   - An `error` issue means the latest event was rejected; give the buyer its message.
   - A `warning` that no events have been received means the source is configured but nothing has arrived yet.
   - A `warning` that nothing arrived in 7 days means the source went quiet after receiving events.
3. Do not treat a new source with no events as a failure or wait to create the campaign. Give the buyer the setup instructions and a concrete verification step.

## Attach it to a campaign

When the buyer wants conversion optimization, read the current campaign first. Then call `save_campaign` with the source's exact `eventSourceId` inside the intended event optimization goal.

Never attach a dangling or guessed ID. If the buyer chooses to proceed without conversion tracking, omit the conversion goal and state that the campaign will not optimize against that outcome.

## Safe updates and removal

Change a source by sending its `eventSourceId` with only the changed fields, under a new `idempotencyKey`. Archive with an entry of only `eventSourceId` and `isArchived: true`, and only after confirming the buyer no longer needs the source; archiving makes existing campaign references stop resolving. `isArchived: false` restores it. Do not use archive as a way to rotate credentials or repair a sender's mapping.

## Completion report

State which advertiser owns the source, whether it was reused or created, its `eventSourceId`, current health, required setup action, and whether it was attached to a campaign. Keep native provider authorization, source registration, first-event receipt, and campaign attachment as separate facts.
