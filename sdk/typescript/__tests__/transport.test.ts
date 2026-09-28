import { describe, expect, it, vi } from 'vitest'

import { operations } from '../src/generated/metadata.js'
import {
  Apostra,
  ApostraError,
  InFlightReceiptError,
  openHandoff,
  ProtocolError,
  paginate,
  poll,
} from '../src/index.js'

const response = (data: unknown) => Response.json({ data, error: null })
const mockFetch = (
  fn: (url: string, init: RequestInit) => Response | Promise<Response>,
) =>
  vi.fn<typeof fetch>((url, init) =>
    Promise.resolve(fn(String(url), init ?? {})),
  )

describe('HTTP transport', () => {
  it('serialises input, targets explicit accounts and obtains a fresh bearer each call', async () => {
    const seen: RequestInit[] = []
    const fetcher = mockFetch((_url, init) => {
      seen.push(init)
      return response({})
    })
    let tokens = 0
    const client = new Apostra({
      tokenProvider: () => `token-${++tokens}`,
      accountId: '12',
      fetch: fetcher,
    })
    await client.getStatus({})
    await client.saveAsk(
      { id: 'ask-1', requesterState: 'accepted' },
      { accountId: '34', idempotencyKey: 'ask-1' },
    )
    expect(new Headers(seen[0].headers).get('authorization')).toBe(
      'Bearer token-1',
    )
    expect(new Headers(seen[1].headers).get('X-SCOPE3-CUSTOMER-ID')).toBe('34')
    expect(new Headers(seen[1].headers).get('user-agent')).toBe(
      'apostra-typescript/0.5.0',
    )
    expect(new Headers(seen[1].headers).get('idempotency-key')).toBe('ask-1')
    expect(seen[1].body).toBe('{"id":"ask-1","requesterState":"accepted"}')
    expect(seen[1].redirect).toBe('error')
    expect(JSON.stringify(client)).not.toContain('token')
  })
  it('returns typed errors without replaying a mutation or exposing the message in the exception', async () => {
    const fetcher = mockFetch(() =>
      Response.json(
        {
          data: null,
          error: {
            code: 'RATE_LIMITED',
            message: 'secret',
            retry_after: 12,
            recovery: 'transient',
          },
        },
        { status: 429, headers: { 'x-request-id': 'request-1' } },
      ),
    )
    const client = new Apostra({ apiKey: 'private-key', fetch: fetcher })
    const error = await client
      .saveAsk(
        { id: 'ask-1', requesterState: 'accepted' },
        { idempotencyKey: 'ask-1' },
      )
      .catch((e) => e)
    expect(error).toBeInstanceOf(ApostraError)
    expect(error.error.retry_after).toBe(12)
    expect(error.requestId).toBe('request-1')
    expect(String(error)).not.toMatch(/secret|private-key/)
    expect(fetcher).toHaveBeenCalledTimes(1)
  })
  it('fails safely on malformed success and HTML failures', async () => {
    for (const value of [
      Response.json({ data: {} }),
      new Response('secret', { status: 502 }),
    ]) {
      await expect(
        new Apostra({ apiKey: 'key', fetch: mockFetch(() => value) }).getStatus(
          {},
        ),
      ).rejects.toBeInstanceOf(ProtocolError)
    }
  })
  it('does not treat an in-flight write receipt as a completed result or replay it', async () => {
    const fetcher = mockFetch(() =>
      Response.json(
        {
          data: {
            receipt: {
              id: '4e8d0bf9-419a-4eb4-a6ee-3438f7bc89a1',
              state: 'uncertain',
              stateVersion: 2,
              stateChangedAt: '2026-09-28T10:00:00.000Z',
            },
          },
          error: null,
        },
        { status: 202, headers: { 'retry-after': '3', 'x-request-id': 'r1' } },
      ),
    )
    const api = new Apostra({ apiKey: 'key', fetch: fetcher })
    const error = await api
      .saveAsk(
        { id: 'ask-1', requesterState: 'accepted' },
        { idempotencyKey: 'ask-1' },
      )
      .catch((value: unknown) => value)
    expect(error).toBeInstanceOf(InFlightReceiptError)
    expect(error).toMatchObject({
      status: 202,
      requestId: 'r1',
      retryAfterMs: 3000,
      receipt: {
        id: '4e8d0bf9-419a-4eb4-a6ee-3438f7bc89a1',
        state: 'uncertain',
        stateVersion: 2,
        stateChangedAt: '2026-09-28T10:00:00.000Z',
      },
    })
    expect(fetcher).toHaveBeenCalledTimes(1)
  })
  it('cancels before credentials, during provider resolution and during fetch', async () => {
    const provider = vi.fn(() => new Promise<string>(() => {}))
    const before = new AbortController()
    before.abort()
    const client = new Apostra({ tokenProvider: provider })
    await expect(
      client.getStatus({}, { signal: before.signal }),
    ).rejects.toThrow()
    expect(provider).not.toHaveBeenCalled()
    await expect(client.getStatus({}, { timeoutMs: 5 })).rejects.toThrow()
    const fetcher = mockFetch(
      (_url, init) =>
        new Promise((_resolve, reject) =>
          init.signal?.addEventListener('abort', () =>
            reject(init.signal?.reason),
          ),
        ),
    )
    await expect(
      new Apostra({ apiKey: 'key', fetch: fetcher }).getStatus(
        {},
        { timeoutMs: 5 },
      ),
    ).rejects.toThrow()
  })
  it('encodes document paths, query and binary download', async () => {
    const fetcher = mockFetch(() => new Response('document bytes'))
    const client = new Apostra({ accessToken: 'm2m', fetch: fetcher })
    expect(
      new TextDecoder().decode(
        await client.downloadV3PublicDocumentRevision({
          documentId: 'a/b',
          revisionId: 'v1',
        }),
      ),
    ).toBe('document bytes')
    expect(String(fetcher.mock.calls[0][0])).toContain(
      '/documents/a%2Fb/revisions/v1/download',
    )
  })
  it('exposes every generated operation', () => {
    const generatedOperationIds = Object.keys(operations)
    for (const id of generatedOperationIds) {
      const name = id.replace(/_([a-z])/g, (_, c: string) => c.toUpperCase())
      expect(
        typeof (Apostra.prototype as unknown as Record<string, unknown>)[name],
      ).toBe('function')
    }
  })
})

