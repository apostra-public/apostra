// Generated. Do not edit.
export const version = '0.37.0'
export const baseUrl = "https://api.apostra.com/api/v3"
export const m2mTokenUrl = "https://identity.scope3.com/oauth2/token"
export const operations = {
  "confirm_payment_authority": {
    "path": "/tools/confirm_payment_authority",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Issue the hosted card-capture link for a token from request_payment_authority. Give the link to the cardholder; cards stay off MCP."
  },
  "downloadV3PublicDocumentRevision": {
    "path": "/documents/{documentId}/revisions/{revisionId}/download",
    "method": "GET",
    "body": false,
    "binary": true,
    "idempotencyKey": false,
    "parameters": [
      {
        "name": "documentId",
        "location": "path",
        "required": true
      },
      {
        "name": "revisionId",
        "location": "path",
        "required": true
      }
    ],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Download a public immutable document revision"
  },
  "generate_variants": {
    "path": "/tools/generate_variants",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Generate variants from a saved brief; use Creative Sessions for voice/audio, radio spots, and voiceovers. Send kind, scope, and variantAction; reuse actionKey only on retries."
  },
  "get": {
    "path": "/tools/get",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Read one object by kind and id, or an account singleton without id. Never guess ids. Campaign reads return targetingOverlay to verify before proposals. include adds detail only for kinds that serve it."
  },
  "getV3PublicDocumentRevisionSections": {
    "path": "/documents/{documentId}/revisions/{revisionId}/sections",
    "method": "GET",
    "body": false,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [
      {
        "name": "documentId",
        "location": "path",
        "required": true
      },
      {
        "name": "revisionId",
        "location": "path",
        "required": true
      },
      {
        "name": "section",
        "location": "query",
        "required": false
      },
      {
        "name": "query",
        "location": "query",
        "required": false
      },
      {
        "name": "cursor",
        "location": "query",
        "required": false
      },
      {
        "name": "asOf",
        "location": "query",
        "required": false
      }
    ],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Read a bounded public immutable document revision"
  },
  "getV3PublicMutationReceipt": {
    "path": "/receipts/{receiptId}",
    "method": "GET",
    "body": false,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [
      {
        "name": "receiptId",
        "location": "path",
        "required": true
      }
    ],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Read the state of a V3 HTTP write receipt"
  },
  "get_delivery": {
    "path": "/tools/get_delivery",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Query seller delivery, stored or live buyer campaign delivery, or margin facts. Use live_campaign_delivery with one campaignId for the connected provider's current response. campaign_delivery preserves stored rows, totals, and paging. Buyer measurement is excluded."
  },
  "get_rfp_performance": {
    "path": "/tools/get_rfp_performance",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns."
  },
  "get_seller_reporting_receipts": {
    "path": "/tools/get_seller_reporting_receipts",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Show a seller what reporting we received for one buyer media buy, whether each receipt was accepted, and the current computed daily totals. Opens the Media Buy Timeline Glance."
  },
  "get_status": {
    "path": "/tools/get_status",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Current account, state, blockers, exact fixes, accounts to pick from. For seller demand, tells if readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand. A Developer account adds each agent's stage, blocker, next call."
  },
  "log_event": {
    "path": "/tools/log_event",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "idempotencyKey",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Send up to 10,000 AdCP conversion events (log_event) to an event source the advertiser registered with save_event_source. Events must also pass the v2 rules: no raw email or phone in user_match, each event_type + event_id once per call. One invalid event refuses the whole call."
  },
  "open_advertisers_page": {
    "path": "/tools/open_advertisers_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the Advertisers Page: every advertiser with its campaign and draft counts and one next action each. Use it for \"show my advertisers\" or \"where do I start\"; the Page self-fetches. To add or set up an advertiser, pass intent: \"add\". For a text answer use search(kind: \"advertiser\")."
  },
  "open_agent_page": {
    "path": "/tools/open_agent_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open one agent owned by this Developer account."
  },
  "open_agent_sources_page": {
    "path": "/tools/open_agent_sources_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open one agent’s Inventory sources Page: the inventory sources it powers and the health of each. Read-only."
  },
  "open_agent_webhooks_page": {
    "path": "/tools/open_agent_webhooks_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open one agent’s Webhooks Page: its recent inbound webhook outcomes, each refusal with its reason. Read-only."
  },
  "open_agents_page": {
    "path": "/tools/open_agents_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open Build an agent for this Developer account."
  },
  "open_approvals": {
    "path": "/tools/open_approvals",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the Approvals Page for reviews, assignments, routing, evidence, decisions, and forward recovery. Focus by exact media-buy identity or reviewRef; creativeId works only for one loaded version."
  },
  "open_campaign_receipt": {
    "path": "/tools/open_campaign_receipt",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign."
  },
  "open_campaigns_page": {
    "path": "/tools/open_campaigns_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the Campaigns Page: campaigns with status, flight, and budget; open one for its media buys and creatives. The Page self-fetches, so do not list campaigns in prose. advertiserId scopes to one advertiser; campaignId focuses one campaign. A draft's go-live review is open_campaign_receipt."
  },
  "open_connections_page": {
    "path": "/tools/open_connections_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction \"connect\" opens that media partner at connection setup without mutating until the user confirms. Replaced by open_media_partners_page, which opens the same Page."
  },
  "open_creative_engines_page": {
    "path": "/tools/open_creative_engines_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the buyer Creative Engines Page. Optionally focus an engine, connection, or its secure setup control; the buyer starts setup in the Page, and this does not authorize a provider or start generation."
  },
  "open_creative_library": {
    "path": "/tools/open_creative_library",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open Creative Library. Use search for a plain object answer. The composer can start from an advertiser or a campaign and does not need a Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format."
  },
  "open_developer_home": {
    "path": "/tools/open_developer_home",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the Developer home for this Developer account: its agents, their stages and what to do next."
  },
  "open_media_buys_page": {
    "path": "/tools/open_media_buys_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the Seller Media Buys Page. Optionally focus one account relationship or seller account mapping (not both) and its buys or creatives; the Page self-fetches."
  },
  "open_media_partners_page": {
    "path": "/tools/open_media_partners_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction \"connect\" opens that media partner at connection setup without mutating until the user confirms."
  },
  "open_page": {
    "path": "/tools/open_page",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open a compatibility Page. Owners create or attach the Agent in source_diagnostics. External hosts may return text. Credentials and authority changes remain human ceremonies."
  },
  "open_proposal_pass": {
    "path": "/tools/open_proposal_pass",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open Proposal Pass on one exact immutable RFP turn. Supply the matching rfpId and turnId from save_rfp or get; the Page loads the private response itself."
  },
  "open_seller_dashboard": {
    "path": "/tools/open_seller_dashboard",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches."
  },
  "open_variant_gallery": {
    "path": "/tools/open_variant_gallery",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Show a saved Creative Session’s variants (find via search/get kind creative_session). Not for generating new variants."
  },
  "refresh_inventory_source_health": {
    "path": "/tools/refresh_inventory_source_health",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Rechecks one external sales-agent source with no-spend get_products and, if it publishes one, a catalog refresh. Returns each check, findings still open, evidence IDs and readiness; no source configuration or media buy. scope accounts re-lists the source's accounts instead."
  },
  "request_buyer_child_account": {
    "path": "/tools/request_buyer_child_account",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "idempotencyKey",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:admin"
        ]
      }
    ],
    "summary": "Request a Buyer child under the selected Organization. Nothing is created until an Organization administrator approves it on our site; the result is approval_required with a link to show the person. Repeat with the same idempotencyKey and name for the outcome."
  },
  "request_payment_authority": {
    "path": "/tools/request_payment_authority",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Stage a card handoff for the organization and return a confirmation token. No link is issued until confirm_payment_authority."
  },
  "request_proposals": {
    "path": "/tools/request_proposals",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "idempotencyKey",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds and sellerAccountIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true."
  },
  "request_seller_reporting_update": {
    "path": "/tools/request_seller_reporting_update",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Requests a scheduler-run reporting refresh or a bounded replay for one seller media buy. It never polls a provider directly."
  },
  "review_buyer_child_account": {
    "path": "/tools/review_buyer_child_account",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:admin"
        ]
      }
    ],
    "summary": "Review a Buyer child under the selected Organization: name, role, capacity, plan coverage, operator, inherited access and other effects. Read-only; nothing is created. Show the review to the person, then call request_buyer_child_account."
  },
  "save_account": {
    "path": "/tools/save_account",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:admin"
        ]
      }
    ],
    "summary": "Create a child Account (omit id), rename one, or archive or restore it (isArchived). Each is recorded for website approval by an Organization administrator; repeat with the same idempotencyKey for the outcome. dryRun previews. settings.company saves at once. Never changes owners or members."
  },
  "save_advertiser": {
    "path": "/tools/save_advertiser",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Save an advertiser or mappings. Buyer privateNotes: owning Buyer Account only; /v3/manage-ads#private-advertiser-notes. Confirm markets/channels (footprintProposal); needs_input=ask; never recreate for currency. Brand: identityContract:confirmed-v1; preview: resolveBrand; read advertiser.brandRef."
  },
  "save_advertiser_grant": {
    "path": "/tools/save_advertiser_grant",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:admin"
        ]
      }
    ],
    "summary": "Invite another Organization to exact advertisers, accept/reject an invitation, or revoke a grant. Limited beta: eligible Organization, entitlement, server-side exposure, and direct human-admin authority are required."
  },
  "save_advertiser_instructions": {
    "path": "/tools/save_advertiser_instructions",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Seller-only CRM notes for an exact brand × operator pair. Buyers use save_advertiser.privateNotes; see /v3/manage-ads#private-advertiser-notes. Effective discounts, routing, access and trust are read-only."
  },
  "save_agent": {
    "path": "/tools/save_agent",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Confirm a Sales Agent product mode, register a Sales or Creative Agent, or update an owned Agent: rename it or allow certification buys. To connect from a URL, send agentUrl with dryRun: true, show what was read, then send it without dryRun. A connected agent is not yet verified as theirs."
  },
  "save_ask": {
    "path": "/tools/save_ask",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "File or update a typed ask in the Apostra Support workflow; returns askId. kind create files a new ask; kind update sends only id and requester. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first."
  },
  "save_audience": {
    "path": "/tools/save_audience",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Sync first-party CRM audiences for a buyer advertiser. Each audiences[] item may add, remove, or delete members. Returns an operationId; use get(kind: audience, advertiserId: \"...\") to read match status after it settles."
  },
  "save_billing": {
    "path": "/tools/save_billing",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Accept Terms, set the payment terms sellers are asked for, or accept a plan, answer its offer and change its renewal. Accepting a plan needs an administrator to approve it on our site. Cards stay off MCP."
  },
  "save_business_rules": {
    "path": "/tools/save_business_rules",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Write seller AI Business Rules. Policy content needs an account admin and both policy fields. Approval auto needs acknowledgeNoHumanReview."
  },
  "save_buyer_agent": {
    "path": "/tools/save_buyer_agent",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:admin"
        ]
      }
    ],
    "summary": "Create a buyer agent, or with id make one change: name, advertiser access, lifecycle state, or credential handoff."
  },
  "save_buyer_operator": {
    "path": "/tools/save_buyer_operator",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:admin"
        ]
      }
    ],
    "summary": "Save buyer commercial identity. Read get_status; use identityContract:confirmed-v1 for preview and confirmation. Guide: /v2/setup/v3/identity-setup."
  },
  "save_campaign": {
    "path": "/tools/save_campaign",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "idempotencyKey",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create: advertiserId/name; flight/budget optional. Receipts and launch previews show local/UTC times in the applicable IANA timezone. desiredPhase: active previews; confirmLaunch: true launches. Cancellation is irreversible: desiredPhase: canceled cancels the campaign and every live media buy."
  },
  "save_catalog": {
    "path": "/tools/save_catalog",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "idempotencyKey",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create or replace a catalog: type and exactly one of url (feed URL) or non-empty items are required. If missing, ask the buyer for the feed URL or items before calling. URL saves refetch the feed. To archive, set isArchived: true with identity only; type, url and items are not needed."
  },
  "save_connection": {
    "path": "/tools/save_connection",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Manage seller or creative-engine authorization, accounts and advertiser mappings. Seller-only: reporting, selection, billing, policy, activation."
  },
  "save_coverage": {
    "path": "/tools/save_coverage",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, `removeProperties`, and `refresh` act on named items only. Read authorization; never assume it."
  },
  "save_creative": {
    "path": "/tools/save_creative",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "advertiserId/campaignId:name,message;assets/landing_page_url/social/sourceAssetRef/sourceAssets;Supplied content/assets only;generate new media (radio spots):save_creative_session;exactly one format selector:formatKind/formatParams,creativeFormatId/formatOptionRef;libraryRole:Buyer Account only."
  },
  "save_creative_collection": {
    "path": "/tools/save_creative_collection",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Manage collections. Create with one owner and name: campaignId or advertiserId. Only advertiser mutations of an existing collection need expectedUpdatedAt; campaign writes and creates do not. isArchived archives or restores advertiser collections."
  },
  "save_creative_session": {
    "path": "/tools/save_creative_session",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Save a Creative Session for image, video, or voice/audio (including radio spots) from a brief: its draft, selected output, approval, or finalisation. It never generates; generate_variants does. To save an approved output to the Library, use save_creative with fromCreativeSessionOutput."
  },
  "save_dimension": {
    "path": "/tools/save_dimension",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "idempotencyKey",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create a dimension, or update an existing dimension by its id. Tags is built in and open. Labels belong only to objects in appliesTo."
  },
  "save_directed_campaign_subscription": {
    "path": "/tools/save_directed_campaign_subscription",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Import native campaigns from Spotify Ads Manager or other platforms, including future-start campaigns, as read-only mirrors. Confirm ongoing sync first. No provider changes. /v3/import-existing-campaigns."
  },
  "save_event_source": {
    "path": "/tools/save_event_source",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "idempotencyKey",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create, change, archive, or restore up to 50 advertiser conversion event sources (pixels, server feeds). Each entry is keyed by eventSourceId and succeeds or fails alone. Setup is not proof events flow: check health with get, then use eventSourceId in an optimization goal."
  },
  "save_inventory_source": {
    "path": "/tools/save_inventory_source",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create or update where a seller's inventory comes from. Pass `id` to change a source or omit it to add one. Pass only `agentId` or `adServer` to open the form that connects an agent or an ad server. Credentials are never passed here; a source that needs one returns the page that collects it."
  },
  "save_lesson": {
    "path": "/tools/save_lesson",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Manage seller lessons in a seller account; send the accountId of that account. propose requires lesson; approve and retire require lessonId; preview requires lessonId and brief. Preserve seller words from a private Session note and ask if kind or scope is unclear."
  },
  "save_library_request": {
    "path": "/tools/save_library_request",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Open a seller library request or close it with seller Material."
  },
  "save_material": {
    "path": "/tools/save_material",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create or update seller Materials. Seller beta: preview, delete, Undo deletion, or Include again for one imported Library document. Delete archives it, excludes its source until Include again, and purges it after 30 days. https://docs.apostra.com/v3/delete-from-apostra"
  },
  "save_media_buy": {
    "path": "/tools/save_media_buy",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "idempotencyKey",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates."
  },
  "save_media_kit": {
    "path": "/tools/save_media_kit",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Deprecated compatibility tool (\"listing\" is the modern term). It writes only the legacy businessProfile and does not update the canonical buyer-visible listing. New clients must read with `get({ kind: \"seller\", include: [\"listing\"] })` and write with `save_seller`."
  },
  "save_notification_config": {
    "path": "/tools/save_notification_config",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create or update a notification subscription. Omit subscriptionId to create; managed subscriptions permit only mutable fields. Use save_integration for credentials when needed."
  },
  "save_playbook": {
    "path": "/tools/save_playbook",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Write selling guidance. `active` turns Playbook prose and its optional seller note into proposed Lessons; the active Playbook is unchanged. `pricing` replaces facts. `discounts` sets or removes brand/operator rules. Halves never roll back each other."
  },
  "save_property_list": {
    "path": "/tools/save_property_list",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create, update, archive, restore, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists."
  },
  "save_rfp": {
    "path": "/tools/save_rfp",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "clientRequestId",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Save an RFP: create it from an origin, revise it with a new request, endorse or unendorse its response, or attach an imported response. A turn’s feedback, release, proposal files and outcome use save_rfp_turn."
  },
  "save_rfp_turn": {
    "path": "/tools/save_rfp_turn",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "bodyKeyField": "clientRequestId",
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Change one RFP turn: release it, request or cancel a proposal file, append feedback, or record its outcome. One of these per call; revise, endorse and attach a response with save_rfp."
  },
  "save_seller": {
    "path": "/tools/save_seller",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Save Seller identity, capabilities, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, an admission, the intake hold, or the demo's expiry and sample sources. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get."
  },
  "save_signal": {
    "path": "/tools/save_signal",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create, replace, or archive a signal. Managed writes need a complete draft; read before updates. Without sourceId, writes the seller catalog."
  },
  "save_wholesale_product": {
    "path": "/tools/save_wholesale_product",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not."
  },
  "save_work_item": {
    "path": "/tools/save_work_item",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:write"
        ]
      }
    ],
    "summary": "Decide a creative or media-buy approval, or complete a modular-source follow-up. Repeats preserve evidence; retry, evaluation, and reassignment stay on the approvals Page."
  },
  "search": {
    "path": "/tools/search",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Find objects in this account, or answer questions from the docs. Pass kind to list one object type, query to match text, or both. Before a multi-step task, search kind skill for a workflow. Reread a docs hit with its document (and revision, for agreements) before you cite it."
  },
  "test_creative_macros": {
    "path": "/tools/test_creative_macros",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": false,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Dry-runs one tracker URL through exact raw input, canonical AdCP compilation, recipient translation, and deterministic synthetic substitution. Use it before preview or trafficking; unresolved required macros fail closed."
  },
  "upload_creative_asset": {
    "path": "/tools/upload_creative_asset",
    "method": "POST",
    "body": true,
    "binary": false,
    "idempotencyKey": true,
    "parameters": [],
    "security": [
      {
        "apiKeyAuth": []
      },
      {
        "m2mOAuth": [
          "interchange:read"
        ]
      }
    ],
    "summary": "Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative."
  }
} as const
export type OperationId = keyof typeof operations
