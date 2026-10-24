/**
 * The credential store behind `apostra login`, shared by the CLI and the SDK.
 *
 * Node only. Nothing here imports a Node module at load time (it uses
 * `process.getBuiltinModule`), so a browser bundle can include the SDK and
 * simply never call it. The SDK never opens a browser; the interactive sign-in
 * lives in `@apostra/cli`.
 */
import { baseUrl as defaultBaseUrl } from './generated/metadata.js'
import type { TokenProvider } from './transport.js'

export type CliLoginEntry = {
  issuer: string
  resource: string
  clientId: string
  accessToken: string
  refreshToken: string
  /** ISO-8601 time the access token stops working. */
  expiresAt: string
  accountId: string
  scopes: string[]
}
export type CliLoginDiscovery = {
  issuer: string
  authorizationEndpoint: string
  tokenEndpoint: string
  revocationEndpoint?: string
  codeChallengeMethods?: string[]
}
export type CliLoginTokens = Pick<
  CliLoginEntry,
  'accessToken' | 'refreshToken' | 'expiresAt'
> & { scopes?: string[]; accountId?: string }
type Fetch = typeof globalThis.fetch
type Options = { fetch?: Fetch }

const FRESH_MARGIN_MS = 60_000
const REQUEST_TIMEOUT_MS = 15_000
const LOCK_STALE_MS = 30_000
const LOCK_HEARTBEAT_MS = 5_000
const LOCK_WAIT_MS = 30_000

// Only the Node surface used here, so the SDK compiles without @types/node.
type NodeProcess = {
  versions?: { node?: string }
  env: Record<string, string | undefined>
  platform: string
  pid: number
  getBuiltinModule?: (id: string) => unknown
}
type NodeFs = {
  readFileSync(path: string, encoding: 'utf8'): string
  mkdirSync(
    path: string,
    options: { recursive: boolean; mode: number },
  ): unknown
  chmodSync(path: string, mode: number): void
  openSync(path: string, flags: string, mode: number): number
  writeSync(fd: number, data: string): unknown
  closeSync(fd: number): void
  renameSync(from: string, to: string): void
  rmSync(path: string, options: { force: boolean }): void
  statSync(path: string): { mtimeMs: number }
  utimesSync(path: string, atime: Date, mtime: Date): void
}
type NodePath = {
  join(...parts: string[]): string
  dirname(path: string): string
  isAbsolute(path: string): boolean
}

function proc(): NodeProcess {
  const p = (globalThis as { process?: NodeProcess }).process
  if (!p?.versions?.node || typeof p.getBuiltinModule !== 'function')
    throw new Error('Apostra CLI login is available only in Node.js')
  return p
}
function node() {
  const p = proc()
  const get = p.getBuiltinModule as (id: string) => unknown
  return {
    fs: get('node:fs') as NodeFs,
    os: get('node:os') as { homedir(): string },
    path: get('node:path') as NodePath,
  }
}
const isRecord = (v: unknown): v is Record<string, unknown> =>
  typeof v === 'object' && v !== null && !Array.isArray(v)
const errorCode = (error: unknown) =>
  isRecord(error) && typeof error.code === 'string' ? error.code : undefined

/** `${XDG_CONFIG_HOME:-~/.config}/apostra/credentials.json` (`%APPDATA%` on Windows). */
export function credentialsPath(): string {
  const { os, path } = node()
  const { env, platform } = proc()
  const base =
    platform === 'win32'
      ? (env.APPDATA ?? path.join(os.homedir(), 'AppData', 'Roaming'))
      : env.XDG_CONFIG_HOME && path.isAbsolute(env.XDG_CONFIG_HOME)
        ? env.XDG_CONFIG_HOME
        : path.join(os.homedir(), '.config')
  return path.join(base, 'apostra', 'credentials.json')
}

function secureUrl(value: unknown, name: string): string {
  const url = new URL(typeof value === 'string' ? value : '')
  if (
    url.username ||
    url.password ||
    url.hash ||
    (url.protocol !== 'https:' &&
      !(
        url.protocol === 'http:' &&
        ['localhost', '127.0.0.1', '[::1]'].includes(url.hostname)
      ))
  )
    throw new TypeError(`${name} must be an HTTPS URL (HTTP only on loopback)`)
  return url.href
}

