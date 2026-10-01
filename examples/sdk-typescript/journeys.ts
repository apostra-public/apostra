import { Apostra, paginate, type GetDeliveryInput } from '@apostra/sdk'

// Supply synthetic-account credentials through the environment, never source.
const api = new Apostra({
  apiKey: process.env.APOSTRA_API_KEY!,
  accountId: process.env.APOSTRA_ACCOUNT_ID!,
  baseUrl: process.env.APOSTRA_BASE_URL,
})
const signal = AbortSignal.timeout(30_000)

// Journey 1: inspect readiness and discover inventory sources.
const status = await api.getStatus({}, {signal})
const sources = await api.search({kind:'inventory_source', limit:20}, {signal})
if (!status.account || !sources.objects) throw new Error('Missing discovery result')

// Journey 2: read every delivery page for a known synthetic campaign.
const query: GetDeliveryInput = {
  report:'campaign_delivery',
  filters:{campaignId:process.env.APOSTRA_CAMPAIGN_ID!},
  range:{startDate:process.env.APOSTRA_START_DATE!,endDate:process.env.APOSTRA_END_DATE!},
  limit:100,
}
let pages=0
let observedImpressions = 0
for await (const page of paginate(
  (cursor, signal)=>api.getDelivery({...query,...(cursor ? {cursor}: {})}, {signal}),
  page=>page.page?.nextCursor,
  signal,
)) {
  pages++
  if (page.report === 'live_campaign_delivery') continue
  const impressions = page.totals?.metrics.impressions?.value
  if (typeof impressions === 'number' && Number.isFinite(impressions)) {
    observedImpressions = Math.max(observedImpressions, impressions)
  }
}
if (pages===0) throw new Error('Missing delivery result')
const minimumImpressions = Number(process.env.APOSTRA_MIN_IMPRESSIONS ?? '0')
if (!Number.isFinite(minimumImpressions) || minimumImpressions < 0) {
  throw new Error('APOSTRA_MIN_IMPRESSIONS must be a non-negative number')
}
if (observedImpressions < minimumImpressions) {
  throw new Error(`Delivery impressions ${observedImpressions} are below ${minimumImpressions}`)
}
