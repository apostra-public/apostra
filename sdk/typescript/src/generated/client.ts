// Generated. Do not edit.
import type * as Wire from './types.gen.js'
import { Transport, type RequestOptions, type ResponseDetails, type WriteRequestOptions } from '../transport.js'
type OptionalWireField<T, K extends PropertyKey> = T extends unknown ? Omit<T, K> & Partial<Pick<T, Extract<K, keyof T>>> : never
export type ConfirmPaymentAuthorityInput = Wire.ConfirmPaymentAuthorityData['body']
export type ConfirmPaymentAuthorityResult = Wire.ConfirmPaymentAuthorityResponses[200]['data']
export type ConfirmPaymentAuthorityError = Wire.ConfirmPaymentAuthorityErrors[keyof Wire.ConfirmPaymentAuthorityErrors]

export type DownloadV3PublicDocumentRevisionInput = { "documentId": NonNullable<Wire.DownloadV3PublicDocumentRevisionData['path']>["documentId"]; "revisionId": NonNullable<Wire.DownloadV3PublicDocumentRevisionData['path']>["revisionId"] }
export type DownloadV3PublicDocumentRevisionResult = Uint8Array
export type DownloadV3PublicDocumentRevisionError = Wire.DownloadV3PublicDocumentRevisionErrors[keyof Wire.DownloadV3PublicDocumentRevisionErrors]

export type GenerateVariantsInput = Wire.GenerateVariantsData['body']
export type GenerateVariantsResult = Wire.GenerateVariantsResponses[200]['data']
export type GenerateVariantsError = Wire.GenerateVariantsErrors[keyof Wire.GenerateVariantsErrors]

export type GetInput = Wire.GetData['body']
export type GetResult = Wire.GetResponses[200]['data']
export type GetError = Wire.GetErrors[keyof Wire.GetErrors]

export type GetV3PublicDocumentRevisionSectionsInput = { "documentId": NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['path']>["documentId"]; "revisionId": NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['path']>["revisionId"]; "section"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["section"]; "query"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["query"]; "cursor"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["cursor"]; "asOf"?: NonNullable<Wire.GetV3PublicDocumentRevisionSectionsData['query']>["asOf"] }
export type GetV3PublicDocumentRevisionSectionsResult = Wire.GetV3PublicDocumentRevisionSectionsResponses[200]['data']
export type GetV3PublicDocumentRevisionSectionsError = Wire.GetV3PublicDocumentRevisionSectionsErrors[keyof Wire.GetV3PublicDocumentRevisionSectionsErrors]

export type GetV3PublicMutationReceiptInput = { "receiptId": NonNullable<Wire.GetV3PublicMutationReceiptData['path']>["receiptId"] }
export type GetV3PublicMutationReceiptResult = Wire.GetV3PublicMutationReceiptResponses[200]['data']
export type GetV3PublicMutationReceiptError = Wire.GetV3PublicMutationReceiptErrors[keyof Wire.GetV3PublicMutationReceiptErrors]

export type GetDeliveryInput = Wire.GetDeliveryData['body']
export type GetDeliveryResult = Wire.GetDeliveryResponses[200]['data']
export type GetDeliveryError = Wire.GetDeliveryErrors[keyof Wire.GetDeliveryErrors]

export type GetRfpPerformanceInput = Wire.GetRfpPerformanceData['body']
export type GetRfpPerformanceResult = Wire.GetRfpPerformanceResponses[200]['data']
export type GetRfpPerformanceError = Wire.GetRfpPerformanceErrors[keyof Wire.GetRfpPerformanceErrors]

export type GetSellerReportingReceiptsInput = Wire.GetSellerReportingReceiptsData['body']
export type GetSellerReportingReceiptsResult = Wire.GetSellerReportingReceiptsResponses[200]['data']
export type GetSellerReportingReceiptsError = Wire.GetSellerReportingReceiptsErrors[keyof Wire.GetSellerReportingReceiptsErrors]

export type GetStatusInput = Wire.GetStatusData['body']
export type GetStatusResult = Wire.GetStatusResponses[200]['data']
export type GetStatusError = Wire.GetStatusErrors[keyof Wire.GetStatusErrors]

export type LogEventInput = OptionalWireField<Wire.LogEventData['body'], "idempotencyKey">
export type LogEventResult = Wire.LogEventResponses[200]['data']
export type LogEventError = Wire.LogEventErrors[keyof Wire.LogEventErrors]

export type OpenAdvertisersPageInput = Wire.OpenAdvertisersPageData['body']
export type OpenAdvertisersPageResult = Wire.OpenAdvertisersPageResponses[200]['data']
export type OpenAdvertisersPageError = Wire.OpenAdvertisersPageErrors[keyof Wire.OpenAdvertisersPageErrors]

export type OpenAgentCertificationPageInput = Wire.OpenAgentCertificationPageData['body']
export type OpenAgentCertificationPageResult = Wire.OpenAgentCertificationPageResponses[200]['data']
export type OpenAgentCertificationPageError = Wire.OpenAgentCertificationPageErrors[keyof Wire.OpenAgentCertificationPageErrors]

export type OpenAgentPageInput = Wire.OpenAgentPageData['body']
export type OpenAgentPageResult = Wire.OpenAgentPageResponses[200]['data']
export type OpenAgentPageError = Wire.OpenAgentPageErrors[keyof Wire.OpenAgentPageErrors]

export type OpenAgentSourcesPageInput = Wire.OpenAgentSourcesPageData['body']
export type OpenAgentSourcesPageResult = Wire.OpenAgentSourcesPageResponses[200]['data']
export type OpenAgentSourcesPageError = Wire.OpenAgentSourcesPageErrors[keyof Wire.OpenAgentSourcesPageErrors]

export type OpenAgentWebhooksPageInput = Wire.OpenAgentWebhooksPageData['body']
export type OpenAgentWebhooksPageResult = Wire.OpenAgentWebhooksPageResponses[200]['data']
export type OpenAgentWebhooksPageError = Wire.OpenAgentWebhooksPageErrors[keyof Wire.OpenAgentWebhooksPageErrors]

export type OpenAgentsPageInput = Wire.OpenAgentsPageData['body']
export type OpenAgentsPageResult = Wire.OpenAgentsPageResponses[200]['data']
export type OpenAgentsPageError = Wire.OpenAgentsPageErrors[keyof Wire.OpenAgentsPageErrors]

export type OpenApprovalsInput = Wire.OpenApprovalsData['body']
export type OpenApprovalsResult = Wire.OpenApprovalsResponses[200]['data']
export type OpenApprovalsError = Wire.OpenApprovalsErrors[keyof Wire.OpenApprovalsErrors]

export type OpenCampaignReceiptInput = Wire.OpenCampaignReceiptData['body']
export type OpenCampaignReceiptResult = Wire.OpenCampaignReceiptResponses[200]['data']
export type OpenCampaignReceiptError = Wire.OpenCampaignReceiptErrors[keyof Wire.OpenCampaignReceiptErrors]

export type OpenCampaignsPageInput = Wire.OpenCampaignsPageData['body']
export type OpenCampaignsPageResult = Wire.OpenCampaignsPageResponses[200]['data']
export type OpenCampaignsPageError = Wire.OpenCampaignsPageErrors[keyof Wire.OpenCampaignsPageErrors]

export type OpenConnectionsPageInput = Wire.OpenConnectionsPageData['body']
export type OpenConnectionsPageResult = Wire.OpenConnectionsPageResponses[200]['data']
export type OpenConnectionsPageError = Wire.OpenConnectionsPageErrors[keyof Wire.OpenConnectionsPageErrors]

export type OpenCreativeEnginesPageInput = Wire.OpenCreativeEnginesPageData['body']
export type OpenCreativeEnginesPageResult = Wire.OpenCreativeEnginesPageResponses[200]['data']
export type OpenCreativeEnginesPageError = Wire.OpenCreativeEnginesPageErrors[keyof Wire.OpenCreativeEnginesPageErrors]

export type OpenCreativeLibraryInput = Wire.OpenCreativeLibraryData['body']
export type OpenCreativeLibraryResult = Wire.OpenCreativeLibraryResponses[200]['data']
export type OpenCreativeLibraryError = Wire.OpenCreativeLibraryErrors[keyof Wire.OpenCreativeLibraryErrors]

export type OpenDeveloperHomeInput = Wire.OpenDeveloperHomeData['body']
export type OpenDeveloperHomeResult = Wire.OpenDeveloperHomeResponses[200]['data']
export type OpenDeveloperHomeError = Wire.OpenDeveloperHomeErrors[keyof Wire.OpenDeveloperHomeErrors]

export type OpenMediaBuysPageInput = Wire.OpenMediaBuysPageData['body']
export type OpenMediaBuysPageResult = Wire.OpenMediaBuysPageResponses[200]['data']
export type OpenMediaBuysPageError = Wire.OpenMediaBuysPageErrors[keyof Wire.OpenMediaBuysPageErrors]

export type OpenMediaPartnersPageInput = Wire.OpenMediaPartnersPageData['body']
export type OpenMediaPartnersPageResult = Wire.OpenMediaPartnersPageResponses[200]['data']
export type OpenMediaPartnersPageError = Wire.OpenMediaPartnersPageErrors[keyof Wire.OpenMediaPartnersPageErrors]

