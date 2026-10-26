import {
  existsSync,
  mkdirSync,
  mkdtempSync,
  readFileSync,
  rmSync,
  statSync,
  writeFileSync,
} from 'node:fs'
import {
  createServer,
  type IncomingMessage,
  type Server,
  type ServerResponse,
} from 'node:http'
import type { AddressInfo } from 'node:net'
import { tmpdir } from 'node:os'
import { join } from 'node:path'

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import {
  type CliLoginEntry,
  cliClientId,
  credentialsPath,
  discoverCliLogin,
  exchangeCliLoginCode,
  logoutCliLogin,
  normalizeBaseUrl,
  readCliLogin,
  refreshCliLogin,
  withCliLoginLock,
  writeCliLogin,
} from '../src/cli-login.js'
import { Apostra, cliLoginTokenProvider } from '../src/index.js'

type Fake = {
  origin: string
  resource: string
  refreshRequests: number
  revokeRequests: string[]
  apiTokens: string[]
  refreshStatus: number
  omitRefreshToken: boolean
  close: () => Promise<void>
}

/** A local authorization server and V3 API. Never production. */
async function startFake(): Promise<Fake> {
  const fake = {
    refreshRequests: 0,
    revokeRequests: [] as string[],
    apiTokens: [] as string[],
    refreshStatus: 200,
    omitRefreshToken: false,
  } as Fake
  const json = (res: ServerResponse, status: number, body: unknown) => {
    res.writeHead(status, { 'Content-Type': 'application/json' })
    res.end(JSON.stringify(body))
  }
  const form = async (req: IncomingMessage) => {
    let text = ''
    for await (const chunk of req) text += chunk
    return new URLSearchParams(text)
  }
  const server: Server = createServer(async (req, res) => {
    const url = new URL(req.url ?? '/', fake.origin)
    if (url.pathname === '/.well-known/oauth-protected-resource/api/v3')
      return json(res, 200, {
        resource: fake.resource,
        authorization_servers: [fake.origin],
      })
    if (url.pathname === '/.well-known/oauth-authorization-server')
      return json(res, 200, {
        issuer: fake.origin,
        authorization_endpoint: `${fake.origin}/authorize`,
        token_endpoint: `${fake.origin}/auth/token`,
        revocation_endpoint: `${fake.origin}/auth/revoke`,
        code_challenge_methods_supported: ['S256'],
      })
    if (url.pathname === '/auth/token') {
      const body = await form(req)
      if (body.get('resource') !== fake.resource)
        return json(res, 400, { error: 'invalid_target' })
      fake.refreshRequests++
      await new Promise((r) => setTimeout(r, 40))
      if (fake.refreshStatus !== 200)
        return json(res, fake.refreshStatus, { error: 'invalid_grant' })
      return json(res, 200, {
        access_token: `at-${fake.refreshRequests}`,
        ...(fake.omitRefreshToken
          ? {}
          : { refresh_token: `rt-${fake.refreshRequests}` }),
        expires_in: 3600,
        scope: 'interchange:read',
      })
    }
    if (url.pathname === '/auth/revoke') {
      fake.revokeRequests.push((await form(req)).get('token') ?? '')
      return json(res, 200, {})
    }
    if (url.pathname === '/api/v3/tools/get_status') {
      fake.apiTokens.push(req.headers.authorization ?? '')
      return json(res, 200, {
        data: { account: { accountId: 7 } },
        error: null,
      })
    }
    json(res, 404, {})
  })
  await new Promise<void>((r) => server.listen(0, '127.0.0.1', r))
  fake.origin = `http://127.0.0.1:${(server.address() as AddressInfo).port}`
  fake.resource = `${fake.origin}/api/v3`
  fake.close = () => new Promise((r) => server.close(() => r()))
  server.unref()
  return fake
}

const entry = (
  fake: Fake,
  over: Partial<CliLoginEntry> = {},
): CliLoginEntry => ({
  issuer: fake.origin,
  resource: fake.resource,
  clientId: cliClientId(fake.resource),
  accessToken: 'at-0',
  refreshToken: 'rt-0',
  expiresAt: new Date(Date.now() - 1000).toISOString(),
  accountId: '7',
  scopes: ['interchange:read'],
  ...over,
})

