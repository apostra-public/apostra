import { spawn } from 'node:child_process'
import { createHash, randomBytes, timingSafeEqual } from 'node:crypto'
import { createServer } from 'node:http'
import type { AddressInfo } from 'node:net'

import { Apostra } from '@apostra/sdk'
import {
  type CliLoginEntry,
  cliClientId,
  discoverCliLogin,
  exchangeCliLoginCode,
  withCliLoginLock,
  writeCliLogin,
} from '@apostra/sdk/cli-login'

export const loginTimeoutMs = 5 * 60_000
export const scopeNames = ['read', 'write'] as const
type Fetch = typeof globalThis.fetch

const base64url = (bytes: Buffer) => bytes.toString('base64url')

/** PKCE (RFC 7636), S256. */
export const pkceChallenge = (verifier: string) =>
  base64url(createHash('sha256').update(verifier).digest())
export function createPkce() {
  const verifier = base64url(randomBytes(32))
  return { verifier, challenge: pkceChallenge(verifier) }
}
export const createState = () => base64url(randomBytes(32))

const page = (message: string) =>
  `<!doctype html><meta charset="utf-8"><title>Apostra</title><body style="font-family:system-ui;margin:4rem auto;max-width:32rem"><h1>Apostra</h1><p>${message}</p></body>`
const printable = (value: string) =>
  value.replace(/[^\x20-\x7e]/g, '').slice(0, 200)

/**
 * Receive the authorization redirect on 127.0.0.1 (RFC 8252 section 7.3). A
 * request with a missing or wrong state is answered 400 and ignored: it never
 * ends the sign-in, and its parameters are never used or echoed.
 */
export async function startCallbackServer(options: {
  state: string
  timeoutMs?: number
}) {
  const expected = Buffer.from(options.state)
  let settle!: (outcome: { code?: string; error?: Error }) => void
  const outcome = new Promise<{ code?: string; error?: Error }>((r) => {
    settle = r
  })
  const server = createServer((req, res) => {
    const url = new URL(req.url ?? '/', 'http://127.0.0.1')
    const reply = (status: number, message: string, done?: () => void) => {
      res.writeHead(status, {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'no-store',
        'Referrer-Policy': 'no-referrer',
        Connection: 'close',
      })
      res.end(page(message), done)
    }
    const state = Buffer.from(url.searchParams.get('state') ?? '')
    if (req.method !== 'GET' || url.pathname !== '/callback')
      return reply(404, 'Not found.')
    if (state.length !== expected.length || !timingSafeEqual(state, expected))
      return reply(
        400,
        'This sign-in link is not valid. Return to your terminal.',
      )
    const error = url.searchParams.get('error')
    const code = url.searchParams.get('code')
    if (error)
      return reply(
        400,
        'Sign-in was not completed. You can close this tab.',
        () =>
          settle({ error: new Error(`Sign-in failed: ${printable(error)}`) }),
      )
    if (!code)
      return reply(400, 'Sign-in did not return a code.', () =>
        settle({ error: new Error('Sign-in did not return a code') }),
      )
    reply(200, 'You are signed in to Apostra. You can close this tab.', () =>
      settle({ code }),
    )
  })
  await new Promise<void>((resolve, reject) => {
    server.once('error', reject)
    server.listen(0, '127.0.0.1', resolve)
  })
  const redirectUri = `http://127.0.0.1:${(server.address() as AddressInfo).port}/callback`
  const close = () => {
    server.close()
    server.closeAllConnections()
  }
  const timeoutMs = options.timeoutMs ?? loginTimeoutMs
  const timer = setTimeout(
    () =>
      settle({
        error: new Error(
          `Timed out after ${Math.round(timeoutMs / 60_000)} minutes waiting for the browser sign-in. Run \`apostra login\` to try again.`,
        ),
      }),
    timeoutMs,
  )
  return {
    redirectUri,
    close,
    async code(): Promise<string> {
      try {
        const result = await outcome
        if (result.error) throw result.error
        return result.code as string
      } finally {
        clearTimeout(timer)
        close()
      }
    },
  }
}

/** Open the system browser. Resolves false when it cannot, so the caller prints the URL. */
export function openBrowser(url: string): Promise<boolean> {
  const [command, args]: [string, string[]] =
    process.platform === 'darwin'
      ? ['open', [url]]
      : process.platform === 'win32'
        ? ['rundll32', ['url.dll,FileProtocolHandler', url]]
        : ['xdg-open', [url]]
  return new Promise((resolve) => {
    try {
      const child = spawn(command, args, { stdio: 'ignore', detached: true })
      const timer = setTimeout(() => resolve(true), 3000)
      const done = (ok: boolean) => {
        clearTimeout(timer)
        resolve(ok)
      }
      child.once('error', () => done(false))
      child.once('exit', (code) => done(code === 0))
      child.unref()
    } catch {
      resolve(false)
    }
  })
}

export type LoginOptions = {
  resource: string
  scopes: string[]
  accountId?: string
  browser: boolean
  timeoutMs?: number
  fetch?: Fetch
  open?: (url: string) => Promise<boolean>
  say: (text: string) => void
}

export async function login(options: LoginOptions): Promise<CliLoginEntry> {
  const { resource, say } = options
  const fetcher = options.fetch ?? globalThis.fetch
  const discovery = await discoverCliLogin(resource, { fetch: fetcher })
  if (
    discovery.codeChallengeMethods &&
    !discovery.codeChallengeMethods.includes('S256')
  )
    throw new Error('The authorization server does not support PKCE S256')
  const { verifier, challenge } = createPkce()
  const state = createState()
  const callback = await startCallbackServer({
    state,
    timeoutMs: options.timeoutMs,
  })
  try {
    const authorize = new URL(discovery.authorizationEndpoint)
    for (const [key, value] of Object.entries({
      response_type: 'code',
      client_id: cliClientId(resource),
      redirect_uri: callback.redirectUri,
      code_challenge: challenge,
      code_challenge_method: 'S256',
      state,
      scope: options.scopes.join(' '),
      resource,
      ...(options.accountId ? { account_id: options.accountId } : {}),
    }))
      authorize.searchParams.set(key, value)
    const opened =
      options.browser && (await (options.open ?? openBrowser)(authorize.href))
    if (opened) say('Opened your browser to sign in to Apostra...\n')
    else say(`Open this URL in a browser to sign in:\n\n${authorize.href}\n\n`)
    const code = await callback.code()
    const tokens = await exchangeCliLoginCode(
      { fetch: fetcher },
      discovery,
      resource,
      {
        code,
        verifier,
        redirectUri: callback.redirectUri,
      },
    )
    // The person bound one account at consent. Take it from the token response
    // if the server states it, else ask the API who this token is.
    const accountId =
      tokens.accountId ??
      String(
        (
          await new Apostra({
            baseUrl: resource,
            accessToken: tokens.accessToken,
            fetch: fetcher,
          }).getStatus()
        ).account.accountId,
      )
    const entry: CliLoginEntry = {
      issuer: discovery.issuer,
      resource,
      clientId: cliClientId(resource),
      accessToken: tokens.accessToken,
      refreshToken: tokens.refreshToken,
      expiresAt: tokens.expiresAt,
      accountId,
      scopes: tokens.scopes ?? options.scopes,
    }
    await withCliLoginLock(async () => writeCliLogin(resource, entry))
    return entry
  } finally {
    callback.close()
  }
}