export type OpenPageInput = Wire.OpenPageData['body']
export type OpenPageResult = Wire.OpenPageResponses[200]['data']
export type OpenPageError = Wire.OpenPageErrors[keyof Wire.OpenPageErrors]

export type OpenProposalPassInput = Wire.OpenProposalPassData['body']
export type OpenProposalPassResult = Wire.OpenProposalPassResponses[200]['data']
export type OpenProposalPassError = Wire.OpenProposalPassErrors[keyof Wire.OpenProposalPassErrors]

export type OpenSellerDashboardInput = Wire.OpenSellerDashboardData['body']
export type OpenSellerDashboardResult = Wire.OpenSellerDashboardResponses[200]['data']
export type OpenSellerDashboardError = Wire.OpenSellerDashboardErrors[keyof Wire.OpenSellerDashboardErrors]

export type OpenVariantGalleryInput = Wire.OpenVariantGalleryData['body']
export type OpenVariantGalleryResult = Wire.OpenVariantGalleryResponses[200]['data']
export type OpenVariantGalleryError = Wire.OpenVariantGalleryErrors[keyof Wire.OpenVariantGalleryErrors]

export type RefreshInventorySourceHealthInput = Wire.RefreshInventorySourceHealthData['body']
export type RefreshInventorySourceHealthResult = Wire.RefreshInventorySourceHealthResponses[200]['data']
export type RefreshInventorySourceHealthError = Wire.RefreshInventorySourceHealthErrors[keyof Wire.RefreshInventorySourceHealthErrors]

export type RequestBuyerChildAccountInput = OptionalWireField<Wire.RequestBuyerChildAccountData['body'], "idempotencyKey">
export type RequestBuyerChildAccountResult = Wire.RequestBuyerChildAccountResponses[200]['data']
export type RequestBuyerChildAccountError = Wire.RequestBuyerChildAccountErrors[keyof Wire.RequestBuyerChildAccountErrors]

export type RequestPaymentAuthorityInput = Wire.RequestPaymentAuthorityData['body']
export type RequestPaymentAuthorityResult = Wire.RequestPaymentAuthorityResponses[200]['data']
export type RequestPaymentAuthorityError = Wire.RequestPaymentAuthorityErrors[keyof Wire.RequestPaymentAuthorityErrors]

export type RequestProposalsInput = OptionalWireField<Wire.RequestProposalsData['body'], "idempotencyKey">
export type RequestProposalsResult = Wire.RequestProposalsResponses[200]['data']
export type RequestProposalsError = Wire.RequestProposalsErrors[keyof Wire.RequestProposalsErrors]

export type RequestSellerReportingUpdateInput = Wire.RequestSellerReportingUpdateData['body']
export type RequestSellerReportingUpdateResult = Wire.RequestSellerReportingUpdateResponses[200]['data']
export type RequestSellerReportingUpdateError = Wire.RequestSellerReportingUpdateErrors[keyof Wire.RequestSellerReportingUpdateErrors]

export type ReviewBuyerChildAccountInput = Wire.ReviewBuyerChildAccountData['body']
export type ReviewBuyerChildAccountResult = Wire.ReviewBuyerChildAccountResponses[200]['data']
export type ReviewBuyerChildAccountError = Wire.ReviewBuyerChildAccountErrors[keyof Wire.ReviewBuyerChildAccountErrors]

export type SaveAccountInput = Wire.SaveAccountData['body']
export type SaveAccountResult = Wire.SaveAccountResponses[200]['data']
export type SaveAccountError = Wire.SaveAccountErrors[keyof Wire.SaveAccountErrors]

export type SaveAdvertiserInput = Wire.SaveAdvertiserData['body']
export type SaveAdvertiserResult = Wire.SaveAdvertiserResponses[200]['data']
export type SaveAdvertiserError = Wire.SaveAdvertiserErrors[keyof Wire.SaveAdvertiserErrors]

export type SaveAdvertiserGrantInput = Wire.SaveAdvertiserGrantData['body']
export type SaveAdvertiserGrantResult = Wire.SaveAdvertiserGrantResponses[200]['data']
export type SaveAdvertiserGrantError = Wire.SaveAdvertiserGrantErrors[keyof Wire.SaveAdvertiserGrantErrors]

export type SaveAdvertiserInstructionsInput = Wire.SaveAdvertiserInstructionsData['body']
export type SaveAdvertiserInstructionsResult = Wire.SaveAdvertiserInstructionsResponses[200]['data']
export type SaveAdvertiserInstructionsError = Wire.SaveAdvertiserInstructionsErrors[keyof Wire.SaveAdvertiserInstructionsErrors]

export type SaveAgentInput = Wire.SaveAgentData['body']
export type SaveAgentResult = Wire.SaveAgentResponses[200]['data']
export type SaveAgentError = Wire.SaveAgentErrors[keyof Wire.SaveAgentErrors]

export type SaveAskInput = Wire.SaveAskData['body']
export type SaveAskResult = Wire.SaveAskResponses[200]['data']
export type SaveAskError = Wire.SaveAskErrors[keyof Wire.SaveAskErrors]

export type SaveAudienceInput = Wire.SaveAudienceData['body']
export type SaveAudienceResult = Wire.SaveAudienceResponses[200]['data']
export type SaveAudienceError = Wire.SaveAudienceErrors[keyof Wire.SaveAudienceErrors]

export type SaveBillingInput = Wire.SaveBillingData['body']
export type SaveBillingResult = Wire.SaveBillingResponses[200]['data']
export type SaveBillingError = Wire.SaveBillingErrors[keyof Wire.SaveBillingErrors]

export type SaveBusinessRulesInput = Wire.SaveBusinessRulesData['body']
export type SaveBusinessRulesResult = Wire.SaveBusinessRulesResponses[200]['data']
export type SaveBusinessRulesError = Wire.SaveBusinessRulesErrors[keyof Wire.SaveBusinessRulesErrors]

export type SaveBuyerAgentInput = Wire.SaveBuyerAgentData['body']
export type SaveBuyerAgentResult = Wire.SaveBuyerAgentResponses[200]['data']
export type SaveBuyerAgentError = Wire.SaveBuyerAgentErrors[keyof Wire.SaveBuyerAgentErrors]

export type SaveBuyerOperatorInput = Wire.SaveBuyerOperatorData['body']
export type SaveBuyerOperatorResult = Wire.SaveBuyerOperatorResponses[200]['data']
export type SaveBuyerOperatorError = Wire.SaveBuyerOperatorErrors[keyof Wire.SaveBuyerOperatorErrors]

export type SaveCampaignInput = OptionalWireField<Wire.SaveCampaignData['body'], "idempotencyKey">
export type SaveCampaignResult = Wire.SaveCampaignResponses[200]['data']
export type SaveCampaignError = Wire.SaveCampaignErrors[keyof Wire.SaveCampaignErrors]

export type SaveCatalogInput = OptionalWireField<Wire.SaveCatalogData['body'], "idempotencyKey">
export type SaveCatalogResult = Wire.SaveCatalogResponses[200]['data']
export type SaveCatalogError = Wire.SaveCatalogErrors[keyof Wire.SaveCatalogErrors]

export type SaveConnectionInput = Wire.SaveConnectionData['body']
export type SaveConnectionResult = Wire.SaveConnectionResponses[200]['data']
export type SaveConnectionError = Wire.SaveConnectionErrors[keyof Wire.SaveConnectionErrors]

export type SaveCoverageInput = Wire.SaveCoverageData['body']
export type SaveCoverageResult = Wire.SaveCoverageResponses[200]['data']
export type SaveCoverageError = Wire.SaveCoverageErrors[keyof Wire.SaveCoverageErrors]

export type SaveCreativeInput = Wire.SaveCreativeData['body']
export type SaveCreativeResult = Wire.SaveCreativeResponses[200]['data']
export type SaveCreativeError = Wire.SaveCreativeErrors[keyof Wire.SaveCreativeErrors]

export type SaveCreativeCollectionInput = Wire.SaveCreativeCollectionData['body']
export type SaveCreativeCollectionResult = Wire.SaveCreativeCollectionResponses[200]['data']
export type SaveCreativeCollectionError = Wire.SaveCreativeCollectionErrors[keyof Wire.SaveCreativeCollectionErrors]

export type SaveCreativeSessionInput = Wire.SaveCreativeSessionData['body']
export type SaveCreativeSessionResult = Wire.SaveCreativeSessionResponses[200]['data']
export type SaveCreativeSessionError = Wire.SaveCreativeSessionErrors[keyof Wire.SaveCreativeSessionErrors]

export type SaveDimensionInput = OptionalWireField<Wire.SaveDimensionData['body'], "idempotencyKey">
export type SaveDimensionResult = Wire.SaveDimensionResponses[200]['data']
export type SaveDimensionError = Wire.SaveDimensionErrors[keyof Wire.SaveDimensionErrors]

export type SaveDirectedCampaignSubscriptionInput = Wire.SaveDirectedCampaignSubscriptionData['body']
export type SaveDirectedCampaignSubscriptionResult = Wire.SaveDirectedCampaignSubscriptionResponses[200]['data']
export type SaveDirectedCampaignSubscriptionError = Wire.SaveDirectedCampaignSubscriptionErrors[keyof Wire.SaveDirectedCampaignSubscriptionErrors]

