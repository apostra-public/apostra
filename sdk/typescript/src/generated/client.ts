// Generated. Do not edit.
import type * as Wire from './types.gen.js'
import { Transport, type RequestOptions, type WriteRequestOptions } from '../transport.js'
export type GetV3PublicDocumentRevisionSectionsInput = { "documentId": NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['path']>["documentId"]; "revisionId": NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['path']>["revisionId"]; "section"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["section"]; "query"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["query"]; "cursor"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["cursor"]; "asOf"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["asOf"] }
export type GetV3PublicDocumentRevisionSectionsResult = Wire.GetV3PublicDocumentRevisionSectionsResponses[200]['data']
export type GetV3PublicDocumentRevisionSectionsError = Wire.GetV3PublicDocumentRevisionSectionsErrors[keyof Wire.GetV3PublicDocumentRevisionSectionsErrors]

export type DownloadV3PublicDocumentRevisionInput = { "documentId": NonNullable<Wire.DownloadV3PublicDocumentRevisionData['path']>["documentId"]; "revisionId": NonNullable<Wire.DownloadV3PublicDocumentRevisionData['path']>["revisionId"] }
export type DownloadV3PublicDocumentRevisionResult = Uint8Array
export type DownloadV3PublicDocumentRevisionError = Wire.DownloadV3PublicDocumentRevisionErrors[keyof Wire.DownloadV3PublicDocumentRevisionErrors]

export type GetStatusInput = Wire.GetStatusData['body']
export type GetStatusResult = Wire.GetStatusResponses[200]['data']
export type GetStatusError = Wire.GetStatusErrors[keyof Wire.GetStatusErrors]

export type RefreshInventorySourceHealthInput = Wire.RefreshInventorySourceHealthData['body']
export type RefreshInventorySourceHealthResult = Wire.RefreshInventorySourceHealthResponses[200]['data']
export type RefreshInventorySourceHealthError = Wire.RefreshInventorySourceHealthErrors[keyof Wire.RefreshInventorySourceHealthErrors]

export type SaveAccountInput = Wire.SaveAccountData['body']
export type SaveAccountResult = Wire.SaveAccountResponses[200]['data']
export type SaveAccountError = Wire.SaveAccountErrors[keyof Wire.SaveAccountErrors]

export type SaveAskInput = Wire.SaveAskData['body']
export type SaveAskResult = Wire.SaveAskResponses[200]['data']
export type SaveAskError = Wire.SaveAskErrors[keyof Wire.SaveAskErrors]

export type SaveBillingInput = Wire.SaveBillingData['body']
export type SaveBillingResult = Wire.SaveBillingResponses[200]['data']
export type SaveBillingError = Wire.SaveBillingErrors[keyof Wire.SaveBillingErrors]

export type SaveNotificationConfigInput = Wire.SaveNotificationConfigData['body']
export type SaveNotificationConfigResult = Wire.SaveNotificationConfigResponses[200]['data']
export type SaveNotificationConfigError = Wire.SaveNotificationConfigErrors[keyof Wire.SaveNotificationConfigErrors]

export type SaveAdvertiserGrantInput = Wire.SaveAdvertiserGrantData['body']
export type SaveAdvertiserGrantResult = Wire.SaveAdvertiserGrantResponses[200]['data']
export type SaveAdvertiserGrantError = Wire.SaveAdvertiserGrantErrors[keyof Wire.SaveAdvertiserGrantErrors]

export type SearchInput = Wire.SearchData['body']
export type SearchResult = Wire.SearchResponses[200]['data']
export type SearchError = Wire.SearchErrors[keyof Wire.SearchErrors]

export type GetInput = Wire.GetData['body']
export type GetResult = Wire.GetResponses[200]['data']
export type GetError = Wire.GetErrors[keyof Wire.GetErrors]

export type SaveConnectionInput = Wire.SaveConnectionData['body']
export type SaveConnectionResult = Wire.SaveConnectionResponses[200]['data']
export type SaveConnectionError = Wire.SaveConnectionErrors[keyof Wire.SaveConnectionErrors]

