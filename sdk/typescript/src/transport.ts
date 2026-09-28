import type { OperationTypes } from './generated/client.js'
import {
  baseUrl,
  type OperationId,
  operations,
  version,
} from './generated/metadata.js'
import type { AdcpError } from './generated/types.gen.js'

export type TokenProvider = () => string | Promise<string>
export type ClientOptions = {
  /** Supply exactly one credential source. Providers own acquisition/refresh. */
  apiKey?: string
  accessToken?: string
  tokenProvider?: TokenProvider
  accountId?: string
  baseUrl?: string
  fetch?: typeof globalThis.fetch
  timeoutMs?: number
}
export type RequestOptions = {
  accountId?: string
  signal?: AbortSignal
  timeoutMs?: number
}
export type ResponseDetails<T> = {
  data: T
  status: number
  headers: Headers
  requestId: string | null
}
export class ApostraError extends Error {
  constructor(
    readonly status: number,
    readonly error: AdcpError,
    readonly requestId: string | null,
  ) {
    // Server messages/details are available explicitly. Do not include them in
    // the default exception string: they can contain reflected request secrets.
    super(`Apostra request failed (${status})`)
    this.name = 'ApostraError'
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
 * This exposes only stable transport facts until V3 publishes the receipt
 * schema and read-only receipt endpoint. Callers retain the original
 * operation-specific idempotency key; the SDK never makes another request or
 * creates a replacement key.
 */
export class InFlightReceiptError extends Error {
  readonly status = 202
  constructor(
    readonly requestId: string | null,
    readonly retryAfterMs: number | null,
  ) {
    super('Apostra write is still in flight')
    this.name = 'InFlightReceiptError'
  }
}
export class UnsupportedCapabilityError extends Error {}
const account = (value: string | undefined) => {
  if (value !== undefined && !/^[1-9][0-9]*$/.test(value))
    throw new TypeError('accountId must be a positive integer string')
  return value
}
function record(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}
function errorModel(value: unknown): value is AdcpError {
  return (
    record(value) &&
    typeof value.code === 'string' &&
    typeof value.message === 'string'
  )
}
function retryAfterMs(value: string | null): number | null {
  if (!value) return null
  const seconds = Number(value)
  if (Number.isFinite(seconds) && seconds >= 0) return seconds * 1000
  const at = Date.parse(value)
  return Number.isFinite(at) ? Math.max(0, at - Date.now()) : null
}

export class Transport {
  readonly #options: ClientOptions
  readonly #url: string
  readonly #fetch: typeof globalThis.fetch
  constructor(options: ClientOptions) {
    if (
      [options.apiKey, options.accessToken, options.tokenProvider].filter(
        (x) => x !== undefined,
      ).length !== 1
    )
      throw new TypeError(
        'Supply exactly one of apiKey, accessToken or tokenProvider',
      )
    account(options.accountId)
    const url = new URL(options.baseUrl ?? baseUrl)
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
    this.#options = { ...options }
    this.#fetch = options.fetch ?? globalThis.fetch
  }
  protected async request<T>(
    operation: OperationId,
    input: object,
    options: RequestOptions = {},
  ): Promise<T> {
    return (await this.perform<T>(operation, input, options)).data
  }
  /** Typed dispatch for CLI reuse, including response headers. */
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
    const signal = options.signal
      ? AbortSignal.any([options.signal, AbortSignal.timeout(timeout)])
      : AbortSignal.timeout(timeout)
    signal.throwIfAborted()
    const target = account(options.accountId ?? this.#options.accountId)
    const token = await abortable(
      Promise.resolve().then(() => {
        signal.throwIfAborted()
        return (
          this.#options.tokenProvider?.() ??
          this.#options.apiKey ??
          this.#options.accessToken
        )
      }),
      signal,
    )
    signal.throwIfAborted()
    if (!token || /[\r\n]/.test(token))
      throw new TypeError(
        'Credential source returned an empty or invalid token',
      )
    const headers = new Headers({
      Authorization: `Bearer ${token}`,
      Accept: meta.binary ? 'text/markdown' : 'application/json',
      'User-Agent': `apostra-typescript/${version}`,
    })
    if (target) headers.set('X-SCOPE3-CUSTOMER-ID', target)
    let path: string = meta.path
    const fields = input as Record<string, unknown>
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
    // Never replay mutations or follow redirects with bearer credentials.
    const response = await abortable(
      this.#fetch(`${this.#url}${path}${query.size ? `?${query}` : ''}`, {
        method: meta.method,
        headers,
        body: meta.body ? JSON.stringify(input) : undefined,
        signal,
        redirect: 'error',
      }),
      signal,
    )
    const requestId = response.headers.get('x-request-id')
    // A 202 is an in-flight/uncertain write receipt, never a completed result.
    // Do not consume an unpublished receipt body as generated operation data.
    if (response.status === 202)
      throw new InFlightReceiptError(
        requestId,
        retryAfterMs(response.headers.get('retry-after')),
      )
    if (meta.binary && response.ok)
      return {
        data: new Uint8Array(
          await abortable(response.arrayBuffer(), signal),
        ) as T,
        status: response.status,
        headers: response.headers,
        requestId,
      }
    let envelope: unknown
    try {
      envelope = await abortable(response.json(), signal)
    } catch (error) {
      signal.throwIfAborted()
      if (!(error instanceof SyntaxError)) throw error
      throw new ProtocolError(response.status, requestId)
    }
    if (!response.ok) {
      if (
        record(envelope) &&
        envelope.data === null &&
        errorModel(envelope.error)
      )
        throw new ApostraError(response.status, envelope.error, requestId)
      throw new ProtocolError(response.status, requestId)
    }
    if (!record(envelope) || envelope.error !== null || !('data' in envelope))
      throw new ProtocolError(response.status, requestId)
    return {
      data: envelope.data as T,
      status: response.status,
      headers: response.headers,
      requestId,
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

/** Pass only a URL returned by an operation; headless calls simply return it. */
export async function openHandoff(
  url: string,
  opener?: (url: string) => void | Promise<void>,
): Promise<string> {
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
