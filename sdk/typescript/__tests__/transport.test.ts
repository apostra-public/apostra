import { afterEach, describe, expect, it, vi } from 'vitest'

import { operations, version } from '../src/generated/metadata.js'
import {
  Apostra,
  ApostraError,
  getHandoff,
  InFlightReceiptError,
  m2mTokenProvider,
  openHandoff,
  ProtocolError,
  paginate,
  poll,
  RateLimitError,
  settle,
  TimeoutError,
} from '../src/index.js'

const response = (data: unknown) => Response.json({ data, error: null })
const mockFetch = (
  fn: (url: string, init: RequestInit) => Response | Promise<Response>,
) =>
  vi.fn<typeof fetch>((url, init) =>
    Promise.resolve(fn(String(url), init ?? {})),
  )

afterEach(() => {
  vi.unstubAllEnvs()
  vi.unstubAllGlobals()
  vi.restoreAllMocks()
})

describe('HTTP transport', () => {
  it('caches M2M tokens, refreshes before expiry and coalesces concurrent refreshes', async () => {
    vi.useFakeTimers()
    try {
      vi.setSystemTime(new Date('2026-10-01T00:00:00.000Z'))
      const fetcher = mockFetch(() =>
        Response.json({
          access_token: `token-${fetcher.mock.calls.length}`,
          expires_in: 120,
        }),
      )
      const provider = m2mTokenProvider({
        clientId: 'client',
        clientSecret: 'secret',
        scope: ['interchange:read', 'interchange:write'],
        fetch: fetcher,
      })
      await expect(Promise.all([provider(), provider()])).resolves.toEqual([
        'token-1',
        'token-1',
      ])
      expect(fetcher).toHaveBeenCalledTimes(1)
      const request = fetcher.mock.calls[0] as [RequestInfo | URL, RequestInit]
      expect(request[0]).toBe('https://identity.scope3.com/oauth2/token')
      expect(new Headers(request[1].headers).get('authorization')).toBeNull()
      expect(new URLSearchParams(String(request[1].body))).toEqual(
        new URLSearchParams({
          client_id: 'client',
          client_secret: 'secret',
          grant_type: 'client_credentials',
          scope: 'interchange:read interchange:write',
        }),
      )
      expect(await provider()).toBe('token-1')
      vi.advanceTimersByTime(61_000)
      expect(await provider()).toBe('token-2')
      expect(fetcher).toHaveBeenCalledTimes(2)
    } finally {
      vi.useRealTimers()
    }
  })
  it('does not expose M2M secrets when a token request fails', async () => {
    const provider = m2mTokenProvider({
      clientId: 'client',
      clientSecret: 'secret-value',
      scope: 'interchange:read',
      fetch: mockFetch(() => new Response('secret-value', { status: 401 })),
    })
    await expect(provider()).rejects.toThrow('M2M token request failed (401)')
    await Promise.resolve(provider()).catch((error: unknown) =>
      expect(String(error)).not.toContain('secret-value'),
    )
  })
  it('bounds M2M token refreshes and permits a later refresh', async () => {
    const controller = new AbortController()
    const timeout = vi
      .spyOn(AbortSignal, 'timeout')
      .mockReturnValue(controller.signal)
    const fetcher = vi.fn<typeof fetch>(
      (_url, init) =>
        new Promise((_resolve, reject) => {
          const signal = init?.signal
          signal?.addEventListener('abort', () => reject(signal.reason))
        }),
    )
    const provider = m2mTokenProvider({
      clientId: 'client',
      clientSecret: 'secret',
      scope: 'interchange:read',
      fetch: fetcher,
      timeoutMs: 1_000,
    })

    const pending = provider()
    expect(timeout).toHaveBeenCalledWith(1_000)
    controller.abort(new DOMException('deadline exceeded', 'TimeoutError'))
    await expect(pending).rejects.toBeInstanceOf(TimeoutError)

    fetcher.mockResolvedValueOnce(
      Response.json({ access_token: 'fresh-token', expires_in: 120 }),
    )
    await expect(provider()).resolves.toBe('fresh-token')
    expect(fetcher).toHaveBeenCalledTimes(2)
  })
  it('uses environment defaults, lets explicit options win and keeps HTTPS validation', async () => {
    vi.stubEnv('APOSTRA_API_KEY', 'environment-key')
    vi.stubEnv('APOSTRA_ACCOUNT_ID', '12')
    vi.stubEnv('APOSTRA_BASE_URL', 'https://environment.example')
    const fetcher = mockFetch(() => response({}))
    vi.stubGlobal('fetch', fetcher)

    await new Apostra().getStatus()
    const environmentRequest = fetcher.mock.calls[0] as [
      RequestInfo | URL,
      RequestInit,
    ]
    expect(environmentRequest[0]).toBe(
      'https://environment.example/tools/get_status',
    )
    expect(
      new Headers(environmentRequest[1].headers).get('authorization'),
    ).toBe('Bearer environment-key')
    expect(
      new Headers(environmentRequest[1].headers).get('X-SCOPE3-CUSTOMER-ID'),
    ).toBe('12')

    await new Apostra({
      accessToken: 'explicit-token',
      accountId: '34',
      baseUrl: 'https://explicit.example',
      fetch: fetcher,
    }).getStatus()
    const explicitRequest = fetcher.mock.calls[1] as [
      RequestInfo | URL,
      RequestInit,
    ]
    expect(explicitRequest[0]).toBe('https://explicit.example/tools/get_status')
    expect(new Headers(explicitRequest[1].headers).get('authorization')).toBe(
      'Bearer explicit-token',
    )
    expect(
      new Headers(explicitRequest[1].headers).get('X-SCOPE3-CUSTOMER-ID'),
    ).toBe('34')

    vi.stubEnv('APOSTRA_BASE_URL', 'http://not-loopback.example')
    expect(() => new Apostra()).toThrow('Use an HTTPS base URL')
  })

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
      `apostra-typescript/${version}`,
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
    const client = new Apostra({
      apiKey: 'private-key',
      fetch: fetcher,
      maxRetries: 0,
    })
    const error = await client
      .saveAsk(
        { id: 'ask-1', requesterState: 'accepted' },
        { idempotencyKey: 'ask-1' },
      )
      .catch((e) => e)
    expect(error).toBeInstanceOf(ApostraError)
    expect(error).toBeInstanceOf(RateLimitError)
    expect(error.error.retry_after).toBe(12)
    expect(error.requestId).toBe('request-1')
    expect(error).toMatchObject({
      code: 'RATE_LIMITED',
      recovery: 'transient',
      retryAfter: 12,
      retryable: true,
    })
    expect(String(error)).toContain('RATE_LIMITED')
    expect(String(error)).toContain('request-1')
    expect(String(error)).not.toMatch(/secret|private-key/)
    expect(fetcher).toHaveBeenCalledTimes(1)
  })
  it('uses one caller key for the header and generated body field', async () => {
    const fetcher = mockFetch(() => response({}))
    const api = new Apostra({ apiKey: 'key', fetch: fetcher })
    await api.requestBuyerChildAccount(
      { parentId: '1', name: 'Buyer' } as never,
      { idempotencyKey: 'request-1' },
    )
    expect(
      new Headers(fetcher.mock.calls[0][1]?.headers).get('idempotency-key'),
    ).toBe('request-1')
    expect(fetcher.mock.calls[0][1]?.body).toBe(
      '{"parentId":"1","name":"Buyer","idempotencyKey":"request-1"}',
    )
    await api.requestBuyerChildAccount(
      { parentId: '1', name: 'Buyer', idempotencyKey: 'request-1' },
      { idempotencyKey: 'request-1' },
    )
    expect(fetcher.mock.calls[1][1]?.body).toBe(
      '{"parentId":"1","name":"Buyer","idempotencyKey":"request-1"}',
    )
    await expect(
      api.requestBuyerChildAccount(
        { parentId: '1', name: 'Buyer', idempotencyKey: 'other' },
        { idempotencyKey: 'request-1' },
      ),
    ).rejects.toThrow('idempotencyKey must match')
    expect(fetcher).toHaveBeenCalledTimes(2)
  })
  it('fails safely on malformed success and HTML failures', async () => {
    for (const value of [
      Response.json({ data: {} }),
      new Response('secret', { status: 502 }),
    ]) {
      await expect(
        new Apostra({
          apiKey: 'key',
          fetch: mockFetch(() => value),
          maxRetries: 0,
        }).getStatus({}),
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
    await expect(client.getStatus({}, { timeoutMs: 5 })).rejects.toBeInstanceOf(
      TimeoutError,
    )
    const cancellation = new AbortController()
    const reason = new Error('caller cancelled')
    const pending = new Apostra({ tokenProvider: provider }).getStatus(
      {},
      { signal: cancellation.signal, timeoutMs: 1000 },
    )
    cancellation.abort(reason)
    await expect(pending).rejects.toBe(reason)
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
  it('returns successful data with request metadata through generated methods', async () => {
    const client = new Apostra({
      apiKey: 'key',
      fetch: mockFetch(() =>
        Response.json(
          { data: { ready: true }, error: null },
          {
            headers: {
              'content-type': 'application/json',
              'x-request-id': 'request-1',
            },
          },
        ),
      ),
    })
    const response = await client.getStatusWithResponse({})
    expect(response.data).toEqual({ ready: true })
    expect(response.requestId).toBe('request-1')
    expect(response.headers.get('content-type')).toContain('application/json')
  })
  it('exposes every generated operation', () => {
    const generatedOperationIds = Object.keys(operations)
    for (const id of generatedOperationIds) {
      const name = id.replace(/_([a-z])/g, (_, c: string) => c.toUpperCase())
      expect(
        typeof (Apostra.prototype as unknown as Record<string, unknown>)[name],
      ).toBe('function')
      expect(
        typeof (Apostra.prototype as unknown as Record<string, unknown>)[
          `${name}WithResponse`
        ],
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
it('narrows supported human handoffs and opens only their supplied URL', async () => {
  const handoff = getHandoff({
    humanHandoff: {
      kind: 'human_action_required',
      url: 'https://example.test/task',
      expiresAt: '2026-10-01T00:05:00.000Z',
      resume: {
        kind: 'manual',
        reason:
          'This Page has no durable completion receipt. Read the affected object before continuing; opening or closing the browser is not completion.',
      },
    },
  })
  expect(handoff).toMatchObject({
    kind: 'human_action_required',
    url: 'https://example.test/task',
  })
  expect(
    getHandoff({ humanHandoff: { kind: 'human_action_unavailable' } }),
  ).toBe(null)
  expect(
    getHandoff({
      humanHandoff: {
        kind: 'human_action_required',
        url: 'https://example.test/task',
        expiresAt: '2026-10-01T00:05:00.000Z',
        resume: {},
      },
    }),
  ).toBe(null)
  if (!handoff) throw new Error('Expected a human handoff')
  expect(await openHandoff(handoff)).toBe('https://example.test/task')
  const opener = vi.fn()
  await openHandoff(handoff, opener)
  expect(opener).toHaveBeenCalledOnce()
  await expect(openHandoff('javascript:alert(1)')).rejects.toThrow()
})

async function collect<T>(items: AsyncIterable<T>): Promise<T[]> {
  const result: T[] = []
  for await (const item of items) result.push(item)
  return result
}

describe('credential and replay boundaries', () => {
  it.each([400, 401, 403])(
    'does not replay a transient-hinted %i response',
    async (status) => {
      const fetcher = mockFetch(() =>
        Response.json(
          {
            data: null,
            error: {
              code: 'REQUEST_REJECTED',
              message: 'do not replay',
              recovery: 'transient',
            },
          },
          { status },
        ),
      )
      await expect(
        new Apostra({ apiKey: 'key', fetch: fetcher }).getStatus({}),
      ).rejects.toMatchObject({ status, retryable: true })
      expect(fetcher).toHaveBeenCalledTimes(1)
    },
  )

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
    const api = new Apostra({
      apiKey: 'key',
      accountId: '12',
      fetch: fetcher,
      maxRetries: 0,
    })
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

  it('retries transient reads and caller-keyed writes with the original payload', async () => {
    const random = vi.spyOn(Math, 'random').mockReturnValue(0)
    const fetcher = mockFetch(
      vi
        .fn()
        .mockReturnValueOnce(
          Response.json(
            { data: null, error: { code: 'UNAVAILABLE', message: 'later' } },
            { status: 503 },
          ),
        )
        .mockReturnValueOnce(response({ read: true }))
        .mockReturnValueOnce(
          Response.json(
            { data: null, error: { code: 'UNAVAILABLE', message: 'later' } },
            { status: 503 },
          ),
        )
        .mockReturnValueOnce(response({ write: true })),
    )
    const api = new Apostra({ apiKey: 'key', fetch: fetcher })
    await expect(api.getStatus({})).resolves.toEqual({ read: true })
    await expect(
      api.saveAsk(
        { id: 'ask-1', requesterState: 'accepted' },
        { idempotencyKey: 'ask-1' },
      ),
    ).resolves.toEqual({ write: true })
    expect(fetcher).toHaveBeenCalledTimes(4)
    const firstWrite = fetcher.mock.calls[2][1]
    const retryWrite = fetcher.mock.calls[3][1]
    expect(retryWrite?.body).toBe(firstWrite?.body)
    expect(new Headers(retryWrite?.headers).get('idempotency-key')).toBe(
      'ask-1',
    )
    random.mockRestore()
  })

  it('honours retry_after before retrying and bounds jittered backoff', async () => {
    vi.useFakeTimers()
    const random = vi.spyOn(Math, 'random').mockReturnValue(0)
    const fetcher = mockFetch(
      vi
        .fn()
        .mockReturnValueOnce(
          Response.json(
            {
              data: null,
              error: {
                code: 'RATE_LIMITED',
                message: 'later',
                retry_after: 1,
                recovery: 'transient',
              },
            },
            { status: 429 },
          ),
        )
        .mockReturnValueOnce(response({})),
    )
    const pending = new Apostra({ apiKey: 'key', fetch: fetcher }).getStatus({})
    await vi.advanceTimersByTimeAsync(999)
    expect(fetcher).toHaveBeenCalledTimes(1)
    await vi.advanceTimersByTimeAsync(1)
    await expect(pending).resolves.toEqual({})
    expect(fetcher).toHaveBeenCalledTimes(2)
    random.mockRestore()
    vi.useRealTimers()
  })

  it('settles in-flight keyed writes until a completed result and can cancel', async () => {
    vi.useFakeTimers()
    const receipt = {
      id: '4e8d0bf9-419a-4eb4-a6ee-3438f7bc89a1',
      state: 'running' as const,
      stateVersion: 1,
      stateChangedAt: '2026-09-28T10:00:00.000Z',
    }
    const run = vi
      .fn()
      .mockRejectedValueOnce(new InFlightReceiptError('r1', 10, receipt))
      .mockResolvedValueOnce({ done: true })
    const pending = settle(run, { timeoutMs: 100 })
    await vi.advanceTimersByTimeAsync(9)
    expect(run).toHaveBeenCalledTimes(1)
    await vi.advanceTimersByTimeAsync(1)
    await expect(pending).resolves.toEqual({ done: true })
    const controller = new AbortController()
    const cancelled = settle(
      () => Promise.reject(new InFlightReceiptError('r1', 100, receipt)),
      { signal: controller.signal },
    )
    controller.abort(new Error('cancelled'))
    await expect(cancelled).rejects.toThrow('cancelled')
    vi.useRealTimers()
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
