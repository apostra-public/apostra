import type { OperationTypes } from './generated/client.js'
import {
  baseUrl,
  m2mTokenUrl,
  type OperationId,
  operations,
  version,
} from './generated/metadata.js'
import type {
  AdcpError,
  InFlightReceipt,
  OpenCampaignsPageSuccessPageHumanHandoffRequired,
} from './generated/types.gen.js'

export type TokenProvider = () => string | Promise<string>
export type M2mTokenProviderOptions = {
  clientId: string
  clientSecret: string
  scope: string | string[]
  /** Override fetch for testing or an application-owned HTTP implementation. */
  fetch?: typeof globalThis.fetch
  /** Deadline for an M2M token refresh. Defaults to 30 seconds. */
  timeoutMs?: number
}
export type ClientOptions = {
  /** Supply exactly one credential source. Providers own acquisition/refresh. */
  apiKey?: string
  accessToken?: string
  tokenProvider?: TokenProvider
  accountId?: string
  baseUrl?: string
  fetch?: typeof globalThis.fetch
  timeoutMs?: number
  /** Retry transient read failures and caller-keyed writes this many times. */
  maxRetries?: number
}
export type RequestOptions = {
  accountId?: string
  /** Required by generated write methods. Never generated or replaced by the SDK. */
  idempotencyKey?: string
  signal?: AbortSignal
  timeoutMs?: number
}
export type WriteRequestOptions = RequestOptions & { idempotencyKey: string }
type WriteOperationId = {
  [O in OperationId]: (typeof operations)[O]['idempotencyKey'] extends true
    ? O
    : never
}[OperationId]
type ReadOperationId = Exclude<OperationId, WriteOperationId>
export type ResponseDetails<T> = {
  data: T
  status: number
  headers: Headers
  requestId: string | null
}
export type HumanHandoff = Pick<
  OpenCampaignsPageSuccessPageHumanHandoffRequired,
  'kind' | 'url' | 'expiresAt' | 'resume'
>
type M2mTokenResponse = {
  access_token: string
  expires_in: number
}
export type ApostraErrorCode =
  | 'UNAUTHENTICATED'
  | 'AUTHENTICATION_FAILED'
  | 'ACCESS_DENIED'
  | 'NOT_FOUND'
  | 'CONFLICT'
  | 'RATE_LIMITED'
  | 'VALIDATION_FAILED'
  | (string & {})
type Recovery = 'transient' | 'correctable' | 'terminal'
type InFlightReceiptEnvelope = {
  data: { receipt: InFlightReceipt }
  error: null
}
export class ApostraError extends Error {
  readonly code: ApostraErrorCode
  readonly recovery: Recovery
  readonly retryAfter: number | null
  readonly retryable: boolean
  constructor(
    readonly status: number,
    readonly error: AdcpError,
    readonly requestId: string | null,
  ) {
    // Server messages/details are available explicitly. Do not include them in
    // the default exception string: they can contain reflected request secrets.
    const code = error.code as ApostraErrorCode
    const recovery = error.recovery ?? recoveryForStatus(status)
    const retryAfter = error.retry_after ?? null
    super(
      `Apostra request failed (${status} ${code}${requestId ? `, request ${requestId}` : ''})`,
    )
    this.name = 'ApostraError'
    this.code = code
    this.recovery = recovery
    this.retryAfter = retryAfter
    this.retryable = recovery === 'transient'
  }
}
export class AuthenticationError extends ApostraError {}
export class PermissionError extends ApostraError {}
export class NotFoundError extends ApostraError {}
export class ConflictError extends ApostraError {}
export class RateLimitError extends ApostraError {}
export class ValidationError extends ApostraError {}
/** @deprecated This compatibility export is never thrown by the transport. */
export class UnsupportedCapabilityError extends Error {}
export class ConnectionError extends Error {
  readonly code = 'CONNECTION_ERROR' as const
  readonly recovery = 'transient' as const
  readonly retryAfter = null
  readonly retryable = true
  readonly requestId = null
  constructor(cause: unknown) {
    super('Apostra connection failed', { cause })
    this.name = 'ConnectionError'
  }
}
export class TimeoutError extends Error {
  readonly code = 'TIMEOUT' as const
  readonly recovery = 'transient' as const
  readonly retryAfter = null
  readonly retryable = true
  readonly requestId = null
  constructor(cause: unknown) {
    super('Apostra request timed out', { cause })
    this.name = 'TimeoutError'
  }
}
export class ProtocolError extends Error {
  constructor(
    readonly status: number,
    readonly requestId: string | null,
  ) {
    super(`Unexpected Apostra response (${status})`)
    this.name = 'ProtocolError'
  }
}
/**
 * The server accepted a write but cannot yet honestly report its completion.
 *
 * Callers retain the original operation-specific idempotency key; the SDK
 * never makes another request or creates a replacement key.
 */