let dir: string
let fake: Fake
beforeEach(async () => {
  dir = mkdtempSync(join(tmpdir(), 'apostra-login-'))
  vi.stubEnv('XDG_CONFIG_HOME', dir)
  vi.stubEnv('APPDATA', dir)
  vi.stubEnv('APOSTRA_API_KEY', undefined)
  vi.stubEnv('APOSTRA_ACCOUNT_ID', undefined)
  vi.stubEnv('APOSTRA_BASE_URL', undefined)
  fake = await startFake()
})
afterEach(async () => {
  vi.unstubAllEnvs()
  await fake.close()
  rmSync(dir, { recursive: true, force: true })
})

describe('credential store', () => {
  it('writes atomically with 0700 directory and 0600 file, keyed per base URL', async () => {
    const other = 'https://other.example/api/v3'
    await withCliLoginLock(async () => {
      writeCliLogin(fake.resource, entry(fake))
      writeCliLogin(other, entry(fake, { resource: other, accountId: '9' }))
    })
    expect(credentialsPath()).toBe(join(dir, 'apostra', 'credentials.json'))
    if (process.platform !== 'win32') {
      expect(statSync(join(dir, 'apostra')).mode & 0o777).toBe(0o700)
      expect(statSync(credentialsPath()).mode & 0o777).toBe(0o600)
    }
    expect(readCliLogin(`${fake.resource}/`)?.accountId).toBe('7')
    expect(readCliLogin(other)?.accountId).toBe('9')
    expect(readCliLogin('https://nobody.example/api/v3')).toBeUndefined()
    const files = (await import('node:fs')).readdirSync(join(dir, 'apostra'))
    expect(files).toEqual(['credentials.json'])
  })

  it('treats a corrupt file as no login and normalizes URLs', () => {
    mkdirSync(join(dir, 'apostra'))
    writeFileSync(credentialsPath(), '{not json')
    expect(readCliLogin(fake.resource)).toBeUndefined()
    expect(normalizeBaseUrl('https://API.example.com/api/v3/')).toBe(
      'https://api.example.com/api/v3',
    )
    expect(() => normalizeBaseUrl('http://example.com/api/v3')).toThrow(
      TypeError,
    )
  })
})

describe('refresh', () => {
  it('rotates the refresh token and writes it back', async () => {
    await withCliLoginLock(async () =>
      writeCliLogin(fake.resource, entry(fake)),
    )
    const next = await refreshCliLogin(fake.resource)
    expect(next).toMatchObject({ accessToken: 'at-1', refreshToken: 'rt-1' })
    expect(readCliLogin(fake.resource)?.refreshToken).toBe('rt-1')
    expect(fake.refreshRequests).toBe(1)
    // Fresh now: no second request.
    await refreshCliLogin(fake.resource)
    expect(fake.refreshRequests).toBe(1)
  })

  it('makes exactly one token request for two concurrent refreshers', async () => {
    await withCliLoginLock(async () =>
      writeCliLogin(fake.resource, entry(fake)),
    )
    const a = cliLoginTokenProvider({ baseUrl: fake.resource })
    const b = cliLoginTokenProvider({ baseUrl: fake.resource })
    expect(await Promise.all([a(), b(), a()])).toEqual(['at-1', 'at-1', 'at-1'])
    expect(fake.refreshRequests).toBe(1)
  })

  it('says to sign in again when the grant was revoked, without echoing the body', async () => {
    await withCliLoginLock(async () =>
      writeCliLogin(fake.resource, entry(fake)),
    )
    fake.refreshStatus = 400
    await expect(refreshCliLogin(fake.resource)).rejects.toThrow(
      'Run `apostra login` again',
    )
  })

  it('keeps the old refresh token when a refresh does not rotate it', async () => {
    await withCliLoginLock(async () =>
      writeCliLogin(fake.resource, entry(fake)),
    )
    fake.omitRefreshToken = true
    await refreshCliLogin(fake.resource)
    expect(readCliLogin(fake.resource)?.refreshToken).toBe('rt-0')
  })

  it('never removes a lock another process owns', async () => {
    const lock = `${credentialsPath()}.lock`
    await withCliLoginLock(async () => {
      // Another process took the lock over while this one held it.
      writeFileSync(lock, 'another-owner')
    })
    expect(readFileSync(lock, 'utf8')).toBe('another-owner')
  })

  it('breaks a stale lock left by a dead process', async () => {
    const { utimesSync } = await import('node:fs')
    await withCliLoginLock(async () =>
      writeCliLogin(fake.resource, entry(fake)),
    )
    const lock = `${credentialsPath()}.lock`
    writeFileSync(lock, '')
    const old = new Date(Date.now() - 60_000)
    utimesSync(lock, old, old)
    await expect(refreshCliLogin(fake.resource)).resolves.toBeDefined()
    expect(existsSync(`${lock}.takeover`)).toBe(false)
  })
})

