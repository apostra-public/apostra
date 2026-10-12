import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

import { expect, it } from 'vitest'

import { verifyWebhook } from '../src/webhooks.js'

type WebhookVector = {
  name: string
  rawBodyUtf8?: string
  headers?: {
    signature?: string | string[]
    timestamp?: string | string[]
    deliveryId?: string | string[]
  }
  expectedStatus: string
  nowUnixSeconds?: number
  sameAs?: string
}
const webhookVectors = JSON.parse(
  readFileSync(
    fileURLToPath(new URL('./fixtures/v3-vectors.json', import.meta.url)),
    'utf8',
  ),
) as {
  nowUnixSeconds: number
  secrets: Array<{ id: string; secret: string; acceptsUntil?: number }>
  vectors: WebhookVector[]
}

it('keeps the browser-safe root free of Node imports', () => {
  for (const file of ['../src/index.ts', '../src/transport.ts']) {
    const source = readFileSync(
      fileURLToPath(new URL(file, import.meta.url)),
      'utf8',
    )
    expect(source).not.toMatch(/from ['"]node:/)
  }
})

it.each(webhookVectors.vectors)(
  'matches the shared webhook vector: $name',
  (vector) => {
    const source = vector.sameAs
      ? webhookVectors.vectors.find(
          (candidate) => candidate.name === vector.sameAs,
        )
      : vector
    if (!source?.rawBodyUtf8 || !source.headers)
      throw new Error(`Invalid shared webhook vector: ${vector.name}`)
    const header = (value: string | string[] | undefined) =>
      value === undefined ? [] : Array.isArray(value) ? value : [value]
    expect(
      verifyWebhook({
        rawBody: source.rawBodyUtf8,
        headers: {
          signature: header(source.headers.signature),
          timestamp: header(source.headers.timestamp),
          deliveryId: header(source.headers.deliveryId),
        },
        secrets: Object.fromEntries(
          webhookVectors.secrets.map((secret) => [
            secret.id,
            { secret: secret.secret, acceptsUntil: secret.acceptsUntil },
          ]),
        ),
        nowUnixSeconds: vector.nowUnixSeconds ?? webhookVectors.nowUnixSeconds,
      }).status,
    ).toBe(vector.expectedStatus)
  },
)
