import { createHmac, timingSafeEqual } from 'node:crypto'

export type WebhookSecret = string | { secret: string; acceptsUntil?: number }
export type WebhookHeaders = {
  signature: readonly string[]
  timestamp: readonly string[]
  deliveryId: readonly string[]
}
export type WebhookVerification =
  | {
      status: 'verified'
      deliveryId: string
      secretId: string
      timestamp: number
    }
  | {
      status:
        | 'malformed'
        | 'unknown_secret'
        | 'expired_secret'
        | 'invalid_signature'
        | 'invalid_clock'
        | 'stale'
    }

const webhookSignature =
  /^v1,kid=([A-Za-z0-9_-]{1,128}),hmac-sha256=([a-f0-9]{64})$/
const webhookTimestamp = /^[1-9][0-9]{9,12}$/
const webhookDeliveryId = /^[!-~]{1,128}$/
const exactlyOne = (values: unknown): string | null =>
  Array.isArray(values) && values.length === 1 && typeof values[0] === 'string'
    ? values[0]
    : null

/** Verify one duplicate-preserving V3 webhook delivery before parsing its body. */
export function verifyWebhook(input: {
  rawBody: Uint8Array | string
  headers: WebhookHeaders
  secrets: Readonly<Record<string, WebhookSecret>>
  nowUnixSeconds?: number
}): WebhookVerification {
  const nowUnixSeconds = input.nowUnixSeconds ?? Math.floor(Date.now() / 1000)
  if (!Number.isSafeInteger(nowUnixSeconds) || nowUnixSeconds < 0)
    return { status: 'invalid_clock' }
  const signatureHeader = exactlyOne(input.headers.signature)
  const timestampHeader = exactlyOne(input.headers.timestamp)
  const deliveryId = exactlyOne(input.headers.deliveryId)
  const signature = signatureHeader && webhookSignature.exec(signatureHeader)
  if (
    !signature ||
    !timestampHeader ||
    !webhookTimestamp.test(timestampHeader) ||
    !deliveryId ||
    !webhookDeliveryId.test(deliveryId)
  )
    return { status: 'malformed' }
  const timestamp = Number(timestampHeader)
  if (!Number.isSafeInteger(timestamp)) return { status: 'malformed' }
  const configured = input.secrets[signature[1]]
  if (!configured) return { status: 'unknown_secret' }
  const secret = typeof configured === 'string' ? configured : configured.secret
  const acceptsUntil =
    typeof configured === 'string' ? undefined : configured.acceptsUntil
  if (
    !secret ||
    (acceptsUntil !== undefined &&
      (!Number.isSafeInteger(acceptsUntil) || nowUnixSeconds > acceptsUntil))
  )
    return { status: 'expired_secret' }
  const body = Buffer.from(input.rawBody)
  const expected = createHmac('sha256', secret)
    .update(
      Buffer.concat([
        Buffer.from(`v1.${timestampHeader}.${deliveryId}.`),
        body,
      ]),
    )
    .digest()
  const supplied = Buffer.from(signature[2], 'hex')
  if (
    supplied.length !== expected.length ||
    !timingSafeEqual(supplied, expected)
  )
    return { status: 'invalid_signature' }
  if (Math.abs(nowUnixSeconds - timestamp) > 300) return { status: 'stale' }
  return { status: 'verified', deliveryId, secretId: signature[1], timestamp }
}
