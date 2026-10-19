// @vitest-environment jsdom

import { describe, expect, it, vi } from 'vitest'

vi.mock('@modelcontextprotocol/ext-apps/app-bridge', () => ({
  AppBridge: class {},
  PostMessageTransport: class {},
  buildAllowAttribute: (permissions: Record<string, unknown> | undefined) =>
    permissions ? Object.keys(permissions).join('; ') : '',
}))

import { resolveMcpAppFrame } from '../frame'
import {
  APOSTRA_WIDGET_PAGE_ORIGINS,
  WIDGET_PAGE_META_KEY,
} from '../widget-page'

const HTML = '<!doctype html><html><body>Widget</body></html>'
const APPEARANCE = { colorScheme: 'light', productBrand: 'new' } as const
const PAGE_META = {
  [WIDGET_PAGE_META_KEY]: {
    url: 'https://widgets.apostra.com/library/mcp-app.html',
    appearanceParams: ['color-scheme', 'product-brand', 'host-corner'],
  },
}
const page = {
  appearance: APPEARANCE,
  allowedOrigins: APOSTRA_WIDGET_PAGE_ORIGINS,
}

describe('resolveMcpAppFrame', () => {
  it('frames the widget page when the resource names one on a trusted origin', () => {
    const frame = resolveMcpAppFrame({ meta: PAGE_META, html: HTML, page })
    expect(frame).toMatchObject({
      kind: 'page',
      src: 'https://widgets.apostra.com/library/mcp-app.html?color-scheme=light&product-brand=new',
      targetOrigin: 'https://widgets.apostra.com',
      sandbox: 'allow-scripts allow-same-origin allow-forms',
    })
  })

  it('needs no HTML to frame a page', () => {
    expect(resolveMcpAppFrame({ meta: PAGE_META, page })?.kind).toBe('page')
  })

  it('falls back to srcdoc when the resource names no page', () => {
    const frame = resolveMcpAppFrame({ meta: { ui: {} }, html: HTML, page })
    expect(frame?.kind).toBe('srcdoc')
    expect(frame).toMatchObject({
      sandbox: 'allow-scripts',
      targetOrigin: undefined,
    })
  })

  it('falls back to srcdoc when the page origin is not trusted', () => {
    const frame = resolveMcpAppFrame({
      meta: PAGE_META,
      html: HTML,
      page: { ...page, allowedOrigins: ['https://widgets.example.com'] },
    })
    expect(frame?.kind).toBe('srcdoc')
  })

  it('renders srcdoc when the host did not opt in to pages', () => {
    expect(resolveMcpAppFrame({ meta: PAGE_META, html: HTML })?.kind).toBe(
      'srcdoc',
    )
  })

  it('returns null with neither a usable page nor HTML', () => {
    expect(resolveMcpAppFrame({ meta: { ui: {} }, page })).toBeNull()
  })

  it('builds the srcdoc CSP from _meta.ui.csp, granting frameDomains only when approved', () => {
    const meta = {
      ui: {
        csp: {
          frameDomains: [
            'https://render.example.com',
            'https://other.example.com',
          ],
          connectDomains: ['https://api.example.com'],
        },
      },
    }
    const frame = resolveMcpAppFrame({
      meta,
      html: HTML,
      approveResourceOrigin: (origin, directive) =>
        directive === 'frameDomains' && origin === 'https://render.example.com',
    })
    const srcDoc = frame?.kind === 'srcdoc' ? frame.srcDoc : ''
    expect(srcDoc).toContain('frame-src https://render.example.com;')
    expect(srcDoc).not.toContain('other.example.com')
    expect(srcDoc).toContain("connect-src 'none'")
  })

  it('grants only the permissions both the widget and the host want', () => {
    const frame = resolveMcpAppFrame({
      meta: { ui: { permissions: { camera: {}, clipboardWrite: {} } } },
      html: HTML,
      approvedPermissions: { clipboardWrite: {} },
    })
    expect(frame).toMatchObject({ kind: 'srcdoc', allow: 'clipboardWrite' })
  })
})