export class InFlightReceiptError extends Error {
  readonly status = 202
  constructor(
    readonly requestId: string | null,
    readonly retryAfterMs: number | null,
    readonly receipt: InFlightReceipt,
  ) {
    super('Apostra write is still in flight')
    this.name = 'InFlightReceiptError'
  }
}
const account = (value: string | undefined) => {
  if (value !== undefined && !/^[1-9][0-9]*$/.test(value))
    throw new TypeError('accountId must be a positive integer string')
  return value
}
function record(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}
function credentialPart(value: string, name: string): string {
  if (!value || /[\r\n]/.test(value))
    throw new TypeError(`${name} must be a non-empty single-line string`)
  return value
}
function m2mScope(value: string | string[]): string {
  const scope = Array.isArray(value) ? value.join(' ') : value
  if (!scope.trim() || /[\r\n]/.test(scope))
    throw new TypeError('scope must be a non-empty single-line string')
  return scope
}
function m2mTimeoutMs(value: number | undefined): number {
  const timeoutMs = value ?? 30_000
  if (!Number.isFinite(timeoutMs) || timeoutMs <= 0)
    throw new TypeError('timeoutMs must be a positive finite number')
  return timeoutMs
}
/**
 * Acquire and cache an OAuth client-credentials token for server-side use.
 *
 * The returned provider performs one refresh for concurrent callers and refreshes
 * 60 seconds before expiry. It never persists or logs a client secret or token.
 */
export function m2mTokenProvider({
  clientId: rawClientId,
  clientSecret: rawClientSecret,
  scope: rawScope,
  fetch: suppliedFetch,
  timeoutMs: rawTimeoutMs,
}: M2mTokenProviderOptions): TokenProvider {
  const clientId = credentialPart(rawClientId, 'clientId')
  const clientSecret = credentialPart(rawClientSecret, 'clientSecret')
  const scope = m2mScope(rawScope)
  const fetcher = suppliedFetch ?? globalThis.fetch
  const timeoutMs = m2mTimeoutMs(rawTimeoutMs)
  let token: string | undefined
  let expiresAt = 0
  let refreshing: Promise<string> | undefined
  const refresh = async (): Promise<string> => {
    let response: Response
    const signal = AbortSignal.timeout(timeoutMs)
    try {
      response = await fetcher(m2mTokenUrl, {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          client_id: clientId,
          client_secret: clientSecret,
          grant_type: 'client_credentials',
          scope,
        }),
        redirect: 'error',
        signal,
      })
    } catch (cause) {
      if (signal.aborted) throw new TimeoutError(cause)
      throw new ConnectionError(cause)
    }
    if (!response.ok)
      throw new Error(`M2M token request failed (${response.status})`)
    let payload: unknown
    try {
      payload = await response.json()
    } catch {
      throw new Error('M2M token response is invalid')
    }
    if (
      !record(payload) ||
      typeof payload.access_token !== 'string' ||
      !payload.access_token ||
      /[\r\n]/.test(payload.access_token) ||
      typeof payload.expires_in !== 'number' ||
      !Number.isFinite(payload.expires_in) ||
      payload.expires_in <= 0
    )
      throw new Error('M2M token response is invalid')
    const result = payload as M2mTokenResponse
    token = result.access_token
    expiresAt = Date.now() + Math.max(0, result.expires_in * 1000 - 60_000)
    return token
  }
  return () => {
    if (token && Date.now() < expiresAt) return token
    refreshing ??= refresh().finally(() => {
      refreshing = undefined
    })
    return refreshing
  }
}
function errorModel(value: unknown): value is AdcpError {
  return (
    record(value) &&
    typeof value.code === 'string' &&
    typeof value.message === 'string'
  )
}

