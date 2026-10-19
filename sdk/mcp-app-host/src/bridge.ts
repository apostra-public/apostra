import {
  AppBridge,
  type McpUiHostContext,
  type McpUiMessageRequest,
  type McpUiUpdateModelContextRequest,
  PostMessageTransport,
} from '@modelcontextprotocol/ext-apps/app-bridge'
import type { Transport } from '@modelcontextprotocol/sdk/shared/transport.js'
import type {
  CallToolRequest,
  CallToolResult,
  JSONRPCMessage,
} from '@modelcontextprotocol/sdk/types.js'
import { JSONRPCMessageSchema } from '@modelcontextprotocol/sdk/types.js'

export type AgentMcpHostContext = McpUiHostContext
export type AgentMcpCallToolParams = CallToolRequest['params']
export type AgentMcpCallToolResult = CallToolResult

export interface AgentMcpAppBridgeHandlers {
  onInitialized?: () => void
  onSizeChange?: (height: number) => void
  onMessage?: (
    params: McpUiMessageRequest['params'],
  ) => Promise<Record<string, unknown>>
  onUpdateModelContext?: (
    params: McpUiUpdateModelContextRequest['params'],
  ) => Promise<Record<string, unknown>>
  onRequestTeardown?: () => void
  onOpenLink?: (url: string) => Promise<Record<string, unknown>>
  onCallTool?: (
    params: AgentMcpCallToolParams,
    signal: AbortSignal,
  ) => Promise<AgentMcpCallToolResult>
  onLoggingMessage?: (params: unknown) => void
}

export interface AgentMcpAppBridgeController {
  addEventListener: AppBridge['addEventListener']
  close: AppBridge['close']
  oncalltool: AppBridge['oncalltool']
  oninitialized: AppBridge['oninitialized']
  onmessage: AppBridge['onmessage']
  onopenlink: AppBridge['onopenlink']
  onrequestteardown: AppBridge['onrequestteardown']
  onsizechange: AppBridge['onsizechange']
  onupdatemodelcontext: AppBridge['onupdatemodelcontext']
  removeEventListener: AppBridge['removeEventListener']
  sendToolInput: AppBridge['sendToolInput']
  sendToolResult: AppBridge['sendToolResult']
  setHostContext: AppBridge['setHostContext']
  teardownResource: AppBridge['teardownResource']
}

export interface AgentMcpAppBridge {
  bridge: AgentMcpAppBridgeController
  connect: () => Promise<void>
  close: (timeoutMs?: number) => Promise<void>
}

// Match the MCP SDK's default request timeout while keeping this host boundary
// independently bounded when an injected handler ignores cancellation.
const DEFAULT_TOOL_CALL_TIMEOUT_MS = 60_000

class ExactOriginPostMessageTransport implements Transport {
  onclose?: () => void
  onerror?: (error: Error) => void
  onmessage?: (message: JSONRPCMessage) => void
  sessionId?: string
  setProtocolVersion?: (version: string) => void

  private started = false
  private readonly messageListener = (event: MessageEvent) => {
    if (
      event.source !== this.targetWindow ||
      event.origin !== this.targetOrigin
    ) {
      return
    }
    const parsed = JSONRPCMessageSchema.safeParse(event.data)
    if (parsed.success) {
      this.onmessage?.(parsed.data)
    } else if (event.data?.jsonrpc === '2.0') {
      this.onerror?.(new Error('Invalid JSON-RPC message received.'))
    }
  }

  constructor(
    private readonly targetWindow: Window,
    private readonly targetOrigin: string,
  ) {}

  async start(): Promise<void> {
    if (this.started) return
    this.started = true
    window.addEventListener('message', this.messageListener)
  }

  async send(message: JSONRPCMessage): Promise<void> {
    this.targetWindow.postMessage(message, this.targetOrigin)
  }

  async close(): Promise<void> {
    if (!this.started) return
    this.started = false
    window.removeEventListener('message', this.messageListener)
    this.onclose?.()
  }
}

function exactHttpsOrigin(origin: string): string {
  try {
    const parsed = new URL(origin)
    if (
      parsed.protocol === 'https:' &&
      parsed.origin === origin &&
      parsed.username === '' &&
      parsed.password === '' &&
      parsed.pathname === '/' &&
      parsed.search === '' &&
      parsed.hash === ''
    ) {
      return parsed.origin
    }
  } catch {
    // Fall through to the single bounded error below.
  }
  throw new Error('MCP app targetOrigin must be an exact HTTPS origin.')
}

/**
 * Creates the MCP Apps protocol bridge for an iframe without making product
 * policy decisions. Consumers inject message, tool, navigation, telemetry and
 * teardown-request handlers, or attach them directly before calling `connect`.
 */