export type SaveLibraryRequestInput = Wire.SaveLibraryRequestData['body']
export type SaveLibraryRequestResult = Wire.SaveLibraryRequestResponses[200]['data']
export type SaveLibraryRequestError = Wire.SaveLibraryRequestErrors[keyof Wire.SaveLibraryRequestErrors]

export type OpenPageInput = Wire.OpenPageData['body']
export type OpenPageResult = Wire.OpenPageResponses[200]['data']
export type OpenPageError = Wire.OpenPageErrors[keyof Wire.OpenPageErrors]

export type OpenProposalPassInput = Wire.OpenProposalPassData['body']
export type OpenProposalPassResult = Wire.OpenProposalPassResponses[200]['data']
export type OpenProposalPassError = Wire.OpenProposalPassErrors[keyof Wire.OpenProposalPassErrors]

export type OpenMediaBuysPageInput = Wire.OpenMediaBuysPageData['body']
export type OpenMediaBuysPageResult = Wire.OpenMediaBuysPageResponses[200]['data']
export type OpenMediaBuysPageError = Wire.OpenMediaBuysPageErrors[keyof Wire.OpenMediaBuysPageErrors]

export type OpenConnectionsPageInput = Wire.OpenConnectionsPageData['body']
export type OpenConnectionsPageResult = Wire.OpenConnectionsPageResponses[200]['data']
export type OpenConnectionsPageError = Wire.OpenConnectionsPageErrors[keyof Wire.OpenConnectionsPageErrors]

export type OpenCreativeEnginesPageInput = Wire.OpenCreativeEnginesPageData['body']
export type OpenCreativeEnginesPageResult = Wire.OpenCreativeEnginesPageResponses[200]['data']
export type OpenCreativeEnginesPageError = Wire.OpenCreativeEnginesPageErrors[keyof Wire.OpenCreativeEnginesPageErrors]

export type OpenAdvertisersPageInput = Wire.OpenAdvertisersPageData['body']
export type OpenAdvertisersPageResult = Wire.OpenAdvertisersPageResponses[200]['data']
export type OpenAdvertisersPageError = Wire.OpenAdvertisersPageErrors[keyof Wire.OpenAdvertisersPageErrors]

export type OpenCampaignsPageInput = Wire.OpenCampaignsPageData['body']
export type OpenCampaignsPageResult = Wire.OpenCampaignsPageResponses[200]['data']
export type OpenCampaignsPageError = Wire.OpenCampaignsPageErrors[keyof Wire.OpenCampaignsPageErrors]

export type OpenCampaignReceiptInput = Wire.OpenCampaignReceiptData['body']
export type OpenCampaignReceiptResult = Wire.OpenCampaignReceiptResponses[200]['data']
export type OpenCampaignReceiptError = Wire.OpenCampaignReceiptErrors[keyof Wire.OpenCampaignReceiptErrors]

export type UploadCreativeAssetInput = Wire.UploadCreativeAssetData['body']
export type UploadCreativeAssetResult = Wire.UploadCreativeAssetResponses[200]['data']
export type UploadCreativeAssetError = Wire.UploadCreativeAssetErrors[keyof Wire.UploadCreativeAssetErrors]

export type OpenApprovalsInput = Wire.OpenApprovalsData['body']
export type OpenApprovalsResult = Wire.OpenApprovalsResponses[200]['data']
export type OpenApprovalsError = Wire.OpenApprovalsErrors[keyof Wire.OpenApprovalsErrors]

export type OpenCreativeLibraryInput = Wire.OpenCreativeLibraryData['body']
export type OpenCreativeLibraryResult = Wire.OpenCreativeLibraryResponses[200]['data']
export type OpenCreativeLibraryError = Wire.OpenCreativeLibraryErrors[keyof Wire.OpenCreativeLibraryErrors]

export type GetDeliveryInput = Wire.GetDeliveryData['body']
export type GetDeliveryResult = Wire.GetDeliveryResponses[200]['data']
export type GetDeliveryError = Wire.GetDeliveryErrors[keyof Wire.GetDeliveryErrors]

