// The sandbox and fixed Content Security Policy that every in-chat app
// (MCP app widget) frame runs under.
//
// A widget frame may run scripts and submit its own forms. `allow-forms` lets
// a submit button, or Enter in a field, fire the form's `submit` event, so the
// widget's own handler runs. Without it the browser drops the submission
// before any event fires, and the button does nothing. The frame's CSP keeps
// `form-action 'none'`, which blocks the submission itself: no form can send
// data anywhere or navigate the frame, whatever its action or target.
//
// Every other capability stays off: an srcdoc frame keeps its opaque origin,
// and no frame may open popups, navigate the top window or show modals.
export const MCP_APP_FRAME_SANDBOX = 'allow-scripts allow-forms'

// Exporting widgets also opt into user-activated downloads. This deliberately
// omits allow-downloads-without-user-activation.
export const MCP_APP_DOWNLOAD_FRAME_SANDBOX =
  'allow-scripts allow-forms allow-downloads'

// A widget served from the dedicated widget origin keeps that origin, so it can
// reach the storage it uploads to; see `WIDGET_PAGE_FRAME_SANDBOX`.
export const DEDICATED_WIDGET_FRAME_SANDBOX =
  'allow-scripts allow-same-origin allow-forms'

export const MCP_APP_FORM_ACTION_DIRECTIVE = "form-action 'none'"

// Widgets reach the API through the host bridge. The direct-upload Pages also
// send signed, create-only PUTs directly to Google Storage; every other widget
// retains connect-src 'none'. frame-src comes from each widget's
// declared CSP (`frameDomains`), which is how the Approvals Page mounts the
// creative live preview on the render origin (AI-8076, AI-8764).
export const MCP_APP_CSP_FIXED_DIRECTIVES = [
  "default-src 'none'",
  'img-src data: blob: https://storage.googleapis.com',
  'media-src https://storage.googleapis.com',
  MCP_APP_FORM_ACTION_DIRECTIVE,
  "base-uri 'none'",
] as const

// An inline widget loads inside a host-owned proxy document
// (`buildMcpAppProxyDocument` in this package), as the `srcdoc` of the
// proxy's child frame. Two rules shape the proxy's CSP:
//
// - The browser checks the proxy's `frame-src` for every navigation of the
//   widget frame, including one the widget's own script starts. The widget
//   document itself is a `srcdoc`, which `frame-src` does not govern, so that
//   frame can only ever hold the widget document or one of the widget's
//   declared frame origins.
// - The widget document inherits the proxy's CSP on top of its own, so the
//   proxy must allow everything the widget's own policy allows.
//
// Firefox also checks a download from a `blob:` link against the proxy's
// `frame-src`, so an exporting widget's proxy adds `blob:` there. Such a widget
// could load a `blob:` document it made itself into its frame; the proxy counts
// that as a second document, stops relaying and has the host remount it.
export function mcpAppProxyCsp(
  widgetPolicy: string,
  { downloads }: { downloads: boolean },
): string {
  if (!downloads) return widgetPolicy
  const directives = widgetPolicy.split('; ')
  const frameSrc = directives.findIndex((directive) =>
    directive.startsWith('frame-src '),
  )
  const frameSources =
    frameSrc === -1
      ? []
      : directives[frameSrc]
          .slice('frame-src '.length)
          .split(' ')
          .filter((source) => source !== "'none'")
  const proxyFrameSrc = ['frame-src', 'blob:', ...frameSources].join(' ')
  return (
    frameSrc === -1
      ? [...directives, proxyFrameSrc]
      : directives.map((directive, index) =>
          index === frameSrc ? proxyFrameSrc : directive,
        )
  ).join('; ')
}