it('preserves cursors and rejects a repeated cursor', async () => {
  const reads: string[] = []
  const pages = paginate(
    async (cursor) => {
      reads.push(cursor ?? '')
      return { next: cursor ? '' : 'next' }
    },
    (p) => p.next,
  )
  expect((await collect(pages)).length).toBe(2)
  expect(reads).toEqual(['', 'next'])
  await expect(
    collect(
      paginate(
        async () => ({ next: 'same' }),
        (p) => p.next,
      ),
    ),
  ).rejects.toBeInstanceOf(ProtocolError)
  const repeated = paginate(
    async () => ({ next: 'same' }),
    (p) => p.next,
  )
  await expect(repeated.next()).resolves.toMatchObject({ done: false })
  await expect(repeated.next()).rejects.toBeInstanceOf(ProtocolError)
})
it('polls only by the supplied predicate and honours cancellation', async () => {
  let n = 0
  expect(
    await poll(
      async () => ++n,
      (x) => x === 2,
      { signal: AbortSignal.timeout(100), intervalMs: 1 },
    ),
  ).toBe(2)
  await expect(
    poll(
      async () => 0,
      () => false,
      { signal: AbortSignal.timeout(5), intervalMs: 50 },
    ),
  ).rejects.toThrow()
})
it('returns URLs in headless mode and requires an explicit opener', async () => {
  expect(await openHandoff('https://example.test/task')).toBe(
    'https://example.test/task',
  )
  const opener = vi.fn()
  await openHandoff('https://example.test/task', opener)
  expect(opener).toHaveBeenCalledOnce()
  await expect(openHandoff('javascript:alert(1)')).rejects.toThrow()
})

async function collect<T>(items: AsyncIterable<T>): Promise<T[]> {
  const result: T[] = []
  for await (const item of items) result.push(item)
  return result
}

