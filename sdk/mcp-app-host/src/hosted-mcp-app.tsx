import {
  type ReactNode,
  useEffect,
  useLayoutEffect,
  useMemo,
  useRef,
  useState,
} from 'react'
import type {
  McpUiResourceCsp,
  McpUiResourcePermissions,
} from '@modelcontextprotocol/ext-apps/app-bridge'

import {
  type AgentMcpAppBridge,
  type AgentMcpAppBridgeHandlers,
  type AgentMcpHostContext,
  createAgentMcpAppBridge,
} from './bridge.js'
import { type McpAppFrame, resolveMcpAppFrame } from './frame.js'
import { MCP_APP_DOCUMENT_REPLACED_MESSAGE } from './proxy-document.js'
import { type ApproveResourceOrigin, allowAttributeFor } from './srcdoc.js'
import type { WidgetPageAppearance } from './widget-page.js'

/**
 * What the frame needs to know about the launch: the resource to load, the
 * frame's accessible title and the data to hand the widget on initialization.
 * `AgentHostDirective` in `@scope3/agent-host` satisfies it.
 */
export interface HostedMcpAppDirective {
  resourceUri: string
  title: string
  data?: Record<string, unknown>
}

const defaultMaxFrameHeight = () => Math.max(320, globalThis.innerHeight - 260)

function frameDocumentIdentity(html: string | undefined): string {
  if (!html) return 'pending'
  let hash = 2_166_136_261
  for (let index = 0; index < html.length; index += 1) {
    hash ^= html.charCodeAt(index)
    hash = Math.imul(hash, 16_777_619)
  }
  return `${html.length}:${hash >>> 0}`
}

function frameLaunchDataIdentity(data: Record<string, unknown> | undefined) {
  return frameDocumentIdentity(data ? JSON.stringify(data) : undefined)
}

export interface HostedMcpAppFrameProps {
  directive: HostedMcpAppDirective
  loadResource: (
    resourceUri: string,
    signal: AbortSignal,
  ) => Promise<string | HostedMcpAppResource>
  createHostContext: (containerWidth?: number) => AgentMcpHostContext
  handlers: AgentMcpAppBridgeHandlers
  hostInfo?: { name: string; version: string }
  contextKey?: string
  resourceLoadTimeoutMs?: number
  initializationTimeoutMs?: number
  initialHeight?: number
  minHeight?: number
  maxHeight?: number | (() => number)
  transformHtml?: (html: string) => string
  approveResourceOrigin?: ApproveResourceOrigin
  approvedPermissions?: McpUiResourcePermissions
  /**
   * Opt in to framing the page a resource names in
   * `_meta['scope3/widget-page']` instead of rendering its HTML. Give the
   * appearance to send and the origins this host trusts to frame a page from.
   * The resource must carry its `_meta` (see `HostedMcpAppResource.meta`).
   * Without it, or when the resource names no page on a trusted origin, the
   * frame renders the HTML as before.
   */
  widgetPage?: {
    appearance: WidgetPageAppearance
    allowedOrigins: readonly string[]
  }
  loadErrorMessage?: string
  initializationErrorMessage?: string
  renderError?: (message: string, retry: () => void) => ReactNode
}

export interface HostedMcpAppResource {
  html: string
  csp?: McpUiResourceCsp
  permissions?: McpUiResourcePermissions
  /** The resource's `_meta`, read for the widget page. */
  meta?: Record<string, unknown>
}

/**
 * Portable, policy-injected MCP App frame. It owns resource cancellation,
 * iframe isolation, bridge initialization, sizing and bounded teardown while
 * the host retains resource resolution, tool authority, identity and copy.
 */
