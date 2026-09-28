# Readiness, inventory discovery and campaign delivery

After the paired SDK release, run `npm install` and `npm run type-check`.
Set `APOSTRA_API_KEY`, `APOSTRA_ACCOUNT_ID`, `APOSTRA_CAMPAIGN_ID`,
`APOSTRA_START_DATE` and `APOSTRA_END_DATE`, then run `npm start`.
`APOSTRA_BASE_URL` optionally selects a test deployment.
One 30-second cancellation signal covers both journeys, including pagination.

Use a provisioned synthetic buyer account and its known campaign. The date
range must contain the fixture's expected delivery. These examples make only
reads, require no LLM or MCP, and do not print credentials or account data.
A successful empty report does not establish that the synthetic seller works.

Repository install smoke also runs this exact example against a local HTTP
fixture using the npm tarball. That checks package installation, account
targeting and cursor handling; it does not replace a live synthetic-seller run.
