// Generated. Do not edit.
import type * as Wire from './types.gen.js'
import { Transport, type RequestOptions, type ResponseDetails, type WriteRequestOptions } from '../transport.js'
export type GetV3PublicDocumentRevisionSectionsInput = { "documentId": NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['path']>["documentId"]; "revisionId": NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['path']>["revisionId"]; "section"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["section"]; "query"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["query"]; "cursor"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["cursor"]; "asOf"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["asOf"] }
export type GetV3PublicDocumentRevisionSectionsResult = Wire.GetV3PublicDocumentRevisionSectionsResponses[200]['data']
export type GetV3PublicDocumentRevisionSectionsError = Wire.GetV3PublicDocumentRevisionSectionsErrors[keyof Wire.GetV3PublicDocumentRevisionSectionsErrors]

export type DownloadV3PublicDocumentRevisionInput = { "documentId": NonNullable<Wire.DownloadV3PublicDocumentRevisionData['path']>["documentId"]; "revisionId": NonNullable<Wire.DownloadV3PublicDocumentRevisionData['path']>["revisionId"] }
export type DownloadV3PublicDocumentRevisionResult = Uint8Array
export type DownloadV3PublicDocumentRevisionError = Wire.DownloadV3PublicDocumentRevisionErrors[keyof Wire.DownloadV3PublicDocumentRevisionErrors]

export type GetV3PublicMutationReceiptInput = { "receiptId": NonNullable<Wire.GetV3PublicMutationReceiptData['path']>["receiptId"] }
export type GetV3PublicMutationReceiptResult = Wire.GetV3PublicMutationReceiptResponses[200]['data']
export type GetV3PublicMutationReceiptError = Wire.GetV3PublicMutationReceiptErrors[keyof Wire.GetV3PublicMutationReceiptErrors]

export type GetStatusInput = Wire.GetStatusData['body']
export type GetStatusResult = Wire.GetStatusResponses[200]['data']
export type GetStatusError = Wire.GetStatusErrors[keyof Wire.GetStatusErrors]

export type RefreshInventorySourceHealthInput = Wire.RefreshInventorySourceHealthData['body']
export type RefreshInventorySourceHealthResult = Wire.RefreshInventorySourceHealthResponses[200]['data']
export type RefreshInventorySourceHealthError = Wire.RefreshInventorySourceHealthErrors[keyof Wire.RefreshInventorySourceHealthErrors]

export type SaveAccountInput = Wire.SaveAccountData['body']
export type SaveAccountResult = Wire.SaveAccountResponses[200]['data']
export type SaveAccountError = Wire.SaveAccountErrors[keyof Wire.SaveAccountErrors]

export type ReviewBuyerChildAccountInput = Wire.ReviewBuyerChildAccountData['body']
export type ReviewBuyerChildAccountResult = Wire.ReviewBuyerChildAccountResponses[200]['data']
export type ReviewBuyerChildAccountError = Wire.ReviewBuyerChildAccountErrors[keyof Wire.ReviewBuyerChildAccountErrors]

export type RequestBuyerChildAccountInput = Omit<Wire.RequestBuyerChildAccountData['body'], "idempotencyKey"> & Partial<Pick<Wire.RequestBuyerChildAccountData['body'], "idempotencyKey">>
export type RequestBuyerChildAccountResult = Wire.RequestBuyerChildAccountResponses[200]['data']
export type RequestBuyerChildAccountError = Wire.RequestBuyerChildAccountErrors[keyof Wire.RequestBuyerChildAccountErrors]

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

export type OpenSellerDashboardInput = Wire.OpenSellerDashboardData['body']
export type OpenSellerDashboardResult = Wire.OpenSellerDashboardResponses[200]['data']
export type OpenSellerDashboardError = Wire.OpenSellerDashboardErrors[keyof Wire.OpenSellerDashboardErrors]

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

export type OpenVariantGalleryInput = Wire.OpenVariantGalleryData['body']
export type OpenVariantGalleryResult = Wire.OpenVariantGalleryResponses[200]['data']
export type OpenVariantGalleryError = Wire.OpenVariantGalleryErrors[keyof Wire.OpenVariantGalleryErrors]

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

export type SaveAgentInput = Wire.SaveAgentData['body']
export type SaveAgentResult = Wire.SaveAgentResponses[200]['data']
export type SaveAgentError = Wire.SaveAgentErrors[keyof Wire.SaveAgentErrors]

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

export type SaveAdvertiserInput = Omit<Wire.SaveAdvertiserData['body'], "idempotencyKey"> & Partial<Pick<Wire.SaveAdvertiserData['body'], "idempotencyKey">>
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

export type SaveCampaignInput = Omit<Wire.SaveCampaignData['body'], "idempotencyKey"> & Partial<Pick<Wire.SaveCampaignData['body'], "idempotencyKey">>
export type SaveCampaignResult = Wire.SaveCampaignResponses[200]['data']
export type SaveCampaignError = Wire.SaveCampaignErrors[keyof Wire.SaveCampaignErrors]

export type SaveCatalogInput = Omit<Wire.SaveCatalogData['body'], "idempotencyKey"> & Partial<Pick<Wire.SaveCatalogData['body'], "idempotencyKey">>
export type SaveCatalogResult = Wire.SaveCatalogResponses[200]['data']
export type SaveCatalogError = Wire.SaveCatalogErrors[keyof Wire.SaveCatalogErrors]

export type SaveEventSourceInput = Omit<Wire.SaveEventSourceData['body'], "idempotencyKey"> & Partial<Pick<Wire.SaveEventSourceData['body'], "idempotencyKey">>
export type SaveEventSourceResult = Wire.SaveEventSourceResponses[200]['data']
export type SaveEventSourceError = Wire.SaveEventSourceErrors[keyof Wire.SaveEventSourceErrors]

export type SaveDimensionInput = Wire.SaveDimensionData['body']
export type SaveDimensionResult = Wire.SaveDimensionResponses[200]['data']
export type SaveDimensionError = Wire.SaveDimensionErrors[keyof Wire.SaveDimensionErrors]

export type SavePropertyListInput = Wire.SavePropertyListData['body']
export type SavePropertyListResult = Wire.SavePropertyListResponses[200]['data']
export type SavePropertyListError = Wire.SavePropertyListErrors[keyof Wire.SavePropertyListErrors]

export type SaveCreativeInput = Omit<Wire.SaveCreativeData['body'], "idempotencyKey"> & Partial<Pick<Wire.SaveCreativeData['body'], "idempotencyKey">>
export type SaveCreativeResult = Wire.SaveCreativeResponses[200]['data']
export type SaveCreativeError = Wire.SaveCreativeErrors[keyof Wire.SaveCreativeErrors]

export type SaveCreativeCollectionInput = Omit<Wire.SaveCreativeCollectionData['body'], "idempotencyKey"> & Partial<Pick<Wire.SaveCreativeCollectionData['body'], "idempotencyKey">>
export type SaveCreativeCollectionResult = Wire.SaveCreativeCollectionResponses[200]['data']
export type SaveCreativeCollectionError = Wire.SaveCreativeCollectionErrors[keyof Wire.SaveCreativeCollectionErrors]

export type SaveCreativeSessionInput = Wire.SaveCreativeSessionData['body']
export type SaveCreativeSessionResult = Wire.SaveCreativeSessionResponses[200]['data']
export type SaveCreativeSessionError = Wire.SaveCreativeSessionErrors[keyof Wire.SaveCreativeSessionErrors]

export type GenerateVariantsInput = Wire.GenerateVariantsData['body']
export type GenerateVariantsResult = Wire.GenerateVariantsResponses[200]['data']
export type GenerateVariantsError = Wire.GenerateVariantsErrors[keyof Wire.GenerateVariantsErrors]