function inFlightReceipt(value: unknown): value is InFlightReceiptEnvelope {
  if (!record(value)) return false
  const data = value.data
  if (!record(data) || !record(data.receipt)) return false
  const receipt = data.receipt
  return (
    value.error === null &&
    typeof receipt.id === 'string' &&
    typeof receipt.operation === 'string' &&
    typeof receipt.state === 'string' &&
    ['claimed', 'running', 'uncertain'].includes(receipt.state) &&
    typeof receipt.stateVersion === 'number' &&
    Number.isInteger(receipt.stateVersion) &&
    receipt.stateVersion >= 1 &&
    typeof receipt.stateChangedAt === 'string' &&
    typeof receipt.pendingReason === 'string'
  )
}
function retryAfterMs(value: string | null): number | null {
  if (!value) return null
  const seconds = Number(value)
  if (Number.isFinite(seconds) && seconds >= 0) return seconds * 1000
  const at = Date.parse(value)
  return Number.isFinite(at) ? Math.max(0, at - Date.now()) : null
}
function retryDelayMs(error: unknown, attempt: number): number {
  const jitter = Math.random() * Math.min(10_000, 250 * 2 ** attempt)
  const retryAfter =
    error instanceof ApostraError && error.retryAfter !== null
      ? error.retryAfter * 1000
      : 0
  return Math.max(jitter, retryAfter)
}
function retryable(error: unknown): boolean {
  if (error instanceof ConnectionError) return true
  if (error instanceof ApostraError)
    return error.status === 429 || error.status >= 500
  return (
    error instanceof ProtocolError &&
    (error.status === 429 || error.status >= 500)
  )
}
function wait(ms: number, signal: AbortSignal): Promise<void> {
  return new Promise((resolve, reject) => {
    const cleanup = () => signal.removeEventListener('abort', abort)
    const timer = setTimeout(() => {
      cleanup()
      resolve()
    }, ms)
    const abort = () => {
      clearTimeout(timer)
      cleanup()
      reject(signal.reason)
    }
    signal.addEventListener('abort', abort, { once: true })
    if (signal.aborted) abort()
  })
}
function recoveryForStatus(status: number): Recovery {
  if (status === 408 || status === 429 || status >= 500) return 'transient'
  if (
    status === 400 ||
    status === 401 ||
    status === 403 ||
    status === 404 ||
    status === 409 ||
    status === 422
  )
    return 'correctable'
  return 'terminal'
}
function typedError(
  status: number,
  error: AdcpError,
  requestId: string | null,
): ApostraError {
  const args = [status, error, requestId] as const
  if (status === 401) return new AuthenticationError(...args)
  if (status === 403) return new PermissionError(...args)
  if (status === 404) return new NotFoundError(...args)
  if (status === 409) return new ConflictError(...args)
  if (status === 429) return new RateLimitError(...args)
  if (status === 400 || status === 422) return new ValidationError(...args)
  return new ApostraError(...args)
}

