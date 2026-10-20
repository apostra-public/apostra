from apostra.models import SaveRfpRequestJsonValue, SaveCampaignInput, SaveBillingInput, SaveRfpInput, SaveLibraryRequestInput, SaveCreativeSessionInput, SaveDimensionInput, SaveMediaBuyInput, SearchInput, GetInput, SaveMaterialInput, RefreshInventorySourceHealthInput, GetDeliveryInput, GetStatusInput
nested: SaveRfpRequestJsonValue = {'deep': [lambda: 0]}
campaign: SaveCampaignInput = {'idempotencyKey': 'k', 'channelGroups': [{'channelGroupId': 'g', 'kind': 'preset', 'presetId': 'ctv', 'inventory': {}}]}
billing: SaveBillingInput = {'operation': 'terms', 'terms': {'accepted': True, 'acceptedVersion': 'v1-1'}}
rfp: SaveRfpInput = {'action': 'feedback'}
library: SaveLibraryRequestInput = {'action': 'close'}
creative: SaveCreativeSessionInput = {'campaignId': 'c', 'advertiserId': '42', 'operation': 'select_output'}
dimension: SaveDimensionInput = {'key': 'market', 'name': 'Market', 'valuesMode': 'open', 'appliesTo': ['campaign'], 'id': '42', 'idempotencyKey': 'k'}
media_buy_create: SaveMediaBuyInput = {'idempotencyKey': 'k', 'sellerId': 'seller', 'products': [{'productId': 'product', 'targetingOverlay': {'geo_countries': None}}]}
search: SearchInput = {'kind': 'creative', 'filter': {'advertiserId': 'a', 'campaignId': 'c'}}
get: GetInput = {'kind': 'catalog', 'id': 'c'}
material: SaveMaterialInput = {'materialId': 'm', 'action': 'archive'}
source_missing: RefreshInventorySourceHealthInput = {}
source_wrong: RefreshInventorySourceHealthInput = {'sourceId': 42}
metrics: GetDeliveryInput = {'metrics': [42]}
status: GetStatusInput = {'unexpected': 'field'}