export type TestCreativeMacrosInput = Wire.TestCreativeMacrosData['body']
export type TestCreativeMacrosResult = Wire.TestCreativeMacrosResponses[200]['data']
export type TestCreativeMacrosError = Wire.TestCreativeMacrosErrors[keyof Wire.TestCreativeMacrosErrors]

export type GetRfpPerformanceInput = Wire.GetRfpPerformanceData['body']
export type GetRfpPerformanceResult = Wire.GetRfpPerformanceResponses[200]['data']
export type GetRfpPerformanceError = Wire.GetRfpPerformanceErrors[keyof Wire.GetRfpPerformanceErrors]

export type SaveSellerInput = Wire.SaveSellerData['body']
export type SaveSellerResult = Wire.SaveSellerResponses[200]['data']
export type SaveSellerError = Wire.SaveSellerErrors[keyof Wire.SaveSellerErrors]

export type SaveInventorySourceInput = Wire.SaveInventorySourceData['body']
export type SaveInventorySourceResult = Wire.SaveInventorySourceResponses[200]['data']
export type SaveInventorySourceError = Wire.SaveInventorySourceErrors[keyof Wire.SaveInventorySourceErrors]

export type SaveCoverageInput = Wire.SaveCoverageData['body']
export type SaveCoverageResult = Wire.SaveCoverageResponses[200]['data']
export type SaveCoverageError = Wire.SaveCoverageErrors[keyof Wire.SaveCoverageErrors]

export type SaveMaterialInput = Wire.SaveMaterialData['body']
export type SaveMaterialResult = Wire.SaveMaterialResponses[200]['data']
export type SaveMaterialError = Wire.SaveMaterialErrors[keyof Wire.SaveMaterialErrors]

export type SaveWholesaleProductInput = Wire.SaveWholesaleProductData['body']
export type SaveWholesaleProductResult = Wire.SaveWholesaleProductResponses[200]['data']
export type SaveWholesaleProductError = Wire.SaveWholesaleProductErrors[keyof Wire.SaveWholesaleProductErrors]

export type SaveMediaKitInput = Wire.SaveMediaKitData['body']
export type SaveMediaKitResult = Wire.SaveMediaKitResponses[200]['data']
export type SaveMediaKitError = Wire.SaveMediaKitErrors[keyof Wire.SaveMediaKitErrors]

export type SavePlaybookInput = Wire.SavePlaybookData['body']
export type SavePlaybookResult = Wire.SavePlaybookResponses[200]['data']
export type SavePlaybookError = Wire.SavePlaybookErrors[keyof Wire.SavePlaybookErrors]

export type SaveBusinessRulesInput = Wire.SaveBusinessRulesData['body']
export type SaveBusinessRulesResult = Wire.SaveBusinessRulesResponses[200]['data']
export type SaveBusinessRulesError = Wire.SaveBusinessRulesErrors[keyof Wire.SaveBusinessRulesErrors]

export type SaveAdvertiserInstructionsInput = Wire.SaveAdvertiserInstructionsData['body']
export type SaveAdvertiserInstructionsResult = Wire.SaveAdvertiserInstructionsResponses[200]['data']
export type SaveAdvertiserInstructionsError = Wire.SaveAdvertiserInstructionsErrors[keyof Wire.SaveAdvertiserInstructionsErrors]

export type SaveSignalInput = Wire.SaveSignalData['body']
export type SaveSignalResult = Wire.SaveSignalResponses[200]['data']
export type SaveSignalError = Wire.SaveSignalErrors[keyof Wire.SaveSignalErrors]

export type SaveWorkItemInput = Wire.SaveWorkItemData['body']
export type SaveWorkItemResult = Wire.SaveWorkItemResponses[200]['data']
export type SaveWorkItemError = Wire.SaveWorkItemErrors[keyof Wire.SaveWorkItemErrors]

export type SaveRfpInput = Wire.SaveRfpData['body']
export type SaveRfpResult = Wire.SaveRfpResponses[200]['data']
export type SaveRfpError = Wire.SaveRfpErrors[keyof Wire.SaveRfpErrors]

