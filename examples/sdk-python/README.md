# Readiness, inventory discovery and campaign delivery

After the paired SDK release, install `requirements.txt` in a virtual
environment. Set `APOSTRA_API_KEY`, `APOSTRA_ACCOUNT_ID`,
`APOSTRA_CAMPAIGN_ID`, `APOSTRA_START_DATE` and `APOSTRA_END_DATE`, then run
`python journeys.py`. `APOSTRA_BASE_URL` optionally selects a test deployment.
The example uses `AsyncApostra` and `paginate_async` with a 30-second deadline
covering both journeys. Cancelling the task cancels its awaited HTTP request.

Use the same provisioned synthetic buyer, known campaign and expected date
range as the TypeScript example. These read-only examples do not print keys or
account data. The fixture owner must assert expected non-zero recent delivery;
a successful empty report does not establish that the synthetic seller works.

Repository install smoke also runs this exact example against a local HTTP
fixture from both the wheel and source distribution. That checks package
installation, account targeting and cursor handling; it does not replace a
live synthetic-seller run.
