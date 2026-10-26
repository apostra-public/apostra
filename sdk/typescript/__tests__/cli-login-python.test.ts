import { spawn, spawnSync } from 'node:child_process'
import {
  appendFileSync,
  existsSync,
  mkdtempSync,
  readFileSync,
  rmSync,
} from 'node:fs'
import { createServer, type Server } from 'node:http'
import type { AddressInfo } from 'node:net'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import {
  type CliLoginEntry,
  cliClientId,
  normalizeBaseUrl,
  readCliLogin,
  refreshCliLogin,
  withCliLoginLock,
  writeCliLogin,
} from '../src/cli-login.js'

/**
 * The CLI and both SDKs share one credentials file and one lock file. These
 * tests run the Python store and the TypeScript store against the same files.
 */
const pythonDir = ['../../apostra-sdk-python', '../../python']
  .map((p) => resolve(import.meta.dirname, p))
  .find((p) => existsSync(join(p, 'pyproject.toml')))
const uvArgs = (script: string, ...args: string[]) => [
  'run',
  '--frozen',
  '--directory',
  pythonDir ?? '.',
  'python',
  '-I',
  '-c',
  script,
  ...args,
]
const pythonReady =
  pythonDir !== undefined &&
  spawnSync('uv', uvArgs('import apostra.cli_login'), {
    stdio: 'ignore',
    timeout: 180_000,
  }).status === 0

let dir: string
let origin: string
let server: Server
let refreshRequests = 0

const env = () => ({ ...process.env, XDG_CONFIG_HOME: dir, APPDATA: dir })
const python = (script: string, ...args: string[]) =>
  new Promise<{ code: number | null; out: string; err: string }>((done) => {
    const child = spawn('uv', uvArgs(script, ...args), { env: env() })
    let out = ''
    let err = ''
    child.stdout.on('data', (d) => {
      out += d
    })
    child.stderr.on('data', (d) => {
      err += d
    })
    child.on('close', (code) => done({ code, out: out.trim(), err }))
  })
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))
const waitFor = async (predicate: () => boolean) => {
  for (let i = 0; i < 600 && !predicate(); i++) await sleep(50)
  expect(predicate()).toBe(true)
}

const entry = (): CliLoginEntry => ({
  issuer: origin,
  resource: `${origin}/api/v3`,
  clientId: cliClientId(`${origin}/api/v3`),
  accessToken: 'at-0',
  refreshToken: 'rt-0',
  expiresAt: new Date(Date.now() - 1000).toISOString(),
  accountId: '7',
  scopes: ['interchange:read'],
})

beforeEach(async () => {
  dir = mkdtempSync(join(tmpdir(), 'apostra-xlang-'))
  vi.stubEnv('XDG_CONFIG_HOME', dir)
  vi.stubEnv('APPDATA', dir)
  refreshRequests = 0
  server = createServer(async (req, res) => {
    const url = new URL(req.url ?? '/', origin)
    const json = (status: number, body: unknown) => {
      res.writeHead(status, { 'Content-Type': 'application/json' })
      res.end(JSON.stringify(body))
    }
    if (url.pathname === '/.well-known/oauth-protected-resource/api/v3')
      return json(200, {
        resource: `${origin}/api/v3`,
        authorization_servers: [origin],
      })
    if (url.pathname === '/.well-known/oauth-authorization-server')
      return json(200, {
        issuer: origin,
        authorization_endpoint: `${origin}/authorize`,
        token_endpoint: `${origin}/auth/token`,
      })
    if (url.pathname === '/auth/token') {
      for await (const _chunk of req);
      const number = ++refreshRequests
      await sleep(300)
      return json(200, {
        access_token: `at-${number}`,
        refresh_token: `rt-${number}`,
        expires_in: 3600,
        scope: 'interchange:read',
      })
    }
    json(404, {})
  })
  await new Promise<void>((r) => server.listen(0, '127.0.0.1', r))
  origin = `http://127.0.0.1:${(server.address() as AddressInfo).port}`
  server.unref()
})
afterEach(async () => {
  vi.unstubAllEnvs()
  await new Promise<void>((r) => server.close(() => r()))
  rmSync(dir, { recursive: true, force: true })
})

