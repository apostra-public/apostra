/**
 * The message a proxy document posts to its host when its app document is
 * leaving or its frame loads a second document. The host should retire its
 * bridge and remount the app.
 */
export const MCP_APP_DOCUMENT_REPLACED_MESSAGE =
  'agent-host:mcp-app-document-replaced'

/** The message an app document posts to its proxy as it unloads. */
export const MCP_APP_DOCUMENT_LEAVING_MESSAGE =
  'agent-host:mcp-app-document-leaving'

/**
 * Tells the proxy that the app document is leaving its frame. A host puts it
 * first in every app document, before any app script, beside the link guard.
 * `beforeunload` runs in the old document before a navigation commits, so its
 * message reaches the proxy before anything a replacement document posts, and
 * the proxy stops relaying before a replacement can use the bridge, however
 * long that page takes to load. (Chrome runs `pagehide` only after a
 * cross-process navigation commits, too late on its own; it stays as a
 * backstop.) The parent is captured here, before app script could shadow
 * `window.parent`.
 */
export const MCP_APP_DOCUMENT_LEAVING_NOTICE_SCRIPT = `(() => {
  const proxy = parent;
  const leaving = () =>
    proxy.postMessage({ type: ${JSON.stringify(MCP_APP_DOCUMENT_LEAVING_MESSAGE)} }, '*');
  addEventListener('beforeunload', leaving);
  addEventListener('pagehide', leaving);
})();`

export interface McpAppProxyDocumentInput {
  /** The complete app document, CSP included. */
  appDocument: string
  /**
   * The proxy document's own CSP. Its `frame-src` decides where the app frame
   * may navigate, because a browser checks the parent's `frame-src` for every
   * navigation of a child frame, including one the child starts itself. The
   * app document is the frame's `srcdoc`, which no `frame-src` governs, so the
   * proxy needs no source for it. The app document inherits this policy on top
   * of its own, so allow everything the app's policy allows and nothing more.
   */
  policy: string
  /** The app frame's sandbox. It may not grant more than the host frame's. */
  sandbox: string
  /** The app frame's permissions policy (`allow`). */
  allow?: string
  /** Pins the proxy canvas to the host's colour scheme. */
  colorScheme?: 'light' | 'dark'
}

/**
 * Builds a host-owned proxy document that loads an MCP app as the `srcdoc` of a
 * child frame and relays bridge messages between the host and the app.
 *
 * The host's bridge talks to the proxy's window, which the app cannot replace:
 * the proxy has no links or app script, and the app frame's sandbox stops it
 * and any frame inside it from navigating an ancestor. The proxy's `frame-src`
 * keeps the app frame itself to the pages `policy` allows. When the app
 * document announces it is leaving (`MCP_APP_DOCUMENT_LEAVING_NOTICE_SCRIPT`),
 * or the app frame loads a second document, the proxy stops relaying in both
 * directions and posts `MCP_APP_DOCUMENT_REPLACED_MESSAGE` to the host.
 */
export function buildMcpAppProxyDocument(
  input: McpAppProxyDocumentInput,
): string {
  const colorScheme =
    input.colorScheme === 'light' || input.colorScheme === 'dark'
      ? input.colorScheme
      : undefined
  const style = `${colorScheme ? `:root{color-scheme:${colorScheme}}` : ''}html,body,#agent-mcp-app{width:100%;height:100%;margin:0;border:0;overflow:hidden}`

  // The script creates the app frame with its `srcdoc` already set, so the
  // first load event a browser fires is the app document's own, never an
  // initial `about:blank`. That keeps the second-document count exact. A
  // `srcdoc` document stays a secure context inside the opaque-origin proxy,
  // so `crypto.randomUUID`, `crypto.subtle` and the clipboard keep working; a
  // `blob:` URL created here is not one in current Chrome. An app that reloads
  // itself reloads this same document, which also retires the proxy. The app's
  // leaving notice is consumed here and never relayed, and the proxy never
  // relays an app's own replaced message, so only the proxy can trigger it.
  const relay = `(() => {
    const payload = document.getElementById('agent-mcp-app-document');
    if (!(payload instanceof HTMLTextAreaElement)) return;
    const frame = document.createElement('iframe');
    frame.id = 'agent-mcp-app';
    frame.title = 'Hosted agent app';
    frame.setAttribute('sandbox', ${scriptString(input.sandbox)});
    ${input.allow ? `frame.setAttribute('allow', ${scriptString(input.allow)});` : ''}
    let retired = false;
    const retire = () => {
      if (retired) return;
      retired = true;
      parent.postMessage({ type: ${scriptString(MCP_APP_DOCUMENT_REPLACED_MESSAGE)} }, '*');
    };
    let loads = 0;
    frame.addEventListener('load', () => {
      loads += 1;
      if (loads > 1) retire();
    });
    frame.srcdoc = payload.value;
    payload.remove();
    document.body.append(frame);
    addEventListener('message', (event) => {
      if (retired) return;
      if (event.source === parent) {
        frame.contentWindow?.postMessage(event.data, '*');
        return;
      }
      if (event.source !== frame.contentWindow) return;
      const type = event.data?.type;
      if (type === ${scriptString(MCP_APP_DOCUMENT_LEAVING_MESSAGE)}) retire();
      else if (type !== ${scriptString(MCP_APP_DOCUMENT_REPLACED_MESSAGE)}) parent.postMessage(event.data, '*');
    });
  })();`
  return `<!doctype html><html><head><meta http-equiv="Content-Security-Policy" content="${escapeAttribute(input.policy)}"><style>${style}</style></head><body><textarea id="agent-mcp-app-document" hidden="">${escapeText(input.appDocument)}</textarea><script>${relay}</script></body></html>`
}

function escapeText(value: string): string {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
}

function escapeAttribute(value: string): string {
  return value.replaceAll('&', '&amp;').replaceAll('"', '&quot;')
}

// A JavaScript string literal that cannot close the surrounding script element.
function scriptString(value: string): string {
  return JSON.stringify(value).replaceAll('<', '\\u003c')
}
