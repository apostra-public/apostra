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
SaveAskSuccessSchema0: TypeAlias = str | None
SaveBillingRequestSchema1: TypeAlias = Literal['capture_link']

class SaveBillingSuccessPendingConfirmationResult(TypedDict):
    status: Literal['pending_confirmation']
    confirmationToken: str
    summary: str
    expiresAt: str

class SaveBillingSuccessCaptureLinkIssuedResult(TypedDict):
    method: Literal['capture_link']
    url: NotRequired[str]
    status: Literal['pending', 'opened', 'verified', 'expired']
    expiresAt: str

class SaveAdvertiserGrantSuccessSchema0(TypedDict):
    organizationRef: str
    displayName: str
SearchRequestCreativeRole: TypeAlias = Literal['evergreen', 'reference']
SearchRequestCreativeSource: TypeAlias = Literal['uploaded', 'generated', 'connected']

class GetRequestSchema51(TypedDict):
    cursor: NotRequired[str | None]
    limit: NotRequired[int]
SaveConnectionRequestSchema3: TypeAlias = str
SaveConnectionRequestBuyerStorefrontSelectionDecision: TypeAlias = Literal['DEFAULT', 'ALWAYS_INCLUDE', 'ALWAYS_EXCLUDE']
SaveConnectionRequestBuyerAdvertiserStorefrontActivationPreferenceDecision: TypeAlias = Literal['DEFAULT', 'ENABLED', 'DISABLED']
SaveConnectionSuccessSchema0: TypeAlias = dict[str, JsonValue] | None

class SaveConnectionSuccessSchema11(TypedDict):
    state: Literal['committed']
    receiptId: str

class SaveConnectionSuccessSchema12(TypedDict):
    state: Literal['replayed']
    receiptId: str

class SaveConnectionSuccessSchema13(TypedDict):
    state: Literal['failed']
    receiptId: str

class SaveConnectionSuccessSchema14(TypedDict):
    state: Literal['missing']

class SaveConnectionSuccessSchema15(TypedDict):
    state: Literal['in_flight']
    receiptId: str

class SaveConnectionSuccessSchema16(TypedDict):
    state: Literal['reconcile_required']
    receiptId: str

class SaveConnectionSuccessSchema17(TypedDict):
    state: Literal['expired']
    receiptId: str

class SaveConnectionSuccessSchema18(TypedDict):
    state: Literal['conflict']
    receiptId: str
SaveConnectionSuccessSchema1: TypeAlias = SaveConnectionSuccessSchema11 | SaveConnectionSuccessSchema12 | SaveConnectionSuccessSchema13 | SaveConnectionSuccessSchema14 | SaveConnectionSuccessSchema15 | SaveConnectionSuccessSchema16 | SaveConnectionSuccessSchema17 | SaveConnectionSuccessSchema18
SaveLibraryRequestSuccessSchema0: TypeAlias = str
SaveLibraryRequestSuccessSchema1: TypeAlias = str
SaveLibraryRequestSuccessSchema2: TypeAlias = str
SaveLibraryRequestSuccessSchema3: TypeAlias = str | None

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
OpenCampaignReceiptSuccessSchema8: TypeAlias = float
OpenCampaignReceiptSuccessSchema9: TypeAlias = str

class OpenCampaignReceiptSuccessSchema12(TypedDict):
    startAt: str
    endAt: str

class OpenCampaignReceiptSuccessSchema15(TypedDict):
    total: OpenCampaignReceiptSuccessSchema8
    currency: OpenCampaignReceiptSuccessSchema9
UploadCreativeAssetRequestSchema1: TypeAlias = str
UploadCreativeAssetSuccessSchema0: TypeAlias = str

class GetDeliverySuccessSchema10(TypedDict):
    value: float | bool | None
    status: Literal['available', 'unavailable']
    reason: NotRequired[Literal['projected_zero', 'missing', 'currency_unavailable', 'incomplete']]
GetDeliverySuccessSchema11: TypeAlias = Literal['get_seller_reporting_metrics', 'get_buyer_reporting_metrics', 'get_seller_margin_reporting']

class Revision(TypedDict):
    sequenceNumber: NotRequired[float]
    observedAt: NotRequired[str]
    receivedAt: NotRequired[str]
    finalizedAt: NotRequired[str]
    dataThrough: NotRequired[str]
    sourceTimezone: NotRequired[str]
    restatesSequenceNumber: NotRequired[float | None]
GetDeliverySuccessSchema13 = TypedDict('GetDeliverySuccessSchema13', {'status': Literal['available', 'unavailable', 'not_applicable'], 'class': Literal['SNAPSHOT', 'OFFICIAL'] | None, 'revision': Revision | None, 'reason': NotRequired[Literal['revision_evidence_unavailable', 'cumulative_margin_ledger']], 'supportedClasses': NotRequired[list[Literal['SNAPSHOT', 'OFFICIAL']]]})
GetDeliverySuccessSchema17: TypeAlias = str

class GetDeliverySuccessSchema18(TypedDict):
    has_more: bool
    cursor: NotRequired[GetDeliverySuccessSchema17]
    total_count: NotRequired[int]
GetDeliverySuccessSchema19: TypeAlias = float | None

class GetDeliverySuccessSchema21(TypedDict):
    interval: int
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
GetDeliverySuccessSchema23: TypeAlias = Literal['cpm', 'vcpm', 'cpc', 'cpcv', 'cpv', 'cpp', 'cpa', 'revenue_share', 'flat_rate', 'time']
GetDeliverySuccessSchema24: TypeAlias = dict[Literal['impressions', 'spend', 'clicks', 'ctr', 'views', 'completed_views', 'completion_rate', 'conversions', 'conversion_value', 'commissionable_value', 'roas', 'cost_per_acquisition', 'new_to_brand_rate', 'reach', 'frequency', 'grps', 'leads', 'incremental_sales_lift', 'brand_lift', 'foot_traffic', 'conversion_lift', 'brand_search_lift', 'plays', 'engagements', 'follows', 'saves', 'profile_visits', 'engagement_rate', 'cost_per_click', 'cost_per_completed_view', 'cpm', 'downloads', 'units_sold', 'new_to_brand_units'], GetDeliverySuccessSchema19]

class GetDeliverySuccessSchema25(TypedDict):
    kind: Literal['cumulative', 'period', 'rolling']
    period: NotRequired[GetDeliverySuccessSchema21]
SaveSellerRequestSchema1: TypeAlias = str
SaveSellerRequestSchema27: TypeAlias = Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence', 'audio', 'video']
SaveSellerRequestSchema30: TypeAlias = str

class SaveSellerRequestSchema34(TypedDict):
    description: NotRequired[str | None]
    channels: NotRequired[list[SaveSellerRequestSchema27]]
    countries: NotRequired[list[SaveSellerRequestSchema30] | None]
    acceptsAllCountries: NotRequired[bool]
SaveSellerRequestSchema41: TypeAlias = Literal['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD', 'CNY', 'HKD', 'SGD', 'SEK', 'NOK', 'DKK', 'PLN', 'KRW', 'INR', 'MXN', 'BRL', 'ZAR']
SaveSellerSuccessSchema0: TypeAlias = dict[str, JsonValue]
SaveInventorySourceSuccessSchema0: TypeAlias = dict[str, JsonValue]
SaveCoverageRequestSchema4Item: TypeAlias = str
SaveCoverageRequestSchema4: TypeAlias = list[SaveCoverageRequestSchema4Item]

class SaveCoverageSuccessSchema0(TypedDict):
    items: list[JsonValue]
    count: int
    truncated: bool
SaveMaterialRequestSchema11: TypeAlias = str
SaveMaterialRequestSchema13: TypeAlias = str

class Geometry(TypedDict):
    page: NotRequired[int]
    slide: NotRequired[int]
    sheet: NotRequired[int]
    x: float
    y: float
    width: float
    height: float
    unit: Literal['pt', 'px', 'percent']

class Node(TypedDict):
    nodeId: str
    nodeType: Literal['page', 'slide', 'sheet', 'section', 'region', 'text', 'list', 'table', 'image', 'chart', 'logo', 'caption', 'ocr', 'speaker_notes', 'accessibility_text']
    index: int
    parentNodeId: NotRequired[str]
    readingOrder: NotRequired[int]
    label: NotRequired[str]
    geometry: NotRequired[Geometry]
    textDigest: NotRequired[SaveMaterialRequestSchema13]
    artifactRef: NotRequired[str]
    provenance: NotRequired[dict[str, str]]

class Crop(TypedDict):
    x: float
    y: float
    width: float
    height: float
    unit: Literal['px', 'percent']

class Caption(TypedDict):
    text: str
    origin: Literal['source', 'generated', 'operator']

class Ocr(TypedDict):
    text: str
    engine: str
    confidence: NotRequired[float]

class AltText(TypedDict):
    text: str
    origin: Literal['source', 'generated', 'operator']
AllowedContext: TypeAlias = str

class SaveMaterialRequestSchema20(TypedDict):
    reusePolicy: NotRequired[Literal['allowed', 'requires_approval', 'prohibited', 'unknown']]
    rightsBasis: NotRequired[Literal['owned', 'licensed', 'seller_attestation', 'public_web', 'operator_verified', 'unknown']]
    use: NotRequired[Literal['owned', 'licensed', 'seller_attested', 'unknown']]
    summary: NotRequired[str]
    expiresAt: NotRequired[str]
    allowedContexts: NotRequired[list[AllowedContext]]
SaveMaterialRequestSchema22: TypeAlias = Literal['public', 'seller_private', 'advertiser_confidential']

class SaveMaterialRequestSchema23Item(TypedDict):
    renditionRevision: NotRequired[int]
    renditionRef: NotRequired[str]
    blocksRef: NotRequired[str]
    visualAssetsRef: NotRequired[str]
    diagnosticsRef: NotRequired[str]
    compositionReceiptsRef: NotRequired[str]
    extractor: NotRequired[str]
    extractorVersion: NotRequired[str]
    configurationDigest: NotRequired[SaveMaterialRequestSchema13]
    completeness: NotRequired[dict[str, Literal['complete', 'degraded', 'unsupported', 'failed']]]
SaveMaterialRequestSchema23: TypeAlias = list[SaveMaterialRequestSchema23Item]
SaveMaterialRequestSchema26: TypeAlias = str
SaveMaterialSuccessSchema0: TypeAlias = dict[str, JsonValue]
SaveMaterialSuccessSchema1: TypeAlias = str
SaveMaterialSuccessSchema2: TypeAlias = int
SaveMaterialSuccessSchema3: TypeAlias = list[SaveMaterialSuccessSchema0]

class SaveMaterialSuccessSchema4Item(TypedDict):
    rowIndex: int
    field: str
    reason: str
SaveMaterialSuccessSchema4: TypeAlias = list[SaveMaterialSuccessSchema4Item]

class SaveMaterialSuccessSchema5(TypedDict):
    added: list[str]
    updated: list[str]
    removed: list[str]

class SaveMaterialSuccessSchema6Item(TypedDict):
    rowIndex: int
    productId: str
    sourceFloor: float
    rateCardPrice: float
    message: str
SaveMaterialSuccessSchema6: TypeAlias = list[SaveMaterialSuccessSchema6Item]
SaveMaterialSuccessSchema7: TypeAlias = str | None
SaveMaterialSuccessSchema8: TypeAlias = str | None
SaveMaterialSuccessSchema9: TypeAlias = int
SaveMaterialSuccessSchema10: TypeAlias = int
SaveMaterialSuccessSchema11: TypeAlias = bool
SaveMaterialSuccessSchema12: TypeAlias = bool
SaveWholesaleProductSuccessSchema0: TypeAlias = dict[str, JsonValue]
SavePlaybookRequestSchema53: TypeAlias = str
SavePlaybookSuccessSchema0: TypeAlias = dict[str, JsonValue]
SaveBusinessRulesSuccessSchema0: TypeAlias = dict[str, JsonValue]
SaveAdvertiserInstructionsRequestSchema4: TypeAlias = str
SaveSignalSuccessSchema0: TypeAlias = dict[str, JsonValue]
SaveRfpRequestSchema48: TypeAlias = str
SaveRfpRequestSchema51: TypeAlias = str
SaveRfpRequestSchema71: TypeAlias = list[Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']]
SaveRfpRequestSchema73: TypeAlias = int
SaveRfpRequestSchema74Item: TypeAlias = str
SaveRfpRequestSchema74: TypeAlias = list[SaveRfpRequestSchema74Item]
SaveRfpRequestSchema77: TypeAlias = str
SaveRfpRequestSchema79: TypeAlias = list[SaveRfpRequestSchema77]
SaveRfpRequestSchema82: TypeAlias = list[Literal['brand_lift', 'closed_loop_attribution', 'sales_attribution']]
SaveRfpRequestSchema86: TypeAlias = str
SaveRfpRequestI: TypeAlias = str
SaveRfpRequestP: TypeAlias = str
SaveRfpRequestK: TypeAlias = str
SaveRfpRequestJ: TypeAlias = Union[SaveRfpRequestP, list['SaveRfpRequestJ'], dict[SaveRfpRequestK, 'SaveRfpRequestJ'], float, bool, None]
SaveRfpSuccessSchema0: TypeAlias = str
SaveRfpSuccessSchema1: TypeAlias = str
SaveRfpSuccessSchema2: TypeAlias = bool

class Arguments(TypedDict):
    kind: Literal['rfp_turn']
    id: str

class SaveRfpSuccessSchema3(TypedDict):
    tool: Literal['get']
    arguments: Arguments

class Arguments1(TypedDict):
    kind: Literal['rfp']
    id: str

class SaveRfpSuccessSchema4(TypedDict):
    tool: Literal['get']
    arguments: Arguments1

class SaveBuyerOperatorSuccessUpdateBuyerOperatorBody(TypedDict):
    operatorDomain: str
    operatorScope: NotRequired[Literal['whole_operator', 'specific_unit']]
    operatorUnitId: NotRequired[str]
SaveBuyerAgentRequestSchema0: TypeAlias = str
SaveBuyerAgentRequestSchema2: TypeAlias = str
SaveBuyerAgentRequestSchema4: TypeAlias = str

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
    eventType: Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']
    customEventName: NotRequired[str]
    valueField: NotRequired[str]
    valueFactor: NotRequired[float]

class Target(TypedDict):
    kind: Literal['per_ad_spend']
    value: float

class Target1(TypedDict):
    kind: Literal['maximize_value']

class SaveCampaignRequestSchema54(TypedDict):
    kind: Literal['cost_per']
    value: float

class SaveCampaignRequestDuration(TypedDict):
    interval: int
    unit: Literal['minutes', 'hours', 'days', 'campaign']

class Target2(TypedDict):
    kind: Literal['threshold_rate']
    value: float
SaveCampaignRequestSchema82: TypeAlias = str
SaveCampaignRequestSchema195: TypeAlias = Literal['required', 'preferred']
SaveCampaignRequestSchema197: TypeAlias = str
SaveCampaignRequestSchema202: TypeAlias = str
SaveCampaignRequestSchema245: TypeAlias = str
SaveCampaignRequestSchema247: TypeAlias = str

class SaveCampaignRequestCampaignTargetingOverlayShared111(TypedDict):
    country: NotRequired[Literal['US']]
    system: NotRequired[Literal['zip', 'zip_plus_four']]

class SaveCampaignRequestCampaignTargetingOverlayShared112(TypedDict):
    country: NotRequired[Literal['GB']]
    system: NotRequired[Literal['outward', 'full']]

class SaveCampaignRequestCampaignTargetingOverlayShared113(TypedDict):
    country: NotRequired[Literal['CA']]
    system: NotRequired[Literal['fsa', 'full']]

class SaveCampaignRequestCampaignTargetingOverlayShared114(TypedDict):
    country: NotRequired[Literal['DE', 'CH', 'AT']]
    system: NotRequired[Literal['plz']]

class SaveCampaignRequestCampaignTargetingOverlayShared115(TypedDict):
    country: NotRequired[Literal['FR']]
    system: NotRequired[Literal['code_postal']]

class SaveCampaignRequestCampaignTargetingOverlayShared116(TypedDict):
    country: NotRequired[Literal['AU']]
    system: NotRequired[Literal['postcode']]

class SaveCampaignRequestCampaignTargetingOverlayShared117(TypedDict):
    country: NotRequired[Literal['BR']]
    system: NotRequired[Literal['cep']]

class SaveCampaignRequestCampaignTargetingOverlayShared118(TypedDict):
    country: NotRequired[Literal['IN']]
    system: NotRequired[Literal['pin']]

class SaveCampaignRequestCampaignTargetingOverlayShared119(TypedDict):
    country: NotRequired[Literal['ZA']]
    system: NotRequired[Literal['postal_code']]

class SaveCampaignRequestCampaignTargetingOverlayShared1110(TypedDict):
    country: NotRequired[JsonValue]
    system: NotRequired[Literal['postal_code', 'custom']]

class SaveCampaignRequestCampaignTargetingOverlayShared1111(TypedDict):
    country: str
    system: Literal['postal_code', 'zip', 'zip_plus_four', 'outward', 'full', 'fsa', 'plz', 'code_postal', 'postcode', 'cep', 'pin', 'custom', 'us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

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
    values: list[str]
SaveCampaignRequestCampaignTargetingOverlayShared1: TypeAlias = list[SaveCampaignRequestCampaignTargetingOverlayShared11 | SaveCampaignRequestCampaignTargetingOverlayShared12]
Value: TypeAlias = str

class SaveCampaignRequestCampaignTargetingOverlayShared2Item1(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]

class SaveCampaignRequestCampaignTargetingOverlayShared2Item2(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

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

class SaveCampaignRequestCampaignTargetingOverlayShared3Item(TypedDict):
    system: Literal['nielsen_dma', 'uk_itl1', 'uk_itl2', 'eurostat_nuts2', 'custom']
    values: list[str]
SaveCampaignRequestCampaignTargetingOverlayShared3: TypeAlias = list[SaveCampaignRequestCampaignTargetingOverlayShared3Item]
SaveCampaignRequestCampaignTargetingOverlayShared4: TypeAlias = list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]
SaveCampaignRequestCampaignTargetingOverlayShared5: TypeAlias = list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]
SaveCampaignRequestCampaignTargetingOverlayShared6: TypeAlias = list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]

class SaveCampaignSuccessSchema2(TypedDict):
    totalMediaBuys: int
    updatedCount: int
    failedCount: int
    skippedCount: int

class SaveCampaignSuccessSchema4(TypedDict):
    total: float
    currency: str
SaveEventSourceRequestEventSourceActionSource: TypeAlias = Literal['website', 'app', 'offline', 'phone_call', 'chat', 'email', 'in_store', 'system_generated', 'other']

class SaveEventSourceRequestEventSourceSurface(TypedDict):
    category: Literal['owned_property', 'website', 'app', 'offline', 'phone_call', 'chat', 'email', 'in_store', 'system_generated', 'other']
    property_type: NotRequired[str]
    namespace: NotRequired[str]
    property_id: NotRequired[str]
SaveDimensionRequestSchema1: TypeAlias = str
SaveDimensionRequestSchema2: TypeAlias = Literal['open', 'governed']
SaveDimensionRequestSchema3: TypeAlias = list[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
SaveDimensionRequestSchema6: TypeAlias = bool

class SaveDimensionRequestSchema8Item(TypedDict):
    value: str
    name: NotRequired[str]
    retired: NotRequired[bool]
    mergeInto: NotRequired[str]
SaveDimensionRequestSchema8: TypeAlias = list[SaveDimensionRequestSchema8Item]
SaveDimensionRequestSchema13: TypeAlias = str

class SavePropertyListRequestPropertyListIdentifier(TypedDict):
    type: Literal['domain', 'subdomain', 'network_id', 'ios_bundle', 'android_package', 'apple_app_store_id', 'google_play_id', 'roku_store_id', 'fire_tv_asin', 'samsung_app_id', 'apple_tv_bundle', 'bundle_id', 'venue_id', 'screen_id', 'openooh_venue_type', 'rss_url', 'apple_podcast_id', 'spotify_collection_id', 'podcast_guid', 'station_id', 'facility_id']
    value: str

class FeatureRequirement(TypedDict):
    feature_id: str
    min_value: NotRequired[float | None]
    max_value: NotRequired[float | None]
    allowed_values: NotRequired[list[JsonValue] | None]
    if_not_covered: NotRequired[Literal['exclude', 'include'] | None]

class SavePropertyListRequestPropertyListFilters(TypedDict):
    channels_any: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement']] | None]
    countries_all: NotRequired[list[str] | None]
    property_types: NotRequired[list[Literal['website', 'mobile_app', 'ctv_app', 'desktop_app', 'dooh', 'podcast', 'radio', 'streaming_audio']] | None]
    feature_requirements: NotRequired[list[FeatureRequirement] | None]

class SavePropertyListSuccessPropertyListFilters(TypedDict):
    channels_any: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement']] | None]
    countries_all: NotRequired[list[str] | None]
    property_types: NotRequired[list[Literal['website', 'mobile_app', 'ctv_app', 'desktop_app', 'dooh', 'podcast', 'radio', 'streaming_audio']] | None]
    feature_requirements: NotRequired[list[FeatureRequirement] | None]

class SavePropertyListSuccessPropertyListResolutionSummary(TypedDict):
    totalRequested: int
    resolvedCount: int
    registeredCount: int
    unresolvedCount: int
    resolutionRate: float

class SavePropertyListSuccessPropertyListCascadeSummary(TypedDict):
    totalMediaBuys: int
    updatedCount: int
    failedCount: int
SaveCreativeRequestSchema33: TypeAlias = str
SaveCreativeRequestSchema49: TypeAlias = str
SaveCreativeRequestSchema51: TypeAlias = str
SaveCreativeRequestSchema53: TypeAlias = bool

class Dimensions(TypedDict):
    width: NotRequired[int]
    height: NotRequired[int]
    duration_seconds: NotRequired[float]

class RenderCrop(TypedDict):
    x: float
    y: float
    width: float
    height: float
    units: NotRequired[Literal['normalized']]
    source: NotRequired[Literal['user', 'system', 'dam', 'product_catalog']]
    notes: NotRequired[str]
SaveCreativeSessionRequestSchema17: TypeAlias = Literal['upload', 'url', 'dam', 'product_catalog', 'brand_library', 'local', 'generated']
SaveCreativeSessionRequestSchema18: TypeAlias = Literal['product', 'logo', 'background', 'reference', 'copy', 'audio', 'video']
SaveCreativeSessionRequestSchema25: TypeAlias = str
SaveCreativeSessionRequestSchema27: TypeAlias = str
SaveCreativeSessionRequestSchema29: TypeAlias = str
SaveCreativeSessionSuccessSchema0: TypeAlias = dict[str, JsonValue]
SaveCreativeSessionSuccessSchema1: TypeAlias = Literal[True]
SaveCreativeSessionSuccessSchema2: TypeAlias = dict[str, int]
SaveCreativeSessionSuccessSchema3: TypeAlias = int
SaveCreativeSessionSuccessSchema4: TypeAlias = str

class Arguments2(TypedDict):
    campaignId: str
    sessionId: str
    actionKey: str
    expectedRevision: int
    sessionGeneration: str

class SaveCreativeSessionSuccessSchema5(TypedDict):
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

class SaveCreativeSessionSuccessSchema6(TypedDict):
    campaignId: str
    sessionId: str
    revision: int
    sessionGeneration: NotRequired[str]
    variants: list[Variant]
    selectedVariantId: NotRequired[str]
    approvedVariantId: NotRequired[str]
    approvedSessionRevision: NotRequired[int]
    finalCreativeId: NotRequired[str]
    generationPending: bool
    terminal: NotRequired[Terminal]
GenerateVariantsRequestSchema0: TypeAlias = str
GenerateVariantsRequestSchema1: TypeAlias = str
GenerateVariantsRequestSchema2: TypeAlias = str
GenerateVariantsRequestSchema3: TypeAlias = int
GenerateVariantsRequestSchema4: TypeAlias = str

class SaveMediaBuyRequestSchema581(TypedDict):
    scope: Literal['product']
    signal_id: str

class SaveMediaBuyRequestSchema582(TypedDict):
    scope: Literal['data_provider']
    data_provider_domain: str
    signal_id: str

class SaveMediaBuyRequestSchema583(TypedDict):
    scope: Literal['signal_source']
    signal_source_url: str
    signal_id: str
SaveMediaBuyRequestSchema58: TypeAlias = SaveMediaBuyRequestSchema581 | SaveMediaBuyRequestSchema582 | SaveMediaBuyRequestSchema583

class SaveMediaBuyRequestSchema111(TypedDict):
    interval: int
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']
SaveMediaBuyRequestSchema115: TypeAlias = float

class SaveMediaBuyRequestSchema118(TypedDict):
    kind: Literal['cost_per']
    value: SaveMediaBuyRequestSchema115
    strength: NotRequired[Literal['cap', 'target']]

class SaveMediaBuyRequestSchema120(TypedDict):
    kind: Literal['threshold_rate']
    value: SaveMediaBuyRequestSchema115
SaveMediaBuyRequestSchema122: TypeAlias = int
SaveMediaBuySuccessSchema0: TypeAlias = Literal['storefront', 'salesagent', 'unknown']
SaveMediaBuySuccessSchema1: TypeAlias = Literal['draft', 'pendingApproval', 'inputRequired', 'active', 'completed', 'canceled', 'failed', 'rejected']
SaveMediaBuySuccessSchema3: TypeAlias = Literal['guaranteed', 'best_effort', 'report_only']

class SaveMediaBuySuccessSchema51(TypedDict):
    kind: Literal['cost_per']
    value: float

class SaveMediaBuySuccessSchema52(TypedDict):
    kind: Literal['threshold_rate']
    value: float

class SaveMediaBuySuccessSchema53(TypedDict):
    kind: Literal['per_ad_spend']
    value: float

class SaveMediaBuySuccessSchema54(TypedDict):
    kind: Literal['maximize_value']
SaveMediaBuySuccessSchema5: TypeAlias = SaveMediaBuySuccessSchema51 | SaveMediaBuySuccessSchema52 | SaveMediaBuySuccessSchema53 | SaveMediaBuySuccessSchema54

class Window(TypedDict):
    interval: int
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']

class SaveMediaBuySuccessSchema14(TypedDict):
    maxImpressions: int
    per: Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']
    window: Window

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
    asOf: NotRequired[str]

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

class Revision1(TypedDict):
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
    revision: Revision1
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

class Blocker(TypedDict):
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
    blockers: list[Blocker]
    nextActions: list[NextAction]
    reachableAccounts: list[ReachableAccount]
    reachableAccountsTruncated: NotRequired[bool]
GetStatusError: TypeAlias = V3ToolErrorResponse

class RefreshInventorySourceHealthInput(TypedDict):
    sourceId: str

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
    company: NotRequired[str]

class SaveAccountInput(TypedDict):
    accountId: int
    name: NotRequired[str]
    settings: NotRequired[Settings]

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

class SaveAskInput1(TypedDict):
    id: str
    requesterState: Literal['confirmed_resolved', 'accepted', 'still_blocked', 'withdrawn']
    note: NotRequired[str]

class SaveAskInput2(TypedDict):
    type: Literal['support']
    title: str
    detail: str
    blocks: NotRequired[str]
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]

