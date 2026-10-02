---
name: apostra-sdk
description: Choose the Apostra TypeScript SDK method for a coding task, then read the public documentation for the current contract.
---

# Apostra TypeScript SDK

Read the [SDK guide](https://docs.apostra.com/v2/sdk), [V3 HTTP API
guide](https://docs.apostra.com/v3/http-api), and [authentication
guide](https://docs.apostra.com/v3/authentication) before relying on an
operation. They are the source of truth for inputs, results, permissions, and
behaviour.

## Job-to-method map

| Job | Method |
| --- | --- |
| Check the resolved account | `getStatus` |
| Discover objects or read one object | `search`, `get` |
| Create, update, preview, or confirm a campaign | `saveCampaign` |
| Read delivery | `getDelivery` |
| Inspect a successful call's request ID or headers | `getStatusWithResponse` (and the matching `WithResponse` method) |
| Handle a human handoff and resume safely | `getHandoff`, then `openHandoff` |
| Authenticate a deployed backend with M2M OAuth | `m2mTokenProvider` |

Use the generated types and the current documentation to construct requests. Do
not infer fields, permissions, lifecycle transitions, or URL formats from this
map.
