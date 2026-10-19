import type {
  McpUiResourceCsp,
  McpUiResourcePermissions,
} from '@modelcontextprotocol/ext-apps/app-bridge'

import {
  type ApproveResourceOrigin,
  allowAttributeFor,
  buildHostedMcpAppSrcDoc,
  HOSTED_MCP_APP_SRCDOC_SANDBOX,
} from './srcdoc.js'
import {
  type WidgetPageAppearance,
  type WidgetPageFrame,
  widgetPageFrame,
} from './widget-page.js'

export interface SrcdocFrame {
  kind: 'srcdoc'
  /** The proxy document to render as the iframe `srcdoc`. */
  srcDoc: string
  /** The iframe `allow` attribute; empty when no permission is granted. */
  allow: string
  /**
   * A srcdoc frame has no origin the host can name, so the bridge matches the
   * proxy's window instead. Omit `targetOrigin` from `createAgentMcpAppBridge`.
   */
  targetOrigin: undefined
  sandbox: typeof HOSTED_MCP_APP_SRCDOC_SANDBOX
}

export type McpAppFrame = WidgetPageFrame | SrcdocFrame

export interface ResolveMcpAppFrameInput {
  /** The resource's `_meta` from `resources/read` or `resources/list`. */
  meta?: Record<string, unknown> | null
  /**
   * The resource's HTML, the fallback when it names no usable page. A host that
   * only ever frames pages may omit it.
   */
  html?: string
  /**
   * Opt in to framing widget pages: the appearance to send and the origins this
   * host trusts to frame a page from. Without it the HTML is always rendered.
   */
  page?: {
    appearance: WidgetPageAppearance
    allowedOrigins: readonly string[]
  }
  /** Overrides `meta.ui.csp`. */
  csp?: McpUiResourceCsp
  /** Overrides `meta.ui.permissions`. */
  permissions?: McpUiResourcePermissions
  /** Grants the origins a widget declares in its CSP (srcdoc only). */
  approveResourceOrigin?: ApproveResourceOrigin
  /** The permissions this host will grant a widget. */
  approvedPermissions?: McpUiResourcePermissions
}

function uiMeta(
  meta: Record<string, unknown> | null | undefined,
): Record<string, unknown> | undefined {
  const ui = meta?.ui
  return typeof ui === 'object' && ui !== null
    ? (ui as Record<string, unknown>)
    : undefined
}

/**
 * Decides how to render a widget resource in an iframe: frame the page it names
 * in `_meta['scope3/widget-page']` when `page` is given and it names one on a trusted origin, else
 * render its HTML as the `srcdoc` of a host-owned proxy document. Null when it
 * has neither.
 *
 * Wire the result to the frame and the bridge:
 *
 * - `page`: `<iframe src={frame.src} sandbox={frame.sandbox}>`, and
 *   `createAgentMcpAppBridge({ targetOrigin: frame.targetOrigin, ... })`.
 * - `srcdoc`: `<iframe srcDoc={frame.srcDoc} sandbox={frame.sandbox}
 *   allow={frame.allow || undefined}>`, and the bridge without a `targetOrigin`.
 */
export function resolveMcpAppFrame(
  input: ResolveMcpAppFrameInput,
): McpAppFrame | null {
  const page = input.page
    ? widgetPageFrame(
        input.meta,
        input.page.appearance,
        input.page.allowedOrigins,
      )
    : null
  if (page) return page
  if (input.html === undefined) return null
  const ui = uiMeta(input.meta)
  const csp = input.csp ?? (ui?.csp as McpUiResourceCsp | undefined)
  const permissions =
    input.permissions ??
    (ui?.permissions as McpUiResourcePermissions | undefined)
  const allow = allowAttributeFor(permissions, input.approvedPermissions)
  return {
    kind: 'srcdoc',
    srcDoc: buildHostedMcpAppSrcDoc({
      html: input.html,
      csp,
      approveResourceOrigin: input.approveResourceOrigin,
      allow,
    }),
    allow,
    targetOrigin: undefined,
    sandbox: HOSTED_MCP_APP_SRCDOC_SANDBOX,
  }
}
