import { createHash } from 'node:crypto'
import { mkdtempSync, rmSync } from 'node:fs'
import {
  createServer,
  type IncomingMessage,
  type ServerResponse,
} from 'node:http'
import type { AddressInfo } from 'node:net'
import { tmpdir } from 'node:os'
import { join } from 'node:path'

import { CommanderError } from 'commander'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import {
  createPkce,
  createState,
  login,
  pkceChallenge,
  scopeNames,
  startCallbackServer,
} from '../src/login.js'
import { createProgram } from '../src/program.js'

describe('PKCE and state', () => {
  it('matches the RFC 7636 appendix B vector', () => {
    expect(pkceChallenge('dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk')).toBe(
      'E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM',
    )
  })

  it('generates unique, URL-safe, long-enough secrets', () => {
    const a = createPkce()
    const b = createPkce()
    expect(a.verifier).not.toBe(b.verifier)
    expect(a.verifier).toMatch(/^[A-Za-z0-9_-]{43,128}$/)
    expect(a.challenge).toBe(
      createHash('sha256').update(a.verifier).digest('base64url'),
    )
    expect(createState()).not.toBe(createState())
    expect(createState().length).toBeGreaterThanOrEqual(32)
  })
})

describe('loopback callback', () => {
  const hit = (redirectUri: string, query: string) =>
    fetch(`${redirectUri}${query}`)

  it('listens on 127.0.0.1 only and returns the code for the right state', async () => {
    const server = await startCallbackServer({ state: 's1' })
    expect(server.redirectUri).toMatch(/^http:\/\/127\.0\.0\.1:\d+\/callback$/)
    const code = server.code()
    const response = await hit(server.redirectUri, '?code=abc&state=s1')
    expect(response.status).toBe(200)
    expect(await response.text()).toContain('You can close this tab')
    await expect(code).resolves.toBe('abc')
  })

  it('refuses a wrong or missing state and keeps waiting', async () => {
    const server = await startCallbackServer({ state: 's1' })
    const code = server.code()
    expect(
      (await hit(server.redirectUri, '?code=evil&state=nope')).status,
    ).toBe(400)
    expect((await hit(server.redirectUri, '?code=evil')).status).toBe(400)
    expect((await hit(server.redirectUri, '?error=access_denied')).status).toBe(
      400,
    )
    const wrongPath = server.redirectUri.replace('/callback', '/other')
    expect((await hit(wrongPath, '?code=x&state=s1')).status).toBe(404)
    await hit(server.redirectUri, '?code=good&state=s1')
    await expect(code).resolves.toBe('good')
  })

  it('fails with the provider error when the state is right', async () => {
    const server = await startCallbackServer({ state: 's1' })
    const code = server.code()
    code.catch(() => {})
    const response = await hit(
      server.redirectUri,
      '?error=access_denied&error_description=x&state=s1',
    )
    expect(await response.text()).not.toContain('access_denied')
    await expect(code).rejects.toThrow('Sign-in failed: access_denied')
  })

  it('times out with a clear message and frees the port', async () => {
    const server = await startCallbackServer({ state: 's1', timeoutMs: 30 })
    await expect(server.code()).rejects.toThrow(/Timed out after .* minutes/)
    await expect(hit(server.redirectUri, '?code=a&state=s1')).rejects.toThrow()
  })
})

type Fake = {
  origin: string
  resource: string
  authorize: URL | undefined
  tokenForms: URLSearchParams[]
  revokes: string[]
  revokeOk: boolean
  close: () => Promise<void>
}

