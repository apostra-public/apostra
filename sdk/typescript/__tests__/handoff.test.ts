import { describe, expect, it, vi } from 'vitest'

import {
  type Apostra,
  findHandoff,
  type Handoff,
  InFlightReceiptError,
} from '../src/index.js'

const URL = 'https://app.example.com/handoff/abc'
const EXPIRES = '2026-11-10T00:00:00.000Z'

const manualResult = (overrides: Record<string, unknown> = {}) => ({
  humanHandoff: {
    kind: 'human_action_required',
    account: { id: 42, name: 'Acme' },
    action: 'connect_provider',
    url: URL,
    expiresAt: EXPIRES,
    resume: { kind: 'manual', reason: 'Finish setup in the browser' },
    ...overrides,
  },
})
const connectionResume = (intendedConnectionId: string | null = 'conn_1') => ({
  kind: 'connection',
  targetKind: 'gam',
  targetId: 'target_1',
  intendedConnectionId,
  correlationId: 'corr_1',
})
const approvalResult = (
  state = 'pending',
  overrides: Record<string, unknown> = {},
) => ({
  action: 'approval_required',
  approval: {
    id: 'appr_1',
    kind: 'iu_plan.accept',
    state,
    url: URL,
    expiresAt: EXPIRES,
    targetCustomerId: '77',
    ...overrides,
  },
})
const handoffOf = (result: unknown): Handoff => {
  const handoff = findHandoff(result)
  if (!handoff) throw new Error('expected a handoff')
  return handoff
}
const receipt = {
  id: '4e8d0bf9-419a-4eb4-a6ee-3438f7bc89a1',
  operation: 'save_ask',
  state: 'running' as const,
  stateVersion: 1,
  stateChangedAt: '2026-09-28T10:00:00.000Z',
  pendingReason: 'The write is still being processed.',
}

describe('findHandoff recognition', () => {
  it('normalises a manual humanHandoff', () => {
    const handoff = handoffOf(manualResult())
    expect(handoff.kind).toBe('human_action_required')
    expect(handoff.url).toBe(URL)
    expect(handoff.account).toEqual({ id: '42', name: 'Acme' })
    expect(handoff.action).toBe('connect_provider')
    expect(handoff.expiresAt).toBe(EXPIRES)
    expect(handoff.resume).toEqual({
      kind: 'manual',
      reason: 'Finish setup in the browser',
    })
  })
  it('normalises a connection humanHandoff with and without an intended connection', () => {
    expect(
      handoffOf(manualResult({ resume: connectionResume() })).resume,
    ).toEqual(connectionResume())
    expect(
      handoffOf(manualResult({ resume: connectionResume(null) })).resume,
    ).toEqual(connectionResume(null))
  })
  it('normalises an approval_required result', () => {
    const handoff = handoffOf(approvalResult('executing'))
    expect(handoff.kind).toBe('approval_required')
    expect(handoff.url).toBe(URL)
    expect(handoff.account).toEqual({ id: '77', name: null })
    expect(handoff.action).toBe('iu_plan.accept')
    expect(handoff.expiresAt).toBe(EXPIRES)
    expect(handoff.resume).toEqual({
      kind: 'approval',
      approvalId: 'appr_1',
      state: 'executing',
    })
  })
  it.each([
    'pending',
    'executing',
    'succeeded',
    'failed',
    'rejected',
    'expired',
  ])('accepts the %s approval state', (state) => {
    expect(handoffOf(approvalResult(state)).resume).toMatchObject({ state })
  })

  it.each([
    ['null', null],
    ['undefined', undefined],
    ['a string', 'text'],
    ['an array', []],
    ['an empty object', {}],
    ['a plain result', { action: 'saved', id: 1 }],
  ])('returns null for %s', (_name, value) => {
    expect(findHandoff(value)).toBeNull()
  })
  it('returns null for human_action_unavailable', () => {
    expect(
      findHandoff(manualResult({ kind: 'human_action_unavailable' })),
    ).toBeNull()
  })
  it.each([
    ['an empty url', { url: '' }],
    ['a missing url', { url: undefined }],
    ['a missing expiresAt', { expiresAt: undefined }],
    ['a missing action', { action: undefined }],
    ['a missing account', { account: undefined }],
    ['a zero account id', { account: { id: 0, name: 'Acme' } }],
    ['a negative account id', { account: { id: -1, name: 'Acme' } }],
    ['a fractional account id', { account: { id: 1.5, name: 'Acme' } }],
    ['a string account id', { account: { id: '42', name: 'Acme' } }],
    ['a missing account name', { account: { id: 42 } }],
    ['a missing resume', { resume: undefined }],
    ['an unknown resume kind', { resume: { kind: 'poll' } }],
    ['a manual resume without a reason', { resume: { kind: 'manual' } }],
    [
      'a connection resume without a correlation id',
      { resume: { ...connectionResume(), correlationId: undefined } },
    ],
    [
      'a connection resume with a non-string connection id',
      { resume: { ...connectionResume(), intendedConnectionId: 5 } },
    ],
  ])('returns null for a humanHandoff with %s', (_name, overrides) => {
    expect(findHandoff(manualResult(overrides))).toBeNull()
  })
  it('returns null for an unknown approval state', () => {
    expect(findHandoff(approvalResult('cancelled'))).toBeNull()
  })
  it.each([
    ['id', { id: '' }],
    ['kind', { kind: undefined }],
    ['url', { url: undefined }],
    ['expiresAt', { expiresAt: undefined }],
    ['targetCustomerId', { targetCustomerId: undefined }],
  ])('returns null for an approval missing %s', (_name, overrides) => {
    expect(findHandoff(approvalResult('pending', overrides))).toBeNull()
  })
  it('returns null for approval_required without an approval object', () => {
    expect(findHandoff({ action: 'approval_required' })).toBeNull()
  })
})

