import { Apostra } from '@apostra/sdk'

function required(name: string): string {
  const value = process.env[name]
  if (!value) throw new Error(`${name} is required`)
  return value
}

const api = new Apostra({
  apiKey: required('APOSTRA_API_KEY'),
  accountId: process.env.APOSTRA_ACCOUNT_ID,
  baseUrl: process.env.APOSTRA_BASE_URL ?? 'https://api.apostra.com/api/v3',
})
const campaignId = required('APOSTRA_CAMPAIGN_ID')

// Verify the credential and discover the resolved account before any write.
const status = await api.getStatus({})
if (!status.account)
  throw new Error('The credential did not resolve an account')

// A unique key belongs to this exact preview request. Reuse it only to retry
// the same request after an uncertain response.
const previewKey = crypto.randomUUID()
const preview = await api.saveCampaign(
  {
    campaignId,
    desiredPhase: 'active',
    idempotencyKey: previewKey,
  },
  { idempotencyKey: previewKey },
)

// Inspect `preview` before confirming. Confirmation is deliberately opt-in so
// running the sample against the synthetic seller remains a preview by default.
if (process.env.APOSTRA_CONFIRM_LAUNCH === 'true') {
  const confirmKey = crypto.randomUUID()
  await api.saveCampaign(
    {
      campaignId,
      desiredPhase: 'active',
      confirmLaunch: true,
      idempotencyKey: confirmKey,
    },
    { idempotencyKey: confirmKey },
  )
}

const delivery = await api.getDelivery({
  report: 'campaign_delivery',
  filters: { campaignId },
  range: {
    startDate: required('APOSTRA_START_DATE'),
    endDate: required('APOSTRA_END_DATE'),
  },
  limit: 100,
})

void [preview, delivery]
