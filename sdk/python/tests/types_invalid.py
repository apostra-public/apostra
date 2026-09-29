from apostra.models import SaveRfpRequestJ, SaveCampaignInput, SaveRfpInput, SaveLibraryRequestInput, SaveCreativeSessionInput, SaveDimensionInput, SearchInput, GetInput, SaveMaterialInput, RefreshInventorySourceHealthInput, GetDeliveryInput, GetStatusInput
nested: SaveRfpRequestJ = {'deep': [lambda: 0]}
campaign: SaveCampaignInput = {'idempotencyKey': 'k', 'channelGroups': [{'channelGroupId': 'g', 'presetId': 'ctv', 'inventory': {}}]}
rfp: SaveRfpInput = {'action': 'feedback'}
library: SaveLibraryRequestInput = {'action': 'close'}
creative: SaveCreativeSessionInput = {'operation': 'select_output', 'campaignId': 'c'}
dimension: SaveDimensionInput = {'key': 'market', 'name': 'Market', 'valuesMode': 'open', 'appliesTo': ['campaign'], 'id': '42', 'idempotencyKey': 'k'}
search: SearchInput = {'kind': 'creative', 'filter': {'advertiserId': 'a', 'campaignId': 'c'}}
get: GetInput = {'kind': 'catalog', 'id': 'c'}
material: SaveMaterialInput = {'action': 'replace_source', 'materialId': 'm', 'source': {'kind': 'inline', 'name': 'n', 'content': 'c'}}
source_missing: RefreshInventorySourceHealthInput = {}
source_wrong: RefreshInventorySourceHealthInput = {'sourceId': 42}
metrics: GetDeliveryInput = {'metrics': [42]}
status: GetStatusInput = {'unexpected': 'field'}
