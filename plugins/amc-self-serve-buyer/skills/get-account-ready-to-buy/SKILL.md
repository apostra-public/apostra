---
name: get-account-ready-to-buy
description: Prepare an Interchange buyer account to transact. Use when a user asks to set up, onboard, activate or unblock the buyer account, connect a provider account, accept terms, establish billing authority, or find what must be completed before buying media.
---

# Get an Account Ready to Buy

Use the attached Interchange V3 buyer tools. Treat `get_status` as the authority on the active account, readiness, blockers, and next actions.

## Workflow

1. Call `get_status` before changing anything.
2. Confirm the account is the buyer account the user intends to configure. If it is not, present the reachable accounts and ask the user which one they mean. Send that account's `accountId` on every call, as `get_status` returns it; do not call `switch_account`.
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
   - For payment terms, call `save_billing` with `{ paymentTerms }`, sent alone, only after the user chooses the terms. The call changes nothing. It returns `approval_required` with a link that a direct administrator of the organization opens on our site to approve the terms. Show the person the link and say that nothing changes until an administrator approves. To check, call again with the same input plus the `idempotencyKey` the answer named, which only reads the approval: `payment_terms_saved` means it is approved, and `approval_required` means it is waiting (its state says which, and a rejected, expired or failed one is over). The same call without the key asks again, so send it only when the user wants to ask again. Terms the organization has already chosen need no approval and return `payment_terms_saved` at once. If you no longer have the key, `get({ kind: 'billing', accountId })` lists your own waiting payment terms and renewal requests as `pendingApprovals`, each with what was asked and its key. If the call is refused, the user is not a direct administrator of the organization: say so and ask one to make the choice.
   - To end the plan at the end of its term, or to keep it renewing, read `renewal` in `get({ kind: 'billing', accountId })`: `allowedActions` names the changes allowed now, `changeAllowedUntil` the deadline, and `version` the renewal version to send. Ask the user for a reason of at least three characters and confirm the change, then call `save_billing` with `{ renewal: { renewalVersion, action, reason } }`, sent alone. The call changes nothing. It returns `approval_required` with a link that a direct administrator of the organization opens on our site to approve the change. Show the person the link and say that nothing changes until an administrator approves. To check, call again with the same input plus the `idempotencyKey` the answer named, which only reads the approval: `renewal_changed` means it is approved, and `approval_required` means it is waiting (its state says which, and a rejected, expired or failed one is over). The same call without the key asks again, so send it only when the user wants to ask again. A refused version or action means the renewal changed: read it again and confirm again. If the call is refused for authority, the user is not a direct administrator of the organization: say so and ask one to make the change.
   - For missing billing details (`payer.complete` is false in `get({ kind: 'billing', accountId })`), ask the user for the payer name, street address and country, and any invoice email or tax ID they want on invoices. Confirm the exact details with the user, then call `save_billing` with `{ payer: { ...only the fields they gave } }`, sent alone. A direct administrator's call saves them straight away and returns `payer_saved` with the saved details; there is no approval link. If the call is refused, the user is not a direct administrator of the organization: say so and ask one to make the change. Never make up payer details.
   - For payment authority, ask for confirmation before requesting it. Then follow this flow exactly: `request_payment_authority` with an `idempotencyKey` records a request and returns `approval_required` with a link. Give that link to the user, because a direct administrator of the organization must approve the card setup on Apostra before anything is prepared. Call `request_payment_authority` again with the same `idempotencyKey` to check; once it is approved it returns a single-use confirmation token. `confirm_payment_authority` spends that token to issue the hosted card-capture link, and `get({ kind: 'billing', accountId })` reports the status afterwards. Send the chosen `accountId` on every call in this flow. If you no longer have the key, `get({ kind: 'billing', accountId })` lists your own waiting card setup as `pendingApprovals`, with its link and key. If the request is rejected, expires or cannot be completed, say so and start a new request with a new `idempotencyKey` only if the user still wants it. A service token or an impersonated session cannot ask: the user must be a direct administrator.
   - Give the hosted link only to the organization cardholder. The cardholder may be someone other than the administrator who approved, and needs no sign-in to open it. Never request or transmit card data in chat or MCP calls.
6. For seller connections:
   - Use `search` and `get` to find the exact seller, connection, provider account, and advertiser mapping.
   - Use `open_media_partners_page` when the host supports its UI; otherwise use `save_connection`.
   - Send authorization through the returned browser URL. Never ask for provider credentials in chat.
   - Use one `save_connection` intent per call. Authorize only when the current connection state requires it, poll with `search` or `get`, then make separate confirmed calls to select a returned provider account and map it to the exact advertiser when required. Re-read after each step.
7. Call `get_status` again. Report what is complete, what still requires the user or an administrator, and whether the account is ready to transact.

If the user asks to create a new campaign, request proposals, or stage a buy, hand off to the campaign-setup skill after readiness is proven. If the user asks to launch, pause, change, or troubleshoot an existing campaign, hand off to the campaign-management skill.

## Safety rules

- Obtain confirmation before every durable identity, terms, billing, connection, selection, or mapping change. A payment terms choice, a renewal change or a card setup only asks an administrator to approve it: do not tell the user it is saved until a repeat call with its `idempotencyKey` returns `payment_terms_saved`, `renewal_changed` or the card setup's confirmation token.
- Copy account, seller, connection, advertiser, version, and confirmation identifiers only from tool responses or explicit user input.
- Do not claim readiness until the final `get_status` result has `canBuyAnywhere: true` and at least one `destinations.readyDestinations` entry. Report `platformReady` separately; it is not proof that any destination is buyable.
- If a required tool or entitlement is unavailable, report that boundary and the exact next action instead of substituting another account or endpoint.