/** A local authorization server and V3 API. Never production. */
async function startFake(): Promise<Fake> {
  const fake = {
    tokenForms: [],
    revokes: [],
    revokeOk: true,
  } as unknown as Fake
  const json = (res: ServerResponse, status: number, body: unknown) => {
    res.writeHead(status, { 'Content-Type': 'application/json' })
    res.end(JSON.stringify(body))
  }
  const form = async (req: IncomingMessage) => {
    let text = ''
    for await (const chunk of req) text += chunk
    return new URLSearchParams(text)
  }
  const server = createServer(async (req, res) => {
    const path = new URL(req.url ?? '/', fake.origin).pathname
    if (path === '/.well-known/oauth-protected-resource/api/v3')
      return json(res, 200, {
        resource: fake.resource,
        authorization_servers: [fake.origin],
      })
    if (path === '/.well-known/oauth-authorization-server')
      return json(res, 200, {
        issuer: fake.origin,
        authorization_endpoint: `${fake.origin}/authorize`,
        token_endpoint: `${fake.origin}/auth/token`,
        revocation_endpoint: `${fake.origin}/auth/revoke`,
        code_challenge_methods_supported: ['S256'],
      })
    if (path === '/auth/token') {
      fake.tokenForms.push(await form(req))
      return json(res, 200, {
        access_token: `at-${fake.tokenForms.length}`,
        refresh_token: `rt-${fake.tokenForms.length}`,
        expires_in: 3600,
        scope: 'interchange:read interchange:write',
      })
    }
    if (path === '/auth/revoke') {
      fake.revokes.push((await form(req)).get('token') ?? '')
      return json(res, fake.revokeOk ? 200 : 500, {})
    }
    if (path === '/api/v3/tools/get_status')
      return json(res, 200, {
        data: {
          account: { accountId: 42, company: 'Acme' },
          state: 'ready',
          canTransact: true,
        },
        error: null,
      })
    json(res, 404, {})
  })
  await new Promise<void>((r) => server.listen(0, '127.0.0.1', r))
  fake.origin = `http://127.0.0.1:${(server.address() as AddressInfo).port}`
  fake.resource = `${fake.origin}/api/v3`
  fake.close = () => new Promise((r) => server.close(() => r()))
  server.unref()
  return fake
}

