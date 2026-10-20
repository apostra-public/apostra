// @vitest-environment jsdom

import {
  act,
  cleanup,
  fireEvent,
  render,
  screen,
  waitFor,
} from '@testing-library/react'
import { afterEach, describe, expect, it, vi } from 'vitest'

const bridgeMocks = vi.hoisted(() => {
  const instances: AppBridge[] = []
  const state: { connectError: Error | null } = { connectError: null }
  class AppBridge {
    oncalltool = async (..._args: unknown[]) => ({})
    oninitialized = (..._args: unknown[]) => undefined
    onmessage = async (..._args: unknown[]) => ({})
    onopenlink = async (..._args: unknown[]) => ({})
    onrequestteardown = (..._args: unknown[]) => undefined
    onsizechange = (..._args: unknown[]) => undefined
    onupdatemodelcontext = async (..._args: unknown[]) => ({})
    addEventListener = vi.fn()
    removeEventListener = vi.fn()
    close = vi.fn().mockResolvedValue(undefined)
    connect = vi.fn(() =>
      state.connectError
        ? Promise.reject(state.connectError)
        : Promise.resolve(undefined),
    )
    sendToolInput = vi.fn()
    sendToolResult = vi.fn()
    setHostContext = vi.fn()
    teardownResource = vi.fn().mockResolvedValue(undefined)

    constructor() {
      instances.push(this)
    }
  }
  return { AppBridge, instances, state }
})

vi.mock('@modelcontextprotocol/ext-apps/app-bridge', () => ({
  AppBridge: bridgeMocks.AppBridge,
  PostMessageTransport: class {},
  buildAllowAttribute: (permissions: Record<string, unknown> | undefined) =>
    permissions ? Object.keys(permissions).join('; ') : '',
}))

import { HostedMcpAppFrame } from '../hosted-mcp-app'
import { MCP_APP_FRAME_LINK_GUARD_SCRIPT } from '../link-guard'
import {
  buildMcpAppProxyDocument,
  MCP_APP_DOCUMENT_LEAVING_NOTICE_SCRIPT,
  MCP_APP_DOCUMENT_REPLACED_MESSAGE,
} from '../proxy-document'

afterEach(() => {
  cleanup()
  bridgeMocks.instances.length = 0
  bridgeMocks.state.connectError = null
})

const directive = {
  kind: 'client-review',
  resourceUri: 'ui://client.example/review/mcp-app.html',
  title: 'Client review',
  data: { revision: 3 },
}

