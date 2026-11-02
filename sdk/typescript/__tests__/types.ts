import type { JsonValue } from '../src/generated/types.gen.js'
import {
  Apostra,
  type GetDeliveryResult,
  type ResponseDetails,
  type SaveBillingInput,
  type SaveCampaignInput,
  type SaveDimensionResult,
  type SaveEventSourceResult,
  type SaveRfpInput,
} from '../src/index.js'

const nested: JsonValue = { deep: [{ nested: ['value', null, 2, true] }] }
// @ts-expect-error recursive JSON cannot contain functions
const invalid: JsonValue = { deep: [() => 0] }
const campaign: SaveCampaignInput = {
  idempotencyKey: 'k',
  channelGroups: [{ channelGroupId: 'g', kind: 'preset', presetId: 'ctv' }],
}
const badCampaign: SaveCampaignInput = {
  idempotencyKey: 'k',
  channelGroups: [
    // @ts-expect-error preset and custom inventory branches cannot mix
    { channelGroupId: 'g', kind: 'preset', presetId: 'ctv', inventory: {} },
  ],
}
const billing: SaveBillingInput = {
  terms: { accepted: true, acceptedVersion: 'v1-1' },
  paymentTerms: 'net_60',
}
const badBilling: SaveBillingInput = {
  terms: { accepted: true, acceptedVersion: 'v1-1' },
  // @ts-expect-error the earlier operation field is no longer published
  operation: 'terms',
}
const api = new Apostra({ apiKey: 'test' })
const delivery: Promise<GetDeliveryResult> = api.getDelivery({})
const deliveryWithResponse: Promise<ResponseDetails<GetDeliveryResult>> =
  api.getDeliveryWithResponse({})
function eventSourceFields(result: SaveEventSourceResult): [string, string] {
  return [result.advertiserId, result.eventSources[0]?.eventSourceId ?? '']
}
function dimensionFields(result: SaveDimensionResult): [string, number] {
  return [result.object.id, result.object.usage.advertiser]
}
// @ts-expect-error generated write methods require a caller-owned key
const writeWithoutKey = api.saveAsk({
  id: 'ask',
  requester: { state: 'accepted' },
})
// @ts-expect-error detailed dispatch must also require a caller-owned key
const detailedWriteWithoutKey = api.requestDetailed('save_ask', {
  kind: 'update',
  id: 'ask',
  requester: { state: 'accepted' },
})
const detailedWrite = api.requestDetailed(
  'save_ask',
  { kind: 'update', id: 'ask', requester: { state: 'accepted' } },
  { idempotencyKey: 'ask' },
)
// @ts-expect-error generated response variants preserve write-key requirements
const writeWithResponseWithoutKey = api.saveAskWithResponse({
  id: 'ask',
  requester: { state: 'accepted' },
})
// @ts-expect-error missing action fields
const bad: SaveRfpInput = { action: 'feedback' }
void [
  nested,
  invalid,
  campaign,
  badCampaign,
  billing,
  badBilling,
  delivery,
  deliveryWithResponse,
  eventSourceFields,
  dimensionFields,
  writeWithoutKey,
  detailedWriteWithoutKey,
  detailedWrite,
  writeWithResponseWithoutKey,
  bad,
]
