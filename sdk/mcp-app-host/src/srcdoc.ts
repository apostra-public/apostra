import {
  buildAllowAttribute,
  type McpUiResourceCsp,
  type McpUiResourcePermissions,
} from '@modelcontextprotocol/ext-apps/app-bridge'

import { MCP_APP_FRAME_LINK_GUARD_SCRIPT } from './link-guard.js'
import {
  buildMcpAppProxyDocument,
  MCP_APP_DOCUMENT_LEAVING_NOTICE_SCRIPT,
} from './proxy-document.js'

/**
 * Decides whether the host grants an origin a widget asked for in its resource
 * `_meta.ui.csp`. A widget never widens its own policy: an origin is granted
 * only when this returns true.
 */
export type ApproveResourceOrigin = (
  origin: string,
  directive: keyof McpUiResourceCsp,
) => boolean

const permissionNames = [
  'camera',
  'microphone',
  'geolocation',
  'clipboardWrite',
] as const satisfies ReadonlyArray<keyof McpUiResourcePermissions>

/** The permissions both the widget requested and the host approved. */
export function intersectPermissions(
  requested: McpUiResourcePermissions | undefined,
  approved: McpUiResourcePermissions | undefined,
): McpUiResourcePermissions | undefined {
  if (!requested || !approved) return undefined
  const permissions: McpUiResourcePermissions = {}
  for (const name of permissionNames) {
    if (requested[name] && approved[name]) permissions[name] = {}
  }
  return Object.keys(permissions).length ? permissions : undefined
}

/** The `allow` attribute for the permissions both sides agree on. */
export function allowAttributeFor(
  requested: McpUiResourcePermissions | undefined,
  approved: McpUiResourcePermissions | undefined,
): string {
  return buildAllowAttribute(intersectPermissions(requested, approved))
}

function approvedOrigins(
  origins: string[] | undefined,
  directive: keyof McpUiResourceCsp,
  approve: ApproveResourceOrigin | undefined,
): string[] {
  if (!origins || !approve) return []
  return origins.filter(
    (origin) => isValidCspOrigin(origin) && approve(origin, directive),
  )
}

function isValidCspOrigin(origin: string): boolean {
  const wildcard = origin.match(/^(https:|wss:)\/\/\*\.([a-z0-9.-]+)$/i)
  if (wildcard) return !wildcard[2].includes('..')
  try {
    const parsed = new URL(origin)
    return (
      (parsed.protocol === 'https:' || parsed.protocol === 'wss:') &&
      parsed.origin === origin
    )
  } catch {
    return false
  }
}

function cspSources(sources: string[]): string {
  return sources.length ? sources.join(' ') : "'none'"
}

export interface ApprovedResourcePolicy {
  connect: string[]
  resources: string[]
  frames: string[]
  bases: string[]
}

/**
 * The origins from a resource's `_meta.ui.csp` (`connectDomains`,
 * `resourceDomains`, `frameDomains`, `baseUriDomains`) that the host approves
 * and that are well-formed `https:` or `wss:` origins.
 */
export function approvedResourcePolicy(
  requested: McpUiResourceCsp | undefined,
  approve: ApproveResourceOrigin | undefined,
): ApprovedResourcePolicy {
  return {
    connect: approvedOrigins(
      requested?.connectDomains,
      'connectDomains',
      approve,
    ),
    resources: approvedOrigins(
      requested?.resourceDomains,
      'resourceDomains',
      approve,
    ),
    frames: approvedOrigins(requested?.frameDomains, 'frameDomains', approve),
    bases: approvedOrigins(
      requested?.baseUriDomains,
      'baseUriDomains',
      approve,
    ),
  }
}

/** The CSP directives for a widget document, from the approved origins. */
export function resourcePolicyDirectives(
  approved: ApprovedResourcePolicy,
): string[] {
  return [
    "default-src 'none'",
    `script-src 'unsafe-inline' ${approved.resources.join(' ')}`.trim(),
    `style-src 'unsafe-inline' ${approved.resources.join(' ')}`.trim(),
    `img-src ${cspSources(['data:', 'blob:', ...approved.resources])}`,
    `font-src ${cspSources(['data:', ...approved.resources])}`,
    `media-src ${cspSources(['data:', 'blob:', ...approved.resources])}`,
    `connect-src ${cspSources(approved.connect)}`,
    `frame-src ${cspSources(approved.frames)}`,
    `base-uri ${cspSources(approved.bases)}`,
    "worker-src 'none'",
    "form-action 'none'",
    "object-src 'none'",
  ]
}

function addContentSecurityPolicy(
  html: string,
  approved: ApprovedResourcePolicy,
): string {
  const policy = resourcePolicyDirectives(approved).join('; ')
  const parsed = new DOMParser().parseFromString(html, 'text/html')
  const meta = parsed.createElement('meta')
  meta.httpEquiv = 'Content-Security-Policy'
  meta.content = policy

  // Parse first, then serialise a fresh host-owned document with the policy as
  // the first real head element. Inserting into an author-supplied `<head>` by
  // string replacement lets scripts before that token execute before the CSP.
  // The link guard and the leaving notice run next, before any app script:
  // the app is the proxy frame's `srcdoc`, so even a `#section` link resolves
  // against the host page and would navigate the frame rather than scroll, and
  // the notice retires the proxy before a replacement document can use it.
  const linkGuard = parsed.createElement('script')
  linkGuard.textContent = MCP_APP_FRAME_LINK_GUARD_SCRIPT
  const leavingNotice = parsed.createElement('script')
  leavingNotice.textContent = MCP_APP_DOCUMENT_LEAVING_NOTICE_SCRIPT
  parsed.head.prepend(meta, linkGuard, leavingNotice)
  return `<!doctype html>${parsed.documentElement.outerHTML}`
}

/** The sandbox of a hosted app frame built from `buildHostedMcpAppSrcDoc`. */
export const HOSTED_MCP_APP_SRCDOC_SANDBOX = 'allow-scripts'

/**
 * Builds the proxy document for a widget's HTML: the CSP built from the
 * resource's declared `csp` (granting only what `approveResourceOrigin`
 * approves), the link guard and the leaving notice, all ahead of any widget
 * script. Render the result as the `srcdoc` of a frame sandboxed with
 * `HOSTED_MCP_APP_SRCDOC_SANDBOX`.
 */
export function buildHostedMcpAppSrcDoc(input: {
  html: string
  csp?: McpUiResourceCsp
  approveResourceOrigin?: ApproveResourceOrigin
  allow?: string
}): string {
  const approved = approvedResourcePolicy(
    input.csp,
    input.approveResourceOrigin,
  )
  const appDocument = addContentSecurityPolicy(input.html, approved)
  return buildMcpAppProxyDocument({
    appDocument,
    policy: resourcePolicyDirectives(approved).join('; '),
    sandbox: HOSTED_MCP_APP_SRCDOC_SANDBOX,
    allow: input.allow,
  })
}
