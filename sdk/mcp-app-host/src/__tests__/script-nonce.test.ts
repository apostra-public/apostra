// @vitest-environment jsdom
import { describe, expect, it } from 'vitest'

import { buildMcpAppProxyDocument } from '../proxy-document'
import { stampScriptNonce } from '../script-nonce'

const NONCE = 'abcdefghijklmnopqrstuv=='

function scripts(html: string): HTMLScriptElement[] {
  return [
    ...new DOMParser()
      .parseFromString(html, 'text/html')
      .querySelectorAll('script'),
  ]
}

describe('stampScriptNonce', () => {
  it('puts the nonce on every script, inline or external, in head or body', () => {
    const stamped = stampScriptNonce(
      `<!doctype html><html><head><script>one()</script><script src="/a.js"></script></head><body><script type="module">two()</script></body></html>`,
      NONCE,
    )

    const found = scripts(stamped)
    expect(found).toHaveLength(3)
    expect(found.map((s) => s.getAttribute('nonce'))).toEqual([
      NONCE,
      NONCE,
      NONCE,
    ])
  })

  it('leaves a script that mentions a script tag in a string exactly as it was', () => {
    // React DOM and other bundles carry markup in strings. Rewriting the HTML
    // as text would put the nonce inside the string and break the bundle.
    const code = `const probe = '<script><\\/script>'; const open = "<script nonce>"; run(probe, open)`
    const stamped = stampScriptNonce(
      `<!doctype html><html><head><script>${code}</script></head><body></body></html>`,
      NONCE,
    )

    const [only] = scripts(stamped)
    expect(scripts(stamped)).toHaveLength(1)
    expect(only?.textContent).toBe(code)
    expect(only?.getAttribute('nonce')).toBe(NONCE)
  })

  it('keeps the document around the scripts: doctype, attributes, policy meta and styles', () => {
    const stamped = stampScriptNonce(
      `<!doctype html><html lang="en" data-product-brand="new"><head><meta http-equiv="Content-Security-Policy" content="default-src 'none'"><style>:root{color-scheme:dark}</style></head><body><p id="x">hi</p></body></html>`,
      NONCE,
    )

    expect(stamped.startsWith('<!doctype html>')).toBe(true)
    const document = new DOMParser().parseFromString(stamped, 'text/html')
    expect(document.documentElement.getAttribute('data-product-brand')).toBe(
      'new',
    )
    expect(
      document
        .querySelector('meta[http-equiv="Content-Security-Policy"]')
        ?.getAttribute('content'),
    ).toBe("default-src 'none'")
    expect(document.querySelector('style')?.textContent).toBe(
      ':root{color-scheme:dark}',
    )
    expect(document.querySelector('#x')?.textContent).toBe('hi')
  })

  it('stamps a fragment-shaped document too', () => {
    const [only] = scripts(
      stampScriptNonce('<script>go()</script><p>hi</p>', NONCE),
    )

    expect(only?.getAttribute('nonce')).toBe(NONCE)
  })
})

describe('the proxy document nonce', () => {
  const input = {
    appDocument: '<!doctype html><html><body>app</body></html>',
    policy: "default-src 'none'; script-src 'unsafe-inline'",
    sandbox: 'allow-scripts',
  }

  it('puts the nonce on the relay script when given one', () => {
    const [relay] = scripts(
      buildMcpAppProxyDocument({ ...input, nonce: NONCE }),
    )

    expect(relay?.getAttribute('nonce')).toBe(NONCE)
  })

  it('adds no nonce when none is given', () => {
    const [relay] = scripts(buildMcpAppProxyDocument(input))

    expect(relay?.hasAttribute('nonce')).toBe(false)
  })

  it('cannot be made to break out of the attribute', () => {
    const html = buildMcpAppProxyDocument({
      ...input,
      nonce: '"><script>alert(1)</script>',
    })

    expect(scripts(html)).toHaveLength(1)
  })
})
