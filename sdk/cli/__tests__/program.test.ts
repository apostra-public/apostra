import { mkdtempSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'

import {
  ApostraError,
  AuthenticationError,
  ConflictError,
  ConnectionError,
  InFlightReceiptError,
  NotFoundError,
  PermissionError,
  RateLimitError,
  TimeoutError,
  ValidationError,
} from '@apostra/sdk'
import { operations } from '@apostra/sdk/metadata'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import packageMetadata from '../package.json' with { type: 'json' }
import { exitCodes, toCliError } from '../src/output.js'
import { runCli } from '../src/program.js'

type Request = {
  method: string
  url: URL
  headers: Headers
  body: Record<string, unknown> | undefined
}
type Responder = (request: Request) => Response | Promise<Response>

const json = (status: number, body: unknown, headers: HeadersInit = {}) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...headers },
  })
const ok = (data: unknown) => json(200, { data, error: null })
const failure = (status: number, code: string, message = 'refused') =>
  json(status, { data: null, error: { code, message } })

/** Runs the CLI against an in-memory API. The credential is an API key. */
async function run(
  args: string[],
  options: { responder?: Responder; stdin?: string } = {},
) {
  const requests: Request[] = []
  const responder = options.responder ?? (() => ok({ ok: true }))
  const fetch = vi.fn(async (input: RequestInfo | URL, init?: RequestInit) => {
    const request: Request = {
      method: init?.method ?? 'GET',
      url: new URL(String(input)),
      headers: new Headers(init?.headers),
      body: init?.body ? JSON.parse(String(init.body)) : undefined,
    }
    requests.push(request)
    return responder(request)
  }) as unknown as typeof globalThis.fetch
  let out = ''
  let err = ''
  const code = await runCli(
    args,
    {
      stdout: (text) => {
        out += text
      },
      stderr: (text) => {
        err += text
      },
    },
    { fetch, readStdin: async () => options.stdin ?? '' },
  )
  return { out, err, code, requests }
}

/** stdout in JSON mode is exactly one envelope that follows the documented shape. */
function envelope(out: string) {
  expect(out.endsWith('\n')).toBe(true)
  expect(out.trim().split('\n')).toHaveLength(1)
  const value = JSON.parse(out)
  expect(value.schemaVersion).toBe(1)
  if (value.ok) {
    expect(Object.keys(value).sort()).toEqual(
      [
        'schemaVersion',
        'ok',
        'data',
        ...('meta' in value ? ['meta'] : []),
      ].sort(),
    )
  } else {
    expect(Object.keys(value).sort()).toEqual(['error', 'ok', 'schemaVersion'])
    expect(value.error).toEqual(
      expect.objectContaining({
        code: expect.any(String),
        message: expect.any(String),
        exitCode: expect.any(Number),
      }),
    )
  }
  return value
}

beforeEach(() => {
  vi.stubEnv('APOSTRA_API_KEY', 'test-key')
  vi.stubEnv('APOSTRA_ACCOUNT_ID', undefined)
  vi.stubEnv('APOSTRA_BASE_URL', undefined)
})
afterEach(() => {
  vi.unstubAllEnvs()
})