export type SaveAdvertiserInput = Wire.SaveAdvertiserData['body']
export type SaveAdvertiserResult = Wire.SaveAdvertiserResponses[200]['data']
export type SaveAdvertiserError = Wire.SaveAdvertiserErrors[keyof Wire.SaveAdvertiserErrors]

export type SaveBuyerOperatorInput = Wire.SaveBuyerOperatorData['body']
export type SaveBuyerOperatorResult = Wire.SaveBuyerOperatorResponses[200]['data']
export type SaveBuyerOperatorError = Wire.SaveBuyerOperatorErrors[keyof Wire.SaveBuyerOperatorErrors]

export type SaveBuyerAgentInput = Wire.SaveBuyerAgentData['body']
export type SaveBuyerAgentResult = Wire.SaveBuyerAgentResponses[200]['data']
export type SaveBuyerAgentError = Wire.SaveBuyerAgentErrors[keyof Wire.SaveBuyerAgentErrors]

export type SaveDirectedCampaignSubscriptionInput = Wire.SaveDirectedCampaignSubscriptionData['body']
export type SaveDirectedCampaignSubscriptionResult = Wire.SaveDirectedCampaignSubscriptionResponses[200]['data']
export type SaveDirectedCampaignSubscriptionError = Wire.SaveDirectedCampaignSubscriptionErrors[keyof Wire.SaveDirectedCampaignSubscriptionErrors]

export type SaveAudienceInput = Wire.SaveAudienceData['body']
export type SaveAudienceResult = Wire.SaveAudienceResponses[200]['data']
export type SaveAudienceError = Wire.SaveAudienceErrors[keyof Wire.SaveAudienceErrors]

export type SaveCampaignInput = Wire.SaveCampaignData['body']
export type SaveCampaignResult = Wire.SaveCampaignResponses[200]['data']
export type SaveCampaignError = Wire.SaveCampaignErrors[keyof Wire.SaveCampaignErrors]

export type SaveCatalogInput = Wire.SaveCatalogData['body']
export type SaveCatalogResult = Wire.SaveCatalogResponses[200]['data']
export type SaveCatalogError = Wire.SaveCatalogErrors[keyof Wire.SaveCatalogErrors]

export type SaveMeasurementSourceInput = Wire.SaveMeasurementSourceData['body']
export type SaveMeasurementSourceResult = Wire.SaveMeasurementSourceResponses[200]['data']
export type SaveMeasurementSourceError = Wire.SaveMeasurementSourceErrors[keyof Wire.SaveMeasurementSourceErrors]

export type SaveEventSourceInput = Wire.SaveEventSourceData['body']
export type SaveEventSourceResult = Wire.SaveEventSourceResponses[200]['data']
export type SaveEventSourceError = Wire.SaveEventSourceErrors[keyof Wire.SaveEventSourceErrors]

export type SaveDimensionInput = Wire.SaveDimensionData['body']
export type SaveDimensionResult = Wire.SaveDimensionResponses[200]['data']
export type SaveDimensionError = Wire.SaveDimensionErrors[keyof Wire.SaveDimensionErrors]

export type SavePropertyListInput = Wire.SavePropertyListData['body']
export type SavePropertyListResult = Wire.SavePropertyListResponses[200]['data']
export type SavePropertyListError = Wire.SavePropertyListErrors[keyof Wire.SavePropertyListErrors]

export type SaveCreativeInput = Wire.SaveCreativeData['body']
export type SaveCreativeResult = Wire.SaveCreativeResponses[200]['data']
export type SaveCreativeError = Wire.SaveCreativeErrors[keyof Wire.SaveCreativeErrors]

export type SaveCreativeCollectionInput = Wire.SaveCreativeCollectionData['body']
export type SaveCreativeCollectionResult = Wire.SaveCreativeCollectionResponses[200]['data']
export type SaveCreativeCollectionError = Wire.SaveCreativeCollectionErrors[keyof Wire.SaveCreativeCollectionErrors]