export function HostedMcpAppFrame({
  directive,
  loadResource,
  createHostContext,
  handlers,
  hostInfo,
  contextKey = 'default',
  resourceLoadTimeoutMs = 15_000,
  initializationTimeoutMs = 15_000,
  initialHeight = 180,
  minHeight = 120,
  maxHeight = defaultMaxFrameHeight,
  transformHtml,
  approveResourceOrigin,
  approvedPermissions,
  widgetPage,
  loadErrorMessage = 'This Task could not be loaded.',
  initializationErrorMessage = 'This Task did not initialize.',
  renderError,
}: HostedMcpAppFrameProps) {
  const iframeRef = useRef<HTMLIFrameElement>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  const directiveRef = useRef(directive)
  const loadResourceRef = useRef(loadResource)
  const loadErrorMessageRef = useRef(loadErrorMessage)
  const handlersRef = useRef(handlers)
  const contextFactoryRef = useRef(createHostContext)
  const [resource, setResource] = useState<HostedMcpAppResource | null>(null)
  const [height, setHeight] = useState(initialHeight)
  const [error, setError] = useState<string | null>(null)
  const [frameLoadSequence, setFrameLoadSequence] = useState(0)
  const activeBridgeFrameKeyRef = useRef<string | null>(null)
  const [retry, setRetry] = useState(0)

  directiveRef.current = directive
  loadResourceRef.current = loadResource
  loadErrorMessageRef.current = loadErrorMessage
  handlersRef.current = handlers
  contextFactoryRef.current = createHostContext

  useEffect(() => {
    void retry
    const controller = new AbortController()
    setError(null)
    setResource(null)
    const timeout = globalThis.setTimeout(() => {
      controller.abort()
      setError(loadErrorMessageRef.current)
    }, resourceLoadTimeoutMs)
    loadResourceRef
      .current(directive.resourceUri, controller.signal)
      .then((nextResource) => {
        globalThis.clearTimeout(timeout)
        if (!controller.signal.aborted) {
          setResource(
            typeof nextResource === 'string'
              ? { html: nextResource }
              : nextResource,
          )
        }
      })
      .catch(() => {
        globalThis.clearTimeout(timeout)
        if (!controller.signal.aborted) setError(loadErrorMessageRef.current)
      })
    return () => {
      globalThis.clearTimeout(timeout)
      controller.abort()
    }
  }, [directive.resourceUri, resourceLoadTimeoutMs, retry])

  const frame = useMemo<McpAppFrame | null>(() => {
    if (!resource) return null
    return resolveMcpAppFrame({
      html: transformHtml?.(resource.html) ?? resource.html,
      meta: resource.meta,
      csp: resource.csp,
      permissions: resource.permissions,
      approveResourceOrigin,
      approvedPermissions,
      page: widgetPage,
    })
  }, [
    approveResourceOrigin,
    approvedPermissions,
    resource,
    transformHtml,
    widgetPage,
  ])
  const frameSource =
    frame?.kind === 'page' ? frame.src : (frame?.srcDoc ?? undefined)
  const targetOrigin = frame?.targetOrigin
  const allow =
    frame?.kind === 'srcdoc'
      ? frame.allow
      : allowAttributeFor(resource?.permissions, approvedPermissions)
  const frameKey = `${directive.resourceUri}:${contextKey}:${retry}:${frameDocumentIdentity(frameSource)}:${frameLaunchDataIdentity(directive.data)}`

  useLayoutEffect(() => {
    void frameLoadSequence
    const targetWindow = iframeRef.current?.contentWindow
    if (!resource || !targetWindow) return
    let cancelled = false
    let hosted: AgentMcpAppBridge
    activeBridgeFrameKeyRef.current = frameKey
    const timeout = globalThis.setTimeout(() => {
      if (!cancelled) {
        cancelled = true
        setError(initializationErrorMessage)
        void hosted.close()
      }
    }, initializationTimeoutMs)
    hosted = createAgentMcpAppBridge({
      targetWindow,
      targetOrigin,
      hostContext: contextFactoryRef.current(containerRef.current?.clientWidth),
      hostInfo,
      handlers: {
        onInitialized: () => {
          if (cancelled) return
          globalThis.clearTimeout(timeout)
          setError(null)
          handlersRef.current.onInitialized?.()
          void hosted.bridge.sendToolInput({
            arguments: directiveRef.current.data ?? {},
          })
          void hosted.bridge.sendToolResult({
            content: [],
            structuredContent: directiveRef.current.data ?? {},
          })
        },
        onSizeChange: (nextHeight) => {
          if (cancelled) return
          const cap = typeof maxHeight === 'function' ? maxHeight() : maxHeight
          setHeight(Math.min(cap, Math.max(minHeight, Math.ceil(nextHeight))))
          handlersRef.current.onSizeChange?.(nextHeight)
        },
        onMessage: (params) =>
          handlersRef.current.onMessage?.(params) ??
          Promise.resolve({ isError: true }),
        onUpdateModelContext: (params) =>
          handlersRef.current.onUpdateModelContext?.(params) ??
          Promise.resolve({}),
        onRequestTeardown: () => handlersRef.current.onRequestTeardown?.(),
        onOpenLink: (url) =>
          handlersRef.current.onOpenLink?.(url) ??
          Promise.resolve({ isError: true }),
        onCallTool: (params, signal) =>
          handlersRef.current.onCallTool?.(params, signal) ??
          Promise.resolve({
            isError: true,
            content: [{ type: 'text', text: 'MCP app tool call denied.' }],
          }),
        onLoggingMessage: (params) =>
          handlersRef.current.onLoggingMessage?.(params),
      },
    })
    void hosted.connect().catch(() => {
      if (!cancelled) {
        cancelled = true
        globalThis.clearTimeout(timeout)
        setError(initializationErrorMessage)
        void hosted.close()
      }
    })
    return () => {
      cancelled = true
      if (activeBridgeFrameKeyRef.current === frameKey) {
        activeBridgeFrameKeyRef.current = null
      }
      globalThis.clearTimeout(timeout)
      void hosted.close()
    }
  }, [
    frameKey,
    frameLoadSequence,
    hostInfo,
    resource,
    targetOrigin,
    initializationErrorMessage,
    initializationTimeoutMs,
    maxHeight,
    minHeight,
  ])

  // The proxy stops relaying once the app document leaves or its frame loads
  // a second document. Show the error and its Retry rather than a frame that
  // no longer answers.
  useEffect(() => {
    const onReplaced = (event: MessageEvent) => {
      if (
        event.source === iframeRef.current?.contentWindow &&
        typeof event.data === 'object' &&
        event.data !== null &&
        (event.data as { type?: unknown }).type ===
          MCP_APP_DOCUMENT_REPLACED_MESSAGE
      ) {
        setError(loadErrorMessageRef.current)
      }
    }
    window.addEventListener('message', onReplaced)
    return () => window.removeEventListener('message', onReplaced)
  }, [])

  const retryLoad = () => setRetry((value) => value + 1)

  return (
    <div ref={containerRef} style={{ minWidth: 0, width: '100%' }}>
      {error
        ? (renderError?.(error, retryLoad) ?? (
            <output>
              <span>{error}</span>{' '}
              <button type="button" onClick={retryLoad}>
                Retry
              </button>
            </output>
          ))
        : null}
      {frame ? (
        <iframe
          key={frameKey}
          ref={iframeRef}
          title={directive.title}
          src={frame.kind === 'page' ? frame.src : undefined}
          srcDoc={frame.kind === 'srcdoc' ? frame.srcDoc : undefined}
          sandbox={frame.sandbox}
          allow={allow || undefined}
          referrerPolicy="no-referrer"
          onLoad={(event) => {
            // Normally the layout effect starts the host listener before the
            // document's scripts can send ui/initialize. A few DOM engines do
            // not expose contentWindow until load; re-arm only for that
            // fallback, never for a duplicate load on an active bridge.
            if (
              event.currentTarget === iframeRef.current &&
              event.currentTarget.contentWindow &&
              activeBridgeFrameKeyRef.current !== frameKey
            ) {
              setFrameLoadSequence((value) => value + 1)
            }
          }}
          style={{
            border: 0,
            display: error ? 'none' : 'block',
            height,
            width: '100%',
          }}
        />
      ) : null}
    </div>
  )
}