describe('operations commands', () => {
  it('reads its version from package metadata', async () => {
    expect((await run(['--version'])).out).toBe(`${packageMetadata.version}\n`)
  })

  it('lists generated SDK operations in the versioned envelope', async () => {
    const { out, code } = await run(['operations', 'list', '--json'])
    expect(code).toBe(0)
    const value = envelope(out)
    expect(value.data.sdkVersion).toEqual(expect.any(String))
    expect(
      value.data.operations.map(
        (operation: { name: string }) => operation.name,
      ),
    ).toEqual(Object.keys(operations).sort((a, b) => a.localeCompare(b)))
  })

  it('describes an operation from the generated metadata, including whether it needs a key', async () => {
    const read = envelope(
      (await run(['operations', 'describe', 'get_delivery', '--json'])).out,
    )
    expect(read.data.operation).toMatchObject({
      name: 'get_delivery',
      method: 'POST',
      path: '/tools/get_delivery',
      idempotencyKey: false,
      parameters: [],
    })
    const write = envelope(
      (await run(['operations', 'describe', 'save_campaign', '--json'])).out,
    )
    expect(write.data.operation.idempotencyKey).toBe(true)
  })

  it('fails with the invalid-input exit code for an unknown operation', async () => {
    const result = await run(['operations', 'describe', 'nope', '--json'])
    expect(result.code).toBe(2)
    expect(envelope(result.out).error).toMatchObject({
      code: 'UNKNOWN_OPERATION',
      exitCode: 2,
    })
    expect(result.err).toBe('error: Unknown public V3 operation: nope\n')
  })

  it('keeps human output free of the envelope', async () => {
    const { out } = await run(['operations', 'list'])
    expect(out).toContain('get_delivery\tPOST\t/tools/get_delivery\n')
    expect(() => JSON.parse(out)).toThrow()
  })
})

describe('call reaches every public V3 operation', () => {
  const names = Object.keys(operations) as (keyof typeof operations)[]

  it.each(names)('%s', async (name) => {
    const meta = operations[name]
    const input = Object.fromEntries(
      meta.parameters
        .filter((parameter) => parameter.required)
        .map((parameter) => [parameter.name, 'x1']),
    )
    const result = await run(
      [
        'call',
        name,
        '--account',
        '1',
        '--input',
        JSON.stringify(input),
        '--json',
        ...(meta.idempotencyKey ? ['--idempotency-key', 'key-1'] : []),
      ],
      {
        responder: () =>
          meta.binary
            ? new Response('# doc', {
                headers: { 'Content-Type': 'text/markdown' },
              })
            : ok({ ok: true }),
      },
    )
    expect(result.code).toBe(0)
    const [request] = result.requests
    expect(result.requests).toHaveLength(1)
    expect(request?.method).toBe(meta.method)
    expect(request?.url.pathname).toBe(
      `/api/v3${meta.path.replace(/\{(\w+)\}/g, 'x1')}`,
    )
    expect(request?.headers.get('x-scope3-customer-id')).toBe('1')
    expect(request?.headers.get('idempotency-key')).toBe(
      meta.idempotencyKey ? 'key-1' : null,
    )
    const value = envelope(result.out)
    expect(value.meta).toMatchObject({ operation: name, accountId: '1' })
    expect(value.data).toEqual(
      meta.binary ? { encoding: 'utf-8', content: '# doc' } : { ok: true },
    )
  })
})