describe('HostedMcpAppFrame', () => {
  it('starts the host bridge before iframe load and keeps the directive isolated', async () => {
    const loadResource = vi
      .fn()
      .mockResolvedValue('<!doctype html><html><body>Review</body></html>')
    const { unmount } = render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={loadResource}
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
      />,
    )

    const frame = await screen.findByTitle('Client review')
    expect(frame.getAttribute('sandbox')).toBe('allow-scripts')
    expect(frame.getAttribute('referrerpolicy')).toBe('no-referrer')
    expect(frame.getAttribute('srcdoc')).toContain("connect-src 'none'")
    expect(frame.hasAttribute('allow')).toBe(false)
    expect(loadResource).toHaveBeenCalledWith(
      directive.resourceUri,
      expect.any(AbortSignal),
    )
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))
    expect(bridgeMocks.instances[0]?.connect).toHaveBeenCalledOnce()

    // A duplicate load event must not replace the bridge that was already
    // listening when the embedded app sent its initialization request.
    fireEvent.load(frame)
    expect(bridgeMocks.instances).toHaveLength(1)

    unmount()
    expect(bridgeMocks.instances[0]?.teardownResource).toHaveBeenCalledOnce()
  })

  it('frames the widget page a resource names when the host opts in', async () => {
    const meta = {
      'scope3/widget-page': {
        url: 'https://widgets.apostra.com/library/mcp-app.html',
        appearanceParams: ['color-scheme', 'product-brand'],
      },
    }
    render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={() =>
          Promise.resolve({
            html: '<!doctype html><html><body>Review</body></html>',
            meta,
          })
        }
        widgetPage={{
          appearance: { colorScheme: 'dark', productBrand: 'new' },
          allowedOrigins: ['https://widgets.apostra.com'],
        }}
        createHostContext={() => ({ theme: 'dark' })}
        handlers={{}}
      />,
    )

    const frame = await screen.findByTitle('Client review')
    expect(frame.getAttribute('src')).toBe(
      'https://widgets.apostra.com/library/mcp-app.html?color-scheme=dark&product-brand=new',
    )
    expect(frame.hasAttribute('srcdoc')).toBe(false)
    expect(frame.getAttribute('sandbox')).toBe(
      'allow-scripts allow-same-origin allow-forms',
    )
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))
    expect(bridgeMocks.instances[0]?.connect).toHaveBeenCalledOnce()
  })

  it('renders the HTML when the resource names a page but the host did not opt in', async () => {
    render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={() =>
          Promise.resolve({
            html: '<!doctype html><html><body>Review</body></html>',
            meta: {
              'scope3/widget-page': {
                url: 'https://widgets.apostra.com/library/mcp-app.html',
                appearanceParams: [],
              },
            },
          })
        }
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
      />,
    )

    const frame = await screen.findByTitle('Client review')
    expect(frame.hasAttribute('src')).toBe(false)
    expect(frame.getAttribute('srcdoc')).toContain('Review')
    expect(frame.getAttribute('sandbox')).toBe('allow-scripts')
  })

  it('grants only host-approved origins and permissions', async () => {
    render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={() =>
          Promise.resolve({
            html: '<!doctype html><html><body>Review</body></html>',
            csp: {
              connectDomains: [
                'https://approved.example',
                'https://unapproved.example',
                'javascript:alert(1)',
              ],
              resourceDomains: ['https://approved.example'],
              baseUriDomains: ['https://approved.example'],
            },
            permissions: { camera: {}, clipboardWrite: {} },
          })
        }
        approveResourceOrigin={(origin) =>
          origin === 'https://approved.example'
        }
        approvedPermissions={{ clipboardWrite: {} }}
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
      />,
    )

    const frame = await screen.findByTitle('Client review')
    const srcDoc = frame.getAttribute('srcdoc') ?? ''
    expect(srcDoc).toContain('connect-src https://approved.example')
    expect(srcDoc).toContain(
      "script-src 'unsafe-inline' https://approved.example",
    )
    expect(srcDoc).toContain('base-uri https://approved.example')
    expect(srcDoc.match(/worker-src 'none'/g)).toHaveLength(2)
    expect(srcDoc).not.toContain('https://unapproved.example')
    expect(srcDoc).not.toContain('javascript:')
    expect(frame.getAttribute('allow')).toBe('clipboardWrite')
  })

  it('places CSP before scripts hidden ahead of an author-supplied head', async () => {
    render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={() =>
          Promise.resolve(
            '<!-- <head> --><script>window.early = true</script><head><title>Hostile</title></head><body><template><head></head></template>Review</body>',
          )
        }
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
      />,
    )

    const frame = await screen.findByTitle('Client review')
    const parsed = new DOMParser().parseFromString(
      frame.getAttribute('srcdoc') ?? '',
      'text/html',
    )
    const payload = parsed.querySelector<HTMLTextAreaElement>(
      '#agent-mcp-app-document',
    )
    const appDocument = new DOMParser().parseFromString(
      payload?.value ?? '',
      'text/html',
    )
    expect(appDocument.head.firstElementChild?.tagName).toBe('META')
    expect(appDocument.head.firstElementChild?.getAttribute('http-equiv')).toBe(
      'Content-Security-Policy',
    )
    // The link guard runs next, before any app script: a srcdoc app resolves
    // even `#section` links against the host page.
    expect(appDocument.head.children[1]?.tagName).toBe('SCRIPT')
    expect(appDocument.head.children[1]?.textContent).toBe(
      MCP_APP_FRAME_LINK_GUARD_SCRIPT,
    )
    // So does the leaving notice, which retires the proxy before any
    // replacement document can use the bridge.
    expect(appDocument.head.children[2]?.textContent).toBe(
      MCP_APP_DOCUMENT_LEAVING_NOTICE_SCRIPT,
    )
    // The proxy script creates the app frame with this sandbox.
    expect(parsed.body.querySelector('script')?.textContent).toContain(
      `frame.setAttribute('sandbox', "allow-scripts")`,
    )
    // The app is the frame's srcdoc, never a blob: URL, so it stays a secure
    // context inside the opaque-origin proxy, and the proxy frames nothing else.
    expect(parsed.body.querySelector('script')?.textContent).toContain(
      'frame.srcdoc = payload.value',
    )
    expect(parsed.body.querySelector('script')?.textContent).not.toContain(
      'createObjectURL',
    )
    expect(parsed.head.firstElementChild?.getAttribute('content')).toContain(
      "frame-src 'none'",
    )
  })

  it('shows its error with Retry once the proxy retires a replaced app document', async () => {
    render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={() => Promise.resolve('<p>Review</p>')}
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
        loadErrorMessage="This app stopped responding."
      />,
    )
    const frame = (await screen.findByTitle(
      'Client review',
    )) as HTMLIFrameElement

    // The same message from any other window is ignored.
    act(() => {
      window.dispatchEvent(
        new MessageEvent('message', {
          data: { type: MCP_APP_DOCUMENT_REPLACED_MESSAGE },
          source: window,
        }),
      )
    })
    expect(screen.queryByText('This app stopped responding.')).toBeNull()

    act(() => {
      window.dispatchEvent(
        new MessageEvent('message', {
          data: { type: MCP_APP_DOCUMENT_REPLACED_MESSAGE },
          source: frame.contentWindow,
        }),
      )
    })
    expect(await screen.findByText('This app stopped responding.')).toBeTruthy()
    expect(screen.getByRole('button', { name: 'Retry' })).toBeTruthy()
  })

  it('aborts a retired resource load', () => {
    let signal: AbortSignal | undefined
    const loadResource = vi.fn((_uri: string, nextSignal: AbortSignal) => {
      signal = nextSignal
      return new Promise<string>(() => undefined)
    })
    const { unmount } = render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={loadResource}
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
      />,
    )

    unmount()
    expect(signal?.aborted).toBe(true)
  })

  it('aborts a resource load that misses its deadline and exposes retry', async () => {
    let signal: AbortSignal | undefined
    render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={(_uri, nextSignal) => {
          signal = nextSignal
          return new Promise<string>(() => undefined)
        }}
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
        resourceLoadTimeoutMs={1}
      />,
    )

    await waitFor(() => {
      expect(signal?.aborted).toBe(true)
      expect(screen.getByText('This Task could not be loaded.')).toBeTruthy()
      expect(screen.getByRole('button', { name: 'Retry' })).toBeTruthy()
    })
  })

  it('ignores a late failure from a retired resource load', async () => {
    let rejectRetired: ((reason: Error) => void) | undefined
    const loadResource = vi.fn((resourceUri: string) => {
      if (resourceUri === directive.resourceUri) {
        return new Promise<string>((_resolve, reject) => {
          rejectRetired = reject
        })
      }
      return Promise.resolve('<!doctype html><html><body>Active</body></html>')
    })
    const activeDirective = {
      ...directive,
      resourceUri: 'ui://client.example/active/mcp-app.html',
      title: 'Active client review',
    }
    const sharedProps = {
      loadResource,
      createHostContext: () => ({ theme: 'light' as const }),
      handlers: {},
    }
    const { rerender } = render(
      <HostedMcpAppFrame directive={directive} {...sharedProps} />,
    )

    rerender(<HostedMcpAppFrame directive={activeDirective} {...sharedProps} />)
    await screen.findByTitle(activeDirective.title)
    rejectRetired?.(new Error('retired request failed late'))

    await waitFor(() => {
      expect(screen.queryByText('This Task could not be loaded.')).toBeNull()
    })
  })

  it('uses iframe load as a fallback when contentWindow is late', async () => {
    let frameReady = false
    const contentWindow = vi
      .spyOn(HTMLIFrameElement.prototype, 'contentWindow', 'get')
      .mockImplementation(() => (frameReady ? window : null))
    try {
      render(
        <HostedMcpAppFrame
          directive={directive}
          loadResource={() =>
            Promise.resolve('<!doctype html><html><body>Review</body></html>')
          }
          createHostContext={() => ({ theme: 'light' })}
          handlers={{}}
        />,
      )

      const frame = await screen.findByTitle(directive.title)
      expect(bridgeMocks.instances).toHaveLength(0)
      // Some environments emit an early load before contentWindow is exposed.
      // A subsequent ready load must still re-arm bridge initialization.
      fireEvent.load(frame)
      expect(bridgeMocks.instances).toHaveLength(0)
      frameReady = true
      fireEvent.load(frame)

      await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))
    } finally {
      contentWindow.mockRestore()
    }
  })

  it('waits for a replacement frame to load after context changes', async () => {
    let frameReady = true
    const contentWindow = vi
      .spyOn(HTMLIFrameElement.prototype, 'contentWindow', 'get')
      .mockImplementation(() => (frameReady ? window : null))
    const sharedProps = {
      directive,
      loadResource: () =>
        Promise.resolve('<!doctype html><html><body>Review</body></html>'),
      createHostContext: () => ({ theme: 'light' as const }),
      handlers: {},
    }
    try {
      const { rerender } = render(
        <HostedMcpAppFrame {...sharedProps} contextKey="first" />,
      )
      const firstFrame = await screen.findByTitle(directive.title)
      await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))

      frameReady = false
      rerender(<HostedMcpAppFrame {...sharedProps} contextKey="second" />)
      const replacementFrame = await screen.findByTitle(directive.title)
      expect(replacementFrame).not.toBe(firstFrame)
      expect(bridgeMocks.instances).toHaveLength(1)

      frameReady = true
      fireEvent.load(replacementFrame)
      await waitFor(() => expect(bridgeMocks.instances).toHaveLength(2))
    } finally {
      contentWindow.mockRestore()
    }
  })

  it('replaces and reconnects the bridge when transformed HTML changes', async () => {
    let frameReady = true
    const contentWindow = vi
      .spyOn(HTMLIFrameElement.prototype, 'contentWindow', 'get')
      .mockImplementation(() => (frameReady ? window : null))
    const sharedProps = {
      directive,
      loadResource: () =>
        Promise.resolve('<!doctype html><html><body>Review</body></html>'),
      createHostContext: () => ({ theme: 'light' as const }),
      handlers: {},
    }
    try {
      const { rerender } = render(
        <HostedMcpAppFrame
          {...sharedProps}
          transformHtml={(value) =>
            value.replace('</body>', '<p>first</p></body>')
          }
        />,
      )
      const firstFrame = await screen.findByTitle(directive.title)
      await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))

      frameReady = false
      rerender(
        <HostedMcpAppFrame
          {...sharedProps}
          transformHtml={(value) =>
            value.replace('</body>', '<p>second</p></body>')
          }
        />,
      )
      const replacementFrame = await screen.findByTitle(directive.title)
      expect(replacementFrame).not.toBe(firstFrame)
      expect(bridgeMocks.instances[0]?.teardownResource).toHaveBeenCalledOnce()
      expect(bridgeMocks.instances).toHaveLength(1)

      frameReady = true
      fireEvent.load(replacementFrame)
      await waitFor(() => expect(bridgeMocks.instances).toHaveLength(2))
    } finally {
      contentWindow.mockRestore()
    }
  })

  it('replaces and reconnects the bridge when directive data changes', async () => {
    const sharedProps = {
      loadResource: () =>
        Promise.resolve('<!doctype html><html><body>Review</body></html>'),
      createHostContext: () => ({ theme: 'light' as const }),
      handlers: {},
    }
    const { rerender } = render(
      <HostedMcpAppFrame directive={directive} {...sharedProps} />,
    )
    const firstFrame = await screen.findByTitle(directive.title)
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))

    const updatedDirective = { ...directive, data: { revision: 4 } }
    rerender(
      <HostedMcpAppFrame directive={updatedDirective} {...sharedProps} />,
    )
    const replacementFrame = await screen.findByTitle(directive.title)
    expect(replacementFrame).not.toBe(firstFrame)
    expect(bridgeMocks.instances[0]?.teardownResource).toHaveBeenCalledOnce()

    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(2))
    bridgeMocks.instances[1]?.oninitialized()
    expect(bridgeMocks.instances[1]?.sendToolInput).toHaveBeenCalledWith({
      arguments: { revision: 4 },
    })
    expect(bridgeMocks.instances[1]?.sendToolResult).toHaveBeenCalledWith({
      content: [],
      structuredContent: { revision: 4 },
    })
  })

  it("delivers the launch result's _meta with its structured content", async () => {
    const meta = {
      'scope3/storefront-v3-page-capability': 'fixture-signed-capability',
    }
    render(
      <HostedMcpAppFrame
        directive={{ ...directive, meta }}
        loadResource={() =>
          Promise.resolve('<!doctype html><html><body>Review</body></html>')
        }
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
      />,
    )
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))
    bridgeMocks.instances[0]?.oninitialized()

    expect(bridgeMocks.instances[0]?.sendToolResult).toHaveBeenCalledWith({
      content: [],
      structuredContent: { revision: 3 },
      _meta: meta,
    })
  })

  it('replaces and reconnects the bridge when the launch _meta changes', async () => {
    const sharedProps = {
      loadResource: () =>
        Promise.resolve('<!doctype html><html><body>Review</body></html>'),
      createHostContext: () => ({ theme: 'light' as const }),
      handlers: {},
    }
    const { rerender } = render(
      <HostedMcpAppFrame
        directive={{ ...directive, meta: { capability: 'first' } }}
        {...sharedProps}
      />,
    )
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))

    rerender(
      <HostedMcpAppFrame
        directive={{ ...directive, meta: { capability: 'second' } }}
        {...sharedProps}
      />,
    )
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(2))
    bridgeMocks.instances[1]?.oninitialized()
    expect(bridgeMocks.instances[1]?.sendToolResult).toHaveBeenCalledWith({
      content: [],
      structuredContent: { revision: 3 },
      _meta: { capability: 'second' },
    })
  })

  it('ignores size changes from a retired bridge', async () => {
    const sharedProps = {
      directive,
      loadResource: () =>
        Promise.resolve('<!doctype html><html><body>Review</body></html>'),
      createHostContext: () => ({ theme: 'light' as const }),
      handlers: {},
    }
    const { rerender } = render(
      <HostedMcpAppFrame {...sharedProps} contextKey="first" />,
    )
    await screen.findByTitle(directive.title)
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))

    rerender(<HostedMcpAppFrame {...sharedProps} contextKey="second" />)
    const replacementFrame = await screen.findByTitle(directive.title)
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(2))

    act(() => bridgeMocks.instances[1]?.onsizechange({ height: 320 }))
    expect(replacementFrame.style.height).toBe('320px')
    act(() => bridgeMocks.instances[0]?.onsizechange({ height: 700 }))
    expect(replacementFrame.style.height).toBe('320px')
  })

  it('revokes a bridge that misses its initialization deadline', async () => {
    render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={() =>
          Promise.resolve('<!doctype html><html><body>Review</body></html>')
        }
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
        initializationTimeoutMs={1}
      />,
    )
    await screen.findByTitle(directive.title)
    await waitFor(() => expect(bridgeMocks.instances).toHaveLength(1))
    await waitFor(() => {
      expect(bridgeMocks.instances[0]?.teardownResource).toHaveBeenCalledOnce()
      expect(screen.getByText('This Task did not initialize.')).toBeTruthy()
    })

    bridgeMocks.instances[0]?.oninitialized()
    expect(screen.getByText('This Task did not initialize.')).toBeTruthy()
  })

  it('revokes a partially connected bridge when initialization rejects', async () => {
    bridgeMocks.state.connectError = new Error('connection rejected')
    render(
      <HostedMcpAppFrame
        directive={directive}
        loadResource={() =>
          Promise.resolve('<!doctype html><html><body>Review</body></html>')
        }
        createHostContext={() => ({ theme: 'light' })}
        handlers={{}}
      />,
    )
    await screen.findByTitle(directive.title)

    await waitFor(() => {
      expect(bridgeMocks.instances[0]?.teardownResource).toHaveBeenCalledOnce()
      expect(screen.getByText('This Task did not initialize.')).toBeTruthy()
    })
  })
})

describe('buildMcpAppProxyDocument', () => {
  it('paints only a light or dark colour scheme', () => {
    const build = (colorScheme: unknown) =>
      buildMcpAppProxyDocument({
        appDocument: '<p>app</p>',
        policy: "default-src 'none'",
        sandbox: 'allow-scripts',
        colorScheme: colorScheme as 'light',
      })
    expect(build('dark')).toContain(':root{color-scheme:dark}')
    expect(build('red}body{display:none')).not.toContain('color-scheme')
  })

  it("retires on the app's leaving notice and never relays the app's own replaced message", () => {
    const relay = buildMcpAppProxyDocument({
      appDocument: '<p>app</p>',
      policy: "default-src 'none'",
      sandbox: 'allow-scripts',
    })
    expect(relay).toContain(
      'if (type === "agent-host:mcp-app-document-leaving") retire();',
    )
    expect(relay).toContain(
      'else if (type !== "agent-host:mcp-app-document-replaced")',
    )
  })
})