export type SaveMediaBuyInput = Omit<Wire.SaveMediaBuyData['body'], "idempotencyKey"> & Partial<Pick<Wire.SaveMediaBuyData['body'], "idempotencyKey">>
export type SaveMediaBuyResult = Wire.SaveMediaBuyResponses[200]['data']
export type SaveMediaBuyError = Wire.SaveMediaBuyErrors[keyof Wire.SaveMediaBuyErrors]

export type RequestProposalsInput = Omit<Wire.RequestProposalsData['body'], "idempotencyKey"> & Partial<Pick<Wire.RequestProposalsData['body'], "idempotencyKey">>
export type RequestProposalsResult = Wire.RequestProposalsResponses[200]['data']
export type RequestProposalsError = Wire.RequestProposalsErrors[keyof Wire.RequestProposalsErrors]

export interface OperationTypes { "getV3PublicDocumentRevisionSections": { input: GetV3PublicDocumentRevisionSectionsInput; result: GetV3PublicDocumentRevisionSectionsResult }; "downloadV3PublicDocumentRevision": { input: DownloadV3PublicDocumentRevisionInput; result: DownloadV3PublicDocumentRevisionResult }; "getV3PublicMutationReceipt": { input: GetV3PublicMutationReceiptInput; result: GetV3PublicMutationReceiptResult }; "get_status": { input: GetStatusInput; result: GetStatusResult }; "refresh_inventory_source_health": { input: RefreshInventorySourceHealthInput; result: RefreshInventorySourceHealthResult }; "save_account": { input: SaveAccountInput; result: SaveAccountResult }; "review_buyer_child_account": { input: ReviewBuyerChildAccountInput; result: ReviewBuyerChildAccountResult }; "request_buyer_child_account": { input: RequestBuyerChildAccountInput; result: RequestBuyerChildAccountResult }; "save_ask": { input: SaveAskInput; result: SaveAskResult }; "save_billing": { input: SaveBillingInput; result: SaveBillingResult }; "save_notification_config": { input: SaveNotificationConfigInput; result: SaveNotificationConfigResult }; "save_advertiser_grant": { input: SaveAdvertiserGrantInput; result: SaveAdvertiserGrantResult }; "search": { input: SearchInput; result: SearchResult }; "get": { input: GetInput; result: GetResult }; "save_connection": { input: SaveConnectionInput; result: SaveConnectionResult }; "save_library_request": { input: SaveLibraryRequestInput; result: SaveLibraryRequestResult }; "open_page": { input: OpenPageInput; result: OpenPageResult }; "open_proposal_pass": { input: OpenProposalPassInput; result: OpenProposalPassResult }; "open_media_buys_page": { input: OpenMediaBuysPageInput; result: OpenMediaBuysPageResult }; "open_seller_dashboard": { input: OpenSellerDashboardInput; result: OpenSellerDashboardResult }; "open_connections_page": { input: OpenConnectionsPageInput; result: OpenConnectionsPageResult }; "open_creative_engines_page": { input: OpenCreativeEnginesPageInput; result: OpenCreativeEnginesPageResult }; "open_advertisers_page": { input: OpenAdvertisersPageInput; result: OpenAdvertisersPageResult }; "open_campaigns_page": { input: OpenCampaignsPageInput; result: OpenCampaignsPageResult }; "open_campaign_receipt": { input: OpenCampaignReceiptInput; result: OpenCampaignReceiptResult }; "upload_creative_asset": { input: UploadCreativeAssetInput; result: UploadCreativeAssetResult }; "open_approvals": { input: OpenApprovalsInput; result: OpenApprovalsResult }; "open_creative_library": { input: OpenCreativeLibraryInput; result: OpenCreativeLibraryResult }; "open_variant_gallery": { input: OpenVariantGalleryInput; result: OpenVariantGalleryResult }; "get_delivery": { input: GetDeliveryInput; result: GetDeliveryResult }; "test_creative_macros": { input: TestCreativeMacrosInput; result: TestCreativeMacrosResult }; "get_rfp_performance": { input: GetRfpPerformanceInput; result: GetRfpPerformanceResult }; "save_seller": { input: SaveSellerInput; result: SaveSellerResult }; "save_agent": { input: SaveAgentInput; result: SaveAgentResult }; "save_inventory_source": { input: SaveInventorySourceInput; result: SaveInventorySourceResult }; "save_coverage": { input: SaveCoverageInput; result: SaveCoverageResult }; "save_material": { input: SaveMaterialInput; result: SaveMaterialResult }; "save_wholesale_product": { input: SaveWholesaleProductInput; result: SaveWholesaleProductResult }; "save_media_kit": { input: SaveMediaKitInput; result: SaveMediaKitResult }; "save_playbook": { input: SavePlaybookInput; result: SavePlaybookResult }; "save_business_rules": { input: SaveBusinessRulesInput; result: SaveBusinessRulesResult }; "save_advertiser_instructions": { input: SaveAdvertiserInstructionsInput; result: SaveAdvertiserInstructionsResult }; "save_signal": { input: SaveSignalInput; result: SaveSignalResult }; "save_work_item": { input: SaveWorkItemInput; result: SaveWorkItemResult }; "save_rfp": { input: SaveRfpInput; result: SaveRfpResult }; "save_advertiser": { input: SaveAdvertiserInput; result: SaveAdvertiserResult }; "save_buyer_operator": { input: SaveBuyerOperatorInput; result: SaveBuyerOperatorResult }; "save_buyer_agent": { input: SaveBuyerAgentInput; result: SaveBuyerAgentResult }; "save_directed_campaign_subscription": { input: SaveDirectedCampaignSubscriptionInput; result: SaveDirectedCampaignSubscriptionResult }; "save_audience": { input: SaveAudienceInput; result: SaveAudienceResult }; "save_campaign": { input: SaveCampaignInput; result: SaveCampaignResult }; "save_catalog": { input: SaveCatalogInput; result: SaveCatalogResult }; "save_event_source": { input: SaveEventSourceInput; result: SaveEventSourceResult }; "save_dimension": { input: SaveDimensionInput; result: SaveDimensionResult }; "save_property_list": { input: SavePropertyListInput; result: SavePropertyListResult }; "save_creative": { input: SaveCreativeInput; result: SaveCreativeResult }; "save_creative_collection": { input: SaveCreativeCollectionInput; result: SaveCreativeCollectionResult }; "save_creative_session": { input: SaveCreativeSessionInput; result: SaveCreativeSessionResult }; "generate_variants": { input: GenerateVariantsInput; result: GenerateVariantsResult }; "save_media_buy": { input: SaveMediaBuyInput; result: SaveMediaBuyResult }; "request_proposals": { input: RequestProposalsInput; result: RequestProposalsResult } }
export class Apostra extends Transport {
  /**
   * Read a bounded public immutable document revision
   *
   * @example
   * await client.getV3PublicDocumentRevisionSections(input)
   */
  getV3PublicDocumentRevisionSections(input: GetV3PublicDocumentRevisionSectionsInput, options?: RequestOptions): Promise<GetV3PublicDocumentRevisionSectionsResult> { return this.request("getV3PublicDocumentRevisionSections", input, options) }

  /** Read a bounded public immutable document revision Returns the data together with response headers and request ID. */
  getV3PublicDocumentRevisionSectionsWithResponse(input: GetV3PublicDocumentRevisionSectionsInput, options?: RequestOptions): Promise<ResponseDetails<GetV3PublicDocumentRevisionSectionsResult>> { return this.requestDetailed("getV3PublicDocumentRevisionSections", input, options) }
  /**
   * Download a public immutable document revision
   *
   * @example
   * await client.downloadV3PublicDocumentRevision(input)
   */
  downloadV3PublicDocumentRevision(input: DownloadV3PublicDocumentRevisionInput, options?: RequestOptions): Promise<DownloadV3PublicDocumentRevisionResult> { return this.request("downloadV3PublicDocumentRevision", input, options) }