describe('call input', () => {
  const callRead = (...args: string[]) =>
    run(['call', 'get_delivery', '--account', '1', '--json', ...args])

  it('takes input from inline JSON, a file, stdin and --set, in that order of precedence', async () => {
    const dir = mkdtempSync(join(tmpdir(), 'apostra-cli-input-'))
    try {
      const file = join(dir, 'request.json')
      writeFileSync(file, '{"from":"file","keep":1}')
      expect(
        (await callRead('--input', '{"from":"inline"}')).requests[0]?.body,
      ).toEqual({ from: 'inline' })
      expect((await callRead('--input', `@${file}`)).requests[0]?.body).toEqual(
        { from: 'file', keep: 1 },
      )
      expect(
        (
          await run(
            ['call', 'get_delivery', '--account', '1', '--input', '-'],
            { stdin: '{"from":"stdin"}' },
          )
        ).requests[0]?.body,
      ).toEqual({ from: 'stdin' })
      const overlaid = await callRead(
        '--input',
        `@${file}`,
        '--set',
        'from="flag"',
        '--set',
        'limit=20',
        '--set',
        'filter.status=active',
      )
      expect(overlaid.requests[0]?.body).toEqual({
        from: 'flag',
        keep: 1,
        limit: 20,
        filter: { status: 'active' },
      })
    } finally {
      rmSync(dir, { recursive: true, force: true })
    }
  })

  it.each([
    ['not JSON', ['--input', '{']],
    ['not an object', ['--input', '[1]']],
    ['a missing file', ['--input', '@/nonexistent/request.json']],
    ['a --set without a value', ['--set', 'limit']],
    ['a prototype path', ['--set', '__proto__.polluted=1']],
    ['a --set through a non-object', ['--input', '{"a":1}', '--set', 'a.b=2']],
    ['a read with an idempotency key', ['--idempotency-key', 'k']],
    ['a --max-pages of zero', ['--max-pages', '0']],
    ['an unknown option', ['--bogus']],
  ])(
    'refuses %s with the invalid-input exit code and sends nothing',
    async (_name, args) => {
      const result = await callRead(...args)
      expect(result.code).toBe(2)
      expect(envelope(result.out).error.exitCode).toBe(2)
      expect(result.requests).toEqual([])
      expect(Object.hasOwn({}, 'polluted')).toBe(false)
      expect(({} as Record<string, unknown>).polluted).toBeUndefined()
    },
  )

  it('refuses a write without an idempotency key, and sends it when given one', async () => {
    const missing = await run([
      'call',
      'save_campaign',
      '--account',
      '1',
      '--json',
    ])
    expect(missing.code).toBe(2)
    expect(envelope(missing.out).error.code).toBe('IDEMPOTENCY_KEY_REQUIRED')
    expect(missing.requests).toEqual([])
    const sent = await run([
      'call',
      'save_campaign',
      '--account',
      '1',
      '--idempotency-key',
      'k-9',
    ])
    expect(sent.code).toBe(0)
    expect(sent.requests[0]?.headers.get('idempotency-key')).toBe('k-9')
  })

  it('refuses an unknown operation', async () => {
    const result = await run(['call', 'nope', '--account', '1', '--json'])
    expect(result.code).toBe(2)
    expect(envelope(result.out).error.code).toBe('UNKNOWN_OPERATION')
  })

  it('prints the data as readable JSON without --json', async () => {
    const result = await run(['call', 'get_delivery', '--account', '1'], {
      responder: () => ok({ rows: [1] }),
    })
    expect(result.out).toBe('{\n  "rows": [\n    1\n  ]\n}\n')
  })
})

describe('call names its account', () => {
  it('refuses an API-key call that names no account', async () => {
    const result = await run(['call', 'get_delivery', '--json'])
    expect(result.code).toBe(2)
    expect(envelope(result.out).error.code).toBe('ACCOUNT_REQUIRED')
    expect(result.requests).toEqual([])
  })

  it('uses --account, then APOSTRA_ACCOUNT_ID, and says which on stderr', async () => {
    vi.stubEnv('APOSTRA_ACCOUNT_ID', '5')
    const fromEnv = await run(['call', 'get_delivery'])
    expect(fromEnv.err).toBe('Using account 5 (APOSTRA_ACCOUNT_ID).\n')
    expect(fromEnv.requests[0]?.headers.get('x-scope3-customer-id')).toBe('5')
    const flag = await run(['call', 'get_delivery', '--account', '6'])
    expect(flag.err).toBe('Using account 6 (--account).\n')
    expect(flag.requests[0]?.headers.get('x-scope3-customer-id')).toBe('6')
  })

  it('refuses an account that is not a positive integer', async () => {
    const result = await run(['call', 'get_delivery', '--account', 'abc'])
    expect(result.code).toBe(2)
    expect(result.requests).toEqual([])
  })

  it('keeps stdout to the envelope while stderr carries the diagnostics', async () => {
    const result = await run([
      'call',
      'get_delivery',
      '--account',
      '1',
      '--json',
    ])
    expect(result.err).toBe('Using account 1 (--account).\n')
    envelope(result.out)
  })

  it('refuses an input whose accountId differs from the account the call runs in', async () => {
    const result = await run([
      'call',
      'get_delivery',
      '--account',
      '1',
      '--set',
      'accountId=2',
      '--json',
    ])
    expect(result.code).toBe(4)
    expect(envelope(result.out).error.code).toBe('ACCOUNT_MISMATCH')
    expect(result.requests).toEqual([])
    const same = await run([
      'call',
      'get_delivery',
      '--account',
      '1',
      '--set',
      'accountId=1',
    ])
    expect(same.code).toBe(0)
  })
})