/** The store key: the API base URL without a trailing slash. */
export function normalizeBaseUrl(raw: string): string {
  const url = new URL(secureUrl(raw, 'Base URL'))
  if (url.search) throw new TypeError('Base URL must not have a query string')
  return url.href.replace(/\/$/, '')
}

/** The first-party public client for an API origin. */
export const cliClientId = (resource: string) =>
  `${new URL(resource).origin}/oauth/clients/apostra-cli.json`

function parseEntry(value: unknown): CliLoginEntry | undefined {
  if (!isRecord(value)) return undefined
  const text = ['issuer', 'resource', 'clientId', 'accessToken', 'refreshToken']
  if (
    !text.every((k) => typeof value[k] === 'string' && value[k]) ||
    typeof value.expiresAt !== 'string' ||
    Number.isNaN(Date.parse(value.expiresAt)) ||
    typeof value.accountId !== 'string' ||
    !Array.isArray(value.scopes) ||
    !value.scopes.every((s) => typeof s === 'string')
  )
    return undefined
  return value as CliLoginEntry
}

function readAll(): Record<string, unknown> {
  const { fs } = node()
  try {
    const file: unknown = JSON.parse(fs.readFileSync(credentialsPath(), 'utf8'))
    return isRecord(file) && isRecord(file.logins) ? file.logins : {}
  } catch {
    return {}
  }
}

/** Atomic (temp file + rename), directory 0700, file 0600. */
function writeAll(logins: Record<string, unknown>): void {
  const { fs, path } = node()
  const file = credentialsPath()
  const dir = path.dirname(file)
  if (Object.keys(logins).length === 0) {
    fs.rmSync(file, { force: true })
    return
  }
  fs.mkdirSync(dir, { recursive: true, mode: 0o700 })
  fs.chmodSync(dir, 0o700)
  const temp = `${file}.${proc().pid}.${Math.random().toString(36).slice(2)}.tmp`
  const fd = fs.openSync(temp, 'wx', 0o600)
  try {
    fs.writeSync(fd, `${JSON.stringify({ version: 1, logins }, null, 2)}\n`)
  } finally {
    fs.closeSync(fd)
  }
  fs.renameSync(temp, file)
}

export function readCliLogin(baseUrl: string): CliLoginEntry | undefined {
  return parseEntry(readAll()[normalizeBaseUrl(baseUrl)])
}
/** Like `readCliLogin`, but never throws: for the SDK's default credential chain. */
export function storedCliLogin(baseUrl: string): CliLoginEntry | undefined {
  try {
    return readCliLogin(baseUrl)
  } catch {
    return undefined
  }
}
export const isFresh = (entry: Pick<CliLoginEntry, 'expiresAt'>) =>
  Date.parse(entry.expiresAt) - FRESH_MARGIN_MS > Date.now()

/**
 * Serialise every read-modify-write of the store, across processes. Refresh
 * tokens rotate, so two processes must never present the same one outside the
 * server's reuse grace. A lock older than 30 seconds belongs to a dead process.
 */
export async function withCliLoginLock<T>(fn: () => Promise<T>): Promise<T> {
  const { fs, path } = node()
  const lock = `${credentialsPath()}.lock`
  fs.mkdirSync(path.dirname(lock), { recursive: true, mode: 0o700 })
  // The lock file holds its owner's token, so a process only ever removes a
  // lock it owns, and a heartbeat keeps a live lock fresh however long the
  // bounded refresh takes. Only a lock whose heartbeat stopped is stale.
  const owner = `${proc().pid}:${globalThis.crypto.randomUUID()}`
  const ownerOf = () => {
    try {
      return fs.readFileSync(lock, 'utf8')
    } catch {
      return undefined
    }
  }
  const deadline = Date.now() + LOCK_WAIT_MS
  for (;;) {
    try {
      const fd = fs.openSync(lock, 'wx', 0o600)
      try {
        fs.writeSync(fd, owner)
      } finally {
        fs.closeSync(fd)
      }
      break
    } catch (error) {
      if (errorCode(error) !== 'EEXIST') throw error
      try {
        const stale = ownerOf()
        if (Date.now() - fs.statSync(lock).mtimeMs > LOCK_STALE_MS) {
          if (ownerOf() === stale) fs.rmSync(lock, { force: true })
          continue
        }
      } catch {
        continue
      }
      if (Date.now() > deadline)
        throw new Error('Timed out waiting for another Apostra login process')
      await new Promise((r) => setTimeout(r, 25 + Math.random() * 50))
    }
  }
  const heartbeat = setInterval(() => {
    try {
      if (ownerOf() === owner) fs.utimesSync(lock, new Date(), new Date())
    } catch {
      // A missed beat only shortens the lease; the owner check still holds.
    }
  }, LOCK_HEARTBEAT_MS)
  ;(heartbeat as { unref?: () => void }).unref?.()
  try {
    return await fn()
  } finally {
    clearInterval(heartbeat)
    if (ownerOf() === owner) fs.rmSync(lock, { force: true })
  }
}