describe.skipIf(!pythonReady)('Python and TypeScript share the store', () => {
  it('serialises a Python holder and a TypeScript waiter', async () => {
    const log = join(dir, 'events.log')
    const holder = python(
      [
        'import sys, time',
        'from apostra.cli_login import cli_login_lock',
        'with cli_login_lock():',
        '    open(sys.argv[1], "a").write("py-in\\n")',
        '    time.sleep(1.5)',
        '    open(sys.argv[1], "a").write("py-out\\n")',
      ].join('\n'),
      log,
    )
    await waitFor(() => existsSync(log))
    await withCliLoginLock(async () => appendFileSync(log, 'ts-in\n'))
    appendFileSync(log, 'ts-out\n')
    expect((await holder).code).toBe(0)
    expect(readFileSync(log, 'utf8').trim().split('\n')).toEqual([
      'py-in',
      'py-out',
      'ts-in',
      'ts-out',
    ])
  }, 120_000)

  it('serialises a TypeScript holder and a Python waiter', async () => {
    const log = join(dir, 'events.log')
    let waiter: ReturnType<typeof python> | undefined
    await withCliLoginLock(async () => {
      appendFileSync(log, 'ts-in\n')
      waiter = python(
        [
          'import sys',
          'from apostra.cli_login import cli_login_lock',
          'with cli_login_lock():',
          '    open(sys.argv[1], "a").write("py-in\\n")',
        ].join('\n'),
        log,
      )
      await sleep(2_500)
      appendFileSync(log, 'ts-out\n')
    })
    expect((await waiter)?.code).toBe(0)
    expect(readFileSync(log, 'utf8').trim().split('\n')).toEqual([
      'ts-in',
      'ts-out',
      'py-in',
    ])
  }, 120_000)

  it('makes exactly one token request when both languages refresh at once', async () => {
    await withCliLoginLock(async () =>
      writeCliLogin(`${origin}/api/v3`, entry()),
    )
    const py = python(
      [
        'import sys',
        'from apostra.cli_login import refresh_cli_login',
        'print(refresh_cli_login(sys.argv[1])["accessToken"])',
      ].join('\n'),
      `${origin}/api/v3`,
    )
    const ts = refreshCliLogin(`${origin}/api/v3`)
    const [pyResult, tsResult] = await Promise.all([py, ts])
    expect(pyResult.code).toBe(0)
    expect(refreshRequests).toBe(1)
    expect(pyResult.out).toBe('at-1')
    expect(tsResult.accessToken).toBe('at-1')
    expect(readCliLogin(`${origin}/api/v3`)?.refreshToken).toBe('rt-1')
  }, 120_000)

  it('reads what the other language wrote and keeps the same file shape', async () => {
    await withCliLoginLock(async () =>
      writeCliLogin(`${origin}/api/v3`, entry()),
    )
    const result = await python(
      [
        'import sys, json',
        'from apostra.cli_login import refresh_cli_login',
        'refresh_cli_login(sys.argv[1])',
      ].join('\n'),
      `${origin}/api/v3`,
    )
    expect(result.code).toBe(0)
    const stored = readCliLogin(`${origin}/api/v3`)
    expect(stored).toMatchObject({
      issuer: origin,
      accessToken: 'at-1',
      refreshToken: 'rt-1',
      accountId: '7',
      scopes: ['interchange:read'],
    })
    expect(Date.parse(stored?.expiresAt ?? '')).toBeGreaterThan(Date.now())
    expect(
      JSON.parse(readFileSync(join(dir, 'apostra', 'credentials.json'), 'utf8'))
        .version,
    ).toBe(1)
  }, 120_000)

  it('keys a base URL the way the TypeScript store does', async () => {
    const urls = [
      'https://api.apostra.com/api/v3',
      'https://API.apostra.com/api/v3/',
      'https://api.apostra.com',
      'https://api.apostra.com:443/api/v3',
      'http://127.0.0.1:8080/api/v3',
      'http://localhost',
      'http://[::1]:3000/x',
    ]
    const result = await python(
      [
        'import sys, json',
        'from apostra.cli_login import normalize_base_url',
        'print(json.dumps([normalize_base_url(u) for u in sys.argv[1:]]))',
      ].join('\n'),
      ...urls,
    )
    expect(result.code).toBe(0)
    expect(JSON.parse(result.out)).toEqual(urls.map(normalizeBaseUrl))
  }, 120_000)
})
