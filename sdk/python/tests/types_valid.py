from apostra import Apostra, AsyncApostra
from apostra.models import EvidenceUrl, JsonValue, RepresentationLocale, SaveCampaignInput, SaveBillingInput, GetDeliveryResult, SaveLibraryRequestInput, SaveCreativeSessionInput, SaveDimensionInput, SaveDimensionResult, SaveMediaBuyInput, SearchInput, GetInput, SaveMaterialInput, RequestBuyerChildAccountInput

nested: JsonValue = {'deep': [{'nested': ['value', None, 2, True]}]}
campaign: SaveCampaignInput = {'idempotencyKey': 'k', 'channelGroups': [{'channelGroupId': 'g', 'kind': 'preset', 'presetId': 'ctv'}]}
billing: SaveBillingInput = {'terms': {'accepted': True, 'acceptedVersion': 'v1-1'}, 'paymentTerms': 'net_60'}
buyer_child: RequestBuyerChildAccountInput = {'parentId': 'parent', 'name': 'Buyer'}

def typed(client: Apostra) -> GetDeliveryResult:
    return client.get_delivery({})

def typed_write(client: Apostra) -> SaveDimensionResult:
    return client.save_dimension(dimension, idempotency_key='dimension-1')

def typed_dimension_fields(result: SaveDimensionResult) -> tuple[str, float]:
    return result['object']['id'], result['object']['usage']['advertiser']

async def typed_async(client: AsyncApostra) -> GetDeliveryResult:
    return await client.get_delivery({})

library: SaveLibraryRequestInput = {'action': 'close', 'id': 'r', 'closedBy': 'upload', 'closingMaterialId': 'm'}
creative: SaveCreativeSessionInput = {'campaignId': 'c', 'sessionId': 's', 'selectedVariantId': 'v', 'expectedRevision': 1}
dimension: SaveDimensionInput = {'kind': 'create', 'key': 'market', 'name': 'Market', 'valuesMode': 'open', 'appliesTo': ['campaign'], 'idempotencyKey': 'k'}
media_buy_create: SaveMediaBuyInput = {'kind': 'create', 'idempotencyKey': 'k', 'sellerAccountId': 2192, 'products': [{'productId': 'product', 'targetingOverlay': {'geo_countries': ['US']}}]}
media_buy_update: SaveMediaBuyInput = {'kind': 'update', 'idempotencyKey': 'k', 'mediaBuyId': 'buy', 'products': [{'productId': 'product', 'targetingOverlay': {'geo_countries': None}}]}
search: SearchInput = {'kind': 'creative', 'filter': {'advertiserId': 'a'}}
get: GetInput = {'kind': 'catalog', 'id': 'c', 'advertiserId': 'a'}
material: SaveMaterialInput = {'materialId': 'm', 'expectedRevision': 1, 'clientRequestId': 'k', 'source': {'kind': 'inline', 'name': 'n', 'content': 'c'}}
postal_targeting: SaveMediaBuyInput = {'kind': 'create', 'idempotencyKey': 'postal-1', 'sellerAccountId': 2192, 'products': [{'productId': 'product', 'targetingOverlay': {'geo_postal_areas': [{'country': 'US', 'system': 'zip', 'values': ['94105']}]}}]}
postal_targeting_fallback: SaveMediaBuyInput = {'kind': 'create', 'idempotencyKey': 'postal-2', 'sellerAccountId': 2192, 'products': [{'productId': 'product', 'targetingOverlay': {'geo_postal_areas': [{'country': 'NZ', 'system': 'custom', 'values': ['00100']}]}}]}
evidence_url: EvidenceUrl = 'https://example.test/evidence'
locale: RepresentationLocale = 'en-GB'