/** Save a login. Call inside `withCliLoginLock`. */
export function writeCliLogin(baseUrl: string, entry: CliLoginEntry): void {
  writeAll({ ...readAll(), [normalizeBaseUrl(baseUrl)]: entry })
}

async function send(
  fetcher: Fetch,
  url: string,
  init: RequestInit = {},
): Promise<Response> {
  return fetcher(url, {
    ...init,
    headers: { Accept: 'application/json', ...init.headers },
    redirect: 'error',
    signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
  })
}
async function getJson(fetcher: Fetch, url: string): Promise<unknown> {
  const response = await send(fetcher, url)
  if (!response.ok)
    throw new Error(`Could not read ${url} (HTTP ${response.status})`)
  return response.json()
}
function wellKnown(name: string, location: string): string {
  const url = new URL(location)
  return `${url.origin}/.well-known/${name}${url.pathname === '/' ? '' : url.pathname}`
}

/** Protected-resource metadata, then authorization-server metadata (RFC 9728, RFC 8414). */
export async function discoverCliLogin(
  resource: string,
  { fetch: f = globalThis.fetch }: Options = {},
): Promise<CliLoginDiscovery> {
  const prm = await getJson(f, wellKnown('oauth-protected-resource', resource))
  if (
    !isRecord(prm) ||
    typeof prm.resource !== 'string' ||
    prm.resource.replace(/\/$/, '') !== resource ||
    !Array.isArray(prm.authorization_servers)
  )
    throw new Error(
      `${resource} does not publish OAuth protected-resource metadata`,
    )
  const issuer = secureUrl(prm.authorization_servers[0], 'Issuer').replace(
    /\/$/,
    '',
  )
  const as = await getJson(f, wellKnown('oauth-authorization-server', issuer))
  if (!isRecord(as) || as.issuer !== issuer)
    throw new Error(
      `${issuer} published mismatched authorization-server metadata`,
    )
  const methods = as.code_challenge_methods_supported
  return {
    issuer,
    authorizationEndpoint: secureUrl(
      as.authorization_endpoint,
      'authorization_endpoint',
    ),
    tokenEndpoint: secureUrl(as.token_endpoint, 'token_endpoint'),
    revocationEndpoint:
      as.revocation_endpoint === undefined
        ? undefined
        : secureUrl(as.revocation_endpoint, 'revocation_endpoint'),
    codeChallengeMethods: Array.isArray(methods)
      ? methods.map(String)
      : undefined,
  }
}

async function tokenRequest(
  { fetch: f = globalThis.fetch }: Options,
  discovery: CliLoginDiscovery,
  resource: string,
  form: Record<string, string>,
): Promise<CliLoginTokens> {
  const response = await send(f, discovery.tokenEndpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ ...form, resource }),
  })
  const body: unknown = await response.json().catch(() => undefined)
  if (!response.ok) {
    // Never echo the response body: it may carry reflected credentials.
    if (isRecord(body) && body.error === 'invalid_grant')
      throw new Error(
        'Your Apostra login expired or was revoked. Run `apostra login` again.',
      )
    throw new Error(`Apostra token request failed (HTTP ${response.status})`)
  }
  if (
    !isRecord(body) ||
    typeof body.access_token !== 'string' ||
    !body.access_token ||
    typeof body.expires_in !== 'number' ||
    !(body.expires_in > 0)
  )
    throw new Error('Apostra token response is invalid')
  // Rotation: the old refresh token is spent; keep the new one. A refresh that
  // does not rotate keeps the old one, but a login with no refresh token
  // could not be kept past the access token's hour, so it is refused here,
  // before anything is written.
  const refreshToken =
    typeof body.refresh_token === 'string' && body.refresh_token
      ? body.refresh_token
      : form.refresh_token
  if (!refreshToken)
    throw new Error(
      'Apostra did not return a refresh token, so this login cannot be kept. Run `apostra login` again.',
    )
  const account = body.account_id
  return {
    accessToken: body.access_token,
    refreshToken,
    expiresAt: new Date(Date.now() + body.expires_in * 1000).toISOString(),
    scopes:
      typeof body.scope === 'string'
        ? body.scope.split(' ').filter(Boolean)
        : undefined,
    accountId:
      typeof account === 'string' || typeof account === 'number'
        ? String(account)
        : undefined,
  }
}

