---
name: manage-a-campaign
description: Review and manage an existing Interchange buyer campaign. Use when a user asks about campaign status, delivery, spend, pacing, an existing campaign's creatives, blockers, launch, pause, archive, budget or flight changes, troubleshooting, or what needs attention.
---

# Manage a Campaign

Ground every recommendation and change in the current campaign, delivery, and creative records from the attached Interchange V3 buyer server.

## Workflow

1. Call `get_status` and confirm the active buyer account.
2. Use `search` to find the intended campaign and `get` with `include: ["mediaBuys", "creatives"]` to read its current revision, phase, flight, budget, media buys, creatives, and blockers. Ask the user to choose if more than one campaign matches.
   - If the phase is `draft`, say plainly that the campaign is not running: its media buys are not booked and nothing delivers until it is launched (step 7).
   - A creative on a draft media buy is sent to that buy's seller as soon as it is saved, so `pending_review` on a draft campaign is the seller's creative review, not a booking or delivery. Read the creative's `platformLinks` to say which seller holds it, why, and who must act, following [Creative sync outcomes](/v3/creative-sync-outcomes). `processing` with no platform link means no seller has the creative yet.
   - For a stored assessment of delivery and optimization goals, also request `include: ["progress"]`. Read each `goalProgress` verdict with its returned evidence; an empty list means no stored assessment yet, and `unavailableIncludes` means the assessment was unavailable, not that a goal failed. Do not substitute it for the live provider delivery read in step 3.