describe('call --all', () => {
  const page = (cursor: string | null, hasMore: boolean, results: number[]) =>
    ok({ objects: { results, nextCursor: cursor, hasMore } })
  const paged: Responder = ({ body }) => {
    if (body?.cursor === undefined) return page('c2', true, [1])
    if (body.cursor === 'c2') return page('c3', true, [2])
    return page(null, false, [3])
  }

  it('follows every cursor and returns every page, in order', async () => {
    const result = await run(
      [
        'call',
        'search',
        '--account',
        '1',
        '--set',
        'kind=campaign',
        '--all',
        '--json',
      ],
      { responder: paged },
    )
    expect(result.code).toBe(0)
    expect(result.requests.map((request) => request.body)).toEqual([
      { kind: 'campaign' },
      { kind: 'campaign', cursor: 'c2' },
      { kind: 'campaign', cursor: 'c3' },
    ])
    const value = envelope(result.out)
    expect(value.data).toEqual([
      { objects: { results: [1], nextCursor: 'c2', hasMore: true } },
      { objects: { results: [2], nextCursor: 'c3', hasMore: true } },
      { objects: { results: [3], nextCursor: null, hasMore: false } },
    ])
    expect(value.meta).toMatchObject({ operation: 'search', pages: 3 })
  })

  it('returns a single page when the first response has no more', async () => {
    const result = await run(
      ['call', 'search', '--account', '1', '--all', '--json'],
      {
        responder: () => page(null, false, [1]),
      },
    )
    expect(envelope(result.out).meta.pages).toBe(1)
  })

  it('stops with an error rather than dropping pages past --max-pages', async () => {
    const result = await run(
      [
        'call',
        'search',
        '--account',
        '1',
        '--all',
        '--max-pages',
        '2',
        '--json',
      ],
      { responder: paged },
    )
    expect(result.code).toBe(2)
    expect(envelope(result.out).error.code).toBe('PAGE_LIMIT')
    expect(result.requests).toHaveLength(2)
  })

  it('refuses to guess when the response says more exists but gives no cursor', async () => {
    const result = await run(
      ['call', 'search', '--account', '1', '--all', '--json'],
      {
        responder: () => page(null, true, [1]),
      },
    )
    expect(result.code).toBe(6)
    expect(envelope(result.out).error.code).toBe('INCOMPLETE_PAGINATION')
  })

  it('refuses a response with two cursors', async () => {
    const result = await run(
      ['call', 'search', '--account', '1', '--all', '--json'],
      {
        responder: () => ok({ a: { nextCursor: 'x' }, b: { nextCursor: 'y' } }),
      },
    )
    expect(result.code).toBe(6)
    expect(envelope(result.out).error.code).toBe('AMBIGUOUS_PAGINATION')
  })

  it('stops on a cursor that repeats instead of looping', async () => {
    const result = await run(
      ['call', 'search', '--account', '1', '--all', '--json'],
      {
        responder: () => page('same', true, [1]),
      },
    )
    expect(result.code).toBe(1)
    expect(envelope(result.out).error.code).toBe('PROTOCOL_ERROR')
  })

  it('applies only to reads that return JSON', async () => {
    for (const name of ['save_campaign', 'downloadV3PublicDocumentRevision']) {
      const result = await run([
        'call',
        name,
        '--account',
        '1',
        '--all',
        '--idempotency-key',
        'k',
        '--json',
      ])
      expect(result.code).toBe(2)
      expect(result.requests).toEqual([])
    }
  })
})

