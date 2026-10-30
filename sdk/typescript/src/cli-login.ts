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
  emitWarning?: (warning: string) => void
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
type NodeModule = {
  createRequire(url: string): (id: string) => unknown
}
type KeyringEntry = {
  getPassword(): string | null
  setPassword(password: string): void
  deletePassword(): boolean
}
type Keyring = {
  Entry: new (
    service: string,
    username: string,
    options?: { linux?: { store: 'secret-service' } },
  ) => KeyringEntry
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
    module: get('node:module') as NodeModule,
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
  const expiresAt =
    typeof value.expiresAt === 'string' &&
    !Number.isNaN(Date.parse(value.expiresAt))
      ? new Date(value.expiresAt).toISOString()
      : undefined
  if (
    !text.every((k) => typeof value[k] === 'string' && value[k]) ||
    !expiresAt ||
    typeof value.accountId !== 'string' ||
    !Array.isArray(value.scopes) ||
    !value.scopes.every((s) => typeof s === 'string')
  )
    return undefined
  // Credential stores round-trip text. Canonicalise at their boundary so a
  // value with sub-millisecond precision cannot oscillate between clients.
  return { ...value, expiresAt } as CliLoginEntry
}

type FileLogins = {
  logins: Record<string, unknown>
  authoritative: Set<string>
}

function readFileStore(): FileLogins {
  const { fs } = node()
  try {
    const file: unknown = JSON.parse(fs.readFileSync(credentialsPath(), 'utf8'))
    if (!isRecord(file) || !isRecord(file.logins))
      return { logins: {}, authoritative: new Set() }
    return {
      logins: file.logins,
      authoritative: new Set(
        Array.isArray(file.authoritativeFileLogins)
          ? file.authoritativeFileLogins.filter(
              (resource): resource is string => typeof resource === 'string',
            )
          : [],
      ),
    }
  } catch {
    return { logins: {}, authoritative: new Set() }
  }
}

/** Atomic (temp file + rename), directory 0700, file 0600. */
function writeFileLogins(
  logins: Record<string, unknown>,
  authoritative = new Set<string>(),
): void {
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
    fs.writeSync(
      fd,
      `${JSON.stringify(
        {
          version: 1,
          logins,
          ...(authoritative.size > 0
            ? {
                authoritativeFileLogins: [...authoritative]
                  .filter((resource) => resource in logins)
                  .sort(),
              }
            : {}),
        },
        null,
        2,
      )}\n`,
    )
  } finally {
    fs.closeSync(fd)
  }
  fs.renameSync(temp, file)
}

const keyringService = 'Apostra CLI login'

/**
 * Resolve the native binding only when this Node-only feature is used. A static
 * import would make the browser SDK bundle a native module.
 */
function keyringEntry(resource: string): KeyringEntry {
  const { module } = node()
  const required = module.createRequire(import.meta.url)('@napi-rs/keyring')
  if (!isRecord(required) || typeof required.Entry !== 'function')
    throw new Error('Apostra credential-store binding is unavailable')
  const Entry = required.Entry as Keyring['Entry']
  // Do not accept keyutils on Linux. It is ephemeral and is not the requested
  // Secret Service store, so an inaccessible service deliberately uses the
  // documented 0600-file fallback instead.
  return new Entry(
    keyringService,
    resource,
    proc().platform === 'linux'
      ? { linux: { store: 'secret-service' } }
      : undefined,
  )
}

type SecureRead = { available: boolean; entry?: CliLoginEntry }

function readSecureLogin(resource: string): SecureRead {
  try {
    const password = keyringEntry(resource).getPassword()
    if (!password) return { available: true }
    return { available: true, entry: parseEntry(JSON.parse(password)) }
  } catch {
    return { available: false }
  }
}

function writeSecureLogin(resource: string, entry: CliLoginEntry): boolean {
  try {
    keyringEntry(resource).setPassword(JSON.stringify(entry))
    return true
  } catch {
    return false
  }
}

function deleteSecureLogin(resource: string): boolean | undefined {
  try {
    return keyringEntry(resource).deletePassword()
  } catch {
    return undefined
  }
}

function warnFileFallback(): void {
  const { fs, path } = node()
  const dir = path.dirname(credentialsPath())
  const marker = path.join(dir, '.file-store-warning')
  try {
    fs.mkdirSync(dir, { recursive: true, mode: 0o700 })
    fs.chmodSync(dir, 0o700)
    const fd = fs.openSync(marker, 'wx', 0o600)
    fs.closeSync(fd)
  } catch (error) {
    if (errorCode(error) === 'EEXIST') return
    // If the marker cannot be written, warn for this process rather than
    // silently accepting plaintext storage.
  }
  proc().emitWarning?.(
    `Apostra could not access your OS credential store. Login tokens are stored in ${credentialsPath()} with 0600 permissions. Use Keychain, Credential Manager, or Secret Service when available.`,
  )
}

/**
 * Move every legacy entry while holding the normal refresh lock. Reads that
 * arrive first use a short synchronous instance of the same lock; contenders
 * keep reading the legacy file until the migration finishes.
 */