  /** Download a public immutable document revision Returns the data together with response headers and request ID. */
  downloadV3PublicDocumentRevisionWithResponse(input: DownloadV3PublicDocumentRevisionInput, options?: RequestOptions): Promise<ResponseDetails<DownloadV3PublicDocumentRevisionResult>> { return this.requestDetailed("downloadV3PublicDocumentRevision", input, options) }
  /**
   * Read the state of a V3 HTTP write receipt
   *
   * @example
   * await client.getV3PublicMutationReceipt(input)
   */
  getV3PublicMutationReceipt(input: GetV3PublicMutationReceiptInput, options?: RequestOptions): Promise<GetV3PublicMutationReceiptResult> { return this.request("getV3PublicMutationReceipt", input, options) }

  /** Read the state of a V3 HTTP write receipt Returns the data together with response headers and request ID. */
  getV3PublicMutationReceiptWithResponse(input: GetV3PublicMutationReceiptInput, options?: RequestOptions): Promise<ResponseDetails<GetV3PublicMutationReceiptResult>> { return this.requestDetailed("getV3PublicMutationReceipt", input, options) }
  /**
   * Current account, state, blockers, exact fixes, and reachable accounts. For seller demand, use it to tell whether readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand.
   *
   * @example
   * await client.getStatus(input)
   */
  getStatus(input: GetStatusInput = {}, options?: RequestOptions): Promise<GetStatusResult> { return this.request("get_status", input, options) }

  /** Current account, state, blockers, exact fixes, and reachable accounts. For seller demand, use it to tell whether readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand. Returns the data together with response headers and request ID. */
  getStatusWithResponse(input: GetStatusInput = {}, options?: RequestOptions): Promise<ResponseDetails<GetStatusResult>> { return this.requestDetailed("get_status", input, options) }
  /**
   * Rechecks one external sales-agent source with no-spend get_products. Returns evidence IDs and seller readiness; no source configuration or media buy.
   *
   * @example
   * await client.refreshInventorySourceHealth(input, { idempotencyKey: 'stable-key' })
   */
  refreshInventorySourceHealth(input: RefreshInventorySourceHealthInput, options: WriteRequestOptions): Promise<RefreshInventorySourceHealthResult> { return this.request("refresh_inventory_source_health", input, options) }

  /** Rechecks one external sales-agent source with no-spend get_products. Returns evidence IDs and seller readiness; no source configuration or media buy. Returns the data together with response headers and request ID. */
  refreshInventorySourceHealthWithResponse(input: RefreshInventorySourceHealthInput, options: WriteRequestOptions): Promise<ResponseDetails<RefreshInventorySourceHealthResult>> { return this.requestDetailed("refresh_inventory_source_health", input, options) }
  /**
   * Rename an existing direct child Account or update settings.company. Never provisions, archives, or changes owners or members; use Account settings for access changes.
   *
   * @example
   * await client.saveAccount(input, { idempotencyKey: 'stable-key' })
   */
  saveAccount(input: SaveAccountInput, options: WriteRequestOptions): Promise<SaveAccountResult> { return this.request("save_account", input, options) }