3. For live delivery questions, call `get_delivery` with `report: "live_campaign_delivery"`, the exact campaign ID, and an explicit inclusive UTC `range` no longer than 90 days. Do not pass metrics, dimensions, other filters, or a cursor. The response preserves the validated live provider payload. Use `campaign_delivery` only when the user asks for stored aggregate rows.
4. Report the provider reporting period, currency, totals, warnings, and missing values. A live provider response does not establish reporting-pipeline finality or billing eligibility. Distinguish observed facts from recommendations; do not turn missing measurement into zero performance.
5. Inspect related creatives or creative collections with `search` and `get` when readiness or delivery indicates a creative issue. Do not claim approval, attachment, or provider propagation unless returned evidence proves it.
   - For a local JPEG, PNG, eligible MP4, HTML5 ZIP, or VAST XML file, call `upload_creative_asset` with the exact buyer-owned `advertiserId`. When the upload is intended for a campaign, also pass `campaign_composition` with its exact `campaign_id` and matching `advertiser_id`; that context does not itself associate the upload. The Task app, not the model, handles the file bytes.
   - Before uploading an HTML5 ZIP, retrieve [HTML5 and display tag creative requirements](/v3/html5-creative-requirements) with `search` and `get`, and check the ZIP against it with the user: one click tag declared in the main HTML file, a declared ad size, and the size limit the page states.
   - After the Task finalizes a JPEG or PNG and returns its private source reference, use `save_creative` with that exact `sourceAssetRef` and either the intended `campaignId` or, for an advertiser-scoped Creative, `advertiserId` after confirmation. A finalized MP4 is upload-only on V3: do not call `save_creative`, claim a Creative or campaign attachment exists, claim delivery, or silently substitute a V2 write.
   - A finalized HTML5 ZIP or VAST file is saved as a draft Library creative, and the Task returns its `creative_id`. Ask for the click-through URL, then finish it with `save_creative` using that `creativeId`, the `advertiserId`, `mode: "complete"`, and `landing_page_url`, with no campaign, following [Finish an uploaded HTML5 ZIP or VAST draft](/v3/manage-ads#finish-an-uploaded-html5-zip-or-vast-draft). A draft cannot be attached to a campaign. Once it is complete, attach it after confirmation with `save_creative`, `creativeId`, `advertiserId`, and `campaignIds`.
   - Report each creative's state separately (uploaded draft, complete, attached to the campaign) and confirm each with `get` before reporting it. If the Task or `save_creative` fails, say which files were not saved; never describe a failed upload as a saved draft.
   - For a file the buyer already hosts at a public URL (an image, video, audio, HTML or VAST XML file), do not use the Task. After confirmation, call `save_creative` with `assets`, each giving exactly one public `url` and its `assetType`, plus the intended `campaignId` (or `advertiserId` for a Library creative) and `landing_page_url`, following [Create and verify a campaign creative](/v3/tool-reference#create-and-verify-a-campaign-creative). A VAST asset also takes `vastVersion` when the buyer knows it. An HTML5 ZIP goes through `upload_creative_asset`, never a URL. Use only a URL the buyer gave you; never invent or rewrite one.
   - Treat an already-existing provider-scoped V2 source as a separate Legacy request: stop and hand off to its matching V2 connection; never reinterpret V3 output as provider-bound.
6. Explain what needs attention and propose the smallest supported change. Before any write, show the exact target, current revision, requested fields, expected effect, and material risk.
7. After confirmation:
   - Use `save_campaign` for supported campaign changes with the current `expectedRevision` and a stable idempotency key. Reuse that key only when retrying the exact same intent.
   - To launch, first call `save_campaign` with `desiredPhase: "active"` and without `confirmLaunch`. Run the checks under "Before you launch" and show their results with the returned preview, obtain confirmation, then call it again with `confirmLaunch: true`, the preview's revision as `expectedRevision`, and the required idempotency key.
   - Use `save_creative` or `save_creative_collection` for confirmed creative changes with exact IDs.
   - Treat campaign or creative archival and financial changes as destructive; require explicit confirmation immediately before the call.
8. Read the updated campaign and relevant delivery evidence again. Report the observed result, warnings, partial writes, downstream errors, and unresolved actions.

## Before you launch

Between the launch preview and `confirmLaunch: true`, check the campaign with the buyer. The preview and the platform's own launch checks decide readiness; present what they return and never work it out yourself.

1. Present the preview in full: every media buy, each creative the preview lists as not ready, each buy that books now with its creative attaching once the seller approves it, and the flight in local time and UTC. Never summarise a preview problem away.
2. Read each buy back with `get` kind `media_buy` and `include: ["products", "creatives"]`. Check that each package's targeting and creatives match what the buyer asked for, following [Add buying steps](/v3/build-an-agent#add-buying-steps).
3. Test each click-through. Read the campaign's tracking with `get` and `include: ["tracking"]`. For each creative's final click URL (its `landing_page_url` with the campaign's click-URL parameters), call `test_creative_macros` with that URL as `rawInput`, a `scenario`, and the macros the URL uses as `requiredMacros`. Report any macro that does not resolve as a blocker for the buyer to decide on. When a creative was just saved, its `save_creative` result also carries `macroPreview`: name to the buyer any macro under `filledBySomeSellers` or `literal`, since it may not expand at every seller. Follow [See how a saved creative's trackers expand](/v3/tool-reference#see-how-a-saved-creatives-trackers-expand) and [Landing-page macros](/v3/landing-page-macros).
4. State each buy's pacing, budget and any daily cap. Report them; change nothing the buyer did not ask for.
5. If the buyer keeps their own analytics or UTM convention, offer to turn Apostra's tags off with `tracking.autoUtm: false` and set their parameters as `tracking.macroAdditions`, following [Auto-tagged links](/v3/auto-tagged-links). Change tracking only after confirmation. A creative a seller already holds keeps its old link until it is sent again, so say which creatives that affects.
6. When a blocker is one the buyer cannot fix, such as a seller refusal or a creative stuck in sync, offer to file it with `save_ask` (`type` `support`, or `supply` for missing inventory). Show the draft and file it only after confirmation.

## Safety rules

- Never invent IDs, revisions, metrics, statuses, prices, or causal explanations.
- Do not silently retry a non-idempotent mutation. Re-read state before deciding whether a retry is safe.
- Never broaden a requested budget, flight, seller, creative, or campaign change.
- Do not claim success from prose alone; require a successful tool result and verify the resulting state.
- If the requested operation is unavailable in the current tool catalog, state the boundary and offer the nearest supported read or next action.
- Never say a campaign is running, booked, or delivering unless its phase is `active` and its media buys are booked.
- Campaign cancellation and unarchiving are not supported by the current V3 tool. Do not imply that pause, archive, and cancellation are interchangeable.

If the user needs buyer-account prerequisites, hand off to the account-readiness skill. If the user needs a new draft campaign, proposal round, or first media-buy staging, hand off to the campaign-setup skill.