export type SaveEventSourceInput = OptionalWireField<Wire.SaveEventSourceData['body'], "idempotencyKey">
export type SaveEventSourceResult = Wire.SaveEventSourceResponses[200]['data']
export type SaveEventSourceError = Wire.SaveEventSourceErrors[keyof Wire.SaveEventSourceErrors]

export type SaveInventorySourceInput = Wire.SaveInventorySourceData['body']
export type SaveInventorySourceResult = Wire.SaveInventorySourceResponses[200]['data']
export type SaveInventorySourceError = Wire.SaveInventorySourceErrors[keyof Wire.SaveInventorySourceErrors]

export type SaveLessonInput = Wire.SaveLessonData['body']
export type SaveLessonResult = Wire.SaveLessonResponses[200]['data']
export type SaveLessonError = Wire.SaveLessonErrors[keyof Wire.SaveLessonErrors]

export type SaveLibraryRequestInput = Wire.SaveLibraryRequestData['body']
export type SaveLibraryRequestResult = Wire.SaveLibraryRequestResponses[200]['data']
export type SaveLibraryRequestError = Wire.SaveLibraryRequestErrors[keyof Wire.SaveLibraryRequestErrors]

export type SaveMaterialInput = Wire.SaveMaterialData['body']
export type SaveMaterialResult = Wire.SaveMaterialResponses[200]['data']
export type SaveMaterialError = Wire.SaveMaterialErrors[keyof Wire.SaveMaterialErrors]

export type SaveMediaBuyInput = OptionalWireField<Wire.SaveMediaBuyData['body'], "idempotencyKey">
export type SaveMediaBuyResult = Wire.SaveMediaBuyResponses[200]['data']
export type SaveMediaBuyError = Wire.SaveMediaBuyErrors[keyof Wire.SaveMediaBuyErrors]

export type SaveMediaKitInput = Wire.SaveMediaKitData['body']
export type SaveMediaKitResult = Wire.SaveMediaKitResponses[200]['data']
export type SaveMediaKitError = Wire.SaveMediaKitErrors[keyof Wire.SaveMediaKitErrors]

export type SaveNotificationConfigInput = Wire.SaveNotificationConfigData['body']
export type SaveNotificationConfigResult = Wire.SaveNotificationConfigResponses[200]['data']
export type SaveNotificationConfigError = Wire.SaveNotificationConfigErrors[keyof Wire.SaveNotificationConfigErrors]

export type SavePlaybookInput = Wire.SavePlaybookData['body']
export type SavePlaybookResult = Wire.SavePlaybookResponses[200]['data']
export type SavePlaybookError = Wire.SavePlaybookErrors[keyof Wire.SavePlaybookErrors]

export type SavePropertyListInput = Wire.SavePropertyListData['body']
export type SavePropertyListResult = Wire.SavePropertyListResponses[200]['data']
export type SavePropertyListError = Wire.SavePropertyListErrors[keyof Wire.SavePropertyListErrors]

export type SaveRfpInput = OptionalWireField<Wire.SaveRfpData['body'], "clientRequestId">
export type SaveRfpResult = Wire.SaveRfpResponses[200]['data']
export type SaveRfpError = Wire.SaveRfpErrors[keyof Wire.SaveRfpErrors]

export type SaveRfpTurnInput = OptionalWireField<Wire.SaveRfpTurnData['body'], "clientRequestId">
export type SaveRfpTurnResult = Wire.SaveRfpTurnResponses[200]['data']
export type SaveRfpTurnError = Wire.SaveRfpTurnErrors[keyof Wire.SaveRfpTurnErrors]

export type SaveSellerInput = Wire.SaveSellerData['body']
export type SaveSellerResult = Wire.SaveSellerResponses[200]['data']
export type SaveSellerError = Wire.SaveSellerErrors[keyof Wire.SaveSellerErrors]

export type SaveSignalInput = Wire.SaveSignalData['body']
export type SaveSignalResult = Wire.SaveSignalResponses[200]['data']
export type SaveSignalError = Wire.SaveSignalErrors[keyof Wire.SaveSignalErrors]

export type SaveWholesaleProductInput = Wire.SaveWholesaleProductData['body']
export type SaveWholesaleProductResult = Wire.SaveWholesaleProductResponses[200]['data']
export type SaveWholesaleProductError = Wire.SaveWholesaleProductErrors[keyof Wire.SaveWholesaleProductErrors]

export type SaveWorkItemInput = Wire.SaveWorkItemData['body']
export type SaveWorkItemResult = Wire.SaveWorkItemResponses[200]['data']
export type SaveWorkItemError = Wire.SaveWorkItemErrors[keyof Wire.SaveWorkItemErrors]

export type SearchInput = Wire.SearchData['body']
export type SearchResult = Wire.SearchResponses[200]['data']
export type SearchError = Wire.SearchErrors[keyof Wire.SearchErrors]

export type TestCreativeMacrosInput = Wire.TestCreativeMacrosData['body']
export type TestCreativeMacrosResult = Wire.TestCreativeMacrosResponses[200]['data']
export type TestCreativeMacrosError = Wire.TestCreativeMacrosErrors[keyof Wire.TestCreativeMacrosErrors]

export type UploadCreativeAssetInput = Wire.UploadCreativeAssetData['body']
export type UploadCreativeAssetResult = Wire.UploadCreativeAssetResponses[200]['data']
export type UploadCreativeAssetError = Wire.UploadCreativeAssetErrors[keyof Wire.UploadCreativeAssetErrors]

