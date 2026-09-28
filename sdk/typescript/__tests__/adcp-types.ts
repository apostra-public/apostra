/** Consumer composition against the pinned upstream declarations, without casts. */
import type { OptimizationGoal, Pacing } from '@adcp/sdk/types/create-media-buy'
import type { Duration } from '@adcp/sdk/types/get-media-buy-delivery'
import type {
  CatalogType,
  ContentIDType,
  EventType,
  FeedFormat,
  UpdateFrequency,
} from '@adcp/sdk/types/sync-catalogs'

import type {
  GetDeliverySuccessSchema20,
  SaveCampaignRequestDuration,
  SaveCampaignRequestEventGoal,
  SaveCampaignRequestMetricGoal,
} from '../src/generated/types.gen.js'
import type {
  Apostra,
  GetDeliveryResult,
  SaveCampaignInput,
  SaveCatalogInput,
  SaveEventSourceInput,
} from '../src/index.js'

type Exact<L, R> = 0 extends 1 & (L | R)
  ? false
  : [L] extends [R]
    ? [R] extends [L]
      ? true
      : false
    : false
type Assert<T extends true> = T

// Both directions matter: accepting an upstream value alone cannot detect a
// broadened generated enum. These are leaf types, not equivalent operations.
export type ExactLeaves = [
  Assert<Exact<NonNullable<SaveCatalogInput['type']>, CatalogType>>,
  Assert<Exact<NonNullable<SaveCatalogInput['feedFormat']>, FeedFormat>>,
  Assert<
    Exact<NonNullable<SaveCatalogInput['updateFrequency']>, UpdateFrequency>
  >,
  Assert<Exact<NonNullable<SaveCatalogInput['contentIdType']>, ContentIDType>>,
  Assert<
    Exact<NonNullable<SaveCatalogInput['conversionEvents']>[number], EventType>
  >,
  Assert<
    Exact<NonNullable<SaveEventSourceInput['eventTypes']>[number], EventType>
  >,
  Assert<
    Exact<
      SaveCampaignRequestEventGoal['eventSources'][number]['eventType'],
      EventType
    >
  >,
  Assert<
    Exact<
      SaveCampaignRequestMetricGoal['metric'],
      Extract<OptimizationGoal, { kind: 'metric' }>['metric']
    >
  >,
  Assert<Exact<GetDeliverySuccessSchema20, Duration>>,
]

export function composeCatalog(
  api: Apostra,
  type: CatalogType,
  feedFormat: FeedFormat,
  updateFrequency: UpdateFrequency,
  contentIdType: ContentIDType,
  event: EventType,
) {
  return api.saveCatalog({
    catalogId: 'catalog',
    advertiserId: 'advertiser',
    idempotencyKey: 'request',
    type,
    feedFormat,
    updateFrequency,
    contentIdType,
    conversionEvents: [event],
  })
}

export function composeGoals(event: EventType): SaveCampaignInput {
  return {
    idempotencyKey: 'request',
    optimizationGoals: [
      {
        kind: 'event',
        eventSources: [{ eventSourceId: 'source', eventType: event }],
      },
    ],
  }
}

// Results can be consumed as upstream durations, but upstream durations still
// need V3's safe-integer bound checked before sending them to an Apostra input.
export function deliveryDuration(
  result: GetDeliveryResult,
): Duration | undefined {
  if (result.report !== 'live_campaign_delivery') return undefined
  return result.deliverySummary?.aggregated_totals?.metric_aggregates?.[0]
    ?.qualifier?.attribution_window
}

export function boundaries(
  duration: Duration,
  pacing: Pacing,
  goal: Extract<OptimizationGoal, { kind: 'event' }>,
) {
  // @ts-expect-error campaign durations exclude the upstream seconds unit
  const campaignDuration: SaveCampaignRequestDuration = duration
  // @ts-expect-error upstream front_loaded is not V3 frontloaded
  const budgetPacing: NonNullable<SaveCampaignInput['budget']>['pacing'] =
    pacing
  // @ts-expect-error upstream event_sources is not V3 eventSources
  const eventGoal: SaveCampaignRequestEventGoal = goal
  void [campaignDuration, budgetPacing, eventGoal]
}
