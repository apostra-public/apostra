---
name: get-account-ready-to-buy
description: Prepare an Interchange buyer account to transact. Use when a user asks to set up, onboard, activate or unblock the buyer account, connect a provider account, accept terms, establish billing authority, or find what must be completed before buying media.
---

# Get an Account Ready to Buy

Use the attached Interchange V3 buyer tools. Treat `get_status` as the authority on the active account, readiness, blockers, and next actions.

## Workflow

1. Call `get_status` before changing anything.
2. Confirm the active account is the buyer account the user intends to configure. If it is not, present reachable accounts and use `switch_account` only when that tool is available and the user selects an account.
3. Work through the returned blockers and `nextActions` in priority order. Do not invent missing requirements or treat a readable public seller page as authorization.
4. For an operator-identity action:
   - Read `operatorIdentity` from `get_status` first.
   - If `locked` is true or `canManage` is false, stop and follow the returned administrator or support action.
   - If `usableForBuying` is true, reuse its returned domain; otherwise ask for the buyer's real business domain.
   - Never invent a domain, unit identifier, or the value `default`.
   - Call `save_buyer_operator` only after the user confirms the exact identity.
   - Buyer readiness treats this check as complete when the account has a usable operator domain and the organization has proved control of it. It does not require a separate identity-scope confirmation.
5. For terms or billing actions:
   - If Terms or full plan review is required, open or direct the user to the Plan & Billing Page and stop that step. The model-visible tools do not expose the complete Terms text and exact version needed for safe acceptance.
   - For payment terms, call `save_billing` with `{ paymentTerms }` only after the user chooses the terms.
   - For payment authority, ask for confirmation before requesting it. Then follow this flow exactly: `request_payment_authority` returns a single-use confirmation token, `confirm_payment_authority` spends that token to issue the hosted card-capture link, and `get({ kind: 'billing' })` reports the status afterwards.
   - Give the hosted link only to the organization cardholder. Never request or transmit card data in chat or MCP calls.
6. For seller connections:
   - Use `search` and `get` to find the exact seller, connection, provider account, and advertiser mapping.
   - Use `open_media_partners_page` when the host supports its UI; otherwise use `save_connection`.
   - Send authorization through the returned browser URL. Never ask for provider credentials in chat.
   - Use one `save_connection` intent per call. Authorize only when the current connection state requires it, poll with `search` or `get`, then make separate confirmed calls to select a returned provider account and map it to the exact advertiser when required. Re-read after each step.
7. Call `get_status` again. Report what is complete, what still requires the user or an administrator, and whether the account is ready to transact.

If the user asks to create a new campaign, request proposals, or stage a buy, hand off to the campaign-setup skill after readiness is proven. If the user asks to launch, pause, change, or troubleshoot an existing campaign, hand off to the campaign-management skill.

## Safety rules

- Obtain confirmation before every durable identity, terms, billing, connection, selection, or mapping change.
- Copy account, seller, connection, advertiser, version, and confirmation identifiers only from tool responses or explicit user input.
- Do not claim readiness until the final `get_status` result has `canBuyAnywhere: true` and at least one `destinations.readyDestinations` entry. Report `platformReady` separately; it is not proof that any destination is buyable.
- If a required tool or entitlement is unavailable, report that boundary and the exact next action instead of substituting another account or endpoint.
