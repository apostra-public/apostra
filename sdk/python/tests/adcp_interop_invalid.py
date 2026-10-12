from adcp.types import Duration, DurationUnit, Pacing
from apostra.models import GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierAttributionWindow, SaveCampaignRequestCampaignGoalDuration, SaveCampaignInput

model_as_dictionary: GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierAttributionWindow = Duration(interval=1, unit=DurationUnit.days)
campaign_seconds: SaveCampaignRequestCampaignGoalDuration = {'interval': 1, 'unit': DurationUnit.seconds.value}
upstream_pacing: SaveCampaignInput = {'idempotencyKey': 'request', 'budget': {'total': 1, 'currency': 'USD', 'pacing': Pacing.front_loaded.value}}
