import type { Apostra, GetResult } from './generated/client.js'
import { InFlightReceiptError, openHandoff, poll } from './transport.js'

/**
 * One shape for the two ways V3 says "a person must act in a browser":
 *
 * - a `humanHandoff` field: an account-bound, expiring link with a `resume`
 *   rule saying how to tell the step is done;
 * - an `action: 'approval_required'` result (the web approval contract): the
 *   request is recorded and runs only after a signed-in person approves it.
 *   Repeating the original call with the same idempotency key reports the
 *   outcome.
 *
 * Nothing here opens a browser unless the caller asks, and a browser opening
 * or closing never counts as completion: only a fresh server read does.
 */

export type ApprovalState =
  | 'pending'
  | 'executing'
  | 'succeeded'
  | 'failed'
  | 'rejected'
  | 'expired'
export type HandoffResume =
  | { kind: 'approval'; approvalId: string; state: ApprovalState }
  | {
      kind: 'connection'
      targetKind: string
      targetId: string
      intendedConnectionId: string | null
      correlationId: string
    }
  | { kind: 'manual'; reason: string }
type WaitTiming = {
  /** Stop waiting after this long. A person can take a while, so there is no default. */
  timeoutMs: number
  /** Time between fresh reads. Defaults to 5 seconds. */
  intervalMs?: number
  signal?: AbortSignal
}
export type WaitForCompletionOptions<R> = WaitTiming & {
  /**
   * The fresh server read. For an approval, repeat the original call with the
   * same body and the same idempotency key.
   */
  read: (signal: AbortSignal) => Promise<R>
  /**
   * Whether a read shows the step is done. Required except for an approval,
   * where it defaults to "the result is no longer a pending or executing
   * approval".
   */
  until?: (result: R) => boolean
}
export type WaitForConnectionOptions = WaitTiming & {
  /** Reads the connection with `get` in the handoff's account. */
  client: Pick<Apostra, 'get'>
  until: (result: GetResult) => boolean
}
export type Handoff = {
  readonly kind: 'human_action_required' | 'approval_required'
  /** Sensitive: show it to the person, but do not log or post it. */
  readonly url: string
  /** The account the step is bound to. An approval carries no account name. */
  readonly account: { readonly id: string; readonly name: string | null }
  /** The handoff action, or the approval kind such as `iu_plan.accept`. */
  readonly action: string
  readonly expiresAt: string
  readonly resume: HandoffResume
  /** Opens only through the caller's opener; without one it returns the URL. */
  open(opener?: (url: string) => void | Promise<void>): Promise<string>
  waitForCompletion<R>(options: WaitForCompletionOptions<R>): Promise<R>
  waitForCompletion(options: WaitForConnectionOptions): Promise<GetResult>
}
type HandoffFacts = Omit<Handoff, 'open' | 'waitForCompletion'>

const APPROVAL_STATES: readonly string[] = [
  'pending',
  'executing',
  'succeeded',
  'failed',
  'rejected',
  'expired',
] satisfies ApprovalState[]

function record(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}
function text(value: unknown): value is string {
  return typeof value === 'string' && value.length > 0
}
function approvalState(value: unknown): value is ApprovalState {
  return typeof value === 'string' && APPROVAL_STATES.includes(value)
}
function approvalWaiting(result: unknown): boolean {
  return (
    record(result) &&
    result.action === 'approval_required' &&
    record(result.approval) &&
    (result.approval.state === 'pending' ||
      result.approval.state === 'executing')
  )
}