export function exchangeCliLoginCode(
  options: Options,
  discovery: CliLoginDiscovery,
  resource: string,
  grant: { code: string; verifier: string; redirectUri: string },
): Promise<CliLoginTokens> {
  return tokenRequest(options, discovery, resource, {
    grant_type: 'authorization_code',
    code: grant.code,
    code_verifier: grant.verifier,
    redirect_uri: grant.redirectUri,
    client_id: cliClientId(resource),
  })
}

/**
 * Return a usable login for `baseUrl`, refreshing it if the access token is
 * about to expire. After taking the lock the file is read again: if another
 * process refreshed first, its token is used and no request is made.
 */
export async function refreshCliLogin(
  baseUrl: string,
  options: Options = {},
): Promise<CliLoginEntry> {
  const key = normalizeBaseUrl(baseUrl)
  const missing = () =>
    new Error(`Not signed in to ${key}. Run \`apostra login\`.`)
  const first = readCliLogin(key)
  if (!first) throw missing()
  if (isFresh(first)) return first
  return withCliLoginLock(async () => {
    const entry = readCliLogin(key)
    if (!entry) throw missing()
    if (isFresh(entry)) return entry
    const discovery = await discoverCliLogin(entry.resource, options)
    const tokens = await tokenRequest(options, discovery, entry.resource, {
      grant_type: 'refresh_token',
      refresh_token: entry.refreshToken,
      client_id: entry.clientId,
    })
    const next: CliLoginEntry = {
      ...entry,
      accessToken: tokens.accessToken,
      refreshToken: tokens.refreshToken,
      expiresAt: tokens.expiresAt,
      scopes: tokens.scopes ?? entry.scopes,
    }
    writeCliLogin(key, next)
    return next
  })
}

/**
 * Revoke the refresh token (RFC 7009), then delete the entry. The entry is
 * deleted even when revocation fails; `revoked` tells the caller which.
 */
export async function logoutCliLogin(
  baseUrl: string,
  { fetch: f = globalThis.fetch }: Options = {},
): Promise<{ found: boolean; revoked: boolean }> {
  const key = normalizeBaseUrl(baseUrl)
  return withCliLoginLock(async () => {
    const entry = readCliLogin(key)
    if (!entry) return { found: false, revoked: false }
    let revoked = false
    try {
      const { revocationEndpoint } = await discoverCliLogin(entry.resource, {
        fetch: f,
      })
      if (revocationEndpoint)
        revoked = (
          await send(f, revocationEndpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
              token: entry.refreshToken,
              token_type_hint: 'refresh_token',
              client_id: entry.clientId,
            }),
          })
        ).ok
    } catch {
      revoked = false
    }
    const { [key]: _removed, ...rest } = readAll()
    writeAll(rest)
    return { found: true, revoked }
  })
}

/**
 * A token provider backed by `apostra login`. Use it as `tokenProvider`, or
 * rely on the default credential chain, which uses it when no explicit
 * credential or `APOSTRA_API_KEY` is set and a login exists for the base URL.
 */
export function cliLoginTokenProvider(
  options: { baseUrl?: string; fetch?: Fetch } = {},
): TokenProvider {
  const key = normalizeBaseUrl(
    options.baseUrl ?? proc().env.APOSTRA_BASE_URL ?? defaultBaseUrl,
  )
  let refreshing: Promise<string> | undefined
  return () => {
    const entry = readCliLogin(key)
    if (entry && isFresh(entry)) return entry.accessToken
    refreshing ??= refreshCliLogin(key, { fetch: options.fetch })
      .then((e) => e.accessToken)
      .finally(() => {
        refreshing = undefined
      })
    return refreshing
  }
}