describe('login', () => {
  it('refuses a token response with no refresh token and stores nothing', async () => {
    fake.omitRefreshToken = true
    const discovery = await discoverCliLogin(fake.resource)
    await expect(
      exchangeCliLoginCode({}, discovery, fake.resource, {
        code: 'code',
        verifier: 'verifier',
        redirectUri: 'http://127.0.0.1:1/callback',
      }),
    ).rejects.toThrow('did not return a refresh token')
    expect(readCliLogin(fake.resource)).toBeUndefined()
  })
})

describe('logout', () => {
  it('revokes the refresh token then deletes the entry', async () => {
    await withCliLoginLock(async () =>
      writeCliLogin(fake.resource, entry(fake)),
    )
    await expect(logoutCliLogin(fake.resource)).resolves.toEqual({
      found: true,
      revoked: true,
    })
    expect(fake.revokeRequests).toEqual(['rt-0'])
    expect(readCliLogin(fake.resource)).toBeUndefined()
    await expect(logoutCliLogin(fake.resource)).resolves.toEqual({
      found: false,
      revoked: false,
    })
  })

  it('still deletes locally when revocation fails', async () => {
    await withCliLoginLock(async () =>
      writeCliLogin(fake.resource, entry(fake)),
    )
    await fake.close()
    await expect(logoutCliLogin(fake.resource)).resolves.toEqual({
      found: true,
      revoked: false,
    })
    expect(readCliLogin(fake.resource)).toBeUndefined()
    fake = await startFake()
  })
})

describe('default credential chain', () => {
  const store = (over: Partial<CliLoginEntry> = {}) =>
    withCliLoginLock(async () =>
      writeCliLogin(
        fake.resource,
        entry(fake, {
          expiresAt: new Date(Date.now() + 3_600_000).toISOString(),
          ...over,
        }),
      ),
    )
  const call = (options: ConstructorParameters<typeof Apostra>[0]) =>
    new Apostra({ baseUrl: fake.resource, ...options }).getStatus()

  it('uses an explicit credential before anything else', async () => {
    await store()
    vi.stubEnv('APOSTRA_API_KEY', 'env-key')
    await call({ apiKey: 'explicit-key' })
    expect(fake.apiTokens).toEqual(['Bearer explicit-key'])
  })

  it('uses APOSTRA_API_KEY before the CLI login', async () => {
    await store()
    vi.stubEnv('APOSTRA_API_KEY', 'env-key')
    await call({})
    expect(fake.apiTokens).toEqual(['Bearer env-key'])
  })

  it('uses the CLI login when nothing else is set', async () => {
    await store()
    await call({})
    expect(fake.apiTokens).toEqual(['Bearer at-0'])
  })

  it('refreshes an expired CLI login transparently', async () => {
    await store({ expiresAt: new Date(Date.now() - 1000).toISOString() })
    await call({})
    expect(fake.apiTokens).toEqual(['Bearer at-1'])
  })

  it('keeps today’s error when there is no credential and no login', () => {
    expect(() => new Apostra({ baseUrl: fake.resource })).toThrow(
      'Supply exactly one of apiKey, accessToken or tokenProvider',
    )
  })

  it('ignores a login stored for a different base URL', async () => {
    await store()
    expect(
      () => new Apostra({ baseUrl: 'https://elsewhere.example/api/v3' }),
    ).toThrow('Supply exactly one')
  })

  it('refuses an explicit accountId that differs from the login', async () => {
    await store()
    expect(
      () => new Apostra({ baseUrl: fake.resource, accountId: '8' }),
    ).toThrow(/does not match account 7/)
    expect(
      () => new Apostra({ baseUrl: fake.resource, accountId: '7' }),
    ).not.toThrow()
  })

  it('keeps the base URL error for an invalid URL even with a login stored', async () => {
    await store()
    expect(() => new Apostra({ baseUrl: 'http://example.com' })).toThrow(
      'Supply exactly one',
    )
  })
})
