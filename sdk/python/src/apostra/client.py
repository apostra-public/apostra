# Generated. Do not edit.
from typing import cast
from . import models
from .transport import AsyncTransport, ResponseDetails, SyncTransport

class Apostra(SyncTransport):
    def get_v3_public_document_revision_sections(self, input: models.GetV3PublicDocumentRevisionSectionsInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetV3PublicDocumentRevisionSectionsResult:
        "Read a bounded public immutable document revision"
        return cast("models.GetV3PublicDocumentRevisionSectionsResult", self._request("getV3PublicDocumentRevisionSections", input, account_id=account_id, timeout=timeout))

    def get_v3_public_document_revision_sections_with_response(self, input: models.GetV3PublicDocumentRevisionSectionsInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetV3PublicDocumentRevisionSectionsResult]:
        "Read a bounded public immutable document revision Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetV3PublicDocumentRevisionSectionsResult], self._request_with_response("getV3PublicDocumentRevisionSections", input, account_id=account_id, timeout=timeout))

    def download_v3_public_document_revision(self, input: models.DownloadV3PublicDocumentRevisionInput, *, account_id: str | None = None, timeout: float | None = None) -> bytes:
        "Download a public immutable document revision"
        return cast("bytes", self._request("downloadV3PublicDocumentRevision", input, account_id=account_id, timeout=timeout))

    def download_v3_public_document_revision_with_response(self, input: models.DownloadV3PublicDocumentRevisionInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[bytes]:
        "Download a public immutable document revision Returns the data together with response headers and request ID."
        return cast(ResponseDetails[bytes], self._request_with_response("downloadV3PublicDocumentRevision", input, account_id=account_id, timeout=timeout))

    def get_v3_public_mutation_receipt(self, input: models.GetV3PublicMutationReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetV3PublicMutationReceiptResult:
        "Read the state of a V3 HTTP write receipt"
        return cast("models.GetV3PublicMutationReceiptResult", self._request("getV3PublicMutationReceipt", input, account_id=account_id, timeout=timeout))

    def get_v3_public_mutation_receipt_with_response(self, input: models.GetV3PublicMutationReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetV3PublicMutationReceiptResult]:
        "Read the state of a V3 HTTP write receipt Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetV3PublicMutationReceiptResult], self._request_with_response("getV3PublicMutationReceipt", input, account_id=account_id, timeout=timeout))

    def get_status(self, input: models.GetStatusInput = {}, *, account_id: str | None = None, timeout: float | None = None) -> models.GetStatusResult:
        "Current account, state, blockers, exact fixes, and reachable accounts. For seller demand, use it to tell whether readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand."
        return cast("models.GetStatusResult", self._request("get_status", input, account_id=account_id, timeout=timeout))

    def get_status_with_response(self, input: models.GetStatusInput = {}, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetStatusResult]:
        "Current account, state, blockers, exact fixes, and reachable accounts. For seller demand, use it to tell whether readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetStatusResult], self._request_with_response("get_status", input, account_id=account_id, timeout=timeout))

    def refresh_inventory_source_health(self, input: models.RefreshInventorySourceHealthInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RefreshInventorySourceHealthResult:
        "Rechecks one external sales-agent source with no-spend get_products. Returns evidence IDs and seller readiness; no source configuration or media buy."
        return cast("models.RefreshInventorySourceHealthResult", self._request("refresh_inventory_source_health", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def refresh_inventory_source_health_with_response(self, input: models.RefreshInventorySourceHealthInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.RefreshInventorySourceHealthResult]:
        "Rechecks one external sales-agent source with no-spend get_products. Returns evidence IDs and seller readiness; no source configuration or media buy. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.RefreshInventorySourceHealthResult], self._request_with_response("refresh_inventory_source_health", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_account(self, input: models.SaveAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAccountResult:
        "Rename an existing direct child Account or update settings.company. Never provisions, archives, or changes owners or members; use Account settings for access changes."
        return cast("models.SaveAccountResult", self._request("save_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_account_with_response(self, input: models.SaveAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAccountResult]:
        "Rename an existing direct child Account or update settings.company. Never provisions, archives, or changes owners or members; use Account settings for access changes. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAccountResult], self._request_with_response("save_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def review_buyer_child_account(self, input: models.ReviewBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None) -> models.ReviewBuyerChildAccountResult:
        "Review a Buyer child under the selected Organization: name, role, capacity, plan coverage, operator, inherited access and other effects. Read-only; nothing is created. Show the review to the person, then call request_buyer_child_account."
        return cast("models.ReviewBuyerChildAccountResult", self._request("review_buyer_child_account", input, account_id=account_id, timeout=timeout))

    def review_buyer_child_account_with_response(self, input: models.ReviewBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.ReviewBuyerChildAccountResult]:
        "Review a Buyer child under the selected Organization: name, role, capacity, plan coverage, operator, inherited access and other effects. Read-only; nothing is created. Show the review to the person, then call request_buyer_child_account. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.ReviewBuyerChildAccountResult], self._request_with_response("review_buyer_child_account", input, account_id=account_id, timeout=timeout))

    def request_buyer_child_account(self, input: models.RequestBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RequestBuyerChildAccountResult:
        "Request a Buyer child under the selected Organization. Nothing is created until an Organization administrator approves it on our site; the result is approval_required with a link to show the person. Repeat with the same idempotencyKey and name for the outcome."
        return cast("models.RequestBuyerChildAccountResult", self._request("request_buyer_child_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def request_buyer_child_account_with_response(self, input: models.RequestBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.RequestBuyerChildAccountResult]:
        "Request a Buyer child under the selected Organization. Nothing is created until an Organization administrator approves it on our site; the result is approval_required with a link to show the person. Repeat with the same idempotencyKey and name for the outcome. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.RequestBuyerChildAccountResult], self._request_with_response("request_buyer_child_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_ask(self, input: models.SaveAskInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAskResult:
        "File or update a typed ask in the Apostra Support workflow; returns askId. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first."
        return cast("models.SaveAskResult", self._request("save_ask", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_ask_with_response(self, input: models.SaveAskInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAskResult]:
        "File or update a typed ask in the Apostra Support workflow; returns askId. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAskResult], self._request_with_response("save_ask", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_billing(self, input: models.SaveBillingInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBillingResult:
        "Accept current Terms, choose the payment terms sellers are asked for, or manage payment authority. Card setup uses a confirmed hosted link; card data never enters MCP."
        return cast("models.SaveBillingResult", self._request("save_billing", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_billing_with_response(self, input: models.SaveBillingInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveBillingResult]:
        "Accept current Terms, choose the payment terms sellers are asked for, or manage payment authority. Card setup uses a confirmed hosted link; card data never enters MCP. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveBillingResult], self._request_with_response("save_billing", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_notification_config(self, input: models.SaveNotificationConfigInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveNotificationConfigResult:
        "Create or update a notification subscription: scope, content, routes; no trigger type is creatable yet, no delivery policy yet. Omit subscriptionId to create, supply it to patch. Managed subscriptions are editable only within their mutability. Credentials belong to save_integration."
        return cast("models.SaveNotificationConfigResult", self._request("save_notification_config", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_notification_config_with_response(self, input: models.SaveNotificationConfigInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveNotificationConfigResult]:
        "Create or update a notification subscription: scope, content, routes; no trigger type is creatable yet, no delivery policy yet. Omit subscriptionId to create, supply it to patch. Managed subscriptions are editable only within their mutability. Credentials belong to save_integration. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveNotificationConfigResult], self._request_with_response("save_notification_config", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser_grant(self, input: models.SaveAdvertiserGrantInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserGrantResult:
        "Invite another Organization to exact advertisers, accept/reject an invitation, or revoke a grant. Limited beta: eligible Organization, entitlement, server-side exposure, and direct human-admin authority are required."
        return cast("models.SaveAdvertiserGrantResult", self._request("save_advertiser_grant", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser_grant_with_response(self, input: models.SaveAdvertiserGrantInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAdvertiserGrantResult]:
        "Invite another Organization to exact advertisers, accept/reject an invitation, or revoke a grant. Limited beta: eligible Organization, entitlement, server-side exposure, and direct human-admin authority are required. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAdvertiserGrantResult], self._request_with_response("save_advertiser_grant", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def search(self, input: models.SearchInput, *, account_id: str | None = None, timeout: float | None = None) -> models.SearchResult:
        "Find objects in this account, or answer questions from the docs. Pass kind to list one object type, query to match text, or both. Before a multi-step task, search kind skill for a workflow. Reread a docs hit with its document (and revision, for agreements) before you cite it."
        return cast("models.SearchResult", self._request("search", input, account_id=account_id, timeout=timeout))

    def search_with_response(self, input: models.SearchInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.SearchResult]:
        "Find objects in this account, or answer questions from the docs. Pass kind to list one object type, query to match text, or both. Before a multi-step task, search kind skill for a workflow. Reread a docs hit with its document (and revision, for agreements) before you cite it. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SearchResult], self._request_with_response("search", input, account_id=account_id, timeout=timeout))

    def get(self, input: models.GetInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetResult:
        "Read one object by kind plus the id that search returned, or an account singleton with no id. Never guess an id. include adds detail; each include value works only for the kinds that serve it."
        return cast("models.GetResult", self._request("get", input, account_id=account_id, timeout=timeout))

    def get_with_response(self, input: models.GetInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetResult]:
        "Read one object by kind plus the id that search returned, or an account singleton with no id. Never guess an id. include adds detail; each include value works only for the kinds that serve it. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetResult], self._request_with_response("get", input, account_id=account_id, timeout=timeout))

    def save_connection(self, input: models.SaveConnectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveConnectionResult:
        "Manage seller or creative-engine authorization, accounts and advertiser mappings. Seller-only: reporting, selection, billing, policy, activation."
        return cast("models.SaveConnectionResult", self._request("save_connection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_connection_with_response(self, input: models.SaveConnectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveConnectionResult]:
        "Manage seller or creative-engine authorization, accounts and advertiser mappings. Seller-only: reporting, selection, billing, policy, activation. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveConnectionResult], self._request_with_response("save_connection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_library_request(self, input: models.SaveLibraryRequestInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveLibraryRequestResult:
        "Open a seller library request or close it with seller Material."
        return cast("models.SaveLibraryRequestResult", self._request("save_library_request", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_library_request_with_response(self, input: models.SaveLibraryRequestInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveLibraryRequestResult]:
        "Open a seller library request or close it with seller Material. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveLibraryRequestResult], self._request_with_response("save_library_request", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def open_page(self, input: models.OpenPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenPageResult:
        "Open a compatibility Page. source_diagnostics can create or attach the Agent. External hosts may return text. Credentials and authority changes remain human ceremonies."
        return cast("models.OpenPageResult", self._request("open_page", input, account_id=account_id, timeout=timeout))

    def open_page_with_response(self, input: models.OpenPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenPageResult]:
        "Open a compatibility Page. source_diagnostics can create or attach the Agent. External hosts may return text. Credentials and authority changes remain human ceremonies. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenPageResult], self._request_with_response("open_page", input, account_id=account_id, timeout=timeout))

    def open_proposal_pass(self, input: models.OpenProposalPassInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenProposalPassResult:
        "Open Proposal Pass on one exact immutable RFP turn. Supply the matching rfpId and turnId from save_rfp or get; the Page loads the private response itself."
        return cast("models.OpenProposalPassResult", self._request("open_proposal_pass", input, account_id=account_id, timeout=timeout))

    def open_proposal_pass_with_response(self, input: models.OpenProposalPassInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenProposalPassResult]:
        "Open Proposal Pass on one exact immutable RFP turn. Supply the matching rfpId and turnId from save_rfp or get; the Page loads the private response itself. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenProposalPassResult], self._request_with_response("open_proposal_pass", input, account_id=account_id, timeout=timeout))

    def open_media_buys_page(self, input: models.OpenMediaBuysPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenMediaBuysPageResult:
        "Open the Seller Media Buys Page. Optionally focus one seller-owned account relationship and its buys or creatives; the Page self-fetches."
        return cast("models.OpenMediaBuysPageResult", self._request("open_media_buys_page", input, account_id=account_id, timeout=timeout))

    def open_media_buys_page_with_response(self, input: models.OpenMediaBuysPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenMediaBuysPageResult]:
        "Open the Seller Media Buys Page. Optionally focus one seller-owned account relationship and its buys or creatives; the Page self-fetches. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenMediaBuysPageResult], self._request_with_response("open_media_buys_page", input, account_id=account_id, timeout=timeout))

    def open_seller_dashboard(self, input: models.OpenSellerDashboardInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenSellerDashboardResult:
        "Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches."
        return cast("models.OpenSellerDashboardResult", self._request("open_seller_dashboard", input, account_id=account_id, timeout=timeout))

    def open_seller_dashboard_with_response(self, input: models.OpenSellerDashboardInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenSellerDashboardResult]:
        "Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenSellerDashboardResult], self._request_with_response("open_seller_dashboard", input, account_id=account_id, timeout=timeout))

    def open_agents_page(self, input: models.OpenAgentsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenAgentsPageResult:
        "Open Build an agent for this Developer account."
        return cast("models.OpenAgentsPageResult", self._request("open_agents_page", input, account_id=account_id, timeout=timeout))

    def open_agents_page_with_response(self, input: models.OpenAgentsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenAgentsPageResult]:
        "Open Build an agent for this Developer account. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenAgentsPageResult], self._request_with_response("open_agents_page", input, account_id=account_id, timeout=timeout))

    def open_agent_page(self, input: models.OpenAgentPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenAgentPageResult:
        "Open one agent owned by this Developer account."
        return cast("models.OpenAgentPageResult", self._request("open_agent_page", input, account_id=account_id, timeout=timeout))

    def open_agent_page_with_response(self, input: models.OpenAgentPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenAgentPageResult]:
        "Open one agent owned by this Developer account. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenAgentPageResult], self._request_with_response("open_agent_page", input, account_id=account_id, timeout=timeout))

    def open_connections_page(self, input: models.OpenConnectionsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenConnectionsPageResult:
        "Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction \"connect\" opens that media partner at connection setup without mutating until the user confirms."
        return cast("models.OpenConnectionsPageResult", self._request("open_connections_page", input, account_id=account_id, timeout=timeout))

    def open_connections_page_with_response(self, input: models.OpenConnectionsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenConnectionsPageResult]:
        "Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction \"connect\" opens that media partner at connection setup without mutating until the user confirms. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenConnectionsPageResult], self._request_with_response("open_connections_page", input, account_id=account_id, timeout=timeout))

    def open_creative_engines_page(self, input: models.OpenCreativeEnginesPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCreativeEnginesPageResult:
        "Open the buyer Creative Engines Page. Optionally focus an engine, connection, or its secure setup control; the buyer starts setup in the Page, and this does not authorize a provider or start generation."
        return cast("models.OpenCreativeEnginesPageResult", self._request("open_creative_engines_page", input, account_id=account_id, timeout=timeout))

    def open_creative_engines_page_with_response(self, input: models.OpenCreativeEnginesPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenCreativeEnginesPageResult]:
        "Open the buyer Creative Engines Page. Optionally focus an engine, connection, or its secure setup control; the buyer starts setup in the Page, and this does not authorize a provider or start generation. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenCreativeEnginesPageResult], self._request_with_response("open_creative_engines_page", input, account_id=account_id, timeout=timeout))

    def open_advertisers_page(self, input: models.OpenAdvertisersPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenAdvertisersPageResult:
        "Open the Advertisers Page: every advertiser on this account with its campaign and draft counts and one next action each. Use it for \"show my advertisers\" or \"where do I start\"; the Page self-fetches, so do not recite the list. For a text answer use search(kind: \"advertiser\")."
        return cast("models.OpenAdvertisersPageResult", self._request("open_advertisers_page", input, account_id=account_id, timeout=timeout))

    def open_advertisers_page_with_response(self, input: models.OpenAdvertisersPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenAdvertisersPageResult]:
        "Open the Advertisers Page: every advertiser on this account with its campaign and draft counts and one next action each. Use it for \"show my advertisers\" or \"where do I start\"; the Page self-fetches, so do not recite the list. For a text answer use search(kind: \"advertiser\"). Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenAdvertisersPageResult], self._request_with_response("open_advertisers_page", input, account_id=account_id, timeout=timeout))

    def open_campaigns_page(self, input: models.OpenCampaignsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCampaignsPageResult:
        "Open the Campaigns Page: campaigns with status, flight, and budget; open one for its media buys and creatives. The Page self-fetches, so do not list campaigns in prose. advertiserId scopes to one advertiser; campaignId focuses one campaign. A draft's go-live review is open_campaign_receipt."
        return cast("models.OpenCampaignsPageResult", self._request("open_campaigns_page", input, account_id=account_id, timeout=timeout))

    def open_campaigns_page_with_response(self, input: models.OpenCampaignsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenCampaignsPageResult]:
        "Open the Campaigns Page: campaigns with status, flight, and budget; open one for its media buys and creatives. The Page self-fetches, so do not list campaigns in prose. advertiserId scopes to one advertiser; campaignId focuses one campaign. A draft's go-live review is open_campaign_receipt. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenCampaignsPageResult], self._request_with_response("open_campaigns_page", input, account_id=account_id, timeout=timeout))

    def open_campaign_receipt(self, input: models.OpenCampaignReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCampaignReceiptResult:
        "Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign."
        return cast("models.OpenCampaignReceiptResult", self._request("open_campaign_receipt", input, account_id=account_id, timeout=timeout))

    def open_campaign_receipt_with_response(self, input: models.OpenCampaignReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenCampaignReceiptResult]:
        "Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenCampaignReceiptResult], self._request_with_response("open_campaign_receipt", input, account_id=account_id, timeout=timeout))

    def upload_creative_asset(self, input: models.UploadCreativeAssetInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.UploadCreativeAssetResult:
        "Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative."
        return cast("models.UploadCreativeAssetResult", self._request("upload_creative_asset", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def upload_creative_asset_with_response(self, input: models.UploadCreativeAssetInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.UploadCreativeAssetResult]:
        "Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.UploadCreativeAssetResult], self._request_with_response("upload_creative_asset", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def open_approvals(self, input: models.OpenApprovalsInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenApprovalsResult:
        "Open the Approvals Page for reviews, assignments, routing, evidence, decisions, and forward recovery. Focus by exact media-buy identity or reviewRef; creativeId works only for one loaded version."
        return cast("models.OpenApprovalsResult", self._request("open_approvals", input, account_id=account_id, timeout=timeout))

    def open_approvals_with_response(self, input: models.OpenApprovalsInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenApprovalsResult]:
        "Open the Approvals Page for reviews, assignments, routing, evidence, decisions, and forward recovery. Focus by exact media-buy identity or reviewRef; creativeId works only for one loaded version. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenApprovalsResult], self._request_with_response("open_approvals", input, account_id=account_id, timeout=timeout))

    def open_creative_library(self, input: models.OpenCreativeLibraryInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.OpenCreativeLibraryResult:
        "Open Creative Library. Use search for a plain object answer. Composer needs campaignId; assembly needs no Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format."
        return cast("models.OpenCreativeLibraryResult", self._request("open_creative_library", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def open_creative_library_with_response(self, input: models.OpenCreativeLibraryInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.OpenCreativeLibraryResult]:
        "Open Creative Library. Use search for a plain object answer. Composer needs campaignId; assembly needs no Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenCreativeLibraryResult], self._request_with_response("open_creative_library", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def open_variant_gallery(self, input: models.OpenVariantGalleryInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenVariantGalleryResult:
        "Show a saved Creative Session’s variants (find via search/get kind creative_session). Not for generating new variants."
        return cast("models.OpenVariantGalleryResult", self._request("open_variant_gallery", input, account_id=account_id, timeout=timeout))

    def open_variant_gallery_with_response(self, input: models.OpenVariantGalleryInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenVariantGalleryResult]:
        "Show a saved Creative Session’s variants (find via search/get kind creative_session). Not for generating new variants. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenVariantGalleryResult], self._request_with_response("open_variant_gallery", input, account_id=account_id, timeout=timeout))

    def get_delivery(self, input: models.GetDeliveryInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetDeliveryResult:
        "Query seller delivery, stored or live buyer campaign delivery, or margin facts. Use live_campaign_delivery with one campaignId for the connected provider's current response. campaign_delivery preserves stored rows, totals, and paging. Buyer measurement is excluded."
        return cast("models.GetDeliveryResult", self._request("get_delivery", input, account_id=account_id, timeout=timeout))

    def get_delivery_with_response(self, input: models.GetDeliveryInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetDeliveryResult]:
        "Query seller delivery, stored or live buyer campaign delivery, or margin facts. Use live_campaign_delivery with one campaignId for the connected provider's current response. campaign_delivery preserves stored rows, totals, and paging. Buyer measurement is excluded. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetDeliveryResult], self._request_with_response("get_delivery", input, account_id=account_id, timeout=timeout))

    def test_creative_macros(self, input: models.TestCreativeMacrosInput, *, account_id: str | None = None, timeout: float | None = None) -> models.TestCreativeMacrosResult:
        "Dry-runs one tracker URL through exact raw input, canonical AdCP compilation, recipient translation, and deterministic synthetic substitution. Use it before preview or trafficking; unresolved required macros fail closed."
        return cast("models.TestCreativeMacrosResult", self._request("test_creative_macros", input, account_id=account_id, timeout=timeout))

    def test_creative_macros_with_response(self, input: models.TestCreativeMacrosInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.TestCreativeMacrosResult]:
        "Dry-runs one tracker URL through exact raw input, canonical AdCP compilation, recipient translation, and deterministic synthetic substitution. Use it before preview or trafficking; unresolved required macros fail closed. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.TestCreativeMacrosResult], self._request_with_response("test_creative_macros", input, account_id=account_id, timeout=timeout))

    def get_rfp_performance(self, input: models.GetRfpPerformanceInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetRfpPerformanceResult:
        "Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns."
        return cast("models.GetRfpPerformanceResult", self._request("get_rfp_performance", input, account_id=account_id, timeout=timeout))

    def get_rfp_performance_with_response(self, input: models.GetRfpPerformanceInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetRfpPerformanceResult]:
        "Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetRfpPerformanceResult], self._request_with_response("get_rfp_performance", input, account_id=account_id, timeout=timeout))

    def save_seller(self, input: models.SaveSellerInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveSellerResult:
        "Save Seller identity, capabilities, Marketplace, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, or a seller-controlled admission. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get(kind:\"distribution\")."
        return cast("models.SaveSellerResult", self._request("save_seller", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_seller_with_response(self, input: models.SaveSellerInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveSellerResult]:
        "Save Seller identity, capabilities, Marketplace, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, or a seller-controlled admission. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get(kind:\"distribution\"). Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveSellerResult], self._request_with_response("save_seller", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_agent(self, input: models.SaveAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAgentResult:
        "Confirm or correct one Sales Agent product mode. Owners change the Agent declaration and reject sourceId; a seller corrects its own binding on an unclaimed Agent and passes sourceId when several bindings match."
        return cast("models.SaveAgentResult", self._request("save_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_agent_with_response(self, input: models.SaveAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAgentResult]:
        "Confirm or correct one Sales Agent product mode. Owners change the Agent declaration and reject sourceId; a seller corrects its own binding on an unclaimed Agent and passes sourceId when several bindings match. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAgentResult], self._request_with_response("save_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_inventory_source(self, input: models.SaveInventorySourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveInventorySourceResult:
        "Create or update where a seller's inventory comes from. Pass `id` to change an existing source, omit it to add one. Credentials are never passed here — a source that needs a secret comes back with the state and the page that collects it."
        return cast("models.SaveInventorySourceResult", self._request("save_inventory_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_inventory_source_with_response(self, input: models.SaveInventorySourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveInventorySourceResult]:
        "Create or update where a seller's inventory comes from. Pass `id` to change an existing source, omit it to add one. Credentials are never passed here — a source that needs a secret comes back with the state and the page that collects it. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveInventorySourceResult], self._request_with_response("save_inventory_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_coverage(self, input: models.SaveCoverageInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCoverageResult:
        "Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, and `removeProperties` change named items only. Read authorization; never assume it."
        return cast("models.SaveCoverageResult", self._request("save_coverage", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_coverage_with_response(self, input: models.SaveCoverageInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCoverageResult]:
        "Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, and `removeProperties` change named items only. Read authorization; never assume it. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCoverageResult], self._request_with_response("save_coverage", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_material(self, input: models.SaveMaterialInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMaterialResult:
        "Register, revise, archive, restore, or reprocess seller Materials; manage candidate decisions and receipts; mark a slide, page, or sheet reusable only when it has no commercial figures (UNIT_NOT_REUSABLE_KIND rejects document containers, UNIT_CONTAINS_PRICING rejects priced units)."
        return cast("models.SaveMaterialResult", self._request("save_material", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_material_with_response(self, input: models.SaveMaterialInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveMaterialResult]:
        "Register, revise, archive, restore, or reprocess seller Materials; manage candidate decisions and receipts; mark a slide, page, or sheet reusable only when it has no commercial figures (UNIT_NOT_REUSABLE_KIND rejects document containers, UNIT_CONTAINS_PRICING rejects priced units). Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveMaterialResult], self._request_with_response("save_material", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_wholesale_product(self, input: models.SaveWholesaleProductInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveWholesaleProductResult:
        "Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not."
        return cast("models.SaveWholesaleProductResult", self._request("save_wholesale_product", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_wholesale_product_with_response(self, input: models.SaveWholesaleProductInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveWholesaleProductResult]:
        "Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveWholesaleProductResult], self._request_with_response("save_wholesale_product", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_media_kit(self, input: models.SaveMediaKitInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMediaKitResult:
        "Deprecated compatibility tool (\"listing\" is the modern term). It writes only the legacy businessProfile and does not update the canonical buyer-visible listing. New clients must read with `get({ kind: \"seller\", include: [\"listing\"] })` and write with `save_seller`."
        return cast("models.SaveMediaKitResult", self._request("save_media_kit", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_media_kit_with_response(self, input: models.SaveMediaKitInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveMediaKitResult]:
        "Deprecated compatibility tool (\"listing\" is the modern term). It writes only the legacy businessProfile and does not update the canonical buyer-visible listing. New clients must read with `get({ kind: \"seller\", include: [\"listing\"] })` and write with `save_seller`. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveMediaKitResult], self._request_with_response("save_media_kit", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_playbook(self, input: models.SavePlaybookInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SavePlaybookResult:
        "Write how the seller sells. `active` creates and activates a new version in one step — no separate activate; the response names the version created and replaced. `pricing` replaces the whole fact list. `discounts` sets or removes brand/operator rules one by one. Halves never roll back each other."
        return cast("models.SavePlaybookResult", self._request("save_playbook", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_playbook_with_response(self, input: models.SavePlaybookInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SavePlaybookResult]:
        "Write how the seller sells. `active` creates and activates a new version in one step — no separate activate; the response names the version created and replaced. `pricing` replaces the whole fact list. `discounts` sets or removes brand/operator rules one by one. Halves never roll back each other. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SavePlaybookResult], self._request_with_response("save_playbook", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_business_rules(self, input: models.SaveBusinessRulesInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBusinessRulesResult:
        "Write seller AI Business Rules. Policy content needs an account admin and both policy fields. Approval auto needs acknowledgeNoHumanReview."
        return cast("models.SaveBusinessRulesResult", self._request("save_business_rules", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_business_rules_with_response(self, input: models.SaveBusinessRulesInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveBusinessRulesResult]:
        "Write seller AI Business Rules. Policy content needs an account admin and both policy fields. Approval auto needs acknowledgeNoHumanReview. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveBusinessRulesResult], self._request_with_response("save_business_rules", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser_instructions(self, input: models.SaveAdvertiserInstructionsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserInstructionsResult:
        "Save seller notes and instructions for an exact brand-domain × operator-domain pair. Configuration does not verify the registry; discounts, source routing, sponsored access, and buyer-account trust are read-only."
        return cast("models.SaveAdvertiserInstructionsResult", self._request("save_advertiser_instructions", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser_instructions_with_response(self, input: models.SaveAdvertiserInstructionsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAdvertiserInstructionsResult]:
        "Save seller notes and instructions for an exact brand-domain × operator-domain pair. Configuration does not verify the registry; discounts, source routing, sponsored access, and buyer-account trust are read-only. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAdvertiserInstructionsResult], self._request_with_response("save_advertiser_instructions", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_signal(self, input: models.SaveSignalInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveSignalResult:
        "Create, replace, or archive a signal. Managed writes need a complete draft; read before updates. Without sourceId, writes the seller catalog."
        return cast("models.SaveSignalResult", self._request("save_signal", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_signal_with_response(self, input: models.SaveSignalInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveSignalResult]:
        "Create, replace, or archive a signal. Managed writes need a complete draft; read before updates. Without sourceId, writes the seller catalog. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveSignalResult], self._request_with_response("save_signal", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_work_item(self, input: models.SaveWorkItemInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveWorkItemResult:
        "Decide a creative or media-buy approval, or complete a modular-source follow-up. Repeats preserve evidence; retry, evaluation, and reassignment stay on the approvals Page."
        return cast("models.SaveWorkItemResult", self._request("save_work_item", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_work_item_with_response(self, input: models.SaveWorkItemInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveWorkItemResult]:
        "Decide a creative or media-buy approval, or complete a modular-source follow-up. Repeats preserve evidence; retry, evaluation, and reassignment stay on the approvals Page. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveWorkItemResult], self._request_with_response("save_work_item", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_rfp(self, input: models.SaveRfpInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveRfpResult:
        "Save RFPs and turns: imported origins, typed feedback, response pairs, endorsement, and proposal-file requests."
        return cast("models.SaveRfpResult", self._request("save_rfp", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_rfp_with_response(self, input: models.SaveRfpInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveRfpResult]:
        "Save RFPs and turns: imported origins, typed feedback, response pairs, endorsement, and proposal-file requests. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveRfpResult], self._request_with_response("save_rfp", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser(self, input: models.SaveAdvertiserInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserResult:
        "Save an advertiser or its mappings. `needs_input` = ask the buyer; never recreate to change currency. Use identityContract:confirmed-v1 for brand corrections. resolveBrand looks up public branding. Guide: /v2/setup/v3/identity-setup."
        return cast("models.SaveAdvertiserResult", self._request("save_advertiser", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser_with_response(self, input: models.SaveAdvertiserInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAdvertiserResult]:
        "Save an advertiser or its mappings. `needs_input` = ask the buyer; never recreate to change currency. Use identityContract:confirmed-v1 for brand corrections. resolveBrand looks up public branding. Guide: /v2/setup/v3/identity-setup. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAdvertiserResult], self._request_with_response("save_advertiser", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_buyer_operator(self, input: models.SaveBuyerOperatorInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBuyerOperatorResult:
        "Save buyer commercial identity. Read get_status; use identityContract:confirmed-v1 for preview and confirmation. Guide: /v2/setup/v3/identity-setup."
        return cast("models.SaveBuyerOperatorResult", self._request("save_buyer_operator", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_buyer_operator_with_response(self, input: models.SaveBuyerOperatorInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveBuyerOperatorResult]:
        "Save buyer commercial identity. Read get_status; use identityContract:confirmed-v1 for preview and confirmation. Guide: /v2/setup/v3/identity-setup. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveBuyerOperatorResult], self._request_with_response("save_buyer_operator", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_buyer_agent(self, input: models.SaveBuyerAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBuyerAgentResult:
        "Create, rename, reconcile access, change lifecycle, or prepare a human credential handoff for one buyer agent per call."
        return cast("models.SaveBuyerAgentResult", self._request("save_buyer_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_buyer_agent_with_response(self, input: models.SaveBuyerAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveBuyerAgentResult]:
        "Create, rename, reconcile access, change lifecycle, or prepare a human credential handoff for one buyer agent per call. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveBuyerAgentResult], self._request_with_response("save_buyer_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_directed_campaign_subscription(self, input: models.SaveDirectedCampaignSubscriptionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveDirectedCampaignSubscriptionResult:
        "Subscribe to a connected seller's directed campaigns, mirroring its media buys into this buyer's view. Set `unsubscribe: true` to remove the subscription and retire mirrored campaigns. Requires a mapped seller account and reachable advertiser."
        return cast("models.SaveDirectedCampaignSubscriptionResult", self._request("save_directed_campaign_subscription", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_directed_campaign_subscription_with_response(self, input: models.SaveDirectedCampaignSubscriptionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveDirectedCampaignSubscriptionResult]:
        "Subscribe to a connected seller's directed campaigns, mirroring its media buys into this buyer's view. Set `unsubscribe: true` to remove the subscription and retire mirrored campaigns. Requires a mapped seller account and reachable advertiser. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveDirectedCampaignSubscriptionResult], self._request_with_response("save_directed_campaign_subscription", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_audience(self, input: models.SaveAudienceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAudienceResult:
        "Sync first-party CRM audiences for a buyer advertiser. Each audiences[] item may add, remove, or delete members. Returns an operationId; use get(kind: audience, advertiserId: \"...\") to read match status after it settles."
        return cast("models.SaveAudienceResult", self._request("save_audience", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_audience_with_response(self, input: models.SaveAudienceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAudienceResult]:
        "Sync first-party CRM audiences for a buyer advertiser. Each audiences[] item may add, remove, or delete members. Returns an operationId; use get(kind: audience, advertiserId: \"...\") to read match status after it settles. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAudienceResult], self._request_with_response("save_audience", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_campaign(self, input: models.SaveCampaignInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCampaignResult:
        "Save a campaign. Create needs advertiserId and name; flight and budget are optional. Split inventory choices into separate media buys; presets expand dimensions. To launch, set desiredPhase: active with confirmLaunch: true; omit confirmation to preview. Cancellation never cancels media buys."
        return cast("models.SaveCampaignResult", self._request("save_campaign", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_campaign_with_response(self, input: models.SaveCampaignInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCampaignResult]:
        "Save a campaign. Create needs advertiserId and name; flight and budget are optional. Split inventory choices into separate media buys; presets expand dimensions. To launch, set desiredPhase: active with confirmLaunch: true; omit confirmation to preview. Cancellation never cancels media buys. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCampaignResult], self._request_with_response("save_campaign", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_catalog(self, input: models.SaveCatalogInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCatalogResult:
        "Create or replace one flat catalog declaration by catalogId, or archive it with isArchived. URL saves refetch the feed."
        return cast("models.SaveCatalogResult", self._request("save_catalog", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_catalog_with_response(self, input: models.SaveCatalogInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCatalogResult]:
        "Create or replace one flat catalog declaration by catalogId, or archive it with isArchived. URL saves refetch the feed. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCatalogResult], self._request_with_response("save_catalog", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_event_source(self, input: models.SaveEventSourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveEventSourceResult:
        "Create, change, archive, or restore up to 50 advertiser conversion event sources (pixels, server feeds). Each entry is keyed by eventSourceId and succeeds or fails alone. Setup is not proof events flow: check health with get, then use eventSourceId in an optimization goal."
        return cast("models.SaveEventSourceResult", self._request("save_event_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_event_source_with_response(self, input: models.SaveEventSourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveEventSourceResult]:
        "Create, change, archive, or restore up to 50 advertiser conversion event sources (pixels, server feeds). Each entry is keyed by eventSourceId and succeeds or fails alone. Setup is not proof events flow: check health with get, then use eventSourceId in an optimization goal. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveEventSourceResult], self._request_with_response("save_event_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_dimension(self, input: models.SaveDimensionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveDimensionResult:
        "Create a dimension, or update an existing dimension by its id. Tags is built in and open. Labels belong only to objects in appliesTo."
        return cast("models.SaveDimensionResult", self._request("save_dimension", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_dimension_with_response(self, input: models.SaveDimensionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveDimensionResult]:
        "Create a dimension, or update an existing dimension by its id. Tags is built in and open. Labels belong only to objects in appliesTo. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveDimensionResult], self._request_with_response("save_dimension", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_property_list(self, input: models.SavePropertyListInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SavePropertyListResult:
        "Create, update, archive, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists."
        return cast("models.SavePropertyListResult", self._request("save_property_list", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_property_list_with_response(self, input: models.SavePropertyListInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SavePropertyListResult]:
        "Create, update, archive, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SavePropertyListResult], self._request_with_response("save_property_list", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative(self, input: models.SaveCreativeInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeResult:
        "Save creative in advertiserId/campaignId with name, message, assets, clickUrl, social, sourceAssetRef/sourceAssets. Use exactly one format selector: formatKind/formatParams, creativeFormatId, formatOptionRef. Supplied content/assets only; generate new media (radio spots) via save_creative_session."
        return cast("models.SaveCreativeResult", self._request("save_creative", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative_with_response(self, input: models.SaveCreativeInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCreativeResult]:
        "Save creative in advertiserId/campaignId with name, message, assets, clickUrl, social, sourceAssetRef/sourceAssets. Use exactly one format selector: formatKind/formatParams, creativeFormatId, formatOptionRef. Supplied content/assets only; generate new media (radio spots) via save_creative_session. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCreativeResult], self._request_with_response("save_creative", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative_collection(self, input: models.SaveCreativeCollectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeCollectionResult:
        "Manage collections. Create with one owner and name: campaignId or advertiserId. Only advertiser mutations of an existing collection need expectedUpdatedAt; campaign writes and creates do not. isArchived archives or restores advertiser collections."
        return cast("models.SaveCreativeCollectionResult", self._request("save_creative_collection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative_collection_with_response(self, input: models.SaveCreativeCollectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCreativeCollectionResult]:
        "Manage collections. Create with one owner and name: campaignId or advertiserId. Only advertiser mutations of an existing collection need expectedUpdatedAt; campaign writes and creates do not. isArchived archives or restores advertiser collections. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCreativeCollectionResult], self._request_with_response("save_creative_collection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative_session(self, input: models.SaveCreativeSessionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeSessionResult:
        "Save a Creative Session to generate new image, hosted video, or voice/audio (radio spots, voiceovers) from a brief, plus selection, approval, finalisation, or Library promotion. Creative Engines is required; use save_creative for supplied content and assets. Never generates variants."
        return cast("models.SaveCreativeSessionResult", self._request("save_creative_session", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative_session_with_response(self, input: models.SaveCreativeSessionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCreativeSessionResult]:
        "Save a Creative Session to generate new image, hosted video, or voice/audio (radio spots, voiceovers) from a brief, plus selection, approval, finalisation, or Library promotion. Creative Engines is required; use save_creative for supplied content and assets. Never generates variants. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCreativeSessionResult], self._request_with_response("save_creative_session", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def generate_variants(self, input: models.GenerateVariantsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.GenerateVariantsResult:
        "Generate or refine new image, hosted video, or voice/audio (radio spots, voiceovers) from a saved Creative Engines brief. Reuse actionKey for an identical retry."
        return cast("models.GenerateVariantsResult", self._request("generate_variants", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def generate_variants_with_response(self, input: models.GenerateVariantsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.GenerateVariantsResult]:
        "Generate or refine new image, hosted video, or voice/audio (radio spots, voiceovers) from a saved Creative Engines brief. Reuse actionKey for an identical retry. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GenerateVariantsResult], self._request_with_response("generate_variants", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_media_buy(self, input: models.SaveMediaBuyInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMediaBuyResult:
        "Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit buy/product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates."
        return cast("models.SaveMediaBuyResult", self._request("save_media_buy", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_media_buy_with_response(self, input: models.SaveMediaBuyInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveMediaBuyResult]:
        "Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit buy/product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveMediaBuyResult], self._request_with_response("save_media_buy", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def request_proposals(self, input: models.RequestProposalsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RequestProposalsResult:
        "Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true."
        return cast("models.RequestProposalsResult", self._request("request_proposals", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def request_proposals_with_response(self, input: models.RequestProposalsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.RequestProposalsResult]:
        "Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.RequestProposalsResult], self._request_with_response("request_proposals", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

class AsyncApostra(AsyncTransport):
    async def get_v3_public_document_revision_sections(self, input: models.GetV3PublicDocumentRevisionSectionsInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetV3PublicDocumentRevisionSectionsResult:
        "Read a bounded public immutable document revision"
        return cast("models.GetV3PublicDocumentRevisionSectionsResult", await self._request("getV3PublicDocumentRevisionSections", input, account_id=account_id, timeout=timeout))

    async def get_v3_public_document_revision_sections_with_response(self, input: models.GetV3PublicDocumentRevisionSectionsInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetV3PublicDocumentRevisionSectionsResult]:
        "Read a bounded public immutable document revision Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetV3PublicDocumentRevisionSectionsResult], await self._request_with_response("getV3PublicDocumentRevisionSections", input, account_id=account_id, timeout=timeout))

    async def download_v3_public_document_revision(self, input: models.DownloadV3PublicDocumentRevisionInput, *, account_id: str | None = None, timeout: float | None = None) -> bytes:
        "Download a public immutable document revision"
        return cast("bytes", await self._request("downloadV3PublicDocumentRevision", input, account_id=account_id, timeout=timeout))

    async def download_v3_public_document_revision_with_response(self, input: models.DownloadV3PublicDocumentRevisionInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[bytes]:
        "Download a public immutable document revision Returns the data together with response headers and request ID."
        return cast(ResponseDetails[bytes], await self._request_with_response("downloadV3PublicDocumentRevision", input, account_id=account_id, timeout=timeout))

    async def get_v3_public_mutation_receipt(self, input: models.GetV3PublicMutationReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetV3PublicMutationReceiptResult:
        "Read the state of a V3 HTTP write receipt"
        return cast("models.GetV3PublicMutationReceiptResult", await self._request("getV3PublicMutationReceipt", input, account_id=account_id, timeout=timeout))

    async def get_v3_public_mutation_receipt_with_response(self, input: models.GetV3PublicMutationReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetV3PublicMutationReceiptResult]:
        "Read the state of a V3 HTTP write receipt Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetV3PublicMutationReceiptResult], await self._request_with_response("getV3PublicMutationReceipt", input, account_id=account_id, timeout=timeout))

    async def get_status(self, input: models.GetStatusInput = {}, *, account_id: str | None = None, timeout: float | None = None) -> models.GetStatusResult:
        "Current account, state, blockers, exact fixes, and reachable accounts. For seller demand, use it to tell whether readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand."
        return cast("models.GetStatusResult", await self._request("get_status", input, account_id=account_id, timeout=timeout))

    async def get_status_with_response(self, input: models.GetStatusInput = {}, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetStatusResult]:
        "Current account, state, blockers, exact fixes, and reachable accounts. For seller demand, use it to tell whether readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetStatusResult], await self._request_with_response("get_status", input, account_id=account_id, timeout=timeout))

    async def refresh_inventory_source_health(self, input: models.RefreshInventorySourceHealthInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RefreshInventorySourceHealthResult:
        "Rechecks one external sales-agent source with no-spend get_products. Returns evidence IDs and seller readiness; no source configuration or media buy."
        return cast("models.RefreshInventorySourceHealthResult", await self._request("refresh_inventory_source_health", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def refresh_inventory_source_health_with_response(self, input: models.RefreshInventorySourceHealthInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.RefreshInventorySourceHealthResult]:
        "Rechecks one external sales-agent source with no-spend get_products. Returns evidence IDs and seller readiness; no source configuration or media buy. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.RefreshInventorySourceHealthResult], await self._request_with_response("refresh_inventory_source_health", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_account(self, input: models.SaveAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAccountResult:
        "Rename an existing direct child Account or update settings.company. Never provisions, archives, or changes owners or members; use Account settings for access changes."
        return cast("models.SaveAccountResult", await self._request("save_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_account_with_response(self, input: models.SaveAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAccountResult]:
        "Rename an existing direct child Account or update settings.company. Never provisions, archives, or changes owners or members; use Account settings for access changes. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAccountResult], await self._request_with_response("save_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def review_buyer_child_account(self, input: models.ReviewBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None) -> models.ReviewBuyerChildAccountResult:
        "Review a Buyer child under the selected Organization: name, role, capacity, plan coverage, operator, inherited access and other effects. Read-only; nothing is created. Show the review to the person, then call request_buyer_child_account."
        return cast("models.ReviewBuyerChildAccountResult", await self._request("review_buyer_child_account", input, account_id=account_id, timeout=timeout))

    async def review_buyer_child_account_with_response(self, input: models.ReviewBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.ReviewBuyerChildAccountResult]:
        "Review a Buyer child under the selected Organization: name, role, capacity, plan coverage, operator, inherited access and other effects. Read-only; nothing is created. Show the review to the person, then call request_buyer_child_account. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.ReviewBuyerChildAccountResult], await self._request_with_response("review_buyer_child_account", input, account_id=account_id, timeout=timeout))

    async def request_buyer_child_account(self, input: models.RequestBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RequestBuyerChildAccountResult:
        "Request a Buyer child under the selected Organization. Nothing is created until an Organization administrator approves it on our site; the result is approval_required with a link to show the person. Repeat with the same idempotencyKey and name for the outcome."
        return cast("models.RequestBuyerChildAccountResult", await self._request("request_buyer_child_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def request_buyer_child_account_with_response(self, input: models.RequestBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.RequestBuyerChildAccountResult]:
        "Request a Buyer child under the selected Organization. Nothing is created until an Organization administrator approves it on our site; the result is approval_required with a link to show the person. Repeat with the same idempotencyKey and name for the outcome. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.RequestBuyerChildAccountResult], await self._request_with_response("request_buyer_child_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_ask(self, input: models.SaveAskInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAskResult:
        "File or update a typed ask in the Apostra Support workflow; returns askId. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first."
        return cast("models.SaveAskResult", await self._request("save_ask", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_ask_with_response(self, input: models.SaveAskInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAskResult]:
        "File or update a typed ask in the Apostra Support workflow; returns askId. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAskResult], await self._request_with_response("save_ask", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_billing(self, input: models.SaveBillingInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBillingResult:
        "Accept current Terms, choose the payment terms sellers are asked for, or manage payment authority. Card setup uses a confirmed hosted link; card data never enters MCP."
        return cast("models.SaveBillingResult", await self._request("save_billing", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_billing_with_response(self, input: models.SaveBillingInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveBillingResult]:
        "Accept current Terms, choose the payment terms sellers are asked for, or manage payment authority. Card setup uses a confirmed hosted link; card data never enters MCP. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveBillingResult], await self._request_with_response("save_billing", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_notification_config(self, input: models.SaveNotificationConfigInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveNotificationConfigResult:
        "Create or update a notification subscription: scope, content, routes; no trigger type is creatable yet, no delivery policy yet. Omit subscriptionId to create, supply it to patch. Managed subscriptions are editable only within their mutability. Credentials belong to save_integration."
        return cast("models.SaveNotificationConfigResult", await self._request("save_notification_config", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_notification_config_with_response(self, input: models.SaveNotificationConfigInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveNotificationConfigResult]:
        "Create or update a notification subscription: scope, content, routes; no trigger type is creatable yet, no delivery policy yet. Omit subscriptionId to create, supply it to patch. Managed subscriptions are editable only within their mutability. Credentials belong to save_integration. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveNotificationConfigResult], await self._request_with_response("save_notification_config", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser_grant(self, input: models.SaveAdvertiserGrantInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserGrantResult:
        "Invite another Organization to exact advertisers, accept/reject an invitation, or revoke a grant. Limited beta: eligible Organization, entitlement, server-side exposure, and direct human-admin authority are required."
        return cast("models.SaveAdvertiserGrantResult", await self._request("save_advertiser_grant", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser_grant_with_response(self, input: models.SaveAdvertiserGrantInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAdvertiserGrantResult]:
        "Invite another Organization to exact advertisers, accept/reject an invitation, or revoke a grant. Limited beta: eligible Organization, entitlement, server-side exposure, and direct human-admin authority are required. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAdvertiserGrantResult], await self._request_with_response("save_advertiser_grant", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def search(self, input: models.SearchInput, *, account_id: str | None = None, timeout: float | None = None) -> models.SearchResult:
        "Find objects in this account, or answer questions from the docs. Pass kind to list one object type, query to match text, or both. Before a multi-step task, search kind skill for a workflow. Reread a docs hit with its document (and revision, for agreements) before you cite it."
        return cast("models.SearchResult", await self._request("search", input, account_id=account_id, timeout=timeout))

    async def search_with_response(self, input: models.SearchInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.SearchResult]:
        "Find objects in this account, or answer questions from the docs. Pass kind to list one object type, query to match text, or both. Before a multi-step task, search kind skill for a workflow. Reread a docs hit with its document (and revision, for agreements) before you cite it. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SearchResult], await self._request_with_response("search", input, account_id=account_id, timeout=timeout))

    async def get(self, input: models.GetInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetResult:
        "Read one object by kind plus the id that search returned, or an account singleton with no id. Never guess an id. include adds detail; each include value works only for the kinds that serve it."
        return cast("models.GetResult", await self._request("get", input, account_id=account_id, timeout=timeout))

    async def get_with_response(self, input: models.GetInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetResult]:
        "Read one object by kind plus the id that search returned, or an account singleton with no id. Never guess an id. include adds detail; each include value works only for the kinds that serve it. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetResult], await self._request_with_response("get", input, account_id=account_id, timeout=timeout))

    async def save_connection(self, input: models.SaveConnectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveConnectionResult:
        "Manage seller or creative-engine authorization, accounts and advertiser mappings. Seller-only: reporting, selection, billing, policy, activation."
        return cast("models.SaveConnectionResult", await self._request("save_connection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_connection_with_response(self, input: models.SaveConnectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveConnectionResult]:
        "Manage seller or creative-engine authorization, accounts and advertiser mappings. Seller-only: reporting, selection, billing, policy, activation. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveConnectionResult], await self._request_with_response("save_connection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_library_request(self, input: models.SaveLibraryRequestInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveLibraryRequestResult:
        "Open a seller library request or close it with seller Material."
        return cast("models.SaveLibraryRequestResult", await self._request("save_library_request", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_library_request_with_response(self, input: models.SaveLibraryRequestInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveLibraryRequestResult]:
        "Open a seller library request or close it with seller Material. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveLibraryRequestResult], await self._request_with_response("save_library_request", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def open_page(self, input: models.OpenPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenPageResult:
        "Open a compatibility Page. source_diagnostics can create or attach the Agent. External hosts may return text. Credentials and authority changes remain human ceremonies."
        return cast("models.OpenPageResult", await self._request("open_page", input, account_id=account_id, timeout=timeout))

    async def open_page_with_response(self, input: models.OpenPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenPageResult]:
        "Open a compatibility Page. source_diagnostics can create or attach the Agent. External hosts may return text. Credentials and authority changes remain human ceremonies. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenPageResult], await self._request_with_response("open_page", input, account_id=account_id, timeout=timeout))

    async def open_proposal_pass(self, input: models.OpenProposalPassInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenProposalPassResult:
        "Open Proposal Pass on one exact immutable RFP turn. Supply the matching rfpId and turnId from save_rfp or get; the Page loads the private response itself."
        return cast("models.OpenProposalPassResult", await self._request("open_proposal_pass", input, account_id=account_id, timeout=timeout))

    async def open_proposal_pass_with_response(self, input: models.OpenProposalPassInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenProposalPassResult]:
        "Open Proposal Pass on one exact immutable RFP turn. Supply the matching rfpId and turnId from save_rfp or get; the Page loads the private response itself. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenProposalPassResult], await self._request_with_response("open_proposal_pass", input, account_id=account_id, timeout=timeout))

    async def open_media_buys_page(self, input: models.OpenMediaBuysPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenMediaBuysPageResult:
        "Open the Seller Media Buys Page. Optionally focus one seller-owned account relationship and its buys or creatives; the Page self-fetches."
        return cast("models.OpenMediaBuysPageResult", await self._request("open_media_buys_page", input, account_id=account_id, timeout=timeout))

    async def open_media_buys_page_with_response(self, input: models.OpenMediaBuysPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenMediaBuysPageResult]:
        "Open the Seller Media Buys Page. Optionally focus one seller-owned account relationship and its buys or creatives; the Page self-fetches. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenMediaBuysPageResult], await self._request_with_response("open_media_buys_page", input, account_id=account_id, timeout=timeout))

    async def open_seller_dashboard(self, input: models.OpenSellerDashboardInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenSellerDashboardResult:
        "Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches."
        return cast("models.OpenSellerDashboardResult", await self._request("open_seller_dashboard", input, account_id=account_id, timeout=timeout))

    async def open_seller_dashboard_with_response(self, input: models.OpenSellerDashboardInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenSellerDashboardResult]:
        "Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenSellerDashboardResult], await self._request_with_response("open_seller_dashboard", input, account_id=account_id, timeout=timeout))

    async def open_agents_page(self, input: models.OpenAgentsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenAgentsPageResult:
        "Open Build an agent for this Developer account."
        return cast("models.OpenAgentsPageResult", await self._request("open_agents_page", input, account_id=account_id, timeout=timeout))

    async def open_agents_page_with_response(self, input: models.OpenAgentsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenAgentsPageResult]:
        "Open Build an agent for this Developer account. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenAgentsPageResult], await self._request_with_response("open_agents_page", input, account_id=account_id, timeout=timeout))

    async def open_agent_page(self, input: models.OpenAgentPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenAgentPageResult:
        "Open one agent owned by this Developer account."
        return cast("models.OpenAgentPageResult", await self._request("open_agent_page", input, account_id=account_id, timeout=timeout))

    async def open_agent_page_with_response(self, input: models.OpenAgentPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenAgentPageResult]:
        "Open one agent owned by this Developer account. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenAgentPageResult], await self._request_with_response("open_agent_page", input, account_id=account_id, timeout=timeout))

    async def open_connections_page(self, input: models.OpenConnectionsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenConnectionsPageResult:
        "Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction \"connect\" opens that media partner at connection setup without mutating until the user confirms."
        return cast("models.OpenConnectionsPageResult", await self._request("open_connections_page", input, account_id=account_id, timeout=timeout))

    async def open_connections_page_with_response(self, input: models.OpenConnectionsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenConnectionsPageResult]:
        "Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction \"connect\" opens that media partner at connection setup without mutating until the user confirms. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenConnectionsPageResult], await self._request_with_response("open_connections_page", input, account_id=account_id, timeout=timeout))

    async def open_creative_engines_page(self, input: models.OpenCreativeEnginesPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCreativeEnginesPageResult:
        "Open the buyer Creative Engines Page. Optionally focus an engine, connection, or its secure setup control; the buyer starts setup in the Page, and this does not authorize a provider or start generation."
        return cast("models.OpenCreativeEnginesPageResult", await self._request("open_creative_engines_page", input, account_id=account_id, timeout=timeout))

    async def open_creative_engines_page_with_response(self, input: models.OpenCreativeEnginesPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenCreativeEnginesPageResult]:
        "Open the buyer Creative Engines Page. Optionally focus an engine, connection, or its secure setup control; the buyer starts setup in the Page, and this does not authorize a provider or start generation. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenCreativeEnginesPageResult], await self._request_with_response("open_creative_engines_page", input, account_id=account_id, timeout=timeout))

    async def open_advertisers_page(self, input: models.OpenAdvertisersPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenAdvertisersPageResult:
        "Open the Advertisers Page: every advertiser on this account with its campaign and draft counts and one next action each. Use it for \"show my advertisers\" or \"where do I start\"; the Page self-fetches, so do not recite the list. For a text answer use search(kind: \"advertiser\")."
        return cast("models.OpenAdvertisersPageResult", await self._request("open_advertisers_page", input, account_id=account_id, timeout=timeout))

    async def open_advertisers_page_with_response(self, input: models.OpenAdvertisersPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenAdvertisersPageResult]:
        "Open the Advertisers Page: every advertiser on this account with its campaign and draft counts and one next action each. Use it for \"show my advertisers\" or \"where do I start\"; the Page self-fetches, so do not recite the list. For a text answer use search(kind: \"advertiser\"). Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenAdvertisersPageResult], await self._request_with_response("open_advertisers_page", input, account_id=account_id, timeout=timeout))

    async def open_campaigns_page(self, input: models.OpenCampaignsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCampaignsPageResult:
        "Open the Campaigns Page: campaigns with status, flight, and budget; open one for its media buys and creatives. The Page self-fetches, so do not list campaigns in prose. advertiserId scopes to one advertiser; campaignId focuses one campaign. A draft's go-live review is open_campaign_receipt."
        return cast("models.OpenCampaignsPageResult", await self._request("open_campaigns_page", input, account_id=account_id, timeout=timeout))

    async def open_campaigns_page_with_response(self, input: models.OpenCampaignsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenCampaignsPageResult]:
        "Open the Campaigns Page: campaigns with status, flight, and budget; open one for its media buys and creatives. The Page self-fetches, so do not list campaigns in prose. advertiserId scopes to one advertiser; campaignId focuses one campaign. A draft's go-live review is open_campaign_receipt. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenCampaignsPageResult], await self._request_with_response("open_campaigns_page", input, account_id=account_id, timeout=timeout))

    async def open_campaign_receipt(self, input: models.OpenCampaignReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCampaignReceiptResult:
        "Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign."
        return cast("models.OpenCampaignReceiptResult", await self._request("open_campaign_receipt", input, account_id=account_id, timeout=timeout))

    async def open_campaign_receipt_with_response(self, input: models.OpenCampaignReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenCampaignReceiptResult]:
        "Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenCampaignReceiptResult], await self._request_with_response("open_campaign_receipt", input, account_id=account_id, timeout=timeout))

    async def upload_creative_asset(self, input: models.UploadCreativeAssetInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.UploadCreativeAssetResult:
        "Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative."
        return cast("models.UploadCreativeAssetResult", await self._request("upload_creative_asset", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def upload_creative_asset_with_response(self, input: models.UploadCreativeAssetInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.UploadCreativeAssetResult]:
        "Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.UploadCreativeAssetResult], await self._request_with_response("upload_creative_asset", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def open_approvals(self, input: models.OpenApprovalsInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenApprovalsResult:
        "Open the Approvals Page for reviews, assignments, routing, evidence, decisions, and forward recovery. Focus by exact media-buy identity or reviewRef; creativeId works only for one loaded version."
        return cast("models.OpenApprovalsResult", await self._request("open_approvals", input, account_id=account_id, timeout=timeout))

    async def open_approvals_with_response(self, input: models.OpenApprovalsInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenApprovalsResult]:
        "Open the Approvals Page for reviews, assignments, routing, evidence, decisions, and forward recovery. Focus by exact media-buy identity or reviewRef; creativeId works only for one loaded version. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenApprovalsResult], await self._request_with_response("open_approvals", input, account_id=account_id, timeout=timeout))

    async def open_creative_library(self, input: models.OpenCreativeLibraryInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.OpenCreativeLibraryResult:
        "Open Creative Library. Use search for a plain object answer. Composer needs campaignId; assembly needs no Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format."
        return cast("models.OpenCreativeLibraryResult", await self._request("open_creative_library", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def open_creative_library_with_response(self, input: models.OpenCreativeLibraryInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.OpenCreativeLibraryResult]:
        "Open Creative Library. Use search for a plain object answer. Composer needs campaignId; assembly needs no Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenCreativeLibraryResult], await self._request_with_response("open_creative_library", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def open_variant_gallery(self, input: models.OpenVariantGalleryInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenVariantGalleryResult:
        "Show a saved Creative Session’s variants (find via search/get kind creative_session). Not for generating new variants."
        return cast("models.OpenVariantGalleryResult", await self._request("open_variant_gallery", input, account_id=account_id, timeout=timeout))

    async def open_variant_gallery_with_response(self, input: models.OpenVariantGalleryInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.OpenVariantGalleryResult]:
        "Show a saved Creative Session’s variants (find via search/get kind creative_session). Not for generating new variants. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.OpenVariantGalleryResult], await self._request_with_response("open_variant_gallery", input, account_id=account_id, timeout=timeout))

    async def get_delivery(self, input: models.GetDeliveryInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetDeliveryResult:
        "Query seller delivery, stored or live buyer campaign delivery, or margin facts. Use live_campaign_delivery with one campaignId for the connected provider's current response. campaign_delivery preserves stored rows, totals, and paging. Buyer measurement is excluded."
        return cast("models.GetDeliveryResult", await self._request("get_delivery", input, account_id=account_id, timeout=timeout))

    async def get_delivery_with_response(self, input: models.GetDeliveryInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetDeliveryResult]:
        "Query seller delivery, stored or live buyer campaign delivery, or margin facts. Use live_campaign_delivery with one campaignId for the connected provider's current response. campaign_delivery preserves stored rows, totals, and paging. Buyer measurement is excluded. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetDeliveryResult], await self._request_with_response("get_delivery", input, account_id=account_id, timeout=timeout))

    async def test_creative_macros(self, input: models.TestCreativeMacrosInput, *, account_id: str | None = None, timeout: float | None = None) -> models.TestCreativeMacrosResult:
        "Dry-runs one tracker URL through exact raw input, canonical AdCP compilation, recipient translation, and deterministic synthetic substitution. Use it before preview or trafficking; unresolved required macros fail closed."
        return cast("models.TestCreativeMacrosResult", await self._request("test_creative_macros", input, account_id=account_id, timeout=timeout))

    async def test_creative_macros_with_response(self, input: models.TestCreativeMacrosInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.TestCreativeMacrosResult]:
        "Dry-runs one tracker URL through exact raw input, canonical AdCP compilation, recipient translation, and deterministic synthetic substitution. Use it before preview or trafficking; unresolved required macros fail closed. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.TestCreativeMacrosResult], await self._request_with_response("test_creative_macros", input, account_id=account_id, timeout=timeout))

    async def get_rfp_performance(self, input: models.GetRfpPerformanceInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetRfpPerformanceResult:
        "Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns."
        return cast("models.GetRfpPerformanceResult", await self._request("get_rfp_performance", input, account_id=account_id, timeout=timeout))

    async def get_rfp_performance_with_response(self, input: models.GetRfpPerformanceInput, *, account_id: str | None = None, timeout: float | None = None) -> ResponseDetails[models.GetRfpPerformanceResult]:
        "Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GetRfpPerformanceResult], await self._request_with_response("get_rfp_performance", input, account_id=account_id, timeout=timeout))

    async def save_seller(self, input: models.SaveSellerInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveSellerResult:
        "Save Seller identity, capabilities, Marketplace, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, or a seller-controlled admission. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get(kind:\"distribution\")."
        return cast("models.SaveSellerResult", await self._request("save_seller", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_seller_with_response(self, input: models.SaveSellerInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveSellerResult]:
        "Save Seller identity, capabilities, Marketplace, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, or a seller-controlled admission. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get(kind:\"distribution\"). Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveSellerResult], await self._request_with_response("save_seller", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_agent(self, input: models.SaveAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAgentResult:
        "Confirm or correct one Sales Agent product mode. Owners change the Agent declaration and reject sourceId; a seller corrects its own binding on an unclaimed Agent and passes sourceId when several bindings match."
        return cast("models.SaveAgentResult", await self._request("save_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_agent_with_response(self, input: models.SaveAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAgentResult]:
        "Confirm or correct one Sales Agent product mode. Owners change the Agent declaration and reject sourceId; a seller corrects its own binding on an unclaimed Agent and passes sourceId when several bindings match. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAgentResult], await self._request_with_response("save_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_inventory_source(self, input: models.SaveInventorySourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveInventorySourceResult:
        "Create or update where a seller's inventory comes from. Pass `id` to change an existing source, omit it to add one. Credentials are never passed here — a source that needs a secret comes back with the state and the page that collects it."
        return cast("models.SaveInventorySourceResult", await self._request("save_inventory_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_inventory_source_with_response(self, input: models.SaveInventorySourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveInventorySourceResult]:
        "Create or update where a seller's inventory comes from. Pass `id` to change an existing source, omit it to add one. Credentials are never passed here — a source that needs a secret comes back with the state and the page that collects it. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveInventorySourceResult], await self._request_with_response("save_inventory_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_coverage(self, input: models.SaveCoverageInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCoverageResult:
        "Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, and `removeProperties` change named items only. Read authorization; never assume it."
        return cast("models.SaveCoverageResult", await self._request("save_coverage", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_coverage_with_response(self, input: models.SaveCoverageInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCoverageResult]:
        "Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, and `removeProperties` change named items only. Read authorization; never assume it. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCoverageResult], await self._request_with_response("save_coverage", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_material(self, input: models.SaveMaterialInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMaterialResult:
        "Register, revise, archive, restore, or reprocess seller Materials; manage candidate decisions and receipts; mark a slide, page, or sheet reusable only when it has no commercial figures (UNIT_NOT_REUSABLE_KIND rejects document containers, UNIT_CONTAINS_PRICING rejects priced units)."
        return cast("models.SaveMaterialResult", await self._request("save_material", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_material_with_response(self, input: models.SaveMaterialInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveMaterialResult]:
        "Register, revise, archive, restore, or reprocess seller Materials; manage candidate decisions and receipts; mark a slide, page, or sheet reusable only when it has no commercial figures (UNIT_NOT_REUSABLE_KIND rejects document containers, UNIT_CONTAINS_PRICING rejects priced units). Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveMaterialResult], await self._request_with_response("save_material", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_wholesale_product(self, input: models.SaveWholesaleProductInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveWholesaleProductResult:
        "Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not."
        return cast("models.SaveWholesaleProductResult", await self._request("save_wholesale_product", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_wholesale_product_with_response(self, input: models.SaveWholesaleProductInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveWholesaleProductResult]:
        "Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveWholesaleProductResult], await self._request_with_response("save_wholesale_product", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_media_kit(self, input: models.SaveMediaKitInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMediaKitResult:
        "Deprecated compatibility tool (\"listing\" is the modern term). It writes only the legacy businessProfile and does not update the canonical buyer-visible listing. New clients must read with `get({ kind: \"seller\", include: [\"listing\"] })` and write with `save_seller`."
        return cast("models.SaveMediaKitResult", await self._request("save_media_kit", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_media_kit_with_response(self, input: models.SaveMediaKitInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveMediaKitResult]:
        "Deprecated compatibility tool (\"listing\" is the modern term). It writes only the legacy businessProfile and does not update the canonical buyer-visible listing. New clients must read with `get({ kind: \"seller\", include: [\"listing\"] })` and write with `save_seller`. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveMediaKitResult], await self._request_with_response("save_media_kit", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_playbook(self, input: models.SavePlaybookInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SavePlaybookResult:
        "Write how the seller sells. `active` creates and activates a new version in one step — no separate activate; the response names the version created and replaced. `pricing` replaces the whole fact list. `discounts` sets or removes brand/operator rules one by one. Halves never roll back each other."
        return cast("models.SavePlaybookResult", await self._request("save_playbook", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_playbook_with_response(self, input: models.SavePlaybookInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SavePlaybookResult]:
        "Write how the seller sells. `active` creates and activates a new version in one step — no separate activate; the response names the version created and replaced. `pricing` replaces the whole fact list. `discounts` sets or removes brand/operator rules one by one. Halves never roll back each other. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SavePlaybookResult], await self._request_with_response("save_playbook", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_business_rules(self, input: models.SaveBusinessRulesInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBusinessRulesResult:
        "Write seller AI Business Rules. Policy content needs an account admin and both policy fields. Approval auto needs acknowledgeNoHumanReview."
        return cast("models.SaveBusinessRulesResult", await self._request("save_business_rules", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_business_rules_with_response(self, input: models.SaveBusinessRulesInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveBusinessRulesResult]:
        "Write seller AI Business Rules. Policy content needs an account admin and both policy fields. Approval auto needs acknowledgeNoHumanReview. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveBusinessRulesResult], await self._request_with_response("save_business_rules", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser_instructions(self, input: models.SaveAdvertiserInstructionsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserInstructionsResult:
        "Save seller notes and instructions for an exact brand-domain × operator-domain pair. Configuration does not verify the registry; discounts, source routing, sponsored access, and buyer-account trust are read-only."
        return cast("models.SaveAdvertiserInstructionsResult", await self._request("save_advertiser_instructions", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser_instructions_with_response(self, input: models.SaveAdvertiserInstructionsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAdvertiserInstructionsResult]:
        "Save seller notes and instructions for an exact brand-domain × operator-domain pair. Configuration does not verify the registry; discounts, source routing, sponsored access, and buyer-account trust are read-only. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAdvertiserInstructionsResult], await self._request_with_response("save_advertiser_instructions", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_signal(self, input: models.SaveSignalInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveSignalResult:
        "Create, replace, or archive a signal. Managed writes need a complete draft; read before updates. Without sourceId, writes the seller catalog."
        return cast("models.SaveSignalResult", await self._request("save_signal", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_signal_with_response(self, input: models.SaveSignalInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveSignalResult]:
        "Create, replace, or archive a signal. Managed writes need a complete draft; read before updates. Without sourceId, writes the seller catalog. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveSignalResult], await self._request_with_response("save_signal", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_work_item(self, input: models.SaveWorkItemInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveWorkItemResult:
        "Decide a creative or media-buy approval, or complete a modular-source follow-up. Repeats preserve evidence; retry, evaluation, and reassignment stay on the approvals Page."
        return cast("models.SaveWorkItemResult", await self._request("save_work_item", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_work_item_with_response(self, input: models.SaveWorkItemInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveWorkItemResult]:
        "Decide a creative or media-buy approval, or complete a modular-source follow-up. Repeats preserve evidence; retry, evaluation, and reassignment stay on the approvals Page. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveWorkItemResult], await self._request_with_response("save_work_item", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_rfp(self, input: models.SaveRfpInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveRfpResult:
        "Save RFPs and turns: imported origins, typed feedback, response pairs, endorsement, and proposal-file requests."
        return cast("models.SaveRfpResult", await self._request("save_rfp", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_rfp_with_response(self, input: models.SaveRfpInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveRfpResult]:
        "Save RFPs and turns: imported origins, typed feedback, response pairs, endorsement, and proposal-file requests. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveRfpResult], await self._request_with_response("save_rfp", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser(self, input: models.SaveAdvertiserInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserResult:
        "Save an advertiser or its mappings. `needs_input` = ask the buyer; never recreate to change currency. Use identityContract:confirmed-v1 for brand corrections. resolveBrand looks up public branding. Guide: /v2/setup/v3/identity-setup."
        return cast("models.SaveAdvertiserResult", await self._request("save_advertiser", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser_with_response(self, input: models.SaveAdvertiserInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAdvertiserResult]:
        "Save an advertiser or its mappings. `needs_input` = ask the buyer; never recreate to change currency. Use identityContract:confirmed-v1 for brand corrections. resolveBrand looks up public branding. Guide: /v2/setup/v3/identity-setup. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAdvertiserResult], await self._request_with_response("save_advertiser", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_buyer_operator(self, input: models.SaveBuyerOperatorInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBuyerOperatorResult:
        "Save buyer commercial identity. Read get_status; use identityContract:confirmed-v1 for preview and confirmation. Guide: /v2/setup/v3/identity-setup."
        return cast("models.SaveBuyerOperatorResult", await self._request("save_buyer_operator", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_buyer_operator_with_response(self, input: models.SaveBuyerOperatorInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveBuyerOperatorResult]:
        "Save buyer commercial identity. Read get_status; use identityContract:confirmed-v1 for preview and confirmation. Guide: /v2/setup/v3/identity-setup. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveBuyerOperatorResult], await self._request_with_response("save_buyer_operator", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_buyer_agent(self, input: models.SaveBuyerAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBuyerAgentResult:
        "Create, rename, reconcile access, change lifecycle, or prepare a human credential handoff for one buyer agent per call."
        return cast("models.SaveBuyerAgentResult", await self._request("save_buyer_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_buyer_agent_with_response(self, input: models.SaveBuyerAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveBuyerAgentResult]:
        "Create, rename, reconcile access, change lifecycle, or prepare a human credential handoff for one buyer agent per call. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveBuyerAgentResult], await self._request_with_response("save_buyer_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_directed_campaign_subscription(self, input: models.SaveDirectedCampaignSubscriptionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveDirectedCampaignSubscriptionResult:
        "Subscribe to a connected seller's directed campaigns, mirroring its media buys into this buyer's view. Set `unsubscribe: true` to remove the subscription and retire mirrored campaigns. Requires a mapped seller account and reachable advertiser."
        return cast("models.SaveDirectedCampaignSubscriptionResult", await self._request("save_directed_campaign_subscription", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_directed_campaign_subscription_with_response(self, input: models.SaveDirectedCampaignSubscriptionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveDirectedCampaignSubscriptionResult]:
        "Subscribe to a connected seller's directed campaigns, mirroring its media buys into this buyer's view. Set `unsubscribe: true` to remove the subscription and retire mirrored campaigns. Requires a mapped seller account and reachable advertiser. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveDirectedCampaignSubscriptionResult], await self._request_with_response("save_directed_campaign_subscription", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_audience(self, input: models.SaveAudienceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAudienceResult:
        "Sync first-party CRM audiences for a buyer advertiser. Each audiences[] item may add, remove, or delete members. Returns an operationId; use get(kind: audience, advertiserId: \"...\") to read match status after it settles."
        return cast("models.SaveAudienceResult", await self._request("save_audience", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_audience_with_response(self, input: models.SaveAudienceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveAudienceResult]:
        "Sync first-party CRM audiences for a buyer advertiser. Each audiences[] item may add, remove, or delete members. Returns an operationId; use get(kind: audience, advertiserId: \"...\") to read match status after it settles. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveAudienceResult], await self._request_with_response("save_audience", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_campaign(self, input: models.SaveCampaignInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCampaignResult:
        "Save a campaign. Create needs advertiserId and name; flight and budget are optional. Split inventory choices into separate media buys; presets expand dimensions. To launch, set desiredPhase: active with confirmLaunch: true; omit confirmation to preview. Cancellation never cancels media buys."
        return cast("models.SaveCampaignResult", await self._request("save_campaign", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_campaign_with_response(self, input: models.SaveCampaignInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCampaignResult]:
        "Save a campaign. Create needs advertiserId and name; flight and budget are optional. Split inventory choices into separate media buys; presets expand dimensions. To launch, set desiredPhase: active with confirmLaunch: true; omit confirmation to preview. Cancellation never cancels media buys. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCampaignResult], await self._request_with_response("save_campaign", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_catalog(self, input: models.SaveCatalogInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCatalogResult:
        "Create or replace one flat catalog declaration by catalogId, or archive it with isArchived. URL saves refetch the feed."
        return cast("models.SaveCatalogResult", await self._request("save_catalog", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_catalog_with_response(self, input: models.SaveCatalogInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCatalogResult]:
        "Create or replace one flat catalog declaration by catalogId, or archive it with isArchived. URL saves refetch the feed. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCatalogResult], await self._request_with_response("save_catalog", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_event_source(self, input: models.SaveEventSourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveEventSourceResult:
        "Create, change, archive, or restore up to 50 advertiser conversion event sources (pixels, server feeds). Each entry is keyed by eventSourceId and succeeds or fails alone. Setup is not proof events flow: check health with get, then use eventSourceId in an optimization goal."
        return cast("models.SaveEventSourceResult", await self._request("save_event_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_event_source_with_response(self, input: models.SaveEventSourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveEventSourceResult]:
        "Create, change, archive, or restore up to 50 advertiser conversion event sources (pixels, server feeds). Each entry is keyed by eventSourceId and succeeds or fails alone. Setup is not proof events flow: check health with get, then use eventSourceId in an optimization goal. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveEventSourceResult], await self._request_with_response("save_event_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_dimension(self, input: models.SaveDimensionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveDimensionResult:
        "Create a dimension, or update an existing dimension by its id. Tags is built in and open. Labels belong only to objects in appliesTo."
        return cast("models.SaveDimensionResult", await self._request("save_dimension", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_dimension_with_response(self, input: models.SaveDimensionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveDimensionResult]:
        "Create a dimension, or update an existing dimension by its id. Tags is built in and open. Labels belong only to objects in appliesTo. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveDimensionResult], await self._request_with_response("save_dimension", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_property_list(self, input: models.SavePropertyListInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SavePropertyListResult:
        "Create, update, archive, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists."
        return cast("models.SavePropertyListResult", await self._request("save_property_list", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_property_list_with_response(self, input: models.SavePropertyListInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SavePropertyListResult]:
        "Create, update, archive, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SavePropertyListResult], await self._request_with_response("save_property_list", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative(self, input: models.SaveCreativeInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeResult:
        "Save creative in advertiserId/campaignId with name, message, assets, clickUrl, social, sourceAssetRef/sourceAssets. Use exactly one format selector: formatKind/formatParams, creativeFormatId, formatOptionRef. Supplied content/assets only; generate new media (radio spots) via save_creative_session."
        return cast("models.SaveCreativeResult", await self._request("save_creative", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative_with_response(self, input: models.SaveCreativeInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCreativeResult]:
        "Save creative in advertiserId/campaignId with name, message, assets, clickUrl, social, sourceAssetRef/sourceAssets. Use exactly one format selector: formatKind/formatParams, creativeFormatId, formatOptionRef. Supplied content/assets only; generate new media (radio spots) via save_creative_session. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCreativeResult], await self._request_with_response("save_creative", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative_collection(self, input: models.SaveCreativeCollectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeCollectionResult:
        "Manage collections. Create with one owner and name: campaignId or advertiserId. Only advertiser mutations of an existing collection need expectedUpdatedAt; campaign writes and creates do not. isArchived archives or restores advertiser collections."
        return cast("models.SaveCreativeCollectionResult", await self._request("save_creative_collection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative_collection_with_response(self, input: models.SaveCreativeCollectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCreativeCollectionResult]:
        "Manage collections. Create with one owner and name: campaignId or advertiserId. Only advertiser mutations of an existing collection need expectedUpdatedAt; campaign writes and creates do not. isArchived archives or restores advertiser collections. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCreativeCollectionResult], await self._request_with_response("save_creative_collection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative_session(self, input: models.SaveCreativeSessionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeSessionResult:
        "Save a Creative Session to generate new image, hosted video, or voice/audio (radio spots, voiceovers) from a brief, plus selection, approval, finalisation, or Library promotion. Creative Engines is required; use save_creative for supplied content and assets. Never generates variants."
        return cast("models.SaveCreativeSessionResult", await self._request("save_creative_session", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative_session_with_response(self, input: models.SaveCreativeSessionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveCreativeSessionResult]:
        "Save a Creative Session to generate new image, hosted video, or voice/audio (radio spots, voiceovers) from a brief, plus selection, approval, finalisation, or Library promotion. Creative Engines is required; use save_creative for supplied content and assets. Never generates variants. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveCreativeSessionResult], await self._request_with_response("save_creative_session", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def generate_variants(self, input: models.GenerateVariantsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.GenerateVariantsResult:
        "Generate or refine new image, hosted video, or voice/audio (radio spots, voiceovers) from a saved Creative Engines brief. Reuse actionKey for an identical retry."
        return cast("models.GenerateVariantsResult", await self._request("generate_variants", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def generate_variants_with_response(self, input: models.GenerateVariantsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.GenerateVariantsResult]:
        "Generate or refine new image, hosted video, or voice/audio (radio spots, voiceovers) from a saved Creative Engines brief. Reuse actionKey for an identical retry. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.GenerateVariantsResult], await self._request_with_response("generate_variants", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_media_buy(self, input: models.SaveMediaBuyInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMediaBuyResult:
        "Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit buy/product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates."
        return cast("models.SaveMediaBuyResult", await self._request("save_media_buy", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_media_buy_with_response(self, input: models.SaveMediaBuyInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.SaveMediaBuyResult]:
        "Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit buy/product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.SaveMediaBuyResult], await self._request_with_response("save_media_buy", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def request_proposals(self, input: models.RequestProposalsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RequestProposalsResult:
        "Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true."
        return cast("models.RequestProposalsResult", await self._request("request_proposals", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def request_proposals_with_response(self, input: models.RequestProposalsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> ResponseDetails[models.RequestProposalsResult]:
        "Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true. Returns the data together with response headers and request ID."
        return cast(ResponseDetails[models.RequestProposalsResult], await self._request_with_response("request_proposals", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))