  /** Rename an existing direct child Account or update settings.company. Never provisions, archives, or changes owners or members; use Account settings for access changes. Returns the data together with response headers and request ID. */
  saveAccountWithResponse(input: SaveAccountInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAccountResult>> { return this.requestDetailed("save_account", input, options) }
  /**
   * Review a Buyer child under the selected Organization: name, role, capacity, plan coverage, operator, inherited access and other effects. Read-only; nothing is created. Show the review to the person, then call request_buyer_child_account.
   *
   * @example
   * await client.reviewBuyerChildAccount(input)
   */
  reviewBuyerChildAccount(input: ReviewBuyerChildAccountInput, options?: RequestOptions): Promise<ReviewBuyerChildAccountResult> { return this.request("review_buyer_child_account", input, options) }

  /** Review a Buyer child under the selected Organization: name, role, capacity, plan coverage, operator, inherited access and other effects. Read-only; nothing is created. Show the review to the person, then call request_buyer_child_account. Returns the data together with response headers and request ID. */
  reviewBuyerChildAccountWithResponse(input: ReviewBuyerChildAccountInput, options?: RequestOptions): Promise<ResponseDetails<ReviewBuyerChildAccountResult>> { return this.requestDetailed("review_buyer_child_account", input, options) }
  /**
   * Request a Buyer child under the selected Organization. Nothing is created until an Organization administrator approves it on our site; the result is approval_required with a link to show the person. Repeat with the same idempotencyKey and name for the outcome.
   *
   * @example
   * await client.requestBuyerChildAccount(input, { idempotencyKey: 'stable-key' })
   */
  requestBuyerChildAccount(input: RequestBuyerChildAccountInput, options: WriteRequestOptions): Promise<RequestBuyerChildAccountResult> { return this.request("request_buyer_child_account", input, options) }

  /** Request a Buyer child under the selected Organization. Nothing is created until an Organization administrator approves it on our site; the result is approval_required with a link to show the person. Repeat with the same idempotencyKey and name for the outcome. Returns the data together with response headers and request ID. */
  requestBuyerChildAccountWithResponse(input: RequestBuyerChildAccountInput, options: WriteRequestOptions): Promise<ResponseDetails<RequestBuyerChildAccountResult>> { return this.requestDetailed("request_buyer_child_account", input, options) }
  /**
   * File or update a typed ask in the Apostra Support workflow; returns askId. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first.
   *
   * @example
   * await client.saveAsk(input, { idempotencyKey: 'stable-key' })
   */
  saveAsk(input: SaveAskInput, options: WriteRequestOptions): Promise<SaveAskResult> { return this.request("save_ask", input, options) }

  /** File or update a typed ask in the Apostra Support workflow; returns askId. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first. Returns the data together with response headers and request ID. */
  saveAskWithResponse(input: SaveAskInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAskResult>> { return this.requestDetailed("save_ask", input, options) }
  /**
   * Accept current Terms, choose the payment terms sellers are asked for, or manage payment authority. Card setup uses a confirmed hosted link; card data never enters MCP.
   *
   * @example
   * await client.saveBilling(input, { idempotencyKey: 'stable-key' })
   */
  saveBilling(input: SaveBillingInput, options: WriteRequestOptions): Promise<SaveBillingResult> { return this.request("save_billing", input, options) }

  /** Accept current Terms, choose the payment terms sellers are asked for, or manage payment authority. Card setup uses a confirmed hosted link; card data never enters MCP. Returns the data together with response headers and request ID. */
  saveBillingWithResponse(input: SaveBillingInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveBillingResult>> { return this.requestDetailed("save_billing", input, options) }
  /**
   * Create or update a notification subscription: scope, content, routes; no trigger type is creatable yet, no delivery policy yet. Omit subscriptionId to create, supply it to patch. Managed subscriptions are editable only within their mutability. Credentials belong to save_integration.
   *
   * @example
   * await client.saveNotificationConfig(input, { idempotencyKey: 'stable-key' })
   */
  saveNotificationConfig(input: SaveNotificationConfigInput, options: WriteRequestOptions): Promise<SaveNotificationConfigResult> { return this.request("save_notification_config", input, options) }

  /** Create or update a notification subscription: scope, content, routes; no trigger type is creatable yet, no delivery policy yet. Omit subscriptionId to create, supply it to patch. Managed subscriptions are editable only within their mutability. Credentials belong to save_integration. Returns the data together with response headers and request ID. */
  saveNotificationConfigWithResponse(input: SaveNotificationConfigInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveNotificationConfigResult>> { return this.requestDetailed("save_notification_config", input, options) }
  /**
   * Invite another Organization to exact advertisers, accept/reject an invitation, or revoke a grant. Limited beta: eligible Organization, entitlement, server-side exposure, and direct human-admin authority are required.
   *
   * @example
   * await client.saveAdvertiserGrant(input, { idempotencyKey: 'stable-key' })
   */
  saveAdvertiserGrant(input: SaveAdvertiserGrantInput, options: WriteRequestOptions): Promise<SaveAdvertiserGrantResult> { return this.request("save_advertiser_grant", input, options) }

  /** Invite another Organization to exact advertisers, accept/reject an invitation, or revoke a grant. Limited beta: eligible Organization, entitlement, server-side exposure, and direct human-admin authority are required. Returns the data together with response headers and request ID. */
  saveAdvertiserGrantWithResponse(input: SaveAdvertiserGrantInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAdvertiserGrantResult>> { return this.requestDetailed("save_advertiser_grant", input, options) }
  /**
   * query/kind; no{}. conversation=Murph; session=retained;creative_session=variants;require filter.advertiserId|filter.campaignId;Seller Library=material/requests;Docs: reread hits; cite;kind=skill before workflows;Agent=org software, not seller/counterparty; seller identity/listing=get/save_seller
   *
   * @example
   * await client.search(input)
   */
  search(input: SearchInput, options?: RequestOptions): Promise<SearchResult> { return this.request("search", input, options) }

  /** query/kind; no{}. conversation=Murph; session=retained;creative_session=variants;require filter.advertiserId|filter.campaignId;Seller Library=material/requests;Docs: reread hits; cite;kind=skill before workflows;Agent=org software, not seller/counterparty; seller identity/listing=get/save_seller Returns the data together with response headers and request ID. */
  searchWithResponse(input: SearchInput, options?: RequestOptions): Promise<ResponseDetails<SearchResult>> { return this.requestDetailed("search", input, options) }
  /**
   * Read object/singleton. billing: omit id; Terms/readiness/payment status. skill: exact user-supplied or search ID; versioned instructions+digest. conversation: bounded. Buyer/seller: search IDs. Seller: include listing, identity, commitmentRecord. Distribution: host/CNAME/readiness.
   *
   * @example
   * await client.get(input)
   */
  get(input: GetInput, options?: RequestOptions): Promise<GetResult> { return this.request("get", input, options) }

  /** Read object/singleton. billing: omit id; Terms/readiness/payment status. skill: exact user-supplied or search ID; versioned instructions+digest. conversation: bounded. Buyer/seller: search IDs. Seller: include listing, identity, commitmentRecord. Distribution: host/CNAME/readiness. Returns the data together with response headers and request ID. */
  getWithResponse(input: GetInput, options?: RequestOptions): Promise<ResponseDetails<GetResult>> { return this.requestDetailed("get", input, options) }
  /**
   * Manage seller or creative-engine authorization, accounts and advertiser mappings. Seller-only: reporting, selection, billing, policy, activation.
   *
   * @example
   * await client.saveConnection(input, { idempotencyKey: 'stable-key' })
   */
  saveConnection(input: SaveConnectionInput, options: WriteRequestOptions): Promise<SaveConnectionResult> { return this.request("save_connection", input, options) }

  /** Manage seller or creative-engine authorization, accounts and advertiser mappings. Seller-only: reporting, selection, billing, policy, activation. Returns the data together with response headers and request ID. */
  saveConnectionWithResponse(input: SaveConnectionInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveConnectionResult>> { return this.requestDetailed("save_connection", input, options) }
  /**
   * Open a seller library request or close it with seller Material.
   *
   * @example
   * await client.saveLibraryRequest(input, { idempotencyKey: 'stable-key' })
   */
  saveLibraryRequest(input: SaveLibraryRequestInput, options: WriteRequestOptions): Promise<SaveLibraryRequestResult> { return this.request("save_library_request", input, options) }

  /** Open a seller library request or close it with seller Material. Returns the data together with response headers and request ID. */
  saveLibraryRequestWithResponse(input: SaveLibraryRequestInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveLibraryRequestResult>> { return this.requestDetailed("save_library_request", input, options) }
  /**
   * Open a compatibility Page. source_diagnostics can create or attach the Agent. External hosts may return text. Credentials and authority changes remain human ceremonies.
   *
   * @example
   * await client.openPage(input)
   */
  openPage(input: OpenPageInput, options?: RequestOptions): Promise<OpenPageResult> { return this.request("open_page", input, options) }

  /** Open a compatibility Page. source_diagnostics can create or attach the Agent. External hosts may return text. Credentials and authority changes remain human ceremonies. Returns the data together with response headers and request ID. */
  openPageWithResponse(input: OpenPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenPageResult>> { return this.requestDetailed("open_page", input, options) }
  /**
   * Open Proposal Pass on one exact immutable RFP turn. Supply the matching rfpId and turnId from save_rfp or get; the Page loads the private response itself.
   *
   * @example
   * await client.openProposalPass(input)
   */
  openProposalPass(input: OpenProposalPassInput, options?: RequestOptions): Promise<OpenProposalPassResult> { return this.request("open_proposal_pass", input, options) }

  /** Open Proposal Pass on one exact immutable RFP turn. Supply the matching rfpId and turnId from save_rfp or get; the Page loads the private response itself. Returns the data together with response headers and request ID. */
  openProposalPassWithResponse(input: OpenProposalPassInput, options?: RequestOptions): Promise<ResponseDetails<OpenProposalPassResult>> { return this.requestDetailed("open_proposal_pass", input, options) }
  /**
   * Open the Seller Media Buys Page. Optionally focus one seller-owned account relationship and its buys or creatives; the Page self-fetches.
   *
   * @example
   * await client.openMediaBuysPage(input)
   */
  openMediaBuysPage(input: OpenMediaBuysPageInput, options?: RequestOptions): Promise<OpenMediaBuysPageResult> { return this.request("open_media_buys_page", input, options) }

  /** Open the Seller Media Buys Page. Optionally focus one seller-owned account relationship and its buys or creatives; the Page self-fetches. Returns the data together with response headers and request ID. */
  openMediaBuysPageWithResponse(input: OpenMediaBuysPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenMediaBuysPageResult>> { return this.requestDetailed("open_media_buys_page", input, options) }
  /**
   * Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches.
   *
   * @example
   * await client.openSellerDashboard(input)
   */
  openSellerDashboard(input: OpenSellerDashboardInput, options?: RequestOptions): Promise<OpenSellerDashboardResult> { return this.request("open_seller_dashboard", input, options) }

  /** Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches. Returns the data together with response headers and request ID. */
  openSellerDashboardWithResponse(input: OpenSellerDashboardInput, options?: RequestOptions): Promise<ResponseDetails<OpenSellerDashboardResult>> { return this.requestDetailed("open_seller_dashboard", input, options) }
  /**
   * Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction "connect" opens that media partner at connection setup without mutating until the user confirms.
   *
   * @example
   * await client.openConnectionsPage(input)
   */
  openConnectionsPage(input: OpenConnectionsPageInput, options?: RequestOptions): Promise<OpenConnectionsPageResult> { return this.request("open_connections_page", input, options) }

  /** Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction "connect" opens that media partner at connection setup without mutating until the user confirms. Returns the data together with response headers and request ID. */
  openConnectionsPageWithResponse(input: OpenConnectionsPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenConnectionsPageResult>> { return this.requestDetailed("open_connections_page", input, options) }
  /**
   * Open the buyer Creative Engines Page. Optionally focus an engine, connection, or its secure setup control; the buyer starts setup in the Page, and this does not authorize a provider or start generation.
   *
   * @example
   * await client.openCreativeEnginesPage(input)
   */
  openCreativeEnginesPage(input: OpenCreativeEnginesPageInput, options?: RequestOptions): Promise<OpenCreativeEnginesPageResult> { return this.request("open_creative_engines_page", input, options) }

  /** Open the buyer Creative Engines Page. Optionally focus an engine, connection, or its secure setup control; the buyer starts setup in the Page, and this does not authorize a provider or start generation. Returns the data together with response headers and request ID. */
  openCreativeEnginesPageWithResponse(input: OpenCreativeEnginesPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenCreativeEnginesPageResult>> { return this.requestDetailed("open_creative_engines_page", input, options) }
  /**
   * Open the Advertisers Page: every advertiser on this account with its campaign and draft counts and one next action each. Use it for "show my advertisers" or "where do I start"; the Page self-fetches, so do not recite the list. For a text answer use search(kind: "advertiser").
   *
   * @example
   * await client.openAdvertisersPage(input)
   */
  openAdvertisersPage(input: OpenAdvertisersPageInput, options?: RequestOptions): Promise<OpenAdvertisersPageResult> { return this.request("open_advertisers_page", input, options) }

  /** Open the Advertisers Page: every advertiser on this account with its campaign and draft counts and one next action each. Use it for "show my advertisers" or "where do I start"; the Page self-fetches, so do not recite the list. For a text answer use search(kind: "advertiser"). Returns the data together with response headers and request ID. */
  openAdvertisersPageWithResponse(input: OpenAdvertisersPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenAdvertisersPageResult>> { return this.requestDetailed("open_advertisers_page", input, options) }
  /**
   * Open the Campaigns Page: campaigns with status, flight, and budget; open one for its media buys and creatives. The Page self-fetches, so do not list campaigns in prose. advertiserId scopes to one advertiser; campaignId focuses one campaign. A draft's go-live review is open_campaign_receipt.
   *
   * @example
   * await client.openCampaignsPage(input)
   */
  openCampaignsPage(input: OpenCampaignsPageInput, options?: RequestOptions): Promise<OpenCampaignsPageResult> { return this.request("open_campaigns_page", input, options) }

  /** Open the Campaigns Page: campaigns with status, flight, and budget; open one for its media buys and creatives. The Page self-fetches, so do not list campaigns in prose. advertiserId scopes to one advertiser; campaignId focuses one campaign. A draft's go-live review is open_campaign_receipt. Returns the data together with response headers and request ID. */
  openCampaignsPageWithResponse(input: OpenCampaignsPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenCampaignsPageResult>> { return this.requestDetailed("open_campaigns_page", input, options) }
  /**
   * Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign.
   *
   * @example
   * await client.openCampaignReceipt(input)
   */
  openCampaignReceipt(input: OpenCampaignReceiptInput, options?: RequestOptions): Promise<OpenCampaignReceiptResult> { return this.request("open_campaign_receipt", input, options) }

  /** Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign. Returns the data together with response headers and request ID. */
  openCampaignReceiptWithResponse(input: OpenCampaignReceiptInput, options?: RequestOptions): Promise<ResponseDetails<OpenCampaignReceiptResult>> { return this.requestDetailed("open_campaign_receipt", input, options) }
  /**
   * Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative.
   *
   * @example
   * await client.uploadCreativeAsset(input, { idempotencyKey: 'stable-key' })
   */
  uploadCreativeAsset(input: UploadCreativeAssetInput, options: WriteRequestOptions): Promise<UploadCreativeAssetResult> { return this.request("upload_creative_asset", input, options) }

  /** Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative. Returns the data together with response headers and request ID. */
  uploadCreativeAssetWithResponse(input: UploadCreativeAssetInput, options: WriteRequestOptions): Promise<ResponseDetails<UploadCreativeAssetResult>> { return this.requestDetailed("upload_creative_asset", input, options) }
  /**
   * Open the Approvals Page for reviews, assignments, routing, evidence, decisions, and forward recovery. Focus by exact media-buy identity or reviewRef; creativeId works only for one loaded version.
   *
   * @example
   * await client.openApprovals(input)
   */
  openApprovals(input: OpenApprovalsInput, options?: RequestOptions): Promise<OpenApprovalsResult> { return this.request("open_approvals", input, options) }

  /** Open the Approvals Page for reviews, assignments, routing, evidence, decisions, and forward recovery. Focus by exact media-buy identity or reviewRef; creativeId works only for one loaded version. Returns the data together with response headers and request ID. */
  openApprovalsWithResponse(input: OpenApprovalsInput, options?: RequestOptions): Promise<ResponseDetails<OpenApprovalsResult>> { return this.requestDetailed("open_approvals", input, options) }
  /**
   * Open Creative Library. Use search for a plain object answer. Composer needs campaignId; assembly needs no Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format.
   *
   * @example
   * await client.openCreativeLibrary(input, { idempotencyKey: 'stable-key' })
   */
  openCreativeLibrary(input: OpenCreativeLibraryInput, options: WriteRequestOptions): Promise<OpenCreativeLibraryResult> { return this.request("open_creative_library", input, options) }

  /** Open Creative Library. Use search for a plain object answer. Composer needs campaignId; assembly needs no Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format. Returns the data together with response headers and request ID. */
  openCreativeLibraryWithResponse(input: OpenCreativeLibraryInput, options: WriteRequestOptions): Promise<ResponseDetails<OpenCreativeLibraryResult>> { return this.requestDetailed("open_creative_library", input, options) }
  /**
   * Show a saved Creative Session’s variants (find via search/get kind creative_session). Not for generating new variants.
   *
   * @example
   * await client.openVariantGallery(input)
   */
  openVariantGallery(input: OpenVariantGalleryInput, options?: RequestOptions): Promise<OpenVariantGalleryResult> { return this.request("open_variant_gallery", input, options) }

  /** Show a saved Creative Session’s variants (find via search/get kind creative_session). Not for generating new variants. Returns the data together with response headers and request ID. */
  openVariantGalleryWithResponse(input: OpenVariantGalleryInput, options?: RequestOptions): Promise<ResponseDetails<OpenVariantGalleryResult>> { return this.requestDetailed("open_variant_gallery", input, options) }
  /**
   * Query seller delivery, stored or live buyer campaign delivery, or margin facts. Use live_campaign_delivery with one campaignId for the connected provider's current response. campaign_delivery preserves stored rows, totals, and paging. Buyer measurement is excluded.
   *
   * @example
   * await client.getDelivery(input)
   */
  getDelivery(input: GetDeliveryInput, options?: RequestOptions): Promise<GetDeliveryResult> { return this.request("get_delivery", input, options) }

  /** Query seller delivery, stored or live buyer campaign delivery, or margin facts. Use live_campaign_delivery with one campaignId for the connected provider's current response. campaign_delivery preserves stored rows, totals, and paging. Buyer measurement is excluded. Returns the data together with response headers and request ID. */
  getDeliveryWithResponse(input: GetDeliveryInput, options?: RequestOptions): Promise<ResponseDetails<GetDeliveryResult>> { return this.requestDetailed("get_delivery", input, options) }
  /**
   * Dry-runs one tracker URL through exact raw input, canonical AdCP compilation, recipient translation, and deterministic synthetic substitution. Use it before preview or trafficking; unresolved required macros fail closed.
   *
   * @example
   * await client.testCreativeMacros(input)
   */
  testCreativeMacros(input: TestCreativeMacrosInput, options?: RequestOptions): Promise<TestCreativeMacrosResult> { return this.request("test_creative_macros", input, options) }

  /** Dry-runs one tracker URL through exact raw input, canonical AdCP compilation, recipient translation, and deterministic synthetic substitution. Use it before preview or trafficking; unresolved required macros fail closed. Returns the data together with response headers and request ID. */
  testCreativeMacrosWithResponse(input: TestCreativeMacrosInput, options?: RequestOptions): Promise<ResponseDetails<TestCreativeMacrosResult>> { return this.requestDetailed("test_creative_macros", input, options) }
  /**
   * Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns.
   *
   * @example
   * await client.getRfpPerformance(input)
   */
  getRfpPerformance(input: GetRfpPerformanceInput, options?: RequestOptions): Promise<GetRfpPerformanceResult> { return this.request("get_rfp_performance", input, options) }

  /** Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns. Returns the data together with response headers and request ID. */
  getRfpPerformanceWithResponse(input: GetRfpPerformanceInput, options?: RequestOptions): Promise<ResponseDetails<GetRfpPerformanceResult>> { return this.requestDetailed("get_rfp_performance", input, options) }
  /**
   * Save Seller identity, capabilities, Marketplace, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, or a seller-controlled admission. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get(kind:"distribution").
   *
   * @example
   * await client.saveSeller(input, { idempotencyKey: 'stable-key' })
   */
  saveSeller(input: SaveSellerInput, options: WriteRequestOptions): Promise<SaveSellerResult> { return this.request("save_seller", input, options) }

  /** Save Seller identity, capabilities, Marketplace, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, or a seller-controlled admission. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get(kind:"distribution"). Returns the data together with response headers and request ID. */
  saveSellerWithResponse(input: SaveSellerInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveSellerResult>> { return this.requestDetailed("save_seller", input, options) }
  /**
   * Confirm or correct one Sales Agent product mode. Owners change the Agent declaration and reject sourceId; a seller corrects its own binding on an unclaimed Agent and passes sourceId when several bindings match.
   *
   * @example
   * await client.saveAgent(input, { idempotencyKey: 'stable-key' })
   */
  saveAgent(input: SaveAgentInput, options: WriteRequestOptions): Promise<SaveAgentResult> { return this.request("save_agent", input, options) }

  /** Confirm or correct one Sales Agent product mode. Owners change the Agent declaration and reject sourceId; a seller corrects its own binding on an unclaimed Agent and passes sourceId when several bindings match. Returns the data together with response headers and request ID. */
  saveAgentWithResponse(input: SaveAgentInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAgentResult>> { return this.requestDetailed("save_agent", input, options) }
  /**
   * Create or update where a seller's inventory comes from. Pass `id` to change an existing source, omit it to add one. Credentials are never passed here — a source that needs a secret comes back with the state and the page that collects it.
   *
   * @example
   * await client.saveInventorySource(input, { idempotencyKey: 'stable-key' })
   */
  saveInventorySource(input: SaveInventorySourceInput, options: WriteRequestOptions): Promise<SaveInventorySourceResult> { return this.request("save_inventory_source", input, options) }

  /** Create or update where a seller's inventory comes from. Pass `id` to change an existing source, omit it to add one. Credentials are never passed here — a source that needs a secret comes back with the state and the page that collects it. Returns the data together with response headers and request ID. */
  saveInventorySourceWithResponse(input: SaveInventorySourceInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveInventorySourceResult>> { return this.requestDetailed("save_inventory_source", input, options) }
  /**
   * Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, and `removeProperties` change named items only. Read authorization; never assume it.
   *
   * @example
   * await client.saveCoverage(input, { idempotencyKey: 'stable-key' })
   */
  saveCoverage(input: SaveCoverageInput, options: WriteRequestOptions): Promise<SaveCoverageResult> { return this.request("save_coverage", input, options) }

  /** Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, and `removeProperties` change named items only. Read authorization; never assume it. Returns the data together with response headers and request ID. */
  saveCoverageWithResponse(input: SaveCoverageInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCoverageResult>> { return this.requestDetailed("save_coverage", input, options) }
  /**
   * Register, revise, archive, restore, or reprocess seller Materials; manage candidate decisions and receipts; mark a slide, page, or sheet reusable only when it has no commercial figures (UNIT_NOT_REUSABLE_KIND rejects document containers, UNIT_CONTAINS_PRICING rejects priced units).
   *
   * @example
   * await client.saveMaterial(input, { idempotencyKey: 'stable-key' })
   */
  saveMaterial(input: SaveMaterialInput, options: WriteRequestOptions): Promise<SaveMaterialResult> { return this.request("save_material", input, options) }

  /** Register, revise, archive, restore, or reprocess seller Materials; manage candidate decisions and receipts; mark a slide, page, or sheet reusable only when it has no commercial figures (UNIT_NOT_REUSABLE_KIND rejects document containers, UNIT_CONTAINS_PRICING rejects priced units). Returns the data together with response headers and request ID. */
  saveMaterialWithResponse(input: SaveMaterialInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveMaterialResult>> { return this.requestDetailed("save_material", input, options) }
  /**
   * Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not.
   *
   * @example
   * await client.saveWholesaleProduct(input, { idempotencyKey: 'stable-key' })
   */
  saveWholesaleProduct(input: SaveWholesaleProductInput, options: WriteRequestOptions): Promise<SaveWholesaleProductResult> { return this.request("save_wholesale_product", input, options) }

  /** Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not. Returns the data together with response headers and request ID. */
  saveWholesaleProductWithResponse(input: SaveWholesaleProductInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveWholesaleProductResult>> { return this.requestDetailed("save_wholesale_product", input, options) }
  /**
   * Deprecated compatibility tool ("listing" is the modern term). It writes only the legacy businessProfile and does not update the canonical buyer-visible listing. New clients must read with `get({ kind: "seller", include: ["listing"] })` and write with `save_seller`.
   *
   * @example
   * await client.saveMediaKit(input, { idempotencyKey: 'stable-key' })
   */
  saveMediaKit(input: SaveMediaKitInput, options: WriteRequestOptions): Promise<SaveMediaKitResult> { return this.request("save_media_kit", input, options) }

  /** Deprecated compatibility tool ("listing" is the modern term). It writes only the legacy businessProfile and does not update the canonical buyer-visible listing. New clients must read with `get({ kind: "seller", include: ["listing"] })` and write with `save_seller`. Returns the data together with response headers and request ID. */
  saveMediaKitWithResponse(input: SaveMediaKitInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveMediaKitResult>> { return this.requestDetailed("save_media_kit", input, options) }
  /**
   * Write how the seller sells. `active` creates and activates a new version in one step — no separate activate; the response names the version created and replaced. `pricing` replaces the whole fact list. `discounts` sets or removes brand/operator rules one by one. Halves never roll back each other.
   *
   * @example
   * await client.savePlaybook(input, { idempotencyKey: 'stable-key' })
   */
  savePlaybook(input: SavePlaybookInput, options: WriteRequestOptions): Promise<SavePlaybookResult> { return this.request("save_playbook", input, options) }

  /** Write how the seller sells. `active` creates and activates a new version in one step — no separate activate; the response names the version created and replaced. `pricing` replaces the whole fact list. `discounts` sets or removes brand/operator rules one by one. Halves never roll back each other. Returns the data together with response headers and request ID. */
  savePlaybookWithResponse(input: SavePlaybookInput, options: WriteRequestOptions): Promise<ResponseDetails<SavePlaybookResult>> { return this.requestDetailed("save_playbook", input, options) }
  /**
   * Write seller AI Business Rules. Policy content needs an account admin and both policy fields. Approval auto needs acknowledgeNoHumanReview.
   *
   * @example
   * await client.saveBusinessRules(input, { idempotencyKey: 'stable-key' })
   */
  saveBusinessRules(input: SaveBusinessRulesInput, options: WriteRequestOptions): Promise<SaveBusinessRulesResult> { return this.request("save_business_rules", input, options) }

  /** Write seller AI Business Rules. Policy content needs an account admin and both policy fields. Approval auto needs acknowledgeNoHumanReview. Returns the data together with response headers and request ID. */
  saveBusinessRulesWithResponse(input: SaveBusinessRulesInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveBusinessRulesResult>> { return this.requestDetailed("save_business_rules", input, options) }
  /**
   * Save seller notes and instructions for an exact brand-domain × operator-domain pair. Configuration does not verify the registry; discounts, source routing, sponsored access, and buyer-account trust are read-only.
   *
   * @example
   * await client.saveAdvertiserInstructions(input, { idempotencyKey: 'stable-key' })
   */
  saveAdvertiserInstructions(input: SaveAdvertiserInstructionsInput, options: WriteRequestOptions): Promise<SaveAdvertiserInstructionsResult> { return this.request("save_advertiser_instructions", input, options) }

  /** Save seller notes and instructions for an exact brand-domain × operator-domain pair. Configuration does not verify the registry; discounts, source routing, sponsored access, and buyer-account trust are read-only. Returns the data together with response headers and request ID. */
  saveAdvertiserInstructionsWithResponse(input: SaveAdvertiserInstructionsInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAdvertiserInstructionsResult>> { return this.requestDetailed("save_advertiser_instructions", input, options) }
  /**
   * Create, replace, or archive a signal. Managed writes need a complete draft; read before updates. Without sourceId, writes the seller catalog.
   *
   * @example
   * await client.saveSignal(input, { idempotencyKey: 'stable-key' })
   */
  saveSignal(input: SaveSignalInput, options: WriteRequestOptions): Promise<SaveSignalResult> { return this.request("save_signal", input, options) }

  /** Create, replace, or archive a signal. Managed writes need a complete draft; read before updates. Without sourceId, writes the seller catalog. Returns the data together with response headers and request ID. */
  saveSignalWithResponse(input: SaveSignalInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveSignalResult>> { return this.requestDetailed("save_signal", input, options) }
  /**
   * Decide a creative or media-buy approval, or complete a modular-source follow-up. Repeats preserve evidence; retry, evaluation, and reassignment stay on the approvals Page.
   *
   * @example
   * await client.saveWorkItem(input, { idempotencyKey: 'stable-key' })
   */
  saveWorkItem(input: SaveWorkItemInput, options: WriteRequestOptions): Promise<SaveWorkItemResult> { return this.request("save_work_item", input, options) }

  /** Decide a creative or media-buy approval, or complete a modular-source follow-up. Repeats preserve evidence; retry, evaluation, and reassignment stay on the approvals Page. Returns the data together with response headers and request ID. */
  saveWorkItemWithResponse(input: SaveWorkItemInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveWorkItemResult>> { return this.requestDetailed("save_work_item", input, options) }
  /**
   * Save RFPs and turns: imported origins, typed feedback, response pairs, endorsement, and proposal-file requests.
   *
   * @example
   * await client.saveRfp(input, { idempotencyKey: 'stable-key' })
   */
  saveRfp(input: SaveRfpInput, options: WriteRequestOptions): Promise<SaveRfpResult> { return this.request("save_rfp", input, options) }

  /** Save RFPs and turns: imported origins, typed feedback, response pairs, endorsement, and proposal-file requests. Returns the data together with response headers and request ID. */
  saveRfpWithResponse(input: SaveRfpInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveRfpResult>> { return this.requestDetailed("save_rfp", input, options) }
  /**
   * Save an advertiser or its mappings. `needs_input` = ask the buyer; never recreate to change currency. Use identityContract:confirmed-v1 for brand corrections. resolveBrand looks up public branding. Guide: /v2/setup/v3/identity-setup.
   *
   * @example
   * await client.saveAdvertiser(input, { idempotencyKey: 'stable-key' })
   */
  saveAdvertiser(input: SaveAdvertiserInput, options: WriteRequestOptions): Promise<SaveAdvertiserResult> { return this.request("save_advertiser", input, options) }

  /** Save an advertiser or its mappings. `needs_input` = ask the buyer; never recreate to change currency. Use identityContract:confirmed-v1 for brand corrections. resolveBrand looks up public branding. Guide: /v2/setup/v3/identity-setup. Returns the data together with response headers and request ID. */
  saveAdvertiserWithResponse(input: SaveAdvertiserInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAdvertiserResult>> { return this.requestDetailed("save_advertiser", input, options) }
  /**
   * Save buyer commercial identity. Read get_status; use identityContract:confirmed-v1 for preview and confirmation. Guide: /v2/setup/v3/identity-setup.
   *
   * @example
   * await client.saveBuyerOperator(input, { idempotencyKey: 'stable-key' })
   */
  saveBuyerOperator(input: SaveBuyerOperatorInput, options: WriteRequestOptions): Promise<SaveBuyerOperatorResult> { return this.request("save_buyer_operator", input, options) }

  /** Save buyer commercial identity. Read get_status; use identityContract:confirmed-v1 for preview and confirmation. Guide: /v2/setup/v3/identity-setup. Returns the data together with response headers and request ID. */
  saveBuyerOperatorWithResponse(input: SaveBuyerOperatorInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveBuyerOperatorResult>> { return this.requestDetailed("save_buyer_operator", input, options) }
  /**
   * Create, rename, reconcile access, change lifecycle, or prepare a human credential handoff for one buyer agent per call.
   *
   * @example
   * await client.saveBuyerAgent(input, { idempotencyKey: 'stable-key' })
   */
  saveBuyerAgent(input: SaveBuyerAgentInput, options: WriteRequestOptions): Promise<SaveBuyerAgentResult> { return this.request("save_buyer_agent", input, options) }

  /** Create, rename, reconcile access, change lifecycle, or prepare a human credential handoff for one buyer agent per call. Returns the data together with response headers and request ID. */
  saveBuyerAgentWithResponse(input: SaveBuyerAgentInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveBuyerAgentResult>> { return this.requestDetailed("save_buyer_agent", input, options) }
  /**
   * Subscribe to a connected seller's directed campaigns, mirroring its media buys into this buyer's view. Set `unsubscribe: true` to remove the subscription and retire mirrored campaigns. Requires a mapped seller account and reachable advertiser.
   *
   * @example
   * await client.saveDirectedCampaignSubscription(input, { idempotencyKey: 'stable-key' })
   */
  saveDirectedCampaignSubscription(input: SaveDirectedCampaignSubscriptionInput, options: WriteRequestOptions): Promise<SaveDirectedCampaignSubscriptionResult> { return this.request("save_directed_campaign_subscription", input, options) }

  /** Subscribe to a connected seller's directed campaigns, mirroring its media buys into this buyer's view. Set `unsubscribe: true` to remove the subscription and retire mirrored campaigns. Requires a mapped seller account and reachable advertiser. Returns the data together with response headers and request ID. */
  saveDirectedCampaignSubscriptionWithResponse(input: SaveDirectedCampaignSubscriptionInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveDirectedCampaignSubscriptionResult>> { return this.requestDetailed("save_directed_campaign_subscription", input, options) }
  /**
   * Sync first-party CRM audiences for a buyer advertiser. Each audiences[] item may add, remove, or delete members. Returns an operationId; use get(kind: audience, advertiserId: "...") to read match status after it settles.
   *
   * @example
   * await client.saveAudience(input, { idempotencyKey: 'stable-key' })
   */
  saveAudience(input: SaveAudienceInput, options: WriteRequestOptions): Promise<SaveAudienceResult> { return this.request("save_audience", input, options) }

  /** Sync first-party CRM audiences for a buyer advertiser. Each audiences[] item may add, remove, or delete members. Returns an operationId; use get(kind: audience, advertiserId: "...") to read match status after it settles. Returns the data together with response headers and request ID. */
  saveAudienceWithResponse(input: SaveAudienceInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAudienceResult>> { return this.requestDetailed("save_audience", input, options) }
  /**
   * Save a campaign. Create needs advertiserId and name; flight and budget are optional. Split inventory choices into separate media buys; presets expand dimensions. To launch, set desiredPhase: active with confirmLaunch: true; omit confirmation to preview. Cancellation never cancels media buys.
   *
   * @example
   * await client.saveCampaign(input, { idempotencyKey: 'stable-key' })
   */
  saveCampaign(input: SaveCampaignInput, options: WriteRequestOptions): Promise<SaveCampaignResult> { return this.request("save_campaign", input, options) }

  /** Save a campaign. Create needs advertiserId and name; flight and budget are optional. Split inventory choices into separate media buys; presets expand dimensions. To launch, set desiredPhase: active with confirmLaunch: true; omit confirmation to preview. Cancellation never cancels media buys. Returns the data together with response headers and request ID. */
  saveCampaignWithResponse(input: SaveCampaignInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCampaignResult>> { return this.requestDetailed("save_campaign", input, options) }
  /**
   * Create or replace one flat catalog declaration by catalogId, or archive it with isArchived. URL saves refetch the feed.
   *
   * @example
   * await client.saveCatalog(input, { idempotencyKey: 'stable-key' })
   */
  saveCatalog(input: SaveCatalogInput, options: WriteRequestOptions): Promise<SaveCatalogResult> { return this.request("save_catalog", input, options) }

  /** Create or replace one flat catalog declaration by catalogId, or archive it with isArchived. URL saves refetch the feed. Returns the data together with response headers and request ID. */
  saveCatalogWithResponse(input: SaveCatalogInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCatalogResult>> { return this.requestDetailed("save_catalog", input, options) }
  /**
   * Create, change, archive, or restore up to 50 advertiser conversion event sources (pixels, server feeds). Each entry is keyed by eventSourceId and succeeds or fails alone. Setup is not proof events flow: check health with get, then use eventSourceId in an optimization goal.
   *
   * @example
   * await client.saveEventSource(input, { idempotencyKey: 'stable-key' })
   */
  saveEventSource(input: SaveEventSourceInput, options: WriteRequestOptions): Promise<SaveEventSourceResult> { return this.request("save_event_source", input, options) }

  /** Create, change, archive, or restore up to 50 advertiser conversion event sources (pixels, server feeds). Each entry is keyed by eventSourceId and succeeds or fails alone. Setup is not proof events flow: check health with get, then use eventSourceId in an optimization goal. Returns the data together with response headers and request ID. */
  saveEventSourceWithResponse(input: SaveEventSourceInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveEventSourceResult>> { return this.requestDetailed("save_event_source", input, options) }
  /**
   * Create a dimension, or update an existing dimension by its id. Tags is built in and open. Labels belong only to objects in appliesTo.
   *
   * @example
   * await client.saveDimension(input, { idempotencyKey: 'stable-key' })
   */
  saveDimension(input: SaveDimensionInput, options: WriteRequestOptions): Promise<SaveDimensionResult> { return this.request("save_dimension", input, options) }

  /** Create a dimension, or update an existing dimension by its id. Tags is built in and open. Labels belong only to objects in appliesTo. Returns the data together with response headers and request ID. */
  saveDimensionWithResponse(input: SaveDimensionInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveDimensionResult>> { return this.requestDetailed("save_dimension", input, options) }
  /**
   * Create, update, archive, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists.
   *
   * @example
   * await client.savePropertyList(input, { idempotencyKey: 'stable-key' })
   */
  savePropertyList(input: SavePropertyListInput, options: WriteRequestOptions): Promise<SavePropertyListResult> { return this.request("save_property_list", input, options) }

  /** Create, update, archive, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists. Returns the data together with response headers and request ID. */
  savePropertyListWithResponse(input: SavePropertyListInput, options: WriteRequestOptions): Promise<ResponseDetails<SavePropertyListResult>> { return this.requestDetailed("save_property_list", input, options) }
  /**
   * Save creative in advertiserId/campaignId with name, message, assets, clickUrl, social, sourceAssetRef/sourceAssets. Use exactly one format selector: formatKind/formatParams, creativeFormatId, formatOptionRef. Supplied content/assets only; generate new media (radio spots) via save_creative_session.
   *
   * @example
   * await client.saveCreative(input, { idempotencyKey: 'stable-key' })
   */
  saveCreative(input: SaveCreativeInput, options: WriteRequestOptions): Promise<SaveCreativeResult> { return this.request("save_creative", input, options) }

  /** Save creative in advertiserId/campaignId with name, message, assets, clickUrl, social, sourceAssetRef/sourceAssets. Use exactly one format selector: formatKind/formatParams, creativeFormatId, formatOptionRef. Supplied content/assets only; generate new media (radio spots) via save_creative_session. Returns the data together with response headers and request ID. */
  saveCreativeWithResponse(input: SaveCreativeInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCreativeResult>> { return this.requestDetailed("save_creative", input, options) }
  /**
   * Manage collections. Create with one owner and name: campaignId or advertiserId. Only advertiser mutations of an existing collection need expectedUpdatedAt; campaign writes and creates do not. isArchived archives or restores advertiser collections.
   *
   * @example
   * await client.saveCreativeCollection(input, { idempotencyKey: 'stable-key' })
   */
  saveCreativeCollection(input: SaveCreativeCollectionInput, options: WriteRequestOptions): Promise<SaveCreativeCollectionResult> { return this.request("save_creative_collection", input, options) }

  /** Manage collections. Create with one owner and name: campaignId or advertiserId. Only advertiser mutations of an existing collection need expectedUpdatedAt; campaign writes and creates do not. isArchived archives or restores advertiser collections. Returns the data together with response headers and request ID. */
  saveCreativeCollectionWithResponse(input: SaveCreativeCollectionInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCreativeCollectionResult>> { return this.requestDetailed("save_creative_collection", input, options) }
  /**
   * Save a Creative Session to generate new image, hosted video, or voice/audio (radio spots, voiceovers) from a brief, plus selection, approval, finalisation, or Library promotion. Creative Engines is required; use save_creative for supplied content and assets. Never generates variants.
   *
   * @example
   * await client.saveCreativeSession(input, { idempotencyKey: 'stable-key' })
   */
  saveCreativeSession(input: SaveCreativeSessionInput, options: WriteRequestOptions): Promise<SaveCreativeSessionResult> { return this.request("save_creative_session", input, options) }

  /** Save a Creative Session to generate new image, hosted video, or voice/audio (radio spots, voiceovers) from a brief, plus selection, approval, finalisation, or Library promotion. Creative Engines is required; use save_creative for supplied content and assets. Never generates variants. Returns the data together with response headers and request ID. */
  saveCreativeSessionWithResponse(input: SaveCreativeSessionInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCreativeSessionResult>> { return this.requestDetailed("save_creative_session", input, options) }
  /**
   * Generate or refine new image, hosted video, or voice/audio (radio spots, voiceovers) from a saved Creative Engines brief. Reuse actionKey for an identical retry.
   *
   * @example
   * await client.generateVariants(input, { idempotencyKey: 'stable-key' })
   */
  generateVariants(input: GenerateVariantsInput, options: WriteRequestOptions): Promise<GenerateVariantsResult> { return this.request("generate_variants", input, options) }

  /** Generate or refine new image, hosted video, or voice/audio (radio spots, voiceovers) from a saved Creative Engines brief. Reuse actionKey for an identical retry. Returns the data together with response headers and request ID. */
  generateVariantsWithResponse(input: GenerateVariantsInput, options: WriteRequestOptions): Promise<ResponseDetails<GenerateVariantsResult>> { return this.requestDetailed("generate_variants", input, options) }
  /**
   * Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit buy/product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates.
   *
   * @example
   * await client.saveMediaBuy(input, { idempotencyKey: 'stable-key' })
   */
  saveMediaBuy(input: SaveMediaBuyInput, options: WriteRequestOptions): Promise<SaveMediaBuyResult> { return this.request("save_media_buy", input, options) }

  /** Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit buy/product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates. Returns the data together with response headers and request ID. */
  saveMediaBuyWithResponse(input: SaveMediaBuyInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveMediaBuyResult>> { return this.requestDetailed("save_media_buy", input, options) }
  /**
   * Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true.
   *
   * @example
   * await client.requestProposals(input, { idempotencyKey: 'stable-key' })
   */
  requestProposals(input: RequestProposalsInput, options: WriteRequestOptions): Promise<RequestProposalsResult> { return this.request("request_proposals", input, options) }

  /** Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true. Returns the data together with response headers and request ID. */
  requestProposalsWithResponse(input: RequestProposalsInput, options: WriteRequestOptions): Promise<ResponseDetails<RequestProposalsResult>> { return this.requestDetailed("request_proposals", input, options) }
}