export interface OperationTypes { "confirm_payment_authority": { input: ConfirmPaymentAuthorityInput; result: ConfirmPaymentAuthorityResult }; "downloadV3PublicDocumentRevision": { input: DownloadV3PublicDocumentRevisionInput; result: DownloadV3PublicDocumentRevisionResult }; "generate_variants": { input: GenerateVariantsInput; result: GenerateVariantsResult }; "get": { input: GetInput; result: GetResult }; "getV3PublicDocumentRevisionSections": { input: GetV3PublicDocumentRevisionSectionsInput; result: GetV3PublicDocumentRevisionSectionsResult }; "getV3PublicMutationReceipt": { input: GetV3PublicMutationReceiptInput; result: GetV3PublicMutationReceiptResult }; "get_delivery": { input: GetDeliveryInput; result: GetDeliveryResult }; "get_rfp_performance": { input: GetRfpPerformanceInput; result: GetRfpPerformanceResult }; "get_seller_reporting_receipts": { input: GetSellerReportingReceiptsInput; result: GetSellerReportingReceiptsResult }; "get_status": { input: GetStatusInput; result: GetStatusResult }; "log_event": { input: LogEventInput; result: LogEventResult }; "open_advertisers_page": { input: OpenAdvertisersPageInput; result: OpenAdvertisersPageResult }; "open_agent_certification_page": { input: OpenAgentCertificationPageInput; result: OpenAgentCertificationPageResult }; "open_agent_page": { input: OpenAgentPageInput; result: OpenAgentPageResult }; "open_agent_sources_page": { input: OpenAgentSourcesPageInput; result: OpenAgentSourcesPageResult }; "open_agent_webhooks_page": { input: OpenAgentWebhooksPageInput; result: OpenAgentWebhooksPageResult }; "open_agents_page": { input: OpenAgentsPageInput; result: OpenAgentsPageResult }; "open_approvals": { input: OpenApprovalsInput; result: OpenApprovalsResult }; "open_campaign_receipt": { input: OpenCampaignReceiptInput; result: OpenCampaignReceiptResult }; "open_campaigns_page": { input: OpenCampaignsPageInput; result: OpenCampaignsPageResult }; "open_connections_page": { input: OpenConnectionsPageInput; result: OpenConnectionsPageResult }; "open_creative_engines_page": { input: OpenCreativeEnginesPageInput; result: OpenCreativeEnginesPageResult }; "open_creative_library": { input: OpenCreativeLibraryInput; result: OpenCreativeLibraryResult }; "open_developer_home": { input: OpenDeveloperHomeInput; result: OpenDeveloperHomeResult }; "open_media_buys_page": { input: OpenMediaBuysPageInput; result: OpenMediaBuysPageResult }; "open_media_partners_page": { input: OpenMediaPartnersPageInput; result: OpenMediaPartnersPageResult }; "open_page": { input: OpenPageInput; result: OpenPageResult }; "open_proposal_pass": { input: OpenProposalPassInput; result: OpenProposalPassResult }; "open_seller_dashboard": { input: OpenSellerDashboardInput; result: OpenSellerDashboardResult }; "open_variant_gallery": { input: OpenVariantGalleryInput; result: OpenVariantGalleryResult }; "refresh_inventory_source_health": { input: RefreshInventorySourceHealthInput; result: RefreshInventorySourceHealthResult }; "request_buyer_child_account": { input: RequestBuyerChildAccountInput; result: RequestBuyerChildAccountResult }; "request_payment_authority": { input: RequestPaymentAuthorityInput; result: RequestPaymentAuthorityResult }; "request_proposals": { input: RequestProposalsInput; result: RequestProposalsResult }; "request_seller_reporting_update": { input: RequestSellerReportingUpdateInput; result: RequestSellerReportingUpdateResult }; "review_buyer_child_account": { input: ReviewBuyerChildAccountInput; result: ReviewBuyerChildAccountResult }; "save_account": { input: SaveAccountInput; result: SaveAccountResult }; "save_advertiser": { input: SaveAdvertiserInput; result: SaveAdvertiserResult }; "save_advertiser_grant": { input: SaveAdvertiserGrantInput; result: SaveAdvertiserGrantResult }; "save_advertiser_instructions": { input: SaveAdvertiserInstructionsInput; result: SaveAdvertiserInstructionsResult }; "save_agent": { input: SaveAgentInput; result: SaveAgentResult }; "save_ask": { input: SaveAskInput; result: SaveAskResult }; "save_audience": { input: SaveAudienceInput; result: SaveAudienceResult }; "save_billing": { input: SaveBillingInput; result: SaveBillingResult }; "save_business_rules": { input: SaveBusinessRulesInput; result: SaveBusinessRulesResult }; "save_buyer_agent": { input: SaveBuyerAgentInput; result: SaveBuyerAgentResult }; "save_buyer_operator": { input: SaveBuyerOperatorInput; result: SaveBuyerOperatorResult }; "save_campaign": { input: SaveCampaignInput; result: SaveCampaignResult }; "save_catalog": { input: SaveCatalogInput; result: SaveCatalogResult }; "save_connection": { input: SaveConnectionInput; result: SaveConnectionResult }; "save_coverage": { input: SaveCoverageInput; result: SaveCoverageResult }; "save_creative": { input: SaveCreativeInput; result: SaveCreativeResult }; "save_creative_collection": { input: SaveCreativeCollectionInput; result: SaveCreativeCollectionResult }; "save_creative_session": { input: SaveCreativeSessionInput; result: SaveCreativeSessionResult }; "save_dimension": { input: SaveDimensionInput; result: SaveDimensionResult }; "save_directed_campaign_subscription": { input: SaveDirectedCampaignSubscriptionInput; result: SaveDirectedCampaignSubscriptionResult }; "save_event_source": { input: SaveEventSourceInput; result: SaveEventSourceResult }; "save_inventory_source": { input: SaveInventorySourceInput; result: SaveInventorySourceResult }; "save_lesson": { input: SaveLessonInput; result: SaveLessonResult }; "save_library_request": { input: SaveLibraryRequestInput; result: SaveLibraryRequestResult }; "save_material": { input: SaveMaterialInput; result: SaveMaterialResult }; "save_media_buy": { input: SaveMediaBuyInput; result: SaveMediaBuyResult }; "save_media_kit": { input: SaveMediaKitInput; result: SaveMediaKitResult }; "save_notification_config": { input: SaveNotificationConfigInput; result: SaveNotificationConfigResult }; "save_playbook": { input: SavePlaybookInput; result: SavePlaybookResult }; "save_property_list": { input: SavePropertyListInput; result: SavePropertyListResult }; "save_rfp": { input: SaveRfpInput; result: SaveRfpResult }; "save_rfp_turn": { input: SaveRfpTurnInput; result: SaveRfpTurnResult }; "save_seller": { input: SaveSellerInput; result: SaveSellerResult }; "save_signal": { input: SaveSignalInput; result: SaveSignalResult }; "save_wholesale_product": { input: SaveWholesaleProductInput; result: SaveWholesaleProductResult }; "save_work_item": { input: SaveWorkItemInput; result: SaveWorkItemResult }; "search": { input: SearchInput; result: SearchResult }; "test_creative_macros": { input: TestCreativeMacrosInput; result: TestCreativeMacrosResult }; "upload_creative_asset": { input: UploadCreativeAssetInput; result: UploadCreativeAssetResult } }
export class Apostra extends Transport {
  /**
   * Issue the hosted card-capture link for a token from request_payment_authority. Give the link to the cardholder; cards stay off MCP.
   *
   * @example
   * await client.confirmPaymentAuthority(input, { idempotencyKey: 'stable-key' })
   */
  confirmPaymentAuthority(input: ConfirmPaymentAuthorityInput, options: WriteRequestOptions): Promise<ConfirmPaymentAuthorityResult> { return this.request("confirm_payment_authority", input, options) }

  /** Issue the hosted card-capture link for a token from request_payment_authority. Give the link to the cardholder; cards stay off MCP. Returns the data together with response headers and request ID. */
  confirmPaymentAuthorityWithResponse(input: ConfirmPaymentAuthorityInput, options: WriteRequestOptions): Promise<ResponseDetails<ConfirmPaymentAuthorityResult>> { return this.requestDetailed("confirm_payment_authority", input, options) }
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
   * Generate variants from a saved brief; use Creative Sessions for voice/audio, radio spots, and voiceovers. Send kind, scope, and variantAction; reuse actionKey only on retries.
   *
   * @example
   * await client.generateVariants(input, { idempotencyKey: 'stable-key' })
   */
  generateVariants(input: GenerateVariantsInput, options: WriteRequestOptions): Promise<GenerateVariantsResult> { return this.request("generate_variants", input, options) }

  /** Generate variants from a saved brief; use Creative Sessions for voice/audio, radio spots, and voiceovers. Send kind, scope, and variantAction; reuse actionKey only on retries. Returns the data together with response headers and request ID. */
  generateVariantsWithResponse(input: GenerateVariantsInput, options: WriteRequestOptions): Promise<ResponseDetails<GenerateVariantsResult>> { return this.requestDetailed("generate_variants", input, options) }
  /**
   * Read one object by kind and id, or an account singleton without id. Never guess ids. Campaign reads return targetingOverlay to verify before proposals. include adds detail only for kinds that serve it.
   *
   * @example
   * await client.get(input)
   */
  get(input: GetInput, options?: RequestOptions): Promise<GetResult> { return this.request("get", input, options) }

  /** Read one object by kind and id, or an account singleton without id. Never guess ids. Campaign reads return targetingOverlay to verify before proposals. include adds detail only for kinds that serve it. Returns the data together with response headers and request ID. */
  getWithResponse(input: GetInput, options?: RequestOptions): Promise<ResponseDetails<GetResult>> { return this.requestDetailed("get", input, options) }
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
   * Read the state of a V3 HTTP write receipt
   *
   * @example
   * await client.getV3PublicMutationReceipt(input)
   */
  getV3PublicMutationReceipt(input: GetV3PublicMutationReceiptInput, options?: RequestOptions): Promise<GetV3PublicMutationReceiptResult> { return this.request("getV3PublicMutationReceipt", input, options) }

  /** Read the state of a V3 HTTP write receipt Returns the data together with response headers and request ID. */
  getV3PublicMutationReceiptWithResponse(input: GetV3PublicMutationReceiptInput, options?: RequestOptions): Promise<ResponseDetails<GetV3PublicMutationReceiptResult>> { return this.requestDetailed("getV3PublicMutationReceipt", input, options) }
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
   * Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns.
   *
   * @example
   * await client.getRfpPerformance(input)
   */
  getRfpPerformance(input: GetRfpPerformanceInput, options?: RequestOptions): Promise<GetRfpPerformanceResult> { return this.request("get_rfp_performance", input, options) }

  /** Query grouped Seller RFP quality, efficiency, and commercial metrics with metric-specific availability and immutable pages. Defaults to live terminal turns; synthetic purposes are opt-in and excluded from commercial metrics. Use get for individual RFPs or turns. Returns the data together with response headers and request ID. */
  getRfpPerformanceWithResponse(input: GetRfpPerformanceInput, options?: RequestOptions): Promise<ResponseDetails<GetRfpPerformanceResult>> { return this.requestDetailed("get_rfp_performance", input, options) }
  /**
   * Show a seller what reporting we received for one buyer media buy, whether each receipt was accepted, and the current computed daily totals. Opens the Media Buy Timeline Glance.
   *
   * @example
   * await client.getSellerReportingReceipts(input)
   */
  getSellerReportingReceipts(input: GetSellerReportingReceiptsInput, options?: RequestOptions): Promise<GetSellerReportingReceiptsResult> { return this.request("get_seller_reporting_receipts", input, options) }

  /** Show a seller what reporting we received for one buyer media buy, whether each receipt was accepted, and the current computed daily totals. Opens the Media Buy Timeline Glance. Returns the data together with response headers and request ID. */
  getSellerReportingReceiptsWithResponse(input: GetSellerReportingReceiptsInput, options?: RequestOptions): Promise<ResponseDetails<GetSellerReportingReceiptsResult>> { return this.requestDetailed("get_seller_reporting_receipts", input, options) }
  /**
   * Current account, state, blockers, exact fixes, accounts to pick from. For seller demand, tells if readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand. A Developer account adds each agent's stage, blocker, next call.
   *
   * @example
   * await client.getStatus(input)
   */
  getStatus(input: GetStatusInput = {}, options?: RequestOptions): Promise<GetStatusResult> { return this.request("get_status", input, options) }

  /** Current account, state, blockers, exact fixes, accounts to pick from. For seller demand, tells if readiness stops requests before source calls; read before diagnosing source health, empty responses, or demand. A Developer account adds each agent's stage, blocker, next call. Returns the data together with response headers and request ID. */
  getStatusWithResponse(input: GetStatusInput = {}, options?: RequestOptions): Promise<ResponseDetails<GetStatusResult>> { return this.requestDetailed("get_status", input, options) }
  /**
   * Send up to 10,000 AdCP conversion events (log_event) to an event source the advertiser registered with save_event_source. Events must also pass the v2 rules: no raw email or phone in user_match, each event_type + event_id once per call. One invalid event refuses the whole call.
   *
   * @example
   * await client.logEvent(input, { idempotencyKey: 'stable-key' })
   */
  logEvent(input: LogEventInput, options: WriteRequestOptions): Promise<LogEventResult> { return this.request("log_event", input, options) }