export type SaveCreativeSessionInput = Wire.SaveCreativeSessionData['body']
export type SaveCreativeSessionResult = Wire.SaveCreativeSessionResponses[200]['data']
export type SaveCreativeSessionError = Wire.SaveCreativeSessionErrors[keyof Wire.SaveCreativeSessionErrors]

export type GenerateVariantsInput = Wire.GenerateVariantsData['body']
export type GenerateVariantsResult = Wire.GenerateVariantsResponses[200]['data']
export type GenerateVariantsError = Wire.GenerateVariantsErrors[keyof Wire.GenerateVariantsErrors]

export type SaveMediaBuyInput = Wire.SaveMediaBuyData['body']
export type SaveMediaBuyResult = Wire.SaveMediaBuyResponses[200]['data']
export type SaveMediaBuyError = Wire.SaveMediaBuyErrors[keyof Wire.SaveMediaBuyErrors]

export type RequestProposalsInput = Wire.RequestProposalsData['body']
export type RequestProposalsResult = Wire.RequestProposalsResponses[200]['data']
export type RequestProposalsError = Wire.RequestProposalsErrors[keyof Wire.RequestProposalsErrors]

export interface OperationTypes { "getV3PublicDocumentRevisionSections": { input: GetV3PublicDocumentRevisionSectionsInput; result: GetV3PublicDocumentRevisionSectionsResult }; "downloadV3PublicDocumentRevision": { input: DownloadV3PublicDocumentRevisionInput; result: DownloadV3PublicDocumentRevisionResult }; "get_status": { input: GetStatusInput; result: GetStatusResult }; "refresh_inventory_source_health": { input: RefreshInventorySourceHealthInput; result: RefreshInventorySourceHealthResult }; "save_account": { input: SaveAccountInput; result: SaveAccountResult }; "save_ask": { input: SaveAskInput; result: SaveAskResult }; "save_billing": { input: SaveBillingInput; result: SaveBillingResult }; "save_notification_config": { input: SaveNotificationConfigInput; result: SaveNotificationConfigResult }; "save_advertiser_grant": { input: SaveAdvertiserGrantInput; result: SaveAdvertiserGrantResult }; "search": { input: SearchInput; result: SearchResult }; "get": { input: GetInput; result: GetResult }; "save_connection": { input: SaveConnectionInput; result: SaveConnectionResult }; "save_library_request": { input: SaveLibraryRequestInput; result: SaveLibraryRequestResult }; "open_page": { input: OpenPageInput; result: OpenPageResult }; "open_proposal_pass": { input: OpenProposalPassInput; result: OpenProposalPassResult }; "open_media_buys_page": { input: OpenMediaBuysPageInput; result: OpenMediaBuysPageResult }; "open_connections_page": { input: OpenConnectionsPageInput; result: OpenConnectionsPageResult }; "open_creative_engines_page": { input: OpenCreativeEnginesPageInput; result: OpenCreativeEnginesPageResult }; "open_advertisers_page": { input: OpenAdvertisersPageInput; result: OpenAdvertisersPageResult }; "open_campaigns_page": { input: OpenCampaignsPageInput; result: OpenCampaignsPageResult }; "open_campaign_receipt": { input: OpenCampaignReceiptInput; result: OpenCampaignReceiptResult }; "upload_creative_asset": { input: UploadCreativeAssetInput; result: UploadCreativeAssetResult }; "open_approvals": { input: OpenApprovalsInput; result: OpenApprovalsResult }; "open_creative_library": { input: OpenCreativeLibraryInput; result: OpenCreativeLibraryResult }; "get_delivery": { input: GetDeliveryInput; result: GetDeliveryResult }; "test_creative_macros": { input: TestCreativeMacrosInput; result: TestCreativeMacrosResult }; "get_rfp_performance": { input: GetRfpPerformanceInput; result: GetRfpPerformanceResult }; "save_seller": { input: SaveSellerInput; result: SaveSellerResult }; "save_inventory_source": { input: SaveInventorySourceInput; result: SaveInventorySourceResult }; "save_coverage": { input: SaveCoverageInput; result: SaveCoverageResult }; "save_material": { input: SaveMaterialInput; result: SaveMaterialResult }; "save_wholesale_product": { input: SaveWholesaleProductInput; result: SaveWholesaleProductResult }; "save_media_kit": { input: SaveMediaKitInput; result: SaveMediaKitResult }; "save_playbook": { input: SavePlaybookInput; result: SavePlaybookResult }; "save_business_rules": { input: SaveBusinessRulesInput; result: SaveBusinessRulesResult }; "save_advertiser_instructions": { input: SaveAdvertiserInstructionsInput; result: SaveAdvertiserInstructionsResult }; "save_signal": { input: SaveSignalInput; result: SaveSignalResult }; "save_work_item": { input: SaveWorkItemInput; result: SaveWorkItemResult }; "save_rfp": { input: SaveRfpInput; result: SaveRfpResult }; "save_advertiser": { input: SaveAdvertiserInput; result: SaveAdvertiserResult }; "save_buyer_operator": { input: SaveBuyerOperatorInput; result: SaveBuyerOperatorResult }; "save_buyer_agent": { input: SaveBuyerAgentInput; result: SaveBuyerAgentResult }; "save_directed_campaign_subscription": { input: SaveDirectedCampaignSubscriptionInput; result: SaveDirectedCampaignSubscriptionResult }; "save_audience": { input: SaveAudienceInput; result: SaveAudienceResult }; "save_campaign": { input: SaveCampaignInput; result: SaveCampaignResult }; "save_catalog": { input: SaveCatalogInput; result: SaveCatalogResult }; "save_measurement_source": { input: SaveMeasurementSourceInput; result: SaveMeasurementSourceResult }; "save_event_source": { input: SaveEventSourceInput; result: SaveEventSourceResult }; "save_dimension": { input: SaveDimensionInput; result: SaveDimensionResult }; "save_property_list": { input: SavePropertyListInput; result: SavePropertyListResult }; "save_creative": { input: SaveCreativeInput; result: SaveCreativeResult }; "save_creative_collection": { input: SaveCreativeCollectionInput; result: SaveCreativeCollectionResult }; "save_creative_session": { input: SaveCreativeSessionInput; result: SaveCreativeSessionResult }; "generate_variants": { input: GenerateVariantsInput; result: GenerateVariantsResult }; "save_media_buy": { input: SaveMediaBuyInput; result: SaveMediaBuyResult }; "request_proposals": { input: RequestProposalsInput; result: RequestProposalsResult } }
export class Apostra extends Transport {
  getV3PublicDocumentRevisionSections(input: GetV3PublicDocumentRevisionSectionsInput, options?: RequestOptions): Promise<GetV3PublicDocumentRevisionSectionsResult> { return this.request("getV3PublicDocumentRevisionSections", input, options) }
  downloadV3PublicDocumentRevision(input: DownloadV3PublicDocumentRevisionInput, options?: RequestOptions): Promise<DownloadV3PublicDocumentRevisionResult> { return this.request("downloadV3PublicDocumentRevision", input, options) }
  getStatus(input: GetStatusInput, options?: RequestOptions): Promise<GetStatusResult> { return this.request("get_status", input, options) }
  refreshInventorySourceHealth(input: RefreshInventorySourceHealthInput, options: WriteRequestOptions): Promise<RefreshInventorySourceHealthResult> { return this.request("refresh_inventory_source_health", input, options) }
  saveAccount(input: SaveAccountInput, options: WriteRequestOptions): Promise<SaveAccountResult> { return this.request("save_account", input, options) }
  saveAsk(input: SaveAskInput, options: WriteRequestOptions): Promise<SaveAskResult> { return this.request("save_ask", input, options) }
  saveBilling(input: SaveBillingInput, options: WriteRequestOptions): Promise<SaveBillingResult> { return this.request("save_billing", input, options) }
  saveNotificationConfig(input: SaveNotificationConfigInput, options: WriteRequestOptions): Promise<SaveNotificationConfigResult> { return this.request("save_notification_config", input, options) }
  saveAdvertiserGrant(input: SaveAdvertiserGrantInput, options: WriteRequestOptions): Promise<SaveAdvertiserGrantResult> { return this.request("save_advertiser_grant", input, options) }
  search(input: SearchInput, options?: RequestOptions): Promise<SearchResult> { return this.request("search", input, options) }
  get(input: GetInput, options?: RequestOptions): Promise<GetResult> { return this.request("get", input, options) }
  saveConnection(input: SaveConnectionInput, options: WriteRequestOptions): Promise<SaveConnectionResult> { return this.request("save_connection", input, options) }
  saveLibraryRequest(input: SaveLibraryRequestInput, options: WriteRequestOptions): Promise<SaveLibraryRequestResult> { return this.request("save_library_request", input, options) }
  openPage(input: OpenPageInput, options?: RequestOptions): Promise<OpenPageResult> { return this.request("open_page", input, options) }
  openProposalPass(input: OpenProposalPassInput, options?: RequestOptions): Promise<OpenProposalPassResult> { return this.request("open_proposal_pass", input, options) }
  openMediaBuysPage(input: OpenMediaBuysPageInput, options?: RequestOptions): Promise<OpenMediaBuysPageResult> { return this.request("open_media_buys_page", input, options) }
  openConnectionsPage(input: OpenConnectionsPageInput, options?: RequestOptions): Promise<OpenConnectionsPageResult> { return this.request("open_connections_page", input, options) }
  openCreativeEnginesPage(input: OpenCreativeEnginesPageInput, options?: RequestOptions): Promise<OpenCreativeEnginesPageResult> { return this.request("open_creative_engines_page", input, options) }
  openAdvertisersPage(input: OpenAdvertisersPageInput, options?: RequestOptions): Promise<OpenAdvertisersPageResult> { return this.request("open_advertisers_page", input, options) }
  openCampaignsPage(input: OpenCampaignsPageInput, options?: RequestOptions): Promise<OpenCampaignsPageResult> { return this.request("open_campaigns_page", input, options) }
  openCampaignReceipt(input: OpenCampaignReceiptInput, options?: RequestOptions): Promise<OpenCampaignReceiptResult> { return this.request("open_campaign_receipt", input, options) }
  uploadCreativeAsset(input: UploadCreativeAssetInput, options: WriteRequestOptions): Promise<UploadCreativeAssetResult> { return this.request("upload_creative_asset", input, options) }
  openApprovals(input: OpenApprovalsInput, options?: RequestOptions): Promise<OpenApprovalsResult> { return this.request("open_approvals", input, options) }
  openCreativeLibrary(input: OpenCreativeLibraryInput, options: WriteRequestOptions): Promise<OpenCreativeLibraryResult> { return this.request("open_creative_library", input, options) }
  getDelivery(input: GetDeliveryInput, options?: RequestOptions): Promise<GetDeliveryResult> { return this.request("get_delivery", input, options) }
  testCreativeMacros(input: TestCreativeMacrosInput, options?: RequestOptions): Promise<TestCreativeMacrosResult> { return this.request("test_creative_macros", input, options) }
  getRfpPerformance(input: GetRfpPerformanceInput, options?: RequestOptions): Promise<GetRfpPerformanceResult> { return this.request("get_rfp_performance", input, options) }
  saveSeller(input: SaveSellerInput, options: WriteRequestOptions): Promise<SaveSellerResult> { return this.request("save_seller", input, options) }
  saveInventorySource(input: SaveInventorySourceInput, options: WriteRequestOptions): Promise<SaveInventorySourceResult> { return this.request("save_inventory_source", input, options) }
  saveCoverage(input: SaveCoverageInput, options: WriteRequestOptions): Promise<SaveCoverageResult> { return this.request("save_coverage", input, options) }
  saveMaterial(input: SaveMaterialInput, options: WriteRequestOptions): Promise<SaveMaterialResult> { return this.request("save_material", input, options) }
  saveWholesaleProduct(input: SaveWholesaleProductInput, options: WriteRequestOptions): Promise<SaveWholesaleProductResult> { return this.request("save_wholesale_product", input, options) }
  saveMediaKit(input: SaveMediaKitInput, options: WriteRequestOptions): Promise<SaveMediaKitResult> { return this.request("save_media_kit", input, options) }
  savePlaybook(input: SavePlaybookInput, options: WriteRequestOptions): Promise<SavePlaybookResult> { return this.request("save_playbook", input, options) }
  saveBusinessRules(input: SaveBusinessRulesInput, options: WriteRequestOptions): Promise<SaveBusinessRulesResult> { return this.request("save_business_rules", input, options) }
  saveAdvertiserInstructions(input: SaveAdvertiserInstructionsInput, options: WriteRequestOptions): Promise<SaveAdvertiserInstructionsResult> { return this.request("save_advertiser_instructions", input, options) }
  saveSignal(input: SaveSignalInput, options: WriteRequestOptions): Promise<SaveSignalResult> { return this.request("save_signal", input, options) }
  saveWorkItem(input: SaveWorkItemInput, options: WriteRequestOptions): Promise<SaveWorkItemResult> { return this.request("save_work_item", input, options) }
  saveRfp(input: SaveRfpInput, options: WriteRequestOptions): Promise<SaveRfpResult> { return this.request("save_rfp", input, options) }
  saveAdvertiser(input: SaveAdvertiserInput, options: WriteRequestOptions): Promise<SaveAdvertiserResult> { return this.request("save_advertiser", input, options) }
  saveBuyerOperator(input: SaveBuyerOperatorInput, options: WriteRequestOptions): Promise<SaveBuyerOperatorResult> { return this.request("save_buyer_operator", input, options) }
  saveBuyerAgent(input: SaveBuyerAgentInput, options: WriteRequestOptions): Promise<SaveBuyerAgentResult> { return this.request("save_buyer_agent", input, options) }
  saveDirectedCampaignSubscription(input: SaveDirectedCampaignSubscriptionInput, options: WriteRequestOptions): Promise<SaveDirectedCampaignSubscriptionResult> { return this.request("save_directed_campaign_subscription", input, options) }
  saveAudience(input: SaveAudienceInput, options: WriteRequestOptions): Promise<SaveAudienceResult> { return this.request("save_audience", input, options) }
  saveCampaign(input: SaveCampaignInput, options: WriteRequestOptions): Promise<SaveCampaignResult> { return this.request("save_campaign", input, options) }
  saveCatalog(input: SaveCatalogInput, options: WriteRequestOptions): Promise<SaveCatalogResult> { return this.request("save_catalog", input, options) }
  saveMeasurementSource(input: SaveMeasurementSourceInput, options: WriteRequestOptions): Promise<SaveMeasurementSourceResult> { return this.request("save_measurement_source", input, options) }
  saveEventSource(input: SaveEventSourceInput, options: WriteRequestOptions): Promise<SaveEventSourceResult> { return this.request("save_event_source", input, options) }
  saveDimension(input: SaveDimensionInput, options: WriteRequestOptions): Promise<SaveDimensionResult> { return this.request("save_dimension", input, options) }
  savePropertyList(input: SavePropertyListInput, options: WriteRequestOptions): Promise<SavePropertyListResult> { return this.request("save_property_list", input, options) }
  saveCreative(input: SaveCreativeInput, options: WriteRequestOptions): Promise<SaveCreativeResult> { return this.request("save_creative", input, options) }
  saveCreativeCollection(input: SaveCreativeCollectionInput, options: WriteRequestOptions): Promise<SaveCreativeCollectionResult> { return this.request("save_creative_collection", input, options) }
  saveCreativeSession(input: SaveCreativeSessionInput, options: WriteRequestOptions): Promise<SaveCreativeSessionResult> { return this.request("save_creative_session", input, options) }
  generateVariants(input: GenerateVariantsInput, options: WriteRequestOptions): Promise<GenerateVariantsResult> { return this.request("generate_variants", input, options) }
  saveMediaBuy(input: SaveMediaBuyInput, options: WriteRequestOptions): Promise<SaveMediaBuyResult> { return this.request("save_media_buy", input, options) }
  requestProposals(input: RequestProposalsInput, options: WriteRequestOptions): Promise<RequestProposalsResult> { return this.request("request_proposals", input, options) }
}
