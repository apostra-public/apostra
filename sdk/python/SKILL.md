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
| Handle a human-handoff URL | `open_handoff` |

Use the generated types and the current documentation to construct requests. Do
not infer fields, permissions, lifecycle transitions, or URL formats from this
map.
