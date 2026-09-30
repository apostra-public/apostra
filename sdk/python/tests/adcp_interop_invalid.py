from adcp.types import Duration, DurationUnit, Pacing
from apostra.models import GetDeliverySuccessSchema21, SaveCampaignRequestDuration, SaveCampaignInput

model_as_dictionary: GetDeliverySuccessSchema21 = Duration(interval=1, unit=DurationUnit.days)
campaign_seconds: SaveCampaignRequestDuration = {'interval': 1, 'unit': DurationUnit.seconds.value}
upstream_pacing: SaveCampaignInput = {'idempotencyKey': 'request', 'budget': {'total': 1, 'currency': 'USD', 'pacing': Pacing.front_loaded.value}}