describe('credential and replay boundaries', () => {
  it('leaves refresh to the provider after a 401 without replaying the request', async () => {
    const provider = vi
      .fn()
      .mockReturnValueOnce('expired')
      .mockReturnValueOnce('fresh')
    const fetcher = mockFetch((_url, init) =>
      new Headers(init.headers).get('authorization') === 'Bearer expired'
        ? Response.json(
            { data: null, error: { code: 'UNAUTHORIZED', message: 'expired' } },
            { status: 401 },
          )
        : response({}),
    )
    const api = new Apostra({ tokenProvider: provider, fetch: fetcher })
    await expect(api.getStatus({})).rejects.toMatchObject({ status: 401 })
    expect(fetcher).toHaveBeenCalledTimes(1)
    expect(provider).toHaveBeenCalledTimes(1)
    await api.getStatus({})
    expect(provider).toHaveBeenCalledTimes(2)
  })

  it('preserves the caller idempotency key and account on an explicit retry', async () => {
    const fetcher = mockFetch(() =>
      Response.json(
        { data: null, error: { code: 'UNAVAILABLE', message: 'try later' } },
        { status: 503 },
      ),
    )
    const api = new Apostra({ apiKey: 'key', accountId: '12', fetch: fetcher })
    const input = {
      catalogId: 'catalog-1',
      advertiserId: '123',
      name: 'Example',
      idempotencyKey: 'original-key',
    }
    await expect(
      api.saveCatalog(
        { ...input, type: 'product', items: [] },
        { idempotencyKey: 'original-key' },
      ),
    ).rejects.toMatchObject({ status: 503 })
    expect(fetcher).toHaveBeenCalledTimes(1)
    await expect(
      api.saveCatalog(
        { ...input, type: 'product', items: [] },
        { idempotencyKey: 'original-key' },
      ),
    ).rejects.toMatchObject({ status: 503 })
    const requests = fetcher.mock.calls.map(([, init]) => init)
    expect(requests[1]?.body).toBe(requests[0]?.body)
    expect(JSON.parse(String(requests[0]?.body)).idempotencyKey).toBe(
      'original-key',
    )
    expect(new Headers(requests[1]?.headers).get('X-SCOPE3-CUSTOMER-ID')).toBe(
      '12',
    )
    expect(new Headers(requests[1]?.headers).get('idempotency-key')).toBe(
      'original-key',
    )
  })

  it('does not dispatch a write without a caller-supplied idempotency key', async () => {
    const fetcher = mockFetch(() => response({}))
    const api = new Apostra({ apiKey: 'key', fetch: fetcher })
    await expect(
      api.saveAsk({ id: 'ask-1', requesterState: 'accepted' }, {} as never),
    ).rejects.toThrow('idempotencyKey')
    expect(fetcher).not.toHaveBeenCalled()
  })

  it('rejects invalid local options before requesting credentials', async () => {
    const provider = vi.fn(() => 'key')
    const api = new Apostra({ tokenProvider: provider })
    await expect(api.getStatus({}, { accountId: '0' })).rejects.toThrow(
      TypeError,
    )
    await expect(api.getStatus({}, { timeoutMs: 0 })).rejects.toThrow(TypeError)
    expect(provider).not.toHaveBeenCalled()
  })
})

describe('cancellation throughout a response', () => {
  it('bounds an injected fetch that ignores its signal', async () => {
    const fetcher = mockFetch(() => new Promise<Response>(() => {}))
    await expect(
      new Apostra({ apiKey: 'key', fetch: fetcher }).getStatus(
        {},
        { timeoutMs: 5 },
      ),
    ).rejects.toMatchObject({ name: 'TimeoutError' })
    expect(fetcher).toHaveBeenCalledTimes(1)
  })

  it('preserves abort reasons while consuming JSON', async () => {
    const controller = new AbortController()
    const value = response({})
    const reason = new Error('caller cancelled')
    vi.spyOn(value, 'json').mockImplementation(() => {
      controller.abort(reason)
      return Promise.reject(reason)
    })
    await expect(
      new Apostra({ apiKey: 'key', fetch: mockFetch(() => value) }).getStatus(
        {},
        { signal: controller.signal },
      ),
    ).rejects.toBe(reason)
  })

  it('bounds binary body consumption', async () => {
    const value = new Response('bytes')
    vi.spyOn(value, 'arrayBuffer').mockImplementation(
      () => new Promise(() => {}),
    )
    await expect(
      new Apostra({
        apiKey: 'key',
        fetch: mockFetch(() => value),
      }).downloadV3PublicDocumentRevision(
        { documentId: 'doc', revisionId: 'rev' },
        { timeoutMs: 5 },
      ),
    ).rejects.toMatchObject({ name: 'TimeoutError' })
  })

  it('preserves body transport errors', async () => {
    const failure = new TypeError('connection terminated')
    const value = new Response(
      new ReadableStream({
        start(controller) {
          controller.error(failure)
        },
      }),
    )
    await expect(
      new Apostra({ apiKey: 'key', fetch: mockFetch(() => value) }).getStatus(
        {},
      ),
    ).rejects.toBe(failure)
  })

  it('passes the cancellation signal into polling and pagination reads', async () => {
    for (const kind of ['poll', 'paginate']) {
      const controller = new AbortController()
      const reason = new Error('stop')
      let observed: AbortSignal | undefined
      const read = (signal?: AbortSignal): Promise<number> => {
        observed = signal
        controller.abort(reason)
        return new Promise(() => {})
      }
      const pending =
        kind === 'poll'
          ? poll(read, () => false, { signal: controller.signal })
          : collect(
              paginate(
                (_cursor, signal) => read(signal),
                () => 'next',
                controller.signal,
              ),
            )
      await expect(pending).rejects.toBe(reason)
      expect(observed).toBe(controller.signal)
    }
  })

  it('does not retry failed polling reads', async () => {
    const failure = new Error('read failed')
    const read = vi.fn(async () => {
      throw failure
    })
    await expect(
      poll(read, () => false, { signal: new AbortController().signal }),
    ).rejects.toBe(failure)
    expect(read).toHaveBeenCalledTimes(1)
  })
})