describe('apostra login, status, token and logout', () => {
  let dir: string
  let fake: Fake
  beforeEach(async () => {
    dir = mkdtempSync(join(tmpdir(), 'apostra-cli-'))
    vi.stubEnv('XDG_CONFIG_HOME', dir)
    vi.stubEnv('APPDATA', dir)
    vi.stubEnv('APOSTRA_BASE_URL', undefined)
    fake = await startFake()
  })
  afterEach(async () => {
    vi.unstubAllEnvs()
    await fake.close()
    rmSync(dir, { recursive: true, force: true })
  })

  /** Follow the redirect the authorization server would send. */
  const redirect = (url: string, query: (state: string) => string) => {
    const authorize = new URL(url)
    fake.authorize = authorize
    const target = authorize.searchParams.get('redirect_uri') as string
    const state = authorize.searchParams.get('state') as string
    void fetch(`${target}?${query(state)}`)
  }
  /** Plays the browser. */
  const browser = async (url: string) => {
    redirect(url, (state) => `code=auth-code&state=${state}`)
    return true
  }
  const run = async (args: string[], open = browser) => {
    let out = ''
    let err = ''
    const program = createProgram(
      (text) => {
        out += text
      },
      { open },
    )
    program.exitOverride()
    program.configureOutput({
      writeOut: (text) => {
        out += text
      },
      writeErr: (text) => {
        err += text
      },
    })
    let code = 0
    try {
      await program.parseAsync(['node', 'apostra', ...args])
    } catch (error) {
      if (!(error instanceof CommanderError)) throw error
      code = error.exitCode
    }
    return { out, err, code }
  }

  it('signs in end to end with PKCE, the resource and the chosen scopes', async () => {
    const result = await run([
      'login',
      '--base-url',
      fake.origin,
      '--account',
      '42',
      '--scope',
      'read',
    ])
    expect(result.code).toBe(0)
    expect(result.out).toContain('Signed in to')
    expect(result.out).toContain('account 42')
    const authorize = fake.authorize as URL
    expect(Object.fromEntries(authorize.searchParams)).toMatchObject({
      response_type: 'code',
      client_id: `${fake.origin}/oauth/clients/apostra-cli.json`,
      code_challenge_method: 'S256',
      scope: 'interchange:read',
      resource: fake.resource,
      account_id: '42',
    })
    const exchange = fake.tokenForms[0] as URLSearchParams
    expect(exchange.get('grant_type')).toBe('authorization_code')
    expect(exchange.get('code')).toBe('auth-code')
    expect(exchange.get('resource')).toBe(fake.resource)
    expect(
      createHash('sha256')
        .update(exchange.get('code_verifier') as string)
        .digest('base64url'),
    ).toBe(authorize.searchParams.get('code_challenge'))
    expect(exchange.get('redirect_uri')).toBe(
      authorize.searchParams.get('redirect_uri'),
    )
    // Nothing secret reached the terminal.
    for (const secret of [
      'at-1',
      'rt-1',
      'auth-code',
      exchange.get('code_verifier') as string,
    ])
      expect(result.out + result.err).not.toContain(secret)
  })

  it('requests read and write by default', async () => {
    await run(['login', '--base-url', fake.origin])
    expect(fake.authorize?.searchParams.get('scope')).toBe(
      'interchange:read interchange:write',
    )
    expect(fake.authorize?.searchParams.has('account_id')).toBe(false)
  })

  it('offers read and write as the only interactive scopes', () => {
    expect(scopeNames).toEqual(['read', 'write'])
  })

  it('prints the URL instead of opening a browser with --no-browser or when opening fails', async () => {
    for (const browserFlag of [false, true]) {
      let said = ''
      const open = vi.fn(async () => false)
      const pending = login({
        resource: fake.resource,
        scopes: ['interchange:read'],
        browser: browserFlag,
        open,
        say: (text) => {
          said += text
        },
      })
      await vi.waitFor(() => expect(said).toMatch(/https?:\/\/\S+/))
      expect(open).toHaveBeenCalledTimes(browserFlag ? 1 : 0)
      redirect(
        (said.match(/https?:\/\/\S+/) as RegExpMatchArray)[0],
        (state) => `code=auth-code&state=${state}`,
      )
      await expect(pending).resolves.toMatchObject({ accountId: '42' })
    }
  })

  it('reports status with the account name and readiness', async () => {
    await run(['login', '--base-url', fake.origin])
    const { out, code } = await run(['status', '--base-url', fake.origin])
    expect(code).toBe(0)
    expect(out).toContain(`Base URL: ${fake.resource}`)
    expect(out).toContain('Account ID: 42')
    expect(out).toContain('Account: Acme')
    expect(out).toContain('Readiness: ready')
  })

  it('prints only the access token for `token`, and fails clearly when signed out', async () => {
    const signedOut = await run(['token', '--base-url', fake.origin])
    expect(signedOut.code).toBe(1)
    expect(signedOut.out).toBe('')
    expect(signedOut.err).toContain('Run `apostra login`')
    await run(['login', '--base-url', fake.origin])
    const { out } = await run(['token', '--base-url', fake.origin])
    expect(out).toBe('at-1\n')
  })

  it('revokes the refresh token on logout, and says so when revocation fails', async () => {
    await run(['login', '--base-url', fake.origin])
    expect((await run(['logout', '--base-url', fake.origin])).out).toContain(
      'Signed out',
    )
    expect(fake.revokes).toEqual(['rt-1'])
    expect((await run(['logout', '--base-url', fake.origin])).out).toContain(
      'Not signed in',
    )
    await run(['login', '--base-url', fake.origin])
    fake.revokeOk = false
    const failed = await run(['logout', '--base-url', fake.origin])
    expect(failed.out).toContain('could not revoke')
    expect((await run(['token', '--base-url', fake.origin])).code).toBe(1)
  })

  it('rejects an invalid --account before opening anything', async () => {
    const open = vi.fn(browser)
    const result = await run(
      ['login', '--base-url', fake.origin, '--account', 'abc'],
      open,
    )
    expect(result.code).toBe(1)
    expect(open).not.toHaveBeenCalled()
  })

  it('surfaces a browser error and stores nothing', async () => {
    const denied = async (url: string) => {
      redirect(url, (state) => `error=access_denied&state=${state}`)
      return true
    }
    const result = await run(['login', '--base-url', fake.origin], denied)
    expect(result.code).toBe(1)
    expect(result.err).toContain('Sign-in failed: access_denied')
    expect((await run(['token', '--base-url', fake.origin])).code).toBe(1)
  })

  it('times out after the configured wait', async () => {
    await expect(
      login({
        resource: fake.resource,
        scopes: ['interchange:read'],
        browser: true,
        timeoutMs: 30,
        open: async () => true,
        say: () => {},
      }),
    ).rejects.toThrow('Timed out')
  })
})