export class Transport {
  readonly #options: ClientOptions
  readonly #url: string
  readonly #fetch: typeof globalThis.fetch
  constructor(options: ClientOptions = {}) {
    const environment = (
      globalThis as typeof globalThis & {
        process?: { env?: Record<string, string | undefined> }
      }
    ).process?.env
    const hasExplicitCredential = [
      options.apiKey,
      options.accessToken,
      options.tokenProvider,
    ].some((value) => value !== undefined)
    const resolvedOptions: ClientOptions = {
      ...options,
      apiKey: hasExplicitCredential
        ? options.apiKey
        : environment?.APOSTRA_API_KEY,
      accountId: options.accountId ?? environment?.APOSTRA_ACCOUNT_ID,
      baseUrl: options.baseUrl ?? environment?.APOSTRA_BASE_URL,
    }
    if (
      [
        resolvedOptions.apiKey,
        resolvedOptions.accessToken,
        resolvedOptions.tokenProvider,
      ].filter((x) => x !== undefined).length !== 1
    )
      throw new TypeError(
        'Supply exactly one of apiKey, accessToken or tokenProvider',
      )
    const maxRetries = resolvedOptions.maxRetries ?? 2
    if (!Number.isInteger(maxRetries) || maxRetries < 0)
      throw new TypeError('maxRetries must be a non-negative integer')
    account(resolvedOptions.accountId)
    const url = new URL(resolvedOptions.baseUrl ?? baseUrl)
    if (
      url.username ||
      url.password ||
      url.search ||
      url.hash ||
      (url.protocol !== 'https:' &&
        !(
          url.protocol === 'http:' &&
          ['localhost', '127.0.0.1', '[::1]'].includes(url.hostname)
        ))
    )
      throw new TypeError(
        'Use an HTTPS base URL (HTTP is allowed only on loopback)',
      )
    this.#url = url.href.replace(/\/$/, '')
    this.#options = { ...resolvedOptions, maxRetries }
    this.#fetch = resolvedOptions.fetch ?? globalThis.fetch
  }
  protected async request<T>(
    operation: OperationId,
    input: object,
    options: RequestOptions = {},
  ): Promise<T> {
    return (await this.perform<T>(operation, input, options)).data
  }
  /** Typed dispatch for CLI reuse, including response headers. */
  async requestDetailed<O extends WriteOperationId>(
    operation: O,
    input: OperationTypes[O]['input'],
    options: WriteRequestOptions,
  ): Promise<ResponseDetails<OperationTypes[O]['result']>>
  async requestDetailed<O extends ReadOperationId>(
    operation: O,
    input: OperationTypes[O]['input'],
    options?: RequestOptions,
  ): Promise<ResponseDetails<OperationTypes[O]['result']>>
  async requestDetailed<O extends OperationId>(
    operation: O,
    input: OperationTypes[O]['input'],
    options: RequestOptions = {},
  ): Promise<ResponseDetails<OperationTypes[O]['result']>> {
    return this.perform(operation, input, options)
  }
  private async perform<T>(
    operation: OperationId,
    input: object,
    options: RequestOptions,
  ): Promise<ResponseDetails<T>> {
    const meta = operations[operation]
    const timeout = options.timeoutMs ?? this.#options.timeoutMs ?? 30_000
    if (!Number.isFinite(timeout) || timeout <= 0)
      throw new TypeError('timeoutMs must be positive')
    const timeoutSignal = AbortSignal.timeout(timeout)
    const signal = options.signal
      ? AbortSignal.any([options.signal, timeoutSignal])
      : timeoutSignal
    const deadline = <T>(promise: Promise<T>): Promise<T> =>
      abortable(promise, signal).catch((error: unknown) => {
        if (timeoutSignal.aborted) throw new TimeoutError(error)
        throw error
      })
    const throwIfAborted = () => {
      try {
        signal.throwIfAborted()
      } catch (error) {
        if (timeoutSignal.aborted) throw new TimeoutError(error)
        throw error
      }
    }
    throwIfAborted()
    const target = account(options.accountId ?? this.#options.accountId)
    const token = await deadline(
      Promise.resolve().then(() => {
        throwIfAborted()
        return (
          this.#options.tokenProvider?.() ??
          this.#options.apiKey ??
          this.#options.accessToken
        )
      }),
    )
    throwIfAborted()
    if (!token || /[\r\n]/.test(token))
      throw new TypeError(
        'Credential source returned an empty or invalid token',
      )
    const headers = new Headers({
      Authorization: `Bearer ${token}`,
      Accept: meta.binary ? 'text/markdown' : 'application/json',
      'User-Agent': `apostra-typescript/${version}`,
    })
    let requestInput = input
    const fields = requestInput as Record<string, unknown>
    const bodyKeyField = 'bodyKeyField' in meta ? meta.bodyKeyField : undefined
    if (target) headers.set('X-SCOPE3-CUSTOMER-ID', target)
    if (meta.idempotencyKey) {
      const key = options.idempotencyKey
      if (typeof key !== 'string' || !/^[\x21-\x7e]{1,255}$/.test(key))
        throw new TypeError(
          'idempotencyKey must be a non-empty printable string',
        )
      headers.set('Idempotency-Key', key)
      if (bodyKeyField) {
        const supplied = fields[bodyKeyField]
        if (supplied !== undefined && supplied !== key)
          throw new TypeError(
            `${bodyKeyField} must match idempotencyKey for ${operation}`,
          )
        requestInput = { ...fields, [bodyKeyField]: key }
      }
    }
    let path: string = meta.path
    const query = new URLSearchParams()
    for (const param of meta.parameters) {
      const value = fields[param.name]
      if (value === undefined) {
        if (param.required) throw new TypeError(`Missing ${param.name}`)
        continue
      }
      if (param.location === 'path')
        path = path.replace(
          `{${param.name}}`,
          encodeURIComponent(String(value)),
        )
      else query.set(param.name, String(value))
    }
    if (meta.body) headers.set('Content-Type', 'application/json')
    const url = `${this.#url}${path}${query.size ? `?${query}` : ''}`
    const retries = this.#options.maxRetries ?? 2
    for (let attempt = 0; ; attempt++) {
      try {
        let response: Response
        try {
          response = await deadline(
            this.#fetch(url, {
              method: meta.method,
              headers,
              body: meta.body ? JSON.stringify(requestInput) : undefined,
              signal,
              redirect: 'error',
            }),
          )
        } catch (error) {
          if (timeoutSignal.aborted) throw new TimeoutError(error)
          if (options.signal?.aborted) throw error
          throw new ConnectionError(error)
        }
        const requestId = response.headers.get('x-request-id')
        // A 202 is an in-flight/uncertain write receipt, never a completed result.
        if (response.status === 202) {
          let receiptEnvelope: unknown
          try {
            receiptEnvelope = await deadline(response.json())
          } catch (error) {
            throwIfAborted()
            if (!(error instanceof SyntaxError)) throw error
            throw new ProtocolError(response.status, requestId)
          }
          if (!inFlightReceipt(receiptEnvelope))
            throw new ProtocolError(response.status, requestId)
          throw new InFlightReceiptError(
            requestId,
            retryAfterMs(response.headers.get('retry-after')),
            receiptEnvelope.data.receipt,
          )
        }
        if (meta.binary && response.ok)
          return {
            data: new Uint8Array(await deadline(response.arrayBuffer())) as T,
            status: response.status,
            headers: response.headers,
            requestId,
          }
        let envelope: unknown
        try {
          envelope = await deadline(response.json())
        } catch (error) {
          throwIfAborted()
          if (!(error instanceof SyntaxError)) throw error
          throw new ProtocolError(response.status, requestId)
        }
        if (!response.ok) {
          if (
            record(envelope) &&
            envelope.data === null &&
            errorModel(envelope.error)
          )
            throw typedError(response.status, envelope.error, requestId)
          throw new ProtocolError(response.status, requestId)
        }
        if (
          !record(envelope) ||
          envelope.error !== null ||
          !('data' in envelope)
        )
          throw new ProtocolError(response.status, requestId)
        return {
          data: envelope.data as T,
          status: response.status,
          headers: response.headers,
          requestId,
        }
      } catch (error) {
        if (attempt >= retries || !retryable(error)) throw error
        await deadline(wait(retryDelayMs(error, attempt), signal))
      }
    }
  }
}