describe('exit codes', () => {
  const call = (responder: Responder) =>
    run(['call', 'get_delivery', '--account', '1', '--json'], { responder })

  it('defines each documented code once', () => {
    expect(exitCodes).toEqual({
      ok: 0,
      serverFailure: 1,
      invalidInput: 2,
      authentication: 3,
      permission: 4,
      conflict: 5,
      unavailable: 6,
    })
  })

  it.each([
    [400, 'VALIDATION_FAILED', 2],
    [422, 'VALIDATION_FAILED', 2],
    [404, 'NOT_FOUND', 2],
    [401, 'UNAUTHENTICATED', 3],
    [403, 'ACCESS_DENIED', 4],
    [403, 'ACCOUNT_NOT_REACHABLE', 4],
    [409, 'CONFLICT', 5],
    [501, 'NOT_IMPLEMENTED', 6],
    [422, 'FEATURE_NOT_ENABLED', 6],
  ])(
    'maps HTTP %i %s to exit %i, with the server error in the envelope',
    async (status, code, exitCode) => {
      const result = await call(() => failure(status, code, 'because'))
      expect(result.code).toBe(exitCode)
      expect(envelope(result.out).error).toEqual({
        code,
        message: 'because',
        exitCode,
        status,
        requestId: null,
        recovery: expect.any(String),
        retryAfter: null,
      })
      expect(result.err).toContain('error: because\n')
    },
  )

  it('maps a failed server to exit 1', async () => {
    const result = await call(() => failure(500, 'INTERNAL_ERROR'))
    expect(result.code).toBe(1)
    expect(envelope(result.out).error).toMatchObject({
      code: 'INTERNAL_ERROR',
      exitCode: 1,
      recovery: 'transient',
    })
  })

  it('maps the SDK error classes without a server', () => {
    const error = (code: string) => ({ code, message: 'm' })
    const exit = (value: unknown) => toCliError(value).exitCode
    expect(exit(new AuthenticationError(401, error('A'), null))).toBe(3)
    expect(exit(new PermissionError(403, error('A'), null))).toBe(4)
    expect(exit(new ConflictError(409, error('A'), null))).toBe(5)
    expect(exit(new ValidationError(422, error('A'), null))).toBe(2)
    expect(exit(new NotFoundError(404, error('A'), null))).toBe(2)
    expect(exit(new RateLimitError(429, error('RATE_LIMITED'), null))).toBe(1)
    expect(
      exit(new ApostraError(503, error('SERVICE_UNAVAILABLE'), null)),
    ).toBe(1)
    expect(exit(new ConnectionError(new Error('x')))).toBe(1)
    expect(exit(new TimeoutError(new Error('x')))).toBe(1)
    expect(exit(new Error('x'))).toBe(1)
  })

  it('reports a write still in flight as a conflict that names the receipt', () => {
    const receipt = {
      id: 'r1',
      operation: 'save_campaign',
      state: 'running',
      stateVersion: 1,
      stateChangedAt: '2026-10-27T00:00:00Z',
      pendingReason: 'dispatch running',
    } as ConstructorParameters<typeof InFlightReceiptError>[2]
    const error = toCliError(new InFlightReceiptError('req-1', 2000, receipt))
    expect(error).toMatchObject({
      code: 'IN_FLIGHT',
      exitCode: 5,
      details: { status: 202, requestId: 'req-1', retryAfter: 2, receipt },
    })
  })

  it('maps a missing sign-in to authentication and bad usage to invalid input', async () => {
    vi.stubEnv('APOSTRA_API_KEY', undefined)
    const signedOut = await run([
      'call',
      'get_delivery',
      '--account',
      '1',
      '--base-url',
      'http://127.0.0.1:1',
      '--json',
    ])
    expect(signedOut.code).toBe(3)
    const usage = await run(['call', '--json'])
    expect(usage.code).toBe(2)
    expect(envelope(usage.out).error.code).toBe('INVALID_INPUT')
  })

  it('returns 0 for help and a usage exit code for a missing command', async () => {
    const help = await run(['--help'])
    expect(help.code).toBe(0)
    expect(help.out).toContain('call [options] <operation>')
    expect((await run([])).code).toBe(2)
  })

  it('exits 0 and prints nothing but data on success', async () => {
    const result = await call(() => ok({ done: true }))
    expect(result.code).toBe(0)
    expect(envelope(result.out)).toEqual({
      schemaVersion: 1,
      ok: true,
      data: { done: true },
      meta: { operation: 'get_delivery', accountId: '1', requestId: null },
    })
  })
})