class SaveAskInput3(TypedDict):
    type: Literal['product']
    title: str
    detail: NotRequired[str]
    blocks: NotRequired[str]
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]

class SaveAskInput4(TypedDict):
    type: Literal['commercial']
    title: str
    detail: NotRequired[str]
    blocks: NotRequired[str]
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]

class SaveAskInput5(TypedDict):
    type: Literal['integration']
    title: str
    detail: NotRequired[str]
    blocks: NotRequired[str]
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    subject: str

class SaveAskInput6(TypedDict):
    type: Literal['supply']
    title: str
    detail: NotRequired[str]
    blocks: NotRequired[str]
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    subject: str
    channel: str
    desiredSupply: NotRequired[str]

class SaveAskInput7(TypedDict):
    title: str
    detail: NotRequired[str]
    blocks: NotRequired[str]
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    subject: NotRequired[str]
    desiredSupply: NotRequired[str]

class SaveAskInput8(TypedDict):
    title: str
    detail: NotRequired[str]
    blocks: NotRequired[str]
    severity: NotRequired[Literal['low', 'medium', 'high', 'urgent']]
    subject: str
    channel: str
    desiredSupply: NotRequired[str]
SaveAskInput: TypeAlias = SaveAskInput1 | SaveAskInput2 | SaveAskInput3 | SaveAskInput4 | SaveAskInput5 | SaveAskInput6 | SaveAskInput7 | SaveAskInput8

class SaveAskResult1(TypedDict):
    askId: NotRequired[SaveAskSuccessSchema0]
    type: Literal['support', 'commercial']
    filed: Literal[True]
    escalationUid: str

class SaveAskResult2(TypedDict):
    askId: NotRequired[SaveAskSuccessSchema0]
    type: Literal['support', 'commercial']
    filed: Literal[False]
    warning: Literal['suppressed in test mode']

class SaveAskResult3(TypedDict):
    askId: NotRequired[SaveAskSuccessSchema0]
    type: Literal['product']
    filed: bool
    created: bool
    state: str

class SaveAskResult4(TypedDict):
    askId: NotRequired[SaveAskSuccessSchema0]
    type: Literal['supply']
    filed: Literal[True]
    created: bool
    registryStatus: Literal['found', 'missing', 'unavailable']

class SaveAskResult5(TypedDict):
    askId: NotRequired[SaveAskSuccessSchema0]
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
    version: str

class SaveBillingInput1(TypedDict):
    terms: Terms

class PaymentAuthority(TypedDict):
    method: NotRequired[SaveBillingRequestSchema1]
    action: NotRequired[Literal['request']]

class PaymentAuthority1(TypedDict):
    method: NotRequired[SaveBillingRequestSchema1]
    action: Literal['confirm']
    confirmationToken: str

class PaymentAuthority2(TypedDict):
    method: NotRequired[SaveBillingRequestSchema1]
    action: Literal['status']

class SaveBillingInput2(TypedDict):
    paymentAuthority: PaymentAuthority | PaymentAuthority1 | PaymentAuthority2
SaveBillingInput: TypeAlias = SaveBillingInput1 | SaveBillingInput2

class SaveBillingResult1(TypedDict):
    action: Literal['terms_accepted']
    terms: Terms

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
    kind: Literal['iu_allowance']
    allowance: Literal['trial_free_grant', 'plan_included']

class Content(TypedDict):
    type: Literal['usage.allowance_threshold']
    presentation: Literal['alert']

class Trigger(TypedDict):
    type: Literal['schedule']
    schedule: str
    timezone: str

class Predicate(TypedDict):
    metric: Literal['iu.percent_consumed']
    op: Literal['>=']
    value: float

class Trigger1(TypedDict):
    type: Literal['condition']
    predicate: Predicate