/** Re-invoke a caller-owned keyed write until an in-flight receipt settles. */
export async function settle<T>(
  run: (signal: AbortSignal) => Promise<T>,
  options: { signal?: AbortSignal; timeoutMs?: number } = {},
): Promise<T> {
  const timeout = options.timeoutMs ?? 30_000
  if (!Number.isFinite(timeout) || timeout <= 0)
    throw new TypeError('timeoutMs must be positive')
  const timeoutSignal = AbortSignal.timeout(timeout)
  const signal = options.signal
    ? AbortSignal.any([options.signal, timeoutSignal])
    : timeoutSignal
  while (true) {
    signal.throwIfAborted()
    try {
      return await abortable(run(signal), signal)
    } catch (error) {
      if (!(error instanceof InFlightReceiptError)) throw error
      await wait(error.retryAfterMs ?? 1000, signal)
    }
  }
}

/** Visit pages while preserving the exact caller-owned query and cursor rules. */
export async function* paginate<T>(
  read: (cursor: string | undefined, signal?: AbortSignal) => Promise<T>,
  next: (page: T) => string | null | undefined,
  signal?: AbortSignal,
): AsyncGenerator<T> {
  let cursor: string | undefined
  const seen = new Set<string>()
  do {
    signal?.throwIfAborted()
    const page = await (signal
      ? abortable(read(cursor, signal), signal)
      : read(cursor))
    signal?.throwIfAborted()
    const nextCursor = next(page) ?? undefined
    if (nextCursor && seen.has(nextCursor)) throw new ProtocolError(200, null)
    if (nextCursor) seen.add(nextCursor)
    yield page
    cursor = nextCursor
  } while (cursor)
}
/** The caller supplies the contract's status predicate and keeps idempotency keys stable. */
export async function poll<T>(
  read: (signal: AbortSignal) => Promise<T>,
  complete: (result: T) => boolean,
  options: { signal: AbortSignal; intervalMs?: number },
): Promise<T> {
  const interval = options.intervalMs ?? 1000
  if (!Number.isFinite(interval) || interval <= 0)
    throw new TypeError('intervalMs must be positive')
  while (true) {
    options.signal.throwIfAborted()
    const result = await abortable(read(options.signal), options.signal)
    options.signal.throwIfAborted()
    if (complete(result)) return result
    await new Promise<void>((resolve, reject) => {
      const cleanup = () => options.signal.removeEventListener('abort', abort)
      const timer = setTimeout(() => {
        cleanup()
        resolve()
      }, interval)
      const abort = () => {
        clearTimeout(timer)
        cleanup()
        reject(options.signal.reason)
      }
      options.signal.addEventListener('abort', abort, { once: true })
      if (options.signal.aborted) abort()
    })
  }
}

