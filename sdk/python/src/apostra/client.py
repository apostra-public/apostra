# Generated. Do not edit.
from typing import cast
from . import models
from .transport import SyncTransport, AsyncTransport

class Apostra(SyncTransport):
    def get_v3_public_document_revision_sections(self, input: models.GetV3PublicDocumentRevisionSectionsInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetV3PublicDocumentRevisionSectionsResult:
        return cast("models.GetV3PublicDocumentRevisionSectionsResult", self._request("getV3PublicDocumentRevisionSections", input, account_id=account_id, timeout=timeout))

    def download_v3_public_document_revision(self, input: models.DownloadV3PublicDocumentRevisionInput, *, account_id: str | None = None, timeout: float | None = None) -> bytes:
        return cast("bytes", self._request("downloadV3PublicDocumentRevision", input, account_id=account_id, timeout=timeout))

    def get_status(self, input: models.GetStatusInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetStatusResult:
        return cast("models.GetStatusResult", self._request("get_status", input, account_id=account_id, timeout=timeout))

    def refresh_inventory_source_health(self, input: models.RefreshInventorySourceHealthInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RefreshInventorySourceHealthResult:
        return cast("models.RefreshInventorySourceHealthResult", self._request("refresh_inventory_source_health", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_account(self, input: models.SaveAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAccountResult:
        return cast("models.SaveAccountResult", self._request("save_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def review_buyer_child_account(self, input: models.ReviewBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None) -> models.ReviewBuyerChildAccountResult:
        return cast("models.ReviewBuyerChildAccountResult", self._request("review_buyer_child_account", input, account_id=account_id, timeout=timeout))

    def request_buyer_child_account(self, input: models.RequestBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RequestBuyerChildAccountResult:
        return cast("models.RequestBuyerChildAccountResult", self._request("request_buyer_child_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_ask(self, input: models.SaveAskInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAskResult:
        return cast("models.SaveAskResult", self._request("save_ask", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_billing(self, input: models.SaveBillingInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBillingResult:
        return cast("models.SaveBillingResult", self._request("save_billing", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_notification_config(self, input: models.SaveNotificationConfigInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveNotificationConfigResult:
        return cast("models.SaveNotificationConfigResult", self._request("save_notification_config", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser_grant(self, input: models.SaveAdvertiserGrantInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserGrantResult:
        return cast("models.SaveAdvertiserGrantResult", self._request("save_advertiser_grant", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def search(self, input: models.SearchInput, *, account_id: str | None = None, timeout: float | None = None) -> models.SearchResult:
        return cast("models.SearchResult", self._request("search", input, account_id=account_id, timeout=timeout))

    def get(self, input: models.GetInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetResult:
        return cast("models.GetResult", self._request("get", input, account_id=account_id, timeout=timeout))

    def save_connection(self, input: models.SaveConnectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveConnectionResult:
        return cast("models.SaveConnectionResult", self._request("save_connection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_library_request(self, input: models.SaveLibraryRequestInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveLibraryRequestResult:
        return cast("models.SaveLibraryRequestResult", self._request("save_library_request", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def open_page(self, input: models.OpenPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenPageResult:
        return cast("models.OpenPageResult", self._request("open_page", input, account_id=account_id, timeout=timeout))

    def open_proposal_pass(self, input: models.OpenProposalPassInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenProposalPassResult:
        return cast("models.OpenProposalPassResult", self._request("open_proposal_pass", input, account_id=account_id, timeout=timeout))

    def open_media_buys_page(self, input: models.OpenMediaBuysPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenMediaBuysPageResult:
        return cast("models.OpenMediaBuysPageResult", self._request("open_media_buys_page", input, account_id=account_id, timeout=timeout))

    def open_connections_page(self, input: models.OpenConnectionsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenConnectionsPageResult:
        return cast("models.OpenConnectionsPageResult", self._request("open_connections_page", input, account_id=account_id, timeout=timeout))

    def open_creative_engines_page(self, input: models.OpenCreativeEnginesPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCreativeEnginesPageResult:
        return cast("models.OpenCreativeEnginesPageResult", self._request("open_creative_engines_page", input, account_id=account_id, timeout=timeout))

    def open_advertisers_page(self, input: models.OpenAdvertisersPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenAdvertisersPageResult:
        return cast("models.OpenAdvertisersPageResult", self._request("open_advertisers_page", input, account_id=account_id, timeout=timeout))

    def open_campaigns_page(self, input: models.OpenCampaignsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCampaignsPageResult:
        return cast("models.OpenCampaignsPageResult", self._request("open_campaigns_page", input, account_id=account_id, timeout=timeout))

    def open_campaign_receipt(self, input: models.OpenCampaignReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCampaignReceiptResult:
        return cast("models.OpenCampaignReceiptResult", self._request("open_campaign_receipt", input, account_id=account_id, timeout=timeout))

    def upload_creative_asset(self, input: models.UploadCreativeAssetInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.UploadCreativeAssetResult:
        return cast("models.UploadCreativeAssetResult", self._request("upload_creative_asset", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def open_approvals(self, input: models.OpenApprovalsInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenApprovalsResult:
        return cast("models.OpenApprovalsResult", self._request("open_approvals", input, account_id=account_id, timeout=timeout))

    def open_creative_library(self, input: models.OpenCreativeLibraryInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.OpenCreativeLibraryResult:
        return cast("models.OpenCreativeLibraryResult", self._request("open_creative_library", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def get_delivery(self, input: models.GetDeliveryInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetDeliveryResult:
        return cast("models.GetDeliveryResult", self._request("get_delivery", input, account_id=account_id, timeout=timeout))

    def test_creative_macros(self, input: models.TestCreativeMacrosInput, *, account_id: str | None = None, timeout: float | None = None) -> models.TestCreativeMacrosResult:
        return cast("models.TestCreativeMacrosResult", self._request("test_creative_macros", input, account_id=account_id, timeout=timeout))

    def get_rfp_performance(self, input: models.GetRfpPerformanceInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetRfpPerformanceResult:
        return cast("models.GetRfpPerformanceResult", self._request("get_rfp_performance", input, account_id=account_id, timeout=timeout))

    def save_seller(self, input: models.SaveSellerInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveSellerResult:
        return cast("models.SaveSellerResult", self._request("save_seller", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_inventory_source(self, input: models.SaveInventorySourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveInventorySourceResult:
        return cast("models.SaveInventorySourceResult", self._request("save_inventory_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_coverage(self, input: models.SaveCoverageInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCoverageResult:
        return cast("models.SaveCoverageResult", self._request("save_coverage", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_material(self, input: models.SaveMaterialInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMaterialResult:
        return cast("models.SaveMaterialResult", self._request("save_material", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_wholesale_product(self, input: models.SaveWholesaleProductInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveWholesaleProductResult:
        return cast("models.SaveWholesaleProductResult", self._request("save_wholesale_product", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_media_kit(self, input: models.SaveMediaKitInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMediaKitResult:
        return cast("models.SaveMediaKitResult", self._request("save_media_kit", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_playbook(self, input: models.SavePlaybookInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SavePlaybookResult:
        return cast("models.SavePlaybookResult", self._request("save_playbook", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_business_rules(self, input: models.SaveBusinessRulesInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBusinessRulesResult:
        return cast("models.SaveBusinessRulesResult", self._request("save_business_rules", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser_instructions(self, input: models.SaveAdvertiserInstructionsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserInstructionsResult:
        return cast("models.SaveAdvertiserInstructionsResult", self._request("save_advertiser_instructions", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_signal(self, input: models.SaveSignalInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveSignalResult:
        return cast("models.SaveSignalResult", self._request("save_signal", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_work_item(self, input: models.SaveWorkItemInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveWorkItemResult:
        return cast("models.SaveWorkItemResult", self._request("save_work_item", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_rfp(self, input: models.SaveRfpInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveRfpResult:
        return cast("models.SaveRfpResult", self._request("save_rfp", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_advertiser(self, input: models.SaveAdvertiserInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserResult:
        return cast("models.SaveAdvertiserResult", self._request("save_advertiser", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_buyer_operator(self, input: models.SaveBuyerOperatorInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBuyerOperatorResult:
        return cast("models.SaveBuyerOperatorResult", self._request("save_buyer_operator", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_buyer_agent(self, input: models.SaveBuyerAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBuyerAgentResult:
        return cast("models.SaveBuyerAgentResult", self._request("save_buyer_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_directed_campaign_subscription(self, input: models.SaveDirectedCampaignSubscriptionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveDirectedCampaignSubscriptionResult:
        return cast("models.SaveDirectedCampaignSubscriptionResult", self._request("save_directed_campaign_subscription", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_audience(self, input: models.SaveAudienceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAudienceResult:
        return cast("models.SaveAudienceResult", self._request("save_audience", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_campaign(self, input: models.SaveCampaignInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCampaignResult:
        return cast("models.SaveCampaignResult", self._request("save_campaign", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_catalog(self, input: models.SaveCatalogInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCatalogResult:
        return cast("models.SaveCatalogResult", self._request("save_catalog", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_measurement_source(self, input: models.SaveMeasurementSourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMeasurementSourceResult:
        return cast("models.SaveMeasurementSourceResult", self._request("save_measurement_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_event_source(self, input: models.SaveEventSourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveEventSourceResult:
        return cast("models.SaveEventSourceResult", self._request("save_event_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_dimension(self, input: models.SaveDimensionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveDimensionResult:
        return cast("models.SaveDimensionResult", self._request("save_dimension", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_property_list(self, input: models.SavePropertyListInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SavePropertyListResult:
        return cast("models.SavePropertyListResult", self._request("save_property_list", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative(self, input: models.SaveCreativeInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeResult:
        return cast("models.SaveCreativeResult", self._request("save_creative", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative_collection(self, input: models.SaveCreativeCollectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeCollectionResult:
        return cast("models.SaveCreativeCollectionResult", self._request("save_creative_collection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_creative_session(self, input: models.SaveCreativeSessionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeSessionResult:
        return cast("models.SaveCreativeSessionResult", self._request("save_creative_session", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def generate_variants(self, input: models.GenerateVariantsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.GenerateVariantsResult:
        return cast("models.GenerateVariantsResult", self._request("generate_variants", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def save_media_buy(self, input: models.SaveMediaBuyInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMediaBuyResult:
        return cast("models.SaveMediaBuyResult", self._request("save_media_buy", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    def request_proposals(self, input: models.RequestProposalsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RequestProposalsResult:
        return cast("models.RequestProposalsResult", self._request("request_proposals", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

class AsyncApostra(AsyncTransport):
    async def get_v3_public_document_revision_sections(self, input: models.GetV3PublicDocumentRevisionSectionsInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetV3PublicDocumentRevisionSectionsResult:
        return cast("models.GetV3PublicDocumentRevisionSectionsResult", await self._request("getV3PublicDocumentRevisionSections", input, account_id=account_id, timeout=timeout))

    async def download_v3_public_document_revision(self, input: models.DownloadV3PublicDocumentRevisionInput, *, account_id: str | None = None, timeout: float | None = None) -> bytes:
        return cast("bytes", await self._request("downloadV3PublicDocumentRevision", input, account_id=account_id, timeout=timeout))

    async def get_status(self, input: models.GetStatusInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetStatusResult:
        return cast("models.GetStatusResult", await self._request("get_status", input, account_id=account_id, timeout=timeout))

    async def refresh_inventory_source_health(self, input: models.RefreshInventorySourceHealthInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RefreshInventorySourceHealthResult:
        return cast("models.RefreshInventorySourceHealthResult", await self._request("refresh_inventory_source_health", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_account(self, input: models.SaveAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAccountResult:
        return cast("models.SaveAccountResult", await self._request("save_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def review_buyer_child_account(self, input: models.ReviewBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None) -> models.ReviewBuyerChildAccountResult:
        return cast("models.ReviewBuyerChildAccountResult", await self._request("review_buyer_child_account", input, account_id=account_id, timeout=timeout))

    async def request_buyer_child_account(self, input: models.RequestBuyerChildAccountInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RequestBuyerChildAccountResult:
        return cast("models.RequestBuyerChildAccountResult", await self._request("request_buyer_child_account", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_ask(self, input: models.SaveAskInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAskResult:
        return cast("models.SaveAskResult", await self._request("save_ask", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_billing(self, input: models.SaveBillingInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBillingResult:
        return cast("models.SaveBillingResult", await self._request("save_billing", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_notification_config(self, input: models.SaveNotificationConfigInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveNotificationConfigResult:
        return cast("models.SaveNotificationConfigResult", await self._request("save_notification_config", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser_grant(self, input: models.SaveAdvertiserGrantInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserGrantResult:
        return cast("models.SaveAdvertiserGrantResult", await self._request("save_advertiser_grant", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def search(self, input: models.SearchInput, *, account_id: str | None = None, timeout: float | None = None) -> models.SearchResult:
        return cast("models.SearchResult", await self._request("search", input, account_id=account_id, timeout=timeout))

    async def get(self, input: models.GetInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetResult:
        return cast("models.GetResult", await self._request("get", input, account_id=account_id, timeout=timeout))

    async def save_connection(self, input: models.SaveConnectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveConnectionResult:
        return cast("models.SaveConnectionResult", await self._request("save_connection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_library_request(self, input: models.SaveLibraryRequestInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveLibraryRequestResult:
        return cast("models.SaveLibraryRequestResult", await self._request("save_library_request", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def open_page(self, input: models.OpenPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenPageResult:
        return cast("models.OpenPageResult", await self._request("open_page", input, account_id=account_id, timeout=timeout))

    async def open_proposal_pass(self, input: models.OpenProposalPassInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenProposalPassResult:
        return cast("models.OpenProposalPassResult", await self._request("open_proposal_pass", input, account_id=account_id, timeout=timeout))

    async def open_media_buys_page(self, input: models.OpenMediaBuysPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenMediaBuysPageResult:
        return cast("models.OpenMediaBuysPageResult", await self._request("open_media_buys_page", input, account_id=account_id, timeout=timeout))

    async def open_connections_page(self, input: models.OpenConnectionsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenConnectionsPageResult:
        return cast("models.OpenConnectionsPageResult", await self._request("open_connections_page", input, account_id=account_id, timeout=timeout))

    async def open_creative_engines_page(self, input: models.OpenCreativeEnginesPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCreativeEnginesPageResult:
        return cast("models.OpenCreativeEnginesPageResult", await self._request("open_creative_engines_page", input, account_id=account_id, timeout=timeout))

    async def open_advertisers_page(self, input: models.OpenAdvertisersPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenAdvertisersPageResult:
        return cast("models.OpenAdvertisersPageResult", await self._request("open_advertisers_page", input, account_id=account_id, timeout=timeout))

    async def open_campaigns_page(self, input: models.OpenCampaignsPageInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCampaignsPageResult:
        return cast("models.OpenCampaignsPageResult", await self._request("open_campaigns_page", input, account_id=account_id, timeout=timeout))

    async def open_campaign_receipt(self, input: models.OpenCampaignReceiptInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenCampaignReceiptResult:
        return cast("models.OpenCampaignReceiptResult", await self._request("open_campaign_receipt", input, account_id=account_id, timeout=timeout))

    async def upload_creative_asset(self, input: models.UploadCreativeAssetInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.UploadCreativeAssetResult:
        return cast("models.UploadCreativeAssetResult", await self._request("upload_creative_asset", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def open_approvals(self, input: models.OpenApprovalsInput, *, account_id: str | None = None, timeout: float | None = None) -> models.OpenApprovalsResult:
        return cast("models.OpenApprovalsResult", await self._request("open_approvals", input, account_id=account_id, timeout=timeout))

    async def open_creative_library(self, input: models.OpenCreativeLibraryInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.OpenCreativeLibraryResult:
        return cast("models.OpenCreativeLibraryResult", await self._request("open_creative_library", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def get_delivery(self, input: models.GetDeliveryInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetDeliveryResult:
        return cast("models.GetDeliveryResult", await self._request("get_delivery", input, account_id=account_id, timeout=timeout))

    async def test_creative_macros(self, input: models.TestCreativeMacrosInput, *, account_id: str | None = None, timeout: float | None = None) -> models.TestCreativeMacrosResult:
        return cast("models.TestCreativeMacrosResult", await self._request("test_creative_macros", input, account_id=account_id, timeout=timeout))

    async def get_rfp_performance(self, input: models.GetRfpPerformanceInput, *, account_id: str | None = None, timeout: float | None = None) -> models.GetRfpPerformanceResult:
        return cast("models.GetRfpPerformanceResult", await self._request("get_rfp_performance", input, account_id=account_id, timeout=timeout))

    async def save_seller(self, input: models.SaveSellerInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveSellerResult:
        return cast("models.SaveSellerResult", await self._request("save_seller", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_inventory_source(self, input: models.SaveInventorySourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveInventorySourceResult:
        return cast("models.SaveInventorySourceResult", await self._request("save_inventory_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_coverage(self, input: models.SaveCoverageInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCoverageResult:
        return cast("models.SaveCoverageResult", await self._request("save_coverage", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_material(self, input: models.SaveMaterialInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMaterialResult:
        return cast("models.SaveMaterialResult", await self._request("save_material", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_wholesale_product(self, input: models.SaveWholesaleProductInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveWholesaleProductResult:
        return cast("models.SaveWholesaleProductResult", await self._request("save_wholesale_product", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_media_kit(self, input: models.SaveMediaKitInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMediaKitResult:
        return cast("models.SaveMediaKitResult", await self._request("save_media_kit", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_playbook(self, input: models.SavePlaybookInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SavePlaybookResult:
        return cast("models.SavePlaybookResult", await self._request("save_playbook", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_business_rules(self, input: models.SaveBusinessRulesInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBusinessRulesResult:
        return cast("models.SaveBusinessRulesResult", await self._request("save_business_rules", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser_instructions(self, input: models.SaveAdvertiserInstructionsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserInstructionsResult:
        return cast("models.SaveAdvertiserInstructionsResult", await self._request("save_advertiser_instructions", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_signal(self, input: models.SaveSignalInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveSignalResult:
        return cast("models.SaveSignalResult", await self._request("save_signal", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_work_item(self, input: models.SaveWorkItemInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveWorkItemResult:
        return cast("models.SaveWorkItemResult", await self._request("save_work_item", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_rfp(self, input: models.SaveRfpInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveRfpResult:
        return cast("models.SaveRfpResult", await self._request("save_rfp", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_advertiser(self, input: models.SaveAdvertiserInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAdvertiserResult:
        return cast("models.SaveAdvertiserResult", await self._request("save_advertiser", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_buyer_operator(self, input: models.SaveBuyerOperatorInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBuyerOperatorResult:
        return cast("models.SaveBuyerOperatorResult", await self._request("save_buyer_operator", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_buyer_agent(self, input: models.SaveBuyerAgentInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveBuyerAgentResult:
        return cast("models.SaveBuyerAgentResult", await self._request("save_buyer_agent", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_directed_campaign_subscription(self, input: models.SaveDirectedCampaignSubscriptionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveDirectedCampaignSubscriptionResult:
        return cast("models.SaveDirectedCampaignSubscriptionResult", await self._request("save_directed_campaign_subscription", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_audience(self, input: models.SaveAudienceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveAudienceResult:
        return cast("models.SaveAudienceResult", await self._request("save_audience", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_campaign(self, input: models.SaveCampaignInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCampaignResult:
        return cast("models.SaveCampaignResult", await self._request("save_campaign", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_catalog(self, input: models.SaveCatalogInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCatalogResult:
        return cast("models.SaveCatalogResult", await self._request("save_catalog", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_measurement_source(self, input: models.SaveMeasurementSourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMeasurementSourceResult:
        return cast("models.SaveMeasurementSourceResult", await self._request("save_measurement_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_event_source(self, input: models.SaveEventSourceInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveEventSourceResult:
        return cast("models.SaveEventSourceResult", await self._request("save_event_source", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_dimension(self, input: models.SaveDimensionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveDimensionResult:
        return cast("models.SaveDimensionResult", await self._request("save_dimension", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_property_list(self, input: models.SavePropertyListInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SavePropertyListResult:
        return cast("models.SavePropertyListResult", await self._request("save_property_list", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative(self, input: models.SaveCreativeInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeResult:
        return cast("models.SaveCreativeResult", await self._request("save_creative", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative_collection(self, input: models.SaveCreativeCollectionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeCollectionResult:
        return cast("models.SaveCreativeCollectionResult", await self._request("save_creative_collection", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_creative_session(self, input: models.SaveCreativeSessionInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveCreativeSessionResult:
        return cast("models.SaveCreativeSessionResult", await self._request("save_creative_session", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def generate_variants(self, input: models.GenerateVariantsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.GenerateVariantsResult:
        return cast("models.GenerateVariantsResult", await self._request("generate_variants", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def save_media_buy(self, input: models.SaveMediaBuyInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.SaveMediaBuyResult:
        return cast("models.SaveMediaBuyResult", await self._request("save_media_buy", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))

    async def request_proposals(self, input: models.RequestProposalsInput, *, account_id: str | None = None, timeout: float | None = None, idempotency_key: str) -> models.RequestProposalsResult:
        return cast("models.RequestProposalsResult", await self._request("request_proposals", input, account_id=account_id, timeout=timeout, idempotency_key=idempotency_key))
