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
  GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierAttributionWindow,
  SaveCampaignRequestCampaignEventGoal,
  SaveCampaignRequestCampaignGoalDuration,
  SaveCampaignRequestCampaignMetricGoal,
} from '../src/generated/types.gen.js'
import type {
  Apostra,
  GetDeliveryResult,
  RequestBuyerChildAccountInput,
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
    Exact<
      NonNullable<
        SaveEventSourceInput['eventSources'][number]['eventTypes']
      >[number],
      EventType
    >
  >,
  Assert<
    Exact<
      SaveCampaignRequestCampaignEventGoal['event_sources'][number]['event_type'],
      EventType
    >
  >,
  Assert<
    Exact<
      SaveCampaignRequestCampaignMetricGoal['metric'],
      Extract<OptimizationGoal, { kind: 'metric' }>['metric']
    >
  >,
  Assert<
    Exact<
      GetDeliverySuccessDeliverySummaryAggregatedTotalsMetricAggregatesItemQualifierAttributionWindow,
      Duration
    >
  >,
]

export function composeCatalog(
  api: Apostra,
  type: CatalogType,
  feedFormat: FeedFormat,
  updateFrequency: UpdateFrequency,
  contentIdType: ContentIDType,
  event: EventType,
) {
  return api.saveCatalog(
    {
      catalogId: 'catalog',
      advertiserId: 'advertiser',
      idempotencyKey: 'request',
      type,
      feedFormat,
      updateFrequency,
      contentIdType,
      conversionEvents: [event],
    },
    { idempotencyKey: 'request' },
  )
}

export function requestBuyerChildAccount(api: Apostra): Promise<unknown> {
  const input: RequestBuyerChildAccountInput = {
    parentId: 'parent',
    name: 'Buyer',
  }
  return api.requestBuyerChildAccount(input, { idempotencyKey: 'request' })
}

export function composeGoals(event: EventType): SaveCampaignInput {
  return {
    idempotencyKey: 'request',
    optimizationGoals: [
      {
        kind: 'event',
        event_sources: [{ event_source_id: 'source', event_type: event }],
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
  const campaignDuration: SaveCampaignRequestCampaignGoalDuration = duration
  // @ts-expect-error upstream front_loaded is not V3 frontloaded
  const budgetPacing: NonNullable<SaveCampaignInput['budget']>['pacing'] =
    pacing
  // @ts-expect-error upstream attribution windows may omit post_click, use
  // seconds, or name a model, none of which a campaign stores
  const eventGoal: SaveCampaignRequestCampaignEventGoal = goal
  void [campaignDuration, budgetPacing, eventGoal]
}
