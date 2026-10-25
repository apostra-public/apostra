import { Apostra } from '@apostra/sdk'
import {
  cliLoginTokenProvider,
  logoutCliLogin,
  normalizeBaseUrl,
  readCliLogin,
  refreshCliLogin,
} from '@apostra/sdk/cli-login'
import { baseUrl as defaultBaseUrl } from '@apostra/sdk/metadata'
import { Command, Option } from 'commander'

import packageMetadata from '../package.json' with { type: 'json' }
import { login, scopeNames } from './login.js'
import {
  cliEnvelopeVersion,
  describeOperation,
  listOperations,
  operationsEnvelope,
} from './operations.js'

type Writer = (text: string) => void
export type ProgramDeps = {
  fetch?: typeof globalThis.fetch
  open?: (url: string) => Promise<boolean>
  loginTimeoutMs?: number
}

/** `--base-url`, then APOSTRA_BASE_URL, then the public API. A bare origin means its `/api/v3`. */
function resolveBaseUrl(option?: string): string {
  const url = new URL(option ?? process.env.APOSTRA_BASE_URL ?? defaultBaseUrl)
  if (url.pathname === '/') url.pathname = '/api/v3'
  return normalizeBaseUrl(url.href)
}

function writeJson(write: Writer, value: unknown): void {
  write(`${JSON.stringify(value)}\n`)
}

export function createProgram(
  write: Writer = (text) => process.stdout.write(text),
  deps: ProgramDeps = {},
) {
  const program = new Command()
  program
    .name('apostra')
    .description('The official Apostra command-line client')
    .version(packageMetadata.version)
    .configureOutput({ writeOut: write })

  const operations = program
    .command('operations')
    .description('Inspect public V3 operations')
  operations
    .command('list')
    .option('--json', 'write the versioned machine-readable envelope')
    .action((options: { json?: boolean }) => {
      if (options.json) return writeJson(write, operationsEnvelope())
      for (const operation of listOperations())
        write(`${operation.name}\t${operation.method}\t${operation.path}\n`)
    })

  operations
    .command('describe <operation>')
    .option('--json', 'write the versioned machine-readable envelope')
    .action((name: string, options: { json?: boolean }) => {
      const operation = describeOperation(name)
      if (!operation) {
        program.error(`Unknown public V3 operation: ${name}`, { exitCode: 2 })
        return
      }
      if (options.json)
        return writeJson(write, {
          version: cliEnvelopeVersion,
          operation,
        })
      write(
        `${operation.name}\n${operation.method} ${operation.path}\n${operation.summary}\n`,
      )
    })

  const baseUrlOption = () =>
    new Option(
      '--base-url <url>',
      'Apostra API base URL (default: APOSTRA_BASE_URL or https://api.apostra.com)',
    )
  // Report a failure on stderr with exit code 1, never a stack trace.
  const run =
    <A extends unknown[]>(action: (...args: A) => Promise<void> | void) =>
    async (...args: A) => {
      try {
        await action(...args)
      } catch (error) {
        program.error(error instanceof Error ? error.message : String(error), {
          exitCode: 1,
        })
      }
    }

  program
    .command('login')
    .description(
      'Sign in with your browser; the SDK and CLI then need no API key',
    )
    .addOption(baseUrlOption())
    .option('--account <id>', 'preselect the account to bind')
    .addOption(
      new Option(
        '--scope <scope...>',
        'access to request (default: read write)',
      ).choices(scopeNames),
    )
    .option(
      '--no-browser',
      'print the sign-in URL instead of opening a browser',
    )
    .action(
      run(
        async (options: {
          baseUrl?: string
          account?: string
          scope?: (typeof scopeNames)[number][]
          browser: boolean
        }) => {
          if (
            options.account !== undefined &&
            !/^[1-9][0-9]*$/.test(options.account)
          )
            throw new Error('--account must be a positive integer')
          const resource = resolveBaseUrl(options.baseUrl)
          const scopes = [...new Set(options.scope ?? ['read', 'write'])].map(
            (scope) => `interchange:${scope}`,
          )
          const entry = await login({
            resource,
            scopes,
            accountId: options.account,
            browser: options.browser,
            timeoutMs: deps.loginTimeoutMs,
            fetch: deps.fetch,
            open: deps.open,
            say: write,
          })
          write(
            `Signed in to ${resource} as account ${entry.accountId} (${entry.scopes.join(' ')}).\n`,
          )
        },
      ),
    )

  program
    .command('logout')
    .description('Revoke the stored refresh token and delete the stored login')
    .addOption(baseUrlOption())
    .action(
      run(async (options: { baseUrl?: string }) => {
        const resource = resolveBaseUrl(options.baseUrl)
        const result = await logoutCliLogin(resource, { fetch: deps.fetch })
        if (!result.found) return write(`Not signed in to ${resource}.\n`)
        write(
          result.revoked
            ? `Signed out of ${resource}.\n`
            : `Removed the local login for ${resource}, but could not revoke it on the server. It stays valid there until it expires; revoke it in your Apostra account if you lost control of this machine.\n`,
        )
      }),
    )

  program
    .command('status')
    .description('Show the stored login and the account it is bound to')
    .addOption(baseUrlOption())
    .action(
      run(async (options: { baseUrl?: string }) => {
        const resource = resolveBaseUrl(options.baseUrl)
        const entry = await refreshCliLogin(resource, { fetch: deps.fetch })
        write(
          `Base URL: ${resource}\nAccount ID: ${entry.accountId}\nScopes: ${entry.scopes.join(' ')}\nAccess token expires: ${entry.expiresAt}\n`,
        )
        const status = await new Apostra({
          baseUrl: resource,
          tokenProvider: cliLoginTokenProvider({
            baseUrl: resource,
            fetch: deps.fetch,
          }),
          fetch: deps.fetch,
        }).getStatus()
        write(
          `Account: ${status.account.company}\nReadiness: ${status.state}${status.canTransact === undefined ? '' : `, can transact: ${status.canTransact}`}\n`,
        )
      }),
    )

  program
    .command('token')
    .description(
      'Print a valid access token (refreshing it if needed) for piping',
    )
    .addOption(baseUrlOption())
    .action(
      run(async (options: { baseUrl?: string }) => {
        const resource = resolveBaseUrl(options.baseUrl)
        if (!readCliLogin(resource))
          throw new Error(
            `Not signed in to ${resource}. Run \`apostra login\`.`,
          )
        write(
          `${await cliLoginTokenProvider({ baseUrl: resource, fetch: deps.fetch })()}\n`,
        )
      }),
    )

  return program
}
