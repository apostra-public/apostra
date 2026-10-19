import { describe, expect, it } from 'vitest'

import {
  APOSTRA_WIDGET_PAGE_ORIGINS,
  readWidgetPageMeta,
  WIDGET_PAGE_FRAME_SANDBOX,
  WIDGET_PAGE_META_KEY,
  widgetPageFrame,
} from '../widget-page'

const APPEARANCE = {
  colorScheme: 'dark',
  productBrand: 'new',
  hostCorner: 'released',
} as const

const PAGE = {
  url: 'https://widgets.apostra.com/upload-creative-asset/mcp-app.html',
  appearanceParams: ['color-scheme', 'product-brand', 'host-corner'],
}

const metaWith = (page: unknown) => ({ [WIDGET_PAGE_META_KEY]: page })

describe('readWidgetPageMeta', () => {
  it('reads the page the resource names', () => {
    expect(readWidgetPageMeta(metaWith(PAGE))).toEqual(PAGE)
  })

  it.each([
    ['no _meta', undefined],
    ['no page key', { ui: {} }],
    ['a page that is not an object', metaWith('https://x.example')],
    ['a page without a url', metaWith({ appearanceParams: [] })],
    ['a page without a parameter list', metaWith({ url: PAGE.url })],
    [
      'a parameter list holding a non-string',
      metaWith({ url: PAGE.url, appearanceParams: [1] }),
    ],
  ])('returns null for %s', (_name, meta) => {
    expect(
      readWidgetPageMeta(meta as Record<string, unknown> | undefined),
    ).toBeNull()
  })
})

describe('widgetPageFrame', () => {
  it('frames the page with the appearance the resource asks for', () => {
    const frame = widgetPageFrame(
      metaWith(PAGE),
      APPEARANCE,
      APOSTRA_WIDGET_PAGE_ORIGINS,
    )
    expect(frame).toEqual({
      kind: 'page',
      src: `${PAGE.url}?color-scheme=dark&product-brand=new&host-corner=released`,
      targetOrigin: 'https://widgets.apostra.com',
      sandbox: WIDGET_PAGE_FRAME_SANDBOX,
    })
  })

  it('keeps the page origin so it can reach storage, and nothing else extra', () => {
    expect(WIDGET_PAGE_FRAME_SANDBOX).toBe(
      'allow-scripts allow-same-origin allow-forms',
    )
  })

  it('sends only the parameters the resource lists', () => {
    const frame = widgetPageFrame(
      metaWith({
        ...PAGE,
        appearanceParams: ['color-scheme', 'product-brand'],
      }),
      APPEARANCE,
      APOSTRA_WIDGET_PAGE_ORIGINS,
    )
    expect(new URL(frame?.src ?? '').search).toBe(
      '?color-scheme=dark&product-brand=new',
    )
  })

  it('leaves out host-corner when the host does not set it, and parameters it cannot fill', () => {
    const frame = widgetPageFrame(
      metaWith({ ...PAGE, appearanceParams: [...PAGE.appearanceParams, 'x'] }),
      { colorScheme: 'light', productBrand: 'legacy' },
      APOSTRA_WIDGET_PAGE_ORIGINS,
    )
    expect(new URL(frame?.src ?? '').search).toBe(
      '?color-scheme=light&product-brand=legacy',
    )
  })

  it('frames a staging page only when the host trusts the staging origin', () => {
    const staging = {
      ...PAGE,
      url: 'https://widgets.staging.apostra.com/library/mcp-app.html',
    }
    expect(
      widgetPageFrame(metaWith(staging), APPEARANCE, [
        'https://widgets.apostra.com',
      ]),
    ).toBeNull()
    expect(
      widgetPageFrame(metaWith(staging), APPEARANCE, [
        'https://widgets.staging.apostra.com',
      ])?.targetOrigin,
    ).toBe('https://widgets.staging.apostra.com')
  })

  it.each([
    ['an untrusted origin', 'https://evil.example/mcp-app.html'],
    ['a plain http page', 'http://widgets.apostra.com/library/mcp-app.html'],
    [
      'a page with credentials',
      'https://user:pw@widgets.apostra.com/library/mcp-app.html',
    ],
    [
      'a page that already has a query',
      'https://widgets.apostra.com/library/mcp-app.html?a=1',
    ],
    [
      'a page with a fragment',
      'https://widgets.apostra.com/library/mcp-app.html#x',
    ],
    ['a url that does not parse', 'not a url'],
  ])('refuses %s', (_name, url) => {
    expect(
      widgetPageFrame(
        metaWith({ ...PAGE, url }),
        APPEARANCE,
        APOSTRA_WIDGET_PAGE_ORIGINS,
      ),
    ).toBeNull()
  })

  it('returns null when the resource names no page', () => {
    expect(
      widgetPageFrame({ ui: {} }, APPEARANCE, APOSTRA_WIDGET_PAGE_ORIGINS),
    ).toBeNull()
  })
})
