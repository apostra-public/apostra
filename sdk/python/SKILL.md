---
name: apostra-sdk
description: Choose the Apostra Python SDK method for a coding task, then read the public documentation for the current contract.
---

# Apostra Python SDK

Read the [SDK guide](https://docs.apostra.com/v2/sdk), [V3 HTTP API
guide](https://docs.apostra.com/v3/http-api), and [authentication
guide](https://docs.apostra.com/v3/authentication) before relying on an
operation. They are the source of truth for inputs, results, permissions, and
behaviour.

## Job-to-method map

| Job | Method |
| --- | --- |
| Check the resolved account | `get_status` |
| Discover objects or read one object | `search`, `get` |
| Create, update, preview, or confirm a campaign | `save_campaign` |
| Read delivery | `get_delivery` |
| Inspect a successful call's request ID or headers | `get_status_with_response` (and the matching `_with_response` method) |
| Handle a human handoff and resume safely | `get_handoff`, then `open_handoff` |
| Authenticate a deployed backend with M2M OAuth | `m2m_token_provider` or `m2m_token_provider_async` |
| Verify an inbound V3 webhook | `verify_webhook` |

Use the generated types and the current documentation to construct requests. Do
not infer fields, permissions, lifecycle transitions, or URL formats from this
map.