function handoffResume(value: unknown): HandoffResume | null {
  if (!record(value)) return null
  const { kind, reason, targetKind, targetId, correlationId } = value
  const intendedConnectionId = value.intendedConnectionId
  if (kind === 'manual' && text(reason)) return { kind, reason }
  if (
    kind === 'connection' &&
    text(targetKind) &&
    text(targetId) &&
    (intendedConnectionId === null || text(intendedConnectionId)) &&
    text(correlationId)
  )
    return {
      kind,
      targetKind,
      targetId,
      intendedConnectionId,
      correlationId,
    }
  return null
}
function humanHandoffFacts(result: unknown): HandoffFacts | null {
  if (!record(result) || !record(result.humanHandoff)) return null
  const { kind, url, expiresAt, action, account } = result.humanHandoff
  const resume = handoffResume(result.humanHandoff.resume)
  if (
    kind !== 'human_action_required' ||
    !text(url) ||
    !text(expiresAt) ||
    !text(action) ||
    !record(account) ||
    typeof account.id !== 'number' ||
    !Number.isSafeInteger(account.id) ||
    account.id <= 0 ||
    typeof account.name !== 'string' ||
    !resume
  )
    return null
  return {
    kind,
    url,
    account: { id: String(account.id), name: account.name },
    action,
    expiresAt,
    resume,
  }
}
function approvalFacts(result: unknown): HandoffFacts | null {
  if (
    !record(result) ||
    result.action !== 'approval_required' ||
    !record(result.approval)
  )
    return null
  const { id, kind, state, url, expiresAt, targetCustomerId } = result.approval
  if (
    !text(id) ||
    !text(kind) ||
    !approvalState(state) ||
    !text(url) ||
    !text(expiresAt) ||
    !text(targetCustomerId)
  )
    return null
  return {
    kind: 'approval_required',
    url,
    account: { id: targetCustomerId, name: null },
    action: kind,
    expiresAt,
    resume: { kind: 'approval', approvalId: id, state },
  }
}

async function waitForCompletion<R>(
  facts: HandoffFacts,
  options: WaitForCompletionOptions<R> | WaitForConnectionOptions,
): Promise<unknown> {
  const { timeoutMs, intervalMs = 5000 } = options
  if (!Number.isFinite(timeoutMs) || timeoutMs <= 0)
    throw new TypeError('timeoutMs must be positive')
  let read: (signal: AbortSignal) => Promise<unknown>
  let until: (result: unknown) => boolean
  if ('client' in options) {
    const { resume } = facts
    if (resume.kind !== 'connection' || resume.intendedConnectionId === null)
      throw new TypeError(
        'client reads only a connection handoff that names its connection; pass read instead',
      )
    const id = resume.intendedConnectionId
    read = (signal) =>
      options.client.get(
        { kind: 'connection', id },
        { accountId: facts.account.id, signal },
      )
    until = options.until as (result: unknown) => boolean
  } else {
    read = options.read
    if (options.until) until = options.until as (result: unknown) => boolean
    else if (facts.resume.kind === 'approval')
      until = (result) => !approvalWaiting(result)
    else
      throw new TypeError(
        'Pass until: only an approval has a completion rule the SDK knows',
      )
  }
  const timeout = AbortSignal.timeout(timeoutMs)
  const signal = options.signal
    ? AbortSignal.any([options.signal, timeout])
    : timeout
  // A keyed write that is still in flight answers 202; that is not an answer
  // about the person's step, so keep reading.
  const settled = await poll(
    async (readSignal) => {
      try {
        return { value: await read(readSignal) }
      } catch (error) {
        if (error instanceof InFlightReceiptError) return null
        throw error
      }
    },
    (fresh) => fresh !== null && until(fresh.value),
    { signal, intervalMs },
  )
  // poll returns only a read that met the predicate, which excludes null.
  return (settled as { value: unknown }).value
}

/**
 * Recognise a human handoff or a web approval in any operation's result, or
 * return null when the result asks nothing of a person.
 */
export function findHandoff(result: unknown): Handoff | null {
  const facts = humanHandoffFacts(result) ?? approvalFacts(result)
  if (!facts) return null
  return {
    ...facts,
    open: (opener) => openHandoff(facts.url, opener),
    waitForCompletion: ((
      options: WaitForCompletionOptions<unknown> | WaitForConnectionOptions,
    ) => waitForCompletion(facts, options)) as Handoff['waitForCompletion'],
  }
}