function migrateFileLogins(lockHeld = false): boolean {
  const { fs, path } = node()
  const fileStore = readFileStore()
  const fileLogins = fileStore.logins
  const entries = Object.entries(fileLogins).flatMap(([resource, value]) => {
    const entry = parseEntry(value)
    return entry ? [[resource, entry] as const] : []
  })
  if (entries.length === 0) return false

  const lock = `${credentialsPath()}.lock`
  let owner: string | undefined
  if (!lockHeld) {
    fs.mkdirSync(path.dirname(lock), { recursive: true, mode: 0o700 })
    owner = `migration:${proc().pid}:${globalThis.crypto.randomUUID()}`
    try {
      const fd = fs.openSync(lock, 'wx', 0o600)
      try {
        fs.writeSync(fd, owner)
      } finally {
        fs.closeSync(fd)
      }
    } catch {
      return false
    }
  }

  try {
    const remaining = { ...fileLogins }
    const remainingAuthoritative = new Set(fileStore.authoritative)
    for (const [resource, entry] of entries) {
      // A keyring value is authoritative: preserving it avoids overwriting a
      // token another process has already refreshed during an interrupted
      // earlier migration, unless the protected fallback marks a replacement
      // as authoritative after a failed secure-store rotation.
      const stored = readSecureLogin(resource)
      if (!fileStore.authoritative.has(resource) && stored.entry) {
        delete remaining[resource]
        remainingAuthoritative.delete(resource)
        continue
      }
      if (!stored.available || !writeSecureLogin(resource, entry)) {
        // Retain only entries that still need migration. Otherwise a
        // successfully migrated authoritative login could shadow its next
        // secure-store refresh while another login remains in the file.
        writeFileLogins(remaining, remainingAuthoritative)
        return false
      }
      delete remaining[resource]
      remainingAuthoritative.delete(resource)
    }
    writeFileLogins(remaining, remainingAuthoritative)
    return true
  } finally {
    if (owner) {
      try {
        if (fs.readFileSync(lock, 'utf8') === owner)
          fs.rmSync(lock, { force: true })
      } catch {
        // The regular lock protocol protects against removing another owner.
      }
    }
  }
}

export function readCliLogin(baseUrl: string): CliLoginEntry | undefined {
  const resource = normalizeBaseUrl(baseUrl)
  const fileStore = readFileStore()
  const fileEntry = parseEntry(fileStore.logins[resource])
  // A refresh token can rotate before a credential store reports an update
  // failure. This marker makes its 0600 fallback authoritative over the now
  // invalid secure-store value until a later read can migrate it safely.
  if (fileStore.authoritative.has(resource) && fileEntry) return fileEntry
  const secure = readSecureLogin(resource)
  if (secure.entry) return secure.entry

  const fileLogins = fileStore.logins
  if (Object.keys(fileLogins).length === 0) return undefined
  if (migrateFileLogins()) return readSecureLogin(resource).entry

  if (!secure.available) warnFileFallback()
  return fileEntry
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
 * Remove a lock whose heartbeat stopped, without ever removing a live one.
 * Only the holder of the takeover guard checks and removes. Checking again
 * under the guard means a lock another process took after the first check is
 * fresh and is left alone. A guard a crashed process left behind goes stale
 * like a lock does. Returns whether this call held the guard, so the caller
 * retries at once; otherwise it waits like any other contender.
 */
function breakStaleLock(fs: NodeFs, lock: string): boolean {
  const guard = `${lock}.takeover`
  try {
    fs.closeSync(fs.openSync(guard, 'wx', 0o600))
  } catch (error) {
    if (errorCode(error) !== 'EEXIST') throw error
    try {
      if (Date.now() - fs.statSync(guard).mtimeMs > LOCK_STALE_MS)
        fs.rmSync(guard, { force: true })
    } catch {
      // The guard went away between the two calls; the caller retries.
    }
    return false
  }
  try {
    if (Date.now() - fs.statSync(lock).mtimeMs > LOCK_STALE_MS)
      fs.rmSync(lock, { force: true })
  } catch {
    // The lock went away; the caller retries.
  } finally {
    fs.rmSync(guard, { force: true })
  }
  return true
}

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
        if (Date.now() - fs.statSync(lock).mtimeMs > LOCK_STALE_MS) {
          if (breakStaleLock(fs, lock)) continue
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
  const resource = normalizeBaseUrl(baseUrl)
  const normalised = parseEntry(entry)
  if (!normalised) throw new TypeError('Apostra login is invalid')
  // Callers hold the cross-process lock, so the legacy file cannot overwrite
  // a rotated credential while it is being migrated.
  migrateFileLogins(true)
  const existing = readSecureLogin(resource)
  if (writeSecureLogin(resource, normalised)) return
  warnFileFallback()
  const fileStore = readFileStore()
  // A refresh token may rotate while the OS credential store disappears. Its
  // next read could reveal the older credential, so the protected fallback is
  // authoritative both when we saw an old entry and when availability is
  // unknown.
  if (!existing.available || existing.entry)
    fileStore.authoritative.add(resource)
  writeFileLogins(
    { ...fileStore.logins, [resource]: normalised },
    fileStore.authoritative,
  )
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
 * about to expire. After taking the lock the credential store is read again:
 * if another process refreshed first, its token is used and no request is made.
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
    deleteSecureLogin(key)
    // A prior fallback login can still be present even when the credential
    // store has no entry (or is available again). Remove it unconditionally:
    // otherwise its refresh token could be migrated back after logout.
    const fileStore = readFileStore()
    const { [key]: _removed, ...rest } = fileStore.logins
    fileStore.authoritative.delete(key)
    writeFileLogins(rest, fileStore.authoritative)
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