function handoffResume(value: unknown): value is HumanHandoff['resume'] {
  return (
    record(value) &&
    value.kind === 'manual' &&
    value.reason ===
      'This Page has no durable completion receipt. Read the affected object before continuing; opening or closing the browser is not completion.'
  )
}

/** Return an actionable human handoff, or null when no supported URL is present. */
export function getHandoff(
  result: { humanHandoff?: unknown } | null | undefined,
): HumanHandoff | null {
  const handoff = result?.humanHandoff
  if (
    !record(handoff) ||
    handoff.kind !== 'human_action_required' ||
    typeof handoff.url !== 'string' ||
    typeof handoff.expiresAt !== 'string' ||
    !handoffResume(handoff.resume)
  )
    return null
  return {
    kind: 'human_action_required',
    url: handoff.url,
    expiresAt: handoff.expiresAt,
    resume: handoff.resume,
  }
}

/** Pass only a handoff returned by getHandoff; headless calls simply return its URL. */
export async function openHandoff(
  handoff: HumanHandoff | string,
  opener?: (url: string) => void | Promise<void>,
): Promise<string> {
  const url = typeof handoff === 'string' ? handoff : handoff.url
  const parsed = new URL(url)
  if (parsed.protocol !== 'https:' || parsed.username || parsed.password)
    throw new TypeError('Expected an HTTPS handoff URL')
  await opener?.(url)
  return url
}

function abortable<T>(promise: Promise<T>, signal: AbortSignal): Promise<T> {
  return new Promise((resolve, reject) => {
    const cleanup = () => signal.removeEventListener('abort', abort)
    const abort = () => {
      cleanup()
      reject(signal.reason)
    }
    signal.addEventListener('abort', abort, { once: true })
    promise.then(
      (value) => {
        cleanup()
        resolve(value)
      },
      (error) => {
        cleanup()
        reject(error)
      },
    )
    if (signal.aborted) abort()
  })
}
