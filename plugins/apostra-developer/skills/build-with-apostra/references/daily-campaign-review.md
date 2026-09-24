# Review campaign performance each morning

Read the public [daily campaign review](https://docs.interchange.io/v3/daily-campaign-review)
and the current `search`, `get`, and `get_delivery` schemas before making calls.
The reporting review is read-only. Authorization setup is a separate,
human-gated step that may establish a provider connection only after the person
completes the browser flow. Apostra owns campaign identity, budget, and flight
state. Campaign delivery is read live through each campaign's connected
provider. The coding-agent host may decide when to run the review.

## Complete human authorization

Call `get_status` first. If the Apostra MCP connection is not authorized, give
the person the host's OAuth link or login prompt and stop until they complete
it. Do not ask them to paste an access token into chat.

When the person names a reporting provider such as Meta, use `search` with
`kind: "seller"` to resolve its exact seller ID, then call
`get({ kind: "seller", id: "<sellerId>" })`. The exact read returns the
connection, credential, selected provider account, mapping, and directed
campaign subscription state. A provider in `get_status` destinations means the
account can use that provider; it does not prove that a customer connection is
authorized. If the exact seller read shows that provider authorization is
missing:

- In a host that renders Apostra's MCP app, call `open_connections_page` with
  the resolved `sellerId` and `connectionAction: "connect"`. The person
  confirms and completes authorization in the browser flow.
- In a command-line or other headless host, call `save_connection` with the
  resolved `sellerId` and `authorization: {}`. Relay the returned
  `authorization.url` to the person and stop. Never ask for the underlying
  provider credential.

After the person says authorization is complete, re-read the connection rather
than trusting the browser redirect. An active connection and credential mean
the agent must not request authorization again. If the connection needs an
account selection or advertiser mapping, state the observed fields and the
exact next action.
Keep the review blocked until a person completes or explicitly approves any
state change. Do not describe an authorization URL as a successful connection,
and do not describe a successful connection as readable delivery until the live
provider read succeeds. Enhanced Reporting is not required for this workflow.

## Establish the review

1. Confirm that `get_status` now returns a Buyer Account. Resolve the advertiser
   when more than one is in scope instead of mixing unrelated portfolios.
2. Use the exact seller read, not the search result, to decide whether the
   connected account has a directed campaign subscription. Search campaigns
   before calling `get_delivery`. Select the active,
   non-archived set using only filters that the current schema accepts, then
   read their media buys. For a provider-specific review, establish the exact
   seller-backed campaign set from returned IDs. Do not pull all delivery and
   guess provider membership from a missing result. If the connection is ready
   but its campaign roster has not been subscribed into Apostra, explain that
   distinction and ask the person before calling
   `save_directed_campaign_subscription`. Do not turn the read-only review into
   a subscription change without that approval.
3. By default, use the previous UTC day as the end of the current seven-day
   window. The comparison window is the seven days immediately before it.
   State both exact windows.
4. For each campaign, call `get_delivery` twice with
   `report: "live_campaign_delivery"` and `filters.campaignId`: once for the current
   window and once for the comparison window. Do not pass metrics, dimensions,
   other filters, a cursor, or a page size. This mode preserves the validated
   provider response and never reads Apostra's reporting store.

Do not persist an extract, create an export, or introduce another reporting
store for an interactive review. A separately requested production routine
may retain its own checkpoints, but it still re-reads Apostra before making a
recommendation.

## Calculate observed facts

Keep calculation deterministic. Read each window's additive totals, such as
impressions, clicks, spend, conversions, and conversion value, then derive CTR,
CPC, CPA, and ROAS from those totals. Do not average rates returned at a finer
level. Keep monetary comparisons inside one currency and preserve unavailable
metrics or provider warnings. Missing data is unknown, not zero. A response
with no delivery totals means "no delivery data returned", not zero
performance. A live provider response does not establish reporting-pipeline
finality.

For pacing, read budget, flight, and pacing from the campaign or media buy and
read lifetime spend when the decision needs it. Compare lifetime spend with a
linear elapsed-flight expectation only when the returned pacing is explicitly
even and the flight has bounded dates. With any other pacing plan, report
budget utilization without inventing an expected curve.

## Make bounded recommendations

Use one action per reviewed item: `keep`, `watch`, `investigate`, `increase`,
`reduce`, or `pause`. Attach the current-period facts, prior-period facts,
comparison, data quality, and reason that support it.

Use the person's numeric target, campaign policy, minimum evidence, and maximum
allowed movement when those are available. An exact budget amount requires a
current budget, one currency, comparable periods, sufficient observed volume,
and an explicit reallocation limit. Without those inputs, describe the trend
and recommend `watch` or `investigate`; do not invent a target, causal story,
or dollar amount. A recommendation never authorizes a write.

Present:

1. The account, scope, extraction time, and two exact comparison windows.
2. What needs attention, ordered by materiality and confidence.
3. An action list with target IDs, action, exact evidence, recommendation,
   and the human step needed next.
4. Missing data, mixed currencies, unavailable metrics, and
   anything that prevented a stronger recommendation.

If the person later asks Apostra to apply a recommendation, stop the read-only
review, retrieve the current account's campaign-management workflow, re-read
the exact target and revision, and follow its confirmation boundary.