class SaveNotificationConfigInput(TypedDict):
    subscriptionId: NotRequired[str]
    enabled: NotRequired[bool]
    scope: NotRequired[Scope]
    content: NotRequired[Content]
    trigger: NotRequired[Trigger | Trigger1]
    routeIds: NotRequired[list[Literal['email', 'slack', 'webhook']]]

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
    grantRef: NotRequired[str]
    granteeOrganizationRef: NotRequired[str]
    advertiserIds: NotRequired[list[AdvertiserId]]
    capabilities: NotRequired[list[Literal['advertiser.read', 'campaign.read', 'campaign.manage']]]
    expiresAt: NotRequired[str]
    reason: str

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
    grantor: SaveAdvertiserGrantSuccessSchema0
    grantee: SaveAdvertiserGrantSuccessSchema0
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
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: NotRequired[str]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput1(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['agent', 'skill', 'inventory_source', 'material', 'coverage', 'wholesale_product', 'playbook_version', 'business_rules_version', 'house_discount', 'connection', 'account_relationship', 'seller', 'advertiser', 'advertiser_grant', 'signal', 'work_item', 'campaign', 'creative_format', 'creative_engine', 'media_buy', 'rfp', 'rfp_turn', 'library_request', 'ask', 'conversation', 'buyer_agent', 'dimension', 'session']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: NotRequired[Filter]
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter1(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: str
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: NotRequired[str]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput2(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['creative_asset', 'catalog']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: Filter1
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter2(TypedDict):
    advertiserId: str

class SearchInput3(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['measurement_source', 'event_source']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: Filter2
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter3(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: str
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput4(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['proposal']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: Filter3
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter4(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: str
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput5(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['creative']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: Filter4
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter5(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: str
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput6(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['creative']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: Filter5
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter6(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: str
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput7(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['creative_collection']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: Filter6
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter7(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: str
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput8(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['creative_collection']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: Filter7
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter8(TypedDict):
    campaignId: str
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]

class SearchInput9(TypedDict):
    query: NotRequired[JsonValue]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['creative_session']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[JsonValue]
    filter: Filter8
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter9(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: NotRequired[str]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput10(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    kind: Literal['ad_server_targeting']
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: str
    filter: NotRequired[Filter9]
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter10(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: NotRequired[str]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput11(TypedDict):
    query: str
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: NotRequired[Filter10]
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter11(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: NotRequired[str]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput12(TypedDict):
    query: NotRequired[str]
    document: str
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: NotRequired[Filter11]
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter12(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: NotRequired[str]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput13(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: str
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: NotRequired[Filter12]
    cursor: NotRequired[str]
    limit: NotRequired[int]

class Filter13(TypedDict):
    targetKind: NotRequired[Literal['seller', 'creative_engine']]
    ids: NotRequired[list[Id]]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED', 'pending', 'approved', 'rejected', 'revoked', 'OPEN', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'CANCELLED', 'ARCHIVED', 'ALL', 'open', 'closed', 'drafting', 'refining', 'evaluating', 'finalized']]
    originRfpTurnId: NotRequired[str]
    authorization: NotRequired[str]
    productStatus: NotRequired[Literal['draft', 'active', 'archived']]
    askType: NotRequired[Literal['support', 'product', 'supply', 'integration', 'commercial']]
    askState: NotRequired[Literal['open', 'closed']]
    candidateType: NotRequired[str]
    parentId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    buyerDomain: NotRequired[str]
    campaignStatus: NotRequired[list[Literal['needs_attention', 'active', 'draft', 'completed', 'paused', 'canceled', 'archived']]]
    campaignMode: NotRequired[Literal['managed', 'tracked']]
    campaignName: NotRequired[str]
    advertiserId: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    propertyListPurpose: NotRequired[Literal['include', 'exclude']]
    phase: NotRequired[list[Literal['draft', 'active', 'completed', 'canceled', 'pendingApproval', 'inputRequired', 'failed', 'rejected']]]
    handling: NotRequired[list[Literal['tracking', 'managing']]]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    sort: NotRequired[Literal['updatedDesc', 'flightStart', 'name', 'spendDesc']]
    campaignId: NotRequired[str]
    formatKind: NotRequired[str]
    productId: NotRequired[str]
    assetType: NotRequired[Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'JAVASCRIPT', 'CSS', 'TEXT', 'URL', 'VAST', 'ZIP', 'FONT', 'LOGO', 'DOCUMENT']]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, Literal['unlabeled'] | list[Label]]]
    appliesTo: NotRequired[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    role: NotRequired[SearchRequestCreativeRole]
    source: NotRequired[SearchRequestCreativeSource]
    promoted: NotRequired[bool]
    state: NotRequired[list[Literal['quoted', 'bound', 'expired', 'withdrawn', 'open', 'released', 'closed']]]
    sellerId: NotRequired[str]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']] | Literal['live', 'draft', 'evaluation']]
    lifecycle: NotRequired[Literal['active', 'closed', 'archived']]
    live: NotRequired[bool]
    attention: NotRequired[Literal['approval_needed']]
    operatorDomain: NotRequired[str]
    actorKind: NotRequired[Literal['human', 'agent']]
    advertiserIds: NotRequired[list[AdvertiserId]]
    buyerAccountIds: NotRequired[list[BuyerAccountId]]
    transport: NotRequired[Literal['chat', 'mcp', 'adcp', 'email', 'slack', 'sms', 'discord', 'fax']]
    updatedAfter: NotRequired[str]
    sessionSource: NotRequired[Literal['murph_conversation_v1', 'storefront_rfp_v1', 'storefront_media_buy_v1']]
    buyer: NotRequired[list[str]]
    advertiser: NotRequired[list[str]]
    category: NotRequired[list[str]]
    market: NotRequired[list[str]]
    channel: NotRequired[list[ChannelItem]]
    selectedPosture: NotRequired[list[str]]
    playbookVersion: NotRequired[list[int]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    outcome: NotRequired[list[str]]
    rfpId: NotRequired[str]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[str]]
    responseRecipeVersion: NotRequired[list[str]]
    modelVersion: NotRequired[list[str]]
    judgeVersion: NotRequired[list[str]]
    feedbackStatus: NotRequired[list[Literal['unreviewed', 'reviewed']]]
    sellerStatus: NotRequired[Literal['pending_approval', 'forwarding', 'forward_failed', 'awaiting_source', 'rejected', 'canceled', 'booked', 'delivering', 'paused', 'completed']]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    sandbox: NotRequired[bool]
    linkedAccountPartnerId: NotRequired[str]
    grantStatus: NotRequired[list[Literal['invited', 'active', 'expired', 'rejected', 'revoked']]]
    flightStartFrom: NotRequired[str]
    flightStartTo: NotRequired[str]
    classification: NotRequired[Literal['global_market_maker', 'regional_market_maker', 'marketplace_seller']]
    marketplaceReady: NotRequired[bool]
    marketplace: NotRequired[bool]
    region: NotRequired[str]
    processingState: NotRequired[list[Literal['needs_upload', 'queued', 'processing', 'ready', 'partial', 'failed']]]
    materialKind: NotRequired[Literal['document', 'response']]
    sourceKind: NotRequired[list[Literal['url', 'site', 'upload', 'crawl_manifest', 'inline', 'history']]]
    visibility: NotRequired[list[Literal['public', 'seller_private', 'advertiser_confidential']]]
    sourceExtension: NotRequired[str]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet', 'uncategorized']]
    vertical: NotRequired[list[VerticalItem]]
    effectiveOn: NotRequired[str]
    expiresAfter: NotRequired[str]
    hasUnits: NotRequired[bool]
    archived: NotRequired[Literal['active', 'archived']]
    conversationStartedAfter: NotRequired[str]
    conversationStartedBefore: NotRequired[str]

class SearchInput14(TypedDict):
    query: NotRequired[str]
    document: NotRequired[str]
    revision: NotRequired[str]
    section: NotRequired[str]
    asOf: NotRequired[str]
    sources: NotRequired[list[Literal['objects', 'docs', 'specs']]]
    docsScope: NotRequired[Literal['caller_relevant', 'public_research']]
    sponsoredBuyerCustomerId: NotRequired[str]
    scope: NotRequired[Literal['unit']]
    include: NotRequired[list[Literal['evidence_matches', 'browse']]]
    sourceId: NotRequired[str]
    filter: NotRequired[Filter13]
    cursor: NotRequired[str]
    limit: NotRequired[int]
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
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items(TypedDict):
    filter: NotRequired[Filter14]
    cursor: NotRequired[str]

class Pages(TypedDict):
    candidates: NotRequired[GetRequestSchema51]
    rendition_blocks: NotRequired[GetRequestSchema51]
    visual_assets: NotRequired[GetRequestSchema51]
    extraction_diagnostics: NotRequired[GetRequestSchema51]
    composition_receipts: NotRequired[GetRequestSchema51]
    usage: NotRequired[GetRequestSchema51]

class Select(TypedDict):
    blockKinds: NotRequired[list[Literal['heading', 'paragraph', 'list', 'table', 'caption', 'speaker_notes', 'ocr', 'accessibility_text', 'other']]]
    unitId: NotRequired[str]
    assetKinds: NotRequired[list[Literal['photo', 'illustration', 'logo', 'chart', 'diagram', 'screenshot', 'background', 'other']]]
    reusePolicies: NotRequired[list[Literal['allowed', 'requires_approval', 'prohibited', 'unknown']]]
    assetStatuses: NotRequired[list[Literal['ready', 'degraded', 'failed']]]

class Options(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class ConnectionTarget(TypedDict):
    kind: Literal['seller', 'creative_engine']
    id: str

class GetInput1(TypedDict):
    kind: Literal['agent', 'buyer_agent', 'skill', 'inventory_source', 'advertiser', 'advertiser_grant', 'signal', 'ask', 'conversation', 'campaign', 'dimension', 'creative_asset', 'media_buy', 'rfp', 'rfp_turn', 'library_request', 'account_relationship']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items]
    options: NotRequired[Options]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter15(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items1(TypedDict):
    filter: NotRequired[Filter15]
    cursor: NotRequired[str]

class Options1(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput2(TypedDict):
    kind: Literal['seller']
    id: NotRequired[str]
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items1]
    options: NotRequired[Options1]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter16(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items2(TypedDict):
    filter: NotRequired[Filter16]
    cursor: NotRequired[str]

class Options2(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput3(TypedDict):
    kind: Literal['listing', 'media_kit', 'playbook', 'business_rules', 'coverage', 'distribution', 'notification_config']
    id: NotRequired[JsonValue]
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items2]
    options: NotRequired[Options2]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter17(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items3(TypedDict):
    filter: NotRequired[Filter17]
    cursor: NotRequired[str]

class Options3(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput4(TypedDict):
    kind: Literal['audience']
    id: NotRequired[JsonValue]
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: str
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items3]
    options: NotRequired[Options3]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter18(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items4(TypedDict):
    filter: NotRequired[Filter18]
    cursor: NotRequired[str]

class Options4(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput5(TypedDict):
    kind: Literal['catalog', 'measurement_source', 'event_source']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: str
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items4]
    options: NotRequired[Options4]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter19(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items5(TypedDict):
    filter: NotRequired[Filter19]
    cursor: NotRequired[str]

class Options5(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput6(TypedDict):
    kind: Literal['creative_format']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: str
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[JsonValue]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[JsonValue]
    items: NotRequired[Items5]
    options: NotRequired[Options5]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter20(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items6(TypedDict):
    filter: NotRequired[Filter20]
    cursor: NotRequired[str]

class Options6(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput7(TypedDict):
    kind: Literal['creative', 'creative_collection']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[JsonValue]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: str
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items6]
    options: NotRequired[Options6]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter21(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items7(TypedDict):
    filter: NotRequired[Filter21]
    cursor: NotRequired[str]

class Options7(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput8(TypedDict):
    kind: Literal['creative', 'creative_collection']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: str
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[JsonValue]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items7]
    options: NotRequired[Options7]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter22(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items8(TypedDict):
    filter: NotRequired[Filter22]
    cursor: NotRequired[str]

class Options8(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput9(TypedDict):
    kind: Literal['creative_engine']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[JsonValue]
    items: NotRequired[Items8]
    options: NotRequired[Options8]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter23(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items9(TypedDict):
    filter: NotRequired[Filter23]
    cursor: NotRequired[str]

class Options9(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput10(TypedDict):
    kind: Literal['creative_session']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: str
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[JsonValue]
    items: NotRequired[Items9]
    options: NotRequired[Options9]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter24(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items10(TypedDict):
    filter: NotRequired[Filter24]
    cursor: NotRequired[str]

class Options10(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput11(TypedDict):
    kind: Literal['wholesale_product']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: str
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items10]
    options: NotRequired[Options10]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter25(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items11(TypedDict):
    filter: NotRequired[Filter25]
    cursor: NotRequired[str]

class Options11(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput12(TypedDict):
    kind: Literal['material']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items11]
    options: NotRequired[Options11]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter26(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items12(TypedDict):
    filter: NotRequired[Filter26]
    cursor: NotRequired[str]

class Options12(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput13(TypedDict):
    kind: Literal['proposal']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items12]
    options: NotRequired[Options12]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter27(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items13(TypedDict):
    filter: NotRequired[Filter27]
    cursor: NotRequired[str]

class Options13(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput14(TypedDict):
    kind: Literal['connection']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items13]
    options: NotRequired[Options13]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter28(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items14(TypedDict):
    filter: NotRequired[Filter28]
    cursor: NotRequired[str]

class Options14(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput15(TypedDict):
    kind: Literal['session']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: NotRequired[Literal['creative_review', 'media_buy_approval', 'modular_source']]
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items14]
    options: NotRequired[Options14]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]

class Filter29(TypedDict):
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    status: NotRequired[Literal['approved']]

class Items15(TypedDict):
    filter: NotRequired[Filter29]
    cursor: NotRequired[str]

class Options15(TypedDict):
    sourceRevision: NotRequired[int]
    renditionRevision: NotRequired[int]
    pages: NotRequired[Pages]
    select: NotRequired[Select]

class GetInput16(TypedDict):
    kind: Literal['work_item']
    id: str
    after: NotRequired[str]
    through: NotRequired[str]
    limit: NotRequired[int]
    buyerCustomerId: NotRequired[int]
    accountId: NotRequired[int]
    advertiserId: NotRequired[str]
    reportId: NotRequired[str]
    identifierOffset: NotRequired[int]
    identifierCategory: NotRequired[Literal['all', 'unresolved', 'registered']]
    productQueryId: NotRequired[str]
    productRevision: NotRequired[int]
    validationRunId: NotRequired[str]
    sourceId: NotRequired[str]
    workItemKind: Literal['creative_review', 'media_buy_approval', 'modular_source']
    include: NotRequired[list[Literal['diagnostics', 'adServerConnection', 'adServerStatus', 'syncHistory', 'sandboxAccount', 'modularReadiness', 'mappingWorkspace', 'mediaBuys', 'proposals', 'creatives', 'recentActivity', 'deliverySummary', 'sourceIdentity', 'tracking', 'propertyLists', 'versions', 'discounts', 'approvalRouting', 'listing', 'identity', 'discoveryCard', 'brief', 'products', 'evaluation', 'certification', 'validationRuns', 'liveStatus', 'accounts', 'preview', 'items', 'report', 'source_access', 'rendition_blocks', 'visual_assets', 'extraction_diagnostics', 'composition_receipts', 'repeats', 'usage']]]
    items: NotRequired[Items15]
    options: NotRequired[Options15]
    version: NotRequired[int]
    subscriptionsOffset: NotRequired[int]
    connectionAccountsOffset: NotRequired[int]
    connectionMappingsOffset: NotRequired[int]
    connectionTarget: NotRequired[ConnectionTarget]
    feedbackOffset: NotRequired[int]
    representationOffset: NotRequired[int]
    representationCursor: NotRequired[str]
    audienceOffset: NotRequired[int]
    proposalProductsCursor: NotRequired[str]
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
    expiresAt: str

class Submission(TypedDict):
    status: Literal['processing', 'verified', 'failed', 'expired']
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
    docsUrl: str | None
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
    kind: Literal['seller', 'creative_engine']
    id: str

class Authorization(TypedDict):
    mode: NotRequired[Literal['oauth', 'bearer']]

class Selection1(TypedDict):
    decision: SaveConnectionRequestBuyerStorefrontSelectionDecision

class AdvertiserActivation(TypedDict):
    advertiserId: SaveConnectionRequestSchema3
    decision: SaveConnectionRequestBuyerAdvertiserStorefrontActivationPreferenceDecision

class Billing(TypedDict):
    requestedParty: Literal['agent', 'operator']

class Billing1(TypedDict):
    directBillingAccepted: Literal[True]

class FeaturePolicy(TypedDict):
    buyEnabled: NotRequired[bool]
    eventsEnabled: NotRequired[bool]
    feedsEnabled: NotRequired[bool]

class EnhancedReporting(TypedDict):
    accountId: SaveConnectionRequestSchema3
    enabled: bool

class AdvertiserMapping(TypedDict):
    accountId: NotRequired[SaveConnectionRequestSchema3]
    advertiserId: SaveConnectionRequestSchema3
    state: Literal['mapped', 'unmapped']
    sourceId: NotRequired[str]
    linkId: NotRequired[SaveConnectionRequestSchema3]

class SaveConnectionInput(TypedDict):
    target: NotRequired[Target3]
    sellerId: NotRequired[str]
    connectionId: NotRequired[str]
    authorization: NotRequired[Authorization]
    selection: NotRequired[Selection1]
    advertiserActivation: NotRequired[AdvertiserActivation]
    billing: NotRequired[Billing | Billing1]
    featurePolicy: NotRequired[FeaturePolicy]
    enhancedReporting: NotRequired[EnhancedReporting]
    refreshAccounts: NotRequired[Literal[True]]
    selectedAccountId: NotRequired[str]
    advertiserMapping: NotRequired[AdvertiserMapping]
    state: NotRequired[Literal['removed']]

class Authorization1(TypedDict):
    url: str
    mode: Literal['oauth', 'bearer']
    connectionId: str | None

class SaveConnectionResult1(TypedDict):
    action: Literal['authorization_required']
    object: SaveConnectionSuccessSchema0
    mutationReceipt: NotRequired[SaveConnectionSuccessSchema1]
    authorization: Authorization1

class SaveConnectionResult2(TypedDict):
    action: Literal['selection_updated', 'advertiser_activation_updated', 'billing_updated', 'direct_billing_accepted', 'feature_policy_updated', 'enhanced_reporting_updated', 'accounts_refreshed', 'account_selected', 'advertiser_mapped', 'advertiser_unmapped', 'removed']
    object: SaveConnectionSuccessSchema0
    mutationReceipt: NotRequired[SaveConnectionSuccessSchema1]
SaveConnectionResult: TypeAlias = SaveConnectionResult1 | SaveConnectionResult2
SaveConnectionError: TypeAlias = V3ToolErrorResponse

class SaveLibraryRequestInput1(TypedDict):
    action: Literal['open']
    gap: str
    originRfpTurnId: NotRequired[str]

class SaveLibraryRequestInput2(TypedDict):
    action: Literal['close']
    id: str
    closedBy: Literal['upload', 'dictation']
    materialId: str
SaveLibraryRequestInput: TypeAlias = SaveLibraryRequestInput1 | SaveLibraryRequestInput2

class Request(TypedDict):
    id: SaveLibraryRequestSuccessSchema0
    gap: SaveLibraryRequestSuccessSchema1
    openedAt: SaveLibraryRequestSuccessSchema2
    originRfpTurnId: SaveLibraryRequestSuccessSchema3
    status: Literal['open']
    closedBy: None
    closingMaterialId: None
    closedAt: None

class SaveLibraryRequestResult1(TypedDict):
    request: Request
    idempotent: bool

class SaveLibraryRequestResult2(TypedDict):
    id: SaveLibraryRequestSuccessSchema0
    gap: SaveLibraryRequestSuccessSchema1
    openedAt: SaveLibraryRequestSuccessSchema2
    originRfpTurnId: SaveLibraryRequestSuccessSchema3
    status: Literal['closed']
    closedBy: Literal['upload', 'dictation']
    closingMaterialId: str
    closedAt: str
SaveLibraryRequestResult: TypeAlias = SaveLibraryRequestResult1 | SaveLibraryRequestResult2
SaveLibraryRequestError: TypeAlias = V3ToolErrorResponse

class OpenPageInput(TypedDict):
    relationshipId: NotRequired[str]
    blockedReason: NotRequired[str]
    page: Literal['connect_ad_server', 'ad_server_source', 'ad_server_diagnostics', 'source_diagnostics', 'seller_setup', 'demo_seller', 'modular_inventory_source', 'modular_source_setup', 'modular_inventory_feed', 'listing', 'discovery_card', 'media_kit', 'business_profile', 'playbook', 'library', 'product_marketing', 'business_rules', 'buyer_account_mapping', 'property_roster', 'plan_and_billing', 'sellers', 'creative_engines', 'advertisers', 'campaigns', 'campaign_receipt', 'approvals', 'release_notes', 'customer_requests', 'notifications']
    sourceId: NotRequired[str]
    sourceName: NotRequired[str]
    esaId: NotRequired[str]

class OpenPageResult(TypedDict):
    success: NotRequired[Literal[True]]
    code: NotRequired[JsonValue]
OpenPageError: TypeAlias = V3ToolErrorResponse

class OpenProposalPassInput(TypedDict):
    rfpId: str
    turnId: str

class Params(TypedDict):
    rfpId: str
    turnId: str

class OpenProposalPassResult(TypedDict):
    params: Params
OpenProposalPassError: TypeAlias = V3ToolErrorResponse

class OpenMediaBuysPageInput(TypedDict):
    accountRelationshipId: NotRequired[str]
    view: NotRequired[Literal['media_buys', 'creatives', 'delivery']]

class Params1(TypedDict):
    accountRelationshipId: NotRequired[str]
    view: NotRequired[Literal['media_buys', 'creatives', 'delivery']]

class OpenMediaBuysPageResult(TypedDict):
    params: Params1
OpenMediaBuysPageError: TypeAlias = V3ToolErrorResponse

class OpenConnectionsPageInput(TypedDict):
    advertiserId: NotRequired[str]
    sellerId: NotRequired[str]
    connectionAction: NotRequired[Literal['connect']]

class OpenConnectionsPageResult(TypedDict):
    advertiserId: NotRequired[str]
    sellerId: NotRequired[str]
    connectionAction: NotRequired[Literal['connect']]
OpenConnectionsPageError: TypeAlias = V3ToolErrorResponse

class OpenCreativeEnginesPageInput(TypedDict):
    engineId: NotRequired[str]
    connectionId: NotRequired[str]
    connectionAction: NotRequired[Literal['connect']]

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
    campaignId: NotRequired[str]
    sponsoredBuyerCustomerId: NotRequired[str]

class Params2(TypedDict):
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    campaignId: NotRequired[str]
    management: NotRequired[Literal['tracked', 'managed', 'all']]
    status: NotRequired[Literal['ALL']]
    sponsoredBuyerCustomerId: NotRequired[str]

class OpenCampaignsPageResult(TypedDict):
    params: NotRequired[Params2]
    humanHandoff: NotRequired[OpenCampaignsPageSuccessPageHumanHandoffRequired | OpenCampaignsPageSuccessPageHumanHandoffUnavailable]
OpenCampaignsPageError: TypeAlias = V3ToolErrorResponse

class OpenCampaignReceiptInput(TypedDict):
    campaignId: str
    sponsoredBuyerCustomerId: NotRequired[str]

class Params3(TypedDict):
    campaignId: str
    advertiserId: NotRequired[str]
    mode: Literal['review']
    sponsoredBuyerCustomerId: NotRequired[str]

class Budget(TypedDict):
    total: OpenCampaignReceiptSuccessSchema8
    currency: OpenCampaignReceiptSuccessSchema9
    dailyCap: NotRequired[float]
    pacing: NotRequired[Literal['even', 'asap', 'frontloaded']]

class MediaBuy(TypedDict):
    mediaBuyId: str
    name: str
    sellerId: str
    sellerName: NotRequired[str]
    phase: Literal['draft', 'pendingApproval', 'inputRequired', 'active', 'ending', 'completed', 'canceled', 'failed', 'rejected']
    isPaused: bool
    budget: OpenCampaignReceiptSuccessSchema15
    budgetShare: NotRequired[float]
    flight: NotRequired[OpenCampaignReceiptSuccessSchema12]
    attentionNote: NotRequired[str]

class Blocker1(TypedDict):
    code: str
    message: str

class Receipt(TypedDict):
    campaignId: str
    advertiserId: str | None
    name: str
    phase: Literal['draft']
    handling: Literal['tracking', 'managing']
    budget: NotRequired[Budget]
    flight: NotRequired[OpenCampaignReceiptSuccessSchema12]
    mediaBuys: list[MediaBuy]
    stagedBudgets: list[OpenCampaignReceiptSuccessSchema15]
    blockers: list[Blocker1]
    readyToGoLive: bool

class OpenCampaignReceiptResult(TypedDict):
    params: Params3
    receipt: Receipt
OpenCampaignReceiptError: TypeAlias = V3ToolErrorResponse
RequiredAuthoredField: TypeAlias = str

class CampaignComposition(TypedDict):
    campaign_id: str
    advertiser_id: NotRequired[UploadCreativeAssetRequestSchema1]
    campaign_name: NotRequired[str]
    creative_name: NotRequired[str]
    required_authored_fields: list[RequiredAuthoredField]

class UploadCreativeAssetInput(TypedDict):
    advertiserId: str
    campaign_composition: NotRequired[CampaignComposition]

class CampaignComposition1(TypedDict):
    campaign_id: str
    advertiser_id: NotRequired[UploadCreativeAssetSuccessSchema0]
    campaign_name: NotRequired[str]
    creative_name: NotRequired[str]
    required_authored_fields: list[RequiredAuthoredField]

class UploadCreativeAssetResult(TypedDict):
    advertiserId: UploadCreativeAssetSuccessSchema0
    advertiserName: NotRequired[str]
    accepted_content_types: list[Literal['image/jpeg', 'image/png', 'video/mp4', 'audio/wav', 'audio/x-wav', 'audio/wave', 'audio/mpeg', 'audio/mp3']]
    max_size_bytes: int
    max_size_bytes_by_content_type: dict[str, int]
    fallback_url: str
    campaign_composition: NotRequired[CampaignComposition1]
UploadCreativeAssetError: TypeAlias = V3ToolErrorResponse

class OpenApprovalsInput(TypedDict):
    mediaBuyId: NotRequired[str]
    buyerCustomerId: NotRequired[int]
    creativeId: NotRequired[str]
    reviewRef: NotRequired[str]

class Params4(TypedDict):
    mediaBuyId: NotRequired[str]
    buyerCustomerId: NotRequired[int]
    creativeId: NotRequired[str]
    reviewRef: NotRequired[str]

class OpenApprovalsResult(TypedDict):
    params: NotRequired[Params4]
OpenApprovalsError: TypeAlias = V3ToolErrorResponse

class OpenCreativeLibraryInput(TypedDict):
    advertiserId: str
    view: NotRequired[Literal['all', 'shelf']]
    lens: NotRequired[Literal['creatives', 'assets', 'composer']]
    campaignId: NotRequired[str]
    creativeId: NotRequired[str]
    sessionId: NotRequired[str]

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
    startDate: NotRequired[str]
    endDate: NotRequired[str]
    lifetime: NotRequired[Literal[True]]

class Filters(TypedDict):
    inventorySourceId: NotRequired[str]
    advertiserId: NotRequired[str]
    campaignId: NotRequired[str]
    channelGroupId: NotRequired[str]
    buyerCustomerId: NotRequired[int]
    mediaBuyId: NotRequired[str]
    packageId: NotRequired[str]

class GetDeliveryInput(TypedDict):
    metrics: NotRequired[list[Literal['impressions', 'spend', 'clicks', 'views', 'completedViews', 'conversions', 'leads', 'videoCompletions', 'conversionValue', 'ecpm', 'cpc', 'ctr', 'completionRate', 'cpa', 'roas', 'sellBooked', 'sellRealized', 'buyBooked', 'buyRealized', 'spreadBooked', 'spreadRealized', 'marginBookedPct', 'marginRealizedPct', 'bookedComplete', 'realizedComplete']]]
    dimensions: NotRequired[list[Literal['date', 'advertiser', 'campaign', 'channel_group', 'channel', 'buyer', 'media_buy', 'package', 'inventory_source', 'seller', 'sales_agent'] | str]]
    sponsoredBuyerCustomerId: NotRequired[str]
    report: NotRequired[Literal['delivery', 'campaign_delivery', 'live_campaign_delivery', 'margin']]
    range: NotRequired[Range]
    filters: NotRequired[Filters]
    limit: NotRequired[int]
    cursor: NotRequired[str]

class Query(TypedDict):
    metrics: list[Literal['impressions', 'spend', 'clicks', 'views', 'completedViews', 'conversions', 'leads', 'videoCompletions', 'conversionValue', 'ecpm', 'cpc', 'ctr', 'completionRate', 'cpa', 'roas', 'sellBooked', 'sellRealized', 'buyBooked', 'buyRealized', 'spreadBooked', 'spreadRealized', 'marginBookedPct', 'marginRealizedPct', 'bookedComplete', 'realizedComplete']]
    dimensions: list[str]
    range: NotRequired[Range]
    filters: Filters

class Period(TypedDict):
    startDate: str
    endDate: str

class Dimensions1(TypedDict):
    id: str | float
    name: NotRequired[str | None]
    status: NotRequired[str]
    management: NotRequired[str]
    productId: NotRequired[str | None]
    productName: NotRequired[str | None]
    upstreamMediaBuyId: NotRequired[str]
    upstreamPackageId: NotRequired[str]

class Source2(TypedDict):
    operation: GetDeliverySuccessSchema11
    inventorySourceIds: list[str]
    inventorySourceIdsTotal: int
    inventorySourceIdsTruncated: bool
    revisionEvidence: Literal['unavailable', 'not_applicable']

class Row(TypedDict):
    dimensions: dict[str, str | float | list[str] | Dimensions1 | None]
    metrics: dict[str, GetDeliverySuccessSchema10]
    authority: Literal['seller_reported_delivery', 'seller_reported_buyer_projection', 'seller_spread_ledger', 'synthetic_demo']
    source: Source2
    currency: str | None
    denomination: Literal['net', 'gross_buyer', 'ledger_settlement']
    dataThrough: str | None
    freshness: Literal['unverified', 'ledger_as_of', 'unavailable']
    finality: GetDeliverySuccessSchema13
    billingEligibility: Literal['not_evaluated']
    settlementStatus: NotRequired[str]

class Totals(TypedDict):
    rowsIncluded: int
    currency: str | None
    metrics: dict[str, GetDeliverySuccessSchema10]
    denomination: Literal['net', 'gross_buyer']
    dataThrough: str | None
    finality: GetDeliverySuccessSchema13
    billingEligibility: Literal['not_evaluated']

class Page1(TypedDict):
    limit: int
    returned: int
    total: int
    truncated: bool
    consistency: Literal['live_per_call']
    nextCursor: NotRequired[str]

class Semantics(TypedDict):
    sourceOperation: GetDeliverySuccessSchema11
    genericFallback: Literal[False]
    measurement: Literal['excluded']
    missingValues: str
    freshness: str
    finality: str
    billingEligibility: str

class Synthetic(TypedDict):
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

class Filters2(TypedDict):
    campaignId: str

class Query1(TypedDict):
    range: Range
    filters: Filters2

class ReportingPeriod(TypedDict):
    start: GetDeliverySuccessSchema17
    end: GetDeliverySuccessSchema17

class ReportingRevision(TypedDict):
    reporting_revision_id: GetDeliverySuccessSchema17
    finality: NotRequired[GetDeliverySuccessSchema17]
    data_through: NotRequired[GetDeliverySuccessSchema17 | None]
    observed_at: NotRequired[GetDeliverySuccessSchema17]
    finalized_at: NotRequired[GetDeliverySuccessSchema17]

class Qualifier(TypedDict):
    viewability_standard: NotRequired[GetDeliverySuccessSchema17]
    completion_source: NotRequired[GetDeliverySuccessSchema17]
    attribution_methodology: NotRequired[GetDeliverySuccessSchema17]
    attribution_window: NotRequired[GetDeliverySuccessSchema21]
    lift_dimension: NotRequired[Literal['awareness', 'consideration', 'favorability', 'purchase_intent', 'ad_recall']]

class Vendor(TypedDict):
    domain: NotRequired[GetDeliverySuccessSchema17]
    brand_id: NotRequired[GetDeliverySuccessSchema17]

class MetricAggregate(TypedDict):
    scope: Literal['standard', 'vendor']
    metric_id: GetDeliverySuccessSchema17
    value: float
    qualifier: NotRequired[Qualifier]
    vendor: NotRequired[Vendor]

class AggregatedTotals(TypedDict):
    metrics: dict[Literal['impressions', 'spend', 'clicks', 'completed_views', 'views', 'conversions', 'conversion_value', 'commissionable_value', 'roas', 'new_to_brand_rate', 'cost_per_acquisition', 'completion_rate', 'reach', 'frequency'], GetDeliverySuccessSchema19]
    media_buy_count: NotRequired[int]
    reach_unit: NotRequired[GetDeliverySuccessSchema17]
    reach_aggregation: NotRequired[GetDeliverySuccessSchema17]
    metric_aggregates: NotRequired[list[MetricAggregate]]
    metric_aggregates_truncated: NotRequired[bool]
    metric_aggregates_total_count: NotRequired[int]

class Totals1(TypedDict):
    metrics: GetDeliverySuccessSchema24
    measurement_source: NotRequired[str]
    reach_unit: NotRequired[GetDeliverySuccessSchema17]
    reach_window: NotRequired[GetDeliverySuccessSchema25]
    effective_rate: NotRequired[GetDeliverySuccessSchema19]

class BreakdownStatus(TypedDict):
    kind: Literal['device_type', 'device_platform', 'audience', 'placement']
    truncated: NotRequired[bool]
    pagination: NotRequired[GetDeliverySuccessSchema18]

class BreakdownStatus1(TypedDict):
    kind: Literal['demographic', 'property', 'collection_property', 'installment_property', 'placement_property']
    truncated: NotRequired[bool]
    suppressed: NotRequired[bool]

class BreakdownStatus2(TypedDict):
    kind: Literal['catalog_item', 'format', 'creative', 'keyword', 'geo', 'collection', 'installment', 'spot']
    truncated: NotRequired[bool]

class ByPackageItem(TypedDict):
    package_id: GetDeliverySuccessSchema17
    metrics: GetDeliverySuccessSchema24
    measurement_source: NotRequired[str]
    reach_unit: NotRequired[GetDeliverySuccessSchema17]
    reach_window: NotRequired[GetDeliverySuccessSchema25]
    currency: NotRequired[GetDeliverySuccessSchema17]
    delivery_status: NotRequired[GetDeliverySuccessSchema17]
    pricing_model: NotRequired[GetDeliverySuccessSchema23]
    pacing_index: NotRequired[float]
    rate: NotRequired[float]
    paused: NotRequired[bool]
    is_final: NotRequired[bool]
    finalized_at: NotRequired[GetDeliverySuccessSchema17]
    measurement_window: NotRequired[str]
    supersedes_window: NotRequired[str]
    breakdown_status: list[BreakdownStatus | BreakdownStatus1 | BreakdownStatus2]

class MediaBuyDelivery(TypedDict):
    media_buy_id: GetDeliverySuccessSchema17
    status: GetDeliverySuccessSchema17
    currency: NotRequired[GetDeliverySuccessSchema17]
    expected_availability: NotRequired[GetDeliverySuccessSchema17]
    is_adjusted: NotRequired[bool]
    pricing_model: NotRequired[GetDeliverySuccessSchema23]
    pacing_index: NotRequired[float]
    is_final: NotRequired[bool]
    finalized_at: NotRequired[GetDeliverySuccessSchema17]
    totals: NotRequired[Totals1]
    by_package: NotRequired[list[ByPackageItem]]
    by_package_truncated: NotRequired[bool]
    by_package_total_count: NotRequired[int]

class DeliverySummary(TypedDict):
    status: GetDeliverySuccessSchema17
    task_id: NotRequired[GetDeliverySuccessSchema17]
    reporting_period: NotRequired[ReportingPeriod]
    currency: NotRequired[GetDeliverySuccessSchema17]
    partial_data: NotRequired[bool]
    unavailable_count: NotRequired[int]
    sequence_number: NotRequired[int]
    next_expected_at: NotRequired[GetDeliverySuccessSchema17]
    pagination: NotRequired[GetDeliverySuccessSchema18]
    reporting_revision: NotRequired[ReportingRevision]
    aggregated_totals: NotRequired[AggregatedTotals]
    media_buy_deliveries: NotRequired[list[MediaBuyDelivery]]
    media_buy_deliveries_truncated: NotRequired[bool]
    media_buy_deliveries_total_count: NotRequired[int]
    sandbox: NotRequired[bool]

class Semantics1(TypedDict):
    sourceOperation: Literal['get_campaign_delivery']
    genericFallback: Literal[False]
    measurement: Literal['excluded']
    missingValues: str
    freshness: str
    finality: str
    billingEligibility: str

class GetDeliveryResult2(TypedDict):
    report: Literal['live_campaign_delivery']
    query: Query1
    campaignId: str
    delivery: dict[str, JsonValue]
    deliverySummary: NotRequired[DeliverySummary]
    authority: Literal['live_provider']
    semantics: Semantics1
GetDeliveryResult: TypeAlias = GetDeliveryResult1 | GetDeliveryResult2
GetDeliveryError: TypeAlias = V3ToolErrorResponse

class Value1(TypedDict):
    macro: Literal['MEDIA_BUY_ID', 'PACKAGE_ID', 'CREATIVE_ID', 'CACHEBUSTER', 'TIMESTAMP', 'CLICK_URL', 'GDPR', 'GDPR_CONSENT', 'US_PRIVACY', 'GPP_STRING', 'GPP_SID', 'IP_ADDRESS', 'LIMIT_AD_TRACKING', 'DEVICE_TYPE', 'OS', 'OS_VERSION', 'DEVICE_MAKE', 'DEVICE_MODEL', 'USER_AGENT', 'APP_BUNDLE', 'APP_NAME', 'COUNTRY', 'REGION', 'CITY', 'ZIP', 'DMA', 'LAT', 'LONG', 'DEVICE_ID', 'DEVICE_ID_TYPE', 'DOMAIN', 'PAGE_URL', 'REFERRER', 'KEYWORDS', 'PLACEMENT_ID', 'FOLD_POSITION', 'AD_WIDTH', 'AD_HEIGHT', 'VIDEO_ID', 'VIDEO_TITLE', 'VIDEO_DURATION', 'VIDEO_CATEGORY', 'CONTENT_GENRE', 'CONTENT_RATING', 'PLAYER_WIDTH', 'PLAYER_HEIGHT', 'POD_POSITION', 'POD_SIZE', 'AD_BREAK_ID', 'STATION_ID', 'COLLECTION_NAME', 'INSTALLMENT_ID', 'AUDIO_DURATION', 'TMPX', 'IMPRESSION_ID', 'AXEM', 'CATALOG_ID', 'SKU', 'GTIN', 'OFFERING_ID', 'JOB_ID', 'HOTEL_ID', 'FLIGHT_ID', 'VEHICLE_ID', 'LISTING_ID', 'STORE_ID', 'PROGRAM_ID', 'DESTINATION_ID', 'CREATIVE_VARIANT_ID', 'APP_ITEM_ID', 'ITEM_NAME', 'ITEM_DESCRIPTION', 'ITEM_TAGLINE', 'ITEM_PRICE', 'ITEM_PRICE_CURRENCY']
    value: str

class TestCreativeMacrosInput(TypedDict):
    requiredMacros: NotRequired[list[Literal['MEDIA_BUY_ID', 'PACKAGE_ID', 'CREATIVE_ID', 'CACHEBUSTER', 'TIMESTAMP', 'CLICK_URL', 'GDPR', 'GDPR_CONSENT', 'US_PRIVACY', 'GPP_STRING', 'GPP_SID', 'IP_ADDRESS', 'LIMIT_AD_TRACKING', 'DEVICE_TYPE', 'OS', 'OS_VERSION', 'DEVICE_MAKE', 'DEVICE_MODEL', 'USER_AGENT', 'APP_BUNDLE', 'APP_NAME', 'COUNTRY', 'REGION', 'CITY', 'ZIP', 'DMA', 'LAT', 'LONG', 'DEVICE_ID', 'DEVICE_ID_TYPE', 'DOMAIN', 'PAGE_URL', 'REFERRER', 'KEYWORDS', 'PLACEMENT_ID', 'FOLD_POSITION', 'AD_WIDTH', 'AD_HEIGHT', 'VIDEO_ID', 'VIDEO_TITLE', 'VIDEO_DURATION', 'VIDEO_CATEGORY', 'CONTENT_GENRE', 'CONTENT_RATING', 'PLAYER_WIDTH', 'PLAYER_HEIGHT', 'POD_POSITION', 'POD_SIZE', 'AD_BREAK_ID', 'STATION_ID', 'COLLECTION_NAME', 'INSTALLMENT_ID', 'AUDIO_DURATION', 'TMPX', 'IMPRESSION_ID', 'AXEM', 'CATALOG_ID', 'SKU', 'GTIN', 'OFFERING_ID', 'JOB_ID', 'HOTEL_ID', 'FLIGHT_ID', 'VEHICLE_ID', 'LISTING_ID', 'STORE_ID', 'PROGRAM_ID', 'DESTINATION_ID', 'CREATIVE_VARIANT_ID', 'APP_ITEM_ID', 'ITEM_NAME', 'ITEM_DESCRIPTION', 'ITEM_TAGLINE', 'ITEM_PRICE', 'ITEM_PRICE_CURRENCY']]]
    rawInput: str
    sourceDialect: NotRequired[Literal['auto', 'adcp', 'happydemics', 'gam', 'vast']]
    targetDialect: Literal['adcp', 'gam']
    scenario: Literal['device_id_present', 'device_id_unavailable', 'gdpr_applies_with_consent', 'gdpr_does_not_apply', 'missing_required_value']
    scenarioKey: NotRequired[str]
    gvlVendorId: NotRequired[int]
    values: NotRequired[list[Value1]]

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
    purpose: NotRequired[list[Literal['live', 'draft', 'evaluation']]]
    origin: NotRequired[list[Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']]]
    selectedPosture: NotRequired[list[SelectedPostureItem]]
    playbookVersion: NotRequired[list[PlaybookVersionItem]]
    material: NotRequired[list[MaterialItem]]
    quickPreset: NotRequired[list[QuickPresetItem]]
    category: NotRequired[list[CategoryItem]]
    location: NotRequired[list[LocationItem]]
    market: NotRequired[list[MarketItem]]
    channel: NotRequired[list[ChannelItem]]
    buyer: NotRequired[list[BuyerItem]]
    advertiser: NotRequired[list[AdvertiserItem]]
    product: NotRequired[list[ProductItem]]
    responseRecipeVersion: NotRequired[list[ResponseRecipeVersionItem]]
    modelVersion: NotRequired[list[ModelVersionItem]]
    judgeVersion: NotRequired[list[JudgeVersionItem]]
    cacheMode: NotRequired[list[Literal['miss_full_compose', 'hit_hydrated', 'hit_customized', 'bypassed']]]
    currency: NotRequired[list[CurrencyItem]]
    responseState: NotRequired[list[Literal['queued', 'processing', 'ready', 'passed', 'needs_clarification', 'failed']]]
    evaluationState: NotRequired[list[EvaluationStateItem]]
    outcome: NotRequired[list[OutcomeItem]]

class Range3(TypedDict):
    startDate: str
    endDate: str

class OrderByItem(TypedDict):
    field: Literal['rfp_count', 'response_ready_rate', 'pass_rate', 'needs_clarification_rate', 'failure_rate', 'average_grade', 'correction_rate', 'revision_rate', 'seller_intervention_rate', 'truth_drop_rate', 'feedback_agreement_rate', 'average_processing_latency_ms', 'p95_processing_latency_ms', 'average_generation_cost', 'full_compose_rate', 'cache_hit_rate', 'retry_rate', 'buyer_response_rate', 'acceptance_rate', 'win_rate', 'booked_budget', 'average_booked_budget', 'date', 'week', 'selected_posture', 'playbook_version', 'material', 'quick_preset', 'category', 'location', 'market', 'channel', 'origin', 'purpose', 'buyer', 'advertiser', 'product', 'response_recipe_version', 'model_version', 'judge_version', 'cache_mode', 'currency']
    direction: Literal['asc', 'desc']

class GetRfpPerformanceInput(TypedDict):
    metrics: list[Literal['rfp_count', 'response_ready_rate', 'pass_rate', 'needs_clarification_rate', 'failure_rate', 'average_grade', 'correction_rate', 'revision_rate', 'seller_intervention_rate', 'truth_drop_rate', 'feedback_agreement_rate', 'average_processing_latency_ms', 'p95_processing_latency_ms', 'average_generation_cost', 'full_compose_rate', 'cache_hit_rate', 'retry_rate', 'buyer_response_rate', 'acceptance_rate', 'win_rate', 'booked_budget', 'average_booked_budget']]
    dimensions: NotRequired[list[Literal['date', 'week', 'selected_posture', 'playbook_version', 'material', 'quick_preset', 'category', 'location', 'market', 'channel', 'origin', 'purpose', 'buyer', 'advertiser', 'product', 'response_recipe_version', 'model_version', 'judge_version', 'cache_mode', 'currency']]]
    filters: NotRequired[Filters3]
    range: Range3
    orderBy: NotRequired[list[OrderByItem]]
    limit: NotRequired[int]
    cursor: NotRequired[str]

class OrderByItem1(TypedDict):
    field: str
    direction: Literal['asc', 'desc']

class Query2(TypedDict):
    metrics: list[str]
    dimensions: list[str]
    filters: dict[str, list[str | float]]
    range: Range3
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
    sourceMaterialId: str
    sourceRevision: int
    candidateId: str
    advertiserRef: NotRequired[str]

class Capabilities(TypedDict):
    offersCreativeReview: NotRequired[bool]
    offersCampaignApproval: NotRequired[bool]

class DemandContact(TypedDict):
    name: str
    email: str

class Listing(TypedDict):
    description: NotRequired[str | None]
    channels: NotRequired[list[SaveSellerRequestSchema27]]
    countries: NotRequired[list[SaveSellerRequestSchema30] | None]
    acceptsAllCountries: NotRequired[bool]

class MediaKit(TypedDict):
    description: NotRequired[str | None]
    channels: NotRequired[list[SaveSellerRequestSchema27]]
    countries: NotRequired[list[SaveSellerRequestSchema30] | None]
    acceptsAllCountries: NotRequired[bool]

class Distribution(TypedDict):
    openaiChallengeToken: str | None
    confirmReplace: NotRequired[bool]
    confirmRemove: NotRequired[bool]

class Admission(TypedDict):
    intakeId: str
    expectedVersion: int
    decision: Literal['admit']
    message: NotRequired[str]

class Admission1(TypedDict):
    intakeId: str
    expectedVersion: int
    decision: Literal['decline']
    message: str

class SaveSellerInput(TypedDict):
    resolveBrand: NotRequired[str]
    identityContract: NotRequired[Literal['confirmed-v1']]
    preview: NotRequired[bool]
    confirmationToken: NotRequired[str]
    materialCandidate: NotRequired[MaterialCandidate]
    operatorDomain: NotRequired[str]
    confirmOperatorDomainProfileReset: NotRequired[bool]
    capabilities: NotRequired[Capabilities]
    setupIntent: NotRequired[Literal['third_party_connect', 'sell_through_scope3']]
    marketplaceParticipation: NotRequired[Literal['PUBLISHED', 'OPTED_OUT']]
    demandContact: NotRequired[DemandContact | None]
    description: NotRequired[str | None]
    channels: NotRequired[list[SaveSellerRequestSchema27]]
    countries: NotRequired[list[SaveSellerRequestSchema30] | None]
    acceptsAllCountries: NotRequired[bool]
    listing: NotRequired[Listing]
    mediaKit: NotRequired[MediaKit]
    defaultCurrency: NotRequired[Literal['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD', 'CNY', 'HKD', 'SGD', 'SEK', 'NOK', 'DKK', 'PLN', 'KRW', 'INR', 'MXN', 'BRL', 'ZAR']]
    paymentCurrencies: NotRequired[list[SaveSellerRequestSchema41]]
    confirmCurrencyCatalogImpact: NotRequired[bool]
    distribution: NotRequired[Distribution]
    admission: NotRequired[Admission | Admission1]

class SaveSellerResult1(TypedDict):
    action: Literal['brand_resolved']
    brand: SaveSellerSuccessSchema0

class SaveSellerResult2(TypedDict):
    action: Literal['admission_recorded', 'decline_recorded']
    intakeId: str
    decision: Literal['admit', 'decline']

class SaveSellerResult3(TypedDict):
    action: Literal['preview']
    identityContract: Literal['confirmed-v1']
    requiresConfirmation: bool
    confirmationToken: str
    before: SaveSellerSuccessSchema0
    after: SaveSellerSuccessSchema0
    docs: str

class SaveSellerResult4(TypedDict):
    action: Literal['updated', 'unchanged']
    object: SaveSellerSuccessSchema0

class SaveSellerResult5(TypedDict):
    action: Literal['updated']
    warning: Literal['updated_but_readback_unavailable']
    readback: Literal['unavailable']

class SaveSellerResult6(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SaveSellerSuccessSchema0

class SaveSellerResult7(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveSellerSuccessSchema0
SaveSellerResult: TypeAlias = SaveSellerResult1 | SaveSellerResult2 | SaveSellerResult3 | SaveSellerResult4 | SaveSellerResult5 | SaveSellerResult6 | SaveSellerResult7
SaveSellerError: TypeAlias = V3ToolErrorResponse

class ModuleConfig(TypedDict):
    moduleInstanceId: str
    config: dict[str, JsonValue]
    merge: NotRequired[bool]
    status: NotRequired[Literal['CONFIGURING', 'DISABLED', 'ERROR']]

class SaveInventorySourceInput(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[Literal['SALES', 'SIGNAL', 'CREATIVE', 'OUTCOME']]
    endpointUrl: NotRequired[str]
    protocol: NotRequired[Literal['MCP', 'A2A']]
    authenticationType: NotRequired[Literal['API_KEY', 'NO_AUTH', 'OAUTH', 'BASIC_AUTH']]
    oauthAudience: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[Literal['PENDING', 'ACTIVE', 'DISABLED']]
    moduleConfig: NotRequired[ModuleConfig]

class ModuleConfig1(TypedDict):
    moduleInstanceId: str
    updated: Literal[True]

class SaveInventorySourceResult1(TypedDict):
    action: Literal['created', 'updated', 'unchanged']
    object: SaveInventorySourceSuccessSchema0
    warning: NotRequired[str]
    moduleConfig: NotRequired[ModuleConfig1]

class SaveInventorySourceResult2(TypedDict):
    success: Literal[True]
    status: int
    data: NotRequired[SaveInventorySourceSuccessSchema0]
SaveInventorySourceResult: TypeAlias = SaveInventorySourceResult1 | SaveInventorySourceResult2
SaveInventorySourceError: TypeAlias = V3ToolErrorResponse
Domain: TypeAlias = str
AddItem: TypeAlias = str
RemoveItem: TypeAlias = str

class Identifier(TypedDict):
    type: str
    value: str

class DeclareProperty(TypedDict):
    domain: str
    propertyId: NotRequired[str]
    propertyType: NotRequired[Literal['website', 'mobile_app', 'ctv_app', 'desktop_app', 'dooh', 'podcast', 'radio', 'streaming_audio']]
    name: NotRequired[str]
    identifiers: NotRequired[list[Identifier]]
    tags: NotRequired[list[Tag]]

class RemoveProperty(TypedDict):
    domain: str
    propertyKey: str

class SaveCoverageInput(TypedDict):
    domains: NotRequired[list[Domain]]
    add: NotRequired[list[AddItem]]
    remove: NotRequired[list[RemoveItem]]
    declareProperties: NotRequired[list[DeclareProperty]]
    removeProperties: NotRequired[list[RemoveProperty]]

class SaveCoverageResult1(TypedDict):
    changed: bool
    added: SaveCoverageSuccessSchema0
    removed: SaveCoverageSuccessSchema0

class SaveCoverageResult2(TypedDict):
    changed: bool
    declared: SaveCoverageSuccessSchema0
    removed: SaveCoverageSuccessSchema0
    failures: SaveCoverageSuccessSchema0
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
    displayName: NotRequired[str]
    documentType: NotRequired[Literal['rate_card']]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet'] | None]
    visibility: NotRequired[SaveMaterialRequestSchema22]
    advertiserRef: NotRequired[str]
    verticals: NotRequired[list[Vertical]]
    markets: NotRequired[list[Market]]
    locales: NotRequired[list[Locale]]
    channels: NotRequired[list[Channel]]
    formats: NotRequired[list[Format]]
    propertyRefs: NotRequired[list[PropertyRef]]
    historicalClientRef: NotRequired[str]
    effectiveFrom: NotRequired[str]
    expiresAt: NotRequired[str]

class Metadata1(TypedDict):
    displayName: NotRequired[str]
    documentType: NotRequired[Literal['rate_card']]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet'] | None]
    visibility: NotRequired[SaveMaterialRequestSchema22]
    advertiserRef: NotRequired[str]
    verticals: NotRequired[list[Vertical]]
    markets: NotRequired[list[Market]]
    locales: NotRequired[list[Locale]]
    channels: NotRequired[list[Channel]]
    formats: NotRequired[list[Format]]
    propertyRefs: NotRequired[list[PropertyRef]]
    historicalClientRef: NotRequired[str]
    effectiveFrom: NotRequired[str]
    expiresAt: NotRequired[str]

class Metadata2(TypedDict):
    displayName: NotRequired[str]
    documentType: NotRequired[Literal['rate_card']]
    documentPurpose: NotRequired[Literal['sales_deck', 'one_sheet', 'case_study', 'response', 'specification_sheet'] | None]
    visibility: NotRequired[SaveMaterialRequestSchema22]
    advertiserRef: NotRequired[str]
    verticals: NotRequired[list[Vertical]]
    markets: NotRequired[list[Market]]
    locales: NotRequired[list[Locale]]
    channels: NotRequired[list[Channel]]
    formats: NotRequired[list[Format]]
    propertyRefs: NotRequired[list[PropertyRef]]
    historicalClientRef: NotRequired[str]
    effectiveFrom: NotRequired[str]
    expiresAt: NotRequired[str]

class SaveMaterialInput3(TypedDict):
    action: Literal['update_metadata']
    materialId: str
    expectedRevision: int
    metadata: Metadata2
    labels: NotRequired[dict[str, list[Label]]]

class SaveMaterialInput4(TypedDict):
    action: Literal['reprocess']
    materialId: str
    sourceRevision: int
    clientRequestId: str

class CorrectedContent(TypedDict):
    title: str
    summary: str
    sourceTextDigest: NotRequired[SaveMaterialRequestSchema13]

class ProposedMutation(TypedDict):
    tool: Literal['save_playbook', 'save_business_rules', 'save_wholesale_product', 'save_signal', 'save_seller']
    arguments: dict[str, JsonValue]

class Correction(TypedDict):
    correctedContent: NotRequired[CorrectedContent]
    proposedMutation: NotRequired[ProposedMutation]

class Decision(TypedDict):
    action: Literal['accept', 'reject', 'correct', 'withdraw']
    correction: NotRequired[Correction]

class SaveMaterialInput5(TypedDict):
    action: Literal['decide_candidate']
    materialId: str
    sourceRevision: int
    candidateId: str
    decision: Decision
    clientRequestId: NotRequired[str]

class SaveMaterialInput6(TypedDict):
    action: Literal['reconcile_candidate']
    applicationId: str

class SaveMaterialInput7(TypedDict):
    action: Literal['mark_reusable']
    materialId: str
    unitId: str
    reusable: bool

class SaveMaterialInput8(TypedDict):
    action: Literal['archive']
    materialId: str

class SaveMaterialInput9(TypedDict):
    action: Literal['restore']
    materialId: str

class SaveMaterialInput10(TypedDict):
    action: Literal['preview_rate_card']
    materialId: str
    sourceRevision: int

class SaveMaterialInput11(TypedDict):
    action: Literal['commit_rate_card']
    materialId: str
    sourceRevision: int
    previewToken: str

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
    facts: list[SaveMaterialSuccessSchema0]
    factsTotal: int
    factsTruncated: bool

class SaveMaterialResult5(TypedDict):
    action: Literal['previewed_rate_card']
    materialId: SaveMaterialSuccessSchema1
    sourceRevision: SaveMaterialSuccessSchema2
    accepted: SaveMaterialSuccessSchema3
    rejected: SaveMaterialSuccessSchema4
    changes: SaveMaterialSuccessSchema5
    floorWarnings: SaveMaterialSuccessSchema6
    previewToken: SaveMaterialSuccessSchema7
    previewExpiresAt: SaveMaterialSuccessSchema8
    acceptedTotal: SaveMaterialSuccessSchema9
    rejectedTotal: SaveMaterialSuccessSchema10
    truncated: SaveMaterialSuccessSchema11
    floorWarningsTruncated: SaveMaterialSuccessSchema12

class Next1(TypedDict):
    tool: Literal['get']
    arguments: Arguments3

class RateCard(TypedDict):
    materialId: SaveMaterialSuccessSchema1
    sourceRevision: SaveMaterialSuccessSchema2
    accepted: SaveMaterialSuccessSchema3
    rejected: SaveMaterialSuccessSchema4
    changes: SaveMaterialSuccessSchema5
    floorWarnings: SaveMaterialSuccessSchema6
    previewToken: SaveMaterialSuccessSchema7
    previewExpiresAt: SaveMaterialSuccessSchema8
    acceptedTotal: SaveMaterialSuccessSchema9
    rejectedTotal: SaveMaterialSuccessSchema10
    truncated: SaveMaterialSuccessSchema11
    floorWarningsTruncated: SaveMaterialSuccessSchema12

class SaveMaterialResult6(TypedDict):
    materialId: str
    sourceRevision: int
    processingState: str
    idempotentReplay: bool
    next: Next1
    rateCard: RateCard

class SaveMaterialResult7(TypedDict):
    action: Literal['reconciled']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveMaterialSuccessSchema0
SaveMaterialResult: TypeAlias = SaveMaterialResult1 | SaveMaterialResult2 | SaveMaterialResult3 | SaveMaterialResult4 | SaveMaterialResult5 | SaveMaterialResult6 | SaveMaterialResult7
SaveMaterialError: TypeAlias = V3ToolErrorResponse

class FormatOption(TypedDict):
    formatOptionId: NotRequired[str]
    publisherDomain: NotRequired[str]
    formatKind: Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']
    params: dict[str, JsonValue]

class PricingOption(TypedDict):
    isFixed: NotRequired[bool]
    rate: NotRequired[float]
    currency: NotRequired[str]
    deliveryType: Literal['guaranteed', 'non_guaranteed']

class SaveWholesaleProductInput(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    sourceId: str
    id: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[Literal['draft', 'active', 'archived']]
    deliveryType: NotRequired[str]
    channels: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence', 'audio', 'video']]]
    inventory: NotRequired[dict[str, JsonValue]]
    formatOptions: NotRequired[list[FormatOption]]
    pricingOptions: NotRequired[list[PricingOption]]
    dryRun: NotRequired[bool]
    delete: NotRequired[Literal[True]]
    confirmName: NotRequired[str]
    prebidIntegrationActive: NotRequired[bool]

class SaveWholesaleProductResult1(TypedDict):
    saved: Literal[True]
    created: bool
    sourceId: str
    id: NotRequired[str]
    status: str
    pricingStatus: str | None
    warnings: list[SaveWholesaleProductSuccessSchema0]

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
    errors: list[SaveWholesaleProductSuccessSchema0]
    warnings: list[SaveWholesaleProductSuccessSchema0]

class SaveWholesaleProductResult6(TypedDict):
    saved: Literal[False]
    dryRun: Literal[True]
    valid: Literal[True]
    sourceId: str
    warnings: list[SaveWholesaleProductSuccessSchema0]

class SaveWholesaleProductResult7(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SaveWholesaleProductSuccessSchema0

class SaveWholesaleProductResult8(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveWholesaleProductSuccessSchema0
SaveWholesaleProductResult: TypeAlias = SaveWholesaleProductResult1 | SaveWholesaleProductResult2 | SaveWholesaleProductResult3 | SaveWholesaleProductResult4 | SaveWholesaleProductResult5 | SaveWholesaleProductResult6 | SaveWholesaleProductResult7 | SaveWholesaleProductResult8
SaveWholesaleProductError: TypeAlias = V3ToolErrorResponse
Region: TypeAlias = str
EvidenceUrl: TypeAlias = str

class SaveMediaKitInput(TypedDict):
    summary: NotRequired[str]
    propertyCount: NotRequired[int]
    channels: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence', 'audio', 'video']]]
    regions: NotRequired[list[Region]]
    verticals: NotRequired[list[Vertical]]
    evidenceUrls: NotRequired[list[EvidenceUrl]]
    notes: NotRequired[str]

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
    height: int

class Hints(TypedDict):
    channels: NotRequired[list[Channel]]
    creativeTerms: NotRequired[list[CreativeTerm]]
    publisherDomains: NotRequired[list[PublisherDomain]]
    countries: NotRequired[list[Country]]
    advertiserVerticals: NotRequired[list[AdvertiserVertical]]
    seasonality: NotRequired[list[SeasonalityItem]]
    signalTags: NotRequired[list[SignalTag]]
    placementTags: NotRequired[list[PlacementTag]]
    formatDimensions: NotRequired[list[FormatDimension]]

class Fact(TypedDict):
    id: str
    label: str
    appliesWhen: str
    hints: NotRequired[Hints]
    pricingModel: NotRequired[Literal['cpm', 'vcpm', 'cpc', 'cpcv', 'cpv', 'cpp', 'cpa', 'revenue_share', 'flat_rate', 'time']]
    currency: NotRequired[str]
    targetPrice: NotRequired[float]
    floorPrice: NotRequired[float]
    ceilingPrice: NotRequired[float]
    strength: NotRequired[Literal['hard_floor', 'default', 'guidance']]
    provenance: NotRequired[str]
    notes: NotRequired[str]

class Pricing(TypedDict):
    currency: NotRequired[str]
    facts: NotRequired[list[Fact]]

class Rule(TypedDict):
    houseDomain: str
    scope: Literal['brand', 'operator']
    discountPercent: float
    notes: NotRequired[str | None]

class RemoveItem1(TypedDict):
    houseDomain: SavePlaybookRequestSchema53
    scope: Literal['brand', 'operator']

class Discounts(TypedDict):
    rules: NotRequired[list[Rule]]
    remove: NotRequired[list[RemoveItem1]]

class SavePlaybookInput(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    content: NotRequired[str]
    notes: NotRequired[str]
    pricing: NotRequired[Pricing]
    discounts: NotRequired[Discounts]

class SavePlaybookResult1(TypedDict):
    playbook: SavePlaybookSuccessSchema0
    createdVersion: NotRequired[float]
    replacedVersion: NotRequired[float | None]

class SavePlaybookResult2(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SavePlaybookSuccessSchema0

class SavePlaybookResult3(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SavePlaybookSuccessSchema0
SavePlaybookResult: TypeAlias = SavePlaybookResult1 | SavePlaybookResult2 | SavePlaybookResult3
SavePlaybookError: TypeAlias = V3ToolErrorResponse

class SaveBusinessRulesInput1(TypedDict):
    pass

class SaveBusinessRulesInput3(TypedDict):
    materialCandidate: NotRequired[MaterialCandidate]
    content: NotRequired[str]
    briefAcceptancePolicy: NotRequired[str]
    creativePolicy: NotRequired[str]
    notes: NotRequired[str]
    creativeApproval: NotRequired[Literal['auto', 'manual']]
    mediaBuyApproval: NotRequired[Literal['auto', 'manual']]
    acknowledgeNoHumanReview: NotRequired[bool]
    advertisingPolicyDisclosure: NotRequired[list[Literal['brief_acceptance', 'creative_policy']]]

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
    businessRules: SaveBusinessRulesSuccessSchema0
    createdVersion: NotRequired[float]
    replacedVersion: NotRequired[float | None]

class SaveBusinessRulesResult2(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SaveBusinessRulesSuccessSchema0

class SaveBusinessRulesResult3(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveBusinessRulesSuccessSchema0
SaveBusinessRulesResult: TypeAlias = SaveBusinessRulesResult1 | SaveBusinessRulesResult2 | SaveBusinessRulesResult3
SaveBusinessRulesError: TypeAlias = V3ToolErrorResponse

class SaveAdvertiserInstructionsInput(TypedDict):
    id: NotRequired[str]
    operatorDomain: NotRequired[SaveAdvertiserInstructionsRequestSchema4 | None]
    brandDomain: NotRequired[SaveAdvertiserInstructionsRequestSchema4 | None]
    discountPercent: NotRequired[float | None]
    notes: NotRequired[str | None]
    countries: NotRequired[list[Country] | None]

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
    sourceId: NotRequired[str]
    id: NotRequired[str]
    draft: NotRequired[dict[str, JsonValue]]
    state: NotRequired[Literal['active', 'archived']]
    confirmArchiveCascade: NotRequired[bool]

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
    object: SaveSignalSuccessSchema0

class SaveSignalResult2(TypedDict):
    action: Literal['unchanged']
    idempotentReplay: Literal[True]
    materialReceipt: SaveSignalSuccessSchema0

class SaveSignalResult3(TypedDict):
    action: Literal['unchanged']
    destinationSaveReplayed: Literal[False]
    materialReceipt: SaveSignalSuccessSchema0
SaveSignalResult: TypeAlias = SaveSignalResult1 | SaveSignalResult2 | SaveSignalResult3
SaveSignalError: TypeAlias = V3ToolErrorResponse

class SaveWorkItemInput(TypedDict):
    kind: Literal['creative_review', 'media_buy_approval', 'modular_source']
    id: str
    sourceId: NotRequired[str]
    status: Literal['approved', 'rejected', 'completed']
    reviewerNotes: NotRequired[str]
    expectedContentDigest: NotRequired[str]
    result: NotRequired[dict[str, JsonValue]]

class ActionEvidence(TypedDict):
    basis: Literal['unproven']
    reason: str

class SaveWorkItemResult(TypedDict):
    action: Literal['created', 'unchanged']
    object: dict[str, JsonValue]
    actionEvidence: NotRequired[ActionEvidence]
SaveWorkItemError: TypeAlias = V3ToolErrorResponse

class Preset(TypedDict):
    buyer: NotRequired[SaveRfpRequestP]
    advertiser: NotRequired[SaveRfpRequestP]
    category: NotRequired[SaveRfpRequestP]
    location: NotRequired[SaveRfpRequestP]
    market: NotRequired[SaveRfpRequestP]
    channels: NotRequired[list[Channel]]
    objective: NotRequired[SaveRfpRequestP]
    advertiserClass: NotRequired[SaveRfpRequestP]
    budgetBand: NotRequired[SaveRfpRequestP]

class Budget1(TypedDict):
    amount: NotRequired[float]
    currency: NotRequired[str]

class Constraints(TypedDict):
    formatKinds: NotRequired[SaveRfpRequestSchema71]
    format_kinds: NotRequired[SaveRfpRequestSchema71]
    productCount: NotRequired[SaveRfpRequestSchema73]
    product_count: NotRequired[SaveRfpRequestSchema73]
    planRoles: NotRequired[SaveRfpRequestSchema74]
    plan_roles: NotRequired[SaveRfpRequestSchema74]
    measurementRequirements: NotRequired[SaveRfpRequestSchema82]
    measurement_requirements: NotRequired[SaveRfpRequestSchema82]
    requiredInputs: NotRequired[list[Literal['flight', 'audience']]]
    requiredCreativeInputs: NotRequired[SaveRfpRequestSchema79]
    locale: NotRequired[SaveRfpRequestSchema86]
    mustInclude: NotRequired[list[SaveRfpRequestSchema77]]

class Strategy(TypedDict):
    posture: NotRequired[SaveRfpRequestSchema51]
    passReason: NotRequired[SaveRfpRequestP]
    pass_reason: NotRequired[SaveRfpRequestP]

class RequiredLibraryUnitId(TypedDict):
    materialId: SaveRfpRequestI
    unitId: SaveRfpRequestI
    renditionRevision: int

class SaveRfpInput3(TypedDict):
    action: Literal['record_feedback']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    turnId: SaveRfpRequestI
    feedback: dict[SaveRfpRequestK, SaveRfpRequestJ]
    grade: NotRequired[Literal['A', 'B', 'C', 'D', 'F']]
    ledBy: NotRequired[Literal['agent', 'human']]
    commentary: NotRequired[SaveRfpRequestP]

class SaveRfpInput4(TypedDict):
    action: Literal['record_feedback']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    turnId: SaveRfpRequestI
    feedback: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    grade: Literal['A', 'B', 'C', 'D', 'F']
    ledBy: NotRequired[Literal['agent', 'human']]
    commentary: NotRequired[SaveRfpRequestP]

class SaveRfpInput5(TypedDict):
    action: Literal['record_feedback']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    turnId: SaveRfpRequestI
    feedback: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    grade: NotRequired[Literal['A', 'B', 'C', 'D', 'F']]
    ledBy: Literal['agent', 'human']
    commentary: NotRequired[SaveRfpRequestP]

class SaveRfpInput6(TypedDict):
    action: Literal['record_feedback']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    turnId: SaveRfpRequestI
    feedback: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    grade: NotRequired[Literal['A', 'B', 'C', 'D', 'F']]
    ledBy: NotRequired[Literal['agent', 'human']]
    commentary: SaveRfpRequestP

class Representation(TypedDict):
    format: Literal['seller_response_json', 'buyer_proposal_json', 'semantic_document_json', 'html', 'pdf', 'pptx']
    renderProfile: NotRequired[Literal['seller_proposal_v1']]
    locale: NotRequired[SaveRfpRequestSchema86]
    audience: NotRequired[Literal['seller_preview', 'buyer_delivery']]

class SaveRfpInput7(TypedDict):
    action: Literal['request_representation']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    turnId: SaveRfpRequestI
    representation: Representation

class SaveRfpInput8(TypedDict):
    action: Literal['cancel_representation']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    turnId: SaveRfpRequestI
    representationId: SaveRfpRequestI

class SaveRfpInput9(TypedDict):
    action: Literal['release_turn']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    turnId: SaveRfpRequestI

class Outcome(TypedDict):
    result: NotRequired[SaveRfpRequestP]
    finality: NotRequired[Literal['preliminary', 'final', 'mixed']]
    details: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]

class SaveRfpInput10(TypedDict):
    action: Literal['record_outcome']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    turnId: SaveRfpRequestI
    outcome: Outcome

class SaveRfpInput11(TypedDict):
    action: Literal['attach_response']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    materialId: SaveRfpRequestI

class SaveRfpInput12(TypedDict):
    action: Literal['endorse']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    commentary: NotRequired[SaveRfpRequestP]

class SaveRfpInput13(TypedDict):
    action: Literal['unendorse']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI

class SaveRfpResult1(TypedDict):
    rfpId: SaveRfpSuccessSchema0
    turnId: SaveRfpSuccessSchema1
    idempotentReplay: SaveRfpSuccessSchema2
    turnNumber: int
    responseState: str
    next: SaveRfpSuccessSchema3

class SaveRfpResult2(TypedDict):
    rfpId: SaveRfpSuccessSchema0
    turnId: SaveRfpSuccessSchema1
    idempotentReplay: SaveRfpSuccessSchema2
    clientRequestId: str
    feedbackId: str
    next: SaveRfpSuccessSchema3

class SaveRfpResult3(TypedDict):
    rfpId: SaveRfpSuccessSchema0
    turnId: SaveRfpSuccessSchema1
    idempotentReplay: SaveRfpSuccessSchema2
    pairId: str
    paired: Literal[True]
    endorsed: bool
    responseKind: Literal['turn', 'material']
    clientRequestId: str
    next: SaveRfpSuccessSchema4

class SaveRfpResult4(TypedDict):
    rfpId: SaveRfpSuccessSchema0
    turnId: SaveRfpSuccessSchema1
    idempotentReplay: SaveRfpSuccessSchema2
    released: Literal[True]
    next: SaveRfpSuccessSchema4

class SaveRfpResult5(TypedDict):
    rfpId: SaveRfpSuccessSchema0
    turnId: SaveRfpSuccessSchema1
    idempotentReplay: SaveRfpSuccessSchema2
    clientRequestId: str
    representationId: str
    representationState: Literal['queued', 'processing', 'ready', 'failed', 'canceled']
    next: SaveRfpSuccessSchema3

class SaveRfpResult6(TypedDict):
    rfpId: SaveRfpSuccessSchema0
    turnId: SaveRfpSuccessSchema1
    idempotentReplay: SaveRfpSuccessSchema2
    outcomeId: str
    next: SaveRfpSuccessSchema3
SaveRfpResult: TypeAlias = SaveRfpResult1 | SaveRfpResult2 | SaveRfpResult3 | SaveRfpResult4 | SaveRfpResult5 | SaveRfpResult6
SaveRfpError: TypeAlias = V3ToolErrorResponse

class CustomMacro(TypedDict):
    name: str
    paramKey: str
    description: NotRequired[str]

class MacroAddition(TypedDict):
    paramKey: str
    value: str | None

class Tracker(TypedDict):
    trackerId: NotRequired[str]
    name: str
    vendorName: NotRequired[str]
    url: NotRequired[str]
    trackerType: Literal['impression', 'click', 'custom']
    customEventName: NotRequired[str]
    enabled: NotRequired[bool]
    gvlVendorId: NotRequired[int]
    sourceDialect: NotRequired[Literal['adcp', 'happydemics', 'gam', 'vast', 'custom']]

class Tracking(TypedDict):
    expectedRevision: NotRequired[int]
    enabledMacros: NotRequired[list[Literal['CAMPAIGN_ID', 'CREATIVE_ID', 'TRACKING_TAG_ID', 'DATA_SET_ID', 'TACTIC_ID', 'MEDIA_BUY_ID', 'SALES_AGENT_ID', 'ATTRIBUTION_TRACKING_ID', 'DEVICE_ID', 'DEVICE_ID_TYPE', 'CACHEBUSTER', 'GDPR', 'GDPR_CONSENT', 'US_PRIVACY', 'LIMIT_AD_TRACKING', 'DEVICE_TYPE', 'OS', 'OS_VERSION', 'DEVICE_MAKE', 'DEVICE_MODEL', 'APP_BUNDLE', 'APP_NAME', 'COUNTRY', 'REGION', 'CITY', 'ZIP', 'DMA', 'LAT', 'LONG', 'PLACEMENT_ID', 'FOLD_POSITION', 'AD_WIDTH', 'AD_HEIGHT', 'VIDEO_ID', 'VIDEO_TITLE', 'VIDEO_DURATION', 'VIDEO_CATEGORY', 'CONTENT_GENRE', 'CONTENT_RATING', 'PLAYER_WIDTH', 'PLAYER_HEIGHT', 'POD_POSITION', 'POD_SIZE', 'AD_BREAK_ID', 'AXEM', 'TIMESTAMP']]]
    customMacros: NotRequired[list[CustomMacro]]
    macroAdditions: NotRequired[list[MacroAddition]]
    impressionTrackerEnabled: NotRequired[bool]
    clickTrackerEnabled: NotRequired[bool]
    trackers: NotRequired[list[Tracker]]

class AssignAccount(TypedDict):
    partnerId: str
    accountId: str
    credentialId: NotRequired[str]

class UnassignAccount(TypedDict):
    linkId: str

class Bucket(TypedDict):
    protocol: Literal['s3', 'gcs', 'azure_blob']
    bucket: str
    prefix: NotRequired[str]
    region: NotRequired[str]
    format: NotRequired[Literal['jsonl', 'csv', 'parquet', 'avro', 'orc']]
    compression: NotRequired[Literal['gzip', 'none']]
    file_retention_days: int
    setup_instructions: NotRequired[str]

class UpdateReportingBucket(TypedDict):
    linkId: str
    bucket: Bucket | None

class SaveAdvertiserInput(TypedDict):
    sponsoredBuyerCustomerId: NotRequired[str]
    advertiserId: NotRequired[str]
    name: NotRequired[str]
    brand: NotRequired[str]
    publicBrand: NotRequired[bool]
    identityContract: NotRequired[Literal['confirmed-v1']]
    preview: NotRequired[bool]
    confirmationToken: NotRequired[str]
    primaryCurrency: NotRequired[str]
    brandCountries: NotRequired[list[str]]
    preferredTimezone: NotRequired[str]
    channels: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence']]]
    sandbox: NotRequired[bool]
    isArchived: NotRequired[bool]
    advertiserIds: NotRequired[list[AdvertiserId]]
    correlationId: NotRequired[str]
    idempotencyKey: NotRequired[str]
    tracking: NotRequired[Tracking]
    labels: NotRequired[dict[str, list[Label]]]
    resolveBrand: NotRequired[str]
    assignAccount: NotRequired[AssignAccount]
    unassignAccount: NotRequired[UnassignAccount]
    updateReportingBucket: NotRequired[UpdateReportingBucket]

class After(TypedDict):
    brand: str

class SaveAdvertiserResult1(TypedDict):
    action: Literal['preview']
    identityContract: Literal['confirmed-v1']
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
    operatorScope: Literal['whole_operator', 'specific_unit']
    operatorUnitId: NotRequired[str]
    identityContract: NotRequired[Literal['confirmed-v1']]
    preview: NotRequired[bool]
    confirmationToken: NotRequired[str]

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
    accessChanged: Literal[False]
    operatorIdentity: NotRequired[OperatorIdentity1]
    preview: NotRequired[Preview1]
    receipt: NotRequired[Receipt2]
    docs: str
SaveBuyerOperatorError: TypeAlias = V3ToolErrorResponse

class SaveBuyerAgentInput1(TypedDict):
    displayName: SaveBuyerAgentRequestSchema0
    kind: NotRequired[Literal['external', 'hosted']]

class SaveBuyerAgentInput2(TypedDict):
    id: SaveBuyerAgentRequestSchema2
    displayName: SaveBuyerAgentRequestSchema0

class Advertiser2(TypedDict):
    advertiserId: str
    role: Literal['READ', 'READ_WRITE']

class Access1(TypedDict):
    expectedAccessRevision: int
    advertisers: list[Advertiser2]

class SaveBuyerAgentInput3(TypedDict):
    id: SaveBuyerAgentRequestSchema2
    access: Access1

class Lifecycle(TypedDict):
    action: Literal['suspend']
    expectedLifecycleState: Literal['active']
    confirmationText: SaveBuyerAgentRequestSchema4

class Lifecycle1(TypedDict):
    action: Literal['resume']
    expectedLifecycleState: Literal['suspended']
    confirmationText: NotRequired[SaveBuyerAgentRequestSchema4]

class Lifecycle2(TypedDict):
    action: Literal['retire']
    expectedLifecycleState: Literal['active', 'suspended']
    confirmationText: SaveBuyerAgentRequestSchema4

class SaveBuyerAgentInput4(TypedDict):
    id: SaveBuyerAgentRequestSchema2
    lifecycle: Lifecycle | Lifecycle1 | Lifecycle2
SaveBuyerAgentInput: TypeAlias = SaveBuyerAgentInput1 | SaveBuyerAgentInput2 | SaveBuyerAgentInput3 | SaveBuyerAgentInput4
SaveBuyerAgentError: TypeAlias = V3ToolErrorResponse

class SaveDirectedCampaignSubscriptionInput(TypedDict):
    connectionId: str
    accountId: str
    advertiserId: NotRequired[str]
    sourceId: NotRequired[str]
    unsubscribe: NotRequired[bool]

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
    email: NotRequired[str]
    hashedEmail: NotRequired[str]
    hashedPhone: NotRequired[str]

class RemoveItem2(TypedDict):
    externalId: str

class Audience(TypedDict):
    audienceId: str
    name: NotRequired[str]
    add: NotRequired[list[AddItem1]]
    remove: NotRequired[list[RemoveItem2]]
    delete: NotRequired[bool]
    consentBasis: NotRequired[Literal['consent', 'legitimate_interest', 'contract', 'legal_obligation']]

class SaveAudienceInput(TypedDict):
    advertiserId: int | str
    audiences: list[Audience]

class SaveAudienceResult(TypedDict):
    action: Literal['synced']
    operationId: str
    advertiserId: int
    audienceCount: int
SaveAudienceError: TypeAlias = V3ToolErrorResponse

class Flight(TypedDict):
    startAt: str
    endAt: str

class Budget7(TypedDict):
    total: float
    currency: str
    dailyCap: NotRequired[float]
    pacing: NotRequired[Literal['even', 'asap', 'frontloaded']]

class Config(TypedDict):
    maxImpressions: int
    per: Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']
    window: Window

class FrequencyCap(TypedDict):
    level: Literal['mediaBuy']
    config: Config
CreativeId: TypeAlias = str

class Autonomy(TypedDict):
    inventorySelection: NotRequired[Literal['manual', 'propose', 'automatic']]
    rebriefing: NotRequired[Literal['manual', 'propose', 'automatic']]

class Tracker1(TypedDict):
    trackerId: NotRequired[SaveCampaignRequestSchema82]
    name: str
    vendorName: NotRequired[str]
    url: NotRequired[str]
    trackerType: Literal['impression', 'click', 'custom']
    customEventName: NotRequired[str]
    enabled: NotRequired[bool]
    gvlVendorId: NotRequired[int]
    sourceDialect: NotRequired[Literal['adcp', 'happydemics', 'gam', 'vast', 'custom']]

class Override(TypedDict):
    trackerId: SaveCampaignRequestSchema82
    enabled: bool

class Tracking1(TypedDict):
    expectedRevision: NotRequired[int]
    trackers: NotRequired[list[Tracker1]]
    overrides: NotRequired[list[Override]]
    macroAdditions: NotRequired[list[MacroAddition]]
GeoCountry: TypeAlias = str
GeoCountriesExcludeItem: TypeAlias = str
GeoRegion: TypeAlias = str
GeoRegionsExcludeItem: TypeAlias = str

class TravelTime(TypedDict):
    value: float
    unit: Literal['min', 'hr']

class Radius(TypedDict):
    value: float
    unit: Literal['km', 'mi', 'm']

class Geometry1(TypedDict):
    type: Literal['Polygon', 'MultiPolygon']
    coordinates: list[JsonValue]

class GeoProximityItem(TypedDict):
    lat: NotRequired[float]
    lng: NotRequired[float]
    label: NotRequired[str]
    travel_time: NotRequired[TravelTime]
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    radius: NotRequired[Radius]
    geometry: NotRequired[Geometry1]
    ext: NotRequired[dict[str, JsonValue]]
LanguageItem: TypeAlias = str

class DaypartTarget(TypedDict):
    days: list[Literal['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]
    start_hour: int
    end_hour: int
    timezone: NotRequired[Literal['inventory_local'] | JsonValue]
    label: NotRequired[str]

class Age1(TypedDict):
    min: JsonValue

class Age2(TypedDict):
    accepted_verification_methods: JsonValue
    accepted_bases: JsonValue

class Age3(TypedDict):
    min: NotRequired[int]
    max: NotRequired[int]
    include_unknown: bool
    accepted_bases: NotRequired[list[Literal['verified', 'declared', 'inferred']]]
    accepted_verification_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]

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

class Demographics(TypedDict):
    age: Age

class AgeRestriction(TypedDict):
    min: int
    verification_required: NotRequired[bool]
    accepted_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]

class TargetingOverlay(TypedDict):
    geo_countries: NotRequired[list[GeoCountry]]
    geo_countries_exclude: NotRequired[list[GeoCountriesExcludeItem]]
    geo_regions: NotRequired[list[GeoRegion]]
    geo_regions_exclude: NotRequired[list[GeoRegionsExcludeItem]]
    geo_metros: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared3]
    geo_metros_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared3]
    geo_postal_areas: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared1]
    geo_postal_areas_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared1]
    geo_places: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared2]
    geo_places_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared2]
    geo_proximity: NotRequired[list[GeoProximityItem]]
    language: NotRequired[list[LanguageItem]]
    device_type: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared6]
    device_type_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared6]
    device_platform: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared4]
    device_platform_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared4]
    browser: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared5]
    browser_exclude: NotRequired[SaveCampaignRequestCampaignTargetingOverlayShared5]
    daypart_targets: NotRequired[list[DaypartTarget]]
    demographics: NotRequired[Demographics]
    age_restriction: NotRequired[AgeRestriction]

class GeoItem(TypedDict):
    requirementId: str
    strength: SaveCampaignRequestSchema195
    include: NotRequired[list[SaveCampaignRequestSchema197]]
    exclude: NotRequired[list[SaveCampaignRequestSchema197]]

class LanguageItem1(TypedDict):
    requirementId: str
    strength: SaveCampaignRequestSchema195
    include: NotRequired[list[SaveCampaignRequestSchema202]]
    exclude: NotRequired[list[SaveCampaignRequestSchema202]]

class DeviceItem(TypedDict):
    requirementId: str
    strength: SaveCampaignRequestSchema195
    include: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]

class Window2(TypedDict):
    days: list[Literal['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']]
    startHour: int
    endHour: int

class Daypart(TypedDict):
    requirementId: str
    strength: SaveCampaignRequestSchema195
    timezone: str
    windows: list[Window2]

class AgeItem(TypedDict):
    requirementId: str
    strength: SaveCampaignRequestSchema195
    minAge: NotRequired[int]
    maxAge: NotRequired[int]
    includeUnknownAge: NotRequired[bool]
    allowModeledAge: NotRequired[bool]

class Demographics1(TypedDict):
    age: NotRequired[list[AgeItem]]
IncludeItem: TypeAlias = str
ExcludeItem: TypeAlias = str

class GeoMetro(TypedDict):
    requirementId: str
    strength: Literal['required']
    system: Literal['nielsen_dma']
    include: NotRequired[list[IncludeItem]]
    exclude: NotRequired[list[ExcludeItem]]

class Targeting(TypedDict):
    geo: NotRequired[list[GeoItem]]
    language: NotRequired[list[LanguageItem1]]
    device: NotRequired[list[DeviceItem]]
    dayparts: NotRequired[list[Daypart]]
    demographics: NotRequired[Demographics1]
    geoMetros: NotRequired[list[GeoMetro]]

class ChannelGroups(TypedDict):
    channelGroupId: SaveCampaignRequestSchema245
    name: NotRequired[SaveCampaignRequestSchema247]
    presetId: Literal['display', 'olv', 'mobile_web_display', 'mobile_web_olv', 'ctv']
    presetVersion: NotRequired[int]

class Inventory(TypedDict):
    channels: NotRequired[list[Literal['display', 'olv', 'social', 'search', 'ctv', 'linear_tv', 'radio', 'streaming_audio', 'podcast', 'dooh', 'ooh', 'print', 'cinema', 'email', 'gaming', 'retail_media', 'influencer', 'affiliate', 'product_placement', 'sponsored_intelligence']]]
    propertyTypes: NotRequired[list[Literal['website', 'mobile_app', 'ctv_app', 'desktop_app', 'dooh', 'podcast', 'radio', 'linear_tv', 'streaming_audio', 'ai_assistant']]]
    deviceTypes: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    formatKinds: NotRequired[list[Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']]]

class ChannelGroups1(TypedDict):
    channelGroupId: SaveCampaignRequestSchema245
    name: NotRequired[SaveCampaignRequestSchema247]
    inventory: Inventory
TargetAudienceId: TypeAlias = str
SuppressAudienceId: TypeAlias = str

class AudienceConfig(TypedDict):
    targetAudienceIds: NotRequired[list[TargetAudienceId]]
    suppressAudienceIds: NotRequired[list[SuppressAudienceId]]
    deleteMissing: NotRequired[bool]

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

class Warnings1(TypedDict):
    type: Literal['stale_draft']
    mediaBuyIds: list[str]
    hint: str

class Execution(TypedDict):
    mediaBuysExecuted: float
    noOp: bool
    errors: NotRequired[list[Error10]]
    warnings: NotRequired[list[Warnings | Warnings1]]

class PropertyListAttachment(TypedDict):
    propertyListId: str
    cascade: SaveCampaignSuccessSchema2

class PropertyListClear(TypedDict):
    cascade: SaveCampaignSuccessSchema2

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
    budget: NotRequired[SaveCampaignSuccessSchema4]
    sellerName: NotRequired[str]

class Launch(TypedDict):
    mediaBuyCount: int
    mediaBuys: list[MediaBuy1]
    mediaBuysTruncated: NotRequired[Literal[True]]
    combinedBudget: SaveCampaignSuccessSchema4 | None
    budgetsByCurrency: NotRequired[list[SaveCampaignSuccessSchema4]]
    blockers: NotRequired[list[Blocker1]]

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
    catalogField: NotRequired[str]
    assetGroupId: NotRequired[str]
    value: NotRequired[JsonValue]
    transform: NotRequired[Literal['date', 'divide', 'boolean', 'split']]
    format: NotRequired[str]
    timezone: NotRequired[str]
    by: NotRequired[float]
    separator: NotRequired[str]
    default: NotRequired[JsonValue]
    ext: NotRequired[dict[str, JsonValue]]

class SaveCatalogInput(TypedDict):
    feedFieldMappings: NotRequired[list[FeedFieldMapping]]
    catalogId: str
    advertiserId: str
    name: NotRequired[str]
    type: NotRequired[Literal['offering', 'product', 'inventory', 'store', 'promotion', 'hotel', 'flight', 'job', 'vehicle', 'real_estate', 'education', 'destination', 'app']]
    url: NotRequired[str]
    feedFormat: NotRequired[Literal['google_merchant_center', 'facebook_catalog', 'shopify', 'linkedin_jobs', 'tiktok_shop', 'pinterest_catalog', 'openai_product_feed', 'custom']]
    updateFrequency: NotRequired[Literal['realtime', 'hourly', 'daily', 'weekly']]
    items: NotRequired[list[dict[str, JsonValue]]]
    ids: NotRequired[list[Id]]
    gtins: NotRequired[list[Gtin]]
    tags: NotRequired[list[Tag]]
    category: NotRequired[str]
    query: NotRequired[str]
    conversionEvents: NotRequired[list[Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']]]
    contentIdType: NotRequired[Literal['sku', 'gtin', 'offering_id', 'job_id', 'hotel_id', 'flight_id', 'vehicle_id', 'listing_id', 'store_id', 'program_id', 'destination_id', 'app_id']]
    isArchived: NotRequired[bool]
    idempotencyKey: str

class SaveCatalogResult(TypedDict):
    action: Literal['created', 'updated', 'unchanged', 'deleted']
    object: JsonValue
    replayed: bool
SaveCatalogError: TypeAlias = V3ToolErrorResponse

class Mapping1(TypedDict):
    eventIdField: NotRequired[str]
    eventTypeField: NotRequired[str]
    eventTimeField: NotRequired[str]
    userMatchFields: NotRequired[list[str]]
    valueField: NotRequired[str]
    currencyField: NotRequired[str]
    orderIdField: NotRequired[str]
    contentIdsField: NotRequired[str]
    consentField: NotRequired[str]
    dedupeStrategy: NotRequired[str]
    notes: NotRequired[str]

class SaveMeasurementSourceInput(TypedDict):
    advertiserId: str
    id: NotRequired[str]
    sourceType: NotRequired[Literal['event']]
    eventSourceId: NotRequired[str]
    name: NotRequired[str]
    eventTypes: NotRequired[list[Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']]]
    allowedDomains: NotRequired[list[str]]
    integrationPlatform: NotRequired[str]
    mapping: NotRequired[Mapping1]
    testEventCode: NotRequired[str]
    isArchived: NotRequired[bool]

class Object3(TypedDict):
    id: str
    sourceType: Literal['event']
    advertiserId: str
    eventSourceId: str

class Setup(TypedDict):
    snippetType: Literal['javascript', 'html', 'pixel_url', 'server_only']
    snippet: NotRequired[str]
    instructions: str

class SaveMeasurementSourceResult(TypedDict):
    action: Literal['created', 'updated', 'unchanged', 'archived', 'restored']
    object: Object3
    setup: NotRequired[Setup]
SaveMeasurementSourceError: TypeAlias = V3ToolErrorResponse
ValueCurrency: TypeAlias = str

class SaveEventSourceInput(TypedDict):
    advertiserId: str
    id: NotRequired[str]
    eventSourceId: NotRequired[str]
    name: NotRequired[str]
    eventTypes: NotRequired[list[Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']]]
    allowedDomains: NotRequired[list[str]]
    integrationPlatform: NotRequired[str]
    mapping: NotRequired[Mapping1]
    testEventCode: NotRequired[str]
    valueCurrencies: NotRequired[list[ValueCurrency] | None]
    actionSource: NotRequired[SaveEventSourceRequestEventSourceActionSource | None]
    surface: NotRequired[SaveEventSourceRequestEventSourceSurface | None]
    isArchived: NotRequired[bool]
    idempotencyKey: str

class Object4(TypedDict):
    id: str
    advertiserId: str
    eventSourceId: str

class SaveEventSourceResult(TypedDict):
    action: Literal['created', 'updated', 'unchanged', 'archived', 'restored']
    replayed: bool
    object: Object4
    setup: NotRequired[Setup]
SaveEventSourceError: TypeAlias = V3ToolErrorResponse

class SaveDimensionInput1(TypedDict):
    key: str
    name: SaveDimensionRequestSchema1
    valuesMode: SaveDimensionRequestSchema2
    appliesTo: SaveDimensionRequestSchema3
    retired: NotRequired[SaveDimensionRequestSchema6]
    values: NotRequired[SaveDimensionRequestSchema8]
    idempotencyKey: SaveDimensionRequestSchema13

class SaveDimensionInput2(TypedDict):
    id: str
    name: NotRequired[SaveDimensionRequestSchema1]
    valuesMode: NotRequired[SaveDimensionRequestSchema2]
    appliesTo: NotRequired[SaveDimensionRequestSchema3]
    retired: NotRequired[SaveDimensionRequestSchema6]
    values: NotRequired[SaveDimensionRequestSchema8]
    idempotencyKey: SaveDimensionRequestSchema13
SaveDimensionInput: TypeAlias = SaveDimensionInput1 | SaveDimensionInput2

class Usage(TypedDict):
    advertiser: float
    campaign: float
    material: float
    creative_asset: float
    creative: float

class Value2(TypedDict):
    value: str
    name: str
    retired: bool

class Object5(TypedDict):
    id: str
    key: str
    name: str
    valuesMode: Literal['open', 'governed']
    appliesTo: list[Literal['advertiser', 'campaign', 'material', 'creative_asset', 'creative']]
    usage: Usage
    retired: bool
    values: list[Value2]
    createdAt: str
    updatedAt: str

class SaveDimensionResult(TypedDict):
    action: Literal['created', 'updated', 'unchanged']
    object: Object5
    replayed: bool
SaveDimensionError: TypeAlias = V3ToolErrorResponse

class SavePropertyListInput(TypedDict):
    advertiserId: str
    propertyListId: NotRequired[str]
    name: NotRequired[str]
    purpose: NotRequired[Literal['include', 'exclude']]
    domains: NotRequired[list[Domain]]
    identifiers: NotRequired[list[SavePropertyListRequestPropertyListIdentifier]]
    filters: NotRequired[SavePropertyListRequestPropertyListFilters | None]
    check: NotRequired[bool]
    isArchived: NotRequired[bool]

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
    value: str
    valueTruncated: NotRequired[Literal[True]]

class IdentifierPage(TypedDict):
    category: Literal['all', 'unresolved', 'registered']
    offset: int
    returned: int
    total: int
    items: list[Item2]
    nextOffset: NotRequired[int]
    valueTruncatedCount: NotRequired[int]

class Object6(TypedDict):
    id: str
    name: str
    purpose: Literal['include', 'exclude']
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
    object: Object6

class SavePropertyListResult3(TypedDict):
    action: Literal['archived']
    propertyListId: str
SavePropertyListResult: TypeAlias = SavePropertyListResult1 | SavePropertyListResult2 | SavePropertyListResult3
SavePropertyListError: TypeAlias = V3ToolErrorResponse
CampaignId: TypeAlias = str

class FormatOptionRef(TypedDict):
    scope: Literal['publisher']
    publisher_domain: str
    format_option_id: str

class FormatOptionRef1(TypedDict):
    scope: Literal['product']
    format_option_id: str

class Asset(TypedDict):
    url: NotRequired[SaveCreativeRequestSchema33]
    dataUrl: NotRequired[str]
    assetType: Literal['IMAGE', 'VIDEO', 'AUDIO', 'HTML', 'TEXT', 'VAST']
    contentType: NotRequired[str]
    label: NotRequired[str]
    makePrimary: NotRequired[bool]

class SourceAssets(TypedDict):
    assetRef: str
    slot: NotRequired[SaveCreativeRequestSchema49]
    label: NotRequired[SaveCreativeRequestSchema51]
    makePrimary: NotRequired[SaveCreativeRequestSchema53]

class SourceAssets1(TypedDict):
    assetId: str
    slot: NotRequired[SaveCreativeRequestSchema49]
    label: NotRequired[SaveCreativeRequestSchema51]
    makePrimary: NotRequired[SaveCreativeRequestSchema53]

class Component(TypedDict):
    slot: str
    text: NotRequired[str]
    url: NotRequired[SaveCreativeRequestSchema33]

class Social(TypedDict):
    headline: NotRequired[str]
    body: NotRequired[str]
    description: NotRequired[str]
    callToAction: NotRequired[str]
    displayName: NotRequired[str]
    components: NotRequired[list[Component]]

class SaveCreativeInput(TypedDict):
    creativeId: NotRequired[str]
    campaignId: NotRequired[str]
    campaignIds: NotRequired[list[CampaignId]]
    advertiserId: NotRequired[str]
    mode: NotRequired[Literal['draft', 'complete']]
    expectedRevision: NotRequired[int]
    name: NotRequired[str]
    message: NotRequired[str]
    formatKind: NotRequired[Literal['image', 'html5', 'display_tag', 'image_carousel', 'video_hosted', 'video_vast', 'audio_hosted', 'audio_vast', 'audio_daast', 'sponsored_placement', 'native_in_feed', 'responsive_creative', 'agent_placement', 'seller_rendered_stateful_display', 'coordinated_placements', 'custom']]
    formatParams: NotRequired[dict[str, JsonValue]]
    formatOptionRef: NotRequired[FormatOptionRef | FormatOptionRef1]
    creativeFormatId: NotRequired[str]
    assets: NotRequired[list[Asset]]
    sourceAssetRef: NotRequired[str]
    sourceAssets: NotRequired[list[SourceAssets | SourceAssets1]]
    clickUrl: NotRequired[str]
    macroAdditions: NotRequired[list[MacroAddition]]
    social: NotRequired[Social]
    tags: NotRequired[list[Tag]]
    labels: NotRequired[dict[str, list[Label]]]
    isArchived: NotRequired[bool]
    idempotencyKey: NotRequired[str]

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
    engineId: str
    connectionId: str

class Rights1(TypedDict):
    status: NotRequired[Literal['unknown', 'owned', 'licensed', 'restricted', 'expired', 'inherited']]
    usage: NotRequired[SaveCreativeSessionRequestSchema25]
    expires_at: NotRequired[SaveCreativeSessionRequestSchema27]
    notes: NotRequired[SaveCreativeSessionRequestSchema29]
    source_asset_id: NotRequired[str]

class Provenance1(TypedDict):
    method: NotRequired[Literal['background_removal', 'thumbnail_generation', 'original_has_alpha', 'render_crop']]
    provider: NotRequired[str]
    source_checksum: NotRequired[str]
    created_at: NotRequired[str]

class Check1(TypedDict):
    code: str
    status: Literal['pass', 'warn', 'fail']
    detail: NotRequired[str]

class Quality(TypedDict):
    status: Literal['approved', 'needs_review', 'failed']
    checks: NotRequired[list[Check1]]

class Rendition(TypedDict):
    asset_id: str
    parent_asset_id: str
    rendition_type: Literal['transparent_cutout', 'thumbnail', 'render_crop']
    label: str
    url: str
    source: NotRequired[SaveCreativeSessionRequestSchema17]
    role: NotRequired[SaveCreativeSessionRequestSchema18]
    mime_type: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    alpha: NotRequired[bool]
    locked_asset: NotRequired[bool]
    can_transform: NotRequired[bool]
    rights: NotRequired[Rights1]
    provenance: NotRequired[Provenance1]
    quality: NotRequired[Quality]

class SaveCreativeSessionInput2(TypedDict):
    operation: Literal['select_output']
    campaignId: str
    sessionId: str
    variantId: str
    expectedRevision: int
    idempotencyKey: NotRequired[str]

class SaveCreativeSessionInput3(TypedDict):
    operation: Literal['approve_output']
    campaignId: str
    sessionId: str
    variantId: str
    expectedRevision: int
    idempotencyKey: NotRequired[str]

class SaveCreativeSessionInput4(TypedDict):
    operation: Literal['finalize_approved_output']
    campaignId: str
    sessionId: str
    approvedVariantId: str
    approvedSessionRevision: int
    name: NotRequired[str]
    message: NotRequired[str]

class SaveCreativeSessionInput5(TypedDict):
    operation: Literal['promote_approved_output']
    campaignId: str
    sessionId: str
    advertiserId: str
    variantId: str
    sessionRevision: int
    outputHash: str
    idempotencyKey: str

class Arguments6(TypedDict):
    campaignId: str
    sessionId: str
    actionKey: str
    expectedRevision: int
    sessionGeneration: str

class NextGenerateVariants(TypedDict):
    tool: Literal['generate_variants']
    arguments: Arguments6

class SaveCreativeSessionResult1(TypedDict):
    nextGenerateVariants: NotRequired[NextGenerateVariants]
    session: SaveCreativeSessionSuccessSchema0
    sessionTruncated: NotRequired[SaveCreativeSessionSuccessSchema1]
    sessionOmitted: NotRequired[SaveCreativeSessionSuccessSchema2]
    revision: SaveCreativeSessionSuccessSchema3
    sessionGeneration: NotRequired[SaveCreativeSessionSuccessSchema4]
    gallery: NotRequired[SaveCreativeSessionSuccessSchema6]
    operation: Literal['saved_draft']

class NextGenerateVariants1(TypedDict):
    tool: Literal['generate_variants']
    arguments: Arguments6

class SaveCreativeSessionResult2(TypedDict):
    nextGenerateVariants: NotRequired[NextGenerateVariants1]
    session: SaveCreativeSessionSuccessSchema0
    sessionTruncated: NotRequired[SaveCreativeSessionSuccessSchema1]
    sessionOmitted: NotRequired[SaveCreativeSessionSuccessSchema2]
    revision: SaveCreativeSessionSuccessSchema3
    sessionGeneration: NotRequired[SaveCreativeSessionSuccessSchema4]
    gallery: NotRequired[SaveCreativeSessionSuccessSchema6]
    operation: Literal['selected_output']

class NextGenerateVariants2(TypedDict):
    tool: Literal['generate_variants']
    arguments: Arguments6

class SaveCreativeSessionResult3(TypedDict):
    nextGenerateVariants: NotRequired[NextGenerateVariants2]
    session: SaveCreativeSessionSuccessSchema0
    sessionTruncated: NotRequired[SaveCreativeSessionSuccessSchema1]
    sessionOmitted: NotRequired[SaveCreativeSessionSuccessSchema2]
    revision: SaveCreativeSessionSuccessSchema3
    sessionGeneration: NotRequired[SaveCreativeSessionSuccessSchema4]
    gallery: NotRequired[SaveCreativeSessionSuccessSchema6]
    operation: Literal['approved_output']

class NextGenerateVariants3(TypedDict):
    tool: Literal['generate_variants']
    arguments: Arguments6

class SaveCreativeSessionResult4(TypedDict):
    nextGenerateVariants: NotRequired[NextGenerateVariants3]
    session: SaveCreativeSessionSuccessSchema0
    sessionTruncated: NotRequired[SaveCreativeSessionSuccessSchema1]
    sessionOmitted: NotRequired[SaveCreativeSessionSuccessSchema2]
    revision: SaveCreativeSessionSuccessSchema3
    sessionGeneration: NotRequired[SaveCreativeSessionSuccessSchema4]
    gallery: NotRequired[SaveCreativeSessionSuccessSchema6]
    operation: Literal['finalized_output']

class NextGenerateVariants4(TypedDict):
    tool: Literal['generate_variants']
    arguments: Arguments6

class SaveCreativeSessionResult5(TypedDict):
    nextGenerateVariants: NotRequired[NextGenerateVariants4]
    operation: Literal['promoted_approved_output']
    assetUid: str
    revisionUid: str
    sha256: str
    receiptUid: str
SaveCreativeSessionResult: TypeAlias = SaveCreativeSessionResult1 | SaveCreativeSessionResult2 | SaveCreativeSessionResult3 | SaveCreativeSessionResult4 | SaveCreativeSessionResult5
SaveCreativeSessionError: TypeAlias = V3ToolErrorResponse

class GenerateVariantsInput1(TypedDict):
    campaignId: GenerateVariantsRequestSchema0
    sessionId: GenerateVariantsRequestSchema1
    actionKey: GenerateVariantsRequestSchema2
    expectedRevision: GenerateVariantsRequestSchema3
    sessionGeneration: GenerateVariantsRequestSchema4

class GenerateVariantsInput2(TypedDict):
    campaignId: GenerateVariantsRequestSchema0
    sessionId: GenerateVariantsRequestSchema1
    actionKey: GenerateVariantsRequestSchema2
    expectedRevision: GenerateVariantsRequestSchema3
    sessionGeneration: GenerateVariantsRequestSchema4
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

class Arguments11(TypedDict):
    kind: Literal['creative_session']
    id: str
    sourceId: str

class Poll(TypedDict):
    tool: Literal['get']
    arguments: Arguments11

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
    revision: int
    sessionGeneration: NotRequired[str]
    variants: list[Variant1]
    selectedVariantId: NotRequired[str]
    approvedVariantId: NotRequired[str]
    approvedSessionRevision: NotRequired[int]
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
    system: Literal['nielsen_dma', 'uk_itl1', 'uk_itl2', 'eurostat_nuts2', 'custom']
    values: list[str]

class GeoMetrosExcludeItem(TypedDict):
    system: Literal['nielsen_dma', 'uk_itl1', 'uk_itl2', 'eurostat_nuts2', 'custom']
    values: list[str]

class GeoPostalAreas(TypedDict):
    country: Literal['US']
    system: Literal['zip', 'zip_plus_four']
    values: list[str]

class GeoPostalAreas1(TypedDict):
    country: Literal['GB']
    system: Literal['outward', 'full']
    values: list[str]

class GeoPostalAreas2(TypedDict):
    country: Literal['CA']
    system: Literal['full', 'fsa']
    values: list[str]

class GeoPostalAreas3(TypedDict):
    country: Literal['DE', 'CH', 'AT']
    system: Literal['plz']
    values: list[str]

class GeoPostalAreas4(TypedDict):
    country: Literal['FR']
    system: Literal['code_postal']
    values: list[str]

class GeoPostalAreas5(TypedDict):
    country: Literal['AU']
    system: Literal['postcode']
    values: list[str]

class GeoPostalAreas6(TypedDict):
    country: Literal['BR']
    system: Literal['cep']
    values: list[str]

class GeoPostalAreas7(TypedDict):
    country: Literal['IN']
    system: Literal['pin']
    values: list[str]

class GeoPostalAreas8(TypedDict):
    country: Literal['ZA']
    system: Literal['postal_code']
    values: list[str]

class GeoPostalAreas9(TypedDict):
    country: str
    system: Literal['postal_code', 'custom']
    values: list[str]

class GeoPostalAreas10(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class GeoPostalAreasExclude(TypedDict):
    country: Literal['US']
    system: Literal['zip', 'zip_plus_four']
    values: list[str]

class GeoPostalAreasExclude1(TypedDict):
    country: Literal['GB']
    system: Literal['outward', 'full']
    values: list[str]

class GeoPostalAreasExclude2(TypedDict):
    country: Literal['CA']
    system: Literal['full', 'fsa']
    values: list[str]

class GeoPostalAreasExclude3(TypedDict):
    country: Literal['DE', 'CH', 'AT']
    system: Literal['plz']
    values: list[str]

class GeoPostalAreasExclude4(TypedDict):
    country: Literal['FR']
    system: Literal['code_postal']
    values: list[str]

class GeoPostalAreasExclude5(TypedDict):
    country: Literal['AU']
    system: Literal['postcode']
    values: list[str]

class GeoPostalAreasExclude6(TypedDict):
    country: Literal['BR']
    system: Literal['cep']
    values: list[str]

class GeoPostalAreasExclude7(TypedDict):
    country: Literal['IN']
    system: Literal['pin']
    values: list[str]

class GeoPostalAreasExclude8(TypedDict):
    country: Literal['ZA']
    system: Literal['postal_code']
    values: list[str]

class GeoPostalAreasExclude9(TypedDict):
    country: str
    system: Literal['postal_code', 'custom']
    values: list[str]

class GeoPostalAreasExclude10(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]
Value3: TypeAlias = str

class GeoPlace1(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]
    country: NotRequired[JsonValue]
    system_version: NotRequired[JsonValue]
    place_type: NotRequired[JsonValue]
    value_labels: NotRequired[JsonValue]
    ext: NotRequired[JsonValue]

class GeoPlace2(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value3]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

class GeoPlace3(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlace: TypeAlias = GeoPlace3

class GeoPlacesExcludeItem1(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]
    country: NotRequired[JsonValue]
    system_version: NotRequired[JsonValue]
    place_type: NotRequired[JsonValue]
    value_labels: NotRequired[JsonValue]
    ext: NotRequired[JsonValue]

class GeoPlacesExcludeItem2(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value3]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

class GeoPlacesExcludeItem3(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlacesExcludeItem: TypeAlias = GeoPlacesExcludeItem3

class Age7(TypedDict):
    min: NotRequired[int]
    max: NotRequired[int]
    include_unknown: bool
    accepted_bases: NotRequired[list[Literal['verified', 'declared', 'inferred']]]
    accepted_verification_methods: NotRequired[list[Literal['facial_age_estimation', 'id_document', 'digital_id', 'credit_card', 'world_id']]]

class Demographics2(TypedDict):
    age: Age7

class Suppress(TypedDict):
    interval: int
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']

class Window3(TypedDict):
    interval: int
    unit: Literal['seconds', 'minutes', 'hours', 'days', 'campaign']

class FrequencyCap11(TypedDict):
    suppress: JsonValue
    suppress_minutes: NotRequired[JsonValue]
    max_impressions: NotRequired[JsonValue]
    per: NotRequired[JsonValue]
    window: NotRequired[JsonValue]

class FrequencyCap12(TypedDict):
    window: JsonValue
    max_impressions: JsonValue
    suppress: NotRequired[JsonValue]
    suppress_minutes: NotRequired[JsonValue]
    per: NotRequired[JsonValue]

class FrequencyCap13(TypedDict):
    max_impressions: JsonValue
    suppress: NotRequired[JsonValue]
    suppress_minutes: NotRequired[JsonValue]
    per: NotRequired[JsonValue]
    window: NotRequired[JsonValue]

class FrequencyCap14(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap15(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap16(TypedDict):
    window: NotRequired[Window3]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]

class FrequencyCap17(TypedDict):
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap18(TypedDict):
    window: NotRequired[Window3]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
FrequencyCap1: TypeAlias = FrequencyCap15 | FrequencyCap16 | FrequencyCap17 | FrequencyCap18

class PropertyList(TypedDict):
    agent_url: str
    list_id: str
    auth_token: NotRequired[str]

class PropertyListExclude(TypedDict):
    agent_url: str
    list_id: str
    auth_token: NotRequired[str]

class CollectionList(TypedDict):
    agent_url: str
    list_id: str
    auth_token: NotRequired[str]

class CollectionListExclude(TypedDict):
    agent_url: str
    list_id: str
    auth_token: NotRequired[str]

class StoreCatchment(TypedDict):
    catalog_id: str
    store_ids: NotRequired[list[str]]
    catchment_ids: NotRequired[list[str]]

class GeoProximityItem1(TypedDict):
    lat: NotRequired[float]
    lng: NotRequired[float]
    label: NotRequired[str]
    travel_time: NotRequired[TravelTime]
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    radius: NotRequired[Radius]
    geometry: NotRequired[Geometry1]
    ext: NotRequired[dict[str, JsonValue]]
LanguageItem2: TypeAlias = str

class KeywordTarget(TypedDict):
    keyword: str
    match_type: Literal['broad', 'phrase', 'exact']
    bid_price: NotRequired[float]

class NegativeKeyword(TypedDict):
    keyword: str
    match_type: Literal['broad', 'phrase', 'exact']

class Signals(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['binary']
    value: Literal[True]

class Signals1(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['categorical']
    values: list[str]

class Signals2(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['numeric']
    min_value: NotRequired[float]
    max_value: NotRequired[float]

class Group(TypedDict):
    operator: Literal['any', 'none']
    signals: list[Signals | Signals1 | Signals2]

class SignalTargetingGroups(TypedDict):
    operator: Literal['all']
    groups: list[Group]

class TargetingOverlay1(TypedDict):
    geo_metros: NotRequired[list[GeoMetro1]]
    geo_metros_exclude: NotRequired[list[GeoMetrosExcludeItem]]
    geo_postal_areas: NotRequired[list[GeoPostalAreas | GeoPostalAreas1 | GeoPostalAreas2 | GeoPostalAreas3 | GeoPostalAreas4 | GeoPostalAreas5 | GeoPostalAreas6 | GeoPostalAreas7 | GeoPostalAreas8 | GeoPostalAreas9 | GeoPostalAreas10]]
    geo_postal_areas_exclude: NotRequired[list[GeoPostalAreasExclude | GeoPostalAreasExclude1 | GeoPostalAreasExclude2 | GeoPostalAreasExclude3 | GeoPostalAreasExclude4 | GeoPostalAreasExclude5 | GeoPostalAreasExclude6 | GeoPostalAreasExclude7 | GeoPostalAreasExclude8 | GeoPostalAreasExclude9 | GeoPostalAreasExclude10]]
    geo_places: NotRequired[list[GeoPlace]]
    geo_places_exclude: NotRequired[list[GeoPlacesExcludeItem]]
    daypart_targets: NotRequired[list[DaypartTarget]]
    axe_include_segment: NotRequired[str]
    axe_exclude_segment: NotRequired[str]
    audience_include: NotRequired[list[str]]
    audience_exclude: NotRequired[list[str]]
    demographics: NotRequired[Demographics2]
    frequency_cap: NotRequired[FrequencyCap1]
    property_list: NotRequired[PropertyList]
    property_list_exclude: NotRequired[PropertyListExclude]
    collection_list: NotRequired[CollectionList]
    collection_list_exclude: NotRequired[CollectionListExclude]
    placement_selection: NotRequired[dict[str, JsonValue]]
    collection_selection: NotRequired[dict[str, JsonValue]]
    age_restriction: NotRequired[AgeRestriction]
    device_platform: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    device_platform_exclude: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    device_type: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    device_type_exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    browser: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    browser_exclude: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    store_catchments: NotRequired[list[StoreCatchment]]
    geo_proximity: NotRequired[list[GeoProximityItem1]]
    language: NotRequired[list[LanguageItem2]]
    keyword_targets: NotRequired[list[KeywordTarget]]
    negative_keywords: NotRequired[list[NegativeKeyword]]
    signal_targeting_groups: NotRequired[SignalTargetingGroups]
    geo_countries: NotRequired[list[str]]
    geo_countries_exclude: NotRequired[list[str]]
    geo_regions: NotRequired[list[str]]
    geo_regions_exclude: NotRequired[list[str]]

class Vendor1(TypedDict):
    domain: str
    brand_id: NotRequired[str]

class PerformanceStandard(TypedDict):
    metric: Literal['viewability', 'ivt', 'completion_rate', 'brand_safety', 'attention_score']
    threshold: float
    standard: NotRequired[Literal['MRC', 'GroupM']]
    vendor: NotRequired[Vendor1]

class Product(TypedDict):
    productId: str
    selectionId: NotRequired[str]
    inventorySourceId: NotRequired[str]
    salesAgentId: NotRequired[str]
    pricingOptionId: NotRequired[str]
    budget: NotRequired[float]
    bidPrice: NotRequired[float]
    targetingOverlay: NotRequired[TargetingOverlay1]
    performanceStandards: NotRequired[list[PerformanceStandard] | None]
    pixelId: NotRequired[str]
    remove: NotRequired[bool]
    lineItemRef: NotRequired[str]

class Budget8(TypedDict):
    total: float
    currency: str

class BudgetAllocation(TypedDict):
    mode: Literal['fixed']

class TargetFrequency(TypedDict):
    min: NotRequired[int]
    max: NotRequired[int]
    window: SaveMediaBuyRequestSchema111

class OptimizationGoals(TypedDict):
    kind: Literal['metric']
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    reach_unit: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    target_frequency: NotRequired[TargetFrequency]
    view_duration_seconds: NotRequired[SaveMediaBuyRequestSchema115]
    target: NotRequired[SaveMediaBuyRequestSchema118 | SaveMediaBuyRequestSchema120]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class EventSource1(TypedDict):
    event_source_id: str
    event_type: Literal['page_view', 'view_content', 'select_content', 'select_item', 'search', 'share', 'add_to_cart', 'remove_from_cart', 'viewed_cart', 'add_to_wishlist', 'initiate_checkout', 'add_payment_info', 'purchase', 'refund', 'lead', 'qualify_lead', 'close_convert_lead', 'disqualify_lead', 'complete_registration', 'subscribe', 'follow', 'content_view', 'watch_milestone', 'start_trial', 'app_install', 'app_launch', 'contact', 'schedule', 'donate', 'submit_application', 'custom']
    custom_event_name: NotRequired[str]
    value_field: NotRequired[str]
    value_factor: NotRequired[float]

class Target5(TypedDict):
    kind: Literal['per_ad_spend']
    value: SaveMediaBuyRequestSchema115
    strength: NotRequired[Literal['floor', 'target']]

class Target6(TypedDict):
    kind: Literal['maximize_value']

class AttributionWindow(TypedDict):
    post_click: NotRequired[SaveMediaBuyRequestSchema111]
    post_view: NotRequired[SaveMediaBuyRequestSchema111]
    model: NotRequired[Literal['last_touch', 'first_touch', 'linear', 'time_decay', 'data_driven']]

class OptimizationGoals1(TypedDict):
    kind: Literal['event']
    event_sources: list[EventSource1]
    target: NotRequired[SaveMediaBuyRequestSchema118 | Target5 | Target6]
    attribution_window: NotRequired[AttributionWindow]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class OptimizationGoals2(TypedDict):
    kind: Literal['vendor_metric']
    vendor: Vendor1
    metric_id: str
    target: NotRequired[SaveMediaBuyRequestSchema118 | SaveMediaBuyRequestSchema120]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class BudgetAllocation1(TypedDict):
    mode: Literal['seller_optimized']
    optimization_goals: list[OptimizationGoals | OptimizationGoals1 | OptimizationGoals2]

class SaveMediaBuyInput4(TypedDict):
    mediaBuyId: NotRequired[str]
    fromProposalId: NotRequired[str]
    campaignId: NotRequired[str]
    channelGroupId: NotRequired[str]
    sellerId: NotRequired[str]
    products: NotRequired[list[Product]]
    budget: NotRequired[Budget8]
    budgetAllocation: NotRequired[BudgetAllocation | BudgetAllocation1]
    flight: NotRequired[Flight]
    isArchived: NotRequired[bool]
    isPaused: NotRequired[bool]
    idempotencyKey: str

class GeoPostalAreas11(TypedDict):
    country: Literal['US']
    system: Literal['zip', 'zip_plus_four']
    values: list[str]

class GeoPostalAreas12(TypedDict):
    country: Literal['GB']
    system: Literal['outward', 'full']
    values: list[str]

class GeoPostalAreas13(TypedDict):
    country: Literal['CA']
    system: Literal['full', 'fsa']
    values: list[str]

class GeoPostalAreas14(TypedDict):
    country: Literal['DE', 'CH', 'AT']
    system: Literal['plz']
    values: list[str]

class GeoPostalAreas15(TypedDict):
    country: Literal['FR']
    system: Literal['code_postal']
    values: list[str]

class GeoPostalAreas16(TypedDict):
    country: Literal['AU']
    system: Literal['postcode']
    values: list[str]

class GeoPostalAreas17(TypedDict):
    country: Literal['BR']
    system: Literal['cep']
    values: list[str]

class GeoPostalAreas18(TypedDict):
    country: Literal['IN']
    system: Literal['pin']
    values: list[str]

class GeoPostalAreas19(TypedDict):
    country: Literal['ZA']
    system: Literal['postal_code']
    values: list[str]

class GeoPostalAreas20(TypedDict):
    country: str
    system: Literal['postal_code', 'custom']
    values: list[str]

class GeoPostalAreas21(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class GeoPostalAreasExclude11(TypedDict):
    country: Literal['US']
    system: Literal['zip', 'zip_plus_four']
    values: list[str]

class GeoPostalAreasExclude12(TypedDict):
    country: Literal['GB']
    system: Literal['outward', 'full']
    values: list[str]

class GeoPostalAreasExclude13(TypedDict):
    country: Literal['CA']
    system: Literal['full', 'fsa']
    values: list[str]

class GeoPostalAreasExclude14(TypedDict):
    country: Literal['DE', 'CH', 'AT']
    system: Literal['plz']
    values: list[str]

class GeoPostalAreasExclude15(TypedDict):
    country: Literal['FR']
    system: Literal['code_postal']
    values: list[str]

class GeoPostalAreasExclude16(TypedDict):
    country: Literal['AU']
    system: Literal['postcode']
    values: list[str]

class GeoPostalAreasExclude17(TypedDict):
    country: Literal['BR']
    system: Literal['cep']
    values: list[str]

class GeoPostalAreasExclude18(TypedDict):
    country: Literal['IN']
    system: Literal['pin']
    values: list[str]

class GeoPostalAreasExclude19(TypedDict):
    country: Literal['ZA']
    system: Literal['postal_code']
    values: list[str]

class GeoPostalAreasExclude20(TypedDict):
    country: str
    system: Literal['postal_code', 'custom']
    values: list[str]

class GeoPostalAreasExclude21(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class GeoPlace41(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]
    country: NotRequired[JsonValue]
    system_version: NotRequired[JsonValue]
    place_type: NotRequired[JsonValue]
    value_labels: NotRequired[JsonValue]
    ext: NotRequired[JsonValue]

class GeoPlace42(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value3]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

class GeoPlace43(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlace4: TypeAlias = GeoPlace43

class GeoPlacesExcludeItem41(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]
    country: NotRequired[JsonValue]
    system_version: NotRequired[JsonValue]
    place_type: NotRequired[JsonValue]
    value_labels: NotRequired[JsonValue]
    ext: NotRequired[JsonValue]

class GeoPlacesExcludeItem42(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value3]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

class GeoPlacesExcludeItem43(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlacesExcludeItem4: TypeAlias = GeoPlacesExcludeItem43

class Demographics3(TypedDict):
    age: Age7

class FrequencyCap21(TypedDict):
    suppress: JsonValue
    suppress_minutes: NotRequired[JsonValue]
    max_impressions: NotRequired[JsonValue]
    per: NotRequired[JsonValue]
    window: NotRequired[JsonValue]

class FrequencyCap22(TypedDict):
    window: JsonValue
    max_impressions: JsonValue
    suppress: NotRequired[JsonValue]
    suppress_minutes: NotRequired[JsonValue]
    per: NotRequired[JsonValue]

class FrequencyCap23(TypedDict):
    max_impressions: JsonValue
    suppress: NotRequired[JsonValue]
    suppress_minutes: NotRequired[JsonValue]
    per: NotRequired[JsonValue]
    window: NotRequired[JsonValue]

class FrequencyCap24(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap25(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap26(TypedDict):
    window: NotRequired[Window3]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]

class FrequencyCap27(TypedDict):
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap28(TypedDict):
    window: NotRequired[Window3]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
FrequencyCap2: TypeAlias = FrequencyCap25 | FrequencyCap26 | FrequencyCap27 | FrequencyCap28

class GeoProximityItem2(TypedDict):
    lat: NotRequired[float]
    lng: NotRequired[float]
    label: NotRequired[str]
    travel_time: NotRequired[TravelTime]
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    radius: NotRequired[Radius]
    geometry: NotRequired[Geometry1]
    ext: NotRequired[dict[str, JsonValue]]

class Signals3(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['binary']
    value: Literal[True]

class Signals4(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['categorical']
    values: list[str]

class Signals5(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['numeric']
    min_value: NotRequired[float]
    max_value: NotRequired[float]

class Group1(TypedDict):
    operator: Literal['any', 'none']
    signals: list[Signals3 | Signals4 | Signals5]

class SignalTargetingGroups1(TypedDict):
    operator: Literal['all']
    groups: list[Group1]

class TargetingOverlay2(TypedDict):
    geo_metros: NotRequired[list[GeoMetro1]]
    geo_metros_exclude: NotRequired[list[GeoMetrosExcludeItem]]
    geo_postal_areas: NotRequired[list[GeoPostalAreas11 | GeoPostalAreas12 | GeoPostalAreas13 | GeoPostalAreas14 | GeoPostalAreas15 | GeoPostalAreas16 | GeoPostalAreas17 | GeoPostalAreas18 | GeoPostalAreas19 | GeoPostalAreas20 | GeoPostalAreas21]]
    geo_postal_areas_exclude: NotRequired[list[GeoPostalAreasExclude11 | GeoPostalAreasExclude12 | GeoPostalAreasExclude13 | GeoPostalAreasExclude14 | GeoPostalAreasExclude15 | GeoPostalAreasExclude16 | GeoPostalAreasExclude17 | GeoPostalAreasExclude18 | GeoPostalAreasExclude19 | GeoPostalAreasExclude20 | GeoPostalAreasExclude21]]
    geo_places: NotRequired[list[GeoPlace4]]
    geo_places_exclude: NotRequired[list[GeoPlacesExcludeItem4]]
    daypart_targets: NotRequired[list[DaypartTarget]]
    axe_include_segment: NotRequired[str]
    axe_exclude_segment: NotRequired[str]
    audience_include: NotRequired[list[str]]
    audience_exclude: NotRequired[list[str]]
    demographics: NotRequired[Demographics3]
    frequency_cap: NotRequired[FrequencyCap2]
    property_list: NotRequired[PropertyList]
    property_list_exclude: NotRequired[PropertyListExclude]
    collection_list: NotRequired[CollectionList]
    collection_list_exclude: NotRequired[CollectionListExclude]
    placement_selection: NotRequired[dict[str, JsonValue]]
    collection_selection: NotRequired[dict[str, JsonValue]]
    age_restriction: NotRequired[AgeRestriction]
    device_platform: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    device_platform_exclude: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    device_type: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    device_type_exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    browser: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    browser_exclude: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    store_catchments: NotRequired[list[StoreCatchment]]
    geo_proximity: NotRequired[list[GeoProximityItem2]]
    language: NotRequired[list[LanguageItem2]]
    keyword_targets: NotRequired[list[KeywordTarget]]
    negative_keywords: NotRequired[list[NegativeKeyword]]
    signal_targeting_groups: NotRequired[SignalTargetingGroups1]
    geo_countries: NotRequired[list[str]]
    geo_countries_exclude: NotRequired[list[str]]
    geo_regions: NotRequired[list[str]]
    geo_regions_exclude: NotRequired[list[str]]

class PerformanceStandard1(TypedDict):
    metric: Literal['viewability', 'ivt', 'completion_rate', 'brand_safety', 'attention_score']
    threshold: float
    standard: NotRequired[Literal['MRC', 'GroupM']]
    vendor: NotRequired[Vendor1]

class Product1(TypedDict):
    productId: str
    selectionId: NotRequired[str]
    inventorySourceId: NotRequired[str]
    salesAgentId: NotRequired[str]
    pricingOptionId: NotRequired[str]
    budget: NotRequired[float]
    bidPrice: NotRequired[float]
    targetingOverlay: NotRequired[TargetingOverlay2]
    performanceStandards: NotRequired[list[PerformanceStandard1] | None]
    pixelId: NotRequired[str]
    remove: NotRequired[bool]
    lineItemRef: NotRequired[str]

class BudgetAllocation2(TypedDict):
    mode: Literal['fixed']

class OptimizationGoals3(TypedDict):
    kind: Literal['metric']
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    reach_unit: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    target_frequency: NotRequired[TargetFrequency]
    view_duration_seconds: NotRequired[SaveMediaBuyRequestSchema115]
    target: NotRequired[SaveMediaBuyRequestSchema118 | SaveMediaBuyRequestSchema120]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class Target7(TypedDict):
    kind: Literal['per_ad_spend']
    value: SaveMediaBuyRequestSchema115
    strength: NotRequired[Literal['floor', 'target']]

class Target8(TypedDict):
    kind: Literal['maximize_value']

class OptimizationGoals4(TypedDict):
    kind: Literal['event']
    event_sources: list[EventSource1]
    target: NotRequired[SaveMediaBuyRequestSchema118 | Target7 | Target8]
    attribution_window: NotRequired[AttributionWindow]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class OptimizationGoals5(TypedDict):
    kind: Literal['vendor_metric']
    vendor: Vendor1
    metric_id: str
    target: NotRequired[SaveMediaBuyRequestSchema118 | SaveMediaBuyRequestSchema120]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class BudgetAllocation3(TypedDict):
    mode: Literal['seller_optimized']
    optimization_goals: list[OptimizationGoals3 | OptimizationGoals4 | OptimizationGoals5]

class SaveMediaBuyInput5(TypedDict):
    mediaBuyId: NotRequired[str]
    fromProposalId: NotRequired[str]
    campaignId: NotRequired[str]
    channelGroupId: NotRequired[str]
    sellerId: NotRequired[str]
    products: NotRequired[list[Product1]]
    budget: NotRequired[Budget8]
    budgetAllocation: NotRequired[BudgetAllocation2 | BudgetAllocation3]
    flight: NotRequired[Flight]
    isArchived: NotRequired[bool]
    isPaused: NotRequired[bool]
    idempotencyKey: str

class GeoPostalAreas22(TypedDict):
    country: Literal['US']
    system: Literal['zip', 'zip_plus_four']
    values: list[str]

class GeoPostalAreas23(TypedDict):
    country: Literal['GB']
    system: Literal['outward', 'full']
    values: list[str]

class GeoPostalAreas24(TypedDict):
    country: Literal['CA']
    system: Literal['full', 'fsa']
    values: list[str]

class GeoPostalAreas25(TypedDict):
    country: Literal['DE', 'CH', 'AT']
    system: Literal['plz']
    values: list[str]

class GeoPostalAreas26(TypedDict):
    country: Literal['FR']
    system: Literal['code_postal']
    values: list[str]

class GeoPostalAreas27(TypedDict):
    country: Literal['AU']
    system: Literal['postcode']
    values: list[str]

class GeoPostalAreas28(TypedDict):
    country: Literal['BR']
    system: Literal['cep']
    values: list[str]

class GeoPostalAreas29(TypedDict):
    country: Literal['IN']
    system: Literal['pin']
    values: list[str]

class GeoPostalAreas30(TypedDict):
    country: Literal['ZA']
    system: Literal['postal_code']
    values: list[str]

class GeoPostalAreas31(TypedDict):
    country: str
    system: Literal['postal_code', 'custom']
    values: list[str]

class GeoPostalAreas32(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class GeoPostalAreasExclude22(TypedDict):
    country: Literal['US']
    system: Literal['zip', 'zip_plus_four']
    values: list[str]

class GeoPostalAreasExclude23(TypedDict):
    country: Literal['GB']
    system: Literal['outward', 'full']
    values: list[str]

class GeoPostalAreasExclude24(TypedDict):
    country: Literal['CA']
    system: Literal['full', 'fsa']
    values: list[str]

class GeoPostalAreasExclude25(TypedDict):
    country: Literal['DE', 'CH', 'AT']
    system: Literal['plz']
    values: list[str]

class GeoPostalAreasExclude26(TypedDict):
    country: Literal['FR']
    system: Literal['code_postal']
    values: list[str]

class GeoPostalAreasExclude27(TypedDict):
    country: Literal['AU']
    system: Literal['postcode']
    values: list[str]

class GeoPostalAreasExclude28(TypedDict):
    country: Literal['BR']
    system: Literal['cep']
    values: list[str]

class GeoPostalAreasExclude29(TypedDict):
    country: Literal['IN']
    system: Literal['pin']
    values: list[str]

class GeoPostalAreasExclude30(TypedDict):
    country: Literal['ZA']
    system: Literal['postal_code']
    values: list[str]

class GeoPostalAreasExclude31(TypedDict):
    country: str
    system: Literal['postal_code', 'custom']
    values: list[str]

class GeoPostalAreasExclude32(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class GeoPlace51(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]
    country: NotRequired[JsonValue]
    system_version: NotRequired[JsonValue]
    place_type: NotRequired[JsonValue]
    value_labels: NotRequired[JsonValue]
    ext: NotRequired[JsonValue]

class GeoPlace52(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value3]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

class GeoPlace53(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlace5: TypeAlias = GeoPlace53

class GeoPlacesExcludeItem51(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]
    country: NotRequired[JsonValue]
    system_version: NotRequired[JsonValue]
    place_type: NotRequired[JsonValue]
    value_labels: NotRequired[JsonValue]
    ext: NotRequired[JsonValue]

class GeoPlacesExcludeItem52(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value3]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

class GeoPlacesExcludeItem53(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlacesExcludeItem5: TypeAlias = GeoPlacesExcludeItem53

class Demographics4(TypedDict):
    age: Age7

class FrequencyCap31(TypedDict):
    suppress: JsonValue
    suppress_minutes: NotRequired[JsonValue]
    max_impressions: NotRequired[JsonValue]
    per: NotRequired[JsonValue]
    window: NotRequired[JsonValue]

class FrequencyCap32(TypedDict):
    window: JsonValue
    max_impressions: JsonValue
    suppress: NotRequired[JsonValue]
    suppress_minutes: NotRequired[JsonValue]
    per: NotRequired[JsonValue]

class FrequencyCap33(TypedDict):
    max_impressions: JsonValue
    suppress: NotRequired[JsonValue]
    suppress_minutes: NotRequired[JsonValue]
    per: NotRequired[JsonValue]
    window: NotRequired[JsonValue]

class FrequencyCap34(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap35(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap36(TypedDict):
    window: NotRequired[Window3]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]

class FrequencyCap37(TypedDict):
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap38(TypedDict):
    window: NotRequired[Window3]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
FrequencyCap3: TypeAlias = FrequencyCap35 | FrequencyCap36 | FrequencyCap37 | FrequencyCap38

class GeoProximityItem3(TypedDict):
    lat: NotRequired[float]
    lng: NotRequired[float]
    label: NotRequired[str]
    travel_time: NotRequired[TravelTime]
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    radius: NotRequired[Radius]
    geometry: NotRequired[Geometry1]
    ext: NotRequired[dict[str, JsonValue]]

class Signals6(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['binary']
    value: Literal[True]

class Signals7(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['categorical']
    values: list[str]

class Signals8(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['numeric']
    min_value: NotRequired[float]
    max_value: NotRequired[float]

class Group2(TypedDict):
    operator: Literal['any', 'none']
    signals: list[Signals6 | Signals7 | Signals8]

class SignalTargetingGroups2(TypedDict):
    operator: Literal['all']
    groups: list[Group2]

class TargetingOverlay3(TypedDict):
    geo_metros: NotRequired[list[GeoMetro1]]
    geo_metros_exclude: NotRequired[list[GeoMetrosExcludeItem]]
    geo_postal_areas: NotRequired[list[GeoPostalAreas22 | GeoPostalAreas23 | GeoPostalAreas24 | GeoPostalAreas25 | GeoPostalAreas26 | GeoPostalAreas27 | GeoPostalAreas28 | GeoPostalAreas29 | GeoPostalAreas30 | GeoPostalAreas31 | GeoPostalAreas32]]
    geo_postal_areas_exclude: NotRequired[list[GeoPostalAreasExclude22 | GeoPostalAreasExclude23 | GeoPostalAreasExclude24 | GeoPostalAreasExclude25 | GeoPostalAreasExclude26 | GeoPostalAreasExclude27 | GeoPostalAreasExclude28 | GeoPostalAreasExclude29 | GeoPostalAreasExclude30 | GeoPostalAreasExclude31 | GeoPostalAreasExclude32]]
    geo_places: NotRequired[list[GeoPlace5]]
    geo_places_exclude: NotRequired[list[GeoPlacesExcludeItem5]]
    daypart_targets: NotRequired[list[DaypartTarget]]
    axe_include_segment: NotRequired[str]
    axe_exclude_segment: NotRequired[str]
    audience_include: NotRequired[list[str]]
    audience_exclude: NotRequired[list[str]]
    demographics: NotRequired[Demographics4]
    frequency_cap: NotRequired[FrequencyCap3]
    property_list: NotRequired[PropertyList]
    property_list_exclude: NotRequired[PropertyListExclude]
    collection_list: NotRequired[CollectionList]
    collection_list_exclude: NotRequired[CollectionListExclude]
    placement_selection: NotRequired[dict[str, JsonValue]]
    collection_selection: NotRequired[dict[str, JsonValue]]
    age_restriction: NotRequired[AgeRestriction]
    device_platform: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    device_platform_exclude: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    device_type: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    device_type_exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    browser: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    browser_exclude: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    store_catchments: NotRequired[list[StoreCatchment]]
    geo_proximity: NotRequired[list[GeoProximityItem3]]
    language: NotRequired[list[LanguageItem2]]
    keyword_targets: NotRequired[list[KeywordTarget]]
    negative_keywords: NotRequired[list[NegativeKeyword]]
    signal_targeting_groups: NotRequired[SignalTargetingGroups2]
    geo_countries: NotRequired[list[str]]
    geo_countries_exclude: NotRequired[list[str]]
    geo_regions: NotRequired[list[str]]
    geo_regions_exclude: NotRequired[list[str]]

class PerformanceStandard2(TypedDict):
    metric: Literal['viewability', 'ivt', 'completion_rate', 'brand_safety', 'attention_score']
    threshold: float
    standard: NotRequired[Literal['MRC', 'GroupM']]
    vendor: NotRequired[Vendor1]

class Product2(TypedDict):
    productId: str
    selectionId: NotRequired[str]
    inventorySourceId: NotRequired[str]
    salesAgentId: NotRequired[str]
    pricingOptionId: NotRequired[str]
    budget: NotRequired[float]
    bidPrice: NotRequired[float]
    targetingOverlay: NotRequired[TargetingOverlay3]
    performanceStandards: NotRequired[list[PerformanceStandard2] | None]
    pixelId: NotRequired[str]
    remove: NotRequired[bool]
    lineItemRef: NotRequired[str]

class BudgetAllocation4(TypedDict):
    mode: Literal['fixed']

class OptimizationGoals6(TypedDict):
    kind: Literal['metric']
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    reach_unit: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    target_frequency: NotRequired[TargetFrequency]
    view_duration_seconds: NotRequired[SaveMediaBuyRequestSchema115]
    target: NotRequired[SaveMediaBuyRequestSchema118 | SaveMediaBuyRequestSchema120]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class Target9(TypedDict):
    kind: Literal['per_ad_spend']
    value: SaveMediaBuyRequestSchema115
    strength: NotRequired[Literal['floor', 'target']]

class Target10(TypedDict):
    kind: Literal['maximize_value']

class OptimizationGoals7(TypedDict):
    kind: Literal['event']
    event_sources: list[EventSource1]
    target: NotRequired[SaveMediaBuyRequestSchema118 | Target9 | Target10]
    attribution_window: NotRequired[AttributionWindow]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class OptimizationGoals8(TypedDict):
    kind: Literal['vendor_metric']
    vendor: Vendor1
    metric_id: str
    target: NotRequired[SaveMediaBuyRequestSchema118 | SaveMediaBuyRequestSchema120]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class BudgetAllocation5(TypedDict):
    mode: Literal['seller_optimized']
    optimization_goals: list[OptimizationGoals6 | OptimizationGoals7 | OptimizationGoals8]

class SaveMediaBuyInput6(TypedDict):
    mediaBuyId: NotRequired[str]
    fromProposalId: NotRequired[str]
    campaignId: NotRequired[str]
    channelGroupId: NotRequired[str]
    sellerId: NotRequired[str]
    products: NotRequired[list[Product2]]
    budget: NotRequired[Budget8]
    budgetAllocation: NotRequired[BudgetAllocation4 | BudgetAllocation5]
    flight: NotRequired[Flight]
    isArchived: NotRequired[bool]
    isPaused: NotRequired[bool]
    idempotencyKey: str

class GeoPostalAreas33(TypedDict):
    country: Literal['US']
    system: Literal['zip', 'zip_plus_four']
    values: list[str]

class GeoPostalAreas34(TypedDict):
    country: Literal['GB']
    system: Literal['outward', 'full']
    values: list[str]

class GeoPostalAreas35(TypedDict):
    country: Literal['CA']
    system: Literal['full', 'fsa']
    values: list[str]

class GeoPostalAreas36(TypedDict):
    country: Literal['DE', 'CH', 'AT']
    system: Literal['plz']
    values: list[str]

class GeoPostalAreas37(TypedDict):
    country: Literal['FR']
    system: Literal['code_postal']
    values: list[str]

class GeoPostalAreas38(TypedDict):
    country: Literal['AU']
    system: Literal['postcode']
    values: list[str]

class GeoPostalAreas39(TypedDict):
    country: Literal['BR']
    system: Literal['cep']
    values: list[str]

class GeoPostalAreas40(TypedDict):
    country: Literal['IN']
    system: Literal['pin']
    values: list[str]

class GeoPostalAreas41(TypedDict):
    country: Literal['ZA']
    system: Literal['postal_code']
    values: list[str]

class GeoPostalAreas42(TypedDict):
    country: str
    system: Literal['postal_code', 'custom']
    values: list[str]

class GeoPostalAreas43(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class GeoPostalAreasExclude33(TypedDict):
    country: Literal['US']
    system: Literal['zip', 'zip_plus_four']
    values: list[str]

class GeoPostalAreasExclude34(TypedDict):
    country: Literal['GB']
    system: Literal['outward', 'full']
    values: list[str]

class GeoPostalAreasExclude35(TypedDict):
    country: Literal['CA']
    system: Literal['full', 'fsa']
    values: list[str]

class GeoPostalAreasExclude36(TypedDict):
    country: Literal['DE', 'CH', 'AT']
    system: Literal['plz']
    values: list[str]

class GeoPostalAreasExclude37(TypedDict):
    country: Literal['FR']
    system: Literal['code_postal']
    values: list[str]

class GeoPostalAreasExclude38(TypedDict):
    country: Literal['AU']
    system: Literal['postcode']
    values: list[str]

class GeoPostalAreasExclude39(TypedDict):
    country: Literal['BR']
    system: Literal['cep']
    values: list[str]

class GeoPostalAreasExclude40(TypedDict):
    country: Literal['IN']
    system: Literal['pin']
    values: list[str]

class GeoPostalAreasExclude41(TypedDict):
    country: Literal['ZA']
    system: Literal['postal_code']
    values: list[str]

class GeoPostalAreasExclude42(TypedDict):
    country: str
    system: Literal['postal_code', 'custom']
    values: list[str]

class GeoPostalAreasExclude43(TypedDict):
    system: Literal['us_zip', 'us_zip_plus_four', 'gb_outward', 'gb_full', 'ca_fsa', 'ca_full', 'de_plz', 'fr_code_postal', 'au_postcode', 'ch_plz', 'at_plz']
    values: list[str]

class GeoPlace61(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]
    country: NotRequired[JsonValue]
    system_version: NotRequired[JsonValue]
    place_type: NotRequired[JsonValue]
    value_labels: NotRequired[JsonValue]
    ext: NotRequired[JsonValue]

class GeoPlace62(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value3]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

class GeoPlace63(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlace6: TypeAlias = GeoPlace63

class GeoPlacesExcludeItem61(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads']
    values: NotRequired[JsonValue]
    country: NotRequired[JsonValue]
    system_version: NotRequired[JsonValue]
    place_type: NotRequired[JsonValue]
    value_labels: NotRequired[JsonValue]
    ext: NotRequired[JsonValue]

class GeoPlacesExcludeItem62(TypedDict):
    country: str
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    values: list[Value3]
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]

class GeoPlacesExcludeItem63(TypedDict):
    system: Literal['geonames', 'google_ads', 'microsoft_ads'] | str
    values: list[Value3]
    country: str
    system_version: NotRequired[str]
    place_type: Literal['airport', 'borough', 'city', 'city_region', 'commune', 'county', 'district', 'municipality', 'neighborhood', 'post_town', 'prefecture', 'province', 'quarter', 'state', 'territory', 'ward'] | str
    value_labels: NotRequired[dict[str, str]]
    ext: NotRequired[dict[str, JsonValue]]
GeoPlacesExcludeItem6: TypeAlias = GeoPlacesExcludeItem63

class Demographics5(TypedDict):
    age: Age7

class FrequencyCap41(TypedDict):
    suppress: JsonValue
    suppress_minutes: NotRequired[JsonValue]
    max_impressions: NotRequired[JsonValue]
    per: NotRequired[JsonValue]
    window: NotRequired[JsonValue]

class FrequencyCap42(TypedDict):
    window: JsonValue
    max_impressions: JsonValue
    suppress: NotRequired[JsonValue]
    suppress_minutes: NotRequired[JsonValue]
    per: NotRequired[JsonValue]

class FrequencyCap43(TypedDict):
    max_impressions: JsonValue
    suppress: NotRequired[JsonValue]
    suppress_minutes: NotRequired[JsonValue]
    per: NotRequired[JsonValue]
    window: NotRequired[JsonValue]

class FrequencyCap44(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap45(TypedDict):
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    max_impressions: NotRequired[int]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap46(TypedDict):
    window: NotRequired[Window3]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]

class FrequencyCap47(TypedDict):
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    window: NotRequired[Window3]

class FrequencyCap48(TypedDict):
    window: NotRequired[Window3]
    max_impressions: NotRequired[int]
    suppress: NotRequired[Suppress]
    suppress_minutes: NotRequired[float]
    per: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
FrequencyCap4: TypeAlias = FrequencyCap45 | FrequencyCap46 | FrequencyCap47 | FrequencyCap48

class GeoProximityItem4(TypedDict):
    lat: NotRequired[float]
    lng: NotRequired[float]
    label: NotRequired[str]
    travel_time: NotRequired[TravelTime]
    transport_mode: NotRequired[Literal['walking', 'cycling', 'driving', 'public_transport']]
    radius: NotRequired[Radius]
    geometry: NotRequired[Geometry1]
    ext: NotRequired[dict[str, JsonValue]]

class Signals9(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['binary']
    value: Literal[True]

class Signals10(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['categorical']
    values: list[str]

class Signals11(TypedDict):
    signal_ref: SaveMediaBuyRequestSchema58
    pricing_option_id: NotRequired[str]
    signal_agent_segment_id: NotRequired[str]
    activation_key: NotRequired[JsonValue]
    value_type: Literal['numeric']
    min_value: NotRequired[float]
    max_value: NotRequired[float]

class Group3(TypedDict):
    operator: Literal['any', 'none']
    signals: list[Signals9 | Signals10 | Signals11]

class SignalTargetingGroups3(TypedDict):
    operator: Literal['all']
    groups: list[Group3]

class TargetingOverlay4(TypedDict):
    geo_metros: NotRequired[list[GeoMetro1]]
    geo_metros_exclude: NotRequired[list[GeoMetrosExcludeItem]]
    geo_postal_areas: NotRequired[list[GeoPostalAreas33 | GeoPostalAreas34 | GeoPostalAreas35 | GeoPostalAreas36 | GeoPostalAreas37 | GeoPostalAreas38 | GeoPostalAreas39 | GeoPostalAreas40 | GeoPostalAreas41 | GeoPostalAreas42 | GeoPostalAreas43]]
    geo_postal_areas_exclude: NotRequired[list[GeoPostalAreasExclude33 | GeoPostalAreasExclude34 | GeoPostalAreasExclude35 | GeoPostalAreasExclude36 | GeoPostalAreasExclude37 | GeoPostalAreasExclude38 | GeoPostalAreasExclude39 | GeoPostalAreasExclude40 | GeoPostalAreasExclude41 | GeoPostalAreasExclude42 | GeoPostalAreasExclude43]]
    geo_places: NotRequired[list[GeoPlace6]]
    geo_places_exclude: NotRequired[list[GeoPlacesExcludeItem6]]
    daypart_targets: NotRequired[list[DaypartTarget]]
    axe_include_segment: NotRequired[str]
    axe_exclude_segment: NotRequired[str]
    audience_include: NotRequired[list[str]]
    audience_exclude: NotRequired[list[str]]
    demographics: NotRequired[Demographics5]
    frequency_cap: NotRequired[FrequencyCap4]
    property_list: NotRequired[PropertyList]
    property_list_exclude: NotRequired[PropertyListExclude]
    collection_list: NotRequired[CollectionList]
    collection_list_exclude: NotRequired[CollectionListExclude]
    placement_selection: NotRequired[dict[str, JsonValue]]
    collection_selection: NotRequired[dict[str, JsonValue]]
    age_restriction: NotRequired[AgeRestriction]
    device_platform: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    device_platform_exclude: NotRequired[list[Literal['ios', 'android', 'windows', 'macos', 'linux', 'chromeos', 'tvos', 'tizen', 'webos', 'fire_os', 'roku_os', 'unknown']]]
    device_type: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    device_type_exclude: NotRequired[list[Literal['desktop', 'mobile', 'tablet', 'ctv', 'dooh', 'unknown']]]
    browser: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    browser_exclude: NotRequired[list[Literal['chrome', 'safari', 'firefox', 'edge', 'opera', 'samsung_internet', 'android_webview', 'other', 'unknown']]]
    store_catchments: NotRequired[list[StoreCatchment]]
    geo_proximity: NotRequired[list[GeoProximityItem4]]
    language: NotRequired[list[LanguageItem2]]
    keyword_targets: NotRequired[list[KeywordTarget]]
    negative_keywords: NotRequired[list[NegativeKeyword]]
    signal_targeting_groups: NotRequired[SignalTargetingGroups3]
    geo_countries: NotRequired[list[str]]
    geo_countries_exclude: NotRequired[list[str]]
    geo_regions: NotRequired[list[str]]
    geo_regions_exclude: NotRequired[list[str]]

class PerformanceStandard3(TypedDict):
    metric: Literal['viewability', 'ivt', 'completion_rate', 'brand_safety', 'attention_score']
    threshold: float
    standard: NotRequired[Literal['MRC', 'GroupM']]
    vendor: NotRequired[Vendor1]

class Product3(TypedDict):
    productId: str
    selectionId: NotRequired[str]
    inventorySourceId: NotRequired[str]
    salesAgentId: NotRequired[str]
    pricingOptionId: NotRequired[str]
    budget: NotRequired[float]
    bidPrice: NotRequired[float]
    targetingOverlay: NotRequired[TargetingOverlay4]
    performanceStandards: NotRequired[list[PerformanceStandard3] | None]
    pixelId: NotRequired[str]
    remove: NotRequired[bool]
    lineItemRef: NotRequired[str]

class BudgetAllocation6(TypedDict):
    mode: Literal['fixed']

class OptimizationGoals9(TypedDict):
    kind: Literal['metric']
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    reach_unit: NotRequired[Literal['individuals', 'households', 'devices', 'accounts', 'cookies', 'custom']]
    target_frequency: NotRequired[TargetFrequency]
    view_duration_seconds: NotRequired[SaveMediaBuyRequestSchema115]
    target: NotRequired[SaveMediaBuyRequestSchema118 | SaveMediaBuyRequestSchema120]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class Target11(TypedDict):
    kind: Literal['per_ad_spend']
    value: SaveMediaBuyRequestSchema115
    strength: NotRequired[Literal['floor', 'target']]

class Target12(TypedDict):
    kind: Literal['maximize_value']

class OptimizationGoals10(TypedDict):
    kind: Literal['event']
    event_sources: list[EventSource1]
    target: NotRequired[SaveMediaBuyRequestSchema118 | Target11 | Target12]
    attribution_window: NotRequired[AttributionWindow]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class OptimizationGoals11(TypedDict):
    kind: Literal['vendor_metric']
    vendor: Vendor1
    metric_id: str
    target: NotRequired[SaveMediaBuyRequestSchema118 | SaveMediaBuyRequestSchema120]
    priority: NotRequired[SaveMediaBuyRequestSchema122]

class BudgetAllocation7(TypedDict):
    mode: Literal['seller_optimized']
    optimization_goals: list[OptimizationGoals9 | OptimizationGoals10 | OptimizationGoals11]

class SaveMediaBuyInput7(TypedDict):
    mediaBuyId: NotRequired[str]
    fromProposalId: NotRequired[str]
    campaignId: NotRequired[str]
    channelGroupId: NotRequired[str]
    sellerId: NotRequired[str]
    products: NotRequired[list[Product3]]
    budget: NotRequired[Budget8]
    budgetAllocation: NotRequired[BudgetAllocation6 | BudgetAllocation7]
    flight: NotRequired[Flight]
    isArchived: NotRequired[bool]
    isPaused: NotRequired[bool]
    idempotencyKey: str
SaveMediaBuyInput: TypeAlias = SaveMediaBuyInput5 | SaveMediaBuyInput6 | SaveMediaBuyInput7

class ChannelGroup(TypedDict):
    channelGroupId: str
    name: str

class PendingChange(TypedDict):
    status: str
    pendingAt: NotRequired[SaveMediaBuySuccessSchema0]

class Ending(TypedDict):
    reason: Literal['canceled']
    since: str

class MediaBuyRef(TypedDict):
    mediaBuyId: str
    channelGroup: NotRequired[ChannelGroup]
    pendingAt: NotRequired[SaveMediaBuySuccessSchema0]
    pendingChange: NotRequired[PendingChange]
    phase: SaveMediaBuySuccessSchema1
    isPaused: NotRequired[bool]
    ending: NotRequired[Ending]

class ProposalSource(TypedDict):
    proposalId: str
    proposalVersionId: str

class FrequencyCap5(TypedDict):
    level: Literal['mediaBuy']
    requested: SaveMediaBuySuccessSchema14
    effective: NotRequired[SaveMediaBuySuccessSchema14]
    status: Literal['requested', 'confirmed']

class Error12(TypedDict):
    mediaBuyId: str
    salesAgentId: str
    message: str
    debug: NotRequired[JsonValue]
SaveMediaBuyError: TypeAlias = V3ToolErrorResponse
SellerId: TypeAlias = str

class Evaluation(TypedDict):
    instructions: NotRequired[str]
    maxRefinementRounds: NotRequired[int]
    ranking: NotRequired[dict[str, JsonValue]]
    policyId: NotRequired[str]

class RequestProposalsInput(TypedDict):
    campaignId: str
    expectedCampaignRevision: int
    sellerIds: NotRequired[list[SellerId]]
    expectedSellerId: NotRequired[str]
    evaluation: NotRequired[Evaluation]
    idempotencyKey: str
    capabilityCursor: NotRequired[str]
    resultCursor: NotRequired[str]
    resultLimit: NotRequired[int]

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
RequestProposalsError: TypeAlias = V3ToolErrorResponse

class Artifact(TypedDict):
    ref: str
    sourceLocator: NotRequired[str]
    role: Literal['original', 'page_image', 'slide_image', 'embedded_image', 'chart', 'logo', 'table', 'ocr', 'caption', 'structure', 'other']
    contentType: NotRequired[str]
    digest: NotRequired[SaveMaterialRequestSchema13]
    bytes: NotRequired[int]
    widthPx: NotRequired[int]
    heightPx: NotRequired[int]
    kind: NotRequired[Literal['photo', 'illustration', 'logo', 'chart', 'diagram', 'screenshot', 'background', 'other']]
    crop: NotRequired[Crop]
    caption: NotRequired[Caption]
    ocr: NotRequired[Ocr]
    altText: NotRequired[AltText]
    licenseScope: NotRequired[str]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    confidentiality: NotRequired[SaveMaterialRequestSchema22]

class SaveMaterialRequestSchema15(TypedDict):
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    structureRef: NotRequired[str]
    readingOrderRef: NotRequired[str]
    geometryRef: NotRequired[str]
    ocrRef: NotRequired[str]
    captionsRef: NotRequired[str]
    parser: NotRequired[str]
    parserVersion: NotRequired[str]
    nodes: NotRequired[list[Node]]
    artifacts: NotRequired[list[Artifact]]
SaveRfpRequestSchema50: TypeAlias = list[SaveRfpRequestSchema51]

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
    credentials: list[SaveBuyerAgentSuccessBuyerAgentCredential]
    credentialCount: int
    credentialsTruncated: bool
    activeCredentialCount: int
    access: Access
    notifications: Notifications | None

class SaveCampaignRequestOptimizationAttributionWindow(TypedDict):
    postClick: SaveCampaignRequestDuration
    postView: NotRequired[SaveCampaignRequestDuration]

class SaveCampaignRequestMetricGoal(TypedDict):
    kind: Literal['metric']
    metric: Literal['clicks', 'views', 'completed_views', 'viewed_seconds', 'viewable_rate', 'attention_seconds', 'attention_score', 'engagements', 'follows', 'saves', 'profile_visits', 'reach']
    viewDurationSeconds: NotRequired[float]
    target: NotRequired[SaveCampaignRequestSchema54 | Target2]
    attributionWindow: NotRequired[SaveCampaignRequestOptimizationAttributionWindow]
    priority: NotRequired[int]

class Rights(TypedDict):
    status: NotRequired[Literal['unknown', 'owned', 'licensed', 'restricted', 'expired']]
    usage: NotRequired[SaveCreativeSessionRequestSchema25]
    expires_at: NotRequired[SaveCreativeSessionRequestSchema27]
    notes: NotRequired[SaveCreativeSessionRequestSchema29]

class SaveCreativeSessionRequestSchema15(TypedDict):
    asset_id: NotRequired[str]
    label: str
    url: str
    source: NotRequired[SaveCreativeSessionRequestSchema17]
    role: NotRequired[SaveCreativeSessionRequestSchema18]
    locked_asset: NotRequired[bool]
    can_transform: NotRequired[bool]
    preservation_notes: NotRequired[str]
    rights: NotRequired[Rights]
    dimensions: NotRequired[Dimensions]
    render_crop: NotRequired[RenderCrop]
    checksum: NotRequired[str]
    mime_type: NotRequired[str]

class SaveMediaBuySuccessSchema4(TypedDict):
    kind: Literal['metric', 'event']
    subject: str
    eventTypes: list[str]
    target: SaveMediaBuySuccessSchema5 | None

class Source3(TypedDict):
    kind: Literal['url']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: NotRequired[str]
    url: SaveMaterialRequestSchema26
    authorization: NotRequired[Literal['seller_attested', 'public_web', 'operator_verified']]

class Source4(TypedDict):
    kind: Literal['site']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: NotRequired[str]
    rootUrl: SaveMaterialRequestSchema26
    relatedDomains: NotRequired[list[RelatedDomain]]
    includePatterns: NotRequired[list[IncludePattern]]
    excludePatterns: NotRequired[list[ExcludePattern]]
    maxPages: NotRequired[int]
    maxDepth: NotRequired[int]
    maxBytes: NotRequired[int]
    robotsPolicy: NotRequired[Literal['respect', 'seller_attested']]

class Source5(TypedDict):
    kind: Literal['upload']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: str
    fileName: str
    contentType: str
    sizeBytes: int
    sha256: NotRequired[str]
    assetRef: NotRequired[str]
    fileRole: NotRequired[Literal['deck', 'rate_card', 'case_study', 'specification', 'policy', 'other']]

class Item(TypedDict):
    url: SaveMaterialRequestSchema26
    status: Literal['fetched', 'skipped', 'failed']
    contentDigest: NotRequired[SaveMaterialRequestSchema13]
    bytes: NotRequired[int]
    reason: NotRequired[str]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]

class Source6(TypedDict):
    kind: Literal['crawl_manifest']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: str
    rootUrl: SaveMaterialRequestSchema26
    fetchedBy: Literal['platform', 'seller_supplied', 'seller_attested']
    generatedAt: str
    items: list[Item]
    manifestDigest: NotRequired[SaveMaterialRequestSchema13]

class Source7(TypedDict):
    kind: Literal['inline']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: str
    content: str

class Source8(TypedDict):
    kind: Literal['history']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: str
    historyKind: Literal['proposal', 'case_study', 'rate_card', 'policy']
    referenceId: str
    advertiserRef: NotRequired[str]
    summary: NotRequired[str]

class SaveMaterialInput1(TypedDict):
    action: Literal['create']
    clientRequestId: str
    source: Source3 | Source4 | Source5 | Source6 | Source7 | Source8
    metadata: NotRequired[Metadata]
    labels: NotRequired[dict[str, list[Label]]]
    commit: NotRequired[bool]
    dryRun: NotRequired[bool]

class Source9(TypedDict):
    kind: Literal['url']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: NotRequired[str]
    url: SaveMaterialRequestSchema26
    authorization: NotRequired[Literal['seller_attested', 'public_web', 'operator_verified']]

class Source10(TypedDict):
    kind: Literal['site']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: NotRequired[str]
    rootUrl: SaveMaterialRequestSchema26
    relatedDomains: NotRequired[list[RelatedDomain]]
    includePatterns: NotRequired[list[IncludePattern]]
    excludePatterns: NotRequired[list[ExcludePattern]]
    maxPages: NotRequired[int]
    maxDepth: NotRequired[int]
    maxBytes: NotRequired[int]
    robotsPolicy: NotRequired[Literal['respect', 'seller_attested']]

class Source11(TypedDict):
    kind: Literal['upload']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: str
    fileName: str
    contentType: str
    sizeBytes: int
    sha256: NotRequired[str]
    assetRef: NotRequired[str]
    fileRole: NotRequired[Literal['deck', 'rate_card', 'case_study', 'specification', 'policy', 'other']]

class Source12(TypedDict):
    kind: Literal['crawl_manifest']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: str
    rootUrl: SaveMaterialRequestSchema26
    fetchedBy: Literal['platform', 'seller_supplied', 'seller_attested']
    generatedAt: str
    items: list[Item]
    manifestDigest: NotRequired[SaveMaterialRequestSchema13]

class Source13(TypedDict):
    kind: Literal['inline']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: str
    content: str

class Source14(TypedDict):
    kind: Literal['history']
    originalRef: NotRequired[SaveMaterialRequestSchema11]
    originalDigest: NotRequired[SaveMaterialRequestSchema13]
    derivedStructure: NotRequired[SaveMaterialRequestSchema15]
    renditionRefs: NotRequired[SaveMaterialRequestSchema23]
    reuseRights: NotRequired[SaveMaterialRequestSchema20]
    name: str
    historyKind: Literal['proposal', 'case_study', 'rate_card', 'policy']
    referenceId: str
    advertiserRef: NotRequired[str]
    summary: NotRequired[str]

class SaveMaterialInput2(TypedDict):
    action: Literal['replace_source']
    materialId: str
    expectedRevision: int
    clientRequestId: str
    source: Source9 | Source10 | Source11 | Source12 | Source13 | Source14
    metadata: NotRequired[Metadata1]
    labels: NotRequired[dict[str, list[Label]]]
SaveMaterialInput: TypeAlias = SaveMaterialInput1 | SaveMaterialInput2 | SaveMaterialInput3 | SaveMaterialInput4 | SaveMaterialInput5 | SaveMaterialInput6 | SaveMaterialInput7 | SaveMaterialInput8 | SaveMaterialInput9 | SaveMaterialInput10 | SaveMaterialInput11

class Origin(TypedDict):
    kind: Literal['quick', 'uploaded', 'inbound', 'manual', 'imported']
    presetId: NotRequired[SaveRfpRequestI]
    preset: NotRequired[Preset | dict[SaveRfpRequestP, SaveRfpRequestJ]]
    sourceMaterialId: NotRequired[SaveRfpRequestI]
    buyer: NotRequired[SaveRfpRequestSchema48]
    advertiser: NotRequired[SaveRfpRequestSchema48]
    category: NotRequired[SaveRfpRequestSchema48]
    market: NotRequired[SaveRfpRequestSchema48]
    channels: NotRequired[SaveRfpRequestSchema50]
    details: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]

class Dimensions2(TypedDict):
    channels: NotRequired[SaveRfpRequestSchema50]
    channel: NotRequired[SaveRfpRequestSchema51]
    formatKinds: NotRequired[SaveRfpRequestSchema71]
    format_kinds: NotRequired[SaveRfpRequestSchema71]
    productCount: NotRequired[SaveRfpRequestSchema73]
    product_count: NotRequired[SaveRfpRequestSchema73]
    planRoles: NotRequired[SaveRfpRequestSchema74]
    plan_roles: NotRequired[SaveRfpRequestSchema74]
    audience: NotRequired[SaveRfpRequestSchema77]
    creativeInputs: NotRequired[SaveRfpRequestSchema79]

class Request1(TypedDict):
    brief: SaveRfpRequestP
    budget: NotRequired[Budget1]
    flight: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    dimensions: NotRequired[Dimensions2]
    constraints: NotRequired[Constraints]

class SaveRfpInput1(TypedDict):
    action: Literal['create']
    clientRequestId: SaveRfpRequestI
    origin: Origin
    purpose: Literal['live', 'draft', 'evaluation']
    request: Request1
    strategy: NotRequired[Strategy]
    requiredEndorsedPairId: NotRequired[SaveRfpRequestI]
    requiredLibraryUnitIds: NotRequired[list[RequiredLibraryUnitId]]

class Request2(TypedDict):
    brief: SaveRfpRequestP
    budget: NotRequired[Budget1]
    flight: NotRequired[dict[SaveRfpRequestK, SaveRfpRequestJ]]
    dimensions: NotRequired[Dimensions2]
    constraints: NotRequired[Constraints]

class SaveRfpInput2(TypedDict):
    action: Literal['append_turn']
    clientRequestId: SaveRfpRequestI
    rfpId: SaveRfpRequestI
    parentTurnId: SaveRfpRequestI
    request: Request2
    strategy: NotRequired[Strategy]
    requiredEndorsedPairId: NotRequired[SaveRfpRequestI]
    requiredLibraryUnitIds: NotRequired[list[RequiredLibraryUnitId]]
SaveRfpInput: TypeAlias = SaveRfpInput1 | SaveRfpInput2 | SaveRfpInput3 | SaveRfpInput4 | SaveRfpInput5 | SaveRfpInput6 | SaveRfpInput7 | SaveRfpInput8 | SaveRfpInput9 | SaveRfpInput10 | SaveRfpInput11 | SaveRfpInput12 | SaveRfpInput13

class SaveBuyerAgentResult(TypedDict):
    kind: Literal['buyer_agent']
    object: SaveBuyerAgentSuccessBuyerAgentNoun

class Draft(TypedDict):
    request: dict[str, JsonValue]
    title: NotRequired[str]
    persona: NotRequired[str]
    brand: NotRequired[str]
    objective: NotRequired[str]
    prompt: NotRequired[str]
    source_asset: NotRequired[SaveCreativeSessionRequestSchema15]
    assets: NotRequired[list[SaveCreativeSessionRequestSchema15]]
    renditions: NotRequired[list[Rendition]]
    partial_success: NotRequired[bool]

class SaveCreativeSessionInput1(TypedDict):
    operation: Literal['save_draft']
    campaignId: str
    engine: NotRequired[Engine]
    draft: Draft
    idempotencyKey: str
SaveCreativeSessionInput: TypeAlias = SaveCreativeSessionInput1 | SaveCreativeSessionInput2 | SaveCreativeSessionInput3 | SaveCreativeSessionInput4 | SaveCreativeSessionInput5

class GoalAnswer(TypedDict):
    productId: str
    storefrontId: NotRequired[str | None]
    pricingOptionId: str | None
    pricingModel: str | None
    fixedPrice: float | None
    currency: str | None
    deliveryType: Literal['guaranteed', 'non_guaranteed'] | None
    measurementTerms: JsonValue
    sellerOptimizationGoals: list[JsonValue] | None
    askedGoal: SaveMediaBuySuccessSchema4 | None
    answeredTarget: SaveMediaBuySuccessSchema5 | None
    commitment: SaveMediaBuySuccessSchema3

class GoalCommitment(TypedDict):
    source: Literal['proposal', 'campaign']
    proposalVersionId: NotRequired[str]
    kind: SaveMediaBuySuccessSchema3
    askedGoal: SaveMediaBuySuccessSchema4 | None
    answeredTarget: SaveMediaBuySuccessSchema5 | None
    meetsAskedTarget: bool | None
    goalAnswers: list[GoalAnswer]
    goalAnswersTruncated: NotRequired[Literal[True]]

class MediaBuy2(TypedDict):
    mediaBuyId: str
    name: str
    channelGroup: NotRequired[ChannelGroup]
    optimizationGoals: NotRequired[JsonValue]
    goalCommitment: NotRequired[GoalCommitment]
    frequencyCap: NotRequired[FrequencyCap5]
    phase: SaveMediaBuySuccessSchema1
    isPaused: bool
    isArchived: bool
    ending: NotRequired[Ending]
    flight: NotRequired[Flight]
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
    action: Literal['staged', 'updated', 'paused', 'resumed', 'unchanged', 'archived', 'cancellation_requested']
    campaignId: NotRequired[str]
    mediaBuyId: NotRequired[str]
    isPaused: NotRequired[bool]
    previousStatus: NotRequired[str]
    newStatus: NotRequired[str]
    mediaBuysStaged: NotRequired[float]
    mediaBuyRefs: NotRequired[list[MediaBuyRef]]
    proposalSource: NotRequired[ProposalSource]
    mediaBuy: NotRequired[MediaBuy2]
    warnings: NotRequired[list[str]]
    errors: NotRequired[list[Error12]]

class SaveCampaignRequestEventGoal(TypedDict):
    kind: Literal['event']
    eventSources: list[EventSource]
    target: NotRequired[SaveCampaignRequestSchema54 | Target | Target1]
    attributionWindow: NotRequired[SaveCampaignRequestOptimizationAttributionWindow]
    priority: NotRequired[int]
SaveCampaignRequestOptimizationGoal: TypeAlias = SaveCampaignRequestEventGoal | SaveCampaignRequestMetricGoal

class SaveCampaignInput(TypedDict):
    sponsoredBuyerCustomerId: NotRequired[str]
    campaignId: NotRequired[str]
    advertiserId: NotRequired[str]
    name: NotRequired[str]
    expectedRevision: NotRequired[int]
    brief: NotRequired[str | None]
    flight: NotRequired[Flight | None]
    budget: NotRequired[Budget7]
    frequencyCap: NotRequired[FrequencyCap | None]
    confirmLaunch: NotRequired[bool]
    sellerIds: NotRequired[list[str]]
    creativeIds: NotRequired[list[CreativeId]]
    autonomy: NotRequired[Autonomy]
    desiredPhase: NotRequired[Literal['active', 'canceled']]
    isPaused: NotRequired[bool]
    isArchived: NotRequired[bool]
    optimizationGoals: NotRequired[list[SaveCampaignRequestOptimizationGoal] | None]
    catalogId: NotRequired[str | None]
    idempotencyKey: str
    tracking: NotRequired[Tracking1]
    targetingOverlay: NotRequired[TargetingOverlay | None]
    targeting: NotRequired[Targeting | None]
    channelGroups: NotRequired[list[ChannelGroups | ChannelGroups1] | None]
    audienceConfig: NotRequired[AudienceConfig]
    labels: NotRequired[dict[str, list[Label]]]
    propertyListId: NotRequired[str | None]
