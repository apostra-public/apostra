# @apostra/mcp-app-host

The host side of MCP Apps for Apostra widgets. It lets a host built outside
Apostra render a V3 widget without reimplementing the bridge, the proxy
document or the frame sandbox. It is plain TypeScript with no React, MUI or
design-system dependency. A React frame lives in a separate `./react` subpath
that takes `react` as an optional peer dependency. Requires Node.js 22.18 or
later for tooling; the runtime code runs in the browser.

```bash
npm install @apostra/mcp-app-host
```

TypeScript: the package's declarations depend on the MCP SDK, whose own
declarations name Node's `Buffer`. A browser project with `skipLibCheck`
(the Vite and Next.js default) needs nothing more. To check every library
declaration, install `@types/node` and add `"node"` to `compilerOptions.types`.

Read [Build an MCP Apps host](https://docs.apostra.com/v3/mcp-apps-host) for
the contract a host must meet. The source is mirrored at
[apostra-public/apostra](https://github.com/apostra-public/apostra/tree/main/sdk/mcp-app-host).

## What it holds

| Export | Role |
|--------|------|
| `createAgentMcpAppBridge` | The ext-apps 2.x host bridge for one iframe: tool calls with a bounded deadline and cancellation, `ui/message`, `ui/update-model-context`, `ui/open-link`, size changes, logging, and bounded teardown. Result `_meta` passes through untouched, so a `_scope3PageCapability` a tool returns reaches the widget. Pass `targetOrigin` to accept messages only from one exact HTTPS origin. |
| `resolveMcpAppFrame` | Decides how to render a resource: frame its `scope3/widget-page` when it names one on an origin you trust, else render its HTML as a `srcdoc`. |
| `widgetPageFrame`, `readWidgetPageMeta` | The page half of that decision, for a host that frames pages only. |
| `buildHostedMcpAppSrcDoc` | The `srcdoc` path: a CSP built from the resource's `_meta.ui.csp` (`connectDomains`, `resourceDomains`, `frameDomains`, `baseUriDomains`), granting only the origins your `approveResourceOrigin` accepts, plus the link guard and leaving notice, inside a host-owned proxy document. |
| `buildMcpAppProxyDocument` | The proxy document itself: it relays bridge messages and retires the app if its frame loads a second document. |
| `MCP_APP_FRAME_LINK_GUARD`, `MCP_APP_FRAME_LINK_GUARD_SCRIPT` | Cancels every link the widget renders, so a stray link cannot replace the widget document. |
| `MCP_APP_FRAME_SANDBOX`, `MCP_APP_DOWNLOAD_FRAME_SANDBOX`, `WIDGET_PAGE_FRAME_SANDBOX`, `mcpAppProxyCsp` and the fixed CSP directives | The sandbox flags and CSP pieces Apostra's own web app uses (`./frame-security` for just these). |
| `HostedMcpAppFrame` (`./react`) | A React frame that owns resource loading, the iframe, bridge initialization, sizing, retry and teardown. |

## Render a V3 widget

1. Call the tool that opens the widget, then `resources/read` its
   `ui://...` resource. On V3 the resource's `_meta` may carry
   `scope3/widget-page`: `{ url, appearanceParams }`, the widget's page on
   Apostra's widget origin (`widgets.apostra.com`, staging
   `widgets.staging.apostra.com`). A resource carries the key only where the API
   publishes a page for it, so always handle its absence.
2. Ask the package how to frame it:

   ```ts
   import {
     APOSTRA_WIDGET_PAGE_ORIGINS,
     createAgentMcpAppBridge,
     resolveMcpAppFrame,
   } from '@apostra/mcp-app-host'

   const frame = resolveMcpAppFrame({
     meta: resource._meta,
     html: resource.text, // the fallback; omit it if you only frame pages
     page: {
       appearance: { colorScheme: 'light', productBrand: 'new' },
       allowedOrigins: APOSTRA_WIDGET_PAGE_ORIGINS,
     },
     approveResourceOrigin: (origin, directive) => /* your policy */ false,
   })
   ```

3. Render it and connect the bridge:

   ```ts
   const iframe = document.createElement('iframe')
   iframe.setAttribute('sandbox', frame.sandbox)
   if (frame.kind === 'page') iframe.src = frame.src
   else {
     iframe.srcdoc = frame.srcDoc
     if (frame.allow) iframe.allow = frame.allow
   }
   container.append(iframe)

   const hosted = createAgentMcpAppBridge({
     targetWindow: iframe.contentWindow as Window,
     targetOrigin: frame.targetOrigin, // set for a page, undefined for srcdoc
     hostContext: { theme: 'light' },
     handlers: { onCallTool, onMessage, onUpdateModelContext, onOpenLink },
   })
   await hosted.connect()
   ```

   Create the bridge before the document loads so it is listening when the
   widget sends `ui/initialize`. After `onInitialized`, send the launch
   result with `hosted.bridge.sendToolInput` and `sendToolResult`. Call
   `hosted.close()` when you remove the frame.

   In React, `HostedMcpAppFrame` from `@apostra/mcp-app-host/react` does steps 2
   and 3 for you. Give it the launch result as
   `directive={{ resourceUri, title, data: result.structuredContent, meta: result._meta }}`:
   a V3 widget reads its page capability from that `_meta` and shows a launch
   failure without it. Pass `widgetPage={{ appearance, allowedOrigins }}` and
   return the resource's `_meta` from `loadResource` to opt in to pages.

### How the two paths differ

- **Page.** `src` is the page URL with only the appearance parameters the
  resource lists (`color-scheme`, `product-brand`, `host-corner`). The sandbox
  is `allow-scripts allow-same-origin allow-forms`, because the page needs its
  real origin to upload straight to storage; a `srcdoc` frame has the opaque
  origin `null`, which no bucket allows. The bridge must be created with
  `targetOrigin`, so it accepts messages only from that exact origin. The page
  holds no cookies or session; every tool call still goes through your bridge.
- **Srcdoc.** The widget runs in a proxy document with the sandbox
  `allow-scripts`. Apostra's own web app also grants `allow-forms`, and
  `allow-downloads` to exporting widgets; see `frame-security.ts` for why. It has no origin, so create the bridge without `targetOrigin`.
- **A page URL is only used from an origin you list.** `allowedOrigins` is
  required, not defaulted: framing a page with `allow-same-origin` hands it its
  own origin, so a resource from a server you do not control must not be able
  to choose it. A resource whose page is on another origin, is not `https`, or
  carries a query, credentials or fragment falls back to the HTML.

### Rules for the host

- **Route app-only tools only from the widget.** Tools declared with
  `_meta.ui.visibility: ['app']` are Page-bound: keep them out of the model's
  tool list and call them only for a `tools/call` that arrives over the bridge
  from the widget. A model must never be able to call them.
- **Use the same principal for launch and app calls.** The widget's tool calls
  run as the user and account that launched it. Send them with the same
  credentials and account context as the tool call that opened the widget, and
  do not let a widget call act for another account.
- **Let the host decide what a link may open.** The widget never opens a page
  itself; it calls the host's `ui/open-link`. Validate the URL in `onOpenLink`
  (allow `http:` and `https:`, open it with no opener) and refuse the rest.
- **Grant CSP origins from policy, not from the resource.** `_meta.ui.csp`
  declares what a widget asks for; `approveResourceOrigin` decides what it gets.
  With no callback a widget gets no network or extra resource origins.
