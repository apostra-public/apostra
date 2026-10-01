# Generated from checked-in OpenAPI. Do not edit.
from __future__ import annotations
from typing import Literal, NotRequired, TypeAlias, TypedDict, Union
from .json_value import JsonValue

class AdcpError(TypedDict):
    code: str
    message: str
    field: NotRequired[str]
    suggestion: NotRequired[str]
    retry_after: NotRequired[float]
    details: NotRequired[dict[str, JsonValue]]
    recovery: NotRequired[Literal['transient', 'correctable', 'terminal']]

class V3ToolErrorResponse(TypedDict):
    data: None
    error: AdcpError
ReviewBuyerChildAccountSuccessParentId: TypeAlias = int
ReviewBuyerChildAccountSuccessProposedAccountParentId: TypeAlias = int
ReviewBuyerChildAccountSuccessOperatorUserId: TypeAlias = int

class RequestBuyerChildAccountSuccessAgentApproval(TypedDict):
    id: str
    '\n    Approval id.\n    '
    kind: str
    '\n    Kind of sensitive action, for example `buyer_child_account.create`.\n    '
    state: Literal['pending', 'executing', 'succeeded', 'failed', 'rejected', 'expired']
    '\n    `pending` waits for a person; `executing` was approved and is running; `succeeded`, `failed`, `rejected` and `expired` are final.\n    '
    targetCustomerId: str
    '\n    Account the action applies to.\n    '
    requiredRole: Literal['ADMIN', 'SUPER_ADMIN']
    '\n    Role the approver must hold on the account.\n    '
    summary: str | None
    '\n    What will happen, in one line. Null once the approval is final.\n    '
    url: str
    '\n    Page on our site where a signed-in person approves or rejects the request.\n    '
    createdAt: str
    expiresAt: str
    decidedAt: str | None
    completedAt: str | None
    resultReference: dict[str, str | float | bool] | None
    '\n    Reference to the result once succeeded.\n    '
    failureCode: str | None
    '\n    Reason code when the action failed.\n    '
SaveAskSuccessAskId: TypeAlias = str | None
SaveBillingRequestPaymentAuthorityMethod: TypeAlias = Literal['capture_link']

class SaveBillingSuccessPendingConfirmationResult(TypedDict):
    status: Literal['pending_confirmation']
    confirmationToken: str
    '\n    Single-use, short-lived token. Call `add_payment_authority` again with `action: "confirm"` and this token to issue the capture link.\n    '
    summary: str
    expiresAt: str
    '\n    When the confirmation token expires. Request again after this if it lapses.\n    '

class SaveBillingSuccessCaptureLinkIssuedResult(TypedDict):
    method: Literal['capture_link']
    "\n    How the payment authority is captured. `capture_link` (the only value today): a hosted link for the org's human cardholder to open. Future methods (e.g. an agent-held payment token) will be additive values — switch on this field rather than assuming it.\n    "
    url: NotRequired[str]
    "\n    The capture link. Hand this to your organization's cardholder — opening it does not require an Apostra session; the link itself is the authorization. Only present when the link is freshly issued, not on status polls.\n    "
    status: Literal['pending', 'opened', 'verified', 'expired']
    '\n    `pending`: issued, not yet opened. `opened`: the hosted page exchanged the token at least once. `verified`: the card-rail webhook confirmed a payment method for this link. `expired`: the TTL elapsed before verification — terminal, never re-armed.\n    '
    expiresAt: str

class SaveAdvertiserGrantSuccessGrantGrantor(TypedDict):
    organizationRef: str
    displayName: str

class SaveAdvertiserGrantSuccessGrantGrantee(TypedDict):
    organizationRef: str
    displayName: str
SearchRequestCreativeRole: TypeAlias = Literal['evergreen', 'reference']
'\nAdvertiser creative-library role: evergreen (serve-ready, reusable across campaigns) or reference (a generation input, not served). Absent for flight-specific creatives. Never seller Library.\n'
SearchRequestCreativeSource: TypeAlias = Literal['uploaded', 'generated', 'connected']
'\nOrigin of the creative: uploaded (bring-your-own), generated (by a creative agent), or connected (from a 3p platform).\n'

class GetRequestOptionsPagesCandidates(TypedDict):
    cursor: NotRequired[str | None]
    '\n    Cursor.\n    '
    limit: NotRequired[int]
    '\n    Max rows.\n    '

class GetRequestOptionsPagesRenditionBlocks(TypedDict):
    cursor: NotRequired[str | None]
    '\n    Cursor.\n    '
    limit: NotRequired[int]
    '\n    Max rows.\n    '

class GetRequestOptionsPagesVisualAssets(TypedDict):
    cursor: NotRequired[str | None]
    '\n    Cursor.\n    '
    limit: NotRequired[int]
    '\n    Max rows.\n    '

class GetRequestOptionsPagesExtractionDiagnostics(TypedDict):
    cursor: NotRequired[str | None]
    '\n    Cursor.\n    '
    limit: NotRequired[int]
    '\n    Max rows.\n    '

class GetRequestOptionsPagesCompositionReceipts(TypedDict):
    cursor: NotRequired[str | None]
    '\n    Cursor.\n    '
    limit: NotRequired[int]
    '\n    Max rows.\n    '

class GetRequestOptionsPagesUsage(TypedDict):
    cursor: NotRequired[str | None]
    '\n    Cursor.\n    '
    limit: NotRequired[int]
    '\n    Max rows.\n    '
SaveConnectionRequestBuyerStorefrontSelectionDecision: TypeAlias = Literal['DEFAULT', 'ALWAYS_INCLUDE', 'ALWAYS_EXCLUDE']
'\nBuyer-account override for one exact Storefront. DEFAULT removes the override.\n'
SaveConnectionRequestBuyerAdvertiserStorefrontActivationPreferenceDecision: TypeAlias = Literal['DEFAULT', 'ENABLED', 'DISABLED']
'\nAdvertiser-specific seller activation preference. DEFAULT removes the preference and inherits account selection.\n'
SaveConnectionRequestSellerId: TypeAlias = str
SaveConnectionRequestConnectionId: TypeAlias = str
SaveConnectionRequestAdvertiserActivationAdvertiserId: TypeAlias = str
SaveConnectionRequestEnhancedReportingAccountId: TypeAlias = str
SaveConnectionRequestSelectedAccountId: TypeAlias = str
SaveConnectionRequestAdvertiserMappingAccountId: TypeAlias = str
SaveConnectionRequestAdvertiserMappingAdvertiserId: TypeAlias = str
SaveConnectionRequestAdvertiserMappingLinkId: TypeAlias = str
SaveConnectionSuccessObject: TypeAlias = dict[str, JsonValue] | None

class SaveConnectionSuccessMutationReceipt1(TypedDict):
    state: Literal['committed']
    receiptId: str

class SaveConnectionSuccessMutationReceipt2(TypedDict):
    state: Literal['replayed']
    receiptId: str

class SaveConnectionSuccessMutationReceipt3(TypedDict):
    state: Literal['failed']
    receiptId: str

class SaveConnectionSuccessMutationReceipt4(TypedDict):
    state: Literal['missing']

class SaveConnectionSuccessMutationReceipt5(TypedDict):
    state: Literal['in_flight']
    receiptId: str

class SaveConnectionSuccessMutationReceipt6(TypedDict):
    state: Literal['reconcile_required']
    receiptId: str

class SaveConnectionSuccessMutationReceipt7(TypedDict):
    state: Literal['expired']
    receiptId: str

class SaveConnectionSuccessMutationReceipt8(TypedDict):
    state: Literal['conflict']
    receiptId: str
SaveConnectionSuccessMutationReceipt: TypeAlias = SaveConnectionSuccessMutationReceipt1 | SaveConnectionSuccessMutationReceipt2 | SaveConnectionSuccessMutationReceipt3 | SaveConnectionSuccessMutationReceipt4 | SaveConnectionSuccessMutationReceipt5 | SaveConnectionSuccessMutationReceipt6 | SaveConnectionSuccessMutationReceipt7 | SaveConnectionSuccessMutationReceipt8
SaveLibraryRequestSuccessRequestId: TypeAlias = str
SaveLibraryRequestSuccessRequestGap: TypeAlias = str
SaveLibraryRequestSuccessRequestOpenedAt: TypeAlias = str
SaveLibraryRequestSuccessRequestOriginRfpTurnId: TypeAlias = str | None
SaveLibraryRequestSuccessId: TypeAlias = str
SaveLibraryRequestSuccessGap: TypeAlias = str
SaveLibraryRequestSuccessOpenedAt: TypeAlias = str
SaveLibraryRequestSuccessOriginRfpTurnId: TypeAlias = str | None

class Account(TypedDict):
    id: int
    name: str

class Presentation(TypedDict):
    openPolicy: Literal['explicit']
    sensitiveUrl: Literal[True]
    instruction: Literal['Show the account and action. Open only at the user’s request; otherwise return the URL. Do not log or post this link publicly.']

class Page(TypedDict):
    resourceUri: Literal['ui://agentic-api/conversation-history/mcp-app.html', 'ui://agentic-api/agent-v2/mcp-app.html', 'ui://agentic-api/agents/mcp-app.html', 'ui://agentic-api/create-agent/mcp-app.html', 'ui://agentic-api/claim-agent/mcp-app.html', 'ui://agentic-api/configure-agent-connection/mcp-app.html', 'ui://agentic-api/register-agent-observed-revision/mcp-app.html', 'ui://agentic-api/buyer-account-admission/mcp-app.html', 'ui://agentic-api/tars-org-supply-asks/mcp-app.html', 'ui://agentic-api/tars-run-rate/mcp-app.html', 'ui://agentic-api/tars-marketing-email-library/mcp-app.html', 'ui://agentic-api/tars-marketing-email-operations/mcp-app.html', 'ui://agentic-api/business-rules/mcp-app.html', 'ui://agentic-api/acceptance-policy/mcp-app.html', 'ui://agentic-api/demo-storefront/mcp-app.html', 'ui://agentic-api/modular-inventory-source/mcp-app.html', 'ui://agentic-api/modular-connect/mcp-app.html', 'ui://agentic-api/modular-avails-commit/mcp-app.html', 'ui://agentic-api/plan-billing/mcp-app.html', 'ui://agentic-api/connections/mcp-app.html', 'ui://agentic-api/creative-engines/mcp-app.html', 'ui://agentic-api/all-advertisers-home/mcp-app.html', 'ui://agentic-api/add-advertiser/mcp-app.html', 'ui://agentic-api/campaigns/mcp-app.html', 'ui://agentic-api/creative-library-v3-assets-v1/mcp-app.html', 'ui://agentic-api/creative-library-v3/mcp-app.html', 'ui://agentic-api/upload-creative-asset/mcp-app.html', 'ui://agentic-api/creative-composer-task/mcp-app.html', 'ui://agentic-api/variant-gallery/mcp-app.html', 'ui://agentic-api/seller-setup/mcp-app.html', 'ui://agentic-api/approvals/mcp-app.html', 'ui://agentic-api/notifications/mcp-app.html', 'ui://agentic-api/buyer-notifications/mcp-app.html', 'ui://agentic-api/proposal-pass/mcp-app.html', 'ui://agentic-api/proposal-pass-v3/mcp-app.html', 'ui://agentic-api/demand-inbox/mcp-app.html', 'ui://agentic-api/demand-inbox-v3/mcp-app.html', 'ui://agentic-api/sessions/mcp-app.html', 'ui://agentic-api/seller-dashboard/mcp-app.html', 'ui://agentic-api/seller-dashboard-v3/mcp-app.html', 'ui://agentic-api/product-marketing/mcp-app.html', 'ui://agentic-api/product-marketing-v3/mcp-app.html', 'ui://agentic-api/library/mcp-app.html', 'ui://agentic-api/release-notes/mcp-app.html', 'ui://agentic-api/playbook/mcp-app.html', 'ui://agentic-api/merchandising-rules/mcp-app.html', 'ui://agentic-api/selling-terms/mcp-app.html', 'ui://agentic-api/media-kit/mcp-app.html', 'ui://agentic-api/business-profile/mcp-app.html', 'ui://agentic-api/buyer-discounts/mcp-app.html', 'ui://agentic-api/sponsored-buyers/mcp-app.html', 'ui://agentic-api/pending-operations/mcp-app.html', 'ui://agentic-api/storefront-briefs/mcp-app.html', 'ui://agentic-api/merchandising-simulator/mcp-app.html', 'ui://agentic-api/media-buys/mcp-app.html', 'ui://agentic-api/seller-accounts/mcp-app.html']
    advertiserId: NotRequired[str]
    campaignId: NotRequired[str]
    capability: Literal['reauthenticate_in_browser', 'manage_webhooks']

class Resume(TypedDict):
    kind: Literal['manual']
    reason: Literal['This Page has no durable completion receipt. Read the affected object before continuing; opening or closing the browser is not completion.']

class OpenCampaignsPageSuccessPageHumanHandoffRequired(TypedDict):
    kind: Literal['human_action_required']
    handoffId: str
    account: Account
    action: Literal['open_page', 'creative_upload']
    url: str
    expiresAt: str
    presentation: Presentation
    page: Page
    resume: Resume

class OpenCampaignsPageSuccessPageHumanHandoffUnavailable(TypedDict):
    kind: Literal['human_action_unavailable']
    account: Account
    action: Literal['open_page', 'creative_upload']
    reason: Literal['owner_browser_url_unavailable']
    instruction: Literal['This Page has no supported browser URL. Use an MCP UI host for this Page. Do not construct a platform URL or treat this result as completion.']
OpenCampaignReceiptSuccessReceiptBudgetTotal: TypeAlias = float
'\nTotal amount.\n'
OpenCampaignReceiptSuccessReceiptBudgetCurrency: TypeAlias = str
'\nISO 4217 currency.\n'

class OpenCampaignReceiptSuccessReceiptFlight(TypedDict):
    startAt: str
    '\n    Flight start (ISO 8601).\n    '
    endAt: str
    '\n    Flight end (ISO 8601).\n    '

class OpenCampaignReceiptSuccessReceiptMediaBuysItemFlight(TypedDict):
    startAt: str
    '\n    Flight start (ISO 8601).\n    '
    endAt: str
    '\n    Flight end (ISO 8601).\n    '
OpenCampaignReceiptSuccessReceiptMediaBuysItemBudgetTotal: TypeAlias = float
'\nTotal amount.\n'
OpenCampaignReceiptSuccessReceiptMediaBuysItemBudgetCurrency: TypeAlias = str
'\nISO 4217 currency.\n'
OpenCampaignReceiptSuccessReceiptStagedBudgetsItemTotal: TypeAlias = float
'\nTotal amount.\n'
OpenCampaignReceiptSuccessReceiptStagedBudgetsItemCurrency: TypeAlias = str
'\nISO 4217 currency.\n'
UploadCreativeAssetRequestAdvertiserId: TypeAlias = str
'\nBuyer-owned advertiser that owns the uploaded source.\n'
UploadCreativeAssetRequestCampaignCompositionAdvertiserId: TypeAlias = str
'\nBuyer-owned advertiser that owns the uploaded source.\n'
UploadCreativeAssetSuccessAdvertiserId: TypeAlias = str
'\nBuyer-owned advertiser that owns the uploaded source.\n'
UploadCreativeAssetSuccessCampaignCompositionAdvertiserId: TypeAlias = str
'\nBuyer-owned advertiser that owns the uploaded source.\n'

class GetDeliverySuccessRowsItemMetricsValue(TypedDict):
    value: float | bool | None
    status: Literal['available', 'unavailable']
    reason: NotRequired[Literal['projected_zero', 'missing', 'currency_unavailable', 'incomplete']]
GetDeliverySuccessRowsItemSourceOperation: TypeAlias = Literal['get_seller_reporting_metrics', 'get_buyer_reporting_metrics', 'get_seller_margin_reporting']

class Revision(TypedDict):
    sequenceNumber: NotRequired[float]
    observedAt: NotRequired[str]
    receivedAt: NotRequired[str]
    finalizedAt: NotRequired[str]
    dataThrough: NotRequired[str]
    sourceTimezone: NotRequired[str]
    restatesSequenceNumber: NotRequired[float | None]
GetDeliverySuccessRowsItemFinality = TypedDict('GetDeliverySuccessRowsItemFinality', {'status': Literal['available', 'unavailable', 'not_applicable'], 'class': Literal['SNAPSHOT', 'OFFICIAL'] | None, 'revision': Revision | None, 'reason': NotRequired[Literal['revision_evidence_unavailable', 'cumulative_margin_ledger']], 'supportedClasses': NotRequired[list[Literal['SNAPSHOT', 'OFFICIAL']]]})

class GetDeliverySuccessTotalsMetricsValue(TypedDict):
    value: float | bool | None
    status: Literal['available', 'unavailable']
    reason: NotRequired[Literal['projected_zero', 'missing', 'currency_unavailable', 'incomplete']]
GetDeliverySuccessTotalsFinality = TypedDict('GetDeliverySuccessTotalsFinality', {'status': Literal['available', 'unavailable', 'not_applicable'], 'class': Literal['SNAPSHOT', 'OFFICIAL'] | None, 'revision': Revision | None, 'reason': NotRequired[Literal['revision_evidence_unavailable', 'cumulative_margin_ledger']], 'supportedClasses': NotRequired[list[Literal['SNAPSHOT', 'OFFICIAL']]]})
GetDeliverySuccessSemanticsSourceOperation: TypeAlias = Literal['get_seller_reporting_metrics', 'get_buyer_reporting_metrics', 'get_seller_margin_reporting']
GetDeliverySuccessDeliverySummaryStatus: TypeAlias = str
GetDeliverySuccessDeliverySummaryTaskId: TypeAlias = str
GetDeliverySuccessDeliverySummaryReportingPeriodStart: TypeAlias = str
GetDeliverySuccessDeliverySummaryReportingPeriodEnd: TypeAlias = str
GetDeliverySuccessDeliverySummaryCurrency: TypeAlias = str
GetDeliverySuccessDeliverySummaryNextExpectedAt: TypeAlias = str
GetDeliverySuccessDeliverySummaryReportingRevisionReportingRevisionId: TypeAlias = str
GetDeliverySuccessDeliverySummaryReportingRevisionFinality: TypeAlias = str
GetDeliverySuccessDeliverySummaryReportingRevisionDataThrough: TypeAlias = str
GetDeliverySuccessDeliverySummaryReportingRevisionObservedAt: TypeAlias = str
GetDeliverySuccessDeliverySummaryReportingRevisionFinalizedAt: TypeAlias = str
GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricsValue: TypeAlias = float | None
GetDeliverySuccessDeliverySummaryAggregatedTotalsReachUnit: TypeAlias = str
GetDeliverySuccessDeliverySummaryAggregatedTotalsReachAggregation: TypeAlias = str
GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemMetricId: TypeAlias = str
GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierViewabilityStandard: TypeAlias = str
GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierCompletionSource: TypeAlias = str
GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierAttributionMethodology: TypeAlias = str

class GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierAttributionWindow(TypedDict):
    interval: int
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemVendorDomain: TypeAlias = str
GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemVendorBrandId: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemMediaBuyId: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemStatus: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemCurrency: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemExpectedAvailability: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemPricingModel: TypeAlias = Literal['cpm', 'vcpm', 'cpc', 'cpcv', 'cpv', 'cpp', 'cpa', 'revenue_share', 'flat_rate', 'time']
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemFinalizedAt: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsReachUnit: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsEffectiveRate: TypeAlias = float | None
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemPackageId: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemReachUnit: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemCurrency: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemDeliveryStatus: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemPricingModel: TypeAlias = Literal['cpm', 'vcpm', 'cpc', 'cpcv', 'cpv', 'cpp', 'cpa', 'revenue_share', 'flat_rate', 'time']
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemFinalizedAt: TypeAlias = str
GetDeliverySuccessDeliverySummaryPaginationCursor: TypeAlias = str
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsMetricsValue: TypeAlias = float | None

class GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsReachWindowPeriod(TypedDict):
    interval: int
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemMetricsValue: TypeAlias = float | None

class GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemReachWindowPeriod(TypedDict):
    interval: int
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemBreakdownStatusItemPaginationCursor: TypeAlias = str
SaveSellerRequestResolveBrand: TypeAlias = str
SaveSellerRequestOperatorDomain: TypeAlias = str
SaveSellerRequestChannelsItem: TypeAlias = Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence', 'audio', 'video']
'\nChannel.\n'
SaveSellerRequestCountriesItem: TypeAlias = str
SaveSellerRequestDefaultCurrency: TypeAlias = Literal['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD', 'CNY', 'HKD', 'SGD', 'SEK', 'NOK', 'DKK', 'PLN', 'KRW', 'INR', 'MXN', 'BRL', 'ZAR']
SaveSellerRequestPaymentCurrenciesItem: TypeAlias = Literal['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD', 'CNY', 'HKD', 'SGD', 'SEK', 'NOK', 'DKK', 'PLN', 'KRW', 'INR', 'MXN', 'BRL', 'ZAR']
SaveSellerRequestListingChannelsItem: TypeAlias = Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence', 'audio', 'video']
'\nChannel.\n'
SaveSellerRequestListingCountriesItem: TypeAlias = str
SaveSellerRequestMediaKitChannelsItem: TypeAlias = Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence', 'audio', 'video']
'\nChannel.\n'
SaveSellerRequestMediaKitCountriesItem: TypeAlias = str
SaveSellerSuccessBrand: TypeAlias = dict[str, JsonValue]
SaveSellerSuccessBefore: TypeAlias = dict[str, JsonValue]
SaveSellerSuccessAfter: TypeAlias = dict[str, JsonValue]
SaveSellerSuccessObject: TypeAlias = dict[str, JsonValue]
SaveSellerSuccessMaterialReceipt: TypeAlias = dict[str, JsonValue]
SaveInventorySourceSuccessObject: TypeAlias = dict[str, JsonValue]
SaveInventorySourceSuccessData: TypeAlias = dict[str, JsonValue]
SaveCoverageRequestAddItem: TypeAlias = str
SaveCoverageRequestAdd: TypeAlias = list[SaveCoverageRequestAddItem]
SaveCoverageRequestRemoveItem: TypeAlias = str
SaveCoverageRequestRemove: TypeAlias = list[SaveCoverageRequestRemoveItem]

class SaveCoverageSuccessAdded(TypedDict):
    items: list[JsonValue]
    count: int
    truncated: bool

class SaveCoverageSuccessRemoved(TypedDict):
    items: list[JsonValue]
    count: int
    truncated: bool

class SaveCoverageSuccessDeclared(TypedDict):
    items: list[JsonValue]
    count: int
    truncated: bool

class SaveCoverageSuccessFailures(TypedDict):
    items: list[JsonValue]
    count: int
    truncated: bool
SaveMaterialRequestSourceOriginalRef: TypeAlias = str
SaveMaterialRequestSourceOriginalDigest: TypeAlias = str

class Geometry(TypedDict):
    """
    Material geometry field.
    """
    page: NotRequired[int]
    '\n    Material page field.\n    '
    slide: NotRequired[int]
    '\n    Material slide field.\n    '
    sheet: NotRequired[int]
    '\n    Material sheet field.\n    '
    x: float
    '\n    Material x field.\n    '
    y: float
    '\n    Material y field.\n    '
    width: float
    '\n    Material width field.\n    '
    height: float
    '\n    Material height field.\n    '
    unit: Literal['pt', 'px', 'percent']
    '\n    Material unit field.\n    '

class Crop(TypedDict):
    """
    Material crop field.
    """
    x: float
    '\n    Material x field.\n    '
    y: float
    '\n    Material y field.\n    '
    width: float
    '\n    Material width field.\n    '
    height: float
    '\n    Material height field.\n    '
    unit: Literal['px', 'percent']
    '\n    Material unit field.\n    '

class Caption(TypedDict):
    """
    Material caption field.
    """
    text: str
    '\n    Material text field.\n    '
    origin: Literal['source', 'generated', 'operator']
    '\n    Material origin field.\n    '

class Ocr(TypedDict):
    """
    Material ocr field.
    """
    text: str
    '\n    Material text field.\n    '
    engine: str
    '\n    Material engine field.\n    '
    confidence: NotRequired[float]
    '\n    Material confidence field.\n    '

class AltText(TypedDict):
    """
    Material altText field.
    """
    text: str
    '\n    Material text field.\n    '
    origin: Literal['source', 'generated', 'operator']
    '\n    Material origin field.\n    '
AllowedContext: TypeAlias = str

class SaveMaterialRequestSourceReuseRights(TypedDict):
    reusePolicy: NotRequired[Literal['allowed', 'requires_approval', 'prohibited', 'unknown']]
    '\n    Material reusePolicy field.\n    '
    rightsBasis: NotRequired[Literal['owned', 'licensed', 'seller_attestation', 'public_web', 'operator_verified', 'unknown']]
    '\n    Material rightsBasis field.\n    '
    use: NotRequired[Literal['owned', 'licensed', 'seller_attested', 'unknown']]
    '\n    Material use field.\n    '
    summary: NotRequired[str]
    '\n    Material summary field.\n    '
    expiresAt: NotRequired[str]
    '\n    Material expiresAt field.\n    '
    allowedContexts: NotRequired[list[AllowedContext]]
    '\n    Material allowedContexts field.\n    '
SaveMaterialRequestSourceUrl: TypeAlias = str
SaveMaterialRequestSourceRootUrl: TypeAlias = str
SaveMaterialRequestSourceItemsItemUrl: TypeAlias = str
SaveMaterialRequestSourceItemsItemContentDigest: TypeAlias = str
SaveMaterialRequestSourceManifestDigest: TypeAlias = str
SaveMaterialRequestMetadataVisibility: TypeAlias = Literal['public', 'seller_private', 'advertiser_confidential']
SaveMaterialRequestDecisionCorrectionCorrectedContentSourceTextDigest: TypeAlias = str
SaveMaterialRequestSourceDerivedStructureOriginalDigest: TypeAlias = str
SaveMaterialRequestSourceDerivedStructureNodesItemTextDigest: TypeAlias = str
SaveMaterialRequestSourceDerivedStructureArtifactsItemDigest: TypeAlias = str

class SaveMaterialRequestSourceDerivedStructureArtifactsItemReuseRights(TypedDict):
    reusePolicy: NotRequired[Literal['allowed', 'requires_approval', 'prohibited', 'unknown']]
    '\n    Material reusePolicy field.\n    '
    rightsBasis: NotRequired[Literal['owned', 'licensed', 'seller_attestation', 'public_web', 'operator_verified', 'unknown']]
    '\n    Material rightsBasis field.\n    '
    use: NotRequired[Literal['owned', 'licensed', 'seller_attested', 'unknown']]
    '\n    Material use field.\n    '
    summary: NotRequired[str]
    '\n    Material summary field.\n    '
    expiresAt: NotRequired[str]
    '\n    Material expiresAt field.\n    '
    allowedContexts: NotRequired[list[AllowedContext]]
    '\n    Material allowedContexts field.\n    '
SaveMaterialRequestSourceDerivedStructureArtifactsItemConfidentiality: TypeAlias = Literal['public', 'seller_private', 'advertiser_confidential']
SaveMaterialRequestSourceRenditionRefsItemConfigurationDigest: TypeAlias = str
SaveMaterialRequestSourceItemsItemDerivedStructureOriginalDigest: TypeAlias = str
SaveMaterialRequestSourceItemsItemDerivedStructureNodesItemTextDigest: TypeAlias = str
SaveMaterialRequestSourceItemsItemDerivedStructureArtifactsItemDigest: TypeAlias = str

class SaveMaterialRequestSourceItemsItemDerivedStructureArtifactsItemReuseRights(TypedDict):
    reusePolicy: NotRequired[Literal['allowed', 'requires_approval', 'prohibited', 'unknown']]
    '\n    Material reusePolicy field.\n    '
    rightsBasis: NotRequired[Literal['owned', 'licensed', 'seller_attestation', 'public_web', 'operator_verified', 'unknown']]
    '\n    Material rightsBasis field.\n    '
    use: NotRequired[Literal['owned', 'licensed', 'seller_attested', 'unknown']]
    '\n    Material use field.\n    '
    summary: NotRequired[str]
    '\n    Material summary field.\n    '
    expiresAt: NotRequired[str]
    '\n    Material expiresAt field.\n    '
    allowedContexts: NotRequired[list[AllowedContext]]
    '\n    Material allowedContexts field.\n    '
SaveMaterialRequestSourceItemsItemDerivedStructureArtifactsItemConfidentiality: TypeAlias = Literal['public', 'seller_private', 'advertiser_confidential']
SaveMaterialSuccessFactsItem: TypeAlias = dict[str, JsonValue]
SaveMaterialSuccessMaterialId: TypeAlias = str
SaveMaterialSuccessSourceRevision: TypeAlias = int

class SaveMaterialSuccessRejectedItem(TypedDict):
    rowIndex: int
    field: str
    reason: str
SaveMaterialSuccessRejected: TypeAlias = list[SaveMaterialSuccessRejectedItem]

class SaveMaterialSuccessChanges(TypedDict):
    added: list[str]
    updated: list[str]
    removed: list[str]

class SaveMaterialSuccessFloorWarning(TypedDict):
    rowIndex: int
    productId: str
    sourceFloor: float
    rateCardPrice: float
    message: str
SaveMaterialSuccessFloorWarnings: TypeAlias = list[SaveMaterialSuccessFloorWarning]
SaveMaterialSuccessPreviewToken: TypeAlias = str | None
SaveMaterialSuccessPreviewExpiresAt: TypeAlias = str | None
SaveMaterialSuccessAcceptedTotal: TypeAlias = int
SaveMaterialSuccessRejectedTotal: TypeAlias = int
SaveMaterialSuccessTruncated: TypeAlias = bool
'\nTrue when any accepted, rejected, change, or floor-warning list is truncated.\n'
SaveMaterialSuccessFloorWarningsTruncated: TypeAlias = bool
'\nTrue when additional matching floor warnings were not returned.\n'
SaveMaterialSuccessRateCardMaterialId: TypeAlias = str
SaveMaterialSuccessRateCardSourceRevision: TypeAlias = int

class SaveMaterialSuccessRateCardRejectedItem(TypedDict):
    rowIndex: int
    field: str
    reason: str
SaveMaterialSuccessRateCardRejected: TypeAlias = list[SaveMaterialSuccessRateCardRejectedItem]

class SaveMaterialSuccessRateCardChanges(TypedDict):
    added: list[str]
    updated: list[str]
    removed: list[str]

class SaveMaterialSuccessRateCardFloorWarning(TypedDict):
    rowIndex: int
    productId: str
    sourceFloor: float
    rateCardPrice: float
    message: str
SaveMaterialSuccessRateCardFloorWarnings: TypeAlias = list[SaveMaterialSuccessRateCardFloorWarning]
SaveMaterialSuccessRateCardPreviewToken: TypeAlias = str | None
SaveMaterialSuccessRateCardPreviewExpiresAt: TypeAlias = str | None
SaveMaterialSuccessRateCardAcceptedTotal: TypeAlias = int
SaveMaterialSuccessRateCardRejectedTotal: TypeAlias = int
SaveMaterialSuccessRateCardTruncated: TypeAlias = bool
'\nTrue when any accepted, rejected, change, or floor-warning list is truncated.\n'
SaveMaterialSuccessRateCardFloorWarningsTruncated: TypeAlias = bool
'\nTrue when additional matching floor warnings were not returned.\n'
SaveMaterialSuccessMaterialReceipt: TypeAlias = dict[str, JsonValue]
SaveMaterialSuccessAcceptedItem: TypeAlias = dict[str, JsonValue]
SaveMaterialSuccessRateCardAcceptedItem: TypeAlias = dict[str, JsonValue]
SaveWholesaleProductSuccessWarningsItem: TypeAlias = dict[str, JsonValue]
SaveWholesaleProductSuccessErrorsItem: TypeAlias = dict[str, JsonValue]
SaveWholesaleProductSuccessMaterialReceipt: TypeAlias = dict[str, JsonValue]
SavePlaybookRequestDiscountsRulesItemHouseDomain: TypeAlias = str
SavePlaybookRequestDiscountsRemoveItemHouseDomain: TypeAlias = str
SavePlaybookSuccessPlaybook: TypeAlias = dict[str, JsonValue]
SavePlaybookSuccessMaterialReceipt: TypeAlias = dict[str, JsonValue]
SaveBusinessRulesSuccessBusinessRules: TypeAlias = dict[str, JsonValue]
SaveBusinessRulesSuccessMaterialReceipt: TypeAlias = dict[str, JsonValue]
SaveAdvertiserInstructionsRequestOperatorDomain: TypeAlias = str
SaveAdvertiserInstructionsRequestBrandDomain: TypeAlias = str
SaveSignalSuccessObject: TypeAlias = dict[str, JsonValue]
SaveSignalSuccessMaterialReceipt: TypeAlias = dict[str, JsonValue]
SaveRfpRequestI: TypeAlias = str
'\nLeading/trailing whitespace is trimmed; the result must contain a visible character and no control, bidi, or line-separator characters.\n'
SaveRfpRequestP: TypeAlias = str
SaveRfpRequestK: TypeAlias = str
'\nLeading/trailing whitespace is trimmed; the result must contain a visible character and no control, bidi, or line-separator characters.\n'
SaveRfpRequestJ: TypeAlias = Union[SaveRfpRequestP, list['SaveRfpRequestJ'], dict[SaveRfpRequestK, 'SaveRfpRequestJ'], float, bool, None]
SaveRfpRequestOriginBuyer: TypeAlias = str
SaveRfpRequestOriginAdvertiser: TypeAlias = str
SaveRfpRequestOriginCategory: TypeAlias = str
SaveRfpRequestOriginMarket: TypeAlias = str
SaveRfpRequestRequestDimensionsChannel: TypeAlias = str
SaveRfpRequestRequestDimensionsFormatKinds: TypeAlias = list[Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']]
SaveRfpRequestRequestDimensionsProductCount: TypeAlias = int
SaveRfpRequestRequestDimensionsPlanRole: TypeAlias = str
SaveRfpRequestRequestDimensionsPlanRoles: TypeAlias = list[SaveRfpRequestRequestDimensionsPlanRole]
SaveRfpRequestRequestDimensionsAudience: TypeAlias = str
SaveRfpRequestRequestConstraintsFormatKinds: TypeAlias = list[Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']]
SaveRfpRequestRequestConstraintsProductCount: TypeAlias = int
SaveRfpRequestRequestConstraintsPlanRole: TypeAlias = str
SaveRfpRequestRequestConstraintsPlanRoles: TypeAlias = list[SaveRfpRequestRequestConstraintsPlanRole]
SaveRfpRequestRequestConstraintsMeasurementRequirements: TypeAlias = list[Literal['brand_lift', 'closed_loop_attribution', 'sales_attribution']]
SaveRfpRequestRequestConstraintsLocale: TypeAlias = str
SaveRfpRequestRequestConstraintsMustIncludeItem: TypeAlias = str
SaveRfpRequestStrategyPosture: TypeAlias = str
SaveRfpRequestRepresentationLocale: TypeAlias = str
SaveRfpRequestOriginChannelsItem: TypeAlias = str
SaveRfpRequestRequestDimensionsChannelsItem: TypeAlias = str
SaveRfpRequestRequestDimensionsCreativeInputsItem: TypeAlias = str
SaveRfpRequestRequestConstraintsRequiredCreativeInputsItem: TypeAlias = str
SaveRfpSuccessRfpId: TypeAlias = str
SaveRfpSuccessTurnId: TypeAlias = str
SaveRfpSuccessIdempotentReplay: TypeAlias = bool

class Arguments(TypedDict):
    kind: Literal['rfp_turn']
    id: str

class SaveRfpSuccessNextRfpTurn(TypedDict):
    tool: Literal['get']
    arguments: Arguments

class Arguments1(TypedDict):
    kind: Literal['rfp']
    id: str

class SaveRfpSuccessNextRfp(TypedDict):
    tool: Literal['get']
    arguments: Arguments1

class SaveBuyerOperatorSuccessUpdateBuyerOperatorBody(TypedDict):
    """
    Confirm or change the authenticated buyer account's commercial operator domain.
    """
    operatorDomain: str
    '\n    Corporate domain of the organization operating this buyer account.\n    '
    operatorScope: NotRequired[Literal['whole_operator', 'specific_unit']]
    '\n    Whether this account represents the whole operator or one specific operating unit. Required for a confirmed AdCP 3.2 identity; omitted only by legacy clients.\n    '
    operatorUnitId: NotRequired[str]
    '\n    Stable operator-issued identifier for the office, team, region, or seat. It is seller-visible and is not an Interchange database ID.\n    '
SaveBuyerAgentRequestDisplayName: TypeAlias = str
SaveBuyerAgentRequestId: TypeAlias = str
SaveBuyerAgentRequestLifecycleConfirmationText: TypeAlias = str
'\nExact current display name; required to suspend or retire.\n'

class CredentialHandoff(TypedDict):
    reference: str
    principalId: str
    expiresAt: str
    verificationState: Literal['pending', 'issuing', 'credential_active', 'invalidated', 'expired', 'reconciliation_required']
    ceremonyPath: str

class AdministrationHandle(TypedDict):
    type: Literal['workos_m2m']
    subject: str

class AdministrationHandle1(TypedDict):
    type: Literal['api_key']
    serviceTokenId: str

class SaveBuyerAgentSuccessBuyerAgentCredential(TypedDict):
    credentialRef: str
    credentialType: Literal['workos_m2m', 'api_key', 'domain_rfc9421', 'runtime_token']
    bindingState: Literal['active', 'retired']
    administrationHandle: AdministrationHandle | AdministrationHandle1 | None
    boundAt: str
    lastVerifiedAt: str
    retiredAt: str | None

class SaveBuyerAgentSuccessBuyerAgentAdvertiser(TypedDict):
    advertiserId: str
    name: str
    role: Literal['READ', 'READ_WRITE']

class SaveBuyerAgentSuccessBuyerAgentNotificationSubscription(TypedDict):
    storefrontId: int
    subscriberId: str
    desiredActive: bool
    proofState: Literal['pending', 'verified', 'failed', 'stale']

class SaveBuyerAgentSuccessBuyerAgentNotificationDestination(TypedDict):
    storefrontId: int
    destinationId: str
    destinationRef: str
    desiredActive: bool
    lifecycle: Literal['current', 'superseded', 'revoked']

class EventSource(TypedDict):
    eventSourceId: str
    '\n    Event source to include (must be configured via sync_event_sources)\n    '
    eventType: Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']
    '\n    IAB ECAPI event type to optimize for\n    '
    customEventName: NotRequired[str]
    "\n    Required when eventType is 'custom'. Platform-specific custom event name.\n    "
    valueField: NotRequired[str]
    "\n    Field on custom_data carrying the monetary value. Required when target is 'per_ad_spend'.\n    "
    valueFactor: NotRequired[float]
    '\n    Multiplier for valueField (default 1). Use -1 for refunds, 0.01 for cents.\n    '

class Target(TypedDict):
    """
    Target cost or return. When omitted, the seller maximizes conversions within budget.
    """
    kind: Literal['per_ad_spend']
    '\n    Target kind.\n    '
    value: float
    '\n    Target return ratio (e.g. 4.0 = $4 of value per $1 spent)\n    '

class Target1(TypedDict):
    """
    Target cost or return. When omitted, the seller maximizes conversions within budget.
    """
    kind: Literal['maximize_value']
    '\n    Target kind.\n    '

class SaveCampaignRequestDuration(TypedDict):
    """
    A duration expressed as an interval and unit
    """
    interval: int
    '\n    Interval count.\n    '
    unit: Literal['minutes', 'hours', 'days', 'campaign']
    '\n    Interval unit.\n    '

class Target2(TypedDict):
    """
    Target for this metric. When omitted, the seller maximizes metric volume within budget.
    """
    kind: Literal['threshold_rate']
    '\n    Target kind.\n    '
    value: float
    '\n    Min per-impression threshold. Proportion, seconds, or score depending on metric.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared111(TypedDict):
    country: NotRequired[Literal['US']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['zip', 'zip_plus_four']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared112(TypedDict):
    country: NotRequired[Literal['GB']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['outward', 'full']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared113(TypedDict):
    country: NotRequired[Literal['CA']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['fsa', 'full']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared114(TypedDict):
    country: NotRequired[Literal['DE', 'CH', 'AT']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['plz']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared115(TypedDict):
    country: NotRequired[Literal['FR']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['code_postal']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared116(TypedDict):
    country: NotRequired[Literal['AU']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['postcode']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared117(TypedDict):
    country: NotRequired[Literal['BR']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['cep']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared118(TypedDict):
    country: NotRequired[Literal['IN']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['pin']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared119(TypedDict):
    country: NotRequired[Literal['ZA']]
    '\n    Country code.\n    '
    system: NotRequired[Literal['postal_code']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared1110(TypedDict):
    country: NotRequired[JsonValue]
    '\n    Country code.\n    '
    system: NotRequired[Literal['postal_code', 'custom']]
    '\n    Code system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared1111(TypedDict):
    country: str
    '\n    Country code.\n    '
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Code system.\n    '
    values: list[str]
    '\n    Values in this system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared1112(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1113(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1114(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1115(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1116(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1117(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1118(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1119(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1120(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class SaveCampaignRequestCampaignTargetingOverlayShared1121(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]
SaveCampaignRequestCampaignTargetingOverlayShared11: TypeAlias = SaveCampaignRequestCampaignTargetingOverlayShared1112 | SaveCampaignRequestCampaignTargetingOverlayShared1113 | SaveCampaignRequestCampaignTargetingOverlayShared1114 | SaveCampaignRequestCampaignTargetingOverlayShared1115 | SaveCampaignRequestCampaignTargetingOverlayShared1116 | SaveCampaignRequestCampaignTargetingOverlayShared1117 | SaveCampaignRequestCampaignTargetingOverlayShared1118 | SaveCampaignRequestCampaignTargetingOverlayShared1119 | SaveCampaignRequestCampaignTargetingOverlayShared1120 | SaveCampaignRequestCampaignTargetingOverlayShared1121

class SaveCampaignRequestCampaignTargetingOverlayShared12(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Code system.\n    '
    values: list[str]
    '\n    Values in this system.\n    '
SaveCampaignRequestCampaignTargetingOverlayShared1: TypeAlias = list[SaveCampaignRequestCampaignTargetingOverlayShared11 | SaveCampaignRequestCampaignTargetingOverlayShared12]
'\nPostal-area groups.\n'
Value: TypeAlias = str

class SaveCampaignRequestCampaignTargetingOverlayShared2Item1(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Code system.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this system.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared2Item2(TypedDict):
    country: str
    '\n    Country code.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Code system.\n    '
    system_version: NotRequired[str]
    '\n    Identifier-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Place category.\n    '
    values: list[Value]
    '\n    Values in this system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels by value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class SaveCampaignRequestCampaignTargetingOverlayShared2Item3(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
SaveCampaignRequestCampaignTargetingOverlayShared2Item: TypeAlias = SaveCampaignRequestCampaignTargetingOverlayShared2Item3
SaveCampaignRequestCampaignTargetingOverlayShared2: TypeAlias = list[SaveCampaignRequestCampaignTargetingOverlayShared2Item]
'\nNamed place groups.\n'

class SaveCampaignRequestCampaignTargetingOverlayShared3Item(TypedDict):
    system: Literal['nielsen_dma', 'uk_itl1', 'uk_itl2', 'eurostat_nuts2', 'custom']
    '\n    Code system.\n    '
    values: list[str]
    '\n    Values in this system.\n    '
SaveCampaignRequestCampaignTargetingOverlayShared3: TypeAlias = list[SaveCampaignRequestCampaignTargetingOverlayShared3Item]
'\nMetro groups.\n'
SaveCampaignRequestCampaignTargetingOverlayShared4: TypeAlias = list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]
'\nDevice platforms.\n'
SaveCampaignRequestCampaignTargetingOverlayShared5: TypeAlias = list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]
'\nBrowsers.\n'
SaveCampaignRequestCampaignTargetingOverlayShared6: TypeAlias = list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]
'\nDevice types.\n'
SaveCampaignRequestTrackingTrackersItemTrackerId: TypeAlias = str
SaveCampaignRequestTrackingOverridesItemTrackerId: TypeAlias = str
SaveCampaignRequestTargetingGeoItemStrength: TypeAlias = Literal['required', 'preferred']
SaveCampaignRequestTargetingGeoItemIncludeItem: TypeAlias = str
SaveCampaignRequestTargetingGeoItemExcludeItem: TypeAlias = str
SaveCampaignRequestTargetingLanguageItemStrength: TypeAlias = Literal['required', 'preferred']
SaveCampaignRequestTargetingLanguageItemIncludeItem: TypeAlias = str
SaveCampaignRequestTargetingLanguageItemExcludeItem: TypeAlias = str
SaveCampaignRequestTargetingDeviceItemStrength: TypeAlias = Literal['required', 'preferred']
SaveCampaignRequestTargetingDaypartsItemStrength: TypeAlias = Literal['required', 'preferred']
SaveCampaignRequestTargetingDemographicsAgeItemStrength: TypeAlias = Literal['required', 'preferred']
SaveCampaignRequestChannelGroupsItemChannelGroupId: TypeAlias = str
'\nCampaign-local stable identifier. One downstream media buy cannot span two channelGroupIds.\n'
SaveCampaignRequestChannelGroupsItemName: TypeAlias = str

class SaveCampaignRequestEventGoalTargetCostPer(TypedDict):
    kind: Literal['cost_per']
    '\n    Target kind.\n    '
    value: float
    '\n    Target cost per unit in buy currency\n    '

class SaveCampaignRequestMetricGoalTargetCostPer(TypedDict):
    kind: Literal['cost_per']
    '\n    Target kind.\n    '
    value: float
    '\n    Target cost per unit in buy currency\n    '
SaveCampaignSuccessDroppedOptimizationGoalCode: TypeAlias = Literal['goal_kind_not_declared', 'metric_not_declared', 'target_kind_not_declared', 'reach_unit_not_declared', 'view_duration_not_declared', 'viewability_standard_not_declared', 'vendor_metric_not_declared', 'over_max_optimization_goals']
"\nWhy the goal was not sent: the product's AdCP optimization declaration (metric_optimization, conversion_tracking, vendor_metric_optimization) does not cover the goal's kind, metric, target kind, reach unit, view duration, viewability standard or vendor metric, or the product's max_optimization_goals was reached.\n"

class SaveCampaignSuccessPropertyListAttachmentCascade(TypedDict):
    totalMediaBuys: int
    updatedCount: int
    failedCount: int
    skippedCount: int

class SaveCampaignSuccessPropertyListClearCascade(TypedDict):
    totalMediaBuys: int
    updatedCount: int
    failedCount: int
    skippedCount: int

class SaveCampaignSuccessLaunchMediaBuysItemBudget(TypedDict):
    total: float
    currency: str

class SaveCampaignSuccessLaunchCombinedBudget(TypedDict):
    total: float
    currency: str

class SaveCampaignSuccessLaunchBudgetsByCurrencyItem(TypedDict):
    total: float
    currency: str
SaveEventSourceRequestEventSourceActionSource: TypeAlias = Literal['website', 'app', 'offline', 'phone_call', 'chat', 'email', 'in_store', 'system_generated', 'other']
'\nAdCP flat action-source category for this event source\n'

class SaveEventSourceRequestEventSourceSurface(TypedDict):
    """
    AdCP EventSurface this source represents, for when the flat actionSource is too coarse.
    """
    category: Literal['owned_property', 'website', 'app', 'offline', 'phone_call', 'chat', 'email', 'in_store', 'system_generated', 'other']
    '\n    Generic surface category; owned_property = durable creator/brand property (channel, feed, etc).\n    '
    property_type: NotRequired[str]
    '\n    Open vocabulary for the property kind, e.g. channel, profile, feed, podcast, playlist, newsletter.\n    '
    namespace: NotRequired[str]
    '\n    Platform, publisher, or system namespace for the property, e.g. video_platform, audio_service.\n    '
    property_id: NotRequired[str]
    '\n    Identifier for the property within namespace.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension object, namespaced by vendor key.\n    '

class Surface(TypedDict):
    category: Literal['owned_property', 'website', 'app', 'offline', 'phone_call', 'chat', 'email', 'in_store', 'system_generated', 'other']
    property_type: NotRequired[str]
    namespace: NotRequired[str]
    property_id: NotRequired[str]
    ext: NotRequired[dict[str, JsonValue]]

class Detail(TypedDict):
    score: float
    max_score: float
    label: NotRequired[str]

class Issue(TypedDict):
    severity: Literal['error', 'warning', 'info']
    message: str

class Health(TypedDict):
    """
    AdCP EventSourceHealth: status is the grade; issues name what needs attention.
    """
    status: Literal['insufficient', 'minimum', 'good', 'excellent']
    detail: NotRequired[Detail]
    match_rate: NotRequired[float]
    last_event_at: NotRequired[str]
    evaluated_at: NotRequired[str]
    events_received_24h: NotRequired[int]
    issues: NotRequired[list[Issue]]

class Storefront(TypedDict):
    id: str
    '\n    Storefront ID.\n    '
    name: str
    '\n    Storefront name.\n    '

class Setup(TypedDict):
    snippet: NotRequired[str]
    snippet_type: NotRequired[Literal['javascript', 'html', 'pixel_url', 'server_only']]
    instructions: NotRequired[str]
SaveEventSourceSuccessEventSourceActionSource: TypeAlias = Literal['website', 'app', 'offline', 'phone_call', 'chat', 'email', 'in_store', 'system_generated', 'other']
'\nAdCP flat action-source category for this event source\n'
SaveEventSourceSuccessSellerObjectSyncState: TypeAlias = Literal['pending', 'syncing', 'synced', 'ending', 'removing', 'removed', 'failed', 'expired', 'superseded', 'needs_reconciliation']
'\nState of one buyer object on one seller account: pending, syncing, synced, ending, removing, removed, failed, expired, superseded, or needs_reconciliation.\n'
SaveEventSourceSuccessSellerObjectSyncBlockerCode: TypeAlias = Literal['SELLER_OBJECT_TYPE_UNSUPPORTED', 'SELLER_OBJECT_INGESTION_UNMAPPABLE', 'SELLER_OBJECT_CAPABILITIES_UNAVAILABLE', 'SELLER_OBJECT_SYNC_PENDING', 'SELLER_OBJECT_SYNC_FAILED', 'SELLER_OBJECT_SYNC_EXPIRED', 'SELLER_OBJECT_SYNC_RECONCILIATION_REQUIRED', 'SELLER_PROPERTY_LIST_UNSUPPORTED', 'SELLER_DATA_SHARING_NOT_PERMITTED', 'SELLER_CREATIVE_REVIEW_PENDING', 'SELLER_CREATIVE_REJECTED', 'ESA_AUDIENCE_NAMESPACE_UNRESOLVED']
'\nNamed reason a buyer object cannot be used on a seller account, from the seller-object-sync blocker table.\n'

class SaveEventSourceSuccessArchivedEventSourceEntry(TypedDict):
    action: Literal['archived']
    eventSourceId: str

class SaveEventSourceSuccessEventSourceEntryError(TypedDict):
    code: str
    message: str
    field: NotRequired[str]
    recovery: NotRequired[Literal['transient', 'correctable', 'terminal']]
SaveDimensionRequestName: TypeAlias = str
'\nDimension display name. Required when creating; optional on update by id.\n'
SaveDimensionRequestValuesMode: TypeAlias = Literal['open', 'governed']
'\nValue policy. Required when creating; optional on update by id. Open creates values on label.\n'
SaveDimensionRequestAppliesTo: TypeAlias = list[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
'\nMaterial is seller-only. Buyers label advertiser, campaign, creative, and creative_asset.\n'
SaveDimensionRequestRetired: TypeAlias = bool

class SaveDimensionRequestValue(TypedDict):
    value: str
    '\n    Stable value slug.\n    '
    name: NotRequired[str]
    '\n    Display name.\n    '
    retired: NotRequired[bool]
    '\n    Hide this value.\n    '
    mergeInto: NotRequired[str]
    '\n    Move labels to this value.\n    '
SaveDimensionRequestValues: TypeAlias = list[SaveDimensionRequestValue]
SaveDimensionRequestIdempotencyKey: TypeAlias = str
'\nStable request key.\n'

class Usage(TypedDict):
    advertiser: float
    campaign: float
    material: float
    creative_asset: float
    creative: float

class Value1(TypedDict):
    value: str
    name: str
    retired: bool

class SaveDimensionSuccessDimension(TypedDict):
    id: str
    key: str
    name: str
    valuesMode: Literal['open', 'governed']
    appliesTo: list[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    usage: Usage
    retired: bool
    values: list[Value1]
    createdAt: str
    updatedAt: str

class SavePropertyListRequestPropertyListIdentifier(TypedDict):
    """
    A typed property identifier (AdCP-aligned, sourced from `@adcp/sdk`). Read-side note: Apple App Store bundles share a single backing column, so `apple_tv_bundle` write-time entries normalize to `ios_bundle` on subsequent get/list responses. `bundle_id` (generic fallback) likewise normalizes to the resolved app row's store-typed form (`ios_bundle` or `android_package`).
    """
    type: Literal['domain', 'subdomain', 'network_id', 'ios_bundle', 'android_package', 'apple_app_store_id', 'google_play_id', 'roku_store_id', 'fire_tv_asin', 'samsung_app_id', 'apple_tv_bundle', 'bundle_id', 'venue_id', 'screen_id', 'openooh_venue_type', 'rss_url', 'apple_podcast_id', 'spotify_collection_id', 'podcast_guid', 'station_id', 'facility_id']
    '\n    AdCP property identifier type, such as domain, app, CTV, DOOH, audio, radio, or network.\n    '
    value: str
    '\n    Identifier value for the selected AdCP property type.\n    '

class FeatureRequirement(TypedDict):
    feature_id: str
    '\n    Feature identifier.\n    '
    min_value: NotRequired[float | None]
    '\n    Minimum acceptable feature value.\n    '
    max_value: NotRequired[float | None]
    '\n    Maximum acceptable feature value.\n    '
    allowed_values: NotRequired[list[JsonValue] | None]
    '\n    Accepted categorical feature values.\n    '
    if_not_covered: NotRequired[Literal['exclude', 'include'] | None]
    '\n    How to treat properties without this feature.\n    '

class SavePropertyListRequestPropertyListFilters(TypedDict):
    channels_any: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement']] | None]
    '\n    Restrict to SmartPropertyLists matching these channels\n    '
    countries_all: NotRequired[list[str] | None]
    '\n    ISO 3166-1 alpha-2 country codes\n    '
    property_types: NotRequired[list[Literal['website', 'mobile_app', 'ctv_app', 'desktop_app', 'dooh', 'podcast', 'radio', 'streaming_audio']] | None]
    '\n    Property inventory types\n    '
    feature_requirements: NotRequired[list[FeatureRequirement] | None]
    '\n    Feature-based requirements (e.g. IVT, MFA, green)\n    '

class SavePropertyListSuccessPropertyListFilters(TypedDict):
    channels_any: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement']] | None]
    '\n    Restrict to SmartPropertyLists matching these channels\n    '
    countries_all: NotRequired[list[str] | None]
    '\n    ISO 3166-1 alpha-2 country codes\n    '
    property_types: NotRequired[list[Literal['website', 'mobile_app', 'ctv_app', 'desktop_app', 'dooh', 'podcast', 'radio', 'streaming_audio']] | None]
    '\n    Property inventory types\n    '
    feature_requirements: NotRequired[list[FeatureRequirement] | None]
    '\n    Feature-based requirements (e.g. IVT, MFA, green)\n    '

class SavePropertyListSuccessPropertyListResolutionSummary(TypedDict):
    """
    Counts describing how a submitted identifier set resolved against the AAO registry and local catalog.
    """
    totalRequested: int
    '\n    Number of unique identifiers the caller submitted (after per-type normalization and dedup)\n    '
    resolvedCount: int
    '\n    Identifiers successfully resolved to local Property records\n    '
    registeredCount: int
    '\n    Identifiers present in the AAO registry but with no local Property record yet (not yet targetable)\n    '
    unresolvedCount: int
    '\n    Identifiers not found anywhere; they will NOT participate in targeting\n    '
    resolutionRate: float
    '\n    resolvedCount / totalRequested as a fraction 0–1 (0 when totalRequested is 0)\n    '

class SavePropertyListSuccessPropertyListCascadeSummary(TypedDict):
    """
    Summary of the retroactive push of this updated property list to active media buys.
    """
    totalMediaBuys: int
    '\n    Active media buys found whose advertisers reference this list. Each received an update_media_buy call with the refreshed list reference.\n    '
    updatedCount: int
    '\n    Active media buys that were successfully notified of the updated list\n    '
    failedCount: int
    '\n    Active media buys where the update_media_buy call failed. See server logs for details.\n    '
SaveCreativeRequestAssetsItemUrl: TypeAlias = str
'\nURL to add as asset (must be http/https)\n'
SaveCreativeRequestSourceAssetsItemSlot: TypeAlias = str
SaveCreativeRequestSourceAssetsItemLabel: TypeAlias = str
SaveCreativeRequestSourceAssetsItemMakePrimary: TypeAlias = bool
SaveCreativeRequestClickUrl: TypeAlias = str
'\nURL to add as asset (must be http/https)\n'
SaveCreativeRequestSocialComponentsItemUrl: TypeAlias = str
'\nURL to add as asset (must be http/https)\n'

class Dimensions(TypedDict):
    """
    Known asset dimensions.
    """
    width: NotRequired[int]
    '\n    Width in pixels.\n    '
    height: NotRequired[int]
    '\n    Height in pixels.\n    '
    duration_seconds: NotRequired[float]
    '\n    Duration in seconds.\n    '

class RenderCrop(TypedDict):
    """
    Requested render crop.
    """
    x: float
    '\n    Normalized horizontal crop origin.\n    '
    y: float
    '\n    Normalized vertical crop origin.\n    '
    width: float
    '\n    Normalized crop width.\n    '
    height: float
    '\n    Normalized crop height.\n    '
    units: NotRequired[Literal['normalized']]
    '\n    Crop coordinate units.\n    '
    source: NotRequired[Literal['user', 'system', 'dam', 'product_catalog']]
    '\n    Source of the crop.\n    '
    notes: NotRequired[str]
    '\n    Crop notes.\n    '
SaveCreativeSessionRequestDraftRenditionsItemSource: TypeAlias = Literal['upload', 'url', 'dam', 'product_catalog', 'brand_library', 'local', 'generated']
SaveCreativeSessionRequestDraftRenditionsItemRole: TypeAlias = Literal['product', 'logo', 'background', 'reference', 'copy', 'audio', 'video']
SaveCreativeSessionRequestDraftRenditionsItemRightsUsage: TypeAlias = str
SaveCreativeSessionRequestDraftRenditionsItemRightsExpiresAt: TypeAlias = str
SaveCreativeSessionRequestDraftRenditionsItemRightsNotes: TypeAlias = str
SaveCreativeSessionRequestDraftSourceAssetSource: TypeAlias = Literal['upload', 'url', 'dam', 'product_catalog', 'brand_library', 'local', 'generated']
SaveCreativeSessionRequestDraftSourceAssetRole: TypeAlias = Literal['product', 'logo', 'background', 'reference', 'copy', 'audio', 'video']
SaveCreativeSessionRequestDraftSourceAssetRightsUsage: TypeAlias = str
SaveCreativeSessionRequestDraftSourceAssetRightsExpiresAt: TypeAlias = str
SaveCreativeSessionRequestDraftSourceAssetRightsNotes: TypeAlias = str
SaveCreativeSessionRequestDraftAssetsItemSource: TypeAlias = Literal['upload', 'url', 'dam', 'product_catalog', 'brand_library', 'local', 'generated']
SaveCreativeSessionRequestDraftAssetsItemRole: TypeAlias = Literal['product', 'logo', 'background', 'reference', 'copy', 'audio', 'video']
SaveCreativeSessionRequestDraftAssetsItemRightsUsage: TypeAlias = str
SaveCreativeSessionRequestDraftAssetsItemRightsExpiresAt: TypeAlias = str
SaveCreativeSessionRequestDraftAssetsItemRightsNotes: TypeAlias = str
SaveCreativeSessionSuccessCreativeSessionDetail: TypeAlias = dict[str, JsonValue]
SaveCreativeSessionSuccessCreativeSessionTruncated: TypeAlias = Literal[True]
SaveCreativeSessionSuccessCreativeSessionOmitted: TypeAlias = dict[str, int]
SaveCreativeSessionSuccessCreativeSessionRevision: TypeAlias = int
SaveCreativeSessionSuccessCreativeSessionGeneration: TypeAlias = str

class Arguments2(TypedDict):
    campaignId: str
    sessionId: str
    actionKey: str
    expectedRevision: int
    sessionGeneration: str

class SaveCreativeSessionSuccessCreativeSessionNextGenerateVariants(TypedDict):
    tool: Literal['generate_variants']
    arguments: Arguments2

class Preview(TypedDict):
    type: str
    url: str
    width: NotRequired[float]
    height: NotRequired[float]

class Variant(TypedDict):
    id: str
    name: str
    direction: NotRequired[str]
    status: NotRequired[str]
    preview: Preview

class Terminal(TypedDict):
    notDispatched: int
    uncertain: int
    replacementActionRequired: Literal[True]
    chargeMayHaveOccurred: NotRequired[Literal[True]]

class SaveCreativeSessionSuccessCreativeSessionGallery(TypedDict):
    campaignId: str
    sessionId: str
    advertiserId: NotRequired[str]
    revision: int
    sessionGeneration: NotRequired[str]
    variants: list[Variant]
    selectedVariantId: NotRequired[str]
    approvedVariantId: NotRequired[str]
    approvedSessionRevision: NotRequired[int]
    approvedOutputHash: NotRequired[str]
    finalCreativeId: NotRequired[str]
    generationPending: bool
    terminal: NotRequired[Terminal]
GenerateVariantsRequestCampaignId: TypeAlias = str
'\nOwning campaign ID.\n'
GenerateVariantsRequestSessionId: TypeAlias = str
'\nSaved session ID.\n'
GenerateVariantsRequestActionKey: TypeAlias = str
'\nAction key; reuse only for an identical retry.\n'
GenerateVariantsRequestExpectedRevision: TypeAlias = int
'\nSaved revision to generate from.\n'
GenerateVariantsRequestSessionGeneration: TypeAlias = str
'\nCurrent session lifecycle ID.\n'

class SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef1(TypedDict):
    scope: Literal['product']
    '\n    Product scope.\n    '
    signal_id: str
    '\n    Product Signal ID.\n    '

class SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef2(TypedDict):
    scope: Literal['data_provider']
    '\n    Provider scope.\n    '
    data_provider_domain: str
    '\n    Provider domain.\n    '
    signal_id: str
    '\n    Provider Signal ID.\n    '

class SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef3(TypedDict):
    scope: Literal['signal_source']
    '\n    Source Signal scope.\n    '
    signal_source_url: str
    '\n    Source URL.\n    '
    signal_id: str
    '\n    Source Signal ID.\n    '
SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef: TypeAlias = SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef1 | SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef2 | SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef3

class SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetFrequencyWindow(TypedDict):
    """
    Duration used for frequency or attribution.
    """
    interval: int
    '\n    Number of units in the window.\n    '
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
    '\n    Unit for the optimization window.\n    '
SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemViewDurationSeconds: TypeAlias = float
SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority: TypeAlias = int
SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetValue: TypeAlias = float

class SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemAttributionWindowPostClick(TypedDict):
    """
    Duration used for frequency or attribution.
    """
    interval: int
    '\n    Number of units in the window.\n    '
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
    '\n    Unit for the optimization window.\n    '

class SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemAttributionWindowPostView(TypedDict):
    """
    Duration used for frequency or attribution.
    """
    interval: int
    '\n    Number of units in the window.\n    '
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
    '\n    Unit for the optimization window.\n    '
SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPerValue: TypeAlias = float
SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRateValue: TypeAlias = float
SaveMediaBuySuccessMediaBuyRefsItemPendingAt: TypeAlias = Literal['storefront', 'salesagent', 'unknown']
SaveMediaBuySuccessMediaBuyRefsItemPendingChangePendingAt: TypeAlias = Literal['storefront', 'salesagent', 'unknown']
SaveMediaBuySuccessMediaBuyRefsItemPhase: TypeAlias = Literal['draft', 'pendingApproval', 'inputRequired', 'active', 'completed', 'canceled', 'failed', 'rejected']
SaveMediaBuySuccessMediaBuyGoalCommitmentKind: TypeAlias = Literal['guaranteed', 'best_effort', 'report_only']

class SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget1(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['cost_per']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget2(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['threshold_rate']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget3(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['per_ad_spend']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget4(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['maximize_value']
SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget: TypeAlias = SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget1 | SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget2 | SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget3 | SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget4
'\nA goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).\n'

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget1(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['cost_per']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget2(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['threshold_rate']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget3(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['per_ad_spend']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget4(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['maximize_value']
SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget: TypeAlias = SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget1 | SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget2 | SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget3 | SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget4
'\nA goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).\n'
SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemCommitment: TypeAlias = Literal['guaranteed', 'best_effort', 'report_only']

class Window(TypedDict):
    """
    Counting window for the cap.
    """
    interval: int
    '\n    Positive whole-number window length.\n    '
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
    '\n    Window unit.\n    '

class SaveMediaBuySuccessMediaBuyFrequencyCapRequested(TypedDict):
    """
    Seller-enforced AdCP 3.2 cap configuration.
    """
    maxImpressions: int
    '\n    Maximum impressions allowed in the window.\n    '
    per: Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']
    '\n    Reach unit counted by the seller.\n    '
    window: Window
    '\n    Counting window for the cap.\n    '

class SaveMediaBuySuccessMediaBuyFrequencyCapEffective(TypedDict):
    """
    Seller-enforced AdCP 3.2 cap configuration.
    """
    maxImpressions: int
    '\n    Maximum impressions allowed in the window.\n    '
    per: Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']
    '\n    Reach unit counted by the seller.\n    '
    window: Window
    '\n    Counting window for the cap.\n    '
SaveMediaBuySuccessMediaBuyPhase: TypeAlias = Literal['draft', 'pendingApproval', 'inputRequired', 'active', 'completed', 'canceled', 'failed', 'rejected']

class SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget1(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['cost_per']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget2(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['threshold_rate']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget3(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['per_ad_spend']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget4(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['maximize_value']
SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget: TypeAlias = SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget1 | SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget2 | SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget3 | SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget4
'\nA goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).\n'

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget1(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['cost_per']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget2(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['threshold_rate']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget3(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['per_ad_spend']
    value: float

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget4(TypedDict):
    """
    A goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).
    """
    kind: Literal['maximize_value']
SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget: TypeAlias = SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget1 | SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget2 | SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget3 | SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget4
'\nA goal target, judged by its kind: cost_per (a cost per unit, met at or under the value; per thousand for CPM pricing), threshold_rate (a minimum rate per impression, met at or above), per_ad_spend (a minimum return on ad spend, met at or above), or maximize_value (no number to meet).\n'

class InFlightReceipt(TypedDict):
    id: str
    state: Literal['claimed', 'running', 'uncertain']
    stateVersion: int
    stateChangedAt: str

class GetV3PublicDocumentRevisionSectionsInput(TypedDict):
    documentId: str
    revisionId: str
    section: NotRequired[str]
    query: NotRequired[str]
    cursor: NotRequired[str]
    '\n    Opaque continuation cursor. When resuming, resend the preceding response applicability.asOf value as asOf.\n    '
    asOf: NotRequired[str]
    '\n    Stable evaluation time. Required with cursor and must equal the preceding response applicability.asOf value.\n    '

class Owner(TypedDict):
    kind: Literal['scope3', 'organization', 'seller', 'third_party']
    id: NotRequired[str]
    displayName: str

class Identity(TypedDict):
    documentId: str
    stableKey: str
    kind: Literal['agreement', 'addendum', 'policy', 'schedule', 'guide', 'product_documentation', 'protocol_specification', 'reference']
    title: str
    owner: Owner
    visibility: Literal['public', 'organization_private', 'relationship_private', 'staff_private']
    maintenanceMode: Literal['published_revisions', 'maintained_current_with_revisions']

class Source(TypedDict):
    system: str
    sourceId: str
    sourceRevision: str
    canonicalCitationUrl: str
    retrievedAt: str

class Approval(TypedDict):
    state: str
    approvedAt: str | None
    approvedBy: str | None
    approvalRef: str | None
Authority = TypedDict('Authority', {'class': str, 'issuer': str, 'approvalRef': str | None})

class Revision2(TypedDict):
    revisionId: str
    documentId: str
    predecessorRevisionId: str | None
    label: str
    contentHash: str
    mediaType: str
    byteLength: int
    publishedAt: str | None
    effectiveFrom: str | None
    effectiveUntil: str | None
    source: Source
    approval: Approval
    authority: Authority

class Selection(TypedDict):
    kind: Literal['exact']
    revisionId: str

class Basis(TypedDict):
    kind: Literal['relevance_only']
    reasonCode: Literal['exact_revision_read']

class Applicability(TypedDict):
    disposition: Literal['reference']
    selectedAccountId: str
    asOf: str
    basis: Basis

class Section1(TypedDict):
    sectionId: str
    revisionId: str
    parentSectionId: str | None
    heading: str
    headingPath: list[str]
    ordinal: int
    canonicalCitationUrl: str
    contentHash: str
    byteLength: int

class Section(TypedDict):
    heading: str
    breadcrumb: list[str]
    content: str
    url: str
    section: Section1
    startByte: int
    endByteExclusive: int
    sectionComplete: bool

class LinkedDocument(TypedDict):
    label: str
    document: str
    url: str
    targetDocumentId: str | None
    targetRevisionId: str | None
    targetSectionId: str | None

class CrossReference(TypedDict):
    label: str
    targetDocumentId: str | None
    targetRevisionId: str | None
    targetSectionId: str | None
    canonicalCitationUrl: str
    includedInResponse: bool

class Completeness(TypedDict):
    status: Literal['complete', 'partial']
    returnedBytes: int
    returnedSectionCount: int
    omittedSectionCount: int
    reasonCodes: list[str]

class Coverage(TypedDict):
    source: str
    outcome: Literal['complete']

class Coverage1(TypedDict):
    source: str
    outcome: Literal['partial']
    reasonCode: Literal['response_bounded', 'selection_incomplete']
    retryable: bool

class Continuation(TypedDict):
    cursor: str
    action: Literal['continue_same_document_read']
    expiresAt: str

class FullDocument(TypedDict):
    available: Literal[True]
    authenticatedDownloadPath: str
    mediaType: str
    contentHash: str

class FullDocument1(TypedDict):
    available: Literal[False]

class GetV3PublicDocumentRevisionSectionsResult(TypedDict):
    source: Literal['docs', 'specs']
    document: str
    url: str
    query: str
    queryApplied: bool
    identity: Identity
    revision: Revision2
    selection: Selection
    applicability: Applicability
    sections: list[Section]
    linkedDocuments: list[LinkedDocument]
    crossReferences: list[CrossReference]
    completeness: Completeness
    coverage: list[Coverage | Coverage1]
    continuation: Continuation | None
    fullDocument: FullDocument | FullDocument1
    bounded: Literal[True]
    truncated: bool
    terminal: Literal[True]
    nextAction: Literal['answer_or_state_not_established']
    linkedDocumentAction: Literal['read_direct_link_once_if_needed']

class CoverageItem(TypedDict):
    source: str
    outcome: Literal['unavailable']
    reasonCode: str
    retryable: bool

class Details(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details

class GetV3PublicDocumentRevisionSectionsError1(TypedDict):
    data: None
    error: Error

class Details1(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error1(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details1

class GetV3PublicDocumentRevisionSectionsError2(TypedDict):
    data: None
    error: Error1

class Details2(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error2(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details2

class GetV3PublicDocumentRevisionSectionsError3(TypedDict):
    data: None
    error: Error2

class Details3(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error3(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details3

class GetV3PublicDocumentRevisionSectionsError4(TypedDict):
    data: None
    error: Error3

class Details4(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error4(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details4

class GetV3PublicDocumentRevisionSectionsError5(TypedDict):
    data: None
    error: Error4
GetV3PublicDocumentRevisionSectionsError: TypeAlias = GetV3PublicDocumentRevisionSectionsError1 | V3ToolErrorResponse | GetV3PublicDocumentRevisionSectionsError2 | GetV3PublicDocumentRevisionSectionsError3 | GetV3PublicDocumentRevisionSectionsError4 | GetV3PublicDocumentRevisionSectionsError5

class DownloadV3PublicDocumentRevisionInput(TypedDict):
    documentId: str
    revisionId: str
DownloadV3PublicDocumentRevisionResult: TypeAlias = bytes

class Details5(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error5(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details5

class DownloadV3PublicDocumentRevisionError1(TypedDict):
    data: None
    error: Error5

class Details6(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error6(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details6

class DownloadV3PublicDocumentRevisionError2(TypedDict):
    data: None
    error: Error6

class Details7(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error7(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details7

class DownloadV3PublicDocumentRevisionError3(TypedDict):
    data: None
    error: Error7

class Details8(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error8(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details8

class DownloadV3PublicDocumentRevisionError4(TypedDict):
    data: None
    error: Error8

class Details9(TypedDict):
    retryable: bool
    correlationId: str
    coverage: list[CoverageItem]

class Error9(TypedDict):
    code: Literal['DOCUMENT_REFERENCE_INVALID', 'DOCUMENT_NOT_FOUND', 'DOCUMENT_CURSOR_STALE', 'DOCUMENT_DEPENDENCY_UNAVAILABLE', 'DOCUMENT_INTERNAL_ERROR']
    message: str
    details: Details9

class DownloadV3PublicDocumentRevisionError5(TypedDict):
    data: None
    error: Error9
DownloadV3PublicDocumentRevisionError: TypeAlias = DownloadV3PublicDocumentRevisionError1 | V3ToolErrorResponse | DownloadV3PublicDocumentRevisionError2 | DownloadV3PublicDocumentRevisionError3 | DownloadV3PublicDocumentRevisionError4 | DownloadV3PublicDocumentRevisionError5

class GetStatusInput(TypedDict):
    pass

class Account2(TypedDict):
    accountId: float
    company: str
    kind: Literal['buyer', 'seller', 'org'] | None

class ReadyDestination(TypedDict):
    sellerId: str
    name: str

class Destinations(TypedDict):
    total: float
    ready: float
    needsConnection: float
    blocked: float
    readyDestinations: list[ReadyDestination]
    readyDestinationsTruncated: bool

class OperatorUnit(TypedDict):
    id: str
    name: str

class DomainProof(TypedDict):
    verified: bool | None
    source: Literal['member_or_admin', 'aao_oauth'] | None
    confirmedAt: str | None

class Organization(TypedDict):
    domain: str | None
    relationship: Literal['same_organization', 'portfolio_brand', 'external_operator', 'unresolved']
    verificationSource: Literal['member_or_admin', 'organization_domain', 'aao_house', 'none']

class Aao(TypedDict):
    status: Literal['matched', 'not_found', 'unavailable', 'not_checked']
    canonicalDomain: str | None
    name: str | None
    source: str | None

class OperatorIdentity(TypedDict):
    canManage: bool
    operatorDomain: NotRequired[str | None]
    operatorDomainSource: NotRequired[str | None]
    operatorScope: NotRequired[str | None]
    operatorUnit: NotRequired[OperatorUnit | None]
    domainProof: NotRequired[DomainProof]
    organization: NotRequired[Organization]
    aao: NotRequired[Aao]
    scopeStatus: str
    locked: bool
    lockedAt: NotRequired[str | None]
    lockReason: NotRequired[str | None]
    hierarchyAccountCount: float
    reconciliation: NotRequired[JsonValue]
    claimedIdentities: list[JsonValue]
    usableForBuying: bool

class Source1(TypedDict):
    id: str
    name: str

class LibraryRequirement(TypedDict):
    id: Literal['merchandising_agent', 'guaranteed_inventory', 'catalogue']
    requirement: str
    status: Literal['met', 'missing']
    documentToAdd: NotRequired[str]
    source: NotRequired[Source1]

class Blocker1(TypedDict):
    id: str
    name: str
    status: str
    why: NotRequired[str]
    effect: NotRequired[str]
    fix: NotRequired[str]

class NextAction(TypedDict):
    id: str
    what: str
    why: NotRequired[str]
    priority: Literal['required', 'recommended']
    tool: NotRequired[str]
    page: NotRequired[str]
    arguments: NotRequired[dict[str, str]]
    url: NotRequired[str]

class ReachableAccount(TypedDict):
    customerId: float
    company: str
    kind: Literal['buyer', 'seller', 'org']

class GetStatusResult(TypedDict):
    account: Account2
    listedToolAccountKinds: list[Literal['buyer', 'seller', 'org']]
    state: str
    canTransact: NotRequired[bool]
    platformReady: NotRequired[bool]
    canBuyAnywhere: NotRequired[bool]
    destinations: NotRequired[Destinations]
    operatorIdentity: NotRequired[OperatorIdentity]
    phase: NotRequired[str]
    libraryRequirements: NotRequired[list[LibraryRequirement] | None]
    libraryRequirementsOmitted: NotRequired[int]
    libraryRequirementsDiagnostic: NotRequired[str]
    blockers: list[Blocker1]
    nextActions: list[NextAction]
    reachableAccounts: list[ReachableAccount]
    reachableAccountsTruncated: NotRequired[bool]
GetStatusError: TypeAlias = V3ToolErrorResponse

class RefreshInventorySourceHealthInput(TypedDict):
    sourceId: str
    '\n    Exact external sales-agent source. Managed and modular sources have dedicated diagnostics.\n    '

class Evidence(TypedDict):
    runId: str | None
    taskId: str | None
    operationId: str | None
    debugId: str | None
    correlationId: str | None

class Readiness(TypedDict):
    status: str
    canTransact: bool

class RefreshInventorySourceHealthResult(TypedDict):
    sourceId: str
    outcome: Literal['passed', 'empty', 'failed', 'not_reached']
    checkedAt: str
    operation: Literal['get_products']
    evidence: Evidence
    readiness: Readiness
RefreshInventorySourceHealthError: TypeAlias = V3ToolErrorResponse

class Settings(TypedDict):
    """
    Safe display settings only. Access, owners, lifecycle, and provisioning are not accepted.
    """
    company: NotRequired[str]
    '\n    Company label shown for this Account.\n    '

class SaveAccountInput(TypedDict):
    accountId: int
    '\n    Existing direct child Account id returned by search.\n    '
    name: NotRequired[str]
    '\n    Account name.\n    '
    settings: NotRequired[Settings]
    '\n    Safe display settings only. Access, owners, lifecycle, and provisioning are not accepted.\n    '

class Settings1(TypedDict):
    company: str

class Object(TypedDict):
    id: str
    name: str
    company: str
    accountType: Literal['buyer', 'seller']
    enabled: bool
    status: Literal['ACTIVE', 'ARCHIVED']
    archivedAt: str | None
    organizationId: str
    settings: Settings1

class SaveAccountResult(TypedDict):
    action: Literal['saved', 'unchanged']
    accessChanged: Literal[False]
    lifecycleChanged: Literal[False]
    object: Object
SaveAccountError: TypeAlias = V3ToolErrorResponse

class ReviewBuyerChildAccountInput(TypedDict):
    parentId: float | str
    '\n    Exact selected Organization parent Account id.\n    '
    name: str
    '\n    Name of the proposed Buyer child Account.\n    '

class Parent(TypedDict):
    id: ReviewBuyerChildAccountSuccessParentId
    name: str

class ProposedAccount(TypedDict):
    name: str
    role: Literal['BUYER']
    parentId: ReviewBuyerChildAccountSuccessProposedAccountParentId

class Operator(TypedDict):
    userId: ReviewBuyerChildAccountSuccessOperatorUserId
    email: str | None
    name: str | None

class Capacity(TypedDict):
    consumed: int
    remaining: int | None
    limit: int | None
    allowed: bool
    denialReasons: list[str]

class AccessChanges(TypedDict):
    parentAdministratorsInheritChildAccess: Literal[True]
    newMemberships: Literal[0]
    invitations: Literal[0]

class OtherChanges(TypedDict):
    featureFlags: Literal[0]
    mediaBuys: Literal[0]

class ReviewBuyerChildAccountResult(TypedDict):
    parent: Parent
    proposedAccount: ProposedAccount
    operator: Operator
    capacity: Capacity
    accessChanges: AccessChanges
    otherChanges: OtherChanges
    transactionReadiness: Literal['not_verified']
    canRequest: bool
    blockers: list[str]
ReviewBuyerChildAccountError: TypeAlias = V3ToolErrorResponse

class RequestBuyerChildAccountInput(TypedDict):
    parentId: float | str
    '\n    Exact selected Organization parent Account id.\n    '
    name: str
    '\n    Name of the proposed Buyer child Account.\n    '
    idempotencyKey: str
    '\n    Stable UUID for this creation. Repeat with the same key and name to get the outcome.\n    '

class RequestBuyerChildAccountResult(TypedDict):
    action: Literal['approval_required']
    message: str
    approval: RequestBuyerChildAccountSuccessAgentApproval
RequestBuyerChildAccountError: TypeAlias = V3ToolErrorResponse

class SaveAskInput1(TypedDict):
    id: str
    '\n    askId from a prior save_ask response.\n    '
    requesterState: Literal['confirmed_resolved', 'accepted', 'still_blocked', 'withdrawn']
    '\n    Requester state for an existing ask.\n    '
    note: NotRequired[str]
    '\n    Optional update context.\n    '

class SaveAskInput2(TypedDict):
    type: Literal['support']
    title: str
    '\n    What is needed or blocked.\n    '
    detail: str
    '\n    Context and expected outcome.\n    '
    blocks: NotRequired[str]
    '\n    Omit when unknown.\n    '
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    '\n    high = one customer blocked. urgent = outage, several customers, or data risk.\n    '

class SaveAskInput3(TypedDict):
    type: Literal['product']
    title: str
    '\n    What is needed or blocked.\n    '
    detail: NotRequired[str]
    '\n    Context and expected outcome.\n    '
    blocks: NotRequired[str]
    '\n    Omit when unknown.\n    '
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    '\n    high = one customer blocked. urgent = outage, several customers, or data risk.\n    '

class SaveAskInput4(TypedDict):
    type: Literal['commercial']
    title: str
    '\n    What is needed or blocked.\n    '
    detail: NotRequired[str]
    '\n    Context and expected outcome.\n    '
    blocks: NotRequired[str]
    '\n    Omit when unknown.\n    '
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    '\n    high = one customer blocked. urgent = outage, several customers, or data risk.\n    '

class SaveAskInput5(TypedDict):
    type: Literal['integration']
    title: str
    '\n    What is needed or blocked.\n    '
    detail: NotRequired[str]
    '\n    Context and expected outcome.\n    '
    blocks: NotRequired[str]
    '\n    Omit when unknown.\n    '
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    '\n    high = one customer blocked. urgent = outage, several customers, or data risk.\n    '
    subject: str
    '\n    Supply domain or integration vendor.\n    '

class SaveAskInput6(TypedDict):
    type: Literal['supply']
    title: str
    '\n    What is needed or blocked.\n    '
    detail: NotRequired[str]
    '\n    Context and expected outcome.\n    '
    blocks: NotRequired[str]
    '\n    Omit when unknown.\n    '
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    '\n    high = one customer blocked. urgent = outage, several customers, or data risk.\n    '
    subject: str
    '\n    Supply domain or integration vendor.\n    '
    channel: str
    '\n    Supply channel or integration channel name.\n    '
    desiredSupply: NotRequired[str]
    '\n    Supply only: inventory or outcome needed.\n    '

class SaveAskInput7(TypedDict):
    title: str
    '\n    What is needed or blocked.\n    '
    detail: NotRequired[str]
    '\n    Context and expected outcome.\n    '
    blocks: NotRequired[str]
    '\n    Omit when unknown.\n    '
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    '\n    high = one customer blocked. urgent = outage, several customers, or data risk.\n    '
    subject: NotRequired[str]
    '\n    Supply domain or integration vendor.\n    '
    desiredSupply: NotRequired[str]
    '\n    Supply only: inventory or outcome needed.\n    '

class SaveAskInput8(TypedDict):
    title: str
    '\n    What is needed or blocked.\n    '
    detail: NotRequired[str]
    '\n    Context and expected outcome.\n    '
    blocks: NotRequired[str]
    '\n    Omit when unknown.\n    '
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    '\n    high = one customer blocked. urgent = outage, several customers, or data risk.\n    '
    subject: str
    '\n    Supply domain or integration vendor.\n    '
    channel: str
    '\n    Supply channel or integration channel name.\n    '
    desiredSupply: NotRequired[str]
    '\n    Supply only: inventory or outcome needed.\n    '
SaveAskInput: TypeAlias = SaveAskInput1 | SaveAskInput2 | SaveAskInput3 | SaveAskInput4 | SaveAskInput5 | SaveAskInput6 | SaveAskInput7 | SaveAskInput8

class SaveAskResult1(TypedDict):
    askId: NotRequired[SaveAskSuccessAskId]
    type: Literal['support', 'commercial']
    filed: Literal[True]
    escalationUid: str

class SaveAskResult2(TypedDict):
    askId: NotRequired[SaveAskSuccessAskId]
    type: Literal['support', 'commercial']
    filed: Literal[False]
    warning: Literal['suppressed in test mode']

class SaveAskResult3(TypedDict):
    askId: NotRequired[SaveAskSuccessAskId]
    type: Literal['product']
    filed: bool
    created: bool
    state: str

class SaveAskResult4(TypedDict):
    askId: NotRequired[SaveAskSuccessAskId]
    type: Literal['supply']
    filed: Literal[True]
    created: bool
    registryStatus: Literal['found', 'missing', 'unavailable']

class SaveAskResult5(TypedDict):
    askId: NotRequired[SaveAskSuccessAskId]
    type: Literal['integration']
    filed: Literal[True]

class SaveAskResult6(TypedDict):
    askId: str
    type: Literal['support', 'product', 'supply', 'integration', 'commercial']
    filed: Literal[False]
    updated: Literal[True]
    requesterState: Literal['confirmed_resolved', 'accepted', 'still_blocked', 'withdrawn']

class SaveAskResult7(TypedDict):
    type: Literal['product', 'supply', 'integration']
    filed: Literal[False]
SaveAskResult: TypeAlias = SaveAskResult1 | SaveAskResult2 | SaveAskResult3 | SaveAskResult4 | SaveAskResult5 | SaveAskResult6 | SaveAskResult7
SaveAskError: TypeAlias = V3ToolErrorResponse

class Terms(TypedDict):
    accepted: Literal[True]
    '\n    Explicitly accept the named Terms version.\n    '
    version: str
    '\n    Terms version shown in Plan & Billing.\n    '

class SaveBillingInput1(TypedDict):
    terms: Terms

class PaymentAuthority(TypedDict):
    method: NotRequired[SaveBillingRequestPaymentAuthorityMethod]
    '\n    Hosted human card capture; the only method today.\n    '
    action: NotRequired[Literal['request']]
    '\n    Stage the payment-authority handoff.\n    '

class PaymentAuthority1(TypedDict):
    method: NotRequired[SaveBillingRequestPaymentAuthorityMethod]
    '\n    Hosted human card capture; the only method today.\n    '
    action: Literal['confirm']
    '\n    Confirm the payment-authority handoff.\n    '
    confirmationToken: str
    '\n    Token returned by the request stage.\n    '

class PaymentAuthority2(TypedDict):
    method: NotRequired[SaveBillingRequestPaymentAuthorityMethod]
    '\n    Hosted human card capture; the only method today.\n    '
    action: Literal['status']
    '\n    Poll the payment-authority handoff.\n    '

class SaveBillingInput2(TypedDict):
    paymentAuthority: PaymentAuthority | PaymentAuthority1 | PaymentAuthority2
SaveBillingInput: TypeAlias = SaveBillingInput1 | SaveBillingInput2

class Terms1(TypedDict):
    accepted: Literal[True]
    version: str

class SaveBillingResult1(TypedDict):
    action: Literal['terms_accepted']
    terms: Terms1

class Terms2(TypedDict):
    accepted: Literal[False]
    version: str
    governedByExistingContract: Literal[True]

class SaveBillingResult2(TypedDict):
    action: Literal['terms_not_required']
    terms: Terms2

class SaveBillingResult3(TypedDict):
    action: Literal['confirmation_required', 'human_action_required', 'payment_authority_pending', 'payment_authority_opened', 'payment_authority_verified', 'payment_authority_expired']
    paymentAuthority: SaveBillingSuccessPendingConfirmationResult | SaveBillingSuccessCaptureLinkIssuedResult
SaveBillingResult: TypeAlias = SaveBillingResult1 | SaveBillingResult2 | SaveBillingResult3
SaveBillingError: TypeAlias = V3ToolErrorResponse

class Scope(TypedDict):
    """
    What this subscription is about. Required on create; fixed after that.
    """
    kind: Literal['iu_allowance']
    '\n    The only scope kind ratified today.\n    '
    allowance: Literal['trial_free_grant', 'plan_included']
    '\n    trial_free_grant: signup credit. plan_included: recurring plan allowance.\n    '

class Content(TypedDict):
    """
    What kind of notice this is and how it renders. Required on create; fixed after that.
    """
    type: Literal['usage.allowance_threshold']
    '\n    "usage.allowance_threshold" is the only ratified content type (enum of one; additive to extend).\n    '
    presentation: Literal['alert']
    '\n    "alert" is the only ratified value; digest rendering ships with the scheduled-digest runtime.\n    '

class Trigger(TypedDict):
    """
    What fires this. Rejected today (no runtime yet). Required on create; patchable if editable.
    """
    type: Literal['schedule']
    '\n    Fires on a schedule. Not creatable/patchable here -- rejected; only managed subscriptions use it.\n    '
    schedule: str
    '\n    Cron-shaped schedule expression.\n    '
    timezone: str
    '\n    IANA timezone, explicit and required.\n    '

class Predicate(TypedDict):
    """
    The typed condition this trigger evaluates.
    """
    metric: Literal['iu.percent_consumed']
    '\n    "iu.percent_consumed" is the only ratified metric today (enum of one; additive to extend).\n    '
    op: Literal['>=']
    '\n    Upward comparator (enum of one): fires once at/above value; no prior state is stored.\n    '
    value: float
    '\n    Threshold percentage the metric is compared against; must be greater than 0 and at most 100.\n    '

class Trigger1(TypedDict):
    """
    What fires this. Rejected today (no runtime yet). Required on create; patchable if editable.
    """
    type: Literal['condition']
    '\n    Fires when predicate crosses, not on a schedule.\n    '
    predicate: Predicate
    '\n    The typed condition this trigger evaluates.\n    '

class SaveNotificationConfigInput(TypedDict):
    subscriptionId: NotRequired[str]
    '\n    Existing subscription to patch. Omit to create a new one.\n    '
    enabled: NotRequired[bool]
    '\n    Enable/disable. Create defaults true. Disabling a non-disableable subscription is rejected.\n    '
    scope: NotRequired[Scope]
    '\n    What this subscription is about. Required on create; fixed after that.\n    '
    content: NotRequired[Content]
    '\n    What kind of notice this is and how it renders. Required on create; fixed after that.\n    '
    trigger: NotRequired[Trigger | Trigger1]
    '\n    What fires this. Rejected today (no runtime yet). Required on create; patchable if editable.\n    '
    routeIds: NotRequired[list[Literal['email', 'slack', 'webhook']]]
    '\n    Delivery channels, at most once each; empty means framework-default routing. Patchable if editable.\n    '

class SaveNotificationConfigResult1(TypedDict):
    action: Literal['created', 'updated']
    subscriptionId: str
    config: dict[str, JsonValue]

class SaveNotificationConfigResult2(TypedDict):
    action: Literal['created', 'updated']
    subscriptionId: str
    config: None
    warning: Literal['created_but_readback_unavailable', 'updated_but_readback_unavailable']
    readback: Literal['unavailable']
SaveNotificationConfigResult: TypeAlias = SaveNotificationConfigResult1 | SaveNotificationConfigResult2
SaveNotificationConfigError: TypeAlias = V3ToolErrorResponse
AdvertiserId: TypeAlias = str

class SaveAdvertiserGrantInput(TypedDict):
    action: Literal['invite', 'accept', 'reject', 'revoke']
    '\n    invite creates a reviewed exact scope; invited org accepts/rejects; grantor revokes.\n    '
    grantRef: NotRequired[str]
    '\n    Required for accept, reject, or revoke.\n    '
    granteeOrganizationRef: NotRequired[str]
    '\n    Invite only: exact canonical Organization reference supplied by that organization.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    Invite only: exact canonical advertiser IDs. Future advertisers are never included.\n    '
    capabilities: NotRequired[list[Literal['advertiser.read', 'campaign.read', 'campaign.manage']]]
    '\n    Invite only: exact capabilities; advertiser.read required; campaign.manage needs campaign.read.\n    '
    expiresAt: NotRequired[str]
    '\n    Invite only: mandatory deadline no more than 365 days away.\n    '
    reason: str
    '\n    Durable purpose or lifecycle decision reason.\n    '

class Advertiser(TypedDict):
    advertiserId: str
    displayName: str

class Event(TypedDict):
    eventRef: str
    type: Literal['invited', 'accepted', 'rejected', 'revoked', 'expired']
    actor: Literal['grantor', 'grantee', 'system']
    reason: str
    observedAt: str

class Grant(TypedDict):
    grantRef: str
    grantor: SaveAdvertiserGrantSuccessGrantGrantor
    grantee: SaveAdvertiserGrantSuccessGrantGrantee
    advertisers: list[Advertiser]
    capabilities: list[Literal['advertiser.read', 'campaign.read', 'campaign.manage']]
    purpose: str
    status: Literal['invited', 'active', 'expired', 'rejected', 'revoked']
    invitedAt: str
    expiresAt: str
    events: NotRequired[list[Event]]

class SaveAdvertiserGrantResult(TypedDict):
    grant: Grant
SaveAdvertiserGrantError: TypeAlias = V3ToolErrorResponse
Id: TypeAlias = str
Tag: TypeAlias = str
Label: TypeAlias = str
BuyerAccountId: TypeAlias = str
ChannelItem: TypeAlias = str
VerticalItem: TypeAlias = str

class Filter(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: NotRequired[str]
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: NotRequired[str]
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput1(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['agent', 'skill', 'inventory_source', 'material', 'coverage', 'wholesale_product', 'playbook_version', 'business_rules_version', 'house_discount', 'connection', 'account_relationship', 'seller', 'advertiser', 'advertiser_grant', 'signal', 'work_item', 'campaign', 'creative_format', 'creative_engine', 'media_buy', 'rfp', 'rfp_turn', 'library_request', 'ask', 'conversation', 'buyer_agent', 'dimension', 'session']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: NotRequired[Filter]
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter1(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: str
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: NotRequired[str]
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput2(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['creative_asset', 'catalog']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: Filter1
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter2(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    advertiserId: str
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '

class SearchInput3(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['measurement_source', 'event_source']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: Filter2
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter3(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: NotRequired[str]
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: str
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput4(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['proposal']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: Filter3
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter4(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: str
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput5(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['creative']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: Filter4
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter5(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: str
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput6(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['creative']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: Filter5
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter6(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: str
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput7(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['creative_collection']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: Filter6
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter7(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: str
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput8(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['creative_collection']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: Filter7
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter8(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    campaignId: str
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '

class SearchInput9(TypedDict):
    query: NotRequired[JsonValue]
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['creative_session']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[JsonValue]
    filter: Filter8
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter9(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: NotRequired[str]
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: NotRequired[str]
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput10(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    kind: Literal['ad_server_targeting']
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: str
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: NotRequired[Filter9]
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter10(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: NotRequired[str]
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: NotRequired[str]
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput11(TypedDict):
    query: str
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: NotRequired[Filter10]
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter11(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: NotRequired[str]
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: NotRequired[str]
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput12(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: str
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: NotRequired[Filter11]
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter12(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: NotRequired[str]
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: NotRequired[str]
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput13(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: str
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: NotRequired[Filter12]
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '

class Filter13(TypedDict):
    """
    Creative requires exactly one owner scope.
    """
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    '\n    connection: target role; defaults to seller.\n    '
    ids: NotRequired[list[Id]]
    '\n    Buyer seller/connection: up to 50 exact IDs; reports missing IDs.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    '\n    inv_source: PENDING/ACTIVE/DISABLED. work_item: verdict/TASK. advertiser: ACTIVE/ARCHIVED/ALL.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    library_request: origin RFP turn.\n    '
    authorization: NotRequired[str]
    '\n    coverage: one authorization verdict, e.g. authorized.\n    '
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    Seller wholesale_product: one status; active = buyable.\n    '
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    '\n    ask: its routing type.\n    '
    askState: NotRequired[Literal['open', 'closed']]
    '\n    ask: open or closed/withdrawn.\n    '
    candidateType: NotRequired[str]
    '\n    ad_server_targeting: which taxonomy to browse.\n    '
    parentId: NotRequired[str]
    '\n    ad_server_targeting: descend into this parent candidate.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    work_item: one stream; modular_source covers source-side follow-ups.\n    '
    buyerDomain: NotRequired[str]
    '\n    house_discount: preview which rule keys to this domain.\n    '
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    '\n    campaign: Page status set. Archived is a visibility state; other values select unarchived campaigns.\n    '
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    '\n    campaign: managed campaigns are platform-authored; tracked campaigns mirror a provider account.\n    '
    campaignName: NotRequired[str]
    '\n    campaign: case-insensitive partial campaign-name match.\n    '
    advertiserId: NotRequired[str]
    '\n    measurement_source/event_source: required. creative*: one of this/campaignId. Others: owner filter.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    catalog: exact AdCP catalog type.\n    '
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    '\n    property_list: include or exclude lists only.\n    '
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    '\n    campaign/media_buy phase; active includes paused and cancel-pending buys; ending is output-only.\n    '
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    '\n    campaign: tracking=mirrors a provider account; managing=platform-authored.\n    '
    isPaused: NotRequired[bool]
    '\n    campaign/media_buy: narrows phase=active to paused (true) or running (false).\n    '
    isArchived: NotRequired[bool]
    '\n    campaign/media_buy: include (true) or exclude (false) archived rows.\n    '
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    '\n    Reserved; unused today. Results are in DB order.\n    '
    campaignId: NotRequired[str]
    '\n    campaign/proposal/creative*: exactly one of this or advertiserId.\n    '
    formatKind: NotRequired[str]
    '\n    creative/creative_format: format kind.\n    '
    productId: NotRequired[str]
    '\n    creative_format: required exact declaring product.\n    '
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    '\n    creative: match objects containing this media kind. creative_asset: use IMAGE, VIDEO, or AUDIO.\n    '
    tags: NotRequired[list[Tag]]
    '\n    creative_asset: require all listed tags.\n    '
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    '\n    advertiser/campaign/material/creative/creative_asset labels: AND keys, OR values.\n    '
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    '\n    dimension: only axes that label this kind.\n    '
    role: NotRequired[SearchRequestCreativeRole]
    '\n    creative: advertiser role; not seller Library.\n    '
    source: NotRequired[SearchRequestCreativeSource]
    '\n    creative: provenance.\n    '
    promoted: NotRequired[bool]
    '\n    creative: omit=all visible; true=promoted shelf; false=non-promoted.\n    '
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    '\n    proposal/rfp: filter lifecycle state.\n    '
    sellerId: NotRequired[str]
    '\n    proposal or creative_format: one seller.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    rfp/rfp_turn: quick/uploaded/inbound/manual.\n    '
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    '\n    rfp/rfp_turn: list; session: one live/draft/evaluation.\n    '
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    '\n    session: active, closed, or archived.\n    '
    live: NotRequired[bool]
    '\n    session: observed liveness only; unknown matches neither value.\n    '
    attention: NotRequired[Literal['approval_needed']]
    '\n    session: unresolved approval attention.\n    '
    operatorDomain: NotRequired[str]
    '\n    session: exact observed operator domain.\n    '
    actorKind: NotRequired[Literal['human', 'agent']]
    '\n    session: exact source-derived agent or human classification.\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    session: exact advertiser identities, never discovery text.\n    '
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    '\n    session: exact buyer account identities, never discovery text.\n    '
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    '\n    session: recorded transport.\n    '
    updatedAfter: NotRequired[str]
    '\n    session: updated strictly after this instant.\n    '
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    '\n    session: one retained native source; RFP and media-buy sources are structured-only.\n    '
    buyer: NotRequired[list[str]]
    '\n    rfp/rfp_turn: buyer dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    advertiser: NotRequired[list[str]]
    '\n    rfp/rfp_turn: advertiser dimension; session: exact RFP discovery metadata, not an account identity.\n    '
    category: NotRequired[list[str]]
    '\n    rfp/rfp_turn: category dimension.\n    '
    market: NotRequired[list[str]]
    '\n    rfp/rfp_turn/material: market dimension.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    rfp/rfp_turn/material: channel dimension; seller: channel filter.\n    '
    selectedPosture: NotRequired[list[str]]
    '\n    rfp/rfp_turn: selected posture.\n    '
    playbookVersion: NotRequired[list[int]]
    '\n    rfp/rfp_turn: receipt playbook version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    rfp/rfp_turn: compose cache mode.\n    '
    outcome: NotRequired[list[str]]
    '\n    rfp/rfp_turn: recorded outcome result.\n    '
    rfpId: NotRequired[str]
    '\n    rfp_turn: parent RFP id.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    rfp_turn: queued/processing/terminal response state.\n    '
    evaluationState: NotRequired[list[str]]
    '\n    rfp_turn: evaluation state.\n    '
    responseRecipeVersion: NotRequired[list[str]]
    '\n    rfp_turn: response recipe version.\n    '
    modelVersion: NotRequired[list[str]]
    '\n    rfp_turn: composer model version.\n    '
    judgeVersion: NotRequired[list[str]]
    '\n    rfp_turn: judge/truth-gate version.\n    '
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    '\n    rfp_turn: whether feedback exists.\n    '
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    '\n    seller media_buy: seller lifecycle state.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    seller media_buy: one buyer.\n    '
    accountId: NotRequired[int]
    '\n    member: account whose roster to read; an org may select one direct child.\n    '
    sandbox: NotRequired[bool]
    '\n    advertiser: true=sandbox; false=live own-supply (Seller needs amc-campaign-management). Buyer: both.\n    '
    linkedAccountPartnerId: NotRequired[str]
    "\n    advertiser: linked through this sales agent by the sales agent record's agent_id; not a seller id.\n    "
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    '\n    advertiser_grant: filter invitation and terminal lifecycle states.\n    '
    flightStartFrom: NotRequired[str]
    '\n    seller media_buy: flight starts at/after this ISO instant.\n    '
    flightStartTo: NotRequired[str]
    '\n    seller media_buy: flight starts at/before this ISO instant.\n    '
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    '\n    seller: market-maker tier or marketplace_seller.\n    '
    marketplaceReady: NotRequired[bool]
    '\n    seller: true=marketplace-ready; false=not.\n    '
    marketplace: NotRequired[bool]
    '\n    seller: true=all marketplace sellers incl. unconnected; false/absent=connected only.\n    '
    region: NotRequired[str]
    '\n    seller: region code filter.\n    '
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    '\n    state.\n    '
    materialKind: NotRequired[Literal['document', 'response']]
    '\n    response: paired or historical; otherwise document.\n    '
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    '\n    source.\n    '
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    '\n    visibility.\n    '
    sourceExtension: NotRequired[str]
    '\n    source ext; not formats.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    '\n    material: Library document category; uncategorized includes documents without a category.\n    '
    vertical: NotRequired[list[VerticalItem]]
    '\n    Vertical.\n    '
    effectiveOn: NotRequired[str]
    '\n    effective.\n    '
    expiresAfter: NotRequired[str]
    '\n    unexpired.\n    '
    hasUnits: NotRequired[bool]
    '\n    material browse: true=has pages/slides\n    '
    archived: NotRequired[Literal['active', 'archived']]
    '\n    material: active (default) or archived Library documents.\n    '
    conversationStartedAfter: NotRequired[str]
    '\n    conversation: created at/after this time.\n    '
    conversationStartedBefore: NotRequired[str]
    '\n    conversation: created at/before this time.\n    '

class SearchInput14(TypedDict):
    query: NotRequired[str]
    '\n    Term/docs question; omit only for kind lists. conversation: max 200 chars.\n    '
    document: NotRequired[str]
    '\n    Prior-hit doc; immutable needs revision; docs/specs only.\n    '
    revision: NotRequired[str]
    '\n    Exact immutable public-document revision; needs document.\n    '
    section: NotRequired[str]
    '\n    Exact section in document revision; needs both IDs.\n    '
    asOf: NotRequired[str]
    '\n    Exact document evaluation time; preserve for continuation.\n    '
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    '\n    Omit for all. Exact docs use docs/specs, not objects.\n    '
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    '\n    Default caller_relevant; public_research is broader. Exact reads ignore relevance.\n    '
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    scope: NotRequired[Literal['unit']]
    '\n    Material scope: unit.\n    '
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    '\n    Evidence/browse\n    '
    sourceId: NotRequired[str]
    '\n    Source scope (not filter.sourceId); required for ad_server_targeting.\n    '
    filter: NotRequired[Filter13]
    '\n    Creative requires exactly one owner scope.\n    '
    cursor: NotRequired[str]
    '\n    Prior response pagination token.\n    '
    limit: NotRequired[int]
    '\n    Max results; default 50, skill max 5.\n    '
SearchInput: TypeAlias = SearchInput1 | SearchInput2 | SearchInput3 | SearchInput4 | SearchInput5 | SearchInput6 | SearchInput7 | SearchInput8 | SearchInput9 | SearchInput10 | SearchInput11 | SearchInput12 | SearchInput13 | SearchInput14

class Result(TypedDict):
    advertiserId: NotRequired[str]
    name: NotRequired[str | None]
    sandbox: NotRequired[bool]

class Objects(TypedDict):
    kind: Literal['account', 'member', 'agent', 'skill', 'inventory_source', 'material', 'coverage', 'wholesale_product', 'playbook_version', 'business_rules_version', 'house_discount', 'connection', 'account_relationship', 'seller', 'advertiser', 'advertiser_grant', 'signal', 'ad_server_targeting', 'work_item', 'campaign', 'catalog', 'measurement_source', 'event_source', 'property_list', 'creative', 'creative_format', 'creative_asset', 'creative_engine', 'creative_session', 'creative_collection', 'media_buy', 'proposal', 'rfp', 'rfp_turn', 'library_request', 'ask', 'conversation', 'buyer_agent', 'dimension', 'session']
    total: NotRequired[float]
    totalLowerBound: NotRequired[float]
    returned: NotRequired[float]
    hasMore: NotRequired[bool]
    truncated: NotRequired[bool]
    nextCursor: NotRequired[str]
    results: list[Result]

class SearchResult(TypedDict):
    sources: list[Literal['objects', 'docs', 'specs']]
    objects: NotRequired[Objects]
    objectsUnavailable: NotRequired[str]
    knowledge: NotRequired[list[JsonValue]]
    knowledgeRelevance: NotRequired[JsonValue]
    knowledgeDocuments: NotRequired[list[JsonValue]]
    knowledgeUnavailable: NotRequired[str]
    knowledgeDocumentNotFound: NotRequired[str]
    knowledgeNextAction: NotRequired[JsonValue]
    knowledgeNoMatch: NotRequired[JsonValue]
SearchError: TypeAlias = V3ToolErrorResponse
Gtin: TypeAlias = str

class Filter14(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter14]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Pages(TypedDict):
    """
    Pages.
    """
    candidates: NotRequired[GetRequestOptionsPagesCandidates]
    '\n    Candidates.\n    '
    rendition_blocks: NotRequired[GetRequestOptionsPagesRenditionBlocks]
    '\n    Blocks.\n    '
    visual_assets: NotRequired[GetRequestOptionsPagesVisualAssets]
    '\n    Assets.\n    '
    extraction_diagnostics: NotRequired[GetRequestOptionsPagesExtractionDiagnostics]
    '\n    Diagnostics.\n    '
    composition_receipts: NotRequired[GetRequestOptionsPagesCompositionReceipts]
    '\n    Receipts.\n    '
    usage: NotRequired[GetRequestOptionsPagesUsage]
    '\n    App-only usage.\n    '

class Select(TypedDict):
    """
    Material selectors.
    """
    blockKinds: NotRequired[list[Literal['heading', 'paragraph', 'list', 'table', 'caption', 'speaker_notes', 'ocr', 'accessibility_text', 'other']]]
    '\n    Semantic block kinds.\n    '
    unitId: NotRequired[str]
    '\n    One page, slide, or sheet.\n    '
    assetKinds: NotRequired[list[Literal['photo', 'illustration', 'logo', 'chart', 'diagram', 'screenshot', 'background', 'other']]]
    '\n    Visual asset kinds.\n    '
    reusePolicies: NotRequired[list[Literal['allowed', 'requires_approval', 'prohibited', 'unknown']]]
    '\n    Asset reuse policies.\n    '
    assetStatuses: NotRequired[list[Literal['ready', 'degraded', 'failed']]]
    '\n    Asset extraction states.\n    '

class Options(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class ConnectionTarget(TypedDict):
    """
    connection only: expected immutable service target; rejects a grant for another service.
    """
    kind: Literal['seller', 'creative_engine']
    '\n    Service role.\n    '
    id: str
    '\n    Service ID.\n    '

class GetInput1(TypedDict):
    kind: Literal['agent', 'buyer_agent', 'skill', 'inventory_source', 'advertiser', 'advertiser_grant', 'signal', 'ask', 'conversation', 'campaign', 'dimension', 'creative_asset', 'media_buy', 'rfp', 'rfp_turn', 'library_request', 'account_relationship']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter15(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items1(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter15]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options1(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput2(TypedDict):
    kind: Literal['seller']
    id: NotRequired[str]
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items1]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options1]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter16(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items2(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter16]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options2(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput3(TypedDict):
    kind: Literal['listing', 'media_kit', 'playbook', 'business_rules', 'coverage', 'distribution', 'notification_config']
    id: NotRequired[JsonValue]
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items2]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options2]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter17(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items3(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter17]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options3(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput4(TypedDict):
    kind: Literal['audience']
    id: NotRequired[JsonValue]
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: str
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items3]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options3]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter18(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items4(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter18]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options4(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput5(TypedDict):
    kind: Literal['catalog', 'measurement_source', 'event_source']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: str
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items4]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options4]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter19(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items5(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter19]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options5(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput6(TypedDict):
    kind: Literal['creative_format']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: str
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[JsonValue]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[JsonValue]
    items: NotRequired[Items5]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options5]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter20(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items6(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter20]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options6(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput7(TypedDict):
    kind: Literal['creative', 'creative_collection']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[JsonValue]
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: str
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items6]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options6]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter21(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items7(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter21]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options7(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput8(TypedDict):
    kind: Literal['creative', 'creative_collection']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: str
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[JsonValue]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items7]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options7]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter22(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items8(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter22]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options8(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput9(TypedDict):
    kind: Literal['creative_engine']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[JsonValue]
    items: NotRequired[Items8]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options8]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter23(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items9(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter23]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options9(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput10(TypedDict):
    kind: Literal['creative_session']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: str
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[JsonValue]
    items: NotRequired[Items9]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options9]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter24(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items10(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter24]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options10(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput11(TypedDict):
    kind: Literal['wholesale_product']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: str
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items10]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options10]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter25(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items11(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter25]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options11(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput12(TypedDict):
    kind: Literal['material']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items11]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options11]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter26(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items12(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter26]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options12(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput13(TypedDict):
    kind: Literal['proposal']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items12]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options12]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter27(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items13(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter27]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options13(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput14(TypedDict):
    kind: Literal['connection']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items13]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options13]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter28(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items14(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter28]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options14(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput15(TypedDict):
    kind: Literal['session']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items14]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options14]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '

class Filter29(TypedDict):
    """
    Exact item filters.
    """
    ids: NotRequired[list[Id]]
    '\n    Exact item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Exact product GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Matching item tags.\n    '
    category: NotRequired[str]
    '\n    Exact item category.\n    '
    query: NotRequired[str]
    '\n    Text contained in an item.\n    '
    status: NotRequired[Literal['approved']]
    '\n    Item review status.\n    '

class Items15(TypedDict):
    """
    Catalog items: exact filters and prior cursor.
    """
    filter: NotRequired[Filter29]
    '\n    Exact item filters.\n    '
    cursor: NotRequired[str]
    '\n    Cursor from the prior item page.\n    '

class Options15(TypedDict):
    """
    Material only: exact revisions, pages, and selectors.
    """
    sourceRevision: NotRequired[int]
    '\n    Exact revision.\n    '
    renditionRevision: NotRequired[int]
    '\n    Revision; active if omitted.\n    '
    pages: NotRequired[Pages]
    '\n    Pages.\n    '
    select: NotRequired[Select]
    '\n    Material selectors.\n    '

class GetInput16(TypedDict):
    kind: Literal['work_item']
    id: str
    '\n    Skill: exact user-supplied or search ID. Others search. Work item: filter.workItemKind; never guess.\n    '
    after: NotRequired[str]
    '\n    session: opaque cursor returned by the preceding Session read.\n    '
    through: NotRequired[str]
    '\n    session: preserve the preceding snapshotThrough with a page cursor.\n    '
    limit: NotRequired[int]
    '\n    session: retained event page size.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Seller media_buy only: buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    accountId: NotRequired[int]
    '\n    member only: direct child account; omit for the selected account.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID for products, measurement sources, collections, or creatives.\n    '
    reportId: NotRequired[str]
    '\n    property_list report include: AAO report ID from save_property_list check.\n    '
    identifierOffset: NotRequired[int]
    '\n    property_list only: offset for one bounded identifier page from get.\n    '
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    '\n    property_list only: identifier set to page; default is all identifiers.\n    '
    productQueryId: NotRequired[str]
    '\n    Seller product polling: execution ID from prior read.\n    '
    productRevision: NotRequired[int]
    '\n    Seller product polling: revision from prior read.\n    '
    validationRunId: NotRequired[str]
    '\n    Agent only: exact validation run ID from validationRuns.\n    '
    sourceId: NotRequired[str]
    '\n    Required: wholesale_product/modular work_item source; creative_session campaign. Signal: ad-server.\n    '
    workItemKind: Literal['creative_review', 'media_buy_approval', 'modular_source']
    '\n    Which work-item stream owns it; modular_source also needs sourceId.\n    '
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    '\n    diagnostics; ESA conn/status/sync/sandbox; modular; versions; discounts; mappingWorkspace deprecated\n    '
    items: NotRequired[Items15]
    '\n    Catalog items: exact filters and prior cursor.\n    '
    options: NotRequired[Options15]
    '\n    Material only: exact revisions, pages, and selectors.\n    '
    version: NotRequired[int]
    '\n    For playbook: read one past version, content included, to re-save it.\n    '
    subscriptionsOffset: NotRequired[int]
    '\n    notification_config only: page offset into subscriptions, newest first.\n    '
    connectionAccountsOffset: NotRequired[int]
    '\n    connection only: page offset into discovered provider accounts.\n    '
    connectionMappingsOffset: NotRequired[int]
    '\n    connection only: page offset into advertiser account-mapping rows.\n    '
    connectionTarget: NotRequired[ConnectionTarget]
    '\n    connection only: expected immutable service target; rejects a grant for another service.\n    '
    feedbackOffset: NotRequired[int]
    '\n    rfp_turn only: page offset into durable feedback.\n    '
    representationOffset: NotRequired[int]
    '\n    rfp_turn representation offset.\n    '
    representationCursor: NotRequired[str]
    '\n    rfp_turn only: opaque snapshot-stable representation continuation.\n    '
    audienceOffset: NotRequired[int]
    '\n    audience only: page offset into audience listing (default 0, page size 50).\n    '
    proposalProductsCursor: NotRequired[str]
    '\n    proposal only: opaque products text continuation.\n    '
GetInput: TypeAlias = GetInput1 | GetInput2 | GetInput3 | GetInput4 | GetInput5 | GetInput6 | GetInput7 | GetInput8 | GetInput9 | GetInput10 | GetInput11 | GetInput12 | GetInput13 | GetInput14 | GetInput15 | GetInput16

class Organization1(TypedDict):
    customerId: int
    name: str

class Terms3(TypedDict):
    requiredVersion: str
    url: str
    acceptedVersion: str | None
    acceptedAt: str | None
    currentVersionAccepted: bool
    acceptanceRequired: bool
    governedByExistingContract: bool
    canAccept: bool

class Capture(TypedDict):
    status: Literal['pending', 'opened', 'verified', 'expired']
    '\n    `pending`: issued, not yet opened. `opened`: the hosted page exchanged the token at least once. `verified`: the card-rail webhook confirmed a payment method for this link. `expired`: the TTL elapsed before verification — terminal, never re-armed.\n    '
    expiresAt: str

class Submission(TypedDict):
    status: Literal['processing', 'verified', 'failed', 'expired']
    '\n    Durable card-confirmation state. Only `verified` produces a usable payment authority; `processing`, `failed`, and `expired` are inert.\n    '
    submittedAt: str
    completedAt: str | None
    failureReason: Literal['verification_failed', 'canceled', 'expired'] | None

class SecureHandoff(TypedDict):
    available: Literal[False]
    reason: Literal['secure_handoff_unavailable', 'card_collection_not_enabled']

class PaymentAuthority3(TypedDict):
    verified: bool
    capture: Capture | None
    submission: Submission | None
    secureHandoff: SecureHandoff

class NextAction1(TypedDict):
    type: Literal['ACCEPT_TOS', 'ACCEPT_GOVERNING_AGREEMENT', 'SELECT_IU_PLAN', 'CONTACT_SCOPE3', 'ADD_BILLING_INFO', 'ADD_PAYMENT_METHOD', 'FUND_PREPAY', 'APPLY_FOR_CREDIT', 'RESOLVE_HOLD', 'UPDATE_PAYMENT_METHOD', 'NONE']
    message: str
    '\n    Human sentence describing the action, for direct display.\n    '
    docsUrl: str | None
    '\n    mintlify/v2 page explaining this action, when one exists.\n    '
    canCompleteInChat: bool

class Object1(TypedDict):
    organization: Organization1
    terms: Terms3
    paymentAuthority: PaymentAuthority3
    nextAction: NextAction1

class GetResult1(TypedDict):
    kind: Literal['billing']
    object: Object1

class Object2(TypedDict):
    advertiserId: NotRequired[str]
    sandbox: NotRequired[bool]
    targetingOverlay: NotRequired[dict[str, JsonValue]]
    '\n    AdCP TargetingOverlay (campaign subset); same shape as the save_campaign targetingOverlay input.\n    '

class GetResult2(TypedDict):
    kind: Literal['account', 'member', 'agent', 'buyer_agent', 'skill', 'inventory_source', 'material', 'wholesale_product', 'advertiser', 'advertiser_grant', 'signal', 'work_item', 'ask', 'conversation', 'session', 'seller', 'listing', 'media_kit', 'playbook', 'business_rules', 'coverage', 'distribution', 'connection', 'creative_engine', 'creative_session', 'campaign', 'catalog', 'measurement_source', 'event_source', 'dimension', 'property_list', 'creative', 'creative_format', 'creative_asset', 'creative_collection', 'media_buy', 'proposal', 'audience', 'rfp', 'rfp_turn', 'library_request', 'account_relationship', 'notification_config']
    object: Object2
    sourceId: NotRequired[str]
    productQueryId: NotRequired[str]
    products: NotRequired[list[JsonValue]]
    catalog: NotRequired[JsonValue]
    accounts: NotRequired[list[JsonValue]]
    accountsTotal: NotRequired[float]
    unavailableIncludes: NotRequired[list[JsonValue]]
    messages: NotRequired[list[JsonValue]]
    truncated: NotRequired[bool]
GetResult: TypeAlias = GetResult1 | GetResult2
GetError: TypeAlias = V3ToolErrorResponse

class Target3(TypedDict):
    """
    Service to authorize. Existing connections cannot change target.
    """
    kind: Literal['seller', 'creative_engine']
    '\n    Service role.\n    '
    id: str
    '\n    Service ID.\n    '

class Authorization(TypedDict):
    """
    Authorize target, sellerId, or an existing connectionId.
    """
    mode: NotRequired[Literal['oauth', 'bearer']]
    '\n    Authorization mode.\n    '

class Selection1(TypedDict):
    """
    Seller selection; requires seller target or sellerId.
    """
    decision: SaveConnectionRequestBuyerStorefrontSelectionDecision
    '\n    Account decision.\n    '

class AdvertiserActivation(TypedDict):
    """
    Seller advertiser activation (limited rollout); requires seller target or sellerId.
    """
    advertiserId: SaveConnectionRequestAdvertiserActivationAdvertiserId
    '\n    Advertiser ID.\n    '
    decision: SaveConnectionRequestBuyerAdvertiserStorefrontActivationPreferenceDecision
    '\n    DEFAULT inherits account selection.\n    '

class Billing(TypedDict):
    """
    Seller billing; requires seller target or sellerId.
    """
    requestedParty: Literal['agent', 'operator']
    '\n    Billing party.\n    '

class Billing1(TypedDict):
    """
    Seller billing; requires seller target or sellerId.
    """
    directBillingAccepted: Literal[True]
    '\n    Accept direct billing.\n    '

class FeaturePolicy(TypedDict):
    """
    Seller buy/events/feeds policy; requires seller target or sellerId.
    """
    buyEnabled: NotRequired[bool]
    '\n    Whether this buyer account should buy through this integration.\n    '
    eventsEnabled: NotRequired[bool]
    '\n    Whether this integration should receive buyer event/CAPI signals.\n    '
    feedsEnabled: NotRequired[bool]
    '\n    Whether buyer audience and feed data should be shared with this integration.\n    '

class EnhancedReporting(TypedDict):
    """
    Set Enhanced Reporting for one account; requires connectionId.
    """
    accountId: SaveConnectionRequestEnhancedReportingAccountId
    '\n    Exact active connected account ID.\n    '
    enabled: bool
    '\n    Desired Enhanced Reporting state.\n    '

class AdvertiserMapping(TypedDict):
    """
    Map or unmap an advertiser; requires connectionId.
    """
    accountId: NotRequired[SaveConnectionRequestAdvertiserMappingAccountId]
    "\n    accounts[].id from get(kind:'connection').\n    "
    advertiserId: SaveConnectionRequestAdvertiserMappingAdvertiserId
    '\n    Advertiser ID.\n    '
    state: Literal['mapped', 'unmapped']
    '\n    Mapping state.\n    '
    sourceId: NotRequired[str]
    '\n    Source ID hint.\n    '
    linkId: NotRequired[SaveConnectionRequestAdvertiserMappingLinkId]
    '\n    Mapping link ID.\n    '

class SaveConnectionInput(TypedDict):
    target: NotRequired[Target3]
    '\n    Service to authorize. Existing connections cannot change target.\n    '
    sellerId: NotRequired[str]
    '\n    Seller ID.\n    '
    connectionId: NotRequired[str]
    '\n    Connection ID.\n    '
    authorization: NotRequired[Authorization]
    '\n    Authorize target, sellerId, or an existing connectionId.\n    '
    selection: NotRequired[Selection1]
    '\n    Seller selection; requires seller target or sellerId.\n    '
    advertiserActivation: NotRequired[AdvertiserActivation]
    '\n    Seller advertiser activation (limited rollout); requires seller target or sellerId.\n    '
    billing: NotRequired[Billing | Billing1]
    '\n    Seller billing; requires seller target or sellerId.\n    '
    featurePolicy: NotRequired[FeaturePolicy]
    '\n    Seller buy/events/feeds policy; requires seller target or sellerId.\n    '
    enhancedReporting: NotRequired[EnhancedReporting]
    '\n    Set Enhanced Reporting for one account; requires connectionId.\n    '
    refreshAccounts: NotRequired[Literal[True]]
    '\n    Refresh provider accounts; requires connectionId.\n    '
    selectedAccountId: NotRequired[str]
    '\n    Select a provider account; requires connectionId.\n    '
    advertiserMapping: NotRequired[AdvertiserMapping]
    '\n    Map or unmap an advertiser; requires connectionId.\n    '
    state: NotRequired[Literal['removed']]
    '\n    Remove the connection; requires connectionId.\n    '

class Authorization1(TypedDict):
    url: str
    mode: Literal['oauth', 'bearer']
    connectionId: str | None

class SaveConnectionResult1(TypedDict):
    action: Literal['authorization_required']
    object: SaveConnectionSuccessObject
    mutationReceipt: NotRequired[SaveConnectionSuccessMutationReceipt]
    authorization: Authorization1

class SaveConnectionResult2(TypedDict):
    action: Literal['selection_updated', 'advertiser_activation_updated', 'billing_updated', 'direct_billing_accepted', 'feature_policy_updated', 'enhanced_reporting_updated', 'accounts_refreshed', 'account_selected', 'advertiser_mapped', 'advertiser_unmapped', 'removed']
    object: SaveConnectionSuccessObject
    mutationReceipt: NotRequired[SaveConnectionSuccessMutationReceipt]
SaveConnectionResult: TypeAlias = SaveConnectionResult1 | SaveConnectionResult2
SaveConnectionError: TypeAlias = V3ToolErrorResponse

class SaveLibraryRequestInput1(TypedDict):
    action: Literal['open']
    '\n    Open a library request.\n    '
    gap: str
    '\n    The exact missing seller-library content.\n    '
    originRfpTurnId: NotRequired[str]
    '\n    Optional RFP turn that identified this gap.\n    '

class SaveLibraryRequestInput2(TypedDict):
    action: Literal['close']
    '\n    Close a library request.\n    '
    id: str
    '\n    Library request id.\n    '
    closedBy: Literal['upload', 'dictation']
    '\n    How the closing Material was supplied.\n    '
    materialId: str
    '\n    Seller Material that closes the gap.\n    '
SaveLibraryRequestInput: TypeAlias = SaveLibraryRequestInput1 | SaveLibraryRequestInput2

class Request(TypedDict):
    id: SaveLibraryRequestSuccessRequestId
    gap: SaveLibraryRequestSuccessRequestGap
    openedAt: SaveLibraryRequestSuccessRequestOpenedAt
    originRfpTurnId: SaveLibraryRequestSuccessRequestOriginRfpTurnId
    status: Literal['open']
    closedBy: None
    closingMaterialId: None
    closedAt: None

class SaveLibraryRequestResult1(TypedDict):
    request: Request
    idempotent: bool

class SaveLibraryRequestResult2(TypedDict):
    id: SaveLibraryRequestSuccessId
    gap: SaveLibraryRequestSuccessGap
    openedAt: SaveLibraryRequestSuccessOpenedAt
    originRfpTurnId: SaveLibraryRequestSuccessOriginRfpTurnId
    status: Literal['closed']
    closedBy: Literal['upload', 'dictation']
    closingMaterialId: str
    closedAt: str
SaveLibraryRequestResult: TypeAlias = SaveLibraryRequestResult1 | SaveLibraryRequestResult2
SaveLibraryRequestError: TypeAlias = V3ToolErrorResponse

class OpenPageInput(TypedDict):
    relationshipId: NotRequired[str]
    '\n    Relationship to focus on.\n    '
    blockedReason: NotRequired[str]
    '\n    Its known blocked reason.\n    '
    page: Literal['connect_ad_server', 'ad_server_source', 'ad_server_diagnostics', 'source_diagnostics', 'seller_setup', 'demo_seller', 'modular_inventory_source', 'modular_source_setup', 'modular_inventory_feed', 'listing', 'discovery_card', 'media_kit', 'business_profile', 'playbook', 'library', 'product_marketing', 'business_rules', 'buyer_account_mapping', 'property_roster', 'plan_and_billing', 'sellers', 'creative_engines', 'advertisers', 'campaigns', 'campaign_receipt', 'approvals', 'release_notes', 'customer_requests', 'notifications']
    '\n    Page to open. source_diagnostics repairs a missing Agent relationship.\n    '
    sourceId: NotRequired[str]
    '\n    Focus diagnostics, modular source, or modular feed pages on an inventory source returned by search.\n    '
    sourceName: NotRequired[str]
    '\n    Optional source display name to seed modular_inventory_feed while it loads.\n    '
    esaId: NotRequired[str]
    '\n    Optional page focus. Use the real managedSa.connectionId from get or search.\n    '

class OpenPageResult(TypedDict):
    success: NotRequired[Literal[True]]
    code: NotRequired[JsonValue]
OpenPageError: TypeAlias = V3ToolErrorResponse

class OpenProposalPassInput(TypedDict):
    rfpId: str
    '\n    Canonical RFP id returned by save_rfp or get.\n    '
    turnId: str
    '\n    Canonical immutable turn id returned by save_rfp or get.\n    '

class Params(TypedDict):
    rfpId: str
    '\n    Canonical RFP id returned by save_rfp or get.\n    '
    turnId: str
    '\n    Canonical immutable turn id returned by save_rfp or get.\n    '

class OpenProposalPassResult(TypedDict):
    params: Params
OpenProposalPassError: TypeAlias = V3ToolErrorResponse

class OpenMediaBuysPageInput(TypedDict):
    accountRelationshipId: NotRequired[str]
    '\n    Seller-owned account relationship to focus.\n    '
    view: NotRequired[Literal['media_buys', 'creatives', 'delivery']]
    '\n    Optional relationship view to open.\n    '

class Params1(TypedDict):
    accountRelationshipId: NotRequired[str]
    view: NotRequired[Literal['media_buys', 'creatives', 'delivery']]

class OpenMediaBuysPageResult(TypedDict):
    params: Params1
OpenMediaBuysPageError: TypeAlias = V3ToolErrorResponse

class OpenConnectionsPageInput(TypedDict):
    advertiserId: NotRequired[str]
    '\n    Canonical advertiser ID; omit for account scope.\n    '
    sellerId: NotRequired[str]
    '\n    Canonical seller (Storefront) ID to open.\n    '
    connectionAction: NotRequired[Literal['connect']]
    '\n    Open seller setup; requires sellerId and user confirmation.\n    '

class OpenConnectionsPageResult(TypedDict):
    advertiserId: NotRequired[str]
    '\n    Opened advertiser ID when advertiser-scoped.\n    '
    sellerId: NotRequired[str]
    '\n    Opened seller ID when seller-scoped.\n    '
    connectionAction: NotRequired[Literal['connect']]
    '\n    Requested seller action when supplied.\n    '
OpenConnectionsPageError: TypeAlias = V3ToolErrorResponse

class OpenCreativeEnginesPageInput(TypedDict):
    engineId: NotRequired[str]
    '\n    Optional creative-engine focus hint.\n    '
    connectionId: NotRequired[str]
    '\n    Optional creative-engine connection focus hint.\n    '
    connectionAction: NotRequired[Literal['connect']]
    '\n    Focus the secure setup control for the selected engine. The buyer must start setup in the Page.\n    '

class OpenCreativeEnginesPageResult(TypedDict):
    engineId: NotRequired[str]
    connectionId: NotRequired[str]
    connectionAction: NotRequired[Literal['connect']]
OpenCreativeEnginesPageError: TypeAlias = V3ToolErrorResponse

class OpenAdvertisersPageInput(TypedDict):
    pass

class OpenAdvertisersPageResult(TypedDict):
    pass
OpenAdvertisersPageError: TypeAlias = V3ToolErrorResponse

class OpenCampaignsPageInput(TypedDict):
    advertiserId: NotRequired[str]
    '\n    Scope to one advertiser; resolve a name with search(kind: "advertiser") first. Omit for all.\n    '
    campaignId: NotRequired[str]
    '\n    Focus one campaign; resolve a name with search(kind: "campaign") first.\n    '
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from a seller Advertisers row.\n    '

class Params2(TypedDict):
    """
    Focus seeded into the Page; absent when unscoped.
    """
    advertiserId: NotRequired[str]
    '\n    Advertiser the list is scoped to.\n    '
    advertiserName: NotRequired[str]
    '\n    Display name for that advertiser while the Page loads.\n    '
    campaignId: NotRequired[str]
    '\n    Campaign the Page is focused on.\n    '
    management: NotRequired[Literal['tracked', 'managed', 'all']]
    status: NotRequired[Literal['ALL']]
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Self-serve buyer child scope revalidated by every Page read.\n    '

class OpenCampaignsPageResult(TypedDict):
    params: NotRequired[Params2]
    '\n    Focus seeded into the Page; absent when unscoped.\n    '
    humanHandoff: NotRequired[OpenCampaignsPageSuccessPageHumanHandoffRequired | OpenCampaignsPageSuccessPageHumanHandoffUnavailable]
OpenCampaignsPageError: TypeAlias = V3ToolErrorResponse

class OpenCampaignReceiptInput(TypedDict):
    campaignId: str
    '\n    The draft campaign to review. Find it with search(kind: "campaign", filter: {phase: ["draft"]}).\n    '
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '

class Params3(TypedDict):
    """
    Focus seeded into the Page.
    """
    campaignId: str
    '\n    Campaign the receipt is for.\n    '
    advertiserId: NotRequired[str]
    '\n    Owning advertiser when linked.\n    '
    mode: Literal['review']
    '\n    Receipt moment the Page renders.\n    '
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued sponsored self-serve child scope.\n    '

class Budget(TypedDict):
    """
    Campaign budget when set.
    """
    total: OpenCampaignReceiptSuccessReceiptBudgetTotal
    currency: OpenCampaignReceiptSuccessReceiptBudgetCurrency
    dailyCap: NotRequired[float]
    '\n    Daily cap.\n    '
    pacing: NotRequired[Literal['even', 'asap', 'frontloaded']]
    '\n    Budget pacing preference.\n    '

class Blocker2(TypedDict):
    code: str
    '\n    Stable blocker code.\n    '
    message: str
    '\n    What is blocking go-live.\n    '
OpenCampaignReceiptError: TypeAlias = V3ToolErrorResponse
RequiredAuthoredField: TypeAlias = str

class CampaignComposition(TypedDict):
    """
    Optional campaign context for composing the uploaded creative.
    """
    campaign_id: str
    '\n    Campaign receiving the uploaded creative.\n    '
    advertiser_id: NotRequired[UploadCreativeAssetRequestCampaignCompositionAdvertiserId]
    '\n    Optional campaign advertiser; when supplied, it must match advertiserId.\n    '
    campaign_name: NotRequired[str]
    '\n    Optional campaign name for the upload experience.\n    '
    creative_name: NotRequired[str]
    '\n    Optional creative name for the upload experience.\n    '
    required_authored_fields: list[RequiredAuthoredField]
    '\n    Creative fields that remain to be authored.\n    '

class UploadCreativeAssetInput(TypedDict):
    advertiserId: str
    '\n    Buyer-owned advertiser that owns the uploaded source.\n    '
    campaign_composition: NotRequired[CampaignComposition]
    '\n    Optional campaign context for composing the uploaded creative.\n    '

class CampaignComposition1(TypedDict):
    """
    Optional campaign context for composing the uploaded creative.
    """
    campaign_id: str
    '\n    Campaign receiving the uploaded creative.\n    '
    advertiser_id: NotRequired[UploadCreativeAssetSuccessCampaignCompositionAdvertiserId]
    '\n    Optional campaign advertiser; when supplied, it must match advertiserId.\n    '
    campaign_name: NotRequired[str]
    '\n    Optional campaign name for the upload experience.\n    '
    creative_name: NotRequired[str]
    '\n    Optional creative name for the upload experience.\n    '
    required_authored_fields: list[RequiredAuthoredField]
    '\n    Creative fields that remain to be authored.\n    '

class UploadCreativeAssetResult(TypedDict):
    advertiserId: UploadCreativeAssetSuccessAdvertiserId
    advertiserName: NotRequired[str]
    accepted_content_types: list[Literal['image/jpeg', 'image/png', 'video/mp4', 'audio/wav', 'audio/x-wav', 'audio/wave', 'audio/mpeg', 'audio/mp3']]
    max_size_bytes: int
    '\n    Largest byte limit among the accepted content types.\n    '
    max_size_bytes_by_content_type: dict[str, int]
    '\n    Exact byte limits keyed by accepted_content_types.\n    '
    fallback_url: str
    campaign_composition: NotRequired[CampaignComposition1]
    '\n    Optional campaign context for composing the uploaded creative.\n    '
UploadCreativeAssetError: TypeAlias = V3ToolErrorResponse

class OpenApprovalsInput(TypedDict):
    mediaBuyId: NotRequired[str]
    '\n    Optional media-buy id to open directly in the queue.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Optional buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    creativeId: NotRequired[str]
    '\n    Legacy creative id to focus only when exactly one loaded review version matches. Prefer reviewRef.\n    '
    reviewRef: NotRequired[str]
    '\n    Exact reviewRef from the approval queue; focuses one creative review version.\n    '

class Params4(TypedDict):
    mediaBuyId: NotRequired[str]
    '\n    Optional media-buy id to open directly in the queue.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Optional buyer customer id that disambiguates a buyer-scoped media-buy id.\n    '
    creativeId: NotRequired[str]
    '\n    Legacy creative id to focus only when exactly one loaded review version matches. Prefer reviewRef.\n    '
    reviewRef: NotRequired[str]
    '\n    Exact reviewRef from the approval queue; focuses one creative review version.\n    '

class OpenApprovalsResult(TypedDict):
    params: NotRequired[Params4]
OpenApprovalsError: TypeAlias = V3ToolErrorResponse

class OpenCreativeLibraryInput(TypedDict):
    advertiserId: str
    '\n    Advertiser ID returned by advertiser search.\n    '
    view: NotRequired[Literal['all', 'shelf']]
    '\n    Creative view: all visible or promoted shelf.\n    '
    lens: NotRequired[Literal['creatives', 'assets', 'composer']]
    '\n    Browse Creatives, assets, or open the campaign composer.\n    '
    campaignId: NotRequired[str]
    '\n    Campaign to focus within this advertiser Library.\n    '
    creativeId: NotRequired[str]
    '\n    Exact Creative to focus within the campaign.\n    '
    sessionId: NotRequired[str]
    '\n    Editable Creative Session to resume in the composer.\n    '

class Params5(TypedDict):
    advertiserId: str
    advertiserName: str
    lens: Literal['creatives', 'assets']
    view: Literal['all', 'shelf']
    campaignId: NotRequired[str]
    campaignName: NotRequired[str]
    creativeId: NotRequired[str]
    initialAction: NotRequired[Literal['upload', 'compose']]
    sessionId: NotRequired[str]

class OpenCreativeLibraryResult(TypedDict):
    params: Params5
    openInBrowserUrl: NotRequired[str]
OpenCreativeLibraryError: TypeAlias = V3ToolErrorResponse

class Range(TypedDict):
    """
    Dates (max 90 days) or lifetime for delivery; invalid for margin.
    """
    startDate: NotRequired[str]
    '\n    Inclusive delivery date, YYYY-MM-DD.\n    '
    endDate: NotRequired[str]
    '\n    Inclusive delivery date, YYYY-MM-DD.\n    '
    lifetime: NotRequired[Literal[True]]
    '\n    Campaign delivery only: provider-supported or stored history, no dates.\n    '

class Filters(TypedDict):
    """
    Optional report filters; invalid combinations are rejected.
    """
    inventorySourceId: NotRequired[str]
    '\n    Filter to one seller inventory source.\n    '
    advertiserId: NotRequired[str]
    '\n    Delivery: filter to one advertiser.\n    '
    campaignId: NotRequired[str]
    '\n    Campaign delivery: filter to one campaign.\n    '
    channelGroupId: NotRequired[str]
    '\n    Campaign delivery: filter to one channel group.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Margin: filter to one buyer customer.\n    '
    mediaBuyId: NotRequired[str]
    '\n    Filter to one media buy.\n    '
    packageId: NotRequired[str]
    '\n    Filter to one buyer-facing package.\n    '

class GetDeliveryInput(TypedDict):
    metrics: NotRequired[list[Literal['impressions', 'spend', 'clicks', 'views', 'completedViews', 'conversions', 'leads', 'videoCompletions', 'conversionValue', 'ecpm', 'cpc', 'ctr', 'completionRate', 'cpa', 'roas', 'sellBooked', 'sellRealized', 'buyBooked', 'buyRealized', 'spreadBooked', 'spreadRealized', 'marginBookedPct', 'marginRealizedPct', 'bookedComplete', 'realizedComplete']]]
    '\n    Metrics; omit for report defaults.\n    '
    dimensions: NotRequired[list[Literal['date', 'advertiser', 'campaign', 'channel_group', 'channel', 'buyer', 'media_buy', 'package', 'inventory_source', 'seller', 'sales_agent'] | str]]
    '\n    Group-by dimensions; campaign delivery also accepts labels.<dimension_key>. Omit for leaf grain.\n    '
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    report: NotRequired[Literal['delivery', 'campaign_delivery', 'live_campaign_delivery', 'margin']]
    '\n    Select seller delivery, stored campaign delivery, live provider campaign delivery, or margin.\n    '
    range: NotRequired[Range]
    '\n    Dates (max 90 days) or lifetime for delivery; invalid for margin.\n    '
    filters: NotRequired[Filters]
    '\n    Optional report filters; invalid combinations are rejected.\n    '
    limit: NotRequired[int]
    '\n    Maximum rows in this page (1-100).\n    '
    cursor: NotRequired[str]
    '\n    Opaque nextCursor from the same query and limit.\n    '

class Range1(TypedDict):
    startDate: NotRequired[str]
    endDate: NotRequired[str]
    lifetime: NotRequired[Literal[True]]

class Filters1(TypedDict):
    inventorySourceId: NotRequired[str]
    '\n    Filter to one seller inventory source.\n    '
    advertiserId: NotRequired[str]
    '\n    Delivery: filter to one advertiser.\n    '
    campaignId: NotRequired[str]
    '\n    Campaign delivery: filter to one campaign.\n    '
    channelGroupId: NotRequired[str]
    '\n    Campaign delivery: filter to one channel group.\n    '
    buyerCustomerId: NotRequired[int]
    '\n    Margin: filter to one buyer customer.\n    '
    mediaBuyId: NotRequired[str]
    '\n    Filter to one media buy.\n    '
    packageId: NotRequired[str]
    '\n    Filter to one buyer-facing package.\n    '

class Query(TypedDict):
    metrics: list[Literal['impressions', 'spend', 'clicks', 'views', 'completedViews', 'conversions', 'leads', 'videoCompletions', 'conversionValue', 'ecpm', 'cpc', 'ctr', 'completionRate', 'cpa', 'roas', 'sellBooked', 'sellRealized', 'buyBooked', 'buyRealized', 'spreadBooked', 'spreadRealized', 'marginBookedPct', 'marginRealizedPct', 'bookedComplete', 'realizedComplete']]
    dimensions: list[str]
    range: NotRequired[Range1]
    filters: Filters1

class Period(TypedDict):
    startDate: str
    endDate: str

class Dimensions2(TypedDict):
    id: str | float
    name: NotRequired[str | None]
    status: NotRequired[str]
    management: NotRequired[str]
    productId: NotRequired[str | None]
    productName: NotRequired[str | None]
    upstreamMediaBuyId: NotRequired[str]
    upstreamPackageId: NotRequired[str]

class Source2(TypedDict):
    operation: GetDeliverySuccessRowsItemSourceOperation
    inventorySourceIds: list[str]
    inventorySourceIdsTotal: int
    inventorySourceIdsTruncated: bool
    revisionEvidence: Literal['unavailable', 'not_applicable']

class Row(TypedDict):
    dimensions: dict[str, str | float | list[str] | Dimensions2 | None]
    metrics: dict[str, GetDeliverySuccessRowsItemMetricsValue]
    authority: Literal['seller_reported_delivery', 'seller_reported_buyer_projection', 'seller_spread_ledger', 'synthetic_demo']
    source: Source2
    currency: str | None
    denomination: Literal['net', 'gross_buyer', 'ledger_settlement']
    dataThrough: str | None
    freshness: Literal['unverified', 'ledger_as_of', 'unavailable']
    finality: GetDeliverySuccessRowsItemFinality
    billingEligibility: Literal['not_evaluated']
    settlementStatus: NotRequired[str]

class Totals(TypedDict):
    rowsIncluded: int
    currency: str | None
    metrics: dict[str, GetDeliverySuccessTotalsMetricsValue]
    denomination: Literal['net', 'gross_buyer']
    dataThrough: str | None
    finality: GetDeliverySuccessTotalsFinality
    billingEligibility: Literal['not_evaluated']

class Page1(TypedDict):
    limit: int
    returned: int
    total: int
    truncated: bool
    consistency: Literal['live_per_call']
    nextCursor: NotRequired[str]

class Semantics(TypedDict):
    sourceOperation: GetDeliverySuccessSemanticsSourceOperation
    genericFallback: Literal[False]
    measurement: Literal['excluded']
    missingValues: str
    freshness: str
    finality: str
    billingEligibility: str

class Synthetic(TypedDict):
    """
    Present only for the Apostra-owned synthetic Demo Storefront scenario. This data is unsuitable for commercial decisions.
    """
    scenarioId: Literal['synthetic-rolling-delivery-v1']
    notice: Literal['Synthetic demo data only. It is unsuitable for commercial decisions.']

class GetDeliveryResult1(TypedDict):
    report: Literal['delivery', 'campaign_delivery', 'margin']
    query: Query
    period: NotRequired[Period]
    rows: list[Row]
    totals: NotRequired[Totals]
    page: Page1
    semantics: Semantics
    synthetic: NotRequired[Synthetic]
    '\n    Present only for the Apostra-owned synthetic Demo Storefront scenario. This data is unsuitable for commercial decisions.\n    '

class Filters2(TypedDict):
    campaignId: str

class Query1(TypedDict):
    range: Range1
    filters: Filters2

class ReportingPeriod(TypedDict):
    start: GetDeliverySuccessDeliverySummaryReportingPeriodStart
    end: GetDeliverySuccessDeliverySummaryReportingPeriodEnd

class ReportingRevision(TypedDict):
    reporting_revision_id: GetDeliverySuccessDeliverySummaryReportingRevisionReportingRevisionId
    finality: NotRequired[GetDeliverySuccessDeliverySummaryReportingRevisionFinality]
    data_through: NotRequired[GetDeliverySuccessDeliverySummaryReportingRevisionDataThrough | None]
    observed_at: NotRequired[GetDeliverySuccessDeliverySummaryReportingRevisionObservedAt]
    finalized_at: NotRequired[GetDeliverySuccessDeliverySummaryReportingRevisionFinalizedAt]

class Qualifier(TypedDict):
    viewability_standard: NotRequired[GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierViewabilityStandard]
    completion_source: NotRequired[GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierCompletionSource]
    attribution_methodology: NotRequired[GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierAttributionMethodology]
    attribution_window: NotRequired[GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierAttributionWindow]
    lift_dimension: NotRequired[Literal['awareness', 'consideration', 'favorability', 'purchase_intent', 'ad_recall']]

class Vendor(TypedDict):
    domain: NotRequired[GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemVendorDomain]
    brand_id: NotRequired[GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemVendorBrandId]

class MetricAggregate(TypedDict):
    scope: Literal['standard', 'vendor']
    metric_id: GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemMetricId
    value: float
    qualifier: NotRequired[Qualifier]
    vendor: NotRequired[Vendor]

class AggregatedTotals(TypedDict):
    metrics: dict[Literal['impressions', 'spend', 'clicks', 'completed_views', 'views', 'conversions', 'conversion_value', 'commissionable_value', 'roas', 'new_to_brand_rate', 'cost_per_acquisition', 'completion_rate', 'reach', 'frequency'], GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricsValue]
    media_buy_count: NotRequired[int]
    reach_unit: NotRequired[GetDeliverySuccessDeliverySummaryAggregatedTotalsReachUnit]
    reach_aggregation: NotRequired[GetDeliverySuccessDeliverySummaryAggregatedTotalsReachAggregation]
    metric_aggregates: NotRequired[list[MetricAggregate]]
    metric_aggregates_truncated: NotRequired[bool]
    metric_aggregates_total_count: NotRequired[int]

class BreakdownStatus1(TypedDict):
    kind: Literal['demographic', 'property', 'collection_property', 'installment_property', 'placement_property']
    truncated: NotRequired[bool]
    suppressed: NotRequired[bool]

class BreakdownStatus2(TypedDict):
    kind: Literal['catalog_item', 'format', 'creative', 'keyword', 'geo', 'collection', 'installment', 'spot']
    truncated: NotRequired[bool]

class Semantics1(TypedDict):
    sourceOperation: Literal['get_campaign_delivery']
    genericFallback: Literal[False]
    measurement: Literal['excluded']
    missingValues: str
    freshness: str
    finality: str
    billingEligibility: str
GetDeliveryError: TypeAlias = V3ToolErrorResponse

class Value2(TypedDict):
    macro: Literal['MEDIA_BUY_ID', 'PACKAGE_ID', 'CREATIVE_ID', 'CACHEBUSTER', 'TIMESTAMP', 'CLICK_URL', 'GDPR', 'GDPR_CONSENT', 'US_PRIVACY', 'GPP_STRING', 'GPP_SID', 'IP_ADDRESS', 'LIMIT_AD_TRACKING', 'DEVICE_TYPE', 'OS', 'OS_VERSION', 'DEVICE_MAKE', 'DEVICE_MODEL', 'USER_AGENT', 'APP_BUNDLE', 'APP_NAME', 'COUNTRY', 'REGION', 'CITY', 'ZIP', 'DMA', 'LAT', 'LONG', 'DEVICE_ID', 'DEVICE_ID_TYPE', 'DOMAIN', 'PAGE_URL', 'REFERRER', 'KEYWORDS', 'PLACEMENT_ID', 'FOLD_POSITION', 'AD_WIDTH', 'AD_HEIGHT', 'VIDEO_ID', 'VIDEO_TITLE', 'VIDEO_DURATION', 'VIDEO_CATEGORY', 'CONTENT_GENRE', 'CONTENT_RATING', 'PLAYER_WIDTH', 'PLAYER_HEIGHT', 'POD_POSITION', 'POD_SIZE', 'AD_BREAK_ID', 'STATION_ID', 'COLLECTION_NAME', 'INSTALLMENT_ID', 'AUDIO_DURATION', 'TMPX', 'IMPRESSION_ID', 'AXEM', 'CATALOG_ID', 'SKU', 'GTIN', 'OFFERING_ID', 'JOB_ID', 'HOTEL_ID', 'FLIGHT_ID', 'VEHICLE_ID', 'LISTING_ID', 'STORE_ID', 'PROGRAM_ID', 'DESTINATION_ID', 'CREATIVE_VARIANT_ID', 'APP_ITEM_ID', 'ITEM_NAME', 'ITEM_DESCRIPTION', 'ITEM_TAGLINE', 'ITEM_PRICE', 'ITEM_PRICE_CURRENCY']
    '\n    AdCP universal macro name.\n    '
    value: str
    '\n    Raw synthetic test value; do not pre-encode it and never submit a real user identifier.\n    '

class TestCreativeMacrosInput(TypedDict):
    requiredMacros: NotRequired[list[Literal['MEDIA_BUY_ID', 'PACKAGE_ID', 'CREATIVE_ID', 'CACHEBUSTER', 'TIMESTAMP', 'CLICK_URL', 'GDPR', 'GDPR_CONSENT', 'US_PRIVACY', 'GPP_STRING', 'GPP_SID', 'IP_ADDRESS', 'LIMIT_AD_TRACKING', 'DEVICE_TYPE', 'OS', 'OS_VERSION', 'DEVICE_MAKE', 'DEVICE_MODEL', 'USER_AGENT', 'APP_BUNDLE', 'APP_NAME', 'COUNTRY', 'REGION', 'CITY', 'ZIP', 'DMA', 'LAT', 'LONG', 'DEVICE_ID', 'DEVICE_ID_TYPE', 'DOMAIN', 'PAGE_URL', 'REFERRER', 'KEYWORDS', 'PLACEMENT_ID', 'FOLD_POSITION', 'AD_WIDTH', 'AD_HEIGHT', 'VIDEO_ID', 'VIDEO_TITLE', 'VIDEO_DURATION', 'VIDEO_CATEGORY', 'CONTENT_GENRE', 'CONTENT_RATING', 'PLAYER_WIDTH', 'PLAYER_HEIGHT', 'POD_POSITION', 'POD_SIZE', 'AD_BREAK_ID', 'STATION_ID', 'COLLECTION_NAME', 'INSTALLMENT_ID', 'AUDIO_DURATION', 'TMPX', 'IMPRESSION_ID', 'AXEM', 'CATALOG_ID', 'SKU', 'GTIN', 'OFFERING_ID', 'JOB_ID', 'HOTEL_ID', 'FLIGHT_ID', 'VEHICLE_ID', 'LISTING_ID', 'STORE_ID', 'PROGRAM_ID', 'DESTINATION_ID', 'CREATIVE_VARIANT_ID', 'APP_ITEM_ID', 'ITEM_NAME', 'ITEM_DESCRIPTION', 'ITEM_TAGLINE', 'ITEM_PRICE', 'ITEM_PRICE_CURRENCY']]]
    '\n    Required macros must occur and have values. Absence fails; defaults to all canonical macros present.\n    '
    rawInput: str
    '\n    Exact tracker URL to test. It is preserved separately from compiled output.\n    '
    sourceDialect: NotRequired[Literal['auto', 'adcp', 'happydemics', 'gam', 'vast']]
    '\n    Source syntax. Use auto only for a registry-recognized origin; never guess ambiguous vendor tokens.\n    '
    targetDialect: Literal['adcp', 'gam']
    '\n    Recipient syntax to inspect. GAM emits native ad-server macros; AdCP retains universal macros.\n    '
    scenario: Literal['device_id_present', 'device_id_unavailable', 'gdpr_applies_with_consent', 'gdpr_does_not_apply', 'missing_required_value']
    '\n    Deterministic privacy/runtime scenario. Values are synthetic unless explicit overrides are supplied.\n    '
    scenarioKey: NotRequired[str]
    '\n    Stable synthetic run key. Change it to test a different deterministic cachebuster.\n    '
    gvlVendorId: NotRequired[int]
    '\n    Syntax-only IAB GVL vendor ID for GAM consent. Never treated as verified or inferred from the URL.\n    '
    values: NotRequired[list[Value2]]
    '\n    Optional explicit synthetic bindings. Their output source is labeled provided, not synthetic.\n    '

class Raw(TypedDict):
    template: str

class Canonical(TypedDict):
    template: str
    compilerVersion: str
    publishable: bool

class Target4(TypedDict):
    template: str
    droppedParameters: list[str]
    unmappedMacros: list[str]
    droppedConsentMacros: list[str]

class Substituted(TypedDict):
    template: str
    droppedParameters: list[str]
    unresolvedMacros: list[str]

class Stages(TypedDict):
    raw: Raw
    canonical: Canonical
    target: Target4
    substituted: Substituted

class Mapping(TypedDict):
    rawToken: str
    canonicalMacro: NotRequired[str]
    semantic: NotRequired[str]
    sourceDialect: str
    status: Literal['canonical', 'mapped', 'unresolved', 'ambiguous']
    start: int
    end: int
    registryEntryId: NotRequired[str]
    registryVersion: NotRequired[str]

class Binding(TypedDict):
    macro: Literal['MEDIA_BUY_ID', 'PACKAGE_ID', 'CREATIVE_ID', 'CACHEBUSTER', 'TIMESTAMP', 'CLICK_URL', 'GDPR', 'GDPR_CONSENT', 'US_PRIVACY', 'GPP_STRING', 'GPP_SID', 'IP_ADDRESS', 'LIMIT_AD_TRACKING', 'DEVICE_TYPE', 'OS', 'OS_VERSION', 'DEVICE_MAKE', 'DEVICE_MODEL', 'USER_AGENT', 'APP_BUNDLE', 'APP_NAME', 'COUNTRY', 'REGION', 'CITY', 'ZIP', 'DMA', 'LAT', 'LONG', 'DEVICE_ID', 'DEVICE_ID_TYPE', 'DOMAIN', 'PAGE_URL', 'REFERRER', 'KEYWORDS', 'PLACEMENT_ID', 'FOLD_POSITION', 'AD_WIDTH', 'AD_HEIGHT', 'VIDEO_ID', 'VIDEO_TITLE', 'VIDEO_DURATION', 'VIDEO_CATEGORY', 'CONTENT_GENRE', 'CONTENT_RATING', 'PLAYER_WIDTH', 'PLAYER_HEIGHT', 'POD_POSITION', 'POD_SIZE', 'AD_BREAK_ID', 'STATION_ID', 'COLLECTION_NAME', 'INSTALLMENT_ID', 'AUDIO_DURATION', 'TMPX', 'IMPRESSION_ID', 'AXEM', 'CATALOG_ID', 'SKU', 'GTIN', 'OFFERING_ID', 'JOB_ID', 'HOTEL_ID', 'FLIGHT_ID', 'VEHICLE_ID', 'LISTING_ID', 'STORE_ID', 'PROGRAM_ID', 'DESTINATION_ID', 'CREATIVE_VARIANT_ID', 'APP_ITEM_ID', 'ITEM_NAME', 'ITEM_DESCRIPTION', 'ITEM_TAGLINE', 'ITEM_PRICE', 'ITEM_PRICE_CURRENCY']
    '\n    AdCP universal macro name.\n    '
    value: NotRequired[str]
    source: Literal['synthetic', 'provided', 'privacy_suppressed', 'missing']

class Diagnostic(TypedDict):
    stage: Literal['source', 'target', 'substitution']
    code: str
    severity: Literal['info', 'warning', 'error']
    message: str
    macro: NotRequired[str]
    parameter: NotRequired[str]

class Projection(TypedDict):
    maxBytes: int
    truncated: bool
    stageTemplatePreviewsTruncated: int
    bindingValuePreviewsTruncated: int
    omittedBindingValues: int
    omittedBindings: int
    omittedMappings: int
    omittedDiagnostics: int
    detailReduced: bool

class TestCreativeMacrosResult(TypedDict):
    testerVersion: str
    passed: bool
    readyForPreview: bool
    syntheticDataOnly: bool
    scenario: Literal['device_id_present', 'device_id_unavailable', 'gdpr_applies_with_consent', 'gdpr_does_not_apply', 'missing_required_value']
    scenarioKey: str
    sourceDialect: str
    targetDialect: Literal['adcp', 'gam']
    stages: Stages
    mappings: list[Mapping]
    bindings: list[Binding]
    diagnostics: list[Diagnostic]
    projection: Projection
TestCreativeMacrosError: TypeAlias = V3ToolErrorResponse
SelectedPostureItem: TypeAlias = str
PlaybookVersionItem: TypeAlias = int
MaterialItem: TypeAlias = str
QuickPresetItem: TypeAlias = str
CategoryItem: TypeAlias = str
LocationItem: TypeAlias = str
MarketItem: TypeAlias = str
BuyerItem: TypeAlias = str
AdvertiserItem: TypeAlias = str
ProductItem: TypeAlias = str
ResponseRecipeVersionItem: TypeAlias = str
ModelVersionItem: TypeAlias = str
JudgeVersionItem: TypeAlias = str
CurrencyItem: TypeAlias = str
EvaluationStateItem: TypeAlias = str
OutcomeItem: TypeAlias = str

class Filters3(TypedDict):
    """
    Optional exact-match filters. Purpose defaults to live.
    """
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']]]
    '\n    Quality/efficiency purposes; commercial stays live-only. Omit for live.\n    '
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    '\n    quick/uploaded/inbound/manual origin.\n    '
    selectedPosture: NotRequired[list[SelectedPostureItem]]
    '\n    Selected posture.\n    '
    playbookVersion: NotRequired[list[PlaybookVersionItem]]
    '\n    Playbook version.\n    '
    material: NotRequired[list[MaterialItem]]
    '\n    Material revision identity.\n    '
    quickPreset: NotRequired[list[QuickPresetItem]]
    '\n    Quick RFP preset identity.\n    '
    category: NotRequired[list[CategoryItem]]
    '\n    Commercial category.\n    '
    location: NotRequired[list[LocationItem]]
    '\n    Location.\n    '
    market: NotRequired[list[MarketItem]]
    '\n    Market.\n    '
    channel: NotRequired[list[ChannelItem]]
    '\n    Requested channel.\n    '
    buyer: NotRequired[list[BuyerItem]]
    '\n    Buyer identity.\n    '
    advertiser: NotRequired[list[AdvertiserItem]]
    '\n    Advertiser identity.\n    '
    product: NotRequired[list[ProductItem]]
    '\n    Offered product identity.\n    '
    responseRecipeVersion: NotRequired[list[ResponseRecipeVersionItem]]
    '\n    Response recipe version.\n    '
    modelVersion: NotRequired[list[ModelVersionItem]]
    '\n    Composer model version.\n    '
    judgeVersion: NotRequired[list[JudgeVersionItem]]
    '\n    Truth-gate or judge version.\n    '
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    '\n    miss/hit/customized/bypassed cache mode.\n    '
    currency: NotRequired[list[CurrencyItem]]
    '\n    Uppercase ISO 4217 currency.\n    '
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    '\n    Terminal response state.\n    '
    evaluationState: NotRequired[list[EvaluationStateItem]]
    '\n    Evaluation state.\n    '
    outcome: NotRequired[list[OutcomeItem]]
    '\n    Recorded outcome result.\n    '

class Range3(TypedDict):
    """
    Required inclusive range, at most 366 days.
    """
    startDate: str
    '\n    Inclusive UTC turn-created date, YYYY-MM-DD.\n    '
    endDate: str
    '\n    Inclusive UTC turn-created date, YYYY-MM-DD.\n    '

class OrderByItem(TypedDict):
    field: Literal['rfp_count', 'response_ready_rate', 'pass_rate', 'needs_clarification_rate', 'failure_rate', 'average_grade', 'correction_rate', 'revision_rate', 'seller_intervention_rate', 'truth_drop_rate', 'feedback_agreement_rate', 'average_processing_latency_ms', 'p95_processing_latency_ms', 'average_generation_cost', 'full_compose_rate', 'cache_hit_rate', 'retry_rate', 'buyer_response_rate', 'acceptance_rate', 'win_rate', 'booked_budget', 'average_booked_budget', 'date', 'week', 'selected_posture', 'playbook_version', 'material', 'quick_preset', 'category', 'location', 'market', 'channel', 'origin', 'purpose', 'buyer', 'advertiser', 'product', 'response_recipe_version', 'model_version', 'judge_version', 'cache_mode', 'currency']
    '\n    Selected metric or dimension.\n    '
    direction: Literal['asc', 'desc']
    '\n    Ascending or descending.\n    '

class GetRfpPerformanceInput(TypedDict):
    metrics: list[Literal['rfp_count', 'response_ready_rate', 'pass_rate', 'needs_clarification_rate', 'failure_rate', 'average_grade', 'correction_rate', 'revision_rate', 'seller_intervention_rate', 'truth_drop_rate', 'feedback_agreement_rate', 'average_processing_latency_ms', 'p95_processing_latency_ms', 'average_generation_cost', 'full_compose_rate', 'cache_hit_rate', 'retry_rate', 'buyer_response_rate', 'acceptance_rate', 'win_rate', 'booked_budget', 'average_booked_budget']]
    '\n    Quality, efficiency, or commercial metrics (1-6).\n    '
    dimensions: NotRequired[list[Literal['date', 'week', 'selected_posture', 'playbook_version', 'material', 'quick_preset', 'category', 'location', 'market', 'channel', 'origin', 'purpose', 'buyer', 'advertiser', 'product', 'response_recipe_version', 'model_version', 'judge_version', 'cache_mode', 'currency']]]
    '\n    Group-by dimensions (0-3).\n    '
    filters: NotRequired[Filters3]
    '\n    Optional exact-match filters. Purpose defaults to live.\n    '
    range: Range3
    '\n    Required inclusive range, at most 366 days.\n    '
    orderBy: NotRequired[list[OrderByItem]]
    '\n    Stable ordering clauses (0-2).\n    '
    limit: NotRequired[int]
    '\n    Maximum rows in this page (1-5).\n    '
    cursor: NotRequired[str]
    '\n    Opaque nextCursor from this exact query.\n    '

class Range4(TypedDict):
    startDate: str
    endDate: str

class OrderByItem1(TypedDict):
    field: str
    direction: Literal['asc', 'desc']

class Query2(TypedDict):
    metrics: list[str]
    dimensions: list[str]
    filters: dict[str, list[str | float]]
    range: Range4
    orderBy: list[OrderByItem1]

class Population(TypedDict):
    unit: Literal['turns', 'rfps']
    eligible: int
    observed: int
    excluded: int
    exclusionReasons: dict[str, int]

class Freshness(TypedDict):
    dataThrough: str | None

class Metrics(TypedDict):
    value: float | None
    status: Literal['available', 'unavailable']
    reason: NotRequired[str]
    population: Population
    freshness: Freshness
    finality: Literal['final', 'preliminary', 'mixed', 'unavailable']
    currency: NotRequired[str | None]

class Provenance(TypedDict):
    authority: Literal['seller_rfp_lifecycle']
    attributionMethod: Literal['explicit_turn_binding']

class Row1(TypedDict):
    dimensions: dict[str, str | float | None]
    metrics: dict[str, Metrics]
    provenance: Provenance

class Page2(TypedDict):
    limit: int
    returned: int
    total: int
    truncated: bool
    consistency: Literal['immutable_snapshot']
    snapshotAt: str
    nextCursor: NotRequired[str]

class MetricFamilies(TypedDict):
    quality: list[str]
    efficiency: list[str]
    commercial: list[str]

class Semantics2(TypedDict):
    commercialPopulation: Literal['live_only']
    includedPurposes: list[str]
    syntheticIncluded: bool
    terminalFactsOnly: Literal[True]
    minimumDisclosureRfps: int
    counterpartyRowsSuppressed: bool
    maximumFactsPerQuery: int
    maximumRowsPerPage: int
    maximumSerializedBytes: int
    maximumApproximateTokens: int
    metricFamilies: MetricFamilies

class GetRfpPerformanceResult(TypedDict):
    query: Query2
    rows: list[Row1]
    page: Page2
    semantics: Semantics2
GetRfpPerformanceError: TypeAlias = V3ToolErrorResponse

class MaterialCandidate(TypedDict):
    """
    Exact get(material) provenance; include only to confirm that candidate.
    """
    sourceMaterialId: str
    '\n    Source Material id returned by get(material).\n    '
    sourceRevision: int
    '\n    Exact immutable Material source revision reviewed.\n    '
    candidateId: str
    '\n    Stable candidate id returned by get(material).\n    '
    advertiserRef: NotRequired[str]
    '\n    Required exact advertiser scope for advertiser-confidential Material.\n    '

class Capabilities(TypedDict):
    """
    Capabilities to patch; omitted flags stay unchanged.
    """
    offersCreativeReview: NotRequired[bool]
    '\n    Advertise creative review to buyers.\n    '
    offersCampaignApproval: NotRequired[bool]
    '\n    Advertise campaign approval to buyers.\n    '

class DemandContact(TypedDict):
    """
    Demand contact, or null to clear it.
    """
    name: str
    '\n    Name of the buyer-facing demand contact.\n    '
    email: str
    '\n    Email address of the buyer-facing demand contact.\n    '

class Listing(TypedDict):
    """
    Canonical grouped Listing write; alternative to the flat fields below.
    """
    description: NotRequired[str | None]
    '\n    Short Marketplace description, or null to clear.\n    '
    channels: NotRequired[list[SaveSellerRequestListingChannelsItem]]
    '\n    Buyer-visible channels.\n    '
    countries: NotRequired[list[SaveSellerRequestListingCountriesItem] | None]
    '\n    Buyer-visible ISO countries, or null to clear.\n    '
    acceptsAllCountries: NotRequired[bool]
    '\n    Accept briefs from every country.\n    '

class MediaKit(TypedDict):
    """
    Deprecated alias for `listing`.
    """
    description: NotRequired[str | None]
    '\n    Short Marketplace description, or null to clear.\n    '
    channels: NotRequired[list[SaveSellerRequestMediaKitChannelsItem]]
    '\n    Buyer-visible channels.\n    '
    countries: NotRequired[list[SaveSellerRequestMediaKitCountriesItem] | None]
    '\n    Buyer-visible ISO countries, or null to clear.\n    '
    acceptsAllCountries: NotRequired[bool]
    '\n    Accept briefs from every country.\n    '

class Distribution(TypedDict):
    """
    Admin-only Distribution configuration. Send separately from other Seller changes.
    """
    openaiChallengeToken: str | None
    '\n    OpenAI domain-challenge token, or null to remove it.\n    '
    confirmReplace: NotRequired[bool]
    '\n    Confirm replacing the current OpenAI challenge token.\n    '
    confirmRemove: NotRequired[bool]
    '\n    Confirm removing the current OpenAI challenge token.\n    '

class Admission(TypedDict):
    """
    Admit one seller-controlled pending buyer-account intake at the version returned by get(account_relationship).
    """
    intakeId: str
    '\n    Pending buyer-account intake ID from get(account_relationship).\n    '
    expectedVersion: int
    '\n    Current intake version from get(account_relationship).\n    '
    decision: Literal['admit']
    '\n    Record admission for this pending buyer-account intake.\n    '
    message: NotRequired[str]
    '\n    Optional note recorded with this admission decision.\n    '

class Admission1(TypedDict):
    """
    Decline one seller-controlled pending buyer-account intake with a reason.
    """
    intakeId: str
    '\n    Pending buyer-account intake ID from get(account_relationship).\n    '
    expectedVersion: int
    '\n    Current intake version from get(account_relationship).\n    '
    decision: Literal['decline']
    '\n    Decline this pending buyer-account intake.\n    '
    message: str
    '\n    Reason recorded with the decision to decline this intake.\n    '

class SaveSellerInput(TypedDict):
    resolveBrand: NotRequired[str]
    '\n    Look up public brand.json without saving. Send as the only field.\n    '
    identityContract: NotRequired[Literal['confirmed-v1']]
    '\n    Opt in to identity preview and confirmation. Guide: /v2/setup/v3/identity-setup.\n    '
    preview: NotRequired[bool]
    '\n    Preview an operator-domain change without saving.\n    '
    confirmationToken: NotRequired[str]
    '\n    Token from the identity preview, supplied after the human confirms the change.\n    '
    materialCandidate: NotRequired[MaterialCandidate]
    '\n    Exact get(material) provenance; include only to confirm that candidate.\n    '
    operatorDomain: NotRequired[str]
    '\n    Canonical brand domain. A change can clear prior identity fields only with explicit confirmation.\n    '
    confirmOperatorDomainProfileReset: NotRequired[bool]
    '\n    Allow a changed brand domain to clear identity fields curated for the previous operator.\n    '
    capabilities: NotRequired[Capabilities]
    '\n    Capabilities to patch; omitted flags stay unchanged.\n    '
    setupIntent: NotRequired[Literal['third_party_connect', 'sell_through_scope3']]
    '\n    Records selling intent. Composition derives from Source product paths and access.\n    '
    marketplaceParticipation: NotRequired[Literal['PUBLISHED', 'OPTED_OUT']]
    '\n    Publish or opt out after Scope3 review; publishing never grants Marketplace eligibility.\n    '
    demandContact: NotRequired[DemandContact | None]
    '\n    Demand contact, or null to clear it.\n    '
    description: NotRequired[str | None]
    '\n    Short Marketplace description, or null to clear it.\n    '
    channels: NotRequired[list[SaveSellerRequestChannelsItem]]
    '\n    Buyer-visible channels for a managed Seller listing.\n    '
    countries: NotRequired[list[SaveSellerRequestCountriesItem] | None]
    '\n    Buyer-visible ISO countries for a managed Seller, or null to clear unconfigured coverage.\n    '
    acceptsAllCountries: NotRequired[bool]
    '\n    Explicitly accept briefs from every country.\n    '
    listing: NotRequired[Listing]
    '\n    Canonical grouped Listing write; alternative to the flat fields below.\n    '
    mediaKit: NotRequired[MediaKit]
    '\n    Deprecated alias for `listing`.\n    '
    defaultCurrency: NotRequired[Literal['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD', 'CNY', 'HKD', 'SGD', 'SEK', 'NOK', 'DKK', 'PLN', 'KRW', 'INR', 'MXN', 'BRL', 'ZAR']]
    '\n    Primary seller-confirmed settlement currency.\n    '
    paymentCurrencies: NotRequired[list[SaveSellerRequestPaymentCurrenciesItem]]
    '\n    Currencies the Seller Account accepts for settlement; include the primary currency.\n    '
    confirmCurrencyCatalogImpact: NotRequired[bool]
    '\n    Allow a settlement-currency change even when it hides currently buyer-visible fixed prices.\n    '
    distribution: NotRequired[Distribution]
    '\n    Admin-only Distribution configuration. Send separately from other Seller changes.\n    '
    admission: NotRequired[Admission | Admission1]
    '\n    Seller-only pending buyer relationship decision; read its intake version immediately before saving.\n    '

class SaveSellerResult1(TypedDict):
    action: Literal['brand_resolved']
    brand: SaveSellerSuccessBrand

class SaveSellerResult2(TypedDict):
    action: Literal['admission_recorded', 'decline_recorded']
    intakeId: str
    decision: Literal['admit', 'decline']

class SaveSellerResult3(TypedDict):
    action: Literal['preview']
    identityContract: Literal['confirmed-v1']
    requiresConfirmation: bool
    confirmationToken: str
    before: SaveSellerSuccessBefore
    after: SaveSellerSuccessAfter
    docs: str

class SaveSellerResult4(TypedDict):
    action: Literal['updated', 'unchanged']
    object: SaveSellerSuccessObject

class SaveSellerResult5(TypedDict):
    action: Literal['updated']
    warning: Literal['updated_but_readback_unavailable']
    readback: Literal['unavailable']

class SaveSellerResult6(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SaveSellerSuccessMaterialReceipt

class SaveSellerResult7(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveSellerSuccessMaterialReceipt
SaveSellerResult: TypeAlias = SaveSellerResult1 | SaveSellerResult2 | SaveSellerResult3 | SaveSellerResult4 | SaveSellerResult5 | SaveSellerResult6 | SaveSellerResult7
SaveSellerError: TypeAlias = V3ToolErrorResponse

class ModuleConfig(TypedDict):
    """
    Update one module on an existing modular source. Credentials are never accepted here.
    """
    moduleInstanceId: str
    "\n    The seller-local module id returned by this source's readiness view.\n    "
    config: dict[str, JsonValue]
    '\n    Non-secret module configuration. Nested values are deep-merged by default.\n    '
    merge: NotRequired[bool]
    '\n    Deep-merge by default; false replaces seller-writable configuration.\n    '
    status: NotRequired[Literal['CONFIGURING', 'DISABLED', 'ERROR']]
    '\n    Optional manual module state. ACTIVE is derived by execution workflows.\n    '

class SaveInventorySourceInput(TypedDict):
    id: NotRequired[str]
    '\n    Omit to create. An existing id changes it; an unused id creates it.\n    '
    name: NotRequired[str]
    '\n    Display name. Required when creating.\n    '
    type: NotRequired[Literal['SALES', 'SIGNAL', 'CREATIVE', 'OUTCOME']]
    '\n    Required when creating, and fixed afterwards. SALES sells media.\n    '
    endpointUrl: NotRequired[str]
    "\n    The agent's endpoint URL. Required when creating.\n    "
    protocol: NotRequired[Literal['MCP', 'A2A']]
    '\n    How to speak to the agent. Required when creating.\n    '
    authenticationType: NotRequired[Literal['API_KEY', 'NO_AUTH', 'OAUTH', 'BASIC_AUTH']]
    '\n    Required when creating. The secret is collected in a form, never here.\n    '
    oauthAudience: NotRequired[str]
    '\n    For OAUTH agents, the resource the token targets. Leave unset to discover it from the agent.\n    '
    description: NotRequired[str]
    '\n    Free-text description.\n    '
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED']]
    '\n    Desired state. ACTIVE sells, DISABLED stops, PENDING is set up but idle.\n    '
    moduleConfig: NotRequired[ModuleConfig]
    '\n    Update one module on an existing modular source. Credentials are never accepted here.\n    '

class ModuleConfig1(TypedDict):
    moduleInstanceId: str
    updated: Literal[True]

class SaveInventorySourceResult1(TypedDict):
    action: Literal['created', 'updated', 'unchanged']
    object: SaveInventorySourceSuccessObject
    warning: NotRequired[str]
    moduleConfig: NotRequired[ModuleConfig1]

class SaveInventorySourceResult2(TypedDict):
    success: Literal[True]
    status: int
    data: NotRequired[SaveInventorySourceSuccessData]
SaveInventorySourceResult: TypeAlias = SaveInventorySourceResult1 | SaveInventorySourceResult2
SaveInventorySourceError: TypeAlias = V3ToolErrorResponse
Domain: TypeAlias = str
AddItem: TypeAlias = str
RemoveItem: TypeAlias = str

class Identifier(TypedDict):
    type: str
    '\n    Identifier kind, e.g. `domain`, `bundle_id`.\n    '
    value: str
    '\n    The identifier itself.\n    '

class DeclareProperty(TypedDict):
    domain: str
    '\n    A publisher domain already declared here.\n    '
    propertyId: NotRequired[str]
    "\n    The publisher's own property id, when known. The best identity to give.\n    "
    propertyType: NotRequired[Literal['website', 'mobile_app', 'ctv_app', 'desktop_app', 'dooh', 'podcast', 'radio', 'streaming_audio']]
    '\n    What kind of inventory this is.\n    '
    name: NotRequired[str]
    '\n    The property as the seller names it, e.g. `The Verge`.\n    '
    identifiers: NotRequired[list[Identifier]]
    '\n    Typed identifiers: site domain, app bundle id, store id.\n    '
    tags: NotRequired[list[Tag]]
    "\n    The publisher's property tags, when known.\n    "

class RemoveProperty(TypedDict):
    domain: str
    '\n    The publisher domain the property sits under.\n    '
    propertyKey: str
    '\n    The roster `propertyKey`. Read it from `get`, do not guess.\n    '

class SaveCoverageInput(TypedDict):
    domains: NotRequired[list[Domain]]
    '\n    The complete set. Anything omitted is removed — prefer `add`/`remove` for small edits.\n    '
    add: NotRequired[list[AddItem]]
    '\n    Domains to declare, leaving others untouched. Max 20 edits per call, all fields combined.\n    '
    remove: NotRequired[list[RemoveItem]]
    '\n    Domains to un-declare. One we crawled reports a conflict, not a removal.\n    '
    declareProperties: NotRequired[list[DeclareProperty]]
    '\n    Properties the seller claims, before the publisher declares them.\n    '
    removeProperties: NotRequired[list[RemoveProperty]]
    '\n    Claims to retract. A publisher-origin property cannot be removed here.\n    '

class SaveCoverageResult1(TypedDict):
    changed: bool
    added: SaveCoverageSuccessAdded
    removed: SaveCoverageSuccessRemoved

class SaveCoverageResult2(TypedDict):
    changed: bool
    declared: SaveCoverageSuccessDeclared
    removed: SaveCoverageSuccessRemoved
    failures: SaveCoverageSuccessFailures
SaveCoverageResult: TypeAlias = SaveCoverageResult1 | SaveCoverageResult2
SaveCoverageError: TypeAlias = V3ToolErrorResponse
RelatedDomain: TypeAlias = str
IncludePattern: TypeAlias = str
ExcludePattern: TypeAlias = str
Vertical: TypeAlias = str
Market: TypeAlias = str
Locale: TypeAlias = str
Channel: TypeAlias = str
Format: TypeAlias = str
PropertyRef: TypeAlias = str

class Metadata(TypedDict):
    """
    Metadata fields; relevance is read-only.
    """
    displayName: NotRequired[str]
    '\n    Material displayName field.\n    '
    documentType: NotRequired[Literal['rate_card']]
    '\n    Typed rate-card Library document.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet'] | None]
    '\n    Seller-governed Library document purpose. Omitted or null values are treated as uncategorized.\n    '
    visibility: NotRequired[SaveMaterialRequestMetadataVisibility]
    '\n    Material visibility field.\n    '
    advertiserRef: NotRequired[str]
    '\n    Material advertiserRef field.\n    '
    verticals: NotRequired[list[Vertical]]
    '\n    Material verticals field.\n    '
    markets: NotRequired[list[Market]]
    '\n    Material markets field.\n    '
    locales: NotRequired[list[Locale]]
    '\n    Material locales field.\n    '
    channels: NotRequired[list[Channel]]
    '\n    Material channels field.\n    '
    formats: NotRequired[list[Format]]
    '\n    Material formats field.\n    '
    propertyRefs: NotRequired[list[PropertyRef]]
    '\n    Material propertyRefs field.\n    '
    historicalClientRef: NotRequired[str]
    '\n    Material historicalClientRef field.\n    '
    effectiveFrom: NotRequired[str]
    '\n    Material effectiveFrom field.\n    '
    expiresAt: NotRequired[str]
    '\n    Material expiresAt field.\n    '

class Metadata1(TypedDict):
    """
    Metadata fields; relevance is read-only.
    """
    displayName: NotRequired[str]
    '\n    Material displayName field.\n    '
    documentType: NotRequired[Literal['rate_card']]
    '\n    Typed rate-card Library document.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet'] | None]
    '\n    Seller-governed Library document purpose. Omitted or null values are treated as uncategorized.\n    '
    visibility: NotRequired[SaveMaterialRequestMetadataVisibility]
    '\n    Material visibility field.\n    '
    advertiserRef: NotRequired[str]
    '\n    Material advertiserRef field.\n    '
    verticals: NotRequired[list[Vertical]]
    '\n    Material verticals field.\n    '
    markets: NotRequired[list[Market]]
    '\n    Material markets field.\n    '
    locales: NotRequired[list[Locale]]
    '\n    Material locales field.\n    '
    channels: NotRequired[list[Channel]]
    '\n    Material channels field.\n    '
    formats: NotRequired[list[Format]]
    '\n    Material formats field.\n    '
    propertyRefs: NotRequired[list[PropertyRef]]
    '\n    Material propertyRefs field.\n    '
    historicalClientRef: NotRequired[str]
    '\n    Material historicalClientRef field.\n    '
    effectiveFrom: NotRequired[str]
    '\n    Material effectiveFrom field.\n    '
    expiresAt: NotRequired[str]
    '\n    Material expiresAt field.\n    '

class Metadata2(TypedDict):
    """
    Metadata fields; relevance is read-only.
    """
    displayName: NotRequired[str]
    '\n    Material displayName field.\n    '
    documentType: NotRequired[Literal['rate_card']]
    '\n    Typed rate-card Library document.\n    '
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet'] | None]
    '\n    Seller-governed Library document purpose. Omitted or null values are treated as uncategorized.\n    '
    visibility: NotRequired[SaveMaterialRequestMetadataVisibility]
    '\n    Material visibility field.\n    '
    advertiserRef: NotRequired[str]
    '\n    Material advertiserRef field.\n    '
    verticals: NotRequired[list[Vertical]]
    '\n    Material verticals field.\n    '
    markets: NotRequired[list[Market]]
    '\n    Material markets field.\n    '
    locales: NotRequired[list[Locale]]
    '\n    Material locales field.\n    '
    channels: NotRequired[list[Channel]]
    '\n    Material channels field.\n    '
    formats: NotRequired[list[Format]]
    '\n    Material formats field.\n    '
    propertyRefs: NotRequired[list[PropertyRef]]
    '\n    Material propertyRefs field.\n    '
    historicalClientRef: NotRequired[str]
    '\n    Material historicalClientRef field.\n    '
    effectiveFrom: NotRequired[str]
    '\n    Material effectiveFrom field.\n    '
    expiresAt: NotRequired[str]
    '\n    Material expiresAt field.\n    '

class SaveMaterialInput3(TypedDict):
    action: Literal['update_metadata']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '
    expectedRevision: int
    '\n    Current source revision required before replacing or editing.\n    '
    metadata: Metadata2
    '\n    Metadata fields; relevance is read-only.\n    '
    labels: NotRequired[dict[str, list[Label]]]
    '\n    Replace labels for each supplied dimension; [] clears.\n    '

class SaveMaterialInput4(TypedDict):
    action: Literal['reprocess']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '
    sourceRevision: int
    "\n    The `sourceRevision` of the Material revision that contains this candidate, exactly as returned with the candidate. Send that revision, not the Material's current revision; a different revision returns a mismatched-candidate error.\n    "
    clientRequestId: str
    '\n    Idempotency key for create/replace or candidate decision.\n    '

class CorrectedContent(TypedDict):
    """
    Replacement proposedContent for this candidate.
    """
    title: str
    '\n    Corrected candidate title to show on get(material).\n    '
    summary: str
    '\n    Corrected candidate body to show on get(material).\n    '
    sourceTextDigest: NotRequired[SaveMaterialRequestDecisionCorrectionCorrectedContentSourceTextDigest]
    '\n    Optional digest of the corrected source text.\n    '

class ProposedMutation(TypedDict):
    """
    Replacement typed proposal; correction does not confirm or save it.
    """
    tool: Literal['save_playbook', 'save_business_rules', 'save_wholesale_product', 'save_signal', 'save_seller']
    '\n    Material tool field.\n    '
    arguments: dict[str, JsonValue]
    '\n    Material arguments field.\n    '

class Correction(TypedDict):
    """
    Required for correct; supplies usable replacement text.
    """
    correctedContent: NotRequired[CorrectedContent]
    '\n    Replacement proposedContent for this candidate.\n    '
    proposedMutation: NotRequired[ProposedMutation]
    '\n    Replacement typed proposal; correction does not confirm or save it.\n    '

class Decision(TypedDict):
    """
    Accept, reject, correct, or withdraw one candidate.
    """
    action: Literal['accept', 'reject', 'correct', 'withdraw']
    '\n    Material action field.\n    '
    correction: NotRequired[Correction]
    '\n    Required for correct; supplies usable replacement text.\n    '

class SaveMaterialInput5(TypedDict):
    action: Literal['decide_candidate']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '
    sourceRevision: int
    "\n    The `sourceRevision` of the Material revision that contains this candidate, exactly as returned with the candidate. Send that revision, not the Material's current revision; a different revision returns a mismatched-candidate error.\n    "
    candidateId: str
    '\n    Material-owned candidate id from get(material).\n    '
    decision: Decision
    '\n    Accept, reject, correct, or withdraw one candidate.\n    '
    clientRequestId: NotRequired[str]
    '\n    Idempotency key for create/replace or candidate decision.\n    '

class SaveMaterialInput6(TypedDict):
    action: Literal['reconcile_candidate']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    applicationId: str
    '\n    Candidate application id from materialPartialReceipt or reconciliation guidance.\n    '

class SaveMaterialInput7(TypedDict):
    action: Literal['mark_reusable']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '
    unitId: str
    '\n    Unit ID for mark_reusable.\n    '
    reusable: bool
    '\n    Whether this unit may be reused.\n    '

class SaveMaterialInput8(TypedDict):
    action: Literal['archive']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '

class SaveMaterialInput9(TypedDict):
    action: Literal['restore']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '

class SaveMaterialInput10(TypedDict):
    action: Literal['preview_rate_card']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '
    sourceRevision: int
    "\n    The `sourceRevision` of the Material revision that contains this candidate, exactly as returned with the candidate. Send that revision, not the Material's current revision; a different revision returns a mismatched-candidate error.\n    "

class SaveMaterialInput11(TypedDict):
    action: Literal['commit_rate_card']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '
    sourceRevision: int
    "\n    The `sourceRevision` of the Material revision that contains this candidate, exactly as returned with the candidate. Send that revision, not the Material's current revision; a different revision returns a mismatched-candidate error.\n    "
    previewToken: str
    '\n    Short-lived exact rate-card preview token required to commit parsed rows.\n    '

class Arguments3(TypedDict):
    kind: Literal['material']
    id: str

class Next(TypedDict):
    tool: Literal['get']
    arguments: Arguments3

class SaveMaterialResult1(TypedDict):
    materialId: str
    sourceRevision: int
    processingState: str
    idempotentReplay: bool
    next: Next

class SaveMaterialResult2(TypedDict):
    materialId: str
    unitId: str
    reusable: bool

class SaveMaterialResult3(TypedDict):
    materialId: str
    sourceRevision: int
    processingState: str
    archivedAt: str | None

class SaveMaterialResult4(TypedDict):
    action: Literal['committed_rate_card']
    committed: Literal[True]
    materialId: str
    sourceRevision: int
    addedTotal: int
    updatedTotal: int
    removedTotal: int
    facts: list[SaveMaterialSuccessFactsItem]
    factsTotal: int
    factsTruncated: bool

class Next1(TypedDict):
    tool: Literal['get']
    arguments: Arguments3

class SaveMaterialResult7(TypedDict):
    action: Literal['reconciled']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveMaterialSuccessMaterialReceipt
SaveMaterialError: TypeAlias = V3ToolErrorResponse

class FormatOption(TypedDict):
    formatOptionId: NotRequired[str]
    '\n    Stable id in the publisher catalog. Required when publisherDomain is present.\n    '
    publisherDomain: NotRequired[str]
    '\n    Publisher catalog namespace for formatOptionId. Omit for a product-local format.\n    '
    formatKind: Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']
    '\n    Canonical AdCP creative format kind.\n    '
    params: dict[str, JsonValue]
    '\n    Canonical constraints. Publisher formats must equal or narrow the catalog declaration.\n    '

class PricingOption(TypedDict):
    isFixed: NotRequired[bool]
    '\n    True to charge your rate; omit for auction.\n    '
    rate: NotRequired[float]
    '\n    CPM to charge. Required with isFixed.\n    '
    currency: NotRequired[str]
    '\n    ISO-4217; must be your settlement currency.\n    '
    deliveryType: Literal['guaranteed', 'non_guaranteed']
    "\n    Required. This option's own delivery type, not the product's.\n    "

class SaveWholesaleProductInput(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    '\n    Exact get(material) provenance; include only to confirm that candidate.\n    '
    sourceId: str
    '\n    The inventory source that holds the product, as returned by `search`. Not an ESA connection id.\n    '
    id: NotRequired[str]
    '\n    The wholesale product to change. Omit to create a new one. Only the fields you pass are changed.\n    '
    name: NotRequired[str]
    '\n    Buyer-facing product name.\n    '
    description: NotRequired[str]
    '\n    Buyer-facing description.\n    '
    status: NotRequired[Literal['draft', 'active', 'archived']]
    '\n    `draft` is hidden from buyers. `active` is discoverable and buyable. `archived` is off the market.\n    '
    deliveryType: NotRequired[str]
    '\n    Delivery type the source recognises, e.g. guaranteed.\n    '
    channels: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence', 'audio', 'video']]]
    '\n    Media channels; omit keeps them, [] clears for inference.\n    '
    inventory: NotRequired[dict[str, JsonValue]]
    "\n    The ad-server selectors to sell, in the source's own shape. Required to create.\n    "
    formatOptions: NotRequired[list[FormatOption]]
    '\n    Canonical format: formatKind and params; publisher entries need publisherDomain and formatOptionId.\n    '
    pricingOptions: NotRequired[list[PricingOption]]
    '\n    Price offers. A fixed rate is a complete price; omitting yields an auction with no floor.\n    '
    dryRun: NotRequired[bool]
    '\n    Validate a new product and report findings without writing it. Creates only.\n    '
    delete: NotRequired[Literal[True]]
    '\n    Permanently remove this product — only once it is archived, and it cannot be undone.\n    '
    confirmName: NotRequired[str]
    "\n    The product's exact stored name, read back to confirm you hold the right one.\n    "
    prebidIntegrationActive: NotRequired[bool]
    "\n    Declare that the Scope3 Prebid module runs on this product's inventory. Set true only if installed.\n    "

class SaveWholesaleProductResult1(TypedDict):
    saved: Literal[True]
    created: bool
    sourceId: str
    id: NotRequired[str]
    status: str
    pricingStatus: str | None
    warnings: list[SaveWholesaleProductSuccessWarningsItem]

class SaveWholesaleProductResult2(TypedDict):
    saved: Literal[True]
    deleted: Literal[True]
    action: Literal['deleted']
    sourceId: str
    id: str
    name: str
    previousStatus: str

class SaveWholesaleProductResult3(TypedDict):
    saved: Literal[False]
    deleted: Literal[False]
    sourceId: str
    id: str
    action: Literal['unchanged']

class SaveWholesaleProductResult4(TypedDict):
    saved: Literal[False]
    deleted: Literal[False]
    sourceId: str
    id: str
    refused: str

class SaveWholesaleProductResult5(TypedDict):
    saved: Literal[False]
    refused: Literal['validation_failed']
    sourceId: str
    errors: list[SaveWholesaleProductSuccessErrorsItem]
    warnings: list[SaveWholesaleProductSuccessWarningsItem]

class SaveWholesaleProductResult6(TypedDict):
    saved: Literal[False]
    dryRun: Literal[True]
    valid: Literal[True]
    sourceId: str
    warnings: list[SaveWholesaleProductSuccessWarningsItem]

class SaveWholesaleProductResult7(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SaveWholesaleProductSuccessMaterialReceipt

class SaveWholesaleProductResult8(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveWholesaleProductSuccessMaterialReceipt
SaveWholesaleProductResult: TypeAlias = SaveWholesaleProductResult1 | SaveWholesaleProductResult2 | SaveWholesaleProductResult3 | SaveWholesaleProductResult4 | SaveWholesaleProductResult5 | SaveWholesaleProductResult6 | SaveWholesaleProductResult7 | SaveWholesaleProductResult8
SaveWholesaleProductError: TypeAlias = V3ToolErrorResponse
Region: TypeAlias = str
EvidenceUrl: TypeAlias = str

class SaveMediaKitInput(TypedDict):
    summary: NotRequired[str]
    "\n    Deprecated legacy Business Profile summary; use save_seller's listing field for the description.\n    "
    propertyCount: NotRequired[int]
    '\n    Deprecated legacy Business Profile count of owned properties or domains.\n    '
    channels: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence', 'audio', 'video']]]
    "\n    Legacy channels; use save_seller's listing field for coverage.\n    "
    regions: NotRequired[list[Region]]
    "\n    Legacy regions; use save_seller's listing field for countries.\n    "
    verticals: NotRequired[list[Vertical]]
    '\n    Deprecated legacy Business Profile topic or vertical focus areas.\n    '
    evidenceUrls: NotRequired[list[EvidenceUrl]]
    '\n    Deprecated legacy Business Profile HTTP(S) media-kit or about-page evidence URLs.\n    '
    notes: NotRequired[str]
    '\n    Deprecated legacy Business Profile notes that do not fit its structured fields.\n    '

class Replacement(TypedDict):
    tool: Literal['save_seller']
    projection: Literal['listing']

class SaveMediaKitResult(TypedDict):
    mediaKit: dict[str, JsonValue]
    deprecated: Literal[True]
    replacement: Replacement
SaveMediaKitError: TypeAlias = V3ToolErrorResponse
CreativeTerm: TypeAlias = str
PublisherDomain: TypeAlias = str
Country: TypeAlias = str
AdvertiserVertical: TypeAlias = str
SeasonalityItem: TypeAlias = str
SignalTag: TypeAlias = str
PlacementTag: TypeAlias = str

class FormatDimension(TypedDict):
    width: int
    '\n    Pixel width.\n    '
    height: int
    '\n    Pixel height.\n    '

class Hints(TypedDict):
    """
    Preserve constraints returned by get(playbook) when replacing all facts.
    """
    channels: NotRequired[list[Channel]]
    '\n    AdCP channel codes; any listed code may match.\n    '
    creativeTerms: NotRequired[list[CreativeTerm]]
    '\n    Creative terms; any listed value may match.\n    '
    publisherDomains: NotRequired[list[PublisherDomain]]
    '\n    Publisher domains; any listed value may match.\n    '
    countries: NotRequired[list[Country]]
    '\n    ISO country codes; any listed value may match.\n    '
    advertiserVerticals: NotRequired[list[AdvertiserVertical]]
    '\n    Advertiser verticals; any listed value may match.\n    '
    seasonality: NotRequired[list[SeasonalityItem]]
    '\n    Seasonal terms; any listed value may match.\n    '
    signalTags: NotRequired[list[SignalTag]]
    '\n    Signal tags; any listed value may match.\n    '
    placementTags: NotRequired[list[PlacementTag]]
    '\n    Placement tags; any listed value may match.\n    '
    formatDimensions: NotRequired[list[FormatDimension]]
    '\n    Pixel sizes admitted by a selected canonical format option.\n    '

class Fact(TypedDict):
    id: str
    '\n    Stable id. Reuse to edit; a new id adds a fact.\n    '
    label: str
    '\n    Short display label.\n    '
    appliesWhen: str
    '\n    Natural-language applicability condition.\n    '
    hints: NotRequired[Hints]
    '\n    Preserve constraints returned by get(playbook) when replacing all facts.\n    '
    pricingModel: NotRequired[Literal['cpm', 'vcpm', 'cpc', 'cpcv', 'cpv', 'cpp', 'cpa', 'revenue_share', 'flat_rate', 'time']]
    '\n    AdCP pricing model this fact anchors.\n    '
    currency: NotRequired[str]
    '\n    ISO 4217 currency. Falls back to `pricing.currency`.\n    '
    targetPrice: NotRequired[float]
    '\n    Preferred value price. Give this or floorPrice.\n    '
    floorPrice: NotRequired[float]
    '\n    Hard minimum price when this fact applies.\n    '
    ceilingPrice: NotRequired[float]
    '\n    Optional maximum price when this fact applies.\n    '
    strength: NotRequired[Literal['hard_floor', 'default', 'guidance']]
    '\n    hard_floor must not be undercut; default is preferred; guidance is advisory.\n    '
    provenance: NotRequired[str]
    '\n    Where this fact came from, e.g. a rate-card page.\n    '
    notes: NotRequired[str]
    '\n    Rationale or caveats for operators.\n    '

class Pricing(TypedDict):
    """
    Replaces the whole fact list. Omit to leave pricing as-is.
    """
    currency: NotRequired[str]
    '\n    Default ISO 4217 currency for facts that omit one.\n    '
    facts: NotRequired[list[Fact]]
    '\n    The complete fact list — anything omitted is removed.\n    '

class Rule(TypedDict):
    houseDomain: str
    '\n    Buyer domain the rule keys to, e.g. nike.com. Covers its family.\n    '
    scope: Literal['brand', 'operator']
    "\n    brand: the buy's advertiser brand. operator: its buying agency.\n    "
    discountPercent: float
    '\n    Percent off the quote, 0-100. Never priced below wholesale cost.\n    '
    notes: NotRequired[str | None]
    '\n    Operator note. Omit to keep the current note; null clears it.\n    '

class RemoveItem1(TypedDict):
    houseDomain: SavePlaybookRequestDiscountsRemoveItemHouseDomain
    '\n    Domain of the rule to remove, exactly as it is stored.\n    '
    scope: Literal['brand', 'operator']
    "\n    brand: the buy's advertiser brand. operator: its buying agency.\n    "

class Discounts(TypedDict):
    """
    Brand/operator rate-card discounts. Per-rule, not whole-list.
    """
    rules: NotRequired[list[Rule]]
    '\n    Rules to set. Keyed by domain+scope; unmentioned rules are untouched.\n    '
    remove: NotRequired[list[RemoveItem1]]
    '\n    Rules to delete. Name the domain and scope of each.\n    '

class SavePlaybookInput(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    '\n    Exact get(material) provenance; include only to confirm that candidate.\n    '
    content: NotRequired[str]
    '\n    Markdown: posture, packaging, selection guidance. Creates a new active version. Live immediately.\n    '
    notes: NotRequired[str]
    '\n    Why this version was written. Version history only.\n    '
    pricing: NotRequired[Pricing]
    '\n    Replaces the whole fact list. Omit to leave pricing as-is.\n    '
    discounts: NotRequired[Discounts]
    '\n    Brand/operator rate-card discounts. Per-rule, not whole-list.\n    '

class SavePlaybookResult1(TypedDict):
    playbook: SavePlaybookSuccessPlaybook
    createdVersion: NotRequired[float]
    replacedVersion: NotRequired[float | None]

class SavePlaybookResult2(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SavePlaybookSuccessMaterialReceipt

class SavePlaybookResult3(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SavePlaybookSuccessMaterialReceipt
SavePlaybookResult: TypeAlias = SavePlaybookResult1 | SavePlaybookResult2 | SavePlaybookResult3
SavePlaybookError: TypeAlias = V3ToolErrorResponse

class SaveBusinessRulesInput1(TypedDict):
    pass

class SaveBusinessRulesInput3(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    '\n    Exact get(material) provenance; include only to confirm that candidate.\n    '
    content: NotRequired[str]
    '\n    Compatibility input for already-sectioned Markdown. Prefer the two explicit policy fields.\n    '
    briefAcceptancePolicy: NotRequired[str]
    '\n    Brief rules for discovery and manual-buy screening. Always pair with creativePolicy; empty clears.\n    '
    creativePolicy: NotRequired[str]
    '\n    Submitted-creative rules. Always pair with briefAcceptancePolicy; empty clears.\n    '
    notes: NotRequired[str]
    '\n    Why this version was written. Version history only.\n    '
    creativeApproval: NotRequired[Literal['auto', 'manual']]
    '\n    auto approves creatives with no review; manual queues them.\n    '
    mediaBuyApproval: NotRequired[Literal['auto', 'manual']]
    '\n    auto skips the create evaluator and human queue; manual evaluates and queues exceptions.\n    '
    acknowledgeNoHumanReview: NotRequired[bool]
    '\n    Required to move either approval to auto. Confirms nobody will review those.\n    '
    advertisingPolicyDisclosure: NotRequired[list[Literal['brief_acceptance', 'creative_policy']]]
    '\n    Policy sections to show buyers on the listing. Empty hides them.\n    '

class SaveBusinessRulesInput4(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    content: NotRequired[str]
    briefAcceptancePolicy: NotRequired[str]
    creativePolicy: NotRequired[str]
    notes: NotRequired[str]
    creativeApproval: NotRequired[Literal['auto', 'manual']]
    mediaBuyApproval: NotRequired[Literal['auto', 'manual']]
    acknowledgeNoHumanReview: NotRequired[bool]
    advertisingPolicyDisclosure: NotRequired[list[Literal['brief_acceptance', 'creative_policy']]]

class SaveBusinessRulesInput5(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    content: NotRequired[str]
    briefAcceptancePolicy: NotRequired[str]
    creativePolicy: NotRequired[str]
    notes: NotRequired[str]
    creativeApproval: NotRequired[Literal['auto', 'manual']]
    mediaBuyApproval: NotRequired[Literal['auto', 'manual']]
    acknowledgeNoHumanReview: NotRequired[bool]
    advertisingPolicyDisclosure: NotRequired[list[Literal['brief_acceptance', 'creative_policy']]]
SaveBusinessRulesInput: TypeAlias = SaveBusinessRulesInput4 | SaveBusinessRulesInput5

class SaveBusinessRulesResult1(TypedDict):
    businessRules: SaveBusinessRulesSuccessBusinessRules
    createdVersion: NotRequired[float]
    replacedVersion: NotRequired[float | None]

class SaveBusinessRulesResult2(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SaveBusinessRulesSuccessMaterialReceipt

class SaveBusinessRulesResult3(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveBusinessRulesSuccessMaterialReceipt
SaveBusinessRulesResult: TypeAlias = SaveBusinessRulesResult1 | SaveBusinessRulesResult2 | SaveBusinessRulesResult3
SaveBusinessRulesError: TypeAlias = V3ToolErrorResponse

class SaveAdvertiserInstructionsInput(TypedDict):
    id: NotRequired[str]
    '\n    Existing instruction row id; omit when using the exact pair.\n    '
    operatorDomain: NotRequired[SaveAdvertiserInstructionsRequestOperatorDomain | None]
    '\n    Buying operator domain in the exact pair.\n    '
    brandDomain: NotRequired[SaveAdvertiserInstructionsRequestBrandDomain | None]
    '\n    Advertised brand domain in the exact pair.\n    '
    discountPercent: NotRequired[float | None]
    '\n    Exact-pair discount instruction; effective value is read-only.\n    '
    notes: NotRequired[str | None]
    '\n    Seller notes or instructions for this exact pair.\n    '
    countries: NotRequired[list[Country] | None]
    '\n    Optional uppercase country scope for the exact pair.\n    '

class SaveAdvertiserInstructionsResult1(TypedDict):
    action: Literal['created', 'updated', 'unchanged']
    object: dict[str, JsonValue]

class SaveAdvertiserInstructionsResult2(TypedDict):
    action: Literal['created']
    warning: Literal['created_but_readback_unavailable']
    readback: Literal['unavailable']
    id: NotRequired[str]
    pair: NotRequired[str]

class SaveAdvertiserInstructionsResult3(TypedDict):
    action: Literal['updated']
    warning: Literal['updated_but_readback_unavailable']
    readback: Literal['unavailable']
    id: NotRequired[str]
    pair: NotRequired[str]
SaveAdvertiserInstructionsResult: TypeAlias = SaveAdvertiserInstructionsResult1 | SaveAdvertiserInstructionsResult2 | SaveAdvertiserInstructionsResult3
SaveAdvertiserInstructionsError: TypeAlias = V3ToolErrorResponse

class SaveSignalInput1(TypedDict):
    state: Literal['archived']

class SaveSignalInput2(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    '\n    Exact get(material) provenance; include only to confirm that candidate.\n    '
    sourceId: NotRequired[str]
    '\n    Ad-server source that owns it. Omit to write a seller-catalog signal.\n    '
    id: NotRequired[str]
    '\n    Existing signal id; omit to create.\n    '
    draft: NotRequired[dict[str, JsonValue]]
    '\n    Signal. Managed writes fully replace; include signalId, name, valueType, and adapterConfig.\n    '
    state: NotRequired[Literal['active', 'archived']]
    '\n    Use archived to delete an existing signal.\n    '
    confirmArchiveCascade: NotRequired[bool]
    '\n    Required to archive a catalog signal: it also archives targeting profiles using it.\n    '

class SaveSignalInput3(TypedDict):
    state: NotRequired[Literal['active', 'archived']]
    materialCandidate: NotRequired[MaterialCandidate]
    sourceId: NotRequired[str]
    id: NotRequired[str]
    draft: NotRequired[dict[str, JsonValue]]
    confirmArchiveCascade: NotRequired[bool]
SaveSignalInput: TypeAlias = SaveSignalInput3

class SaveSignalResult1(TypedDict):
    action: Literal['created', 'updated', 'deleted', 'unchanged']
    object: SaveSignalSuccessObject

class SaveSignalResult2(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SaveSignalSuccessMaterialReceipt

class SaveSignalResult3(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveSignalSuccessMaterialReceipt
SaveSignalResult: TypeAlias = SaveSignalResult1 | SaveSignalResult2 | SaveSignalResult3
SaveSignalError: TypeAlias = V3ToolErrorResponse

class SaveWorkItemInput(TypedDict):
    kind: Literal['creative_review', 'media_buy_approval', 'modular_source']
    '\n    Workstream owning this item.\n    '
    id: str
    '\n    Work-item identifier from search or get.\n    '
    sourceId: NotRequired[str]
    '\n    Required for `modular_source`; copy it from search.\n    '
    status: Literal['approved', 'rejected', 'completed']
    '\n    Desired terminal state for this kind.\n    '
    reviewerNotes: NotRequired[str]
    '\n    Optional note preserved with the decision.\n    '
    expectedContentDigest: NotRequired[str]
    '\n    Required for `creative_review`; copy contentDigest from the exact search or get result.\n    '
    result: NotRequired[dict[str, JsonValue]]
    '\n    Modular completion fields named by requiredResultFields. Never secrets.\n    '

class ActionEvidence(TypedDict):
    basis: Literal['unproven']
    reason: str

class SaveWorkItemResult(TypedDict):
    action: Literal['created', 'unchanged']
    object: dict[str, JsonValue]
    actionEvidence: NotRequired[ActionEvidence]
SaveWorkItemError: TypeAlias = V3ToolErrorResponse

class Preset(TypedDict):
    """
    Preset data.
    """
    buyer: NotRequired[SaveRfpRequestP]
    '\n    Stable buyer segment or buyer name.\n    '
    advertiser: NotRequired[SaveRfpRequestP]
    '\n    Stable advertiser or brand segment.\n    '
    category: NotRequired[SaveRfpRequestP]
    '\n    Commercial category.\n    '
    location: NotRequired[SaveRfpRequestP]
    '\n    Geographic location.\n    '
    market: NotRequired[SaveRfpRequestP]
    '\n    Commercial market.\n    '
    channels: NotRequired[list[Channel]]
    '\n    Normalized media channels.\n    '
    objective: NotRequired[SaveRfpRequestP]
    '\n    Campaign objective.\n    '
    advertiserClass: NotRequired[SaveRfpRequestP]
    '\n    Advertiser business class.\n    '
    budgetBand: NotRequired[SaveRfpRequestP]
    '\n    Stable planning budget band, never exact budget.\n    '

class Budget1(TypedDict):
    """
    Budget.
    """
    amount: NotRequired[float]
    '\n    Minor unit.\n    '
    currency: NotRequired[str]
    '\n    Currency group.\n    '

class Strategy(TypedDict):
    """
    Strategy.
    """
    posture: NotRequired[SaveRfpRequestStrategyPosture]
    '\n    Posture.\n    '
    passReason: NotRequired[SaveRfpRequestP]
    '\n    Pass reason.\n    '
    pass_reason: NotRequired[SaveRfpRequestP]
    '\n    Pass-reason alias.\n    '

class RequiredLibraryUnitId(TypedDict):
    materialId: SaveRfpRequestI
    '\n    Material id.\n    '
    unitId: SaveRfpRequestI
    '\n    Unit id.\n    '
    renditionRevision: int
    '\n    Rendition revision.\n    '

class SaveRfpInput3(TypedDict):
    action: Literal['record_feedback']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    turnId: SaveRfpRequestI
    '\n    Turn id.\n    '
    feedback: dict[SaveRfpRequestK, SaveRfpRequestJ]
    '\n    Feedback.\n    '
    grade: NotRequired[Literal['A', 'B', 'C', 'D', 'F']]
    '\n    Seller grade.\n    '
    ledBy: NotRequired[Literal['agent', 'human']]
    '\n    Who led the response.\n    '
    commentary: NotRequired[SaveRfpRequestP]
    '\n    Seller commentary.\n    '

class SaveRfpInput4(TypedDict):
    action: Literal['record_feedback']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    turnId: SaveRfpRequestI
    '\n    Turn id.\n    '
    feedback: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    '\n    Feedback.\n    '
    grade: Literal['A', 'B', 'C', 'D', 'F']
    '\n    Seller grade.\n    '
    ledBy: NotRequired[Literal['agent', 'human']]
    '\n    Who led the response.\n    '
    commentary: NotRequired[SaveRfpRequestP]
    '\n    Seller commentary.\n    '

class SaveRfpInput5(TypedDict):
    action: Literal['record_feedback']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    turnId: SaveRfpRequestI
    '\n    Turn id.\n    '
    feedback: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    '\n    Feedback.\n    '
    grade: NotRequired[Literal['A', 'B', 'C', 'D', 'F']]
    '\n    Seller grade.\n    '
    ledBy: Literal['agent', 'human']
    '\n    Who led the response.\n    '
    commentary: NotRequired[SaveRfpRequestP]
    '\n    Seller commentary.\n    '

class SaveRfpInput6(TypedDict):
    action: Literal['record_feedback']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    turnId: SaveRfpRequestI
    '\n    Turn id.\n    '
    feedback: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    '\n    Feedback.\n    '
    grade: NotRequired[Literal['A', 'B', 'C', 'D', 'F']]
    '\n    Seller grade.\n    '
    ledBy: NotRequired[Literal['agent', 'human']]
    '\n    Who led the response.\n    '
    commentary: SaveRfpRequestP
    '\n    Seller commentary.\n    '

class Representation(TypedDict):
    """
    Representation.
    """
    format: Literal['seller_response_json', 'buyer_proposal_json', 'semantic_document_json', 'html', 'pdf', 'pptx']
    '\n    Format.\n    '
    renderProfile: NotRequired[Literal['seller_proposal_v1']]
    '\n    Renderer profile.\n    '
    locale: NotRequired[SaveRfpRequestRepresentationLocale]
    '\n    BCP-47 locale.\n    '
    audience: NotRequired[Literal['seller_preview', 'buyer_delivery']]
    '\n    Audience: buyer_delivery (default; no seller notes) or seller_preview.\n    '

class SaveRfpInput7(TypedDict):
    action: Literal['request_representation']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    turnId: SaveRfpRequestI
    '\n    Turn id.\n    '
    representation: Representation
    '\n    Representation.\n    '

class SaveRfpInput8(TypedDict):
    action: Literal['cancel_representation']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    turnId: SaveRfpRequestI
    '\n    Turn id.\n    '
    representationId: SaveRfpRequestI
    '\n    Cancel ID.\n    '

class SaveRfpInput9(TypedDict):
    action: Literal['release_turn']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    turnId: SaveRfpRequestI
    '\n    Turn id.\n    '

class Outcome(TypedDict):
    """
    Outcome
    """
    result: NotRequired[SaveRfpRequestP]
    '\n    Result.\n    '
    finality: NotRequired[Literal['preliminary', 'final', 'mixed']]
    '\n    Finality.\n    '
    details: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    '\n    Details.\n    '

class SaveRfpInput10(TypedDict):
    action: Literal['record_outcome']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    turnId: SaveRfpRequestI
    '\n    Turn id.\n    '
    outcome: Outcome
    '\n    Outcome\n    '

class SaveRfpInput11(TypedDict):
    action: Literal['attach_response']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    materialId: SaveRfpRequestI
    '\n    Response material id.\n    '

class SaveRfpInput12(TypedDict):
    action: Literal['endorse']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    commentary: NotRequired[SaveRfpRequestP]
    '\n    Seller commentary.\n    '

class SaveRfpInput13(TypedDict):
    action: Literal['unendorse']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '

class SaveRfpResult1(TypedDict):
    rfpId: SaveRfpSuccessRfpId
    turnId: SaveRfpSuccessTurnId
    idempotentReplay: SaveRfpSuccessIdempotentReplay
    turnNumber: int
    responseState: str
    next: SaveRfpSuccessNextRfpTurn

class SaveRfpResult2(TypedDict):
    rfpId: SaveRfpSuccessRfpId
    turnId: SaveRfpSuccessTurnId
    idempotentReplay: SaveRfpSuccessIdempotentReplay
    clientRequestId: str
    feedbackId: str
    next: SaveRfpSuccessNextRfpTurn

class SaveRfpResult3(TypedDict):
    rfpId: SaveRfpSuccessRfpId
    turnId: SaveRfpSuccessTurnId
    idempotentReplay: SaveRfpSuccessIdempotentReplay
    pairId: str
    paired: Literal[True]
    endorsed: bool
    responseKind: Literal['turn', 'material']
    clientRequestId: str
    next: SaveRfpSuccessNextRfp

class SaveRfpResult4(TypedDict):
    rfpId: SaveRfpSuccessRfpId
    turnId: SaveRfpSuccessTurnId
    idempotentReplay: SaveRfpSuccessIdempotentReplay
    released: Literal[True]
    next: SaveRfpSuccessNextRfp

class SaveRfpResult5(TypedDict):
    rfpId: SaveRfpSuccessRfpId
    turnId: SaveRfpSuccessTurnId
    idempotentReplay: SaveRfpSuccessIdempotentReplay
    clientRequestId: str
    representationId: str
    representationState: Literal['queued', 'processing', 'ready', 'failed', 'canceled']
    next: SaveRfpSuccessNextRfpTurn

class SaveRfpResult6(TypedDict):
    rfpId: SaveRfpSuccessRfpId
    turnId: SaveRfpSuccessTurnId
    idempotentReplay: SaveRfpSuccessIdempotentReplay
    outcomeId: str
    next: SaveRfpSuccessNextRfpTurn
SaveRfpResult: TypeAlias = SaveRfpResult1 | SaveRfpResult2 | SaveRfpResult3 | SaveRfpResult4 | SaveRfpResult5 | SaveRfpResult6
SaveRfpError: TypeAlias = V3ToolErrorResponse

class CustomMacro(TypedDict):
    name: str
    '\n    Custom macro name in UPPER_SNAKE_CASE.\n    '
    paramKey: str
    '\n    URL parameter key populated by this macro.\n    '
    description: NotRequired[str]
    '\n    Human-readable purpose of this custom macro.\n    '

class MacroAddition(TypedDict):
    paramKey: str
    '\n    Query parameter key, for example utm_campaign.\n    '
    value: str | None
    '\n    Literal or canonical AdCP macro template such as {CAMPAIGN_ID}; null suppresses the inherited key.\n    '

class Tracker(TypedDict):
    trackerId: NotRequired[str]
    '\n    Stable tracker ID returned by a prior read. Omit when creating.\n    '
    name: str
    '\n    Human-readable tracker name.\n    '
    vendorName: NotRequired[str]
    '\n    Measurement or tracking vendor name.\n    '
    url: NotRequired[str]
    '\n    Raw vendor URL. Required on create; omit with trackerId on update to keep the stored URL.\n    '
    trackerType: Literal['impression', 'click', 'custom']
    '\n    Event that causes this tracker to fire.\n    '
    customEventName: NotRequired[str]
    '\n    Required when trackerType is custom.\n    '
    enabled: NotRequired[bool]
    '\n    Whether this tracker is enabled at its owning scope.\n    '
    gvlVendorId: NotRequired[int]
    '\n    IAB GVL vendor ID for TCF consent macro scoping (e.g. 550 for HappyDemics).\n    '
    sourceDialect: NotRequired[Literal['adcp', 'happydemics', 'gam', 'vast', 'custom']]
    '\n    Declare only when trusted context identifies the dialect; otherwise omit for exact-origin detection.\n    '

class Tracking(TypedDict):
    """
    Advertiser tracker defaults, macros, and URL parameters inherited by campaigns and creatives.
    """
    expectedRevision: NotRequired[int]
    '\n    Last-read tracking revision. Rejects concurrent tracking updates.\n    '
    enabledMacros: NotRequired[list[Literal['CAMPAIGN_ID', 'CREATIVE_ID', 'TRACKING_TAG_ID', 'DATA_SET_ID', 'TACTIC_ID', 'MEDIA_BUY_ID', 'SALES_AGENT_ID', 'ATTRIBUTION_TRACKING_ID', 'DEVICE_ID', 'DEVICE_ID_TYPE', 'CACHEBUSTER', 'GDPR', 'GDPR_CONSENT', 'US_PRIVACY', 'LIMIT_AD_TRACKING', 'DEVICE_TYPE', 'OS', 'OS_VERSION', 'DEVICE_MAKE', 'DEVICE_MODEL', 'APP_BUNDLE', 'APP_NAME', 'COUNTRY', 'REGION', 'CITY', 'ZIP', 'DMA', 'LAT', 'LONG', 'PLACEMENT_ID', 'FOLD_POSITION', 'AD_WIDTH', 'AD_HEIGHT', 'VIDEO_ID', 'VIDEO_TITLE', 'VIDEO_DURATION', 'VIDEO_CATEGORY', 'CONTENT_GENRE', 'CONTENT_RATING', 'PLAYER_WIDTH', 'PLAYER_HEIGHT', 'POD_POSITION', 'POD_SIZE', 'AD_BREAK_ID', 'AXEM', 'TIMESTAMP']]]
    '\n    System macros enabled for advertiser tracking.\n    '
    customMacros: NotRequired[list[CustomMacro]]
    '\n    Advertiser-defined custom macro declarations.\n    '
    macroAdditions: NotRequired[list[MacroAddition]]
    '\n    Default click-URL query parameters inherited by campaigns and creatives.\n    '
    impressionTrackerEnabled: NotRequired[bool]
    '\n    Whether impression tracking is enabled.\n    '
    clickTrackerEnabled: NotRequired[bool]
    '\n    Whether click tracking is enabled.\n    '
    trackers: NotRequired[list[Tracker]]
    '\n    Complete desired advertiser tracker-default list. Campaigns inherit these trackers.\n    '

class AssignAccount(TypedDict):
    """
    Requires advertiserId. For connection accounts use save_connection advertiserMapping.
    """
    partnerId: str
    '\n    Partner/storefront ID to link.\n    '
    accountId: str
    '\n    Provider account ID.\n    '
    credentialId: NotRequired[str]
    '\n    Credential ID when the partner has multiple connections.\n    '

class UnassignAccount(TypedDict):
    """
    Remove a linked provider account. Requires advertiserId.
    """
    linkId: str
    '\n    Account link ID to remove (from listAccounts).\n    '

class Bucket(TypedDict):
    """
    Reporting bucket. null to clear.
    """
    protocol: Literal['s3', 'gcs', 'azure_blob']
    '\n    Object storage protocol\n    '
    bucket: str
    '\n    Bucket name. Lowercase alphanumerics, dots, hyphens; start/end alphanumeric; 3-63 chars.\n    '
    prefix: NotRequired[str]
    '\n    Object key prefix within the bucket\n    '
    region: NotRequired[str]
    '\n    Storage region identifier (lowercase alphanumerics and hyphens)\n    '
    format: NotRequired[Literal['jsonl', 'csv', 'parquet', 'avro', 'orc']]
    '\n    Report file format\n    '
    compression: NotRequired[Literal['gzip', 'none']]
    '\n    Compression applied to report files\n    '
    file_retention_days: int
    '\n    Number of days the customer retains report files in the bucket\n    '
    setup_instructions: NotRequired[str]
    '\n    Optional URL pointing to setup instructions for granting the agent access to the bucket\n    '

class UpdateReportingBucket(TypedDict):
    """
    Change the reporting bucket for a linked account. Requires advertiserId.
    """
    linkId: str
    '\n    Account link ID to update.\n    '
    bucket: Bucket | None
    '\n    Reporting bucket. null to clear.\n    '

class SaveAdvertiserInput(TypedDict):
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    advertiserId: NotRequired[str]
    '\n    ID of the advertiser to update. Omit to create a new one.\n    '
    name: NotRequired[str]
    '\n    Advertiser name. Required when creating.\n    '
    brand: NotRequired[str]
    '\n    Brand domain (e.g. "nike.com") or URL. Required when creating. Resolved via AdCP brand registry.\n    '
    publicBrand: NotRequired[bool]
    '\n    Require a published brand.json or AAO-hosted profile when linking brand; no inferred branding.\n    '
    identityContract: NotRequired[Literal['confirmed-v1']]
    '\n    Opt in to identity preview and confirmation. Guide: /v2/setup/v3/identity-setup.\n    '
    preview: NotRequired[bool]
    '\n    Preview an existing advertiser brand change without saving.\n    '
    confirmationToken: NotRequired[str]
    '\n    Brand-change preview token, supplied only after the human confirms the exact change.\n    '
    primaryCurrency: NotRequired[str]
    '\n    ISO 4217, e.g. "EUR". Optional on create; defaults to "USD" when omitted. Update to change.\n    '
    brandCountries: NotRequired[list[str]]
    '\n    ISO 3166-1 alpha-2 brand-market countries; pass an empty array to clear.\n    '
    preferredTimezone: NotRequired[str]
    '\n    IANA timezone for future account provisioning and reporting.\n    '
    channels: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence']]]
    '\n    Replacement AdCP channel preferences; empty clears them.\n    '
    sandbox: NotRequired[bool]
    '\n    Create only: true = test mode, no real spend. Omit = live. Permanent, cannot change after creation.\n    '
    isArchived: NotRequired[bool]
    '\n    true = archive, false = restore. Send alone with advertiserId (one) or advertiserIds (several).\n    '
    advertiserIds: NotRequired[list[AdvertiserId]]
    '\n    Bulk archive/restore with isArchived: up to 50 IDs in one call; results lists each outcome.\n    '
    correlationId: NotRequired[str]
    '\n    Tracing handle for this call. Not an idempotency key; the service does not deduplicate on this.\n    '
    idempotencyKey: NotRequired[str]
    '\n    Create-only: reuse one stable key for a logical create; use a new correlationId each attempt.\n    '
    tracking: NotRequired[Tracking]
    '\n    Advertiser tracker defaults, macros, and URL parameters inherited by campaigns and creatives.\n    '
    labels: NotRequired[dict[str, list[Label]]]
    '\n    Replace labels for each supplied dimension; [] clears.\n    '
    resolveBrand: NotRequired[str]
    '\n    Domain to resolve to a brand card preview. Set this alone — no other fields.\n    '
    assignAccount: NotRequired[AssignAccount]
    '\n    Requires advertiserId. For connection accounts use save_connection advertiserMapping.\n    '
    unassignAccount: NotRequired[UnassignAccount]
    '\n    Remove a linked provider account. Requires advertiserId.\n    '
    updateReportingBucket: NotRequired[UpdateReportingBucket]
    '\n    Change the reporting bucket for a linked account. Requires advertiserId.\n    '

class After(TypedDict):
    brand: str

class SaveAdvertiserResult1(TypedDict):
    action: Literal['preview']
    identityContract: Literal['confirmed-v1']
    '\n    Opt in to identity preview and confirmation. Guide: /v2/setup/v3/identity-setup.\n    '
    advertiserId: str
    before: JsonValue
    after: After
    confirmationToken: str
    requiresConfirmation: bool
    docs: str

class BrandRef(TypedDict):
    domain: str
    brand_id: str | None

class BrandIdentity(TypedDict):
    brandRef: BrandRef
    name: str | None
    logoUrl: str | None
    manifestUrl: str | None
    source: Literal['saved_brand_link', 'brand_json', 'hosted'] | None
    grantsAuthority: Literal[False]
    editingSupported: Literal[False]

class IdentityChangeReceipt(TypedDict):
    auditLogId: str
    previousBrandLinkId: str
    brandLinkId: str

class Advertiser1(TypedDict):
    advertiserId: str
    name: str
    status: str
    sandbox: bool
    primaryCurrency: str
    brandCountries: JsonValue
    preferredTimezone: JsonValue
    channels: list[JsonValue]
    currencyLocked: bool
    reportingTimezoneLocked: bool
    brand: NotRequired[str]
    brandIdentity: NotRequired[BrandIdentity | None]
    identityChangeReceipt: NotRequired[IdentityChangeReceipt]
    tracking: NotRequired[JsonValue]

class Receipt1(TypedDict):
    resourceId: str
    auditEventId: str

class SaveAdvertiserResult2(TypedDict):
    action: Literal['created', 'updated', 'unchanged', 'restored']
    advertiser: Advertiser1
    currencyDefaulted: NotRequired[bool]
    receipt: NotRequired[Receipt1]

class Result1(TypedDict):
    advertiserId: str
    ok: bool
    code: NotRequired[str]
    message: NotRequired[str]
    partialWrite: NotRequired[bool]

class SaveAdvertiserResult3(TypedDict):
    action: Literal['archived', 'restored']
    advertiserIds: list[str]
    results: list[Result1]
    partialWrite: NotRequired[bool]

class NeedsInputItem(TypedDict):
    field: str
    prompt: str

class SaveAdvertiserResult4(TypedDict):
    action: Literal['needs_input']
    message: str
    needsInput: list[NeedsInputItem]

class SaveAdvertiserResult5(TypedDict):
    action: Literal['archived']
    advertiserId: str

class Brand(TypedDict):
    domain: str
    resolved: bool

class SaveAdvertiserResult6(TypedDict):
    action: Literal['brand_resolved']
    brand: Brand

class Account3(TypedDict):
    linkId: str | float
    advertiserId: str

class SaveAdvertiserResult7(TypedDict):
    action: Literal['account_assigned', 'reporting_bucket_updated']
    account: Account3

class SaveAdvertiserResult8(TypedDict):
    action: Literal['account_unassigned']
    advertiserId: str
SaveAdvertiserResult: TypeAlias = SaveAdvertiserResult1 | SaveAdvertiserResult2 | SaveAdvertiserResult3 | SaveAdvertiserResult4 | SaveAdvertiserResult5 | SaveAdvertiserResult6 | SaveAdvertiserResult7 | SaveAdvertiserResult8
SaveAdvertiserError: TypeAlias = V3ToolErrorResponse

class SaveBuyerOperatorInput(TypedDict):
    operatorDomain: str
    '\n    Corporate domain of the organization operating this buyer account.\n    '
    operatorScope: Literal['whole_operator', 'specific_unit']
    '\n    whole_operator for the organization; specific_unit for one stable office, team, region, or seat.\n    '
    operatorUnitId: NotRequired[str]
    '\n    Stable seller-visible unit identifier. Required only with specific_unit; never use default.\n    '
    identityContract: NotRequired[Literal['confirmed-v1']]
    '\n    Opt in to identity preview and confirmation. Guide: /v2/setup/v3/identity-setup.\n    '
    preview: NotRequired[bool]
    '\n    Preview this identity change without saving.\n    '
    confirmationToken: NotRequired[str]
    '\n    Token from the preview, supplied only after the human confirms the exact change.\n    '

class OperatorIdentity1(TypedDict):
    id: int
    operatorDomain: str
    operatorScope: Literal['whole_operator', 'specific_unit'] | None
    operatorUnitId: str | None
    scopeConfirmedAt: str | None
    lockedAt: str | None
    verified: bool
    source: Literal['user_confirmed']
    confirmedAt: str

class Preview1(TypedDict):
    before: JsonValue
    after: SaveBuyerOperatorSuccessUpdateBuyerOperatorBody
    requiresConfirmation: bool
    confirmationToken: str
    domainProofWillReset: bool

class Receipt2(TypedDict):
    resourceType: Literal['buyer_account_identity']
    resourceId: str
    confirmedAt: str
    auditLogId: NotRequired[str]

class SaveBuyerOperatorResult(TypedDict):
    action: Literal['preview', 'saved', 'unchanged']
    identityContract: NotRequired[Literal['confirmed-v1']]
    '\n    Opt in to identity preview and confirmation. Guide: /v2/setup/v3/identity-setup.\n    '
    accessChanged: Literal[False]
    operatorIdentity: NotRequired[OperatorIdentity1]
    preview: NotRequired[Preview1]
    receipt: NotRequired[Receipt2]
    docs: str
SaveBuyerOperatorError: TypeAlias = V3ToolErrorResponse

class SaveBuyerAgentInput1(TypedDict):
    displayName: SaveBuyerAgentRequestDisplayName
    kind: NotRequired[Literal['external', 'hosted']]
    '\n    external is available. hosted creation is not available yet.\n    '

class SaveBuyerAgentInput2(TypedDict):
    id: SaveBuyerAgentRequestId
    displayName: SaveBuyerAgentRequestDisplayName

class Advertiser2(TypedDict):
    advertiserId: str
    '\n    Advertiser ID receiving this exact role.\n    '
    role: Literal['READ', 'READ_WRITE']
    '\n    READ or READ_WRITE access for this advertiser.\n    '

class Access1(TypedDict):
    expectedAccessRevision: int
    '\n    Access revision returned by the most recent read.\n    '
    advertisers: list[Advertiser2]
    '\n    Complete replacement list of advertiser grants.\n    '

class SaveBuyerAgentInput3(TypedDict):
    id: SaveBuyerAgentRequestId
    access: Access1

class Lifecycle(TypedDict):
    action: Literal['suspend']
    '\n    Suspend an active buyer agent.\n    '
    expectedLifecycleState: Literal['active']
    '\n    State fence required before suspension.\n    '
    confirmationText: SaveBuyerAgentRequestLifecycleConfirmationText

class Lifecycle1(TypedDict):
    action: Literal['resume']
    '\n    Resume a suspended buyer agent.\n    '
    expectedLifecycleState: Literal['suspended']
    '\n    State fence required before resumption.\n    '
    confirmationText: NotRequired[SaveBuyerAgentRequestLifecycleConfirmationText]

class Lifecycle2(TypedDict):
    action: Literal['retire']
    '\n    Permanently retire an active or suspended buyer agent.\n    '
    expectedLifecycleState: Literal['active', 'suspended']
    '\n    State fence required before retirement.\n    '
    confirmationText: SaveBuyerAgentRequestLifecycleConfirmationText

class SaveBuyerAgentInput4(TypedDict):
    id: SaveBuyerAgentRequestId
    lifecycle: Lifecycle | Lifecycle1 | Lifecycle2

class SaveBuyerAgentInput5(TypedDict):
    id: SaveBuyerAgentRequestId
    credentialHandoff: Literal[True]
SaveBuyerAgentInput: TypeAlias = SaveBuyerAgentInput1 | SaveBuyerAgentInput2 | SaveBuyerAgentInput3 | SaveBuyerAgentInput4 | SaveBuyerAgentInput5
SaveBuyerAgentError: TypeAlias = V3ToolErrorResponse

class SaveDirectedCampaignSubscriptionInput(TypedDict):
    connectionId: str
    '\n    Seller connection ID.\n    '
    accountId: str
    '\n    Provider account ID within the connection.\n    '
    advertiserId: NotRequired[str]
    '\n    Required when subscribing; the advertiser to mirror directed campaigns into.\n    '
    sourceId: NotRequired[str]
    '\n    Required for third-party AdCP sources. Omit for standard adapter connections.\n    '
    unsubscribe: NotRequired[bool]
    '\n    true = unsubscribe this connection+account pair.\n    '

class SaveDirectedCampaignSubscriptionResult1(TypedDict):
    action: Literal['subscribed']
    connectionId: str
    accountId: str
    advertiserId: str
    mirrored: int
    errors: NotRequired[list[str]]
    errorCode: NotRequired[str]
    errorField: NotRequired[str]
    errorReason: NotRequired[str]
    upstreamCode: NotRequired[str]

class SaveDirectedCampaignSubscriptionResult2(TypedDict):
    action: Literal['unsubscribed']
    connectionId: str
    accountId: str
    retired: int
SaveDirectedCampaignSubscriptionResult: TypeAlias = SaveDirectedCampaignSubscriptionResult1 | SaveDirectedCampaignSubscriptionResult2
SaveDirectedCampaignSubscriptionError: TypeAlias = V3ToolErrorResponse

class AddItem1(TypedDict):
    externalId: str
    '\n    Audience-scoped identifier for this member. Must not contain raw PII.\n    '
    email: NotRequired[str]
    '\n    Raw email; normalized (lowercase, trimmed) and SHA-256 hashed before forwarding.\n    '
    hashedEmail: NotRequired[str]
    '\n    Pre-hashed SHA-256 of lowercase, trimmed email (64-char hex).\n    '
    hashedPhone: NotRequired[str]
    '\n    Pre-hashed SHA-256 of E.164-formatted phone number (64-char hex).\n    '

class RemoveItem2(TypedDict):
    externalId: str
    '\n    External ID of the member to remove.\n    '

class Audience(TypedDict):
    audienceId: str
    "\n    Buyer's identifier for this audience. Used in targeting.\n    "
    name: NotRequired[str]
    '\n    Human-readable audience name.\n    '
    add: NotRequired[list[AddItem1]]
    '\n    Members to add to this audience.\n    '
    remove: NotRequired[list[RemoveItem2]]
    '\n    Members to remove from this audience by externalId.\n    '
    delete: NotRequired[bool]
    '\n    When true, delete this audience entirely.\n    '
    consentBasis: NotRequired[Literal['consent', 'legitimate_interest', 'contract', 'legal_obligation']]
    '\n    GDPR lawful basis for processing.\n    '

class SaveAudienceInput(TypedDict):
    advertiserId: int | str
    '\n    Numeric advertiser ID (positive integer, e.g. 42 or "42").\n    '
    audiences: list[Audience]
    '\n    Audiences to sync. At least one required.\n    '

class SaveAudienceResult(TypedDict):
    action: Literal['synced']
    operationId: str
    advertiserId: int
    audienceCount: int
SaveAudienceError: TypeAlias = V3ToolErrorResponse

class Flight(TypedDict):
    """
    Flight window. Null clears it; omit to leave it unchanged.
    """
    startAt: str
    '\n    ISO 8601 datetime. Use current time for today, not midnight (T00:00:00Z). Must be >= now.\n    '
    endAt: str
    '\n    ISO 8601 datetime (e.g. 2026-09-30T23:59:59Z). Must be after startAt.\n    '

class Budget7(TypedDict):
    """
    Campaign budget.
    """
    total: float
    '\n    Total budget in the campaign currency.\n    '
    currency: str
    '\n    ISO 4217 currency code.\n    '
    dailyCap: NotRequired[float]
    '\n    Daily spend cap.\n    '
    pacing: NotRequired[Literal['even', 'asap', 'frontloaded']]
    '\n    Delivery pacing strategy.\n    '

class Config(TypedDict):
    """
    Seller-enforced AdCP 3.2 cap configuration.
    """
    maxImpressions: int
    '\n    Maximum impressions allowed in the window.\n    '
    per: Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']
    '\n    Reach unit counted by the seller.\n    '
    window: Window
    '\n    Counting window for the cap.\n    '

class FrequencyCap(TypedDict):
    """
    Per-seller AdCP 3.2 MediaBuy cap. Null clears it; draft only. Other levels are unavailable.
    """
    level: Literal['mediaBuy']
    '\n    Counter scope. Only mediaBuy is available.\n    '
    config: Config
    '\n    Seller-enforced AdCP 3.2 cap configuration.\n    '
CreativeId: TypeAlias = str

class Autonomy(TypedDict):
    """
    Autonomy settings, persisted per campaign. Set one or both dimensions; omitted are unchanged.
    """
    inventorySelection: NotRequired[Literal['manual', 'propose', 'automatic']]
    '\n    manual: human-driven; propose: agent drafts, waits for approval; automatic: agent acts.\n    '
    rebriefing: NotRequired[Literal['manual', 'propose', 'automatic']]
    '\n    How the brief is updated: manual (human), propose (agent drafts), automatic (agent applies).\n    '

class Tracker1(TypedDict):
    trackerId: NotRequired[SaveCampaignRequestTrackingTrackersItemTrackerId]
    '\n    Stable tracker ID returned by a prior read. Omit when creating.\n    '
    name: str
    '\n    Human-readable tracker name.\n    '
    vendorName: NotRequired[str]
    '\n    Measurement or tracking vendor name.\n    '
    url: NotRequired[str]
    '\n    Raw vendor URL. Required on create; omit with trackerId on update to keep the stored URL.\n    '
    trackerType: Literal['impression', 'click', 'custom']
    '\n    Event that causes this tracker to fire.\n    '
    customEventName: NotRequired[str]
    '\n    Required when trackerType is custom.\n    '
    enabled: NotRequired[bool]
    '\n    Whether this tracker is enabled at its owning scope.\n    '
    gvlVendorId: NotRequired[int]
    '\n    IAB GVL vendor ID for TCF consent macro scoping (e.g. 550 for HappyDemics).\n    '
    sourceDialect: NotRequired[Literal['adcp', 'happydemics', 'gam', 'vast', 'custom']]
    '\n    Declare only when trusted context identifies the dialect; otherwise omit for exact-origin detection.\n    '

class Override(TypedDict):
    trackerId: SaveCampaignRequestTrackingOverridesItemTrackerId
    '\n    Stable ID of an inherited advertiser tracker.\n    '
    enabled: bool
    '\n    Desired enabled state for the inherited tracker.\n    '

class Tracking1(TypedDict):
    """
    Campaign trackers, advertiser overrides, and creative URL parameters.
    """
    expectedRevision: NotRequired[int]
    '\n    Last-read campaignRevision. Rejects concurrent tracking updates.\n    '
    trackers: NotRequired[list[Tracker1]]
    '\n    Complete desired campaign-local tracker list.\n    '
    overrides: NotRequired[list[Override]]
    '\n    Enable or disable inherited advertiser trackers by stable tracker ID.\n    '
    macroAdditions: NotRequired[list[MacroAddition]]
    '\n    Campaign URL parameters. Same keys override advertiser values; null suppresses inheritance.\n    '
GeoCountry: TypeAlias = str
GeoCountriesExcludeItem: TypeAlias = str
GeoRegion: TypeAlias = str
GeoRegionsExcludeItem: TypeAlias = str

class TravelTime(TypedDict):
    """
    Maximum travel time.
    """
    value: float
    '\n    Value.\n    '
    unit: Literal['min', 'hr']
    '\n    Unit.\n    '

class Radius(TypedDict):
    """
    Radius.
    """
    value: float
    '\n    Value.\n    '
    unit: Literal['km', 'mi', 'm']
    '\n    Unit.\n    '

class Geometry2(TypedDict):
    """
    Geographic boundary.
    """
    type: Literal['Polygon', 'MultiPolygon']
    '\n    Geometry type.\n    '
    coordinates: list[JsonValue]
    '\n    Geometry coordinates.\n    '

class GeoProximityItem(TypedDict):
    lat: NotRequired[float]
    '\n    Latitude.\n    '
    lng: NotRequired[float]
    '\n    Longitude.\n    '
    label: NotRequired[str]
    '\n    Optional display label.\n    '
    travel_time: NotRequired[TravelTime]
    '\n    Maximum travel time.\n    '
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    '\n    Travel mode.\n    '
    radius: NotRequired[Radius]
    '\n    Radius.\n    '
    geometry: NotRequired[Geometry2]
    '\n    Geographic boundary.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '
LanguageItem: TypeAlias = str

class DaypartTarget(TypedDict):
    days: list[Literal['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]
    '\n    Weekdays in this window.\n    '
    start_hour: int
    '\n    Start hour.\n    '
    end_hour: int
    '\n    End hour.\n    '
    timezone: NotRequired[Literal['inventory_local'] | JsonValue]
    '\n    IANA timezone.\n    '
    label: NotRequired[str]
    '\n    Optional display label.\n    '

class Age1(TypedDict):
    min: JsonValue
    '\n    Minimum age.\n    '

class Age2(TypedDict):
    accepted_verification_methods: JsonValue
    '\n    Methods.\n    '
    accepted_bases: JsonValue
    '\n    Accepted age-data bases.\n    '

class Age3(TypedDict):
    """
    Age range.
    """
    min: NotRequired[int]
    '\n    Minimum age.\n    '
    max: NotRequired[int]
    '\n    Maximum age.\n    '
    include_unknown: bool
    '\n    Include unknown ages.\n    '
    accepted_bases: NotRequired[list[Literal['verified', 'declared', 'inferred']]]
    '\n    Accepted age-data bases.\n    '
    accepted_verification_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]
    '\n    Methods.\n    '

class Age4(TypedDict):
    min: NotRequired[int]
    max: NotRequired[int]
    include_unknown: bool
    accepted_bases: NotRequired[list[Literal['verified', 'declared', 'inferred']]]
    accepted_verification_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]

class Age5(TypedDict):
    accepted_verification_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]
    accepted_bases: NotRequired[list[Literal['verified', 'declared', 'inferred']]]
    min: NotRequired[int]
    max: NotRequired[int]
    include_unknown: bool
Age: TypeAlias = Age4 | Age5
'\nAge range.\n'

class Demographics(TypedDict):
    """
    Demographic criteria.
    """
    age: Age
    '\n    Age range.\n    '

class AgeRestriction(TypedDict):
    """
    Minimum audience age.
    """
    min: int
    '\n    Minimum age.\n    '
    verification_required: NotRequired[bool]
    '\n    Require age verification.\n    '
    accepted_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]
    '\n    Accepted age-verification methods.\n    '

class TargetingOverlay(TypedDict):
    """
    AdCP campaign targeting overlay.
    """
    geo_countries: NotRequired[list[GeoCountry]]
    '\n    Country codes.\n    '
    geo_countries_exclude: NotRequired[list[GeoCountriesExcludeItem]]
    '\n    Country codes.\n    '
    geo_regions: NotRequired[list[GeoRegion]]
    '\n    Subdivision codes.\n    '
    geo_regions_exclude: NotRequired[list[GeoRegionsExcludeItem]]
    '\n    Subdivision codes.\n    '
    geo_metros: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared3]
    geo_metros_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared3]
    geo_postal_areas: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared1]
    geo_postal_areas_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared1]
    geo_places: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared2]
    geo_places_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared2]
    geo_proximity: NotRequired[list[GeoProximityItem]]
    '\n    Location and radius groups.\n    '
    language: NotRequired[list[LanguageItem]]
    '\n    Language codes to include.\n    '
    device_type: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared6]
    device_type_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared6]
    device_platform: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared4]
    device_platform_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared4]
    browser: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared5]
    browser_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared5]
    daypart_targets: NotRequired[list[DaypartTarget]]
    '\n    Delivery windows.\n    '
    demographics: NotRequired[Demographics]
    '\n    Demographic criteria.\n    '
    age_restriction: NotRequired[AgeRestriction]
    '\n    Minimum audience age.\n    '

class GeoItem(TypedDict):
    requirementId: str
    '\n    Stable identifier for this requirement; unique across all targeting dimensions.\n    '
    strength: SaveCampaignRequestTargetingGeoItemStrength
    '\n    "required" means must satisfy; "preferred" means optimize toward.\n    '
    include: NotRequired[list[SaveCampaignRequestTargetingGeoItemIncludeItem]]
    '\n    ISO 3166-1 alpha-2 country codes or CLDR region subdivisions to include.\n    '
    exclude: NotRequired[list[SaveCampaignRequestTargetingGeoItemExcludeItem]]
    '\n    ISO 3166-1 alpha-2 country codes or CLDR region subdivisions to exclude.\n    '

class LanguageItem1(TypedDict):
    requirementId: str
    '\n    Stable identifier for this requirement; unique across all targeting dimensions.\n    '
    strength: SaveCampaignRequestTargetingLanguageItemStrength
    '\n    "required" means must satisfy; "preferred" means optimize toward.\n    '
    include: NotRequired[list[SaveCampaignRequestTargetingLanguageItemIncludeItem]]
    '\n    BCP 47 language tags to include (e.g. "en", "en-US").\n    '
    exclude: NotRequired[list[SaveCampaignRequestTargetingLanguageItemExcludeItem]]
    '\n    BCP 47 language tags to exclude.\n    '

class DeviceItem(TypedDict):
    requirementId: str
    '\n    Stable identifier for this requirement; unique across all targeting dimensions.\n    '
    strength: SaveCampaignRequestTargetingDeviceItemStrength
    '\n    "required" means must satisfy; "preferred" means optimize toward.\n    '
    include: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    AdCP device types to include: desktop, mobile, tablet, ctv, dooh, unknown.\n    '
    exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    AdCP device types to exclude.\n    '

class Window3(TypedDict):
    days: list[Literal['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']]
    '\n    Days of the week this window applies to.\n    '
    startHour: int
    '\n    Window start in 24-hour local time, inclusive (0-23).\n    '
    endHour: int
    '\n    Window end in 24-hour local time, exclusive (1-24); 24 means end-of-day.\n    '

class Daypart(TypedDict):
    requirementId: str
    '\n    Stable identifier for this requirement; unique across all targeting dimensions.\n    '
    strength: SaveCampaignRequestTargetingDaypartsItemStrength
    '\n    "required" means must satisfy; "preferred" means optimize toward.\n    '
    timezone: str
    '\n    IANA tzdata identifier (e.g. "America/New_York").\n    '
    windows: list[Window3]
    '\n    One or more time windows; delivery is in-scope if it falls inside any window.\n    '

class AgeItem(TypedDict):
    requirementId: str
    '\n    Stable identifier for this requirement; unique across all targeting dimensions.\n    '
    strength: SaveCampaignRequestTargetingDemographicsAgeItemStrength
    '\n    "required" means must satisfy; "preferred" means optimize toward.\n    '
    minAge: NotRequired[int]
    '\n    Inclusive lower age bound (integer years).\n    '
    maxAge: NotRequired[int]
    '\n    Inclusive upper age bound (integer years).\n    '
    includeUnknownAge: NotRequired[bool]
    '\n    Include users whose age cannot be determined. Defaults to false.\n    '
    allowModeledAge: NotRequired[bool]
    '\n    Accept statistically modeled age when verified signal is unavailable. Defaults to false.\n    '

class Demographics1(TypedDict):
    """
    Demographic targeting requirements.
    """
    age: NotRequired[list[AgeItem]]
    '\n    Age targeting requirements.\n    '
IncludeItem: TypeAlias = str
ExcludeItem: TypeAlias = str

class GeoMetro(TypedDict):
    """
    One retired Nielsen DMA targeting requirement.
    """
    requirementId: str
    '\n    Retired requirement identifier.\n    '
    strength: Literal['required']
    '\n    Retired requirement strength.\n    '
    system: Literal['nielsen_dma']
    '\n    Nielsen DMA code system.\n    '
    include: NotRequired[list[IncludeItem]]
    '\n    Nielsen DMA codes to include.\n    '
    exclude: NotRequired[list[ExcludeItem]]
    '\n    Nielsen DMA codes to exclude.\n    '

class Targeting(TypedDict):
    """
    Deprecated; unchanged. Use targetingOverlay. AI-10440: 14-day notice; planned 2 Nov 2026.
    """
    geo: NotRequired[list[GeoItem]]
    '\n    Geographic targeting requirements (countries and regions).\n    '
    language: NotRequired[list[LanguageItem1]]
    '\n    Language targeting requirements (BCP 47 tags).\n    '
    device: NotRequired[list[DeviceItem]]
    '\n    Device-type targeting requirements.\n    '
    dayparts: NotRequired[list[Daypart]]
    '\n    Daypart targeting requirements (time windows per timezone).\n    '
    demographics: NotRequired[Demographics1]
    '\n    Demographic targeting requirements.\n    '
    geoMetros: NotRequired[list[GeoMetro]]
    '\n    Nielsen DMA targeting requirements.\n    '

class ChannelGroups(TypedDict):
    channelGroupId: SaveCampaignRequestChannelGroupsItemChannelGroupId
    name: NotRequired[SaveCampaignRequestChannelGroupsItemName]
    '\n    Buyer-facing label. Presets supply a default when omitted.\n    '
    presetId: Literal['display', 'olv', 'mobile_web_display', 'mobile_web_olv', 'ctv']
    '\n    Versioned channel group preset to expand into AdCP inventory dimensions.\n    '
    presetVersion: NotRequired[int]
    '\n    Expected preset version. Omit to use the current version; a mismatch is rejected.\n    '

class Inventory(TypedDict):
    """
    Custom AdCP inventory dimensions. Values within a dimension are OR; populated dimensions are AND.
    """
    channels: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence']]]
    '\n    Buyer-declared AdCP media channels. Values are OR.\n    '
    propertyTypes: NotRequired[list[Literal['website', 'mobile_app', 'ctv_app', 'desktop_app', 'dooh', 'podcast', 'radio', 'linear_tv', 'streaming_audio', 'ai_assistant']]]
    '\n    Buyer-declared AdCP property types. Values are OR.\n    '
    deviceTypes: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Buyer-declared AdCP device types. Values are OR.\n    '
    formatKinds: NotRequired[list[Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']]]
    '\n    Buyer-declared AdCP canonical creative format kinds. Values are OR.\n    '

class ChannelGroups1(TypedDict):
    channelGroupId: SaveCampaignRequestChannelGroupsItemChannelGroupId
    name: NotRequired[SaveCampaignRequestChannelGroupsItemName]
    '\n    Buyer-facing label. Presets supply a default when omitted.\n    '
    inventory: Inventory
    '\n    Custom AdCP inventory dimensions. Values within a dimension are OR; populated dimensions are AND.\n    '
TargetAudienceId: TypeAlias = str
SuppressAudienceId: TypeAlias = str

class AudienceConfig(TypedDict):
    """
    Campaign audiences. deleteMissing: true replaces each list. Seller sync is unavailable (AI-10203).
    """
    targetAudienceIds: NotRequired[list[TargetAudienceId]]
    '\n    Audience IDs to target. Can be empty when deleteMissing is true to remove all targeted audiences.\n    '
    suppressAudienceIds: NotRequired[list[SuppressAudienceId]]
    '\n    Audience IDs to suppress. Empty with deleteMissing: true clears suppressions.\n    '
    deleteMissing: NotRequired[bool]
    '\n    When true, replace each list. Otherwise, supplied IDs are added.\n    '

class SaveCampaignResult1(TypedDict):
    action: NotRequired[Literal['archived']]
    campaignId: str

class Campaign(TypedDict):
    campaignId: str
    advertiserId: str | None
    name: str
    phase: Literal['draft', 'active', 'ending', 'completed', 'canceled']
    revision: int
    updatedAt: str
    targetingOverlay: NotRequired[dict[str, JsonValue]]
    '\n    AdCP TargetingOverlay (campaign subset); same shape as the save_campaign targetingOverlay input.\n    '

class Membership(TypedDict):
    creativeIds: list[str]
    attached: list[str]
    detached: list[str]

class Error10(TypedDict):
    mediaBuyId: str
    salesAgentId: str
    message: str
    code: NotRequired[str]
    recovery: NotRequired[Literal['transient', 'correctable', 'terminal']]
    safeMessage: NotRequired[str]
    cleanup_required: NotRequired[Literal[True]]
    retry_safe: NotRequired[Literal[False]]
    scope3_partial_creation: NotRequired[dict[str, JsonValue]]
    scope3_create_uncertain: NotRequired[dict[str, JsonValue]]
    scope3_mutation_uncertain: NotRequired[dict[str, JsonValue]]

class DroppedItem(TypedDict):
    creativeId: str
    formatId: str
    reason: str

class Warnings(TypedDict):
    type: Literal['creatives_dropped']
    mediaBuyId: str
    dropped: list[DroppedItem]

class DroppedItem1(TypedDict):
    productId: str
    buyerRef: str
    goal: dict[str, JsonValue]
    code: SaveCampaignSuccessDroppedOptimizationGoalCode
    reason: str

class Warnings1(TypedDict):
    type: Literal['optimization_goals_dropped']
    mediaBuyId: str
    dropped: list[DroppedItem1]

class Warnings2(TypedDict):
    type: Literal['stale_draft']
    mediaBuyIds: list[str]
    hint: str

class Execution(TypedDict):
    mediaBuysExecuted: float
    noOp: bool
    errors: NotRequired[list[Error10]]
    warnings: NotRequired[list[Warnings | Warnings1 | Warnings2]]

class PropertyListAttachment(TypedDict):
    propertyListId: str
    cascade: SaveCampaignSuccessPropertyListAttachmentCascade

class PropertyListClear(TypedDict):
    cascade: SaveCampaignSuccessPropertyListClearCascade

class MediaBuys(TypedDict):
    mediaBuyId: str
    outcome: Literal['canceled']

class MediaBuys1(TypedDict):
    mediaBuyId: str
    outcome: Literal['completed', 'failed', 'rejected', 'archived']

class MediaBuys2(TypedDict):
    mediaBuyId: str
    outcome: Literal['cancel_pending']

class Error11(TypedDict):
    code: str
    message: str

class MediaBuys3(TypedDict):
    mediaBuyId: str
    outcome: Literal['cancel_failed']
    error: Error11

class SaveCampaignResult2(TypedDict):
    action: Literal['created', 'updated', 'activated', 'restored', 'canceled', 'cancellation_requested']
    campaign: Campaign
    partialWrite: NotRequired[bool]
    priorSteps: NotRequired[list[str]]
    membership: NotRequired[Membership]
    execution: NotRequired[Execution]
    warnings: NotRequired[list[str]]
    skippedSellerIds: NotRequired[list[str]]
    propertyListAttachment: NotRequired[PropertyListAttachment]
    propertyListClear: NotRequired[PropertyListClear]
    mediaBuys: NotRequired[list[MediaBuys | MediaBuys1 | MediaBuys2 | MediaBuys3]]

class SaveCampaignResult3(TypedDict):
    action: Literal['pending_approval']
    campaignId: str
    proposalCount: int
    skippedTransitions: NotRequired[list[str]]

class Campaign1(TypedDict):
    campaignId: str
    name: str
    phase: str
    revision: float

class MediaBuy1(TypedDict):
    mediaBuyId: str
    name: str
    phase: Literal['draft']
    budget: NotRequired[SaveCampaignSuccessLaunchMediaBuysItemBudget]
    sellerName: NotRequired[str]

class Blocker3(TypedDict):
    code: str
    message: str

class Launch(TypedDict):
    mediaBuyCount: int
    mediaBuys: list[MediaBuy1]
    mediaBuysTruncated: NotRequired[Literal[True]]
    combinedBudget: SaveCampaignSuccessLaunchCombinedBudget | None
    budgetsByCurrency: NotRequired[list[SaveCampaignSuccessLaunchBudgetsByCurrencyItem]]
    blockers: NotRequired[list[Blocker3]]

class Arguments5(TypedDict):
    campaignId: str
    desiredPhase: Literal['active']
    confirmLaunch: Literal[True]
    expectedRevision: float
    idempotencyKey: str

class NextStep(TypedDict):
    tool: Literal['save_campaign']
    arguments: Arguments5

class SaveCampaignResult4(TypedDict):
    action: Literal['pending_confirmation']
    campaign: Campaign1
    launch: Launch
    nextStep: NextStep
SaveCampaignResult: TypeAlias = SaveCampaignResult1 | SaveCampaignResult2 | SaveCampaignResult3 | SaveCampaignResult4
SaveCampaignError: TypeAlias = V3ToolErrorResponse

class FeedFieldMapping(TypedDict):
    feedField: NotRequired[str]
    '\n    Feed field.\n    '
    catalogField: NotRequired[str]
    '\n    Item path.\n    '
    assetGroupId: NotRequired[str]
    '\n    Asset pool.\n    '
    value: NotRequired[JsonValue]
    '\n    Value.\n    '
    transform: NotRequired[Literal['date', 'divide', 'boolean', 'split']]
    '\n    Transform.\n    '
    format: NotRequired[str]
    '\n    Format.\n    '
    timezone: NotRequired[str]
    '\n    Timezone.\n    '
    by: NotRequired[float]
    '\n    Divisor.\n    '
    separator: NotRequired[str]
    '\n    Separator.\n    '
    default: NotRequired[JsonValue]
    '\n    Fallback.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    Extensions.\n    '

class SaveCatalogInput(TypedDict):
    feedFieldMappings: NotRequired[list[FeedFieldMapping]]
    '\n    Feed field mappings.\n    '
    catalogId: str
    '\n    Buyer-assigned catalog ID. Saving it again replaces this catalog.\n    '
    advertiserId: str
    '\n    Advertiser that owns this catalog.\n    '
    name: NotRequired[str]
    '\n    Name.\n    '
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    '\n    Catalog type. Required when declaring a catalog.\n    '
    url: NotRequired[str]
    '\n    Feed URL.\n    '
    feedFormat: NotRequired[Literal['google_merchant_center', 'facebook_catalog', 'shopify', 'linkedin_jobs', 'tiktok_shop', 'pinterest_catalog', 'openai_product_feed', 'custom']]
    '\n    Feed format.\n    '
    updateFrequency: NotRequired[Literal['realtime', 'hourly', 'daily', 'weekly']]
    '\n    Refresh cadence.\n    '
    items: NotRequired[list[dict[str, JsonValue]]]
    '\n    Inline items.\n    '
    ids: NotRequired[list[Id]]
    '\n    Catalog item IDs.\n    '
    gtins: NotRequired[list[Gtin]]
    '\n    Catalog item GTINs.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Catalog item tags.\n    '
    category: NotRequired[str]
    '\n    Catalog item category.\n    '
    query: NotRequired[str]
    '\n    Catalog item search query.\n    '
    conversionEvents: NotRequired[list[Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']]]
    '\n    Conversion events.\n    '
    contentIdType: NotRequired[Literal['sku', 'gtin', 'offering_id', 'job_id', 'hotel_id', 'flight_id', 'vehicle_id', 'listing_id', 'store_id', 'program_id', 'destination_id', 'app_id']]
    '\n    Catalog item identifier.\n    '
    isArchived: NotRequired[bool]
    '\n    Set true to archive this catalog. Omit to create or replace its declaration.\n    '
    idempotencyKey: str
    '\n    Unique key for this one catalog save; replays return the original result.\n    '

class SaveCatalogResult(TypedDict):
    action: Literal['created', 'updated', 'unchanged', 'deleted']
    object: JsonValue
    replayed: bool
SaveCatalogError: TypeAlias = V3ToolErrorResponse

class Mapping1(TypedDict):
    """
    How source fields map into accepted conversion events.
    """
    eventIdField: NotRequired[str]
    '\n    Source field mapped to the event ID.\n    '
    eventTypeField: NotRequired[str]
    '\n    Source field or expression mapped to event type.\n    '
    eventTimeField: NotRequired[str]
    '\n    Source timestamp field mapped to event time.\n    '
    userMatchFields: NotRequired[list[str]]
    '\n    Source fields available for privacy-safe user matching.\n    '
    valueField: NotRequired[str]
    '\n    Source field mapped to conversion value.\n    '
    currencyField: NotRequired[str]
    '\n    Source field mapped to currency.\n    '
    orderIdField: NotRequired[str]
    '\n    Source field mapped to order ID.\n    '
    contentIdsField: NotRequired[str]
    '\n    Source field mapped to content IDs.\n    '
    consentField: NotRequired[str]
    '\n    Source field carrying consent or privacy state.\n    '
    dedupeStrategy: NotRequired[str]
    '\n    How stable event IDs are generated and deduplicated.\n    '
    notes: NotRequired[str]
    '\n    Additional integration notes.\n    '

class SaveMeasurementSourceInput(TypedDict):
    advertiserId: str
    '\n    Owning advertiser ID.\n    '
    id: NotRequired[str]
    '\n    Existing measurement source id from search/get, beginning `event:`. Omit to create.\n    '
    sourceType: NotRequired[Literal['event']]
    '\n    Event source for conversion tracking. Additional measurement-provider types are not yet writable.\n    '
    eventSourceId: NotRequired[str]
    '\n    Buyer-assigned event source ID. Required on create; use object.id on later writes.\n    '
    name: NotRequired[str]
    '\n    Human-readable source name. Required on create.\n    '
    eventTypes: NotRequired[list[Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']]]
    '\n    Accepted event types. Omit to accept every event type.\n    '
    allowedDomains: NotRequired[list[str]]
    '\n    Authorized browser domains. An empty list is valid for a server-to-server feed.\n    '
    integrationPlatform: NotRequired[str]
    '\n    Source system, such as a CRM, server API, or measurement partner.\n    '
    mapping: NotRequired[Mapping1]
    '\n    How source fields map into accepted conversion events.\n    '
    testEventCode: NotRequired[str]
    '\n    Optional code that marks test events from this source.\n    '
    isArchived: NotRequired[bool]
    '\n    Set true to archive this exact source or false to restore it. Archived sources stop resolving.\n    '

class Object3(TypedDict):
    id: str
    sourceType: Literal['event']
    advertiserId: str
    eventSourceId: str

class Setup1(TypedDict):
    snippetType: Literal['javascript', 'html', 'pixel_url', 'server_only']
    snippet: NotRequired[str]
    instructions: str

class SaveMeasurementSourceResult(TypedDict):
    action: Literal['created', 'updated', 'unchanged', 'archived', 'restored']
    object: Object3
    setup: NotRequired[Setup1]
SaveMeasurementSourceError: TypeAlias = V3ToolErrorResponse
ValueCurrency: TypeAlias = str

class EventSource1(TypedDict):
    eventSourceId: str
    '\n    Buyer-assigned event source ID. Creates the source if new, updates it if it exists.\n    '
    name: NotRequired[str]
    '\n    Human-readable source name. Required when this entry creates a source.\n    '
    eventTypes: NotRequired[list[Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']]]
    '\n    Accepted event types. Omit to accept every event type.\n    '
    valueCurrencies: NotRequired[list[ValueCurrency] | None]
    '\n    ISO 4217 currencies accepted for monetary values; required for canonical ROAS. Null clears it.\n    '
    actionSource: NotRequired[SaveEventSourceRequestEventSourceActionSource | None]
    '\n    Flat AdCP action-source category (website, app, in_store, ...); null clears it.\n    '
    surface: NotRequired[SaveEventSourceRequestEventSourceSurface | None]
    '\n    Structured AdCP surface; a channel, feed, or list when actionSource is too coarse. Null clears it.\n    '
    isArchived: NotRequired[bool]
    '\n    True archives; false undoes the archive, keeping its configuration. Must be the only change.\n    '

class SaveEventSourceInput(TypedDict):
    eventSources: list[EventSource1]
    '\n    Event sources to create, change, archive, or restore (1 to 50).\n    '
    advertiserId: str
    '\n    Owning advertiser ID for every entry.\n    '
    idempotencyKey: str
    '\n    Client-generated key for the whole batch. Same key + same batch replays the prior result.\n    '
SaveEventSourceError: TypeAlias = V3ToolErrorResponse

class SaveDimensionInput1(TypedDict):
    key: str
    '\n    Immutable dimension key. Required only for creation; use id to update an existing dimension.\n    '
    name: SaveDimensionRequestName
    valuesMode: SaveDimensionRequestValuesMode
    appliesTo: SaveDimensionRequestAppliesTo
    retired: NotRequired[SaveDimensionRequestRetired]
    '\n    Hide this dimension.\n    '
    values: NotRequired[SaveDimensionRequestValues]
    '\n    Values to add or change.\n    '
    idempotencyKey: SaveDimensionRequestIdempotencyKey

class SaveDimensionInput2(TypedDict):
    id: str
    '\n    Opaque id returned on creation. Required for every update; key never changes.\n    '
    name: NotRequired[SaveDimensionRequestName]
    valuesMode: NotRequired[SaveDimensionRequestValuesMode]
    appliesTo: NotRequired[SaveDimensionRequestAppliesTo]
    retired: NotRequired[SaveDimensionRequestRetired]
    '\n    Hide this dimension.\n    '
    values: NotRequired[SaveDimensionRequestValues]
    '\n    Values to add or change.\n    '
    idempotencyKey: SaveDimensionRequestIdempotencyKey
SaveDimensionInput: TypeAlias = SaveDimensionInput1 | SaveDimensionInput2

class SaveDimensionResult(TypedDict):
    action: Literal['created', 'updated', 'unchanged']
    object: SaveDimensionSuccessDimension
    replayed: bool
SaveDimensionError: TypeAlias = V3ToolErrorResponse

class SavePropertyListInput(TypedDict):
    advertiserId: str
    '\n    Advertiser that owns this property list.\n    '
    propertyListId: NotRequired[str]
    '\n    Existing property-list ID from search/get. Omit to create or check.\n    '
    name: NotRequired[str]
    '\n    List name. Required when creating.\n    '
    purpose: NotRequired[Literal['include', 'exclude']]
    '\n    include or exclude. Required when creating and immutable afterwards.\n    '
    domains: NotRequired[list[Domain]]
    '\n    Domain shorthand for typed identifiers.\n    '
    identifiers: NotRequired[list[SavePropertyListRequestPropertyListIdentifier]]
    '\n    AdCP typed property identifiers.\n    '
    filters: NotRequired[SavePropertyListRequestPropertyListFilters | None]
    '\n    Create-only SmartPropertyList filters.\n    '
    check: NotRequired[bool]
    '\n    true checks identifiers against AAO without saving a list.\n    '
    isArchived: NotRequired[bool]
    '\n    true archives an existing list. Restore is not available yet.\n    '

class Summary(TypedDict):
    total: int
    remove: int
    modify: int
    assess: int
    ok: int

class Check(TypedDict):
    summary: Summary
    reportId: NotRequired[str]
    reportIds: NotRequired[list[str]]

class SavePropertyListResult1(TypedDict):
    action: Literal['checked']
    check: Check

class Item2(TypedDict):
    type: Literal['domain', 'subdomain', 'network_id', 'ios_bundle', 'android_package', 'apple_app_store_id', 'google_play_id', 'roku_store_id', 'fire_tv_asin', 'samsung_app_id', 'apple_tv_bundle', 'bundle_id', 'venue_id', 'screen_id', 'openooh_venue_type', 'rss_url', 'apple_podcast_id', 'spotify_collection_id', 'podcast_guid', 'station_id', 'facility_id']
    '\n    AdCP property identifier type, such as domain, app, CTV, DOOH, audio, radio, or network.\n    '
    value: str
    '\n    Identifier value for the selected AdCP property type.\n    '
    valueTruncated: NotRequired[Literal[True]]

class IdentifierPage(TypedDict):
    category: Literal['all', 'unresolved', 'registered']
    offset: int
    returned: int
    total: int
    items: list[Item2]
    nextOffset: NotRequired[int]
    valueTruncatedCount: NotRequired[int]

class Object4(TypedDict):
    id: str
    name: str
    purpose: Literal['include', 'exclude']
    '\n    Whether properties in this list should be included or excluded\n    '
    identifierCount: int
    unresolvedIdentifierCount: int
    registeredIdentifierCount: int
    identifierPage: IdentifierPage
    propertyCount: int
    filters: SavePropertyListSuccessPropertyListFilters | None
    createdAt: str
    updatedAt: str
    status: NotRequired[Literal['processing', 'ready', 'failed']]
    errorMessage: NotRequired[str]
    resolutionSummary: NotRequired[SavePropertyListSuccessPropertyListResolutionSummary]
    cascadeSummary: NotRequired[SavePropertyListSuccessPropertyListCascadeSummary]

class SavePropertyListResult2(TypedDict):
    action: Literal['created', 'updated']
    object: Object4

class SavePropertyListResult3(TypedDict):
    action: Literal['archived']
    propertyListId: str
SavePropertyListResult: TypeAlias = SavePropertyListResult1 | SavePropertyListResult2 | SavePropertyListResult3
SavePropertyListError: TypeAlias = V3ToolErrorResponse
CampaignId: TypeAlias = str

class FormatOptionRef(TypedDict):
    """
    Canonical format option; derived from creativeFormatId when supplied.
    """
    scope: Literal['publisher']
    '\n    Resolve this option from a publisher format catalog.\n    '
    publisher_domain: str
    '\n    Publisher domain that owns the catalog option.\n    '
    format_option_id: str
    '\n    Exact format option ID from the publisher catalog.\n    '

class FormatOptionRef1(TypedDict):
    """
    Canonical format option; derived from creativeFormatId when supplied.
    """
    scope: Literal['product']
    '\n    Resolve this option from the campaign product.\n    '
    format_option_id: str
    '\n    Exact format option ID declared inline by the product.\n    '

class Asset(TypedDict):
    url: NotRequired[SaveCreativeRequestAssetsItemUrl]
    '\n    Public URL for an already-hosted creative asset.\n    '
    dataUrl: NotRequired[str]
    '\n    Inline creative bytes as a base64 data URL.\n    '
    assetType: Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'TEXT', 'VAST']
    '\n    Type: IMAGE, VIDEO, AUDIO, HTML, TEXT, or VAST. ZIP requires inspected HTML5 ingestion.\n    '
    contentType: NotRequired[str]
    '\n    MIME type when it cannot be inferred.\n    '
    label: NotRequired[str]
    '\n    Human-readable asset label.\n    '
    makePrimary: NotRequired[bool]
    '\n    Make this primary. Allowed for IMAGE, VIDEO, AUDIO, HTML, or VAST; TEXT must remain subsidiary.\n    '

class SourceAssets(TypedDict):
    assetRef: str
    '\n    Owner-bound upload reference returned by upload_creative_asset.\n    '
    slot: NotRequired[SaveCreativeRequestSourceAssetsItemSlot]
    '\n    Format slot; repeatable members use group[index].member.\n    '
    label: NotRequired[SaveCreativeRequestSourceAssetsItemLabel]
    '\n    Human-readable label on this use of the asset.\n    '
    makePrimary: NotRequired[SaveCreativeRequestSourceAssetsItemMakePrimary]
    '\n    Whether this is the primary renderable asset.\n    '

class SourceAssets1(TypedDict):
    assetId: str
    '\n    Durable asset ID returned by upload_creative_asset or creative_asset search/get.\n    '
    slot: NotRequired[SaveCreativeRequestSourceAssetsItemSlot]
    '\n    Format slot; repeatable members use group[index].member.\n    '
    label: NotRequired[SaveCreativeRequestSourceAssetsItemLabel]
    '\n    Human-readable label on this use of the asset.\n    '
    makePrimary: NotRequired[SaveCreativeRequestSourceAssetsItemMakePrimary]
    '\n    Whether this is the primary renderable asset.\n    '

class Component(TypedDict):
    slot: str
    '\n    Declared slot; repeatable members use group[index].member.\n    '
    text: NotRequired[str]
    '\n    Text for a text slot.\n    '
    url: NotRequired[SaveCreativeRequestSocialComponentsItemUrl]
    '\n    URL for a URL slot.\n    '

class Social(TypedDict):
    """
    Authored social copy slots.
    """
    headline: NotRequired[str]
    '\n    Headline; slot headline.\n    '
    body: NotRequired[str]
    '\n    Primary/body text; slot body.\n    '
    description: NotRequired[str]
    '\n    Secondary description; slot description.\n    '
    callToAction: NotRequired[str]
    '\n    Call-to-action label; slot call_to_action.\n    '
    displayName: NotRequired[str]
    '\n    Brand/display name; slot display_name.\n    '
    components: NotRequired[list[Component]]
    '\n    Format-native slots by declared id; text or url each.\n    '

class SaveCreativeInput(TypedDict):
    creativeId: NotRequired[str]
    '\n    ID of the creative to update. Omit to create a new one.\n    '
    campaignId: NotRequired[str]
    '\n    Campaign to create the creative in. Required on create unless advertiserId is set.\n    '
    campaignIds: NotRequired[list[CampaignId]]
    '\n    All campaigns this creative runs on; replaces membership, a missing id detaches. Omit to keep.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser scope. Required on create when no campaignId, and on archive.\n    '
    mode: NotRequired[Literal['draft', 'complete']]
    '\n    Save a partial draft or validate and complete it. Omission preserves complete-save behaviour.\n    '
    expectedRevision: NotRequired[int]
    '\n    Current whole-state Creative stateRevision. Required for advertiser-scoped replacement.\n    '
    name: NotRequired[str]
    '\n    Creative name.\n    '
    message: NotRequired[str]
    '\n    Creative brief or direction.\n    '
    formatKind: NotRequired[Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']]
    '\n    Direct draft format.\n    '
    formatParams: NotRequired[dict[str, JsonValue]]
    '\n    Docs: Format parameters.\n    '
    formatOptionRef: NotRequired[FormatOptionRef | FormatOptionRef1]
    '\n    Canonical format option; derived from creativeFormatId when supplied.\n    '
    creativeFormatId: NotRequired[str]
    '\n    Signed product-bound selection. Do not combine with formatKind/formatParams.\n    '
    assets: NotRequired[list[Asset]]
    '\n    Unbound hosted or inline assets; at most one primary. They cannot satisfy formatOptionRef slots.\n    '
    sourceAssetRef: NotRequired[str]
    '\n    Finalized private JPEG/PNG; create-only with advertiserId/campaignId, not with assets/sourceAssets.\n    '
    sourceAssets: NotRequired[list[SourceAssets | SourceAssets1]]
    '\n    Finalized JPEG/PNG/promoted MP4 for formatOptionRef slots; supports pre-campaign advertiser scope.\n    '
    clickUrl: NotRequired[str]
    '\n    Click-through destination URL for this creative.\n    '
    macroAdditions: NotRequired[list[MacroAddition]]
    '\n    Creative URL parameters. Same keys override inherited values; null suppresses them.\n    '
    social: NotRequired[Social]
    '\n    Authored social copy slots.\n    '
    tags: NotRequired[list[Tag]]
    '\n    Tags; [] clears.\n    '
    labels: NotRequired[dict[str, list[Label]]]
    '\n    Dimension values; [] clears.\n    '
    isArchived: NotRequired[bool]
    '\n    true archives globally (frees the name); false is not supported.\n    '
    idempotencyKey: NotRequired[str]
    '\n    Stable key per call. Best-effort dedup - V2 creative endpoints are not exactly-once.\n    '

class Creative(TypedDict):
    creativeId: str
    stateRevision: int

class SaveCreativeResult1(TypedDict):
    action: Literal['created', 'updated']
    creative: Creative
    alreadyExisted: NotRequired[Literal[True]]
    assetAttachWarning: NotRequired[Literal[True]]
    assetsRequested: NotRequired[int]
    assetsAttached: NotRequired[int]
    clickUrlAttached: NotRequired[bool]
    providerContacted: NotRequired[Literal[False]]
    deliveryDeferredReason: NotRequired[Literal['destination_required']]
    warnings: NotRequired[list[str]]

class Membership1(TypedDict):
    campaignId: str

class SaveCreativeResult2(TypedDict):
    action: Literal['associated']
    creativeId: str
    membership: Membership1
    packageAssignmentAttempted: Literal[False]
    providerDeliveryAttempted: Literal[False]

class Membership2(TypedDict):
    campaignIds: list[str]

class SaveCreativeResult3(TypedDict):
    action: Literal['membership_updated']
    creativeId: str
    membership: Membership2
    attached: list[str]
    detached: list[str]

class Creative1(TypedDict):
    creativeId: str

class SaveCreativeResult4(TypedDict):
    action: Literal['archived']
    creative: Creative1
    nameReleased: Literal[True]
SaveCreativeResult: TypeAlias = SaveCreativeResult1 | SaveCreativeResult2 | SaveCreativeResult3 | SaveCreativeResult4
SaveCreativeError: TypeAlias = V3ToolErrorResponse

class SaveCreativeCollectionInput1(TypedDict):
    pass

class SaveCreativeCollectionInput3(TypedDict):
    collectionId: NotRequired[str]
    '\n    Collection ID; omit to create.\n    '
    campaignId: NotRequired[str]
    '\n    Campaign owner; required for campaign operations.\n    '
    advertiserId: NotRequired[str]
    '\n    Advertiser ID.\n    '
    expectedUpdatedAt: NotRequired[str]
    '\n    Advertiser collection revision.\n    '
    name: NotRequired[str]
    '\n    Collection name. Required on create.\n    '
    description: NotRequired[str | None]
    '\n    Description; null clears it on update.\n    '
    isArchived: NotRequired[bool]
    '\n    Archive or restore.\n    '
    parentId: NotRequired[str | None]
    '\n    Parent ID; null clears it.\n    '
    role: NotRequired[Literal['creative_library', 'source_assets', 'approved_set', 'test_set']]
    '\n    Campaign role; create-only; default creative_library.\n    '
    syncPolicy: NotRequired[Literal['manual', 'auto_include_new_members']]
    '\n    New-member sync; create-only; default manual.\n    '
    attachToCampaign: NotRequired[bool]
    '\n    Attach after creation; default true.\n    '
    addMemberIds: NotRequired[list[str]]
    '\n    Saved creative IDs added after create/update.\n    '
    removeMemberIds: NotRequired[list[str]]
    '\n    Saved creative IDs removed after create/update.\n    '
    idempotencyKey: NotRequired[str]
    '\n    Trace-only; writes are not exactly-once.\n    '

class SaveCreativeCollectionInput4(TypedDict):
    collectionId: NotRequired[str]
    campaignId: NotRequired[str]
    advertiserId: NotRequired[str]
    expectedUpdatedAt: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str | None]
    isArchived: NotRequired[bool]
    parentId: NotRequired[str | None]
    role: NotRequired[Literal['creative_library', 'source_assets', 'approved_set', 'test_set']]
    syncPolicy: NotRequired[Literal['manual', 'auto_include_new_members']]
    attachToCampaign: NotRequired[bool]
    addMemberIds: NotRequired[list[str]]
    removeMemberIds: NotRequired[list[str]]
    idempotencyKey: NotRequired[str]

class SaveCreativeCollectionInput5(TypedDict):
    collectionId: NotRequired[str]
    campaignId: NotRequired[str]
    advertiserId: NotRequired[str]
    expectedUpdatedAt: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str | None]
    isArchived: NotRequired[bool]
    parentId: NotRequired[str | None]
    role: NotRequired[Literal['creative_library', 'source_assets', 'approved_set', 'test_set']]
    syncPolicy: NotRequired[Literal['manual', 'auto_include_new_members']]
    attachToCampaign: NotRequired[bool]
    addMemberIds: NotRequired[list[str]]
    removeMemberIds: NotRequired[list[str]]
    idempotencyKey: NotRequired[str]
SaveCreativeCollectionInput: TypeAlias = SaveCreativeCollectionInput4 | SaveCreativeCollectionInput5

class Collection(TypedDict):
    collection_id: str
    campaign_id: NotRequired[str]
    advertiser_id: NotRequired[str]
    name: str
    member_count: int
    creative_count: int
    asset_count: int
    attached_campaign_count: int
    updated_at: str

class SaveCreativeCollectionResult1(TypedDict):
    action: Literal['created', 'updated', 'restored']
    collection: Collection
    added_count: NotRequired[int]
    removed_count: NotRequired[int]

class SaveCreativeCollectionResult2(TypedDict):
    action: Literal['archived']
    collectionId: str
    expectedUpdatedAt: str
SaveCreativeCollectionResult: TypeAlias = SaveCreativeCollectionResult1 | SaveCreativeCollectionResult2
SaveCreativeCollectionError: TypeAlias = V3ToolErrorResponse

class Engine(TypedDict):
    """
    Leave unset for funded image drafts unless user names an engine. See Creative Engines guide.
    """
    engineId: str
    '\n    Saved Creative Engine identifier.\n    '
    connectionId: str
    '\n    Saved engine connection identifier.\n    '

class Rights2(TypedDict):
    """
    Usage rights for the rendition.
    """
    status: NotRequired[Literal['unknown', 'owned', 'licensed', 'restricted', 'expired', 'inherited']]
    '\n    Rendition rights status.\n    '
    usage: NotRequired[SaveCreativeSessionRequestDraftRenditionsItemRightsUsage]
    '\n    Permitted asset usage.\n    '
    expires_at: NotRequired[SaveCreativeSessionRequestDraftRenditionsItemRightsExpiresAt]
    '\n    ISO timestamp when the asset rights expire.\n    '
    notes: NotRequired[SaveCreativeSessionRequestDraftRenditionsItemRightsNotes]
    '\n    Rights notes.\n    '
    source_asset_id: NotRequired[str]
    '\n    Asset from which rights are inherited.\n    '

class Provenance1(TypedDict):
    """
    How the rendition was produced.
    """
    method: NotRequired[Literal['background_removal', 'thumbnail_generation', 'original_has_alpha', 'render_crop']]
    '\n    Method used to create the rendition.\n    '
    provider: NotRequired[str]
    '\n    Provider that created the rendition.\n    '
    source_checksum: NotRequired[str]
    '\n    Checksum of the source asset.\n    '
    created_at: NotRequired[str]
    '\n    ISO timestamp when the rendition was created.\n    '

class Check1(TypedDict):
    code: str
    '\n    Quality check code.\n    '
    status: Literal['pass', 'warn', 'fail']
    '\n    Quality check status.\n    '
    detail: NotRequired[str]
    '\n    Quality check detail.\n    '

class Quality(TypedDict):
    """
    Rendition quality assessment.
    """
    status: Literal['approved', 'needs_review', 'failed']
    '\n    Overall rendition quality status.\n    '
    checks: NotRequired[list[Check1]]
    '\n    Individual rendition quality checks.\n    '

class Rendition(TypedDict):
    asset_id: str
    '\n    Rendition asset identifier.\n    '
    parent_asset_id: str
    '\n    Identifier of the source asset.\n    '
    rendition_type: Literal['transparent_cutout', 'thumbnail', 'render_crop']
    '\n    Kind of derived rendition.\n    '
    label: str
    '\n    Human-readable rendition label.\n    '
    url: str
    '\n    Rendition URL.\n    '
    source: NotRequired[SaveCreativeSessionRequestDraftRenditionsItemSource]
    '\n    Where the rendition originated.\n    '
    role: NotRequired[SaveCreativeSessionRequestDraftRenditionsItemRole]
    '\n    How the rendition is used in the creative.\n    '
    mime_type: NotRequired[str]
    '\n    Rendition media type.\n    '
    width: NotRequired[int]
    '\n    Rendition width in pixels.\n    '
    height: NotRequired[int]
    '\n    Rendition height in pixels.\n    '
    alpha: NotRequired[bool]
    '\n    Whether the rendition includes transparency.\n    '
    locked_asset: NotRequired[bool]
    '\n    Whether the rendition must be preserved.\n    '
    can_transform: NotRequired[bool]
    '\n    Whether the rendition may be transformed.\n    '
    rights: NotRequired[Rights2]
    '\n    Usage rights for the rendition.\n    '
    provenance: NotRequired[Provenance1]
    '\n    How the rendition was produced.\n    '
    quality: NotRequired[Quality]
    '\n    Rendition quality assessment.\n    '

class SaveCreativeSessionInput2(TypedDict):
    operation: Literal['select_output']
    '\n    Select one generated output.\n    '
    campaignId: str
    '\n    Campaign that owns the Creative Session.\n    '
    sessionId: str
    '\n    Creative Session identifier.\n    '
    variantId: str
    '\n    Exact generated output to select.\n    '
    expectedRevision: int
    '\n    Session revision being changed.\n    '
    idempotencyKey: NotRequired[str]
    '\n    Optional idempotency key for this selection.\n    '

class SaveCreativeSessionInput3(TypedDict):
    operation: Literal['approve_output']
    '\n    Approve one selected output for finalisation.\n    '
    campaignId: str
    '\n    Campaign that owns the Creative Session.\n    '
    sessionId: str
    '\n    Creative Session identifier.\n    '
    variantId: str
    '\n    Exact selected output to approve.\n    '
    expectedRevision: int
    '\n    Session revision being approved.\n    '
    idempotencyKey: NotRequired[str]
    '\n    Optional idempotency key for this approval.\n    '

class SaveCreativeSessionInput4(TypedDict):
    operation: Literal['finalize_approved_output']
    '\n    Finalise the exact approved output.\n    '
    campaignId: str
    '\n    Campaign that owns the Creative Session.\n    '
    sessionId: str
    '\n    Creative Session identifier.\n    '
    approvedVariantId: str
    '\n    Exact approved output identifier.\n    '
    approvedSessionRevision: int
    '\n    Revision that recorded the approval.\n    '
    name: NotRequired[str]
    '\n    Optional final Creative name.\n    '
    message: NotRequired[str]
    '\n    Optional finalisation message.\n    '

class SaveCreativeSessionInput5(TypedDict):
    operation: Literal['promote_approved_output']
    '\n    Promote one exact approved output into a Creative Asset revision.\n    '
    campaignId: str
    '\n    Campaign that owns the Creative Session.\n    '
    sessionId: str
    '\n    Creative Session identifier.\n    '
    advertiserId: str
    '\n    Advertiser that will own the promoted Creative Asset.\n    '
    variantId: str
    '\n    Exact approved output identifier.\n    '
    sessionRevision: int
    '\n    Session revision that recorded the approval.\n    '
    outputHash: str
    '\n    SHA-256 digest recorded by the exact output approval.\n    '
    idempotencyKey: str
    '\n    Idempotency key for this promotion.\n    '

class SaveCreativeSessionResult1(TypedDict):
    nextGenerateVariants: NotRequired[SaveCreativeSessionSuccessCreativeSessionNextGenerateVariants]
    session: SaveCreativeSessionSuccessCreativeSessionDetail
    sessionTruncated: NotRequired[SaveCreativeSessionSuccessCreativeSessionTruncated]
    sessionOmitted: NotRequired[SaveCreativeSessionSuccessCreativeSessionOmitted]
    revision: SaveCreativeSessionSuccessCreativeSessionRevision
    sessionGeneration: NotRequired[SaveCreativeSessionSuccessCreativeSessionGeneration]
    gallery: NotRequired[SaveCreativeSessionSuccessCreativeSessionGallery]
    operation: Literal['saved_draft']

class SaveCreativeSessionResult2(TypedDict):
    nextGenerateVariants: NotRequired[SaveCreativeSessionSuccessCreativeSessionNextGenerateVariants]
    session: SaveCreativeSessionSuccessCreativeSessionDetail
    sessionTruncated: NotRequired[SaveCreativeSessionSuccessCreativeSessionTruncated]
    sessionOmitted: NotRequired[SaveCreativeSessionSuccessCreativeSessionOmitted]
    revision: SaveCreativeSessionSuccessCreativeSessionRevision
    sessionGeneration: NotRequired[SaveCreativeSessionSuccessCreativeSessionGeneration]
    gallery: NotRequired[SaveCreativeSessionSuccessCreativeSessionGallery]
    operation: Literal['selected_output']

class SaveCreativeSessionResult3(TypedDict):
    nextGenerateVariants: NotRequired[SaveCreativeSessionSuccessCreativeSessionNextGenerateVariants]
    session: SaveCreativeSessionSuccessCreativeSessionDetail
    sessionTruncated: NotRequired[SaveCreativeSessionSuccessCreativeSessionTruncated]
    sessionOmitted: NotRequired[SaveCreativeSessionSuccessCreativeSessionOmitted]
    revision: SaveCreativeSessionSuccessCreativeSessionRevision
    sessionGeneration: NotRequired[SaveCreativeSessionSuccessCreativeSessionGeneration]
    gallery: NotRequired[SaveCreativeSessionSuccessCreativeSessionGallery]
    operation: Literal['approved_output']

class SaveCreativeSessionResult4(TypedDict):
    nextGenerateVariants: NotRequired[SaveCreativeSessionSuccessCreativeSessionNextGenerateVariants]
    session: SaveCreativeSessionSuccessCreativeSessionDetail
    sessionTruncated: NotRequired[SaveCreativeSessionSuccessCreativeSessionTruncated]
    sessionOmitted: NotRequired[SaveCreativeSessionSuccessCreativeSessionOmitted]
    revision: SaveCreativeSessionSuccessCreativeSessionRevision
    sessionGeneration: NotRequired[SaveCreativeSessionSuccessCreativeSessionGeneration]
    gallery: NotRequired[SaveCreativeSessionSuccessCreativeSessionGallery]
    operation: Literal['finalized_output']

class SaveCreativeSessionResult5(TypedDict):
    nextGenerateVariants: NotRequired[SaveCreativeSessionSuccessCreativeSessionNextGenerateVariants]
    operation: Literal['promoted_approved_output']
    assetUid: str
    revisionUid: str
    sha256: str
    receiptUid: str
SaveCreativeSessionResult: TypeAlias = SaveCreativeSessionResult1 | SaveCreativeSessionResult2 | SaveCreativeSessionResult3 | SaveCreativeSessionResult4 | SaveCreativeSessionResult5
SaveCreativeSessionError: TypeAlias = V3ToolErrorResponse

class GenerateVariantsInput1(TypedDict):
    campaignId: GenerateVariantsRequestCampaignId
    sessionId: GenerateVariantsRequestSessionId
    actionKey: GenerateVariantsRequestActionKey
    expectedRevision: GenerateVariantsRequestExpectedRevision
    sessionGeneration: GenerateVariantsRequestSessionGeneration

class GenerateVariantsInput2(TypedDict):
    campaignId: GenerateVariantsRequestCampaignId
    sessionId: GenerateVariantsRequestSessionId
    actionKey: GenerateVariantsRequestActionKey
    expectedRevision: GenerateVariantsRequestExpectedRevision
    sessionGeneration: GenerateVariantsRequestSessionGeneration
    parentVariantId: str
    feedback: str
GenerateVariantsInput: TypeAlias = GenerateVariantsInput1 | GenerateVariantsInput2

class Leaf(TypedDict):
    leafId: str
    status: Literal['pending', 'dispatching', 'submitted', 'completed', 'uncertain', 'not_dispatched']
    taskId: NotRequired[str]
    variantIds: NotRequired[list[str]]

class Asset1(TypedDict):
    url: str
    width: NotRequired[float]
    height: NotRequired[float]
    mimeType: str

class Preview2(TypedDict):
    type: str
    url: str

class CompletedVariant(TypedDict):
    variantId: str
    asset: Asset1
    preview: Preview2

class Arguments6(TypedDict):
    kind: Literal['creative_session']
    id: str
    sourceId: str

class Poll(TypedDict):
    tool: Literal['get']
    arguments: Arguments6

class Preview3(TypedDict):
    type: str
    url: str
    width: NotRequired[float]
    height: NotRequired[float]

class Variant1(TypedDict):
    id: str
    name: str
    direction: NotRequired[str]
    status: NotRequired[str]
    preview: Preview3

class Gallery(TypedDict):
    campaignId: str
    sessionId: str
    advertiserId: NotRequired[str]
    revision: int
    sessionGeneration: NotRequired[str]
    variants: list[Variant1]
    selectedVariantId: NotRequired[str]
    approvedVariantId: NotRequired[str]
    approvedSessionRevision: NotRequired[int]
    approvedOutputHash: NotRequired[str]
    finalCreativeId: NotRequired[str]
    generationPending: bool
    terminal: NotRequired[Terminal]

class GenerateVariantsResult(TypedDict):
    actionId: str
    session: dict[str, JsonValue]
    sessionTruncated: NotRequired[Literal[True]]
    sessionOmitted: NotRequired[dict[str, int]]
    revision: int
    sessionGeneration: NotRequired[str]
    leaves: list[Leaf]
    completedVariants: NotRequired[list[CompletedVariant]]
    terminal: NotRequired[Terminal]
    poll: NotRequired[Poll]
    gallery: NotRequired[Gallery]
GenerateVariantsError: TypeAlias = V3ToolErrorResponse

class SaveMediaBuyInput1(TypedDict):
    pass

class GeoMetro1(TypedDict):
    """
    Nielsen DMA groups to include.
    """
    system: Literal['nielsen_dma', 'uk_itl1', 'uk_itl2', 'eurostat_nuts2', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoMetrosExcludeItem(TypedDict):
    """
    Nielsen DMA groups to exclude.
    """
    system: Literal['nielsen_dma', 'uk_itl1', 'uk_itl2', 'eurostat_nuts2', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['US']
    '\n    Country code for this area.\n    '
    system: Literal['zip', 'zip_plus_four']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas1(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['GB']
    '\n    Country code for this area.\n    '
    system: Literal['outward', 'full']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas2(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['CA']
    '\n    Country code for this area.\n    '
    system: Literal['full', 'fsa']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas3(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['DE', 'CH', 'AT']
    '\n    Country code for this area.\n    '
    system: Literal['plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas4(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['FR']
    '\n    Country code for this area.\n    '
    system: Literal['code_postal']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas5(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['AU']
    '\n    Country code for this area.\n    '
    system: Literal['postcode']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas6(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['BR']
    '\n    Country code for this area.\n    '
    system: Literal['cep']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas7(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['IN']
    '\n    Country code for this area.\n    '
    system: Literal['pin']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas8(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['ZA']
    '\n    Country code for this area.\n    '
    system: Literal['postal_code']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas9(TypedDict):
    """
    Postal areas to include.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['postal_code', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas10(TypedDict):
    """
    Postal areas to include.
    """
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['US']
    '\n    Country code for this area.\n    '
    system: Literal['zip', 'zip_plus_four']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude1(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['GB']
    '\n    Country code for this area.\n    '
    system: Literal['outward', 'full']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude2(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['CA']
    '\n    Country code for this area.\n    '
    system: Literal['full', 'fsa']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude3(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['DE', 'CH', 'AT']
    '\n    Country code for this area.\n    '
    system: Literal['plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude4(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['FR']
    '\n    Country code for this area.\n    '
    system: Literal['code_postal']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude5(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['AU']
    '\n    Country code for this area.\n    '
    system: Literal['postcode']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude6(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['BR']
    '\n    Country code for this area.\n    '
    system: Literal['cep']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude7(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['IN']
    '\n    Country code for this area.\n    '
    system: Literal['pin']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude8(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['ZA']
    '\n    Country code for this area.\n    '
    system: Literal['postal_code']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude9(TypedDict):
    """
    Postal areas to exclude.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['postal_code', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude10(TypedDict):
    """
    Postal areas to exclude.
    """
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '
Value3: TypeAlias = str
'\nValues in this targeting system.\n'

class GeoPlace1(TypedDict):
    """
    Named geographic places to include.
    """
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Targeting system identifier.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this targeting system.\n    '
    country: NotRequired[JsonValue]
    '\n    Country code for this area.\n    '
    system_version: NotRequired[JsonValue]
    '\n    Targeting-system version.\n    '
    place_type: NotRequired[JsonValue]
    '\n    Geographic place category.\n    '
    value_labels: NotRequired[JsonValue]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[JsonValue]
    '\n    AdCP extension values.\n    '

class GeoPlace2(TypedDict):
    """
    Named geographic places to include.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Targeting system identifier.\n    '
    system_version: NotRequired[str]
    '\n    Targeting-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Geographic place category.\n    '
    values: list[Value3]
    '\n    Values in this targeting system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class GeoPlace3(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlace: TypeAlias = GeoPlace3
'\nNamed geographic places to include.\n'

class GeoPlacesExcludeItem1(TypedDict):
    """
    Named geographic places to exclude.
    """
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Targeting system identifier.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this targeting system.\n    '
    country: NotRequired[JsonValue]
    '\n    Country code for this area.\n    '
    system_version: NotRequired[JsonValue]
    '\n    Targeting-system version.\n    '
    place_type: NotRequired[JsonValue]
    '\n    Geographic place category.\n    '
    value_labels: NotRequired[JsonValue]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[JsonValue]
    '\n    AdCP extension values.\n    '

class GeoPlacesExcludeItem2(TypedDict):
    """
    Named geographic places to exclude.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Targeting system identifier.\n    '
    system_version: NotRequired[str]
    '\n    Targeting-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Geographic place category.\n    '
    values: list[Value3]
    '\n    Values in this targeting system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class GeoPlacesExcludeItem3(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlacesExcludeItem: TypeAlias = GeoPlacesExcludeItem3
'\nNamed geographic places to exclude.\n'

class DaypartTarget1(TypedDict):
    """
    Time windows when delivery is allowed.
    """
    days: list[Literal['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]
    '\n    Days covered by the window.\n    '
    start_hour: int
    '\n    Window start hour.\n    '
    end_hour: int
    '\n    Window end hour.\n    '
    timezone: NotRequired[Literal['inventory_local'] | JsonValue]
    '\n    IANA timezone for the window.\n    '
    label: NotRequired[str]
    '\n    Optional human-readable label.\n    '

class Age7(TypedDict):
    """
    Audience age range.
    """
    min: NotRequired[int]
    '\n    Minimum permitted age.\n    '
    max: NotRequired[int]
    '\n    Maximum permitted age.\n    '
    include_unknown: bool
    '\n    Whether unknown ages are included.\n    '
    accepted_bases: NotRequired[list[Literal['verified', 'declared', 'inferred']]]
    '\n    Accepted age-data bases.\n    '
    accepted_verification_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]
    '\n    Accepted age verification methods.\n    '

class Demographics2(TypedDict):
    """
    demographics reject before dispatch.
    """
    age: Age7
    '\n    Audience age range.\n    '

class Suppress(TypedDict):
    """
    Whether to suppress delivery after the cap.
    """
    interval: int
    '\n    Number of time units.\n    '
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
    '\n    Time unit.\n    '

class Window4(TypedDict):
    """
    Frequency-cap window size.
    """
    interval: int
    '\n    Number of time units.\n    '
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
    '\n    Time unit.\n    '

class FrequencyCap11(TypedDict):
    """
    Package impression frequency limit.
    """
    suppress: JsonValue
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    max_impressions: NotRequired[JsonValue]
    '\n    Maximum impressions in the window.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[JsonValue]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap12(TypedDict):
    """
    Package impression frequency limit.
    """
    window: JsonValue
    '\n    Frequency-cap window size.\n    '
    max_impressions: JsonValue
    '\n    Maximum impressions in the window.\n    '
    suppress: NotRequired[JsonValue]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '

class FrequencyCap13(TypedDict):
    """
    Package impression frequency limit.
    """
    max_impressions: JsonValue
    '\n    Maximum impressions in the window.\n    '
    suppress: NotRequired[JsonValue]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[JsonValue]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap14(TypedDict):
    """
    Package impression frequency limit.
    """
    suppress: NotRequired[Suppress]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[float]
    '\n    Suppression duration in minutes.\n    '
    max_impressions: NotRequired[int]
    '\n    Maximum impressions in the window.\n    '
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[Window4]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap15(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window4]

class FrequencyCap16(TypedDict):
    window: NotRequired[Window4]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]

class FrequencyCap17(TypedDict):
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window4]

class FrequencyCap18(TypedDict):
    window: NotRequired[Window4]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
FrequencyCap1: TypeAlias = FrequencyCap15 | FrequencyCap16 | FrequencyCap17 | FrequencyCap18
'\nPackage impression frequency limit.\n'

class PropertyList(TypedDict):
    """
    Property-list reference to include.
    """
    agent_url: str
    '\n    Seller agent URL.\n    '
    list_id: str
    '\n    Seller list ID.\n    '
    auth_token: NotRequired[str]
    '\n    Seller authorization token.\n    '

class PropertyListExclude(TypedDict):
    """
    Property-list reference to exclude.
    """
    agent_url: str
    '\n    Seller agent URL.\n    '
    list_id: str
    '\n    Seller list ID.\n    '
    auth_token: NotRequired[str]
    '\n    Seller authorization token.\n    '

class CollectionList(TypedDict):
    """
    Collection-list reference to include.
    """
    agent_url: str
    '\n    Seller agent URL.\n    '
    list_id: str
    '\n    Seller list ID.\n    '
    auth_token: NotRequired[str]
    '\n    Seller authorization token.\n    '

class CollectionListExclude(TypedDict):
    """
    Collection-list reference to exclude.
    """
    agent_url: str
    '\n    Seller agent URL.\n    '
    list_id: str
    '\n    Seller list ID.\n    '
    auth_token: NotRequired[str]
    '\n    Seller authorization token.\n    '

class AgeRestriction1(TypedDict):
    """
    Minimum audience age and verification.
    """
    min: int
    '\n    Minimum permitted age.\n    '
    verification_required: NotRequired[bool]
    '\n    Whether age verification is required.\n    '
    accepted_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]
    '\n    Accepted age verification methods.\n    '

class StoreCatchment(TypedDict):
    """
    Store or catchment identifiers.
    """
    catalog_id: str
    '\n    Store-catchment catalog ID.\n    '
    store_ids: NotRequired[list[str]]
    '\n    Store identifiers.\n    '
    catchment_ids: NotRequired[list[str]]
    '\n    Catchment identifiers.\n    '

class TravelTime1(TypedDict):
    """
    Maximum travel time.
    """
    value: float
    '\n    Numeric value.\n    '
    unit: Literal['min', 'hr']
    '\n    Time unit.\n    '

class Radius1(TypedDict):
    """
    Radius around this area.
    """
    value: float
    '\n    Numeric value.\n    '
    unit: Literal['km', 'mi', 'm']
    '\n    Time unit.\n    '

class GeoProximityItem1(TypedDict):
    """
    Proximity areas to include.
    """
    lat: NotRequired[float]
    '\n    Latitude in decimal degrees.\n    '
    lng: NotRequired[float]
    '\n    Longitude in decimal degrees.\n    '
    label: NotRequired[str]
    '\n    Optional human-readable label.\n    '
    travel_time: NotRequired[TravelTime1]
    '\n    Maximum travel time.\n    '
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    '\n    Travel mode for this area.\n    '
    radius: NotRequired[Radius1]
    '\n    Radius around this area.\n    '
    geometry: NotRequired[Geometry2]
    '\n    Geographic boundary.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '
LanguageItem2: TypeAlias = str
'\nLanguage codes to include.\n'

class KeywordTarget(TypedDict):
    """
    Keyword targets and bid prices.
    """
    keyword: str
    '\n    Keyword text.\n    '
    match_type: Literal['broad', 'phrase', 'exact']
    '\n    Keyword matching mode.\n    '
    bid_price: NotRequired[float]
    '\n    Bid price for this keyword.\n    '

class NegativeKeyword(TypedDict):
    """
    Keywords to exclude.
    """
    keyword: str
    '\n    Keyword text.\n    '
    match_type: Literal['broad', 'phrase', 'exact']
    '\n    Keyword matching mode.\n    '

class Signals(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['binary']
    '\n    Targeting detail.\n    '
    value: Literal[True]
    '\n    Numeric value.\n    '

class Signals1(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['categorical']
    '\n    Targeting detail.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class Signals2(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['numeric']
    '\n    Targeting detail.\n    '
    min_value: NotRequired[float]
    '\n    Targeting detail.\n    '
    max_value: NotRequired[float]
    '\n    Targeting detail.\n    '

class Group(TypedDict):
    """
    Signal groups to combine.
    """
    operator: Literal['any', 'none']
    '\n    How child selections combine.\n    '
    signals: list[Signals | Signals1 | Signals2]
    '\n    Signals in this group.\n    '

class SignalTargetingGroups(TypedDict):
    """
    Signal groups and their selection mode.
    """
    operator: Literal['all']
    '\n    How child selections combine.\n    '
    groups: list[Group]
    '\n    Signal groups to combine.\n    '

class TargetingOverlay1(TypedDict):
    """
    Deprecated. Numeric codes replace names; AI-10440 removal will have at least 14 days notice.
    """
    geo_metros: NotRequired[list[GeoMetro1]]
    '\n    Nielsen DMA groups to include.\n    '
    geo_metros_exclude: NotRequired[list[GeoMetrosExcludeItem]]
    '\n    Nielsen DMA groups to exclude.\n    '
    geo_postal_areas: NotRequired[list[GeoPostalAreas | GeoPostalAreas1 | GeoPostalAreas2 | GeoPostalAreas3 | GeoPostalAreas4 | GeoPostalAreas5 | GeoPostalAreas6 | GeoPostalAreas7 | GeoPostalAreas8 | GeoPostalAreas9 | GeoPostalAreas10]]
    '\n    Postal areas to include.\n    '
    geo_postal_areas_exclude: NotRequired[list[GeoPostalAreasExclude | GeoPostalAreasExclude1 | GeoPostalAreasExclude2 | GeoPostalAreasExclude3 | GeoPostalAreasExclude4 | GeoPostalAreasExclude5 | GeoPostalAreasExclude6 | GeoPostalAreasExclude7 | GeoPostalAreasExclude8 | GeoPostalAreasExclude9 | GeoPostalAreasExclude10]]
    '\n    Postal areas to exclude.\n    '
    geo_places: NotRequired[list[GeoPlace]]
    '\n    Named geographic places to include.\n    '
    geo_places_exclude: NotRequired[list[GeoPlacesExcludeItem]]
    '\n    Named geographic places to exclude.\n    '
    daypart_targets: NotRequired[list[DaypartTarget1]]
    '\n    Time windows when delivery is allowed.\n    '
    axe_include_segment: NotRequired[str]
    '\n    AXE segment IDs to include.\n    '
    axe_exclude_segment: NotRequired[str]
    '\n    AXE segment IDs to exclude.\n    '
    audience_include: NotRequired[list[str]]
    '\n    Audience segment IDs to include.\n    '
    audience_exclude: NotRequired[list[str]]
    '\n    Audience segment IDs to exclude.\n    '
    demographics: NotRequired[Demographics2]
    '\n    demographics reject before dispatch.\n    '
    frequency_cap: NotRequired[FrequencyCap1]
    '\n    Package impression frequency limit.\n    '
    property_list: NotRequired[PropertyList]
    '\n    Property-list reference to include.\n    '
    property_list_exclude: NotRequired[PropertyListExclude]
    '\n    Property-list reference to exclude.\n    '
    collection_list: NotRequired[CollectionList]
    '\n    Collection-list reference to include.\n    '
    collection_list_exclude: NotRequired[CollectionListExclude]
    '\n    Collection-list reference to exclude.\n    '
    placement_selection: NotRequired[dict[str, JsonValue]]
    '\n    Placement selection reference.\n    '
    collection_selection: NotRequired[dict[str, JsonValue]]
    '\n    Collection selection reference.\n    '
    age_restriction: NotRequired[AgeRestriction1]
    '\n    Minimum audience age and verification.\n    '
    device_platform: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    '\n    Device platforms to include.\n    '
    device_platform_exclude: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    '\n    Device platforms to exclude.\n    '
    device_type: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Device types to include.\n    '
    device_type_exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Device types to exclude.\n    '
    browser: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    '\n    Browsers to include.\n    '
    browser_exclude: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    '\n    Browsers to exclude.\n    '
    store_catchments: NotRequired[list[StoreCatchment]]
    '\n    Store or catchment identifiers.\n    '
    geo_proximity: NotRequired[list[GeoProximityItem1]]
    '\n    Proximity areas to include.\n    '
    language: NotRequired[list[LanguageItem2]]
    '\n    Language codes to include.\n    '
    keyword_targets: NotRequired[list[KeywordTarget]]
    '\n    Keyword targets and bid prices.\n    '
    negative_keywords: NotRequired[list[NegativeKeyword]]
    '\n    Keywords to exclude.\n    '
    signal_targeting_groups: NotRequired[SignalTargetingGroups]
    '\n    Signal groups and their selection mode.\n    '
    geo_countries: NotRequired[list[str]]
    '\n    Country codes or names.\n    '
    geo_countries_exclude: NotRequired[list[str]]
    '\n    Country codes or names to exclude.\n    '
    geo_regions: NotRequired[list[str]]
    '\n    Subdivision codes or names.\n    '
    geo_regions_exclude: NotRequired[list[str]]
    '\n    Subdivision codes or names to exclude.\n    '

class Vendor1(TypedDict):
    """
    Optional measurement vendor.
    """
    domain: str
    '\n    Vendor brand domain.\n    '
    brand_id: NotRequired[str]
    '\n    Optional vendor brand ID.\n    '

class PerformanceStandard(TypedDict):
    metric: Literal['viewability', 'ivt', 'completion_rate', 'brand_safety', 'attention_score']
    '\n    Quality metric to commit.\n    '
    threshold: float
    '\n    Value from 0 to 1.\n    '
    standard: NotRequired[Literal['MRC', 'GroupM']]
    '\n    Required for viewability only.\n    '
    vendor: NotRequired[Vendor1]
    '\n    Optional measurement vendor.\n    '

class Product(TypedDict):
    productId: str
    '\n    Qualified ID returned by discovery. Pass it unchanged.\n    '
    selectionId: NotRequired[str]
    '\n    Create only: give repeats of one productId distinct values to add separate line items.\n    '
    inventorySourceId: NotRequired[str]
    '\n    Returned inventory source ID. Pass unchanged when present to keep modular products unambiguous.\n    '
    salesAgentId: NotRequired[str]
    '\n    Returned sales agent ID. Pass unchanged when present to preserve the selected seller route.\n    '
    pricingOptionId: NotRequired[str]
    '\n    Returned Product pricing option ID. Pass unchanged when present.\n    '
    budget: NotRequired[float]
    '\n    Per-product budget. Required with fixed allocation; refused with seller_optimized.\n    '
    bidPrice: NotRequired[float]
    '\n    Bid in campaign currency. Required for auction products; omit for fixed-price.\n    '
    targetingOverlay: NotRequired[TargetingOverlay1]
    '\n    Deprecated. Numeric codes replace names; AI-10440 removal will have at least 14 days notice.\n    '
    performanceStandards: NotRequired[list[PerformanceStandard] | None]
    '\n    Package standards. Viewability: MRC/GroupM. IVT ceiling; others floors. Update: null/[] clears.\n    '
    pixelId: NotRequired[str]
    '\n    Meta Pixel/Dataset ID for conversion tracking. Required for Meta Sales; no auto-select.\n    '
    remove: NotRequired[bool]
    '\n    Update only: true removes this line item.\n    '
    lineItemRef: NotRequired[str]
    '\n    Update only: line-item handle from the read; needed for a repeated product.\n    '

class Budget8(TypedDict):
    """
    Single total. One-allocation proposal allowed; multi: products[].budget; else retain allocation.
    """
    total: float
    '\n    Total budget amount.\n    '
    currency: str
    '\n    ISO 4217 currency code (e.g. USD).\n    '

class BudgetAllocation(TypedDict):
    """
    New-media-buy-only allocation: fixed requires products[].budget; seller_optimized refuses it.
    """
    mode: Literal['fixed']
    '\n    Keep the stated per-package budgets.\n    '

class TargetFrequency(TypedDict):
    """
    Desired exposure frequency and window.
    """
    min: NotRequired[int]
    '\n    Minimum exposures in the window.\n    '
    max: NotRequired[int]
    '\n    Maximum exposures in the window.\n    '
    window: SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetFrequencyWindow

class EventSource2(TypedDict):
    event_source_id: str
    '\n    Identifier of the event source.\n    '
    event_type: Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']
    '\n    Tracked event type to optimize.\n    '
    custom_event_name: NotRequired[str]
    '\n    Custom event name when event_type is custom.\n    '
    value_field: NotRequired[str]
    '\n    Event property containing its value.\n    '
    value_factor: NotRequired[float]
    '\n    Multiplier applied to the event value.\n    '

class Target5(TypedDict):
    """
    Optional conversion outcome target.
    """
    kind: Literal['per_ad_spend']
    '\n    Optimize value relative to ad spend.\n    '
    value: SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetValue
    '\n    Positive value per ad-spend target.\n    '
    strength: NotRequired[Literal['floor', 'target']]
    '\n    Use a minimum floor or delivery target.\n    '

class Target6(TypedDict):
    """
    Optional conversion outcome target.
    """
    kind: Literal['maximize_value']
    '\n    Maximize attributed event value.\n    '

class AttributionWindow(TypedDict):
    """
    Optional event attribution settings.
    """
    post_click: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemAttributionWindowPostClick]
    '\n    Attribution window after a click.\n    '
    post_view: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemAttributionWindowPostView]
    '\n    Attribution window after a view.\n    '
    model: NotRequired[Literal['last_touch', 'first_touch', 'linear', 'time_decay', 'data_driven']]
    '\n    Attribution model to apply.\n    '

class Vendor2(TypedDict):
    """
    Vendor that owns the metric definition.
    """
    domain: str
    '\n    Vendor domain that defines the metric.\n    '
    brand_id: NotRequired[str]
    '\n    Optional vendor brand identifier.\n    '

class Flight1(TypedDict):
    """
    Flight for a new or existing draft. Specific starts need a future UTC day; use "asap" to start now.
    """
    startAt: str
    '\n    ISO 8601 start date-time or "asap".\n    '
    endAt: str
    '\n    ISO 8601 end date-time.\n    '

class GeoPostalAreas11(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['US']
    '\n    Country code for this area.\n    '
    system: Literal['zip', 'zip_plus_four']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas12(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['GB']
    '\n    Country code for this area.\n    '
    system: Literal['outward', 'full']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas13(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['CA']
    '\n    Country code for this area.\n    '
    system: Literal['full', 'fsa']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas14(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['DE', 'CH', 'AT']
    '\n    Country code for this area.\n    '
    system: Literal['plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas15(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['FR']
    '\n    Country code for this area.\n    '
    system: Literal['code_postal']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas16(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['AU']
    '\n    Country code for this area.\n    '
    system: Literal['postcode']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas17(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['BR']
    '\n    Country code for this area.\n    '
    system: Literal['cep']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas18(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['IN']
    '\n    Country code for this area.\n    '
    system: Literal['pin']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas19(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['ZA']
    '\n    Country code for this area.\n    '
    system: Literal['postal_code']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas20(TypedDict):
    """
    Postal areas to include.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['postal_code', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas21(TypedDict):
    """
    Postal areas to include.
    """
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude11(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['US']
    '\n    Country code for this area.\n    '
    system: Literal['zip', 'zip_plus_four']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude12(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['GB']
    '\n    Country code for this area.\n    '
    system: Literal['outward', 'full']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude13(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['CA']
    '\n    Country code for this area.\n    '
    system: Literal['full', 'fsa']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude14(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['DE', 'CH', 'AT']
    '\n    Country code for this area.\n    '
    system: Literal['plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude15(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['FR']
    '\n    Country code for this area.\n    '
    system: Literal['code_postal']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude16(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['AU']
    '\n    Country code for this area.\n    '
    system: Literal['postcode']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude17(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['BR']
    '\n    Country code for this area.\n    '
    system: Literal['cep']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude18(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['IN']
    '\n    Country code for this area.\n    '
    system: Literal['pin']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude19(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['ZA']
    '\n    Country code for this area.\n    '
    system: Literal['postal_code']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude20(TypedDict):
    """
    Postal areas to exclude.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['postal_code', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude21(TypedDict):
    """
    Postal areas to exclude.
    """
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPlace41(TypedDict):
    """
    Named geographic places to include.
    """
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Targeting system identifier.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this targeting system.\n    '
    country: NotRequired[JsonValue]
    '\n    Country code for this area.\n    '
    system_version: NotRequired[JsonValue]
    '\n    Targeting-system version.\n    '
    place_type: NotRequired[JsonValue]
    '\n    Geographic place category.\n    '
    value_labels: NotRequired[JsonValue]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[JsonValue]
    '\n    AdCP extension values.\n    '

class GeoPlace42(TypedDict):
    """
    Named geographic places to include.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Targeting system identifier.\n    '
    system_version: NotRequired[str]
    '\n    Targeting-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Geographic place category.\n    '
    values: list[Value3]
    '\n    Values in this targeting system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class GeoPlace43(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlace4: TypeAlias = GeoPlace43
'\nNamed geographic places to include.\n'

class GeoPlacesExcludeItem41(TypedDict):
    """
    Named geographic places to exclude.
    """
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Targeting system identifier.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this targeting system.\n    '
    country: NotRequired[JsonValue]
    '\n    Country code for this area.\n    '
    system_version: NotRequired[JsonValue]
    '\n    Targeting-system version.\n    '
    place_type: NotRequired[JsonValue]
    '\n    Geographic place category.\n    '
    value_labels: NotRequired[JsonValue]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[JsonValue]
    '\n    AdCP extension values.\n    '

class GeoPlacesExcludeItem42(TypedDict):
    """
    Named geographic places to exclude.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Targeting system identifier.\n    '
    system_version: NotRequired[str]
    '\n    Targeting-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Geographic place category.\n    '
    values: list[Value3]
    '\n    Values in this targeting system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class GeoPlacesExcludeItem43(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlacesExcludeItem4: TypeAlias = GeoPlacesExcludeItem43
'\nNamed geographic places to exclude.\n'

class Demographics3(TypedDict):
    """
    demographics reject before dispatch.
    """
    age: Age7
    '\n    Audience age range.\n    '

class FrequencyCap21(TypedDict):
    """
    Package impression frequency limit.
    """
    suppress: JsonValue
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    max_impressions: NotRequired[JsonValue]
    '\n    Maximum impressions in the window.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[JsonValue]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap22(TypedDict):
    """
    Package impression frequency limit.
    """
    window: JsonValue
    '\n    Frequency-cap window size.\n    '
    max_impressions: JsonValue
    '\n    Maximum impressions in the window.\n    '
    suppress: NotRequired[JsonValue]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '

class FrequencyCap23(TypedDict):
    """
    Package impression frequency limit.
    """
    max_impressions: JsonValue
    '\n    Maximum impressions in the window.\n    '
    suppress: NotRequired[JsonValue]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[JsonValue]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap24(TypedDict):
    """
    Package impression frequency limit.
    """
    suppress: NotRequired[Suppress]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[float]
    '\n    Suppression duration in minutes.\n    '
    max_impressions: NotRequired[int]
    '\n    Maximum impressions in the window.\n    '
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[Window4]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap25(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window4]

class FrequencyCap26(TypedDict):
    window: NotRequired[Window4]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]

class FrequencyCap27(TypedDict):
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window4]

class FrequencyCap28(TypedDict):
    window: NotRequired[Window4]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
FrequencyCap2: TypeAlias = FrequencyCap25 | FrequencyCap26 | FrequencyCap27 | FrequencyCap28
'\nPackage impression frequency limit.\n'

class GeoProximityItem2(TypedDict):
    """
    Proximity areas to include.
    """
    lat: NotRequired[float]
    '\n    Latitude in decimal degrees.\n    '
    lng: NotRequired[float]
    '\n    Longitude in decimal degrees.\n    '
    label: NotRequired[str]
    '\n    Optional human-readable label.\n    '
    travel_time: NotRequired[TravelTime1]
    '\n    Maximum travel time.\n    '
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    '\n    Travel mode for this area.\n    '
    radius: NotRequired[Radius1]
    '\n    Radius around this area.\n    '
    geometry: NotRequired[Geometry2]
    '\n    Geographic boundary.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class Signals3(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['binary']
    '\n    Targeting detail.\n    '
    value: Literal[True]
    '\n    Numeric value.\n    '

class Signals4(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['categorical']
    '\n    Targeting detail.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class Signals5(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['numeric']
    '\n    Targeting detail.\n    '
    min_value: NotRequired[float]
    '\n    Targeting detail.\n    '
    max_value: NotRequired[float]
    '\n    Targeting detail.\n    '

class Group1(TypedDict):
    """
    Signal groups to combine.
    """
    operator: Literal['any', 'none']
    '\n    How child selections combine.\n    '
    signals: list[Signals3 | Signals4 | Signals5]
    '\n    Signals in this group.\n    '

class SignalTargetingGroups1(TypedDict):
    """
    Signal groups and their selection mode.
    """
    operator: Literal['all']
    '\n    How child selections combine.\n    '
    groups: list[Group1]
    '\n    Signal groups to combine.\n    '

class TargetingOverlay2(TypedDict):
    """
    Deprecated. Numeric codes replace names; AI-10440 removal will have at least 14 days notice.
    """
    geo_metros: NotRequired[list[GeoMetro1]]
    '\n    Nielsen DMA groups to include.\n    '
    geo_metros_exclude: NotRequired[list[GeoMetrosExcludeItem]]
    '\n    Nielsen DMA groups to exclude.\n    '
    geo_postal_areas: NotRequired[list[GeoPostalAreas11 | GeoPostalAreas12 | GeoPostalAreas13 | GeoPostalAreas14 | GeoPostalAreas15 | GeoPostalAreas16 | GeoPostalAreas17 | GeoPostalAreas18 | GeoPostalAreas19 | GeoPostalAreas20 | GeoPostalAreas21]]
    '\n    Postal areas to include.\n    '
    geo_postal_areas_exclude: NotRequired[list[GeoPostalAreasExclude11 | GeoPostalAreasExclude12 | GeoPostalAreasExclude13 | GeoPostalAreasExclude14 | GeoPostalAreasExclude15 | GeoPostalAreasExclude16 | GeoPostalAreasExclude17 | GeoPostalAreasExclude18 | GeoPostalAreasExclude19 | GeoPostalAreasExclude20 | GeoPostalAreasExclude21]]
    '\n    Postal areas to exclude.\n    '
    geo_places: NotRequired[list[GeoPlace4]]
    '\n    Named geographic places to include.\n    '
    geo_places_exclude: NotRequired[list[GeoPlacesExcludeItem4]]
    '\n    Named geographic places to exclude.\n    '
    daypart_targets: NotRequired[list[DaypartTarget1]]
    '\n    Time windows when delivery is allowed.\n    '
    axe_include_segment: NotRequired[str]
    '\n    AXE segment IDs to include.\n    '
    axe_exclude_segment: NotRequired[str]
    '\n    AXE segment IDs to exclude.\n    '
    audience_include: NotRequired[list[str]]
    '\n    Audience segment IDs to include.\n    '
    audience_exclude: NotRequired[list[str]]
    '\n    Audience segment IDs to exclude.\n    '
    demographics: NotRequired[Demographics3]
    '\n    demographics reject before dispatch.\n    '
    frequency_cap: NotRequired[FrequencyCap2]
    '\n    Package impression frequency limit.\n    '
    property_list: NotRequired[PropertyList]
    '\n    Property-list reference to include.\n    '
    property_list_exclude: NotRequired[PropertyListExclude]
    '\n    Property-list reference to exclude.\n    '
    collection_list: NotRequired[CollectionList]
    '\n    Collection-list reference to include.\n    '
    collection_list_exclude: NotRequired[CollectionListExclude]
    '\n    Collection-list reference to exclude.\n    '
    placement_selection: NotRequired[dict[str, JsonValue]]
    '\n    Placement selection reference.\n    '
    collection_selection: NotRequired[dict[str, JsonValue]]
    '\n    Collection selection reference.\n    '
    age_restriction: NotRequired[AgeRestriction1]
    '\n    Minimum audience age and verification.\n    '
    device_platform: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    '\n    Device platforms to include.\n    '
    device_platform_exclude: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    '\n    Device platforms to exclude.\n    '
    device_type: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Device types to include.\n    '
    device_type_exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Device types to exclude.\n    '
    browser: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    '\n    Browsers to include.\n    '
    browser_exclude: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    '\n    Browsers to exclude.\n    '
    store_catchments: NotRequired[list[StoreCatchment]]
    '\n    Store or catchment identifiers.\n    '
    geo_proximity: NotRequired[list[GeoProximityItem2]]
    '\n    Proximity areas to include.\n    '
    language: NotRequired[list[LanguageItem2]]
    '\n    Language codes to include.\n    '
    keyword_targets: NotRequired[list[KeywordTarget]]
    '\n    Keyword targets and bid prices.\n    '
    negative_keywords: NotRequired[list[NegativeKeyword]]
    '\n    Keywords to exclude.\n    '
    signal_targeting_groups: NotRequired[SignalTargetingGroups1]
    '\n    Signal groups and their selection mode.\n    '
    geo_countries: NotRequired[list[str]]
    '\n    Country codes or names.\n    '
    geo_countries_exclude: NotRequired[list[str]]
    '\n    Country codes or names to exclude.\n    '
    geo_regions: NotRequired[list[str]]
    '\n    Subdivision codes or names.\n    '
    geo_regions_exclude: NotRequired[list[str]]
    '\n    Subdivision codes or names to exclude.\n    '

class Vendor3(TypedDict):
    """
    Optional measurement vendor.
    """
    domain: str
    '\n    Vendor brand domain.\n    '
    brand_id: NotRequired[str]
    '\n    Optional vendor brand ID.\n    '

class PerformanceStandard1(TypedDict):
    metric: Literal['viewability', 'ivt', 'completion_rate', 'brand_safety', 'attention_score']
    '\n    Quality metric to commit.\n    '
    threshold: float
    '\n    Value from 0 to 1.\n    '
    standard: NotRequired[Literal['MRC', 'GroupM']]
    '\n    Required for viewability only.\n    '
    vendor: NotRequired[Vendor3]
    '\n    Optional measurement vendor.\n    '

class Product1(TypedDict):
    productId: str
    '\n    Qualified ID returned by discovery. Pass it unchanged.\n    '
    selectionId: NotRequired[str]
    '\n    Create only: give repeats of one productId distinct values to add separate line items.\n    '
    inventorySourceId: NotRequired[str]
    '\n    Returned inventory source ID. Pass unchanged when present to keep modular products unambiguous.\n    '
    salesAgentId: NotRequired[str]
    '\n    Returned sales agent ID. Pass unchanged when present to preserve the selected seller route.\n    '
    pricingOptionId: NotRequired[str]
    '\n    Returned Product pricing option ID. Pass unchanged when present.\n    '
    budget: NotRequired[float]
    '\n    Per-product budget. Required with fixed allocation; refused with seller_optimized.\n    '
    bidPrice: NotRequired[float]
    '\n    Bid in campaign currency. Required for auction products; omit for fixed-price.\n    '
    targetingOverlay: NotRequired[TargetingOverlay2]
    '\n    Deprecated. Numeric codes replace names; AI-10440 removal will have at least 14 days notice.\n    '
    performanceStandards: NotRequired[list[PerformanceStandard1] | None]
    '\n    Package standards. Viewability: MRC/GroupM. IVT ceiling; others floors. Update: null/[] clears.\n    '
    pixelId: NotRequired[str]
    '\n    Meta Pixel/Dataset ID for conversion tracking. Required for Meta Sales; no auto-select.\n    '
    remove: NotRequired[bool]
    '\n    Update only: true removes this line item.\n    '
    lineItemRef: NotRequired[str]
    '\n    Update only: line-item handle from the read; needed for a repeated product.\n    '

class Target7(TypedDict):
    """
    Optional conversion outcome target.
    """
    kind: Literal['per_ad_spend']
    '\n    Optimize value relative to ad spend.\n    '
    value: SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetValue
    '\n    Positive value per ad-spend target.\n    '
    strength: NotRequired[Literal['floor', 'target']]
    '\n    Use a minimum floor or delivery target.\n    '

class Target8(TypedDict):
    """
    Optional conversion outcome target.
    """
    kind: Literal['maximize_value']
    '\n    Maximize attributed event value.\n    '

class Vendor4(TypedDict):
    """
    Vendor that owns the metric definition.
    """
    domain: str
    '\n    Vendor domain that defines the metric.\n    '
    brand_id: NotRequired[str]
    '\n    Optional vendor brand identifier.\n    '

class GeoPostalAreas22(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['US']
    '\n    Country code for this area.\n    '
    system: Literal['zip', 'zip_plus_four']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas23(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['GB']
    '\n    Country code for this area.\n    '
    system: Literal['outward', 'full']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas24(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['CA']
    '\n    Country code for this area.\n    '
    system: Literal['full', 'fsa']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas25(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['DE', 'CH', 'AT']
    '\n    Country code for this area.\n    '
    system: Literal['plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas26(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['FR']
    '\n    Country code for this area.\n    '
    system: Literal['code_postal']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas27(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['AU']
    '\n    Country code for this area.\n    '
    system: Literal['postcode']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas28(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['BR']
    '\n    Country code for this area.\n    '
    system: Literal['cep']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas29(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['IN']
    '\n    Country code for this area.\n    '
    system: Literal['pin']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas30(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['ZA']
    '\n    Country code for this area.\n    '
    system: Literal['postal_code']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas31(TypedDict):
    """
    Postal areas to include.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['postal_code', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas32(TypedDict):
    """
    Postal areas to include.
    """
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude22(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['US']
    '\n    Country code for this area.\n    '
    system: Literal['zip', 'zip_plus_four']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude23(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['GB']
    '\n    Country code for this area.\n    '
    system: Literal['outward', 'full']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude24(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['CA']
    '\n    Country code for this area.\n    '
    system: Literal['full', 'fsa']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude25(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['DE', 'CH', 'AT']
    '\n    Country code for this area.\n    '
    system: Literal['plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude26(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['FR']
    '\n    Country code for this area.\n    '
    system: Literal['code_postal']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude27(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['AU']
    '\n    Country code for this area.\n    '
    system: Literal['postcode']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude28(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['BR']
    '\n    Country code for this area.\n    '
    system: Literal['cep']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude29(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['IN']
    '\n    Country code for this area.\n    '
    system: Literal['pin']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude30(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['ZA']
    '\n    Country code for this area.\n    '
    system: Literal['postal_code']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude31(TypedDict):
    """
    Postal areas to exclude.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['postal_code', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude32(TypedDict):
    """
    Postal areas to exclude.
    """
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPlace51(TypedDict):
    """
    Named geographic places to include.
    """
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Targeting system identifier.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this targeting system.\n    '
    country: NotRequired[JsonValue]
    '\n    Country code for this area.\n    '
    system_version: NotRequired[JsonValue]
    '\n    Targeting-system version.\n    '
    place_type: NotRequired[JsonValue]
    '\n    Geographic place category.\n    '
    value_labels: NotRequired[JsonValue]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[JsonValue]
    '\n    AdCP extension values.\n    '

class GeoPlace52(TypedDict):
    """
    Named geographic places to include.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Targeting system identifier.\n    '
    system_version: NotRequired[str]
    '\n    Targeting-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Geographic place category.\n    '
    values: list[Value3]
    '\n    Values in this targeting system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class GeoPlace53(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlace5: TypeAlias = GeoPlace53
'\nNamed geographic places to include.\n'

class GeoPlacesExcludeItem51(TypedDict):
    """
    Named geographic places to exclude.
    """
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Targeting system identifier.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this targeting system.\n    '
    country: NotRequired[JsonValue]
    '\n    Country code for this area.\n    '
    system_version: NotRequired[JsonValue]
    '\n    Targeting-system version.\n    '
    place_type: NotRequired[JsonValue]
    '\n    Geographic place category.\n    '
    value_labels: NotRequired[JsonValue]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[JsonValue]
    '\n    AdCP extension values.\n    '

class GeoPlacesExcludeItem52(TypedDict):
    """
    Named geographic places to exclude.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Targeting system identifier.\n    '
    system_version: NotRequired[str]
    '\n    Targeting-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Geographic place category.\n    '
    values: list[Value3]
    '\n    Values in this targeting system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class GeoPlacesExcludeItem53(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlacesExcludeItem5: TypeAlias = GeoPlacesExcludeItem53
'\nNamed geographic places to exclude.\n'

class Demographics4(TypedDict):
    """
    demographics reject before dispatch.
    """
    age: Age7
    '\n    Audience age range.\n    '

class FrequencyCap31(TypedDict):
    """
    Package impression frequency limit.
    """
    suppress: JsonValue
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    max_impressions: NotRequired[JsonValue]
    '\n    Maximum impressions in the window.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[JsonValue]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap32(TypedDict):
    """
    Package impression frequency limit.
    """
    window: JsonValue
    '\n    Frequency-cap window size.\n    '
    max_impressions: JsonValue
    '\n    Maximum impressions in the window.\n    '
    suppress: NotRequired[JsonValue]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '

class FrequencyCap33(TypedDict):
    """
    Package impression frequency limit.
    """
    max_impressions: JsonValue
    '\n    Maximum impressions in the window.\n    '
    suppress: NotRequired[JsonValue]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[JsonValue]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap34(TypedDict):
    """
    Package impression frequency limit.
    """
    suppress: NotRequired[Suppress]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[float]
    '\n    Suppression duration in minutes.\n    '
    max_impressions: NotRequired[int]
    '\n    Maximum impressions in the window.\n    '
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[Window4]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap35(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window4]

class FrequencyCap36(TypedDict):
    window: NotRequired[Window4]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]

class FrequencyCap37(TypedDict):
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window4]

class FrequencyCap38(TypedDict):
    window: NotRequired[Window4]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
FrequencyCap3: TypeAlias = FrequencyCap35 | FrequencyCap36 | FrequencyCap37 | FrequencyCap38
'\nPackage impression frequency limit.\n'

class GeoProximityItem3(TypedDict):
    """
    Proximity areas to include.
    """
    lat: NotRequired[float]
    '\n    Latitude in decimal degrees.\n    '
    lng: NotRequired[float]
    '\n    Longitude in decimal degrees.\n    '
    label: NotRequired[str]
    '\n    Optional human-readable label.\n    '
    travel_time: NotRequired[TravelTime1]
    '\n    Maximum travel time.\n    '
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    '\n    Travel mode for this area.\n    '
    radius: NotRequired[Radius1]
    '\n    Radius around this area.\n    '
    geometry: NotRequired[Geometry2]
    '\n    Geographic boundary.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class Signals6(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['binary']
    '\n    Targeting detail.\n    '
    value: Literal[True]
    '\n    Numeric value.\n    '

class Signals7(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['categorical']
    '\n    Targeting detail.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class Signals8(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['numeric']
    '\n    Targeting detail.\n    '
    min_value: NotRequired[float]
    '\n    Targeting detail.\n    '
    max_value: NotRequired[float]
    '\n    Targeting detail.\n    '

class Group2(TypedDict):
    """
    Signal groups to combine.
    """
    operator: Literal['any', 'none']
    '\n    How child selections combine.\n    '
    signals: list[Signals6 | Signals7 | Signals8]
    '\n    Signals in this group.\n    '

class SignalTargetingGroups2(TypedDict):
    """
    Signal groups and their selection mode.
    """
    operator: Literal['all']
    '\n    How child selections combine.\n    '
    groups: list[Group2]
    '\n    Signal groups to combine.\n    '

class TargetingOverlay3(TypedDict):
    """
    Deprecated. Numeric codes replace names; AI-10440 removal will have at least 14 days notice.
    """
    geo_metros: NotRequired[list[GeoMetro1]]
    '\n    Nielsen DMA groups to include.\n    '
    geo_metros_exclude: NotRequired[list[GeoMetrosExcludeItem]]
    '\n    Nielsen DMA groups to exclude.\n    '
    geo_postal_areas: NotRequired[list[GeoPostalAreas22 | GeoPostalAreas23 | GeoPostalAreas24 | GeoPostalAreas25 | GeoPostalAreas26 | GeoPostalAreas27 | GeoPostalAreas28 | GeoPostalAreas29 | GeoPostalAreas30 | GeoPostalAreas31 | GeoPostalAreas32]]
    '\n    Postal areas to include.\n    '
    geo_postal_areas_exclude: NotRequired[list[GeoPostalAreasExclude22 | GeoPostalAreasExclude23 | GeoPostalAreasExclude24 | GeoPostalAreasExclude25 | GeoPostalAreasExclude26 | GeoPostalAreasExclude27 | GeoPostalAreasExclude28 | GeoPostalAreasExclude29 | GeoPostalAreasExclude30 | GeoPostalAreasExclude31 | GeoPostalAreasExclude32]]
    '\n    Postal areas to exclude.\n    '
    geo_places: NotRequired[list[GeoPlace5]]
    '\n    Named geographic places to include.\n    '
    geo_places_exclude: NotRequired[list[GeoPlacesExcludeItem5]]
    '\n    Named geographic places to exclude.\n    '
    daypart_targets: NotRequired[list[DaypartTarget1]]
    '\n    Time windows when delivery is allowed.\n    '
    axe_include_segment: NotRequired[str]
    '\n    AXE segment IDs to include.\n    '
    axe_exclude_segment: NotRequired[str]
    '\n    AXE segment IDs to exclude.\n    '
    audience_include: NotRequired[list[str]]
    '\n    Audience segment IDs to include.\n    '
    audience_exclude: NotRequired[list[str]]
    '\n    Audience segment IDs to exclude.\n    '
    demographics: NotRequired[Demographics4]
    '\n    demographics reject before dispatch.\n    '
    frequency_cap: NotRequired[FrequencyCap3]
    '\n    Package impression frequency limit.\n    '
    property_list: NotRequired[PropertyList]
    '\n    Property-list reference to include.\n    '
    property_list_exclude: NotRequired[PropertyListExclude]
    '\n    Property-list reference to exclude.\n    '
    collection_list: NotRequired[CollectionList]
    '\n    Collection-list reference to include.\n    '
    collection_list_exclude: NotRequired[CollectionListExclude]
    '\n    Collection-list reference to exclude.\n    '
    placement_selection: NotRequired[dict[str, JsonValue]]
    '\n    Placement selection reference.\n    '
    collection_selection: NotRequired[dict[str, JsonValue]]
    '\n    Collection selection reference.\n    '
    age_restriction: NotRequired[AgeRestriction1]
    '\n    Minimum audience age and verification.\n    '
    device_platform: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    '\n    Device platforms to include.\n    '
    device_platform_exclude: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    '\n    Device platforms to exclude.\n    '
    device_type: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Device types to include.\n    '
    device_type_exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Device types to exclude.\n    '
    browser: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    '\n    Browsers to include.\n    '
    browser_exclude: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    '\n    Browsers to exclude.\n    '
    store_catchments: NotRequired[list[StoreCatchment]]
    '\n    Store or catchment identifiers.\n    '
    geo_proximity: NotRequired[list[GeoProximityItem3]]
    '\n    Proximity areas to include.\n    '
    language: NotRequired[list[LanguageItem2]]
    '\n    Language codes to include.\n    '
    keyword_targets: NotRequired[list[KeywordTarget]]
    '\n    Keyword targets and bid prices.\n    '
    negative_keywords: NotRequired[list[NegativeKeyword]]
    '\n    Keywords to exclude.\n    '
    signal_targeting_groups: NotRequired[SignalTargetingGroups2]
    '\n    Signal groups and their selection mode.\n    '
    geo_countries: NotRequired[list[str]]
    '\n    Country codes or names.\n    '
    geo_countries_exclude: NotRequired[list[str]]
    '\n    Country codes or names to exclude.\n    '
    geo_regions: NotRequired[list[str]]
    '\n    Subdivision codes or names.\n    '
    geo_regions_exclude: NotRequired[list[str]]
    '\n    Subdivision codes or names to exclude.\n    '

class Vendor5(TypedDict):
    """
    Optional measurement vendor.
    """
    domain: str
    '\n    Vendor brand domain.\n    '
    brand_id: NotRequired[str]
    '\n    Optional vendor brand ID.\n    '

class PerformanceStandard2(TypedDict):
    metric: Literal['viewability', 'ivt', 'completion_rate', 'brand_safety', 'attention_score']
    '\n    Quality metric to commit.\n    '
    threshold: float
    '\n    Value from 0 to 1.\n    '
    standard: NotRequired[Literal['MRC', 'GroupM']]
    '\n    Required for viewability only.\n    '
    vendor: NotRequired[Vendor5]
    '\n    Optional measurement vendor.\n    '

class Product2(TypedDict):
    productId: str
    '\n    Qualified ID returned by discovery. Pass it unchanged.\n    '
    selectionId: NotRequired[str]
    '\n    Create only: give repeats of one productId distinct values to add separate line items.\n    '
    inventorySourceId: NotRequired[str]
    '\n    Returned inventory source ID. Pass unchanged when present to keep modular products unambiguous.\n    '
    salesAgentId: NotRequired[str]
    '\n    Returned sales agent ID. Pass unchanged when present to preserve the selected seller route.\n    '
    pricingOptionId: NotRequired[str]
    '\n    Returned Product pricing option ID. Pass unchanged when present.\n    '
    budget: NotRequired[float]
    '\n    Per-product budget. Required with fixed allocation; refused with seller_optimized.\n    '
    bidPrice: NotRequired[float]
    '\n    Bid in campaign currency. Required for auction products; omit for fixed-price.\n    '
    targetingOverlay: NotRequired[TargetingOverlay3]
    '\n    Deprecated. Numeric codes replace names; AI-10440 removal will have at least 14 days notice.\n    '
    performanceStandards: NotRequired[list[PerformanceStandard2] | None]
    '\n    Package standards. Viewability: MRC/GroupM. IVT ceiling; others floors. Update: null/[] clears.\n    '
    pixelId: NotRequired[str]
    '\n    Meta Pixel/Dataset ID for conversion tracking. Required for Meta Sales; no auto-select.\n    '
    remove: NotRequired[bool]
    '\n    Update only: true removes this line item.\n    '
    lineItemRef: NotRequired[str]
    '\n    Update only: line-item handle from the read; needed for a repeated product.\n    '

class Target9(TypedDict):
    """
    Optional conversion outcome target.
    """
    kind: Literal['per_ad_spend']
    '\n    Optimize value relative to ad spend.\n    '
    value: SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetValue
    '\n    Positive value per ad-spend target.\n    '
    strength: NotRequired[Literal['floor', 'target']]
    '\n    Use a minimum floor or delivery target.\n    '

class Target10(TypedDict):
    """
    Optional conversion outcome target.
    """
    kind: Literal['maximize_value']
    '\n    Maximize attributed event value.\n    '

class Vendor6(TypedDict):
    """
    Vendor that owns the metric definition.
    """
    domain: str
    '\n    Vendor domain that defines the metric.\n    '
    brand_id: NotRequired[str]
    '\n    Optional vendor brand identifier.\n    '

class GeoPostalAreas33(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['US']
    '\n    Country code for this area.\n    '
    system: Literal['zip', 'zip_plus_four']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas34(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['GB']
    '\n    Country code for this area.\n    '
    system: Literal['outward', 'full']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas35(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['CA']
    '\n    Country code for this area.\n    '
    system: Literal['full', 'fsa']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas36(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['DE', 'CH', 'AT']
    '\n    Country code for this area.\n    '
    system: Literal['plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas37(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['FR']
    '\n    Country code for this area.\n    '
    system: Literal['code_postal']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas38(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['AU']
    '\n    Country code for this area.\n    '
    system: Literal['postcode']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas39(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['BR']
    '\n    Country code for this area.\n    '
    system: Literal['cep']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas40(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['IN']
    '\n    Country code for this area.\n    '
    system: Literal['pin']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas41(TypedDict):
    """
    Postal areas to include.
    """
    country: Literal['ZA']
    '\n    Country code for this area.\n    '
    system: Literal['postal_code']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas42(TypedDict):
    """
    Postal areas to include.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['postal_code', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreas43(TypedDict):
    """
    Postal areas to include.
    """
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude33(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['US']
    '\n    Country code for this area.\n    '
    system: Literal['zip', 'zip_plus_four']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude34(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['GB']
    '\n    Country code for this area.\n    '
    system: Literal['outward', 'full']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude35(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['CA']
    '\n    Country code for this area.\n    '
    system: Literal['full', 'fsa']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude36(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['DE', 'CH', 'AT']
    '\n    Country code for this area.\n    '
    system: Literal['plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude37(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['FR']
    '\n    Country code for this area.\n    '
    system: Literal['code_postal']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude38(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['AU']
    '\n    Country code for this area.\n    '
    system: Literal['postcode']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude39(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['BR']
    '\n    Country code for this area.\n    '
    system: Literal['cep']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude40(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['IN']
    '\n    Country code for this area.\n    '
    system: Literal['pin']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude41(TypedDict):
    """
    Postal areas to exclude.
    """
    country: Literal['ZA']
    '\n    Country code for this area.\n    '
    system: Literal['postal_code']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude42(TypedDict):
    """
    Postal areas to exclude.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['postal_code', 'custom']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPostalAreasExclude43(TypedDict):
    """
    Postal areas to exclude.
    """
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    '\n    Targeting system identifier.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class GeoPlace61(TypedDict):
    """
    Named geographic places to include.
    """
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Targeting system identifier.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this targeting system.\n    '
    country: NotRequired[JsonValue]
    '\n    Country code for this area.\n    '
    system_version: NotRequired[JsonValue]
    '\n    Targeting-system version.\n    '
    place_type: NotRequired[JsonValue]
    '\n    Geographic place category.\n    '
    value_labels: NotRequired[JsonValue]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[JsonValue]
    '\n    AdCP extension values.\n    '

class GeoPlace62(TypedDict):
    """
    Named geographic places to include.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Targeting system identifier.\n    '
    system_version: NotRequired[str]
    '\n    Targeting-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Geographic place category.\n    '
    values: list[Value3]
    '\n    Values in this targeting system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class GeoPlace63(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlace6: TypeAlias = GeoPlace63
'\nNamed geographic places to include.\n'

class GeoPlacesExcludeItem61(TypedDict):
    """
    Named geographic places to exclude.
    """
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    '\n    Targeting system identifier.\n    '
    values: NotRequired[JsonValue]
    '\n    Values in this targeting system.\n    '
    country: NotRequired[JsonValue]
    '\n    Country code for this area.\n    '
    system_version: NotRequired[JsonValue]
    '\n    Targeting-system version.\n    '
    place_type: NotRequired[JsonValue]
    '\n    Geographic place category.\n    '
    value_labels: NotRequired[JsonValue]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[JsonValue]
    '\n    AdCP extension values.\n    '

class GeoPlacesExcludeItem62(TypedDict):
    """
    Named geographic places to exclude.
    """
    country: str
    '\n    Country code for this area.\n    '
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    '\n    Targeting system identifier.\n    '
    system_version: NotRequired[str]
    '\n    Targeting-system version.\n    '
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    '\n    Geographic place category.\n    '
    values: list[Value3]
    '\n    Values in this targeting system.\n    '
    value_labels: NotRequired[dict[str, str]]
    '\n    Labels keyed by targeting value ID.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class GeoPlacesExcludeItem63(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlacesExcludeItem6: TypeAlias = GeoPlacesExcludeItem63
'\nNamed geographic places to exclude.\n'

class Demographics5(TypedDict):
    """
    demographics reject before dispatch.
    """
    age: Age7
    '\n    Audience age range.\n    '

class FrequencyCap41(TypedDict):
    """
    Package impression frequency limit.
    """
    suppress: JsonValue
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    max_impressions: NotRequired[JsonValue]
    '\n    Maximum impressions in the window.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[JsonValue]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap42(TypedDict):
    """
    Package impression frequency limit.
    """
    window: JsonValue
    '\n    Frequency-cap window size.\n    '
    max_impressions: JsonValue
    '\n    Maximum impressions in the window.\n    '
    suppress: NotRequired[JsonValue]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '

class FrequencyCap43(TypedDict):
    """
    Package impression frequency limit.
    """
    max_impressions: JsonValue
    '\n    Maximum impressions in the window.\n    '
    suppress: NotRequired[JsonValue]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[JsonValue]
    '\n    Suppression duration in minutes.\n    '
    per: NotRequired[JsonValue]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[JsonValue]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap44(TypedDict):
    """
    Package impression frequency limit.
    """
    suppress: NotRequired[Suppress]
    '\n    Whether to suppress delivery after the cap.\n    '
    suppress_minutes: NotRequired[float]
    '\n    Suppression duration in minutes.\n    '
    max_impressions: NotRequired[int]
    '\n    Maximum impressions in the window.\n    '
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    '\n    Frequency-cap time unit.\n    '
    window: NotRequired[Window4]
    '\n    Frequency-cap window size.\n    '

class FrequencyCap45(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window4]

class FrequencyCap46(TypedDict):
    window: NotRequired[Window4]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]

class FrequencyCap47(TypedDict):
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window4]

class FrequencyCap48(TypedDict):
    window: NotRequired[Window4]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
FrequencyCap4: TypeAlias = FrequencyCap45 | FrequencyCap46 | FrequencyCap47 | FrequencyCap48
'\nPackage impression frequency limit.\n'

class GeoProximityItem4(TypedDict):
    """
    Proximity areas to include.
    """
    lat: NotRequired[float]
    '\n    Latitude in decimal degrees.\n    '
    lng: NotRequired[float]
    '\n    Longitude in decimal degrees.\n    '
    label: NotRequired[str]
    '\n    Optional human-readable label.\n    '
    travel_time: NotRequired[TravelTime1]
    '\n    Maximum travel time.\n    '
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    '\n    Travel mode for this area.\n    '
    radius: NotRequired[Radius1]
    '\n    Radius around this area.\n    '
    geometry: NotRequired[Geometry2]
    '\n    Geographic boundary.\n    '
    ext: NotRequired[dict[str, JsonValue]]
    '\n    AdCP extension values.\n    '

class Signals9(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['binary']
    '\n    Targeting detail.\n    '
    value: Literal[True]
    '\n    Numeric value.\n    '

class Signals10(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['categorical']
    '\n    Targeting detail.\n    '
    values: list[str]
    '\n    Values in this targeting system.\n    '

class Signals11(TypedDict):
    """
    Signals in this group.
    """
    signal_ref: SaveMediaBuyRequestProductsItemTargetingOverlaySignalTargetingGroupsGroupsItemSignalsItemSignalRef
    '\n    Targeting detail.\n    '
    pricing_option_id: NotRequired[str]
    '\n    Seller pricing-option reference.\n    '
    signal_agent_segment_id: NotRequired[str]
    '\n    Signal-agent segment reference.\n    '
    activation_key: NotRequired[JsonValue]
    '\n    Seller activation reference.\n    '
    value_type: Literal['numeric']
    '\n    Targeting detail.\n    '
    min_value: NotRequired[float]
    '\n    Targeting detail.\n    '
    max_value: NotRequired[float]
    '\n    Targeting detail.\n    '

class Group3(TypedDict):
    """
    Signal groups to combine.
    """
    operator: Literal['any', 'none']
    '\n    How child selections combine.\n    '
    signals: list[Signals9 | Signals10 | Signals11]
    '\n    Signals in this group.\n    '

class SignalTargetingGroups3(TypedDict):
    """
    Signal groups and their selection mode.
    """
    operator: Literal['all']
    '\n    How child selections combine.\n    '
    groups: list[Group3]
    '\n    Signal groups to combine.\n    '

class TargetingOverlay4(TypedDict):
    """
    Deprecated. Numeric codes replace names; AI-10440 removal will have at least 14 days notice.
    """
    geo_metros: NotRequired[list[GeoMetro1]]
    '\n    Nielsen DMA groups to include.\n    '
    geo_metros_exclude: NotRequired[list[GeoMetrosExcludeItem]]
    '\n    Nielsen DMA groups to exclude.\n    '
    geo_postal_areas: NotRequired[list[GeoPostalAreas33 | GeoPostalAreas34 | GeoPostalAreas35 | GeoPostalAreas36 | GeoPostalAreas37 | GeoPostalAreas38 | GeoPostalAreas39 | GeoPostalAreas40 | GeoPostalAreas41 | GeoPostalAreas42 | GeoPostalAreas43]]
    '\n    Postal areas to include.\n    '
    geo_postal_areas_exclude: NotRequired[list[GeoPostalAreasExclude33 | GeoPostalAreasExclude34 | GeoPostalAreasExclude35 | GeoPostalAreasExclude36 | GeoPostalAreasExclude37 | GeoPostalAreasExclude38 | GeoPostalAreasExclude39 | GeoPostalAreasExclude40 | GeoPostalAreasExclude41 | GeoPostalAreasExclude42 | GeoPostalAreasExclude43]]
    '\n    Postal areas to exclude.\n    '
    geo_places: NotRequired[list[GeoPlace6]]
    '\n    Named geographic places to include.\n    '
    geo_places_exclude: NotRequired[list[GeoPlacesExcludeItem6]]
    '\n    Named geographic places to exclude.\n    '
    daypart_targets: NotRequired[list[DaypartTarget1]]
    '\n    Time windows when delivery is allowed.\n    '
    axe_include_segment: NotRequired[str]
    '\n    AXE segment IDs to include.\n    '
    axe_exclude_segment: NotRequired[str]
    '\n    AXE segment IDs to exclude.\n    '
    audience_include: NotRequired[list[str]]
    '\n    Audience segment IDs to include.\n    '
    audience_exclude: NotRequired[list[str]]
    '\n    Audience segment IDs to exclude.\n    '
    demographics: NotRequired[Demographics5]
    '\n    demographics reject before dispatch.\n    '
    frequency_cap: NotRequired[FrequencyCap4]
    '\n    Package impression frequency limit.\n    '
    property_list: NotRequired[PropertyList]
    '\n    Property-list reference to include.\n    '
    property_list_exclude: NotRequired[PropertyListExclude]
    '\n    Property-list reference to exclude.\n    '
    collection_list: NotRequired[CollectionList]
    '\n    Collection-list reference to include.\n    '
    collection_list_exclude: NotRequired[CollectionListExclude]
    '\n    Collection-list reference to exclude.\n    '
    placement_selection: NotRequired[dict[str, JsonValue]]
    '\n    Placement selection reference.\n    '
    collection_selection: NotRequired[dict[str, JsonValue]]
    '\n    Collection selection reference.\n    '
    age_restriction: NotRequired[AgeRestriction1]
    '\n    Minimum audience age and verification.\n    '
    device_platform: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    '\n    Device platforms to include.\n    '
    device_platform_exclude: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    '\n    Device platforms to exclude.\n    '
    device_type: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Device types to include.\n    '
    device_type_exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    '\n    Device types to exclude.\n    '
    browser: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    '\n    Browsers to include.\n    '
    browser_exclude: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    '\n    Browsers to exclude.\n    '
    store_catchments: NotRequired[list[StoreCatchment]]
    '\n    Store or catchment identifiers.\n    '
    geo_proximity: NotRequired[list[GeoProximityItem4]]
    '\n    Proximity areas to include.\n    '
    language: NotRequired[list[LanguageItem2]]
    '\n    Language codes to include.\n    '
    keyword_targets: NotRequired[list[KeywordTarget]]
    '\n    Keyword targets and bid prices.\n    '
    negative_keywords: NotRequired[list[NegativeKeyword]]
    '\n    Keywords to exclude.\n    '
    signal_targeting_groups: NotRequired[SignalTargetingGroups3]
    '\n    Signal groups and their selection mode.\n    '
    geo_countries: NotRequired[list[str]]
    '\n    Country codes or names.\n    '
    geo_countries_exclude: NotRequired[list[str]]
    '\n    Country codes or names to exclude.\n    '
    geo_regions: NotRequired[list[str]]
    '\n    Subdivision codes or names.\n    '
    geo_regions_exclude: NotRequired[list[str]]
    '\n    Subdivision codes or names to exclude.\n    '

class Vendor7(TypedDict):
    """
    Optional measurement vendor.
    """
    domain: str
    '\n    Vendor brand domain.\n    '
    brand_id: NotRequired[str]
    '\n    Optional vendor brand ID.\n    '

class PerformanceStandard3(TypedDict):
    metric: Literal['viewability', 'ivt', 'completion_rate', 'brand_safety', 'attention_score']
    '\n    Quality metric to commit.\n    '
    threshold: float
    '\n    Value from 0 to 1.\n    '
    standard: NotRequired[Literal['MRC', 'GroupM']]
    '\n    Required for viewability only.\n    '
    vendor: NotRequired[Vendor7]
    '\n    Optional measurement vendor.\n    '

class Product3(TypedDict):
    productId: str
    '\n    Qualified ID returned by discovery. Pass it unchanged.\n    '
    selectionId: NotRequired[str]
    '\n    Create only: give repeats of one productId distinct values to add separate line items.\n    '
    inventorySourceId: NotRequired[str]
    '\n    Returned inventory source ID. Pass unchanged when present to keep modular products unambiguous.\n    '
    salesAgentId: NotRequired[str]
    '\n    Returned sales agent ID. Pass unchanged when present to preserve the selected seller route.\n    '
    pricingOptionId: NotRequired[str]
    '\n    Returned Product pricing option ID. Pass unchanged when present.\n    '
    budget: NotRequired[float]
    '\n    Per-product budget. Required with fixed allocation; refused with seller_optimized.\n    '
    bidPrice: NotRequired[float]
    '\n    Bid in campaign currency. Required for auction products; omit for fixed-price.\n    '
    targetingOverlay: NotRequired[TargetingOverlay4]
    '\n    Deprecated. Numeric codes replace names; AI-10440 removal will have at least 14 days notice.\n    '
    performanceStandards: NotRequired[list[PerformanceStandard3] | None]
    '\n    Package standards. Viewability: MRC/GroupM. IVT ceiling; others floors. Update: null/[] clears.\n    '
    pixelId: NotRequired[str]
    '\n    Meta Pixel/Dataset ID for conversion tracking. Required for Meta Sales; no auto-select.\n    '
    remove: NotRequired[bool]
    '\n    Update only: true removes this line item.\n    '
    lineItemRef: NotRequired[str]
    '\n    Update only: line-item handle from the read; needed for a repeated product.\n    '

class Target11(TypedDict):
    """
    Optional conversion outcome target.
    """
    kind: Literal['per_ad_spend']
    '\n    Optimize value relative to ad spend.\n    '
    value: SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetValue
    '\n    Positive value per ad-spend target.\n    '
    strength: NotRequired[Literal['floor', 'target']]
    '\n    Use a minimum floor or delivery target.\n    '

class Target12(TypedDict):
    """
    Optional conversion outcome target.
    """
    kind: Literal['maximize_value']
    '\n    Maximize attributed event value.\n    '

class Vendor8(TypedDict):
    """
    Vendor that owns the metric definition.
    """
    domain: str
    '\n    Vendor domain that defines the metric.\n    '
    brand_id: NotRequired[str]
    '\n    Optional vendor brand identifier.\n    '

class ChannelGroup(TypedDict):
    channelGroupId: str
    name: str

class PendingChange(TypedDict):
    status: str
    pendingAt: NotRequired[SaveMediaBuySuccessMediaBuyRefsItemPendingChangePendingAt]

class Ending(TypedDict):
    reason: Literal['canceled']
    since: str

class MediaBuyRef(TypedDict):
    mediaBuyId: str
    channelGroup: NotRequired[ChannelGroup]
    pendingAt: NotRequired[SaveMediaBuySuccessMediaBuyRefsItemPendingAt]
    pendingChange: NotRequired[PendingChange]
    phase: SaveMediaBuySuccessMediaBuyRefsItemPhase
    isPaused: NotRequired[bool]
    ending: NotRequired[Ending]

class ProposalSource(TypedDict):
    proposalId: str
    proposalVersionId: str

class FrequencyCap5(TypedDict):
    level: Literal['mediaBuy']
    '\n    Counter scope.\n    '
    requested: SaveMediaBuySuccessMediaBuyFrequencyCapRequested
    effective: NotRequired[SaveMediaBuySuccessMediaBuyFrequencyCapEffective]
    '\n    Exact cap echoed by the seller after acceptance.\n    '
    status: Literal['requested', 'confirmed']
    '\n    Requested until the seller returns the exact cap; confirmed afterwards.\n    '

class Flight5(TypedDict):
    startAt: str
    endAt: str

class Error12(TypedDict):
    mediaBuyId: str
    salesAgentId: str
    message: str
    debug: NotRequired[JsonValue]
SaveMediaBuyError: TypeAlias = V3ToolErrorResponse
SellerId: TypeAlias = str

class Evaluation(TypedDict):
    """
    Evaluation instructions, inline or by saved policyId. Not yet applied to results.
    """
    instructions: NotRequired[str]
    '\n    Buyer evaluation instructions for the returned proposals. Provide this or policyId, not both.\n    '
    maxRefinementRounds: NotRequired[int]
    '\n    Cap on refinement rounds. Accepted for forward compatibility; not yet applied.\n    '
    ranking: NotRequired[dict[str, JsonValue]]
    '\n    Structured ranking configuration. Accepted for forward compatibility; not yet applied.\n    '
    policyId: NotRequired[str]
    '\n    Saved evaluation policy id. Provide this or instructions, not both. Not yet applied.\n    '

class RequestProposalsInput(TypedDict):
    campaignId: str
    '\n    Campaign to request proposals for.\n    '
    expectedCampaignRevision: int
    '\n    revision from the last get. Rejected with REVISION_CONFLICT if the campaign has changed since.\n    '
    sellerIds: NotRequired[list[SellerId]]
    '\n    Deprecated. Omit: fresh rounds contact all eligible sellers. Legacy values cannot narrow that set.\n    '
    expectedSellerId: NotRequired[str]
    '\n    Optional fail-closed seller check; never grants access. Requires matching current server authority.\n    '
    evaluation: NotRequired[Evaluation]
    '\n    Evaluation instructions, inline or by saved policyId. Not yet applied to results.\n    '
    idempotencyKey: str
    '\n    Stable key per round. Same key returns the same execution; a new key requests a fresh round.\n    '
    capabilityCursor: NotRequired[str]
    '\n    Opaque cursor for full capability details from a terminal response. Omit on normal result pages.\n    '
    resultCursor: NotRequired[str]
    '\n    Opaque cursor from a terminal response. Omit on the first result page.\n    '
    resultLimit: NotRequired[int]
    '\n    Maximum seller outcomes returned on this page (1-50).\n    '

class OverlaySupportCursor(TypedDict):
    pagePath: list[str]
    cursor: str
    itemsTotal: NotRequired[float]

class DemographicTargetingCursor(TypedDict):
    pagePath: list[str]
    cursor: str
    itemsTotal: NotRequired[float]

class ResolvedAgeTargeting(TypedDict):
    min: float
    max: float | None
    includeUnknown: bool

class Product4(TypedDict):
    productId: str
    name: str
    description: NotRequired[str]
    storefrontId: str
    salesAgentId: str
    inventorySourceId: NotRequired[str]
    deliveryType: NotRequired[Literal['guaranteed', 'non_guaranteed']]
    inventoryType: NotRequired[Literal['premium', 'run_of_site', 'targeted_package']]
    pricingOptions: NotRequired[list[JsonValue]]
    formatKinds: NotRequired[list[str]]
    validUntil: NotRequired[str]
    detailsTruncated: NotRequired[bool]
    overlaySupportUnavailable: NotRequired[bool]
    overlaySupportUnavailableReason: NotRequired[str]
    overlaySupportCursorDescriptorsOmitted: NotRequired[float]
    overlaySupportCursor: NotRequired[str]
    capabilityDescriptorCursor: NotRequired[str]
    capabilityDescriptorCount: NotRequired[float]
    overlaySupportCursors: NotRequired[list[OverlaySupportCursor]]
    demographicTargetingUnavailable: NotRequired[bool]
    demographicTargetingUnavailableReason: NotRequired[str]
    demographicTargetingCursorDescriptorsOmitted: NotRequired[float]
    demographicTargetingCursor: NotRequired[str]
    demographicTargetingCursors: NotRequired[list[DemographicTargetingCursor]]
    demographicTargetingExecutable: NotRequired[Literal[False]]
    demographicTargetingExecutionBlocker: NotRequired[str]
    overlaySupport: NotRequired[JsonValue]
    demographicTargeting: NotRequired[JsonValue]
    resolvedAgeTargeting: NotRequired[ResolvedAgeTargeting]

class ProductError(TypedDict):
    code: str
    message: str
    sellerExplanation: NotRequired[str]

class Error13(TypedDict):
    code: str
    message: str
    sellerExplanation: NotRequired[str]

class Outcome1(TypedDict):
    kind: Literal['returned_products']
    productCount: int

class Outcome2(TypedDict):
    kind: Literal['no_matching_products']

class Outcome3(TypedDict):
    kind: Literal['no_inventory_for_request']

class Outcome4(TypedDict):
    kind: Literal['skipped']
    reasonCode: Literal['coverage', 'auth', 'eligibility']

class Outcome5(TypedDict):
    kind: Literal['failed']
    reasonCode: Literal['timeout', 'transport', 'protocol']

class PropertyCoverageItem(TypedDict):
    domain: str
    productCount: int

class InclusionPropertyList(TypedDict):
    filterSupported: bool
    receiptMatchedCount: NotRequired[int]
    receiptUnmatchedCount: NotRequired[int]
    sellerReportedNoMatch: NotRequired[bool]
    incomplete: NotRequired[bool]

class PerSellerItem(TypedDict):
    sellerId: str
    status: Literal['quoted', 'products', 'failed']
    proposalIds: NotRequired[list[str]]
    productQueryId: NotRequired[str]
    products: NotRequired[list[Product4]]
    productError: NotRequired[ProductError]
    error: NotRequired[Error13]
    proposalIdsTruncated: NotRequired[bool]
    outcome: NotRequired[Outcome1 | Outcome2 | Outcome3 | Outcome4 | Outcome5]
    propertyCoverage: NotRequired[list[PropertyCoverageItem]]
    propertyCoverageTotal: NotRequired[int]
    propertyCoverageTruncated: NotRequired[bool]
    filterResult: NotRequired[Literal['no_matching_products', 'filtered_out', 'partial']]
    channelExcludedProductCount: NotRequired[int]
    inclusionPropertyList: NotRequired[InclusionPropertyList]

class Summary1(TypedDict):
    sellersRequested: float
    sellersQuoted: float
    sellersWithProducts: float
    sellersResponded: float
    sellersFailed: float
    sellersPending: float

class MissingProperty(TypedDict):
    domain: str
    sellerId: str
    reason: Literal['not_in_seller_scope', 'seller_reported_no_match', 'seller_unsupported_filter']

class IncompleteProperty(TypedDict):
    domain: str
    sellerId: str

class InclusionPropertyList1(TypedDict):
    requestedDomains: int
    coveredDomains: NotRequired[int]
    missingProperties: list[MissingProperty]
    missingPropertiesTotal: NotRequired[int]
    missingPropertiesTruncated: NotRequired[bool]
    incompleteProperties: NotRequired[list[IncompleteProperty]]
    incompletePropertiesTotal: NotRequired[int]
    incompletePropertiesTruncated: NotRequired[bool]
    incomplete: bool
    capabilityGap: bool

class Page3(TypedDict):
    returned: float
    total: float
    hasMore: bool
    nextCursor: NotRequired[str]

class CapabilityPage(TypedDict):
    field: Literal['demographicTargeting', 'overlaySupport']
    sellerId: str
    productId: str
    pagePath: NotRequired[list[str]]
    offset: NotRequired[float]
    overlaySupport: NotRequired[JsonValue]
    demographicTargeting: NotRequired[JsonValue]
    itemsReturned: NotRequired[float]
    itemsTotal: NotRequired[float]
    intervalsReturned: NotRequired[float]
    intervalsTotal: NotRequired[float]
    complete: bool
    nextCapabilityCursor: NotRequired[str]
    actionableForSave: Literal[False]
    blocker: Literal['APPLICATION_TRANSPORT_ADCP31']
    unavailableReason: NotRequired[str]

class Descriptor(TypedDict):
    field: Literal['demographicTargeting', 'overlaySupport']
    pagePath: NotRequired[list[str]]
    cursor: NotRequired[str]
    itemsTotal: NotRequired[float]
    unavailableReason: NotRequired[Literal['DESCRIPTOR_TOO_LARGE']]
    descriptorOffset: NotRequired[float]
    pagePathDigest: NotRequired[str]

class CapabilityDescriptorPage(TypedDict):
    sellerId: str
    productId: str
    offset: float
    descriptors: list[Descriptor]
    descriptorsReturned: float
    descriptorsTotal: float
    descriptorsOmitted: NotRequired[float]
    unavailableReason: NotRequired[Literal['DESCRIPTOR_TOO_LARGE']]
    blockedDescriptorOffset: NotRequired[float]
    complete: bool
    nextCapabilityCursor: NotRequired[str]

class CohortError(TypedDict):
    code: str
    message: str

class Seller(TypedDict):
    sellerId: str
    sellerName: NotRequired[str]
    reason: Literal['channel_mismatch']
    sellerChannels: list[str]

class SkippedSellers(TypedDict):
    requestedChannels: list[str]
    sellers: list[Seller]
    total: int
    truncated: bool

class RequestProposalsResult(TypedDict):
    executionId: str
    status: Literal['running', 'complete', 'partial', 'failed']
    perSeller: list[PerSellerItem]
    summary: Summary1
    inclusionPropertyList: NotRequired[InclusionPropertyList1]
    page: Page3
    capabilityPage: NotRequired[CapabilityPage]
    capabilityDescriptorPage: NotRequired[CapabilityDescriptorPage]
    cohortError: NotRequired[CohortError | None]
    skippedSellers: NotRequired[SkippedSellers]
RequestProposalsError: TypeAlias = V3ToolErrorResponse

class OpenCampaignReceiptSuccessReceiptMediaBuysItemBudget(TypedDict):
    total: OpenCampaignReceiptSuccessReceiptMediaBuysItemBudgetTotal
    currency: OpenCampaignReceiptSuccessReceiptMediaBuysItemBudgetCurrency

class OpenCampaignReceiptSuccessReceiptStagedBudgetsItem(TypedDict):
    total: OpenCampaignReceiptSuccessReceiptStagedBudgetsItemTotal
    currency: OpenCampaignReceiptSuccessReceiptStagedBudgetsItemCurrency

class GetDeliverySuccessDeliverySummaryPagination(TypedDict):
    has_more: bool
    cursor: NotRequired[GetDeliverySuccessDeliverySummaryPaginationCursor]
    total_count: NotRequired[int]
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsMetrics: TypeAlias = dict[Literal['impressions', 'spend', 'clicks', 'ctr', 'views', 'completed_views', 'completion_rate', 'conversions', 'conversion_value', 'commissionable_value', 'roas', 'cost_per_acquisition', 'new_to_brand_rate', 'reach', 'frequency', 'grps', 'leads', 'incremental_sales_lift', 'brand_lift', 'foot_traffic', 'conversion_lift', 'brand_search_lift', 'plays', 'engagements', 'follows', 'saves', 'profile_visits', 'engagement_rate', 'cost_per_click', 'cost_per_completed_view', 'cpm', 'downloads', 'units_sold', 'new_to_brand_units'], GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsMetricsValue]

class GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsReachWindow(TypedDict):
    kind: Literal['cumulative', 'period', 'rolling']
    period: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsReachWindowPeriod]
GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemMetrics: TypeAlias = dict[Literal['impressions', 'spend', 'clicks', 'ctr', 'views', 'completed_views', 'completion_rate', 'conversions', 'conversion_value', 'commissionable_value', 'roas', 'cost_per_acquisition', 'new_to_brand_rate', 'reach', 'frequency', 'grps', 'leads', 'incremental_sales_lift', 'brand_lift', 'foot_traffic', 'conversion_lift', 'brand_search_lift', 'plays', 'engagements', 'follows', 'saves', 'profile_visits', 'engagement_rate', 'cost_per_click', 'cost_per_completed_view', 'cpm', 'downloads', 'units_sold', 'new_to_brand_units'], GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemMetricsValue]

class GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemReachWindow(TypedDict):
    kind: Literal['cumulative', 'period', 'rolling']
    period: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemReachWindowPeriod]

class GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemBreakdownStatusItemPagination(TypedDict):
    has_more: bool
    cursor: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemBreakdownStatusItemPaginationCursor]
    total_count: NotRequired[int]

class SaveSellerRequestListing(TypedDict):
    description: NotRequired[str | None]
    '\n    Short Marketplace description, or null to clear.\n    '
    channels: NotRequired[list[SaveSellerRequestListingChannelsItem]]
    '\n    Buyer-visible channels.\n    '
    countries: NotRequired[list[SaveSellerRequestListingCountriesItem] | None]
    '\n    Buyer-visible ISO countries, or null to clear.\n    '
    acceptsAllCountries: NotRequired[bool]
    '\n    Accept briefs from every country.\n    '

class SaveSellerRequestMediaKit(TypedDict):
    description: NotRequired[str | None]
    '\n    Short Marketplace description, or null to clear.\n    '
    channels: NotRequired[list[SaveSellerRequestMediaKitChannelsItem]]
    '\n    Buyer-visible channels.\n    '
    countries: NotRequired[list[SaveSellerRequestMediaKitCountriesItem] | None]
    '\n    Buyer-visible ISO countries, or null to clear.\n    '
    acceptsAllCountries: NotRequired[bool]
    '\n    Accept briefs from every country.\n    '

class Node(TypedDict):
    nodeId: str
    '\n    Material nodeId field.\n    '
    nodeType: Literal['page', 'slide', 'sheet', 'section', 'region', 'text', 'list', 'table', 'image', 'chart', 'logo', 'caption', 'ocr', 'speaker_notes', 'accessibility_text']
    '\n    Material nodeType field.\n    '
    index: int
    '\n    Material index field.\n    '
    parentNodeId: NotRequired[str]
    '\n    Material parentNodeId field.\n    '
    readingOrder: NotRequired[int]
    '\n    Material readingOrder field.\n    '
    label: NotRequired[str]
    '\n    Material label field.\n    '
    geometry: NotRequired[Geometry]
    '\n    Material geometry field.\n    '
    textDigest: NotRequired[SaveMaterialRequestSourceDerivedStructureNodesItemTextDigest]
    '\n    Material textDigest field.\n    '
    artifactRef: NotRequired[str]
    '\n    Material artifactRef field.\n    '
    provenance: NotRequired[dict[str, str]]
    '\n    Material provenance field.\n    '

class Artifact(TypedDict):
    ref: str
    '\n    Material ref field.\n    '
    sourceLocator: NotRequired[str]
    '\n    Material sourceLocator field.\n    '
    role: Literal['original', 'page_image', 'slide_image', 'embedded_image', 'chart', 'logo', 'table', 'ocr', 'caption', 'structure', 'other']
    '\n    Material role field.\n    '
    contentType: NotRequired[str]
    '\n    Material contentType field.\n    '
    digest: NotRequired[SaveMaterialRequestSourceDerivedStructureArtifactsItemDigest]
    '\n    Material digest field.\n    '
    bytes: NotRequired[int]
    '\n    Material bytes field.\n    '
    widthPx: NotRequired[int]
    '\n    Material widthPx field.\n    '
    heightPx: NotRequired[int]
    '\n    Material heightPx field.\n    '
    kind: NotRequired[Literal['photo', 'illustration', 'logo', 'chart', 'diagram', 'screenshot', 'background', 'other']]
    '\n    Material kind field.\n    '
    crop: NotRequired[Crop]
    '\n    Material crop field.\n    '
    caption: NotRequired[Caption]
    '\n    Material caption field.\n    '
    ocr: NotRequired[Ocr]
    '\n    Material ocr field.\n    '
    altText: NotRequired[AltText]
    '\n    Material altText field.\n    '
    licenseScope: NotRequired[str]
    '\n    Material licenseScope field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceDerivedStructureArtifactsItemReuseRights]
    '\n    Material reuseRights field.\n    '
    confidentiality: NotRequired[SaveMaterialRequestSourceDerivedStructureArtifactsItemConfidentiality]
    '\n    Material confidentiality field.\n    '

class SaveMaterialRequestSourceDerivedStructure(TypedDict):
    originalDigest: NotRequired[SaveMaterialRequestSourceDerivedStructureOriginalDigest]
    '\n    Material originalDigest field.\n    '
    structureRef: NotRequired[str]
    '\n    Material structureRef field.\n    '
    readingOrderRef: NotRequired[str]
    '\n    Material readingOrderRef field.\n    '
    geometryRef: NotRequired[str]
    '\n    Material geometryRef field.\n    '
    ocrRef: NotRequired[str]
    '\n    Material ocrRef field.\n    '
    captionsRef: NotRequired[str]
    '\n    Material captionsRef field.\n    '
    parser: NotRequired[str]
    '\n    Material parser field.\n    '
    parserVersion: NotRequired[str]
    '\n    Material parserVersion field.\n    '
    nodes: NotRequired[list[Node]]
    '\n    Material nodes field.\n    '
    artifacts: NotRequired[list[Artifact]]
    '\n    Material artifacts field.\n    '

class SaveMaterialRequestSourceRenditionRef(TypedDict):
    renditionRevision: NotRequired[int]
    '\n    Material renditionRevision field.\n    '
    renditionRef: NotRequired[str]
    '\n    Material renditionRef field.\n    '
    blocksRef: NotRequired[str]
    '\n    Material blocksRef field.\n    '
    visualAssetsRef: NotRequired[str]
    '\n    Material visualAssetsRef field.\n    '
    diagnosticsRef: NotRequired[str]
    '\n    Material diagnosticsRef field.\n    '
    compositionReceiptsRef: NotRequired[str]
    '\n    Material compositionReceiptsRef field.\n    '
    extractor: NotRequired[str]
    '\n    Material extractor field.\n    '
    extractorVersion: NotRequired[str]
    '\n    Material extractorVersion field.\n    '
    configurationDigest: NotRequired[SaveMaterialRequestSourceRenditionRefsItemConfigurationDigest]
    '\n    Material configurationDigest field.\n    '
    completeness: NotRequired[dict[str, Literal['complete', 'degraded', 'unsupported', 'failed']]]
    '\n    Material completeness field.\n    '
SaveMaterialRequestSourceRenditionRefs: TypeAlias = list[SaveMaterialRequestSourceRenditionRef]

class Node1(TypedDict):
    nodeId: str
    '\n    Material nodeId field.\n    '
    nodeType: Literal['page', 'slide', 'sheet', 'section', 'region', 'text', 'list', 'table', 'image', 'chart', 'logo', 'caption', 'ocr', 'speaker_notes', 'accessibility_text']
    '\n    Material nodeType field.\n    '
    index: int
    '\n    Material index field.\n    '
    parentNodeId: NotRequired[str]
    '\n    Material parentNodeId field.\n    '
    readingOrder: NotRequired[int]
    '\n    Material readingOrder field.\n    '
    label: NotRequired[str]
    '\n    Material label field.\n    '
    geometry: NotRequired[Geometry]
    '\n    Material geometry field.\n    '
    textDigest: NotRequired[SaveMaterialRequestSourceItemsItemDerivedStructureNodesItemTextDigest]
    '\n    Material textDigest field.\n    '
    artifactRef: NotRequired[str]
    '\n    Material artifactRef field.\n    '
    provenance: NotRequired[dict[str, str]]
    '\n    Material provenance field.\n    '

class Artifact1(TypedDict):
    ref: str
    '\n    Material ref field.\n    '
    sourceLocator: NotRequired[str]
    '\n    Material sourceLocator field.\n    '
    role: Literal['original', 'page_image', 'slide_image', 'embedded_image', 'chart', 'logo', 'table', 'ocr', 'caption', 'structure', 'other']
    '\n    Material role field.\n    '
    contentType: NotRequired[str]
    '\n    Material contentType field.\n    '
    digest: NotRequired[SaveMaterialRequestSourceItemsItemDerivedStructureArtifactsItemDigest]
    '\n    Material digest field.\n    '
    bytes: NotRequired[int]
    '\n    Material bytes field.\n    '
    widthPx: NotRequired[int]
    '\n    Material widthPx field.\n    '
    heightPx: NotRequired[int]
    '\n    Material heightPx field.\n    '
    kind: NotRequired[Literal['photo', 'illustration', 'logo', 'chart', 'diagram', 'screenshot', 'background', 'other']]
    '\n    Material kind field.\n    '
    crop: NotRequired[Crop]
    '\n    Material crop field.\n    '
    caption: NotRequired[Caption]
    '\n    Material caption field.\n    '
    ocr: NotRequired[Ocr]
    '\n    Material ocr field.\n    '
    altText: NotRequired[AltText]
    '\n    Material altText field.\n    '
    licenseScope: NotRequired[str]
    '\n    Material licenseScope field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceItemsItemDerivedStructureArtifactsItemReuseRights]
    '\n    Material reuseRights field.\n    '
    confidentiality: NotRequired[SaveMaterialRequestSourceItemsItemDerivedStructureArtifactsItemConfidentiality]
    '\n    Material confidentiality field.\n    '

class SaveMaterialRequestSourceItemsItemDerivedStructure(TypedDict):
    originalDigest: NotRequired[SaveMaterialRequestSourceItemsItemDerivedStructureOriginalDigest]
    '\n    Material originalDigest field.\n    '
    structureRef: NotRequired[str]
    '\n    Material structureRef field.\n    '
    readingOrderRef: NotRequired[str]
    '\n    Material readingOrderRef field.\n    '
    geometryRef: NotRequired[str]
    '\n    Material geometryRef field.\n    '
    ocrRef: NotRequired[str]
    '\n    Material ocrRef field.\n    '
    captionsRef: NotRequired[str]
    '\n    Material captionsRef field.\n    '
    parser: NotRequired[str]
    '\n    Material parser field.\n    '
    parserVersion: NotRequired[str]
    '\n    Material parserVersion field.\n    '
    nodes: NotRequired[list[Node1]]
    '\n    Material nodes field.\n    '
    artifacts: NotRequired[list[Artifact1]]
    '\n    Material artifacts field.\n    '
SaveMaterialSuccessAccepted: TypeAlias = list[SaveMaterialSuccessAcceptedItem]
SaveMaterialSuccessRateCardAccepted: TypeAlias = list[SaveMaterialSuccessRateCardAcceptedItem]
SaveRfpRequestOriginChannels: TypeAlias = list[SaveRfpRequestOriginChannelsItem]
SaveRfpRequestRequestDimensionsChannels: TypeAlias = list[SaveRfpRequestRequestDimensionsChannelsItem]
SaveRfpRequestRequestDimensionsCreativeInputs: TypeAlias = list[SaveRfpRequestRequestDimensionsCreativeInputsItem]
SaveRfpRequestRequestConstraintsRequiredCreativeInputs: TypeAlias = list[SaveRfpRequestRequestConstraintsRequiredCreativeInputsItem]

class Access(TypedDict):
    accessRevision: int
    advertisers: list[SaveBuyerAgentSuccessBuyerAgentAdvertiser]
    advertiserCount: int
    advertisersTruncated: bool

class Notifications(TypedDict):
    subscriptions: list[SaveBuyerAgentSuccessBuyerAgentNotificationSubscription]
    subscriptionCount: int
    subscriptionsTruncated: bool
    destinations: list[SaveBuyerAgentSuccessBuyerAgentNotificationDestination]
    destinationCount: int
    destinationsTruncated: bool
    contextsTruncated: NotRequired[bool]

class SaveBuyerAgentSuccessBuyerAgentNoun(TypedDict):
    principalId: str
    principalKind: Literal['buyer_agent']
    displayName: str
    lifecycleState: Literal['active', 'suspended', 'retired']
    registeredAt: str
    credentialHandoff: NotRequired[CredentialHandoff]
    credentials: list[SaveBuyerAgentSuccessBuyerAgentCredential]
    credentialCount: int
    credentialsTruncated: bool
    activeCredentialCount: int
    access: Access
    notifications: Notifications | None

class SaveCampaignRequestOptimizationAttributionWindow(TypedDict):
    """
    Attribution window for conversion optimization
    """
    postClick: SaveCampaignRequestDuration
    '\n    Click-through attribution window\n    '
    postView: NotRequired[SaveCampaignRequestDuration]
    '\n    View-through attribution window\n    '

class SaveCampaignRequestMetricGoal(TypedDict):
    """
    Optimize for a seller-tracked delivery metric. No event source required.
    """
    kind: Literal['metric']
    '\n    Goal kind.\n    '
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'viewable_rate', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    '\n    Metric name. Includes viewed_seconds, attention_seconds, attention_score, reach. See enum.\n    '
    viewDurationSeconds: NotRequired[float]
    '\n    Min video seconds for completed_views metric.\n    '
    target: NotRequired[SaveCampaignRequestMetricGoalTargetCostPer | Target2]
    '\n    Target for this metric. When omitted, the seller maximizes metric volume within budget.\n    '
    attributionWindow: NotRequired[SaveCampaignRequestOptimizationAttributionWindow]
    '\n    Attribution window for this goal. When omitted, the seller uses their default.\n    '
    priority: NotRequired[int]
    '\n    Priority among goals on this package. 1 = highest. When omitted, sellers use array position.\n    '

class Blocker(TypedDict):
    """
    Why this account cannot use the source yet.
    """
    code: SaveEventSourceSuccessSellerObjectSyncBlockerCode
    message: str

class SellerAccount(TypedDict):
    storefront: Storefront
    accountId: str
    '\n    Seller account ID.\n    '
    sellerId: str | None
    "\n    The seller's ID for this source; null until the sync is proved.\n    "
    status: SaveEventSourceSuccessSellerObjectSyncState
    lastSyncedAt: str | None
    '\n    When this source last synced to this account; null if never.\n    '
    blocker: NotRequired[Blocker]
    '\n    Why this account cannot use the source yet.\n    '

class SaveEventSourceSuccessSavedEventSourceEntry(TypedDict):
    advertiserId: str
    eventSourceId: str
    '\n    Buyer-assigned event source ID; the only ID of this object.\n    '
    name: str
    eventTypes: list[Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']] | None
    '\n    Accepted event types; null accepts every type.\n    '
    valueCurrencies: list[str] | None
    actionSource: SaveEventSourceSuccessEventSourceActionSource | None
    surface: Surface | None
    health: Health
    '\n    AdCP EventSourceHealth: status is the grade; issues name what needs attention.\n    '
    managedBy: Literal['buyer', 'seller']
    sellerAccounts: list[SellerAccount]
    '\n    Per-seller-account sync state. Empty until seller sync is available.\n    '
    createdAt: str
    updatedAt: str
    action: Literal['created', 'updated', 'unchanged']
    setup: Setup

class SaveEventSourceSuccessFailedEventSourceEntry(TypedDict):
    action: Literal['failed']
    eventSourceId: str
    errors: list[SaveEventSourceSuccessEventSourceEntryError]

class Rights(TypedDict):
    """
    Usage rights for the asset.
    """
    status: NotRequired[Literal['unknown', 'owned', 'licensed', 'restricted', 'expired']]
    '\n    Rights status for this asset.\n    '
    usage: NotRequired[SaveCreativeSessionRequestDraftSourceAssetRightsUsage]
    '\n    Permitted asset usage.\n    '
    expires_at: NotRequired[SaveCreativeSessionRequestDraftSourceAssetRightsExpiresAt]
    '\n    ISO timestamp when the asset rights expire.\n    '
    notes: NotRequired[SaveCreativeSessionRequestDraftSourceAssetRightsNotes]
    '\n    Rights notes.\n    '

class SaveCreativeSessionRequestDraftSourceAsset(TypedDict):
    asset_id: NotRequired[str]
    '\n    Stable asset identifier, when known.\n    '
    label: str
    '\n    Human-readable asset label.\n    '
    url: str
    '\n    Asset URL.\n    '
    source: NotRequired[SaveCreativeSessionRequestDraftSourceAssetSource]
    '\n    Where the asset originated.\n    '
    role: NotRequired[SaveCreativeSessionRequestDraftSourceAssetRole]
    '\n    How the asset is used in the creative.\n    '
    locked_asset: NotRequired[bool]
    '\n    Whether generation must preserve this asset.\n    '
    can_transform: NotRequired[bool]
    '\n    Whether the asset may be transformed.\n    '
    preservation_notes: NotRequired[str]
    '\n    Instructions for preserving the asset.\n    '
    rights: NotRequired[Rights]
    '\n    Usage rights for the asset.\n    '
    dimensions: NotRequired[Dimensions]
    '\n    Known asset dimensions.\n    '
    render_crop: NotRequired[RenderCrop]
    '\n    Requested render crop.\n    '
    checksum: NotRequired[str]
    '\n    Asset content checksum, when available.\n    '
    mime_type: NotRequired[str]
    '\n    Asset media type.\n    '

class Rights1(TypedDict):
    """
    Usage rights for the asset.
    """
    status: NotRequired[Literal['unknown', 'owned', 'licensed', 'restricted', 'expired']]
    '\n    Rights status for this asset.\n    '
    usage: NotRequired[SaveCreativeSessionRequestDraftAssetsItemRightsUsage]
    '\n    Permitted asset usage.\n    '
    expires_at: NotRequired[SaveCreativeSessionRequestDraftAssetsItemRightsExpiresAt]
    '\n    ISO timestamp when the asset rights expire.\n    '
    notes: NotRequired[SaveCreativeSessionRequestDraftAssetsItemRightsNotes]
    '\n    Rights notes.\n    '

class SaveCreativeSessionRequestDraftAssetsItem(TypedDict):
    asset_id: NotRequired[str]
    '\n    Stable asset identifier, when known.\n    '
    label: str
    '\n    Human-readable asset label.\n    '
    url: str
    '\n    Asset URL.\n    '
    source: NotRequired[SaveCreativeSessionRequestDraftAssetsItemSource]
    '\n    Where the asset originated.\n    '
    role: NotRequired[SaveCreativeSessionRequestDraftAssetsItemRole]
    '\n    How the asset is used in the creative.\n    '
    locked_asset: NotRequired[bool]
    '\n    Whether generation must preserve this asset.\n    '
    can_transform: NotRequired[bool]
    '\n    Whether the asset may be transformed.\n    '
    preservation_notes: NotRequired[str]
    '\n    Instructions for preserving the asset.\n    '
    rights: NotRequired[Rights1]
    '\n    Usage rights for the asset.\n    '
    dimensions: NotRequired[Dimensions]
    '\n    Known asset dimensions.\n    '
    render_crop: NotRequired[RenderCrop]
    '\n    Requested render crop.\n    '
    checksum: NotRequired[str]
    '\n    Asset content checksum, when available.\n    '
    mime_type: NotRequired[str]
    '\n    Asset media type.\n    '

class SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer(TypedDict):
    kind: Literal['cost_per']
    '\n    Optimize toward a cost per result.\n    '
    value: SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPerValue
    '\n    Positive target cost per result.\n    '
    strength: NotRequired[Literal['cap', 'target']]
    '\n    Use a hard cap or a delivery target.\n    '

class SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate(TypedDict):
    kind: Literal['threshold_rate']
    '\n    Optimize toward a threshold rate.\n    '
    value: SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRateValue
    '\n    Positive threshold rate.\n    '

class SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoal(TypedDict):
    kind: Literal['metric', 'event']
    subject: str
    eventTypes: list[str]
    target: SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoalTarget | None

class SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoal(TypedDict):
    kind: Literal['metric', 'event']
    subject: str
    eventTypes: list[str]
    target: SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoalTarget | None

class MediaBuy(TypedDict):
    mediaBuyId: str
    '\n    Media buy id.\n    '
    name: str
    '\n    Media buy name.\n    '
    sellerId: str
    '\n    Seller the buy is placed with.\n    '
    sellerName: NotRequired[str]
    '\n    Seller display name.\n    '
    phase: Literal['draft', 'pendingApproval', 'inputRequired', 'active', 'ending', 'completed', 'canceled', 'failed', 'rejected']
    '\n    Lifecycle phase.\n    '
    isPaused: bool
    '\n    Whether the buy is paused.\n    '
    budget: OpenCampaignReceiptSuccessReceiptMediaBuysItemBudget
    '\n    Budget allocated to this buy (packages, else products).\n    '
    budgetShare: NotRequired[float]
    '\n    Percent of the staged total in this currency; absent when nothing is allocated or buys span currencies.\n    '
    flight: NotRequired[OpenCampaignReceiptSuccessReceiptMediaBuysItemFlight]
    '\n    Buy flight.\n    '
    attentionNote: NotRequired[str]
    '\n    Why the buy is not live yet, when the seller said.\n    '

class Receipt(TypedDict):
    campaignId: str
    '\n    Campaign id.\n    '
    advertiserId: str | None
    '\n    Owning advertiser; null for pre-linking campaigns.\n    '
    name: str
    '\n    Campaign name.\n    '
    phase: Literal['draft']
    '\n    Always draft.\n    '
    handling: Literal['tracking', 'managing']
    '\n    Whether Interchange manages or only tracks the campaign.\n    '
    budget: NotRequired[Budget]
    '\n    Campaign budget when set.\n    '
    flight: NotRequired[OpenCampaignReceiptSuccessReceiptFlight]
    '\n    Campaign flight when set.\n    '
    mediaBuys: list[MediaBuy]
    '\n    Staged media buys on the campaign, with their budget split.\n    '
    stagedBudgets: list[OpenCampaignReceiptSuccessReceiptStagedBudgetsItem]
    '\n    Sum of staged media-buy budgets, one entry per currency.\n    '
    blockers: list[Blocker2]
    '\n    Readiness blockers; empty when nothing is recorded.\n    '
    readyToGoLive: bool
    '\n    True when no readiness blocker is recorded.\n    '

class OpenCampaignReceiptResult(TypedDict):
    params: Params3
    '\n    Focus seeded into the Page.\n    '
    receipt: Receipt

class Totals1(TypedDict):
    metrics: GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsMetrics
    measurement_source: NotRequired[str]
    reach_unit: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsReachUnit]
    reach_window: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsReachWindow]
    effective_rate: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemTotalsEffectiveRate]

class BreakdownStatus(TypedDict):
    kind: Literal['device_type', 'device_platform', 'audience', 'placement']
    truncated: NotRequired[bool]
    pagination: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemBreakdownStatusItemPagination]

class ByPackageItem(TypedDict):
    package_id: GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemPackageId
    metrics: GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemMetrics
    measurement_source: NotRequired[str]
    reach_unit: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemReachUnit]
    reach_window: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemReachWindow]
    currency: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemCurrency]
    delivery_status: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemDeliveryStatus]
    pricing_model: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemPricingModel]
    pacing_index: NotRequired[float]
    rate: NotRequired[float]
    paused: NotRequired[bool]
    is_final: NotRequired[bool]
    finalized_at: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemByPackageItemFinalizedAt]
    measurement_window: NotRequired[str]
    supersedes_window: NotRequired[str]
    breakdown_status: list[BreakdownStatus | BreakdownStatus1 | BreakdownStatus2]

class MediaBuyDelivery(TypedDict):
    media_buy_id: GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemMediaBuyId
    status: GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemStatus
    currency: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemCurrency]
    expected_availability: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemExpectedAvailability]
    is_adjusted: NotRequired[bool]
    pricing_model: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemPricingModel]
    pacing_index: NotRequired[float]
    is_final: NotRequired[bool]
    finalized_at: NotRequired[GetDeliverySuccessDeliverySummaryMediaBuyDeliveriesItemFinalizedAt]
    totals: NotRequired[Totals1]
    by_package: NotRequired[list[ByPackageItem]]
    by_package_truncated: NotRequired[bool]
    by_package_total_count: NotRequired[int]

class DeliverySummary(TypedDict):
    status: GetDeliverySuccessDeliverySummaryStatus
    task_id: NotRequired[GetDeliverySuccessDeliverySummaryTaskId]
    reporting_period: NotRequired[ReportingPeriod]
    currency: NotRequired[GetDeliverySuccessDeliverySummaryCurrency]
    partial_data: NotRequired[bool]
    unavailable_count: NotRequired[int]
    sequence_number: NotRequired[int]
    next_expected_at: NotRequired[GetDeliverySuccessDeliverySummaryNextExpectedAt]
    pagination: NotRequired[GetDeliverySuccessDeliverySummaryPagination]
    reporting_revision: NotRequired[ReportingRevision]
    aggregated_totals: NotRequired[AggregatedTotals]
    media_buy_deliveries: NotRequired[list[MediaBuyDelivery]]
    media_buy_deliveries_truncated: NotRequired[bool]
    media_buy_deliveries_total_count: NotRequired[int]
    sandbox: NotRequired[bool]

class GetDeliveryResult2(TypedDict):
    report: Literal['live_campaign_delivery']
    query: Query1
    campaignId: str
    delivery: dict[str, JsonValue]
    '\n    Opaque legacy provider delivery payload. Source-validated against AdCP and bounded by the tool response size limit; use deliverySummary for the stable typed reporting contract.\n    '
    deliverySummary: NotRequired[DeliverySummary]
    authority: Literal['live_provider']
    semantics: Semantics1
GetDeliveryResult: TypeAlias = GetDeliveryResult1 | GetDeliveryResult2

class Source3(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['url']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: NotRequired[str]
    '\n    Material name field.\n    '
    url: SaveMaterialRequestSourceUrl
    '\n    Material url field.\n    '
    authorization: NotRequired[Literal['seller_attested', 'public_web', 'operator_verified']]
    '\n    Material authorization field.\n    '

class Source4(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['site']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: NotRequired[str]
    '\n    Material name field.\n    '
    rootUrl: SaveMaterialRequestSourceRootUrl
    '\n    Material rootUrl field.\n    '
    relatedDomains: NotRequired[list[RelatedDomain]]
    '\n    Material relatedDomains field.\n    '
    includePatterns: NotRequired[list[IncludePattern]]
    '\n    Material includePatterns field.\n    '
    excludePatterns: NotRequired[list[ExcludePattern]]
    '\n    Material excludePatterns field.\n    '
    maxPages: NotRequired[int]
    '\n    Material maxPages field.\n    '
    maxDepth: NotRequired[int]
    '\n    Material maxDepth field.\n    '
    maxBytes: NotRequired[int]
    '\n    Material maxBytes field.\n    '
    robotsPolicy: NotRequired[Literal['respect', 'seller_attested']]
    '\n    Material robotsPolicy field.\n    '

class Source5(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['upload']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: str
    '\n    Material name field.\n    '
    fileName: str
    '\n    Material fileName field.\n    '
    contentType: str
    '\n    Material contentType field.\n    '
    sizeBytes: int
    '\n    Material sizeBytes field.\n    '
    sha256: NotRequired[str]
    '\n    Material sha256 field.\n    '
    assetRef: NotRequired[str]
    '\n    Material assetRef field.\n    '
    fileRole: NotRequired[Literal['deck', 'rate_card', 'case_study', 'specification', 'policy', 'other']]
    '\n    Material fileRole field.\n    '

class Item(TypedDict):
    url: SaveMaterialRequestSourceItemsItemUrl
    '\n    Material url field.\n    '
    status: Literal['fetched', 'skipped', 'failed']
    '\n    Material status field.\n    '
    contentDigest: NotRequired[SaveMaterialRequestSourceItemsItemContentDigest]
    '\n    Material contentDigest field.\n    '
    bytes: NotRequired[int]
    '\n    Material bytes field.\n    '
    reason: NotRequired[str]
    '\n    Material reason field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceItemsItemDerivedStructure]
    '\n    Material derivedStructure field.\n    '

class Source6(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['crawl_manifest']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: str
    '\n    Material name field.\n    '
    rootUrl: SaveMaterialRequestSourceRootUrl
    '\n    Material rootUrl field.\n    '
    fetchedBy: Literal['platform', 'seller_supplied', 'seller_attested']
    '\n    Material fetchedBy field.\n    '
    generatedAt: str
    '\n    Material generatedAt field.\n    '
    items: list[Item]
    '\n    Material items field.\n    '
    manifestDigest: NotRequired[SaveMaterialRequestSourceManifestDigest]
    '\n    Material manifestDigest field.\n    '

class Source7(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['inline']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: str
    '\n    Material name field.\n    '
    content: str
    '\n    Material content field.\n    '

class Source8(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['history']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: str
    '\n    Material name field.\n    '
    historyKind: Literal['proposal', 'case_study', 'rate_card', 'policy']
    '\n    Material historyKind field.\n    '
    referenceId: str
    '\n    Material referenceId field.\n    '
    advertiserRef: NotRequired[str]
    '\n    Material advertiserRef field.\n    '
    summary: NotRequired[str]
    '\n    Material summary field.\n    '

class SaveMaterialInput1(TypedDict):
    action: Literal['create']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    clientRequestId: str
    '\n    Idempotency key for create/replace or candidate decision.\n    '
    source: Source3 | Source4 | Source5 | Source6 | Source7 | Source8
    '\n    Portable source: url, site, upload, crawl_manifest, inline, history.\n    '
    metadata: NotRequired[Metadata]
    '\n    Metadata fields; relevance is read-only.\n    '
    labels: NotRequired[dict[str, list[Label]]]
    '\n    Replace labels for each supplied dimension; [] clears.\n    '
    commit: NotRequired[bool]
    '\n    For an inline rate-card create only, commit an otherwise valid preview immediately.\n    '
    dryRun: NotRequired[bool]
    '\n    For an inline rate-card create only, return its preview without committing facts.\n    '

class Source9(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['url']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: NotRequired[str]
    '\n    Material name field.\n    '
    url: SaveMaterialRequestSourceUrl
    '\n    Material url field.\n    '
    authorization: NotRequired[Literal['seller_attested', 'public_web', 'operator_verified']]
    '\n    Material authorization field.\n    '

class Source10(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['site']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: NotRequired[str]
    '\n    Material name field.\n    '
    rootUrl: SaveMaterialRequestSourceRootUrl
    '\n    Material rootUrl field.\n    '
    relatedDomains: NotRequired[list[RelatedDomain]]
    '\n    Material relatedDomains field.\n    '
    includePatterns: NotRequired[list[IncludePattern]]
    '\n    Material includePatterns field.\n    '
    excludePatterns: NotRequired[list[ExcludePattern]]
    '\n    Material excludePatterns field.\n    '
    maxPages: NotRequired[int]
    '\n    Material maxPages field.\n    '
    maxDepth: NotRequired[int]
    '\n    Material maxDepth field.\n    '
    maxBytes: NotRequired[int]
    '\n    Material maxBytes field.\n    '
    robotsPolicy: NotRequired[Literal['respect', 'seller_attested']]
    '\n    Material robotsPolicy field.\n    '

class Source11(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['upload']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: str
    '\n    Material name field.\n    '
    fileName: str
    '\n    Material fileName field.\n    '
    contentType: str
    '\n    Material contentType field.\n    '
    sizeBytes: int
    '\n    Material sizeBytes field.\n    '
    sha256: NotRequired[str]
    '\n    Material sha256 field.\n    '
    assetRef: NotRequired[str]
    '\n    Material assetRef field.\n    '
    fileRole: NotRequired[Literal['deck', 'rate_card', 'case_study', 'specification', 'policy', 'other']]
    '\n    Material fileRole field.\n    '

class Source12(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['crawl_manifest']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: str
    '\n    Material name field.\n    '
    rootUrl: SaveMaterialRequestSourceRootUrl
    '\n    Material rootUrl field.\n    '
    fetchedBy: Literal['platform', 'seller_supplied', 'seller_attested']
    '\n    Material fetchedBy field.\n    '
    generatedAt: str
    '\n    Material generatedAt field.\n    '
    items: list[Item]
    '\n    Material items field.\n    '
    manifestDigest: NotRequired[SaveMaterialRequestSourceManifestDigest]
    '\n    Material manifestDigest field.\n    '

class Source13(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['inline']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: str
    '\n    Material name field.\n    '
    content: str
    '\n    Material content field.\n    '

class Source14(TypedDict):
    """
    Portable source: url, site, upload, crawl_manifest, inline, history.
    """
    kind: Literal['history']
    '\n    Material kind field.\n    '
    originalRef: NotRequired[SaveMaterialRequestSourceOriginalRef]
    '\n    Material originalRef field.\n    '
    originalDigest: NotRequired[SaveMaterialRequestSourceOriginalDigest]
    '\n    Material originalDigest field.\n    '
    derivedStructure: NotRequired[SaveMaterialRequestSourceDerivedStructure]
    '\n    Material derivedStructure field.\n    '
    renditionRefs: NotRequired[SaveMaterialRequestSourceRenditionRefs]
    '\n    Material renditionRefs field.\n    '
    reuseRights: NotRequired[SaveMaterialRequestSourceReuseRights]
    '\n    Material reuseRights field.\n    '
    name: str
    '\n    Material name field.\n    '
    historyKind: Literal['proposal', 'case_study', 'rate_card', 'policy']
    '\n    Material historyKind field.\n    '
    referenceId: str
    '\n    Material referenceId field.\n    '
    advertiserRef: NotRequired[str]
    '\n    Material advertiserRef field.\n    '
    summary: NotRequired[str]
    '\n    Material summary field.\n    '

class SaveMaterialInput2(TypedDict):
    action: Literal['replace_source']
    '\n    Create, revise, archive, or restore Material; decide candidates or mark a unit reusable.\n    '
    materialId: str
    '\n    Material id from save/search/get.\n    '
    expectedRevision: int
    '\n    Current source revision required before replacing or editing.\n    '
    clientRequestId: str
    '\n    Idempotency key for create/replace or candidate decision.\n    '
    source: Source9 | Source10 | Source11 | Source12 | Source13 | Source14
    '\n    Portable source: url, site, upload, crawl_manifest, inline, history.\n    '
    metadata: NotRequired[Metadata1]
    '\n    Metadata fields; relevance is read-only.\n    '
    labels: NotRequired[dict[str, list[Label]]]
    '\n    Replace labels for each supplied dimension; [] clears.\n    '
SaveMaterialInput: TypeAlias = SaveMaterialInput1 | SaveMaterialInput2 | SaveMaterialInput3 | SaveMaterialInput4 | SaveMaterialInput5 | SaveMaterialInput6 | SaveMaterialInput7 | SaveMaterialInput8 | SaveMaterialInput9 | SaveMaterialInput10 | SaveMaterialInput11

class SaveMaterialResult5(TypedDict):
    action: Literal['previewed_rate_card']
    materialId: SaveMaterialSuccessMaterialId
    sourceRevision: SaveMaterialSuccessSourceRevision
    accepted: SaveMaterialSuccessAccepted
    rejected: SaveMaterialSuccessRejected
    changes: SaveMaterialSuccessChanges
    floorWarnings: SaveMaterialSuccessFloorWarnings
    previewToken: SaveMaterialSuccessPreviewToken
    previewExpiresAt: SaveMaterialSuccessPreviewExpiresAt
    acceptedTotal: SaveMaterialSuccessAcceptedTotal
    rejectedTotal: SaveMaterialSuccessRejectedTotal
    truncated: SaveMaterialSuccessTruncated
    floorWarningsTruncated: SaveMaterialSuccessFloorWarningsTruncated

class RateCard(TypedDict):
    materialId: SaveMaterialSuccessRateCardMaterialId
    sourceRevision: SaveMaterialSuccessRateCardSourceRevision
    accepted: SaveMaterialSuccessRateCardAccepted
    rejected: SaveMaterialSuccessRateCardRejected
    changes: SaveMaterialSuccessRateCardChanges
    floorWarnings: SaveMaterialSuccessRateCardFloorWarnings
    previewToken: SaveMaterialSuccessRateCardPreviewToken
    previewExpiresAt: SaveMaterialSuccessRateCardPreviewExpiresAt
    acceptedTotal: SaveMaterialSuccessRateCardAcceptedTotal
    rejectedTotal: SaveMaterialSuccessRateCardRejectedTotal
    truncated: SaveMaterialSuccessRateCardTruncated
    floorWarningsTruncated: SaveMaterialSuccessRateCardFloorWarningsTruncated

class SaveMaterialResult6(TypedDict):
    materialId: str
    sourceRevision: int
    processingState: str
    idempotentReplay: bool
    next: Next1
    rateCard: RateCard
SaveMaterialResult: TypeAlias = SaveMaterialResult1 | SaveMaterialResult2 | SaveMaterialResult3 | SaveMaterialResult4 | SaveMaterialResult5 | SaveMaterialResult6 | SaveMaterialResult7

class Origin(TypedDict):
    """
    Origin.
    """
    kind: Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']
    '\n    Origin type.\n    '
    presetId: NotRequired[SaveRfpRequestI]
    '\n    Preset id.\n    '
    preset: NotRequired[Preset | dict[SaveRfpRequestP, SaveRfpRequestJ]]
    '\n    Preset data.\n    '
    sourceMaterialId: NotRequired[SaveRfpRequestI]
    '\n    Material id.\n    '
    buyer: NotRequired[SaveRfpRequestOriginBuyer]
    '\n    Buyer.\n    '
    advertiser: NotRequired[SaveRfpRequestOriginAdvertiser]
    '\n    Advertiser.\n    '
    category: NotRequired[SaveRfpRequestOriginCategory]
    '\n    Category.\n    '
    market: NotRequired[SaveRfpRequestOriginMarket]
    '\n    Market.\n    '
    channels: NotRequired[SaveRfpRequestOriginChannels]
    '\n    Channels.\n    '
    details: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    '\n    Origin facts.\n    '

class Dimensions3(TypedDict):
    """
    Intent.
    """
    channels: NotRequired[SaveRfpRequestRequestDimensionsChannels]
    '\n    Channels.\n    '
    channel: NotRequired[SaveRfpRequestRequestDimensionsChannel]
    '\n    Channel.\n    '
    formatKinds: NotRequired[SaveRfpRequestRequestDimensionsFormatKinds]
    '\n    Formats.\n    '
    format_kinds: NotRequired[SaveRfpRequestRequestDimensionsFormatKinds]
    '\n    Alias.\n    '
    productCount: NotRequired[SaveRfpRequestRequestDimensionsProductCount]
    '\n    Products.\n    '
    product_count: NotRequired[SaveRfpRequestRequestDimensionsProductCount]
    '\n    Alias.\n    '
    planRoles: NotRequired[SaveRfpRequestRequestDimensionsPlanRoles]
    '\n    Buyer requests; counter-pitch unsupported roles.\n    '
    plan_roles: NotRequired[SaveRfpRequestRequestDimensionsPlanRoles]
    '\n    Alias.\n    '
    audience: NotRequired[SaveRfpRequestRequestDimensionsAudience]
    '\n    Audience.\n    '
    creativeInputs: NotRequired[SaveRfpRequestRequestDimensionsCreativeInputs]
    '\n    Creative inputs.\n    '

class Constraints(TypedDict):
    """
    Constraints.
    """
    formatKinds: NotRequired[SaveRfpRequestRequestConstraintsFormatKinds]
    '\n    Formats.\n    '
    format_kinds: NotRequired[SaveRfpRequestRequestConstraintsFormatKinds]
    '\n    Alias.\n    '
    productCount: NotRequired[SaveRfpRequestRequestConstraintsProductCount]
    '\n    Products.\n    '
    product_count: NotRequired[SaveRfpRequestRequestConstraintsProductCount]
    '\n    Alias.\n    '
    planRoles: NotRequired[SaveRfpRequestRequestConstraintsPlanRoles]
    '\n    Roles.\n    '
    plan_roles: NotRequired[SaveRfpRequestRequestConstraintsPlanRoles]
    '\n    Alias.\n    '
    measurementRequirements: NotRequired[SaveRfpRequestRequestConstraintsMeasurementRequirements]
    '\n    Measurements.\n    '
    measurement_requirements: NotRequired[SaveRfpRequestRequestConstraintsMeasurementRequirements]
    '\n    Alias.\n    '
    requiredInputs: NotRequired[list[Literal['flight', 'audience']]]
    '\n    Required inputs.\n    '
    requiredCreativeInputs: NotRequired[SaveRfpRequestRequestConstraintsRequiredCreativeInputs]
    '\n    Creative inputs.\n    '
    locale: NotRequired[SaveRfpRequestRequestConstraintsLocale]
    '\n    Locale.\n    '
    mustInclude: NotRequired[list[SaveRfpRequestRequestConstraintsMustIncludeItem]]
    '\n    Legacy inputs (1-16, 1-160 chars).\n    '

class Request1(TypedDict):
    """
    Request.
    """
    brief: SaveRfpRequestP
    '\n    Brief.\n    '
    budget: NotRequired[Budget1]
    '\n    Budget.\n    '
    flight: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    '\n    Flight.\n    '
    dimensions: NotRequired[Dimensions3]
    '\n    Intent.\n    '
    constraints: NotRequired[Constraints]
    '\n    Constraints.\n    '

class SaveRfpInput1(TypedDict):
    action: Literal['create']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    origin: Origin
    '\n    Origin.\n    '
    purpose: Literal['live', 'draft', 'evaluation']
    '\n    Purpose.\n    '
    request: Request1
    '\n    Request.\n    '
    strategy: NotRequired[Strategy]
    '\n    Strategy.\n    '
    requiredEndorsedPairId: NotRequired[SaveRfpRequestI]
    '\n    Exact currently endorsed seller response pair to require for this composed turn.\n    '
    requiredLibraryUnitIds: NotRequired[list[RequiredLibraryUnitId]]
    '\n    Exact {materialId,unitId,renditionRevision} of reusable, price-free seller-offered Library units.\n    '

class Request2(TypedDict):
    """
    Request.
    """
    brief: SaveRfpRequestP
    '\n    Brief.\n    '
    budget: NotRequired[Budget1]
    '\n    Budget.\n    '
    flight: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    '\n    Flight.\n    '
    dimensions: NotRequired[Dimensions3]
    '\n    Intent.\n    '
    constraints: NotRequired[Constraints]
    '\n    Constraints.\n    '

class SaveRfpInput2(TypedDict):
    action: Literal['append_turn']
    clientRequestId: SaveRfpRequestI
    '\n    Idempotency key.\n    '
    rfpId: SaveRfpRequestI
    '\n    RFP id.\n    '
    parentTurnId: SaveRfpRequestI
    '\n    Parent turn id.\n    '
    request: Request2
    '\n    Request.\n    '
    strategy: NotRequired[Strategy]
    '\n    Strategy.\n    '
    requiredEndorsedPairId: NotRequired[SaveRfpRequestI]
    '\n    Exact currently endorsed seller response pair to require for this composed turn.\n    '
    requiredLibraryUnitIds: NotRequired[list[RequiredLibraryUnitId]]
    '\n    Exact {materialId,unitId,renditionRevision} of reusable, price-free seller-offered Library units.\n    '
SaveRfpInput: TypeAlias = SaveRfpInput1 | SaveRfpInput2 | SaveRfpInput3 | SaveRfpInput4 | SaveRfpInput5 | SaveRfpInput6 | SaveRfpInput7 | SaveRfpInput8 | SaveRfpInput9 | SaveRfpInput10 | SaveRfpInput11 | SaveRfpInput12 | SaveRfpInput13

class SaveBuyerAgentResult(TypedDict):
    kind: Literal['buyer_agent']
    object: SaveBuyerAgentSuccessBuyerAgentNoun

class SaveEventSourceResult(TypedDict):
    advertiserId: str
    replayed: bool
    eventSources: list[SaveEventSourceSuccessSavedEventSourceEntry | SaveEventSourceSuccessArchivedEventSourceEntry | SaveEventSourceSuccessFailedEventSourceEntry]
    '\n    One result per request entry, in request order.\n    '

class Draft(TypedDict):
    """
    Copy exact user brief to request.creative_brief.prompt; requested count to request.variant_count.
    """
    request: dict[str, JsonValue]
    '\n    Provider-neutral creative request.\n    '
    title: NotRequired[str]
    '\n    Creative brief title.\n    '
    persona: NotRequired[str]
    '\n    Intended audience persona.\n    '
    brand: NotRequired[str]
    '\n    Brand for the creative.\n    '
    objective: NotRequired[str]
    '\n    Creative objective.\n    '
    prompt: NotRequired[str]
    '\n    Creative prompt.\n    '
    source_asset: NotRequired[SaveCreativeSessionRequestDraftSourceAsset]
    '\n    Primary locked reference asset.\n    '
    assets: NotRequired[list[SaveCreativeSessionRequestDraftAssetsItem]]
    '\n    Reference assets for the session.\n    '
    renditions: NotRequired[list[Rendition]]
    '\n    Derived reference-asset renditions.\n    '
    partial_success: NotRequired[bool]
    '\n    Whether partial generation success is acceptable.\n    '

class SaveCreativeSessionInput1(TypedDict):
    operation: Literal['save_draft']
    '\n    Save the supplied session draft.\n    '
    campaignId: str
    '\n    Campaign that owns the Creative Session.\n    '
    engine: NotRequired[Engine]
    '\n    Leave unset for funded image drafts unless user names an engine. See Creative Engines guide.\n    '
    draft: Draft
    '\n    Copy exact user brief to request.creative_brief.prompt; requested count to request.variant_count.\n    '
    idempotencyKey: str
    '\n    Idempotency key for this draft save.\n    '
SaveCreativeSessionInput: TypeAlias = SaveCreativeSessionInput1 | SaveCreativeSessionInput2 | SaveCreativeSessionInput3 | SaveCreativeSessionInput4 | SaveCreativeSessionInput5

class OptimizationGoals(TypedDict):
    kind: Literal['metric']
    '\n    Optimize a delivery metric.\n    '
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    '\n    Delivery metric to optimize.\n    '
    reach_unit: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    '\n    Reach unit; required for reach.\n    '
    target_frequency: NotRequired[TargetFrequency]
    '\n    Desired exposure frequency and window.\n    '
    view_duration_seconds: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemViewDurationSeconds]
    '\n    Minimum viewed seconds when optimizing views.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate]
    '\n    Optional delivery outcome target.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class OptimizationGoals1(TypedDict):
    kind: Literal['event']
    '\n    Optimize tracked conversion events.\n    '
    event_sources: list[EventSource2]
    '\n    Event sources for this conversion goal.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | Target5 | Target6]
    '\n    Optional conversion outcome target.\n    '
    attribution_window: NotRequired[AttributionWindow]
    '\n    Optional event attribution settings.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class OptimizationGoals2(TypedDict):
    kind: Literal['vendor_metric']
    '\n    Optimize a vendor-defined metric.\n    '
    vendor: Vendor2
    '\n    Vendor that owns the metric definition.\n    '
    metric_id: str
    '\n    Vendor-defined metric identifier.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate]
    '\n    Optional vendor-metric outcome target.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class BudgetAllocation1(TypedDict):
    """
    New-media-buy-only allocation: fixed requires products[].budget; seller_optimized refuses it.
    """
    mode: Literal['seller_optimized']
    '\n    Let the seller distribute one campaign total.\n    '
    optimization_goals: list[OptimizationGoals | OptimizationGoals1 | OptimizationGoals2]
    '\n    Goals that guide the seller allocation.\n    '

class SaveMediaBuyInput4(TypedDict):
    mediaBuyId: NotRequired[str]
    '\n    ID of an existing DRAFT media buy to update.\n    '
    fromProposalId: NotRequired[str]
    '\n    sfp1: qualified Proposal ID from request_proposals to accept into a new DRAFT media buy.\n    '
    campaignId: NotRequired[str]
    '\n    Campaign to place the media buy under. Required for explicit creation.\n    '
    channelGroupId: NotRequired[str]
    '\n    channelGroupId for a new buy. Required when campaign has channelGroups; invalid on updates.\n    '
    sellerId: NotRequired[str]
    '\n    Storefront ID of the seller. Required for explicit creation.\n    '
    products: NotRequired[list[Product]]
    '\n    Products. Omit with fromProposalId; retain allocation.\n    '
    budget: NotRequired[Budget8]
    '\n    Single total. One-allocation proposal allowed; multi: products[].budget; else retain allocation.\n    '
    budgetAllocation: NotRequired[BudgetAllocation | BudgetAllocation1]
    '\n    New-media-buy-only allocation: fixed requires products[].budget; seller_optimized refuses it.\n    '
    flight: NotRequired[Flight1]
    '\n    Flight for a new or existing draft. Specific starts need a future UTC day; use "asap" to start now.\n    '
    isArchived: NotRequired[bool]
    '\n    Update only: true archives an unwanted DRAFT (campaign unaffected). Send alone. false unsupported.\n    '
    isPaused: NotRequired[bool]
    '\n    true pauses ACTIVE; false activates PAUSED; same state unchanged. Other states refuse. Send alone.\n    '
    isCanceled: NotRequired[bool]
    '\n    Update only: true irreversibly requests cancellation of one buy; send as the only change. Seller confirmation may be pending; already canceled returns unchanged. false is unsupported.\n    '
    idempotencyKey: str
    '\n    Creation: returned productQueryId. Update: deduplication key. Unused with fromProposalId.\n    '

class OptimizationGoals3(TypedDict):
    kind: Literal['metric']
    '\n    Optimize a delivery metric.\n    '
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    '\n    Delivery metric to optimize.\n    '
    reach_unit: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    '\n    Reach unit; required for reach.\n    '
    target_frequency: NotRequired[TargetFrequency]
    '\n    Desired exposure frequency and window.\n    '
    view_duration_seconds: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemViewDurationSeconds]
    '\n    Minimum viewed seconds when optimizing views.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate]
    '\n    Optional delivery outcome target.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class OptimizationGoals4(TypedDict):
    kind: Literal['event']
    '\n    Optimize tracked conversion events.\n    '
    event_sources: list[EventSource2]
    '\n    Event sources for this conversion goal.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | Target7 | Target8]
    '\n    Optional conversion outcome target.\n    '
    attribution_window: NotRequired[AttributionWindow]
    '\n    Optional event attribution settings.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class OptimizationGoals5(TypedDict):
    kind: Literal['vendor_metric']
    '\n    Optimize a vendor-defined metric.\n    '
    vendor: Vendor4
    '\n    Vendor that owns the metric definition.\n    '
    metric_id: str
    '\n    Vendor-defined metric identifier.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate]
    '\n    Optional vendor-metric outcome target.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class BudgetAllocation3(TypedDict):
    """
    New-media-buy-only allocation: fixed requires products[].budget; seller_optimized refuses it.
    """
    mode: Literal['seller_optimized']
    '\n    Let the seller distribute one campaign total.\n    '
    optimization_goals: list[OptimizationGoals3 | OptimizationGoals4 | OptimizationGoals5]
    '\n    Goals that guide the seller allocation.\n    '

class SaveMediaBuyInput5(TypedDict):
    mediaBuyId: NotRequired[str]
    fromProposalId: NotRequired[str]
    campaignId: NotRequired[str]
    channelGroupId: NotRequired[str]
    sellerId: NotRequired[str]
    products: NotRequired[list[Product1]]
    budget: NotRequired[Budget8]
    budgetAllocation: NotRequired[BudgetAllocation | BudgetAllocation3]
    flight: NotRequired[Flight1]
    isArchived: NotRequired[bool]
    isPaused: NotRequired[bool]
    isCanceled: NotRequired[bool]
    idempotencyKey: str

class OptimizationGoals6(TypedDict):
    kind: Literal['metric']
    '\n    Optimize a delivery metric.\n    '
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    '\n    Delivery metric to optimize.\n    '
    reach_unit: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    '\n    Reach unit; required for reach.\n    '
    target_frequency: NotRequired[TargetFrequency]
    '\n    Desired exposure frequency and window.\n    '
    view_duration_seconds: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemViewDurationSeconds]
    '\n    Minimum viewed seconds when optimizing views.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate]
    '\n    Optional delivery outcome target.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class OptimizationGoals7(TypedDict):
    kind: Literal['event']
    '\n    Optimize tracked conversion events.\n    '
    event_sources: list[EventSource2]
    '\n    Event sources for this conversion goal.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | Target9 | Target10]
    '\n    Optional conversion outcome target.\n    '
    attribution_window: NotRequired[AttributionWindow]
    '\n    Optional event attribution settings.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class OptimizationGoals8(TypedDict):
    kind: Literal['vendor_metric']
    '\n    Optimize a vendor-defined metric.\n    '
    vendor: Vendor6
    '\n    Vendor that owns the metric definition.\n    '
    metric_id: str
    '\n    Vendor-defined metric identifier.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate]
    '\n    Optional vendor-metric outcome target.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class BudgetAllocation5(TypedDict):
    """
    New-media-buy-only allocation: fixed requires products[].budget; seller_optimized refuses it.
    """
    mode: Literal['seller_optimized']
    '\n    Let the seller distribute one campaign total.\n    '
    optimization_goals: list[OptimizationGoals6 | OptimizationGoals7 | OptimizationGoals8]
    '\n    Goals that guide the seller allocation.\n    '

class SaveMediaBuyInput6(TypedDict):
    mediaBuyId: NotRequired[str]
    fromProposalId: NotRequired[str]
    campaignId: NotRequired[str]
    channelGroupId: NotRequired[str]
    sellerId: NotRequired[str]
    products: NotRequired[list[Product2]]
    budget: NotRequired[Budget8]
    budgetAllocation: NotRequired[BudgetAllocation | BudgetAllocation5]
    flight: NotRequired[Flight1]
    isArchived: NotRequired[bool]
    isPaused: NotRequired[bool]
    isCanceled: NotRequired[bool]
    idempotencyKey: str

class OptimizationGoals9(TypedDict):
    kind: Literal['metric']
    '\n    Optimize a delivery metric.\n    '
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    '\n    Delivery metric to optimize.\n    '
    reach_unit: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    '\n    Reach unit; required for reach.\n    '
    target_frequency: NotRequired[TargetFrequency]
    '\n    Desired exposure frequency and window.\n    '
    view_duration_seconds: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemViewDurationSeconds]
    '\n    Minimum viewed seconds when optimizing views.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate]
    '\n    Optional delivery outcome target.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class OptimizationGoals10(TypedDict):
    kind: Literal['event']
    '\n    Optimize tracked conversion events.\n    '
    event_sources: list[EventSource2]
    '\n    Event sources for this conversion goal.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | Target11 | Target12]
    '\n    Optional conversion outcome target.\n    '
    attribution_window: NotRequired[AttributionWindow]
    '\n    Optional event attribution settings.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class OptimizationGoals11(TypedDict):
    kind: Literal['vendor_metric']
    '\n    Optimize a vendor-defined metric.\n    '
    vendor: Vendor8
    '\n    Vendor that owns the metric definition.\n    '
    metric_id: str
    '\n    Vendor-defined metric identifier.\n    '
    target: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetCostPer | SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemTargetThresholdRate]
    '\n    Optional vendor-metric outcome target.\n    '
    priority: NotRequired[SaveMediaBuyRequestBudgetAllocationOptimizationGoalsItemPriority]
    '\n    Goal priority; lower values take precedence.\n    '

class BudgetAllocation7(TypedDict):
    """
    New-media-buy-only allocation: fixed requires products[].budget; seller_optimized refuses it.
    """
    mode: Literal['seller_optimized']
    '\n    Let the seller distribute one campaign total.\n    '
    optimization_goals: list[OptimizationGoals9 | OptimizationGoals10 | OptimizationGoals11]
    '\n    Goals that guide the seller allocation.\n    '

class SaveMediaBuyInput7(TypedDict):
    mediaBuyId: NotRequired[str]
    fromProposalId: NotRequired[str]
    campaignId: NotRequired[str]
    channelGroupId: NotRequired[str]
    sellerId: NotRequired[str]
    products: NotRequired[list[Product3]]
    budget: NotRequired[Budget8]
    budgetAllocation: NotRequired[BudgetAllocation | BudgetAllocation7]
    flight: NotRequired[Flight1]
    isArchived: NotRequired[bool]
    isPaused: NotRequired[bool]
    isCanceled: NotRequired[bool]
    idempotencyKey: str
SaveMediaBuyInput: TypeAlias = SaveMediaBuyInput5 | SaveMediaBuyInput6 | SaveMediaBuyInput7

class GoalAnswer(TypedDict):
    productId: str
    storefrontId: NotRequired[str | None]
    "\n    The Storefront the answered line resolves to, fixed when the answer was booked so a later refresh keeps it for exactly that Storefront's line. Present on every booked answer whose line resolved to a Storefront, campaign-derived or copied from an accepted proposal alike.\n    "
    pricingOptionId: str | None
    pricingModel: str | None
    fixedPrice: float | None
    currency: str | None
    deliveryType: Literal['guaranteed', 'non_guaranteed'] | None
    measurementTerms: JsonValue
    sellerOptimizationGoals: list[JsonValue] | None
    askedGoal: SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAskedGoal | None
    answeredTarget: SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemAnsweredTarget | None
    commitment: SaveMediaBuySuccessMediaBuyGoalCommitmentGoalAnswersItemCommitment

class GoalCommitment(TypedDict):
    source: Literal['proposal', 'campaign']
    "\n    Where the answers came from: 'proposal' when at least one product on the buy keeps the accepted proposal version's answer, 'campaign' when every answer was derived from the campaign's goals and the products' own terms.\n    "
    proposalVersionId: NotRequired[str]
    "\n    The accepted proposal version the buy was booked from, whenever there was one. Present even when source reads 'campaign' because none of the buy's products matched that version's answers, so the booking's provenance is never lost.\n    "
    kind: SaveMediaBuySuccessMediaBuyGoalCommitmentKind
    askedGoal: SaveMediaBuySuccessMediaBuyGoalCommitmentAskedGoal | None
    answeredTarget: SaveMediaBuySuccessMediaBuyGoalCommitmentAnsweredTarget | None
    "\n    The target the products' terms commit or aim at for the asked goal, of the same kind as the ask when they answer it: the worst across products, meaning the highest cost_per, the lowest threshold_rate, or the lowest per_ad_spend. maximize_value carries no number.\n    "
    meetsAskedTarget: bool | None
    '\n    Whether every product answers the asked target, judged by kind: a cost_per is met at or under the ask, a threshold_rate or per_ad_spend at or above it. false when any product misses it or did not answer with the same kind. null when the goal carries no target or a maximize_value target, which has no number to meet.\n    '
    goalAnswers: list[GoalAnswer]
    '\n    One answer per product on the buy: the product the accepted proposal answered keeps that answer, any other product is answered from its own terms.\n    '
    goalAnswersTruncated: NotRequired[Literal[True]]
    '\n    Present when this read carries fewer goalAnswers than the buy has.\n    '

class MediaBuy2(TypedDict):
    mediaBuyId: str
    name: str
    channelGroup: NotRequired[ChannelGroup]
    optimizationGoals: NotRequired[JsonValue]
    goalCommitment: NotRequired[GoalCommitment]
    frequencyCap: NotRequired[FrequencyCap5]
    phase: SaveMediaBuySuccessMediaBuyPhase
    isPaused: bool
    isArchived: bool
    ending: NotRequired[Ending]
    flight: NotRequired[Flight5]
    pendingReason: NotRequired[str]
    pendingSince: NotRequired[str]
    pendingAt: NotRequired[Literal['storefront', 'salesagent', 'unknown']]
    errorCode: NotRequired[str]
    errorOwner: NotRequired[str]
    forwardedAt: NotRequired[str]
    buyerReference: NotRequired[str]
    createdAt: str
    updatedAt: str

class SaveMediaBuyResult(TypedDict):
    action: Literal['staged', 'updated', 'paused', 'resumed', 'unchanged', 'archived', 'cancellation_requested', 'canceled']
    campaignId: NotRequired[str]
    mediaBuyId: NotRequired[str]
    isPaused: NotRequired[bool]
    previousStatus: NotRequired[str]
    newStatus: NotRequired[str]
    cancellationPending: NotRequired[bool]
    mediaBuysStaged: NotRequired[float]
    mediaBuyRefs: NotRequired[list[MediaBuyRef]]
    proposalSource: NotRequired[ProposalSource]
    mediaBuy: NotRequired[MediaBuy2]
    warnings: NotRequired[list[str]]
    errors: NotRequired[list[Error12]]

class SaveCampaignRequestEventGoal(TypedDict):
    """
    Optimize for advertiser-tracked conversion events via event sources.
    """
    kind: Literal['event']
    '\n    Goal kind.\n    '
    eventSources: list[EventSource]
    '\n    Event source and type pairs feeding this goal. Seller deduplicates by event_id across entries.\n    '
    target: NotRequired[SaveCampaignRequestEventGoalTargetCostPer | Target | Target1]
    '\n    Target cost or return. When omitted, the seller maximizes conversions within budget.\n    '
    attributionWindow: NotRequired[SaveCampaignRequestOptimizationAttributionWindow]
    '\n    Attribution window for this goal. When omitted, the seller uses their default.\n    '
    priority: NotRequired[int]
    '\n    Priority among goals on this package. 1 = highest. When omitted, sellers use array position.\n    '
SaveCampaignRequestOptimizationGoal: TypeAlias = SaveCampaignRequestEventGoal | SaveCampaignRequestMetricGoal
'\nA single optimization target. Either kind "event" (conversion events) or kind "metric" (seller-native delivery metric).\n'

class SaveCampaignInput(TypedDict):
    sponsoredBuyerCustomerId: NotRequired[str]
    '\n    Server-issued self-serve buyer child scope from the Campaigns Page launch.\n    '
    campaignId: NotRequired[str]
    '\n    ID of the campaign to update. Omit to create a new one.\n    '
    advertiserId: NotRequired[str]
    '\n    Required when creating. The advertiser this campaign belongs to.\n    '
    name: NotRequired[str]
    '\n    Campaign name.\n    '
    expectedRevision: NotRequired[int]
    '\n    Revision from last get. Required to cancel; re-read and retry after a conflict.\n    '
    brief: NotRequired[str | None]
    '\n    Campaign brief: goal, audience, and promoted item. Null clears it; omit to leave it unchanged.\n    '
    flight: NotRequired[Flight | None]
    '\n    Flight window. Null clears it; omit to leave it unchanged.\n    '
    budget: NotRequired[Budget7]
    '\n    Campaign budget.\n    '
    frequencyCap: NotRequired[FrequencyCap | None]
    '\n    Per-seller AdCP 3.2 MediaBuy cap. Null clears it; draft only. Other levels are unavailable.\n    '
    confirmLaunch: NotRequired[bool]
    '\n    Use with desiredPhase: active. Omit = preview what will launch. true = execute.\n    '
    sellerIds: NotRequired[list[str]]
    '\n    Numeric seller IDs (as strings). Non-numeric values are skipped.\n    '
    creativeIds: NotRequired[list[CreativeId]]
    '\n    All creatives on this campaign; replaces membership, a missing id detaches. Omit to keep.\n    '
    autonomy: NotRequired[Autonomy]
    '\n    Autonomy settings, persisted per campaign. Set one or both dimensions; omitted are unchanged.\n    '
    desiredPhase: NotRequired[Literal['active', 'canceled']]
    '\n    active: launch. canceled: cancel all buys; revision required; stays ending while sellers confirm.\n    '
    isPaused: NotRequired[bool]
    '\n    true to pause; false to reactivate. Only valid on active campaigns.\n    '
    isArchived: NotRequired[bool]
    '\n    true archives; false restores an archived campaign as a draft (send alone).\n    '
    optimizationGoals: NotRequired[list[SaveCampaignRequestOptimizationGoal] | None]
    '\n    Only when the buyer states a goal. Never infer from name or brief. null clears.\n    '
    catalogId: NotRequired[str | None]
    '\n    Advertiser catalog to bind to this campaign. Null clears the binding; omit to leave it unchanged.\n    '
    idempotencyKey: str
    '\n    Required. Dedupes creates only; updates rely on expectedRevision.\n    '
    tracking: NotRequired[Tracking1]
    '\n    Campaign trackers, advertiser overrides, and creative URL parameters.\n    '
    targetingOverlay: NotRequired[TargetingOverlay | None]
    '\n    AdCP campaign targeting overlay.\n    '
    targeting: NotRequired[Targeting | None]
    '\n    Deprecated; unchanged. Use targetingOverlay. AI-10440: 14-day notice; planned 2 Nov 2026.\n    '
    channelGroups: NotRequired[list[ChannelGroups | ChannelGroups1] | None]
    '\n    Inventory execution groups. Use a preset or custom AdCP dimensions; null removes all groups.\n    '
    audienceConfig: NotRequired[AudienceConfig]
    '\n    Campaign audiences. deleteMissing: true replaces each list. Seller sync is unavailable (AI-10203).\n    '
    labels: NotRequired[dict[str, list[Label]]]
    '\n    Replace labels for each supplied dimension; [] clears.\n    '
    propertyListId: NotRequired[str | None]
    '\n    Apply an include list to active media buys; it must belong to the advertiser. Null clears targeting.\n    '