describe('Handoff.open', () => {
  it('returns the URL without calling anything when headless', async () => {
    await expect(handoffOf(manualResult()).open()).resolves.toBe(URL)
  })
  it('calls the opener with the URL and returns it', async () => {
    const opener = vi.fn()
    await expect(handoffOf(manualResult()).open(opener)).resolves.toBe(URL)
    expect(opener).toHaveBeenCalledExactlyOnceWith(URL)
  })
  it('rejects a non-HTTPS URL and never calls the opener', async () => {
    const opener = vi.fn()
    const handoff = handoffOf(
      manualResult({ url: 'http://app.example.com/handoff' }),
    )
    await expect(handoff.open(opener)).rejects.toThrow()
    expect(opener).not.toHaveBeenCalled()
  })
})

describe('Handoff.waitForCompletion with read', () => {
  it('polls an approval until it leaves pending and executing, returning the final read', async () => {
    const final = { saved: true }
    const read = vi
      .fn()
      .mockResolvedValueOnce(approvalResult('pending'))
      .mockResolvedValueOnce(approvalResult('executing'))
      .mockResolvedValueOnce(final)
    const result = await handoffOf(approvalResult()).waitForCompletion({
      read,
      timeoutMs: 1000,
      intervalMs: 1,
    })
    expect(result).toBe(final)
    expect(read).toHaveBeenCalledTimes(3)
  })
  it('treats a terminal rejected approval_required read as done', async () => {
    const rejected = approvalResult('rejected')
    const read = vi
      .fn()
      .mockResolvedValueOnce(approvalResult('pending'))
      .mockResolvedValueOnce(rejected)
    const result = await handoffOf(approvalResult()).waitForCompletion({
      read,
      timeoutMs: 1000,
      intervalMs: 1,
    })
    expect(result).toBe(rejected)
    expect(read).toHaveBeenCalledTimes(2)
  })
  it('reads once even when the handoff already looks final', async () => {
    const fresh = approvalResult('succeeded')
    const read = vi.fn().mockResolvedValue(fresh)
    const result = await handoffOf(
      approvalResult('succeeded'),
    ).waitForCompletion({ read, timeoutMs: 1000, intervalMs: 1 })
    expect(result).toBe(fresh)
    expect(read).toHaveBeenCalledTimes(1)
  })
  it('passes an abort signal to the read', async () => {
    const read = vi.fn().mockResolvedValue({})
    await handoffOf(approvalResult()).waitForCompletion({
      read,
      timeoutMs: 1000,
      intervalMs: 1,
    })
    expect(read.mock.calls[0]?.[0]).toBeInstanceOf(AbortSignal)
  })
  it('uses a caller until over the approval default', async () => {
    const read = vi
      .fn()
      .mockResolvedValueOnce({ n: 1 })
      .mockResolvedValueOnce({ n: 2 })
    const result = await handoffOf(approvalResult()).waitForCompletion({
      read,
      until: (value: { n: number }) => value.n === 2,
      timeoutMs: 1000,
      intervalMs: 1,
    })
    expect(result).toEqual({ n: 2 })
  })
  it('requires until for a manual handoff', async () => {
    const read = vi.fn()
    await expect(
      handoffOf(manualResult()).waitForCompletion({ read, timeoutMs: 1000 }),
    ).rejects.toThrow(TypeError)
    expect(read).not.toHaveBeenCalled()
  })
  it('waits on a manual handoff when until is given', async () => {
    const read = vi
      .fn()
      .mockResolvedValueOnce({ done: false })
      .mockResolvedValueOnce({ done: true })
    const result = await handoffOf(manualResult()).waitForCompletion({
      read,
      until: (value: { done: boolean }) => value.done,
      timeoutMs: 1000,
      intervalMs: 1,
    })
    expect(result).toEqual({ done: true })
  })
  it('retries an in-flight receipt without ending the wait', async () => {
    const final = { saved: true }
    const read = vi
      .fn()
      .mockRejectedValueOnce(new InFlightReceiptError('r1', 1, receipt))
      .mockResolvedValueOnce(final)
    const result = await handoffOf(approvalResult()).waitForCompletion({
      read,
      timeoutMs: 1000,
      intervalMs: 1,
    })
    expect(result).toBe(final)
    expect(read).toHaveBeenCalledTimes(2)
  })
  it('propagates any other read error', async () => {
    const failure = new Error('upstream exploded')
    const read = vi.fn().mockRejectedValue(failure)
    await expect(
      handoffOf(approvalResult()).waitForCompletion({
        read,
        timeoutMs: 1000,
        intervalMs: 1,
      }),
    ).rejects.toBe(failure)
    expect(read).toHaveBeenCalledTimes(1)
  })
  it('rejects with a TimeoutError when the step never completes', async () => {
    const read = vi.fn().mockResolvedValue(approvalResult('pending'))
    await expect(
      handoffOf(approvalResult()).waitForCompletion({
        read,
        timeoutMs: 30,
        intervalMs: 1,
      }),
    ).rejects.toMatchObject({ name: 'TimeoutError' })
  })
  it('rejects when the caller aborts', async () => {
    const controller = new AbortController()
    const read = vi.fn().mockImplementation(async () => {
      controller.abort(new Error('caller gave up'))
      return approvalResult('pending')
    })
    await expect(
      handoffOf(approvalResult()).waitForCompletion({
        read,
        timeoutMs: 5000,
        intervalMs: 1,
        signal: controller.signal,
      }),
    ).rejects.toThrow('caller gave up')
  })
  it('rejects without reading when the caller already aborted', async () => {
    const read = vi.fn()
    await expect(
      handoffOf(approvalResult()).waitForCompletion({
        read,
        timeoutMs: 5000,
        intervalMs: 1,
        signal: AbortSignal.abort(new Error('already aborted')),
      }),
    ).rejects.toThrow('already aborted')
    expect(read).not.toHaveBeenCalled()
  })
  it.each([0, -1, Number.NaN, Number.POSITIVE_INFINITY])(
    'rejects timeoutMs %s with a TypeError',
    async (timeoutMs) => {
      const read = vi.fn()
      await expect(
        handoffOf(approvalResult()).waitForCompletion({ read, timeoutMs }),
      ).rejects.toThrow(TypeError)
      expect(read).not.toHaveBeenCalled()
    },
  )
  it.each([0, -1, Number.NaN])(
    'rejects intervalMs %s with a TypeError',
    async (intervalMs) => {
      const read = vi.fn().mockResolvedValue({})
      await expect(
        handoffOf(approvalResult()).waitForCompletion({
          read,
          timeoutMs: 1000,
          intervalMs,
        }),
      ).rejects.toThrow(TypeError)
    },
  )
})