export function createAgentMcpAppBridge(input: {
  targetWindow: Window
  targetOrigin?: string
  hostContext: AgentMcpHostContext
  hostInfo?: { name: string; version: string }
  handlers?: AgentMcpAppBridgeHandlers
  toolCallTimeoutMs?: number
}): AgentMcpAppBridge {
  let closed = false
  let closePromise: Promise<void> | null = null
  const activeToolCalls = new Set<AbortController>()
  const toolCallTimeoutMs =
    input.toolCallTimeoutMs !== undefined &&
    Number.isFinite(input.toolCallTimeoutMs) &&
    input.toolCallTimeoutMs > 0
      ? input.toolCallTimeoutMs
      : DEFAULT_TOOL_CALL_TIMEOUT_MS
  const bridge = new AppBridge(
    null,
    input.hostInfo ?? { name: 'Agentic host', version: '1.0.0' },
    {
      openLinks: {},
      serverTools: {},
      logging: {},
      message: { text: {} },
      updateModelContext: { text: {}, structuredContent: {} },
    },
    { hostContext: input.hostContext },
  )
  const handlers = input.handlers
  const loggingMessageHandler = handlers?.onLoggingMessage
  if (handlers) {
    bridge.oninitialized = () => handlers.onInitialized?.()
    bridge.onsizechange = ({ height }) => {
      if (typeof height === 'number') handlers.onSizeChange?.(height)
    }
    bridge.onmessage = async (params) =>
      handlers.onMessage?.(params) ?? { isError: true }
    bridge.onupdatemodelcontext = async (params) =>
      handlers.onUpdateModelContext?.(params) ?? {}
    bridge.onrequestteardown = () => handlers.onRequestTeardown?.()
    bridge.onopenlink = async ({ url }) =>
      handlers.onOpenLink?.(url) ?? { isError: true }
    bridge.oncalltool = async (params, extra) => {
      if (closed || !handlers.onCallTool) {
        return deniedToolResult()
      }
      const controller = new AbortController()
      const abort = () => controller.abort(extra.mcpReq.signal.reason)
      if (extra.mcpReq.signal.aborted) abort()
      else extra.mcpReq.signal.addEventListener('abort', abort, { once: true })
      activeToolCalls.add(controller)
      let timeout: ReturnType<typeof globalThis.setTimeout> | undefined
      try {
        const handlerResult = handlers.onCallTool(params, controller.signal)
        const deadlineResult = new Promise<AgentMcpCallToolResult>(
          (resolve) => {
            timeout = globalThis.setTimeout(() => {
              const timeoutError = new Error(
                `MCP app tool call timed out after ${toolCallTimeoutMs}ms.`,
              )
              timeoutError.name = 'TimeoutError'
              resolve(toolCallTimeoutResult(toolCallTimeoutMs))
              controller.abort(timeoutError)
            }, toolCallTimeoutMs)
          },
        )
        return await Promise.race([handlerResult, deadlineResult])
      } finally {
        if (timeout !== undefined) globalThis.clearTimeout(timeout)
        activeToolCalls.delete(controller)
        extra.mcpReq.signal.removeEventListener('abort', abort)
      }
    }
    if (loggingMessageHandler) {
      bridge.addEventListener('loggingmessage', loggingMessageHandler)
    }
  }
  const transport =
    input.targetOrigin !== undefined
      ? new ExactOriginPostMessageTransport(
          input.targetWindow,
          exactHttpsOrigin(input.targetOrigin),
        )
      : new PostMessageTransport(input.targetWindow, input.targetWindow)

  return {
    bridge,
    connect: () => bridge.connect(transport),
    close: (timeoutMs = 500) => {
      if (closePromise) return closePromise
      closed = true
      for (const controller of activeToolCalls) controller.abort()
      bridge.oninitialized = () => undefined
      bridge.onsizechange = () => undefined
      bridge.oncalltool = async () => deniedToolResult()
      bridge.onmessage = async () => ({ isError: true })
      bridge.onupdatemodelcontext = async () => ({})
      bridge.onopenlink = async () => ({ isError: true })
      bridge.onrequestteardown = () => undefined
      if (loggingMessageHandler) {
        bridge.removeEventListener('loggingmessage', loggingMessageHandler)
      }

      closePromise = (async () => {
        let timeout: ReturnType<typeof globalThis.setTimeout> | undefined
        const deadline = new Promise<void>((resolve) => {
          timeout = globalThis.setTimeout(resolve, timeoutMs)
        })
        try {
          await Promise.race([
            bridge.teardownResource({}).catch(() => undefined),
            deadline,
          ])
          // A transport whose close promise stalls must no longer retain the
          // retired bridge through its callbacks or deliver iframe messages.
          transport.onclose = undefined
          transport.onerror = undefined
          transport.onmessage = undefined
          await Promise.race([bridge.close(), deadline])
        } finally {
          if (timeout !== undefined) globalThis.clearTimeout(timeout)
        }
      })()
      return closePromise
    },
  }
}

function deniedToolResult(): AgentMcpCallToolResult {
  return {
    isError: true,
    content: [{ type: 'text', text: 'MCP app tool call denied.' }],
  }
}

function toolCallTimeoutResult(timeoutMs: number): AgentMcpCallToolResult {
  const message = `MCP app tool call timed out after ${timeoutMs}ms.`
  return {
    isError: true,
    content: [{ type: 'text', text: message }],
    structuredContent: {
      code: 'SERVICE_UNAVAILABLE',
      message,
      retryable: true,
    },
  }
}

export function textFromMcpUiMessage(
  content: McpUiMessageRequest['params']['content'] | undefined,
): string {
  if (!content) return ''
  return content
    .flatMap((block) => (block.type === 'text' ? [block.text] : []))
    .join('\n\n')
    .trim()
}
