// @vitest-environment jsdom

import type { Transport } from '@modelcontextprotocol/sdk/shared/transport.js'
import { afterEach, describe, expect, it, vi } from 'vitest'

const mocks = vi.hoisted(() => {
  class AppBridge {
    static instances: AppBridge[] = []

    private readonly eventListeners = new Map<
      string,
      Set<(params: unknown) => void>
    >()

    addEventListener = vi.fn(
      (event: string, listener: (params: unknown) => void) => {
        const listeners = this.eventListeners.get(event) ?? new Set()
        listeners.add(listener)
        this.eventListeners.set(event, listeners)
      },
    )
    close = vi.fn().mockResolvedValue(undefined)
    connect = vi.fn().mockResolvedValue(undefined)
    oninitialized?: () => void
    onsizechange?: (params: { height: number }) => void
    removeEventListener = vi.fn(
      (event: string, listener: (params: unknown) => void) => {
        this.eventListeners.get(event)?.delete(listener)
      },
    )
    teardownResource = vi.fn().mockResolvedValue(undefined)

    dispatchEvent(event: string, params: unknown) {
      for (const listener of this.eventListeners.get(event) ?? []) {
        listener(params)
      }
    }

    constructor(
      readonly server: unknown,
      readonly hostInfo: unknown,
      readonly capabilities: unknown,
      readonly options: unknown,
    ) {
      AppBridge.instances.push(this)
    }
  }

  class PostMessageTransport {
    static instances: PostMessageTransport[] = []

    onclose?: () => void
    onerror?: (error: Error) => void
    onmessage?: (message: unknown) => void

    constructor(
      readonly targetWindow: Window,
      readonly sourceWindow: Window,
    ) {
      PostMessageTransport.instances.push(this)
    }
  }

  return { AppBridge, PostMessageTransport }
})

vi.mock('@modelcontextprotocol/ext-apps/app-bridge', () => ({
  AppBridge: mocks.AppBridge,
  PostMessageTransport: mocks.PostMessageTransport,
}))

import { createAgentMcpAppBridge, textFromMcpUiMessage } from '../bridge'

afterEach(() => {
  vi.useRealTimers()
  vi.restoreAllMocks()
  mocks.AppBridge.instances.length = 0
  mocks.PostMessageTransport.instances.length = 0
})