  /** Send up to 10,000 AdCP conversion events (log_event) to an event source the advertiser registered with save_event_source. Events must also pass the v2 rules: no raw email or phone in user_match, each event_type + event_id once per call. One invalid event refuses the whole call. Returns the data together with response headers and request ID. */
  logEventWithResponse(input: LogEventInput, options: WriteRequestOptions): Promise<ResponseDetails<LogEventResult>> { return this.requestDetailed("log_event", input, options) }
  /**
   * Open the Advertisers Page: every advertiser with its campaign and draft counts and one next action each. Use it for "show my advertisers" or "where do I start"; the Page self-fetches. To add or set up an advertiser, pass intent: "add". For a text answer use search(kind: "advertiser").
   *
   * @example
   * await client.openAdvertisersPage(input)
   */
  openAdvertisersPage(input: OpenAdvertisersPageInput, options?: RequestOptions): Promise<OpenAdvertisersPageResult> { return this.request("open_advertisers_page", input, options) }

  /** Open the Advertisers Page: every advertiser with its campaign and draft counts and one next action each. Use it for "show my advertisers" or "where do I start"; the Page self-fetches. To add or set up an advertiser, pass intent: "add". For a text answer use search(kind: "advertiser"). Returns the data together with response headers and request ID. */
  openAdvertisersPageWithResponse(input: OpenAdvertisersPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenAdvertisersPageResult>> { return this.requestDetailed("open_advertisers_page", input, options) }
  /**
   * Open one agent’s Test & certify Page: live certification per use case, recent test runs, AdCP 4.0 readiness and capability declarations. Read-only.
   *
   * @example
   * await client.openAgentCertificationPage(input)
   */
  openAgentCertificationPage(input: OpenAgentCertificationPageInput, options?: RequestOptions): Promise<OpenAgentCertificationPageResult> { return this.request("open_agent_certification_page", input, options) }

  /** Open one agent’s Test & certify Page: live certification per use case, recent test runs, AdCP 4.0 readiness and capability declarations. Read-only. Returns the data together with response headers and request ID. */
  openAgentCertificationPageWithResponse(input: OpenAgentCertificationPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenAgentCertificationPageResult>> { return this.requestDetailed("open_agent_certification_page", input, options) }
  /**
   * Open one agent owned by this Developer account.
   *
   * @example
   * await client.openAgentPage(input)
   */
  openAgentPage(input: OpenAgentPageInput, options?: RequestOptions): Promise<OpenAgentPageResult> { return this.request("open_agent_page", input, options) }

  /** Open one agent owned by this Developer account. Returns the data together with response headers and request ID. */
  openAgentPageWithResponse(input: OpenAgentPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenAgentPageResult>> { return this.requestDetailed("open_agent_page", input, options) }
  /**
   * Open one agent’s Inventory sources Page: the inventory sources it powers and the health of each. Read-only.
   *
   * @example
   * await client.openAgentSourcesPage(input)
   */
  openAgentSourcesPage(input: OpenAgentSourcesPageInput, options?: RequestOptions): Promise<OpenAgentSourcesPageResult> { return this.request("open_agent_sources_page", input, options) }

  /** Open one agent’s Inventory sources Page: the inventory sources it powers and the health of each. Read-only. Returns the data together with response headers and request ID. */
  openAgentSourcesPageWithResponse(input: OpenAgentSourcesPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenAgentSourcesPageResult>> { return this.requestDetailed("open_agent_sources_page", input, options) }
  /**
   * Open one agent’s Webhooks Page: its recent inbound webhook outcomes, each refusal with its reason. Read-only.
   *
   * @example
   * await client.openAgentWebhooksPage(input)
   */
  openAgentWebhooksPage(input: OpenAgentWebhooksPageInput, options?: RequestOptions): Promise<OpenAgentWebhooksPageResult> { return this.request("open_agent_webhooks_page", input, options) }

  /** Open one agent’s Webhooks Page: its recent inbound webhook outcomes, each refusal with its reason. Read-only. Returns the data together with response headers and request ID. */
  openAgentWebhooksPageWithResponse(input: OpenAgentWebhooksPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenAgentWebhooksPageResult>> { return this.requestDetailed("open_agent_webhooks_page", input, options) }
  /**
   * Open Build an agent for this Developer account.
   *
   * @example
   * await client.openAgentsPage(input)
   */
  openAgentsPage(input: OpenAgentsPageInput, options?: RequestOptions): Promise<OpenAgentsPageResult> { return this.request("open_agents_page", input, options) }

  /** Open Build an agent for this Developer account. Returns the data together with response headers and request ID. */
  openAgentsPageWithResponse(input: OpenAgentsPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenAgentsPageResult>> { return this.requestDetailed("open_agents_page", input, options) }
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
   * Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign.
   *
   * @example
   * await client.openCampaignReceipt(input)
   */
  openCampaignReceipt(input: OpenCampaignReceiptInput, options?: RequestOptions): Promise<OpenCampaignReceiptResult> { return this.request("open_campaign_receipt", input, options) }

  /** Open Review & go live for one draft campaign: budget, flight, staged media buys and their budget split, why each buy is not live yet, and the readiness blockers. Use when a buyer asks if a draft is ready to launch. Refuses non-draft campaigns; launching stays a separate confirmed save_campaign. Returns the data together with response headers and request ID. */
  openCampaignReceiptWithResponse(input: OpenCampaignReceiptInput, options?: RequestOptions): Promise<ResponseDetails<OpenCampaignReceiptResult>> { return this.requestDetailed("open_campaign_receipt", input, options) }
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
   * Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction "connect" opens that media partner at connection setup without mutating until the user confirms. Replaced by open_media_partners_page, which opens the same Page.
   *
   * @example
   * await client.openConnectionsPage(input)
   */
  openConnectionsPage(input: OpenConnectionsPageInput, options?: RequestOptions): Promise<OpenConnectionsPageResult> { return this.request("open_connections_page", input, options) }

  /** Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction "connect" opens that media partner at connection setup without mutating until the user confirms. Replaced by open_media_partners_page, which opens the same Page. Returns the data together with response headers and request ID. */
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
   * Open Creative Library. Use search for a plain object answer. The composer can start from an advertiser or a campaign and does not need a Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format.
   *
   * @example
   * await client.openCreativeLibrary(input, { idempotencyKey: 'stable-key' })
   */
  openCreativeLibrary(input: OpenCreativeLibraryInput, options: WriteRequestOptions): Promise<OpenCreativeLibraryResult> { return this.request("open_creative_library", input, options) }

  /** Open Creative Library. Use search for a plain object answer. The composer can start from an advertiser or a campaign and does not need a Creative Engine. To save a draft, use exactly one format: a canonical format such as image, hosted video, or hosted audio, or a seller format. Returns the data together with response headers and request ID. */
  openCreativeLibraryWithResponse(input: OpenCreativeLibraryInput, options: WriteRequestOptions): Promise<ResponseDetails<OpenCreativeLibraryResult>> { return this.requestDetailed("open_creative_library", input, options) }
  /**
   * Open the Developer home for this Developer account: its agents, their stages and what to do next.
   *
   * @example
   * await client.openDeveloperHome(input)
   */
  openDeveloperHome(input: OpenDeveloperHomeInput, options?: RequestOptions): Promise<OpenDeveloperHomeResult> { return this.request("open_developer_home", input, options) }

  /** Open the Developer home for this Developer account: its agents, their stages and what to do next. Returns the data together with response headers and request ID. */
  openDeveloperHomeWithResponse(input: OpenDeveloperHomeInput, options?: RequestOptions): Promise<ResponseDetails<OpenDeveloperHomeResult>> { return this.requestDetailed("open_developer_home", input, options) }
  /**
   * Open the Seller Media Buys Page. Optionally focus one account relationship or seller account mapping (not both) and its buys or creatives; the Page self-fetches.
   *
   * @example
   * await client.openMediaBuysPage(input)
   */
  openMediaBuysPage(input: OpenMediaBuysPageInput, options?: RequestOptions): Promise<OpenMediaBuysPageResult> { return this.request("open_media_buys_page", input, options) }

  /** Open the Seller Media Buys Page. Optionally focus one account relationship or seller account mapping (not both) and its buys or creatives; the Page self-fetches. Returns the data together with response headers and request ID. */
  openMediaBuysPageWithResponse(input: OpenMediaBuysPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenMediaBuysPageResult>> { return this.requestDetailed("open_media_buys_page", input, options) }
  /**
   * Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction "connect" opens that media partner at connection setup without mutating until the user confirms.
   *
   * @example
   * await client.openMediaPartnersPage(input)
   */
  openMediaPartnersPage(input: OpenMediaPartnersPageInput, options?: RequestOptions): Promise<OpenMediaPartnersPageResult> { return this.request("open_media_partners_page", input, options) }

  /** Open the buyer Media Partners Page. Optionally scope to an advertiser or seller; connectionAction "connect" opens that media partner at connection setup without mutating until the user confirms. Returns the data together with response headers and request ID. */
  openMediaPartnersPageWithResponse(input: OpenMediaPartnersPageInput, options?: RequestOptions): Promise<ResponseDetails<OpenMediaPartnersPageResult>> { return this.requestDetailed("open_media_partners_page", input, options) }
  /**
   * Open a compatibility Page. Owners create or attach the Agent in source_diagnostics. External hosts may return text. Credentials and authority changes remain human ceremonies.
   *
   * @example
   * await client.openPage(input)
   */
  openPage(input: OpenPageInput, options?: RequestOptions): Promise<OpenPageResult> { return this.request("open_page", input, options) }

  /** Open a compatibility Page. Owners create or attach the Agent in source_diagnostics. External hosts may return text. Credentials and authority changes remain human ceremonies. Returns the data together with response headers and request ID. */
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
   * Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches.
   *
   * @example
   * await client.openSellerDashboard(input)
   */
  openSellerDashboard(input: OpenSellerDashboardInput, options?: RequestOptions): Promise<OpenSellerDashboardResult> { return this.request("open_seller_dashboard", input, options) }

  /** Open the Seller Dashboard Page: seller analytics, or the synthetic evaluation view of practice runs while this is an active demo Seller Account. The Page self-fetches. Returns the data together with response headers and request ID. */
  openSellerDashboardWithResponse(input: OpenSellerDashboardInput, options?: RequestOptions): Promise<ResponseDetails<OpenSellerDashboardResult>> { return this.requestDetailed("open_seller_dashboard", input, options) }
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
   * Rechecks one external sales-agent source with no-spend get_products and, if it publishes one, a catalog refresh. Returns each check, findings still open, evidence IDs and readiness; no source configuration or media buy. scope accounts re-lists the source's accounts instead.
   *
   * @example
   * await client.refreshInventorySourceHealth(input, { idempotencyKey: 'stable-key' })
   */
  refreshInventorySourceHealth(input: RefreshInventorySourceHealthInput, options: WriteRequestOptions): Promise<RefreshInventorySourceHealthResult> { return this.request("refresh_inventory_source_health", input, options) }

  /** Rechecks one external sales-agent source with no-spend get_products and, if it publishes one, a catalog refresh. Returns each check, findings still open, evidence IDs and readiness; no source configuration or media buy. scope accounts re-lists the source's accounts instead. Returns the data together with response headers and request ID. */
  refreshInventorySourceHealthWithResponse(input: RefreshInventorySourceHealthInput, options: WriteRequestOptions): Promise<ResponseDetails<RefreshInventorySourceHealthResult>> { return this.requestDetailed("refresh_inventory_source_health", input, options) }
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
   * Stage a card handoff for the organization and return a confirmation token. No link is issued until confirm_payment_authority.
   *
   * @example
   * await client.requestPaymentAuthority(input, { idempotencyKey: 'stable-key' })
   */
  requestPaymentAuthority(input: RequestPaymentAuthorityInput, options: WriteRequestOptions): Promise<RequestPaymentAuthorityResult> { return this.request("request_payment_authority", input, options) }

  /** Stage a card handoff for the organization and return a confirmation token. No link is issued until confirm_payment_authority. Returns the data together with response headers and request ID. */
  requestPaymentAuthorityWithResponse(input: RequestPaymentAuthorityInput, options: WriteRequestOptions): Promise<ResponseDetails<RequestPaymentAuthorityResult>> { return this.requestDetailed("request_payment_authority", input, options) }
  /**
   * Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds and sellerAccountIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true.
   *
   * @example
   * await client.requestProposals(input, { idempotencyKey: 'stable-key' })
   */
  requestProposals(input: RequestProposalsInput, options: WriteRequestOptions): Promise<RequestProposalsResult> { return this.request("request_proposals", input, options) }

  /** Request quotes/products. With a MediaBuy cap, only quotes confirming the exact cap are usable. sellerIds and sellerAccountIds fail closed; campaign-only lists use eligible subset. Broadcast needs confirmBroadcast:true. Returns the data together with response headers and request ID. */
  requestProposalsWithResponse(input: RequestProposalsInput, options: WriteRequestOptions): Promise<ResponseDetails<RequestProposalsResult>> { return this.requestDetailed("request_proposals", input, options) }
  /**
   * Requests a scheduler-run reporting refresh or a bounded replay for one seller media buy. It never polls a provider directly.
   *
   * @example
   * await client.requestSellerReportingUpdate(input, { idempotencyKey: 'stable-key' })
   */
  requestSellerReportingUpdate(input: RequestSellerReportingUpdateInput, options: WriteRequestOptions): Promise<RequestSellerReportingUpdateResult> { return this.request("request_seller_reporting_update", input, options) }

  /** Requests a scheduler-run reporting refresh or a bounded replay for one seller media buy. It never polls a provider directly. Returns the data together with response headers and request ID. */
  requestSellerReportingUpdateWithResponse(input: RequestSellerReportingUpdateInput, options: WriteRequestOptions): Promise<ResponseDetails<RequestSellerReportingUpdateResult>> { return this.requestDetailed("request_seller_reporting_update", input, options) }
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
   * Create a child Account (omit id), rename one, or archive or restore it (isArchived). Each is recorded for website approval by an Organization administrator; repeat with the same idempotencyKey for the outcome. dryRun previews. settings.company saves at once. Never changes owners or members.
   *
   * @example
   * await client.saveAccount(input, { idempotencyKey: 'stable-key' })
   */
  saveAccount(input: SaveAccountInput, options: WriteRequestOptions): Promise<SaveAccountResult> { return this.request("save_account", input, options) }

  /** Create a child Account (omit id), rename one, or archive or restore it (isArchived). Each is recorded for website approval by an Organization administrator; repeat with the same idempotencyKey for the outcome. dryRun previews. settings.company saves at once. Never changes owners or members. Returns the data together with response headers and request ID. */
  saveAccountWithResponse(input: SaveAccountInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAccountResult>> { return this.requestDetailed("save_account", input, options) }
  /**
   * Save an advertiser or mappings. Buyer privateNotes: owning Buyer Account only; /v3/manage-ads#private-advertiser-notes. Confirm markets/channels (footprintProposal); needs_input=ask; never recreate for currency. Brand: identityContract:confirmed-v1; preview: resolveBrand; read advertiser.brandRef.
   *
   * @example
   * await client.saveAdvertiser(input, { idempotencyKey: 'stable-key' })
   */
  saveAdvertiser(input: SaveAdvertiserInput, options: WriteRequestOptions): Promise<SaveAdvertiserResult> { return this.request("save_advertiser", input, options) }

  /** Save an advertiser or mappings. Buyer privateNotes: owning Buyer Account only; /v3/manage-ads#private-advertiser-notes. Confirm markets/channels (footprintProposal); needs_input=ask; never recreate for currency. Brand: identityContract:confirmed-v1; preview: resolveBrand; read advertiser.brandRef. Returns the data together with response headers and request ID. */
  saveAdvertiserWithResponse(input: SaveAdvertiserInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAdvertiserResult>> { return this.requestDetailed("save_advertiser", input, options) }
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
   * Seller-only CRM notes for an exact brand × operator pair. Buyers use save_advertiser.privateNotes; see /v3/manage-ads#private-advertiser-notes. Effective discounts, routing, access and trust are read-only.
   *
   * @example
   * await client.saveAdvertiserInstructions(input, { idempotencyKey: 'stable-key' })
   */
  saveAdvertiserInstructions(input: SaveAdvertiserInstructionsInput, options: WriteRequestOptions): Promise<SaveAdvertiserInstructionsResult> { return this.request("save_advertiser_instructions", input, options) }

  /** Seller-only CRM notes for an exact brand × operator pair. Buyers use save_advertiser.privateNotes; see /v3/manage-ads#private-advertiser-notes. Effective discounts, routing, access and trust are read-only. Returns the data together with response headers and request ID. */
  saveAdvertiserInstructionsWithResponse(input: SaveAdvertiserInstructionsInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAdvertiserInstructionsResult>> { return this.requestDetailed("save_advertiser_instructions", input, options) }
  /**
   * Confirm a Sales Agent product mode, register a Sales or Creative Agent, or update an owned Agent: rename it or allow certification buys. To connect from a URL, send agentUrl with dryRun: true, show what was read, then send it without dryRun. A connected agent is not yet verified as theirs.
   *
   * @example
   * await client.saveAgent(input, { idempotencyKey: 'stable-key' })
   */
  saveAgent(input: SaveAgentInput, options: WriteRequestOptions): Promise<SaveAgentResult> { return this.request("save_agent", input, options) }

  /** Confirm a Sales Agent product mode, register a Sales or Creative Agent, or update an owned Agent: rename it or allow certification buys. To connect from a URL, send agentUrl with dryRun: true, show what was read, then send it without dryRun. A connected agent is not yet verified as theirs. Returns the data together with response headers and request ID. */
  saveAgentWithResponse(input: SaveAgentInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAgentResult>> { return this.requestDetailed("save_agent", input, options) }
  /**
   * File or update a typed ask in the Apostra Support workflow; returns askId. kind create files a new ask; kind update sends only id and requester. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first.
   *
   * @example
   * await client.saveAsk(input, { idempotencyKey: 'stable-key' })
   */
  saveAsk(input: SaveAskInput, options: WriteRequestOptions): Promise<SaveAskResult> { return this.request("save_ask", input, options) }

  /** File or update a typed ask in the Apostra Support workflow; returns askId. kind create files a new ask; kind update sends only id and requester. Supply is buyer inventory. Call immediately with type support when a person explicitly asks for a human; do not diagnose first. Returns the data together with response headers and request ID. */
  saveAskWithResponse(input: SaveAskInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveAskResult>> { return this.requestDetailed("save_ask", input, options) }
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
   * Accept Terms, set the payment terms sellers are asked for, or accept a plan, answer its offer and change its renewal. Accepting a plan needs an administrator to approve it on our site. Cards stay off MCP.
   *
   * @example
   * await client.saveBilling(input, { idempotencyKey: 'stable-key' })
   */
  saveBilling(input: SaveBillingInput, options: WriteRequestOptions): Promise<SaveBillingResult> { return this.request("save_billing", input, options) }

  /** Accept Terms, set the payment terms sellers are asked for, or accept a plan, answer its offer and change its renewal. Accepting a plan needs an administrator to approve it on our site. Cards stay off MCP. Returns the data together with response headers and request ID. */
  saveBillingWithResponse(input: SaveBillingInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveBillingResult>> { return this.requestDetailed("save_billing", input, options) }
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
   * Create a buyer agent, or with id make one change: name, advertiser access, lifecycle state, or credential handoff.
   *
   * @example
   * await client.saveBuyerAgent(input, { idempotencyKey: 'stable-key' })
   */
  saveBuyerAgent(input: SaveBuyerAgentInput, options: WriteRequestOptions): Promise<SaveBuyerAgentResult> { return this.request("save_buyer_agent", input, options) }

  /** Create a buyer agent, or with id make one change: name, advertiser access, lifecycle state, or credential handoff. Returns the data together with response headers and request ID. */
  saveBuyerAgentWithResponse(input: SaveBuyerAgentInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveBuyerAgentResult>> { return this.requestDetailed("save_buyer_agent", input, options) }
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
   * Create: advertiserId/name; flight/budget optional. Receipts and launch previews show local/UTC times in the applicable IANA timezone. desiredPhase: active previews; confirmLaunch: true launches. Cancellation is irreversible: desiredPhase: canceled cancels the campaign and every live media buy.
   *
   * @example
   * await client.saveCampaign(input, { idempotencyKey: 'stable-key' })
   */
  saveCampaign(input: SaveCampaignInput, options: WriteRequestOptions): Promise<SaveCampaignResult> { return this.request("save_campaign", input, options) }

  /** Create: advertiserId/name; flight/budget optional. Receipts and launch previews show local/UTC times in the applicable IANA timezone. desiredPhase: active previews; confirmLaunch: true launches. Cancellation is irreversible: desiredPhase: canceled cancels the campaign and every live media buy. Returns the data together with response headers and request ID. */
  saveCampaignWithResponse(input: SaveCampaignInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCampaignResult>> { return this.requestDetailed("save_campaign", input, options) }
  /**
   * Create or replace a catalog: type and exactly one of url (feed URL) or non-empty items are required. If missing, ask the buyer for the feed URL or items before calling. URL saves refetch the feed. To archive, set isArchived: true with identity only; type, url and items are not needed.
   *
   * @example
   * await client.saveCatalog(input, { idempotencyKey: 'stable-key' })
   */
  saveCatalog(input: SaveCatalogInput, options: WriteRequestOptions): Promise<SaveCatalogResult> { return this.request("save_catalog", input, options) }

  /** Create or replace a catalog: type and exactly one of url (feed URL) or non-empty items are required. If missing, ask the buyer for the feed URL or items before calling. URL saves refetch the feed. To archive, set isArchived: true with identity only; type, url and items are not needed. Returns the data together with response headers and request ID. */
  saveCatalogWithResponse(input: SaveCatalogInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCatalogResult>> { return this.requestDetailed("save_catalog", input, options) }
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
   * Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, `removeProperties`, and `refresh` act on named items only. Read authorization; never assume it.
   *
   * @example
   * await client.saveCoverage(input, { idempotencyKey: 'stable-key' })
   */
  saveCoverage(input: SaveCoverageInput, options: WriteRequestOptions): Promise<SaveCoverageResult> { return this.request("save_coverage", input, options) }

  /** Declare publisher domains this Seller sells and its claimed properties. `domains` replaces the complete set; `add`, `remove`, `declareProperties`, `removeProperties`, and `refresh` act on named items only. Read authorization; never assume it. Returns the data together with response headers and request ID. */
  saveCoverageWithResponse(input: SaveCoverageInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCoverageResult>> { return this.requestDetailed("save_coverage", input, options) }
  /**
   * advertiserId/campaignId:name,message;assets/landing_page_url/social/sourceAssetRef/sourceAssets;Supplied content/assets only;generate new media (radio spots):save_creative_session;exactly one format selector:formatKind/formatParams,creativeFormatId/formatOptionRef;libraryRole:Buyer Account only.
   *
   * @example
   * await client.saveCreative(input, { idempotencyKey: 'stable-key' })
   */
  saveCreative(input: SaveCreativeInput, options: WriteRequestOptions): Promise<SaveCreativeResult> { return this.request("save_creative", input, options) }

  /** advertiserId/campaignId:name,message;assets/landing_page_url/social/sourceAssetRef/sourceAssets;Supplied content/assets only;generate new media (radio spots):save_creative_session;exactly one format selector:formatKind/formatParams,creativeFormatId/formatOptionRef;libraryRole:Buyer Account only. Returns the data together with response headers and request ID. */
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
   * Save a Creative Session for image, video, or voice/audio (including radio spots) from a brief: its draft, selected output, approval, or finalisation. It never generates; generate_variants does. To save an approved output to the Library, use save_creative with fromCreativeSessionOutput.
   *
   * @example
   * await client.saveCreativeSession(input, { idempotencyKey: 'stable-key' })
   */
  saveCreativeSession(input: SaveCreativeSessionInput, options: WriteRequestOptions): Promise<SaveCreativeSessionResult> { return this.request("save_creative_session", input, options) }

  /** Save a Creative Session for image, video, or voice/audio (including radio spots) from a brief: its draft, selected output, approval, or finalisation. It never generates; generate_variants does. To save an approved output to the Library, use save_creative with fromCreativeSessionOutput. Returns the data together with response headers and request ID. */
  saveCreativeSessionWithResponse(input: SaveCreativeSessionInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveCreativeSessionResult>> { return this.requestDetailed("save_creative_session", input, options) }
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
   * Import native campaigns from Spotify Ads Manager or other platforms, including future-start campaigns, as read-only mirrors. Confirm ongoing sync first. No provider changes. /v3/import-existing-campaigns.
   *
   * @example
   * await client.saveDirectedCampaignSubscription(input, { idempotencyKey: 'stable-key' })
   */
  saveDirectedCampaignSubscription(input: SaveDirectedCampaignSubscriptionInput, options: WriteRequestOptions): Promise<SaveDirectedCampaignSubscriptionResult> { return this.request("save_directed_campaign_subscription", input, options) }

  /** Import native campaigns from Spotify Ads Manager or other platforms, including future-start campaigns, as read-only mirrors. Confirm ongoing sync first. No provider changes. /v3/import-existing-campaigns. Returns the data together with response headers and request ID. */
  saveDirectedCampaignSubscriptionWithResponse(input: SaveDirectedCampaignSubscriptionInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveDirectedCampaignSubscriptionResult>> { return this.requestDetailed("save_directed_campaign_subscription", input, options) }
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
   * Create or update where a seller's inventory comes from. Pass `id` to change a source or omit it to add one. Pass only `agentId` or `adServer` to open the form that connects an agent or an ad server. Credentials are never passed here; a source that needs one returns the page that collects it.
   *
   * @example
   * await client.saveInventorySource(input, { idempotencyKey: 'stable-key' })
   */
  saveInventorySource(input: SaveInventorySourceInput, options: WriteRequestOptions): Promise<SaveInventorySourceResult> { return this.request("save_inventory_source", input, options) }

  /** Create or update where a seller's inventory comes from. Pass `id` to change a source or omit it to add one. Pass only `agentId` or `adServer` to open the form that connects an agent or an ad server. Credentials are never passed here; a source that needs one returns the page that collects it. Returns the data together with response headers and request ID. */
  saveInventorySourceWithResponse(input: SaveInventorySourceInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveInventorySourceResult>> { return this.requestDetailed("save_inventory_source", input, options) }
  /**
   * Manage seller lessons in a seller account; send the accountId of that account. propose requires lesson; approve and retire require lessonId; preview requires lessonId and brief. Preserve seller words from a private Session note and ask if kind or scope is unclear.
   *
   * @example
   * await client.saveLesson(input, { idempotencyKey: 'stable-key' })
   */
  saveLesson(input: SaveLessonInput, options: WriteRequestOptions): Promise<SaveLessonResult> { return this.request("save_lesson", input, options) }

  /** Manage seller lessons in a seller account; send the accountId of that account. propose requires lesson; approve and retire require lessonId; preview requires lessonId and brief. Preserve seller words from a private Session note and ask if kind or scope is unclear. Returns the data together with response headers and request ID. */
  saveLessonWithResponse(input: SaveLessonInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveLessonResult>> { return this.requestDetailed("save_lesson", input, options) }
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
   * Create or update seller Materials. Seller beta: preview, delete, Undo deletion, or Include again for one imported Library document. Delete archives it, excludes its source until Include again, and purges it after 30 days. https://docs.apostra.com/v3/delete-from-apostra
   *
   * @example
   * await client.saveMaterial(input, { idempotencyKey: 'stable-key' })
   */
  saveMaterial(input: SaveMaterialInput, options: WriteRequestOptions): Promise<SaveMaterialResult> { return this.request("save_material", input, options) }

  /** Create or update seller Materials. Seller beta: preview, delete, Undo deletion, or Include again for one imported Library document. Delete archives it, excludes its source until Include again, and purges it after 30 days. https://docs.apostra.com/v3/delete-from-apostra Returns the data together with response headers and request ID. */
  saveMaterialWithResponse(input: SaveMaterialInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveMaterialResult>> { return this.requestDetailed("save_material", input, options) }
  /**
   * Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates.
   *
   * @example
   * await client.saveMediaBuy(input, { idempotencyKey: 'stable-key' })
   */
  saveMediaBuy(input: SaveMediaBuyInput, options: WriteRequestOptions): Promise<SaveMediaBuyResult> { return this.request("save_media_buy", input, options) }

  /** Create DRAFT buy; no spend until confirmed. Meta: shared campaign=seller_optimized; ad sets=fixed; ask if unclear. Shared: omit product budgets. Pause/resume: mediaBuyId + isPaused. Proposal: flight + total budget; omit products. channelGroupId: required if grouped; invalid ungrouped/updates. Returns the data together with response headers and request ID. */
  saveMediaBuyWithResponse(input: SaveMediaBuyInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveMediaBuyResult>> { return this.requestDetailed("save_media_buy", input, options) }
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
   * Create or update a notification subscription. Omit subscriptionId to create; managed subscriptions permit only mutable fields. Use save_integration for credentials when needed.
   *
   * @example
   * await client.saveNotificationConfig(input, { idempotencyKey: 'stable-key' })
   */
  saveNotificationConfig(input: SaveNotificationConfigInput, options: WriteRequestOptions): Promise<SaveNotificationConfigResult> { return this.request("save_notification_config", input, options) }

  /** Create or update a notification subscription. Omit subscriptionId to create; managed subscriptions permit only mutable fields. Use save_integration for credentials when needed. Returns the data together with response headers and request ID. */
  saveNotificationConfigWithResponse(input: SaveNotificationConfigInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveNotificationConfigResult>> { return this.requestDetailed("save_notification_config", input, options) }
  /**
   * Write selling guidance. `active` turns Playbook prose and its optional seller note into proposed Lessons; the active Playbook is unchanged. `pricing` replaces facts. `discounts` sets or removes brand/operator rules. Halves never roll back each other.
   *
   * @example
   * await client.savePlaybook(input, { idempotencyKey: 'stable-key' })
   */
  savePlaybook(input: SavePlaybookInput, options: WriteRequestOptions): Promise<SavePlaybookResult> { return this.request("save_playbook", input, options) }

  /** Write selling guidance. `active` turns Playbook prose and its optional seller note into proposed Lessons; the active Playbook is unchanged. `pricing` replaces facts. `discounts` sets or removes brand/operator rules. Halves never roll back each other. Returns the data together with response headers and request ID. */
  savePlaybookWithResponse(input: SavePlaybookInput, options: WriteRequestOptions): Promise<ResponseDetails<SavePlaybookResult>> { return this.requestDetailed("save_playbook", input, options) }
  /**
   * Create, update, archive, restore, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists.
   *
   * @example
   * await client.savePropertyList(input, { idempotencyKey: 'stable-key' })
   */
  savePropertyList(input: SavePropertyListInput, options: WriteRequestOptions): Promise<SavePropertyListResult> { return this.request("save_property_list", input, options) }

  /** Create, update, archive, restore, or AAO-check an advertiser property list. Check uses identifiers without saving. Search/get read saved lists. Returns the data together with response headers and request ID. */
  savePropertyListWithResponse(input: SavePropertyListInput, options: WriteRequestOptions): Promise<ResponseDetails<SavePropertyListResult>> { return this.requestDetailed("save_property_list", input, options) }
  /**
   * Save an RFP: create it from an origin, revise it with a new request, endorse or unendorse its response, or attach an imported response. A turn’s feedback, release, proposal files and outcome use save_rfp_turn.
   *
   * @example
   * await client.saveRfp(input, { idempotencyKey: 'stable-key' })
   */
  saveRfp(input: SaveRfpInput, options: WriteRequestOptions): Promise<SaveRfpResult> { return this.request("save_rfp", input, options) }

  /** Save an RFP: create it from an origin, revise it with a new request, endorse or unendorse its response, or attach an imported response. A turn’s feedback, release, proposal files and outcome use save_rfp_turn. Returns the data together with response headers and request ID. */
  saveRfpWithResponse(input: SaveRfpInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveRfpResult>> { return this.requestDetailed("save_rfp", input, options) }
  /**
   * Change one RFP turn: release it, request or cancel a proposal file, append feedback, or record its outcome. One of these per call; revise, endorse and attach a response with save_rfp.
   *
   * @example
   * await client.saveRfpTurn(input, { idempotencyKey: 'stable-key' })
   */
  saveRfpTurn(input: SaveRfpTurnInput, options: WriteRequestOptions): Promise<SaveRfpTurnResult> { return this.request("save_rfp_turn", input, options) }

  /** Change one RFP turn: release it, request or cancel a proposal file, append feedback, or record its outcome. One of these per call; revise, endorse and attach a response with save_rfp. Returns the data together with response headers and request ID. */
  saveRfpTurnWithResponse(input: SaveRfpTurnInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveRfpTurnResult>> { return this.requestDetailed("save_rfp_turn", input, options) }
  /**
   * Save Seller identity, capabilities, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, an admission, the intake hold, or the demo's expiry and sample sources. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get.
   *
   * @example
   * await client.saveSeller(input, { idempotencyKey: 'stable-key' })
   */
  saveSeller(input: SaveSellerInput, options: WriteRequestOptions): Promise<SaveSellerResult> { return this.request("save_seller", input, options) }

  /** Save Seller identity, capabilities, buyer-visible listing (mediaKit is a deprecated alias), Distribution's OpenAI challenge token, an admission, the intake hold, or the demo's expiry and sample sources. Scope3 eligibility and Market Maker entitlements are read-only here. Read Distribution with get. Returns the data together with response headers and request ID. */
  saveSellerWithResponse(input: SaveSellerInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveSellerResult>> { return this.requestDetailed("save_seller", input, options) }
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
   * Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not.
   *
   * @example
   * await client.saveWholesaleProduct(input, { idempotencyKey: 'stable-key' })
   */
  saveWholesaleProduct(input: SaveWholesaleProductInput, options: WriteRequestOptions): Promise<SaveWholesaleProductResult> { return this.request("save_wholesale_product", input, options) }

  /** Create, change, or delete one wholesale product on an ad-server source — what buyers discover and buy. Omit `id` to create: needs `name` and `inventory`, validated first. Pass `id` to change only the fields you name. `active` = buyable, `archived` = off the market and reversible, `delete` is not. Returns the data together with response headers and request ID. */
  saveWholesaleProductWithResponse(input: SaveWholesaleProductInput, options: WriteRequestOptions): Promise<ResponseDetails<SaveWholesaleProductResult>> { return this.requestDetailed("save_wholesale_product", input, options) }
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
   * Find objects in this account, or answer questions from the docs. Pass kind to list one object type, query to match text, or both. Before a multi-step task, search kind skill for a workflow. Reread a docs hit with its document (and revision, for agreements) before you cite it.
   *
   * @example
   * await client.search(input)
   */
  search(input: SearchInput, options?: RequestOptions): Promise<SearchResult> { return this.request("search", input, options) }

  /** Find objects in this account, or answer questions from the docs. Pass kind to list one object type, query to match text, or both. Before a multi-step task, search kind skill for a workflow. Reread a docs hit with its document (and revision, for agreements) before you cite it. Returns the data together with response headers and request ID. */
  searchWithResponse(input: SearchInput, options?: RequestOptions): Promise<ResponseDetails<SearchResult>> { return this.requestDetailed("search", input, options) }
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
   * Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative.
   *
   * @example
   * await client.uploadCreativeAsset(input, { idempotencyKey: 'stable-key' })
   */
  uploadCreativeAsset(input: UploadCreativeAssetInput, options: WriteRequestOptions): Promise<UploadCreativeAssetResult> { return this.request("upload_creative_asset", input, options) }

  /** Open the embedded Task for an advertiser. Returns accepted MIME types and exact byte limits by type. max_size_bytes is only the largest. Use fallback_url if the Task does not render. Uploading never creates or delivers a Creative. Returns the data together with response headers and request ID. */
  uploadCreativeAssetWithResponse(input: UploadCreativeAssetInput, options: WriteRequestOptions): Promise<ResponseDetails<UploadCreativeAssetResult>> { return this.requestDetailed("upload_creative_asset", input, options) }
}
