import { DEDICATED_WIDGET_FRAME_SANDBOX } from './frame-security.js'

/**
 * The `_meta` key under which a V3 MCP App resource names the page it is also
 * served from on the Apostra widget origin, in both `resources/list` and
 * `resources/read`. It is a top-level key, so the standard `_meta.ui` object
 * stays what the MCP Apps spec defines. A resource without it has no page: load
 * its HTML instead.
 */
export const WIDGET_PAGE_META_KEY = 'scope3/widget-page'

/**
 * The origins Apostra serves widget pages from. Pass these (or the one for your
 * environment) as `allowedOrigins`; a host must not frame a page from an origin
 * it has not chosen to trust.
 */
export const APOSTRA_WIDGET_PAGE_ORIGINS = [
  'https://widgets.apostra.com',
  'https://widgets.staging.apostra.com',
] as const

/** The sandbox of a frame that loads a widget page. */
export const WIDGET_PAGE_FRAME_SANDBOX = DEDICATED_WIDGET_FRAME_SANDBOX

export interface WidgetPageMeta {
  /** The absolute page URL, without a query string. */
  url: string
  /** The query parameters the host appends to describe its appearance. */
  appearanceParams: readonly string[]
}

/** How the host looks, which the widget page matches. */
export interface WidgetPageAppearance {
  colorScheme: 'light' | 'dark'
  productBrand: 'new' | 'legacy'
  /**
   * `reserved` when the host draws its own control in the widget's top-right
   * corner and the widget leaves room for it, `released` when it does not.
   * Omit it to render as a host that does not send it does (`reserved`).
   */
  hostCorner?: 'reserved' | 'released'
}

export interface WidgetPageFrame {
  kind: 'page'
  /** The iframe `src`: the page URL with the appearance parameters set. */
  src: string
  /**
   * The one origin the host bridge exchanges messages with. Pass it as
   * `targetOrigin` to `createAgentMcpAppBridge`.
   */
  targetOrigin: string
  sandbox: typeof WIDGET_PAGE_FRAME_SANDBOX
}

/**
 * Reads the widget page a resource names in its `_meta`, or null when the
 * resource names none or names one that is not an https page URL.
 */
export function readWidgetPageMeta(
  meta: Record<string, unknown> | null | undefined,
): WidgetPageMeta | null {
  const value = meta?.[WIDGET_PAGE_META_KEY]
  if (typeof value !== 'object' || value === null) return null
  const { url, appearanceParams } = value as Record<string, unknown>
  if (typeof url !== 'string') return null
  if (
    !Array.isArray(appearanceParams) ||
    !appearanceParams.every((param) => typeof param === 'string')
  ) {
    return null
  }
  return { url, appearanceParams }
}

/**
 * Builds the frame for a widget page, or null when the resource names no page
 * or its page is not on an origin in `allowedOrigins`. A null result means
 * render the resource's HTML instead (see `resolveMcpAppFrame`).
 *
 * The page keeps its own origin, so its sandbox grants `allow-same-origin`.
 * That is safe only because the page holds no cookies or session and every
 * tool call goes through the host bridge under the host's own credentials, and
 * only for an origin the host trusts, which is why `allowedOrigins` is
 * required rather than defaulted. Only the parameters the resource lists are
 * sent, and only the ones this host knows how to fill.
 */
export function widgetPageFrame(
  meta: Record<string, unknown> | null | undefined,
  appearance: WidgetPageAppearance,
  allowedOrigins: readonly string[],
): WidgetPageFrame | null {
  const page = readWidgetPageMeta(meta)
  if (!page) return null
  let url: URL
  try {
    url = new URL(page.url)
  } catch {
    return null
  }
  if (
    url.protocol !== 'https:' ||
    url.username !== '' ||
    url.password !== '' ||
    url.search !== '' ||
    url.hash !== '' ||
    !allowedOrigins.includes(url.origin)
  ) {
    return null
  }
  const values: Record<string, string | undefined> = {
    'color-scheme': appearance.colorScheme,
    'product-brand': appearance.productBrand,
    'host-corner': appearance.hostCorner,
  }
  for (const param of page.appearanceParams) {
    const value = values[param]
    if (value !== undefined) url.searchParams.set(param, value)
  }
  return {
    kind: 'page',
    src: url.href,
    targetOrigin: url.origin,
    sandbox: WIDGET_PAGE_FRAME_SANDBOX,
  }
}
