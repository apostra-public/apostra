/**
 * Puts a content security policy nonce on every `<script>` in an app document.
 *
 * An app frame loaded as a `srcdoc` inherits its host page's `script-src`. When
 * that policy allows scripts only by nonce, every inline script the frame runs
 * needs the nonce, and a header cannot list them: an app's inline bundle is far
 * too large to hash into one. Parsing the document is what makes this safe. A
 * bundle holds strings such as `"<script>"`, so rewriting the markup as text
 * would corrupt it, while the parser finds only real script elements and
 * serializes each script's text back unchanged. Nothing runs: a parsed
 * document's scripts do not execute.
 */
export function stampScriptNonce(html: string, nonce: string): string {
  const document = new DOMParser().parseFromString(html, 'text/html')
  for (const script of document.querySelectorAll('script')) {
    script.setAttribute('nonce', nonce)
  }
  return `<!doctype html>${document.documentElement.outerHTML}`
}
