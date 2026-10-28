import {
  ApostraError,
  AuthenticationError,
  ConflictError,
  ConnectionError,
  InFlightReceiptError,
  NotFoundError,
  PermissionError,
  ProtocolError,
  TimeoutError,
  ValidationError,
} from '@apostra/sdk'
import { CommanderError } from 'commander'

/** Version of the `--json` envelope. Raised only for a breaking change to it. */
export const schemaVersion = 1

/** Process exit codes. Documented in `mintlify/v3/cli.mdx`; never renumber. */
export const exitCodes = {
  ok: 0,
  serverFailure: 1,
  invalidInput: 2,
  authentication: 3,
  permission: 4,
  conflict: 5,
  unavailable: 6,
} as const
export type ExitCode = (typeof exitCodes)[keyof typeof exitCodes]

export type ErrorDetails = {
  status?: number
  requestId?: string | null
  recovery?: string
  retryAfter?: number | null
  receipt?: unknown
}

/** A failure the CLI reports in the envelope and as its exit code. */
export class CliError extends Error {
  constructor(
    message: string,
    readonly code: string,
    readonly exitCode: ExitCode,
    readonly details: ErrorDetails = {},
  ) {
    super(message)
    this.name = 'CliError'
  }
}

export const invalidInput = (message: string, code = 'INVALID_INPUT') =>
  new CliError(message, code, exitCodes.invalidInput)

export type Meta = Record<string, unknown>

export function successEnvelope(data: unknown, meta?: Meta) {
  return { schemaVersion, ok: true as const, data, ...(meta && { meta }) }
}

export function errorEnvelope(error: CliError) {
  return {
    schemaVersion,
    ok: false as const,
    error: {
      code: error.code,
      message: error.message,
      exitCode: error.exitCode,
      ...error.details,
    },
  }
}

/** Server error codes that mean the capability is not offered, whatever the status. */
const unavailableCodes = new Set([
  'FEATURE_NOT_ENABLED',
  'NOT_IMPLEMENTED',
  'UNSUPPORTED_OPERATION',
  'CAPABILITY_UNAVAILABLE',
])

function apiError(error: ApostraError): CliError {
  const details = {
    status: error.status,
    requestId: error.requestId,
    recovery: error.recovery,
    retryAfter: error.retryAfter,
  }
  const message = error.error.message || error.message
  const build = (exitCode: ExitCode) =>
    new CliError(message, error.code, exitCode, details)
  if (unavailableCodes.has(error.code) || error.status === 501)
    return build(exitCodes.unavailable)
  if (error instanceof AuthenticationError)
    return build(exitCodes.authentication)
  if (
    error instanceof PermissionError ||
    error.code === 'ACCOUNT_NOT_REACHABLE'
  )
    return build(exitCodes.permission)
  if (error instanceof ConflictError) return build(exitCodes.conflict)
  if (error instanceof ValidationError || error instanceof NotFoundError)
    return build(exitCodes.invalidInput)
  return build(exitCodes.serverFailure)
}

/** Classify anything an action can throw into one error with one exit code. */
export function toCliError(error: unknown): CliError {
  if (error instanceof CliError) return error
  if (error instanceof ApostraError) return apiError(error)
  if (error instanceof InFlightReceiptError)
    return new CliError(
      'The write was accepted but has not settled. Repeat the same call with the same --idempotency-key to read its outcome.',
      'IN_FLIGHT',
      exitCodes.conflict,
      {
        status: error.status,
        requestId: error.requestId,
        recovery: 'transient',
        retryAfter:
          error.retryAfterMs === null ? null : error.retryAfterMs / 1000,
        receipt: error.receipt,
      },
    )
  if (error instanceof TimeoutError || error instanceof ConnectionError)
    return new CliError(error.message, error.code, exitCodes.serverFailure, {
      recovery: error.recovery,
    })
  if (error instanceof ProtocolError)
    return new CliError(
      error.message,
      'PROTOCOL_ERROR',
      exitCodes.serverFailure,
      { status: error.status, requestId: error.requestId },
    )
  if (error instanceof CommanderError)
    return invalidInput(error.message.replace(/^error: /, ''))
  return new CliError(
    error instanceof Error ? error.message : String(error),
    'ERROR',
    exitCodes.serverFailure,
  )
}