describe('Handoff.waitForCompletion with client', () => {
  const connectionHandoff = (intendedConnectionId: string | null = 'conn_1') =>
    handoffOf(manualResult({ resume: connectionResume(intendedConnectionId) }))

  it('reads the named connection in the handoff account until done', async () => {
    const get = vi
      .fn()
      .mockResolvedValueOnce({ status: 'pending' })
      .mockResolvedValueOnce({ status: 'connected' })
    const client = { get } as unknown as Pick<Apostra, 'get'>
    const result = await connectionHandoff().waitForCompletion({
      client,
      until: (value) =>
        (value as unknown as { status: string }).status === 'connected',
      timeoutMs: 1000,
      intervalMs: 1,
    })
    expect(result).toEqual({ status: 'connected' })
    expect(get).toHaveBeenCalledTimes(2)
    expect(get.mock.calls[0]?.[0]).toEqual({ kind: 'connection', id: 'conn_1' })
    expect(get.mock.calls[0]?.[1]).toMatchObject({ accountId: '42' })
    expect(get.mock.calls[0]?.[1].signal).toBeInstanceOf(AbortSignal)
  })
  it('throws a TypeError when the connection handoff names no connection', async () => {
    const get = vi.fn()
    await expect(
      connectionHandoff(null).waitForCompletion({
        client: { get } as unknown as Pick<Apostra, 'get'>,
        until: () => true,
        timeoutMs: 1000,
      }),
    ).rejects.toThrow(TypeError)
    expect(get).not.toHaveBeenCalled()
  })
  it('throws a TypeError when the handoff is not a connection handoff', async () => {
    const get = vi.fn()
    await expect(
      handoffOf(manualResult()).waitForCompletion({
        client: { get } as unknown as Pick<Apostra, 'get'>,
        until: () => true,
        timeoutMs: 1000,
      }),
    ).rejects.toThrow(TypeError)
    await expect(
      handoffOf(approvalResult()).waitForCompletion({
        client: { get } as unknown as Pick<Apostra, 'get'>,
        until: () => true,
        timeoutMs: 1000,
      }),
    ).rejects.toThrow(TypeError)
    expect(get).not.toHaveBeenCalled()
  })
})
