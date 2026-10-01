from apostra import Apostra, AsyncApostra
from apostra.models import EvidenceUrl, SaveRfpRequestJ, SaveRfpRequestSchema86, SaveCampaignInput, GetDeliveryResult, SaveLibraryRequestInput, SaveCreativeSessionInput, SaveDimensionInput, SaveDimensionResult, SearchInput, GetInput, SaveMaterialInput, TargetingOverlay3

nested: SaveRfpRequestJ = {'deep': [{'nested': ['value', None, 2, True]}]}
campaign: SaveCampaignInput = {'idempotencyKey': 'k', 'channelGroups': [{'channelGroupId': 'g', 'presetId': 'ctv'}]}

def typed(client: Apostra) -> GetDeliveryResult:
    return client.get_delivery({})

def typed_write(client: Apostra) -> SaveDimensionResult:
    return client.save_dimension(dimension, idempotency_key='dimension-1')

def typed_dimension_fields(result: SaveDimensionResult) -> tuple[str, float]:
    return result['object']['id'], result['object']['usage']['advertiser']

async def typed_async(client: AsyncApostra) -> GetDeliveryResult:
    return await client.get_delivery({})

library: SaveLibraryRequestInput = {'action': 'close', 'id': 'r', 'closedBy': 'upload', 'materialId': 'm'}
creative: SaveCreativeSessionInput = {'operation': 'select_output', 'campaignId': 'c', 'sessionId': 's', 'variantId': 'v', 'expectedRevision': 1}
dimension: SaveDimensionInput = {'key': 'market', 'name': 'Market', 'valuesMode': 'open', 'appliesTo': ['campaign'], 'idempotencyKey': 'k'}
search: SearchInput = {'kind': 'creative', 'filter': {'advertiserId': 'a'}}
get: GetInput = {'kind': 'catalog', 'id': 'c', 'advertiserId': 'a'}
material: SaveMaterialInput = {'action': 'replace_source', 'materialId': 'm', 'expectedRevision': 1, 'clientRequestId': 'k', 'source': {'kind': 'inline', 'name': 'n', 'content': 'c'}}
postal_targeting: TargetingOverlay3 = {'geo_postal_areas': [{'country': 'US', 'system': 'zip', 'values': ['94105']}]}
postal_targeting_fallback: TargetingOverlay3 = {'geo_postal_areas': [{'country': 'NZ', 'system': 'custom', 'values': ['00100']}]}
evidence_url: EvidenceUrl = 'https://example.test/evidence'
locale: SaveRfpRequestSchema86 = 'en-GB'
