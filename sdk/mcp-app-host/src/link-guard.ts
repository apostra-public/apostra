/**
 * Keeps a link from loading another page into an inline widget frame.
 *
 * An inline widget runs inside the host's proxy frame, whose CSP already stops
 * the widget frame loading any outside page (see `mcpAppProxyCsp` in `frame-security.ts`). A blocked
 * navigation still replaces the widget's document with the browser's error
 * page, which makes the host remount the widget and lose its state. The host
 * therefore puts this script first in every inline widget document, so a link
 * the widget renders does nothing instead.
 *
 * It cancels the default action of every link the widget renders, before any
 * widget handler runs, including an SVG link and a link in an open shadow
 * root. A widget opens a page through the host's `openLink` (see `HostLink`
 * in packages/mcp-apps/shared/host-link.tsx), so a cancelled link loses
 * nothing. A `download` link to a `blob:` or `data:` URL keeps its default,
 * which the sandbox allows only for exporting widgets; a `download` link to
 * any other URL is cancelled, because the browser ignores `download` on a
 * cross-origin URL and navigates instead. A `#section` link is cancelled too;
 * a widget scrolls to a section in script. The Navigation API cannot do this
 * job, because it fires no events in an opaque-origin document.
 */
/** The guard's script source, for a host that inserts it as a DOM element. */
export const MCP_APP_FRAME_LINK_GUARD_SCRIPT = `addEventListener('click', (event) => {
  const link = event.composedPath().find(
    (node) => node instanceof Element && node.matches('a[*|href], area[href]'),
  );
  if (!link) return;
  const href =
    link.getAttribute('href') ??
    link.getAttributeNS('http://www.w3.org/1999/xlink', 'href') ??
    '';
  if (link.hasAttribute('download') && /^\\s*(blob|data):/i.test(href)) return;
  event.preventDefault();
}, true);`

/** The guard as markup, for a host that composes the document as a string. */
export const MCP_APP_FRAME_LINK_GUARD = `<script>${MCP_APP_FRAME_LINK_GUARD_SCRIPT}</script>`
