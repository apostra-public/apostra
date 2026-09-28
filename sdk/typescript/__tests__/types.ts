import type { SaveRfpRequestJ } from '../src/generated/types.gen.js'
import {
  Apostra,
  type GetDeliveryResult,
  type SaveCampaignInput,
  type SaveRfpInput,
} from '../src/index.js'

const nested: SaveRfpRequestJ = { deep: [{ nested: ['value', null, 2, true] }] }
// @ts-expect-error recursive JSON cannot contain functions
const invalid: SaveRfpRequestJ = { deep: [() => 0] }
const campaign: SaveCampaignInput = {
  idempotencyKey: 'k',
  channelGroups: [{ channelGroupId: 'g', presetId: 'ctv' }],
}
const badCampaign: SaveCampaignInput = {
  idempotencyKey: 'k',
  // @ts-expect-error preset and custom inventory branches cannot mix
  channelGroups: [{ channelGroupId: 'g', presetId: 'ctv', inventory: {} }],
}
const api = new Apostra({ apiKey: 'test' })
const delivery: Promise<GetDeliveryResult> = api.getDelivery({})
// @ts-expect-error missing action fields
const bad: SaveRfpInput = { action: 'feedback' }
void [nested, invalid, campaign, badCampaign, delivery, bad]