describe('createAgentMcpAppBridge', () => {
  it('creates and connects the neutral protocol bridge to one iframe window', async () => {
    const targetWindow = {} as Window
    const hosted = createAgentMcpAppBridge({
      targetWindow,
      hostContext: { theme: 'light' },
    })

    const bridge = mocks.AppBridge.instances[0]
    const transport = mocks.PostMessageTransport.instances[0]
    expect(bridge?.hostInfo).toEqual({
      name: 'Agentic host',
      version: '1.0.0',
    })
    expect(bridge?.capabilities).toEqual({
      openLinks: {},
      serverTools: {},
      logging: {},
      message: { text: {} },
      updateModelContext: { text: {}, structuredContent: {} },
    })
    expect(bridge?.options).toEqual({ hostContext: { theme: 'light' } })
    expect(transport).toMatchObject({
      targetWindow,
      sourceWindow: targetWindow,
    })

    await hosted.connect()
    expect(bridge?.connect).toHaveBeenCalledWith(transport)
  })

  it('binds a dedicated frame transport to its exact HTTPS origin', async () => {
    const iframe = document.createElement('iframe')
    document.body.append(iframe)
    const targetWindow = iframe.contentWindow
    if (!targetWindow) throw new Error('expected iframe window')
    const postMessage = vi.spyOn(targetWindow, 'postMessage')
    const hosted = createAgentMcpAppBridge({
      targetWindow,
      targetOrigin: 'https://widgets.staging.interchange.io',
      hostContext: { theme: 'light' },
    })

    await hosted.connect()
    const transport = mocks.AppBridge.instances[0]?.connect.mock
      .calls[0]?.[0] as Transport | undefined
    if (!transport) throw new Error('expected transport')
    await transport.start()
    const onmessage = vi.fn()
    transport.onmessage = onmessage
    const request = {
      jsonrpc: '2.0' as const,
      id: 1,
      method: 'tools/call',
      params: {
        name: 'teach_save_material',
        arguments: { clientRequestId: 'teach-url:page:1' },
      },
    }
    const reservationResult = {
      jsonrpc: '2.0' as const,
      id: 1,
      result: { structuredContent: { processingState: 'needs_upload' } },
    }

    await transport.send(reservationResult)
    expect(postMessage).toHaveBeenCalledWith(
      reservationResult,
      'https://widgets.staging.interchange.io',
    )
    expect(mocks.PostMessageTransport.instances).toHaveLength(0)

    window.dispatchEvent(
      new MessageEvent('message', {
        data: request,
        origin: 'https://evil.example',
        source: targetWindow,
      }),
    )
    window.dispatchEvent(
      new MessageEvent('message', {
        data: request,
        origin: 'https://widgets.staging.interchange.io',
        source: window,
      }),
    )
    expect(onmessage).not.toHaveBeenCalled()

    window.dispatchEvent(
      new MessageEvent('message', {
        data: request,
        origin: 'https://widgets.staging.interchange.io',
        source: targetWindow,
      }),
    )
    expect(onmessage).toHaveBeenCalledWith(request)
  })

  it.each([
    '',
    'null',
    '*',
    'http://widgets.interchange.io',
    'https://evil.example/path',
  ])('rejects an invalid dedicated frame target origin: %s', (targetOrigin) => {
    expect(() =>
      createAgentMcpAppBridge({
        targetWindow: window,
        targetOrigin,
        hostContext: { theme: 'light' },
      }),
    ).toThrow('exact HTTPS origin')
  })

  it('performs the bounded resource teardown before closing', async () => {
    vi.useFakeTimers()
    const hosted = createAgentMcpAppBridge({
      targetWindow: {} as Window,
      hostContext: { theme: 'dark' },
    })
    const bridge = mocks.AppBridge.instances[0]

    hosted.close()
    await vi.runAllTimersAsync()

    expect(bridge?.teardownResource).toHaveBeenCalledWith({})
    expect(bridge?.close).toHaveBeenCalledOnce()
  })

  it('retires listeners and settles when transport close hangs', async () => {
    vi.useFakeTimers()
    const onInitialized = vi.fn()
    const onSizeChange = vi.fn()
    const onLoggingMessage = vi.fn()
    const hosted = createAgentMcpAppBridge({
      targetWindow: {} as Window,
      hostContext: { theme: 'dark' },
      handlers: { onInitialized, onSizeChange, onLoggingMessage },
    })
    const bridge = mocks.AppBridge.instances[0]
    const transport = mocks.PostMessageTransport.instances[0]
    if (!bridge || !transport) throw new Error('expected bridge and transport')
    bridge.teardownResource.mockReturnValueOnce(
      new Promise<void>((resolve) => globalThis.setTimeout(resolve, 400)),
    )
    bridge.close.mockReturnValueOnce(new Promise<never>(() => undefined))
    transport.onclose = vi.fn()
    transport.onerror = vi.fn()
    transport.onmessage = vi.fn()

    const retirement = hosted.close(500)
    const duplicateRetirement = hosted.close(500)
    bridge.oninitialized?.()
    bridge.onsizechange?.({ height: 720 })
    bridge.dispatchEvent('loggingmessage', { level: 'info' })

    expect(duplicateRetirement).toBe(retirement)
    expect(onInitialized).not.toHaveBeenCalled()
    expect(onSizeChange).not.toHaveBeenCalled()
    expect(onLoggingMessage).not.toHaveBeenCalled()
    expect(bridge.removeEventListener).toHaveBeenCalledWith(
      'loggingmessage',
      onLoggingMessage,
    )
    let settled = false
    void retirement.then(() => {
      settled = true
    })
    await vi.advanceTimersByTimeAsync(399)
    expect(settled).toBe(false)
    expect(bridge.close).not.toHaveBeenCalled()
    await vi.advanceTimersByTimeAsync(1)
    expect(transport.onclose).toBeUndefined()
    expect(transport.onerror).toBeUndefined()
    expect(transport.onmessage).toBeUndefined()
    expect(bridge.close).toHaveBeenCalledOnce()
    expect(settled).toBe(false)
    await vi.advanceTimersByTimeAsync(99)
    expect(settled).toBe(false)
    await vi.advanceTimersByTimeAsync(1)
    await expect(retirement).resolves.toBeUndefined()
    expect(settled).toBe(true)
    expect(bridge.teardownResource).toHaveBeenCalledWith({})
    expect(bridge.close).toHaveBeenCalledOnce()
  })

  it('times out a hung tool call, clears it, and permits teardown', async () => {
    vi.useFakeTimers()
    const abortSpy = vi.spyOn(AbortController.prototype, 'abort')
    let handlerSignal: AbortSignal | undefined
    const hosted = createAgentMcpAppBridge({
      targetWindow: {} as Window,
      hostContext: { theme: 'dark' },
      toolCallTimeoutMs: 1_000,
      handlers: {
        onCallTool: (_params, signal) => {
          handlerSignal = signal
          return new Promise<never>(() => undefined)
        },
      },
    })
    const bridge = mocks.AppBridge.instances[0] as unknown as {
      oncalltool: (
        params: { name: string; arguments: Record<string, unknown> },
        extra: { mcpReq: { signal: AbortSignal } },
      ) => Promise<{
        isError?: boolean
        content: unknown[]
        structuredContent?: Record<string, unknown>
      }>
      close: ReturnType<typeof vi.fn>
      teardownResource: ReturnType<typeof vi.fn>
    }
    const appController = new AbortController()
    const pending = bridge.oncalltool(
      { name: 'hung_tool', arguments: {} },
      { mcpReq: { signal: appController.signal } },
    )

    await vi.advanceTimersByTimeAsync(1_000)

    await expect(pending).resolves.toMatchObject({
      isError: true,
      content: [
        {
          type: 'text',
          text: 'MCP app tool call timed out after 1000ms.',
        },
      ],
      structuredContent: {
        code: 'SERVICE_UNAVAILABLE',
        message: 'MCP app tool call timed out after 1000ms.',
        retryable: true,
      },
    })
    expect(handlerSignal?.aborted).toBe(true)
    expect(handlerSignal?.reason).toMatchObject({ name: 'TimeoutError' })
    expect(abortSpy).toHaveBeenCalledOnce()

    await hosted.close()

    expect(bridge.teardownResource).toHaveBeenCalledWith({})
    expect(bridge.close).toHaveBeenCalledOnce()
    // close() aborts every active call. No second abort proves the timed-out
    // controller left activeToolCalls before resource teardown.
    expect(abortSpy).toHaveBeenCalledOnce()
  })
})

describe('textFromMcpUiMessage', () => {
  it('joins only text blocks into one trimmed prompt', () => {
    expect(
      textFromMcpUiMessage([
        { type: 'text', text: ' First ' },
        { type: 'image', data: 'ignored', mimeType: 'image/png' },
        { type: 'text', text: 'Second' },
      ]),
    ).toBe('First \n\nSecond')
  })
})
