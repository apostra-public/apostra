import { Apostra } from '@apostra/sdk'
import {
  cliLoginTokenProvider,
  logoutCliLogin,
  normalizeBaseUrl,
} from '@apostra/sdk/cli-login'
import { baseUrl as defaultBaseUrl } from '@apostra/sdk/metadata'
import {
  Command,
  CommanderError,
  InvalidArgumentError,
  Option,
} from 'commander'

import packageMetadata from '../package.json' with { type: 'json' }
import { callOperation } from './call.js'
import { login, scopeNames } from './login.js'
import {
  describeOperation,
  listOperations,
  operationDetail,
  operationsData,
} from './operations.js'
import {
  type CliError,
  errorEnvelope,
  exitCodes,
  invalidInput,
  successEnvelope,
  toCliError,
} from './output.js'
import { freshLogin } from './session.js'

type Writer = (text: string) => void
export type ProgramDeps = {
  fetch?: typeof globalThis.fetch
  open?: (url: string) => Promise<boolean>
  loginTimeoutMs?: number
  /** Where diagnostics go. Defaults to process.stderr. */
  stderr?: Writer
  env?: NodeJS.ProcessEnv
  readStdin?: () => Promise<string>
}

async function readProcessStdin(): Promise<string> {
  const chunks: Buffer[] = []
  for await (const chunk of process.stdin) chunks.push(chunk as Buffer)
  return Buffer.concat(chunks).toString('utf8')
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
  const stderr: Writer = deps.stderr ?? ((text) => process.stderr.write(text))
  const program = new Command()
  // Set before any subcommand exists: subcommands inherit both. runCli reports
  // usage errors itself, in the envelope when --json was asked for.
  program
    .name('apostra')
    .description('The official Apostra command-line client')
    .version(packageMetadata.version)
    .exitOverride()
    .configureOutput({
      writeOut: write,
      writeErr: stderr,
      outputError: () => {},
    })
  const jsonOption = () =>
    new Option(
      '--json',
      'write one versioned JSON envelope to stdout; diagnostics go to stderr',
    )
  const finish = (
    json: boolean | undefined,
    data: unknown,
    text: () => string,
    meta?: Record<string, unknown>,
  ) => {
    if (json) writeJson(write, successEnvelope(data, meta))
    else write(text())
  }

  const operations = program
    .command('operations')
    .description('Inspect public V3 operations')
  operations
    .command('list')
    .addOption(jsonOption())
    .action((options: { json?: boolean }) => {
      finish(options.json, operationsData(), () =>
        listOperations()
          .map(({ name, method, path }) => `${name}\t${method}\t${path}\n`)
          .join(''),
      )
    })

  operations
    .command('describe <operation>')
    .addOption(jsonOption())
    .action((name: string, options: { json?: boolean }) => {
      const summary = describeOperation(name)
      if (!summary)
        throw invalidInput(
          `Unknown public V3 operation: ${name}`,
          'UNKNOWN_OPERATION',
        )
      finish(
        options.json,
        { operation: operationDetail(summary) },
        () =>
          `${summary.name}\n${summary.method} ${summary.path}\n${summary.summary}\n`,
      )
    })

  const baseUrlOption = () =>
    new Option(
      '--base-url <url>',
      'Apostra API base URL (default: APOSTRA_BASE_URL or https://api.apostra.com)',
    )
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
          throw invalidInput('--account must be a positive integer')
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
    )

  program
    .command('logout')
    .description('Revoke the stored refresh token and delete the stored login')
    .addOption(baseUrlOption())
    .addOption(jsonOption())
    .action(async (options: { baseUrl?: string; json?: boolean }) => {
      const resource = resolveBaseUrl(options.baseUrl)
      const result = await logoutCliLogin(resource, { fetch: deps.fetch })
      finish(
        options.json,
        { baseUrl: resource, signedIn: result.found, revoked: result.revoked },
        () => {
          if (!result.found) return `Not signed in to ${resource}.\n`
          return result.revoked
            ? `Signed out of ${resource}.\n`
            : `Removed the local login for ${resource}, but could not revoke it on the server. It stays valid there until it expires; revoke it in your Apostra account if you lost control of this machine.\n`
        },
      )
    })

  program
    .command('status')
    .description('Show the stored login and the account it is bound to')
    .addOption(baseUrlOption())
    .addOption(jsonOption())
    .action(async (options: { baseUrl?: string; json?: boolean }) => {
      const resource = resolveBaseUrl(options.baseUrl)
      const entry = await freshLogin(resource, deps.fetch)
      const status = await new Apostra({
        baseUrl: resource,
        tokenProvider: cliLoginTokenProvider({
          baseUrl: resource,
          fetch: deps.fetch,
        }),
        fetch: deps.fetch,
      }).getStatus()
      finish(
        options.json,
        {
          baseUrl: resource,
          accountId: entry.accountId,
          scopes: entry.scopes,
          expiresAt: entry.expiresAt,
          account: { company: status.account.company },
          readiness: status.state,
          canTransact: status.canTransact ?? null,
        },
        () =>
          `Base URL: ${resource}\nAccount ID: ${entry.accountId}\nScopes: ${entry.scopes.join(' ')}\nAccess token expires: ${entry.expiresAt}\nAccount: ${status.account.company}\nReadiness: ${status.state}${status.canTransact === undefined ? '' : `, can transact: ${status.canTransact}`}\n`,
      )
    })

  program
    .command('token')
    .description(
      'Print a valid access token (refreshing it if needed) for piping',
    )
    .addOption(baseUrlOption())
    .addOption(jsonOption())
    .action(async (options: { baseUrl?: string; json?: boolean }) => {
      const { accessToken, expiresAt } = await freshLogin(
        resolveBaseUrl(options.baseUrl),
        deps.fetch,
      )
      finish(
        options.json,
        { token: accessToken, expiresAt },
        () => `${accessToken}\n`,
      )
    })

  const positiveInteger = (text: string) => {
    if (!/^[1-9][0-9]*$/.test(text))
      throw new InvalidArgumentError('must be a positive integer')
    return Number(text)
  }
  program
    .command('call <operation>')
    .description(
      'Call any public V3 operation by name; see `apostra operations list`',
    )
    .addOption(baseUrlOption())
    .option(
      '--input <json>',
      'request input: inline JSON, @file.json, or - for stdin (default: {})',
    )
    .addOption(
      new Option(
        '--set <path=value>',
        'set one input field; repeatable; the value is JSON when it parses as JSON',
      )
        .default([])
        .argParser((value: string, previous: string[]) => [...previous, value]),
    )
    .option(
      '--account <id>',
      'the account this call runs in (default: APOSTRA_ACCOUNT_ID, then your sign-in)',
    )
    .option(
      '--idempotency-key <key>',
      'required for writes; reuse it only to retry the same call',
    )
    .option('--all', 'follow nextCursor until the last page; data is the pages')
    .addOption(
      new Option('--max-pages <n>', 'stop with an error after this many pages')
        .default(100)
        .argParser(positiveInteger),
    )
    .addOption(jsonOption())
    .action(
      async (
        name: string,
        options: {
          baseUrl?: string
          input?: string
          set: string[]
          account?: string
          idempotencyKey?: string
          all?: boolean
          maxPages: number
          json?: boolean
        },
      ) => {
        const { data, meta } = await callOperation(name, options, {
          resource: resolveBaseUrl(options.baseUrl),
          fetch: deps.fetch,
          env: deps.env ?? process.env,
          readStdin: deps.readStdin ?? readProcessStdin,
          note: stderr,
        })
        finish(
          options.json,
          data,
          () => `${JSON.stringify(data, null, 2)}\n`,
          meta,
        )
      },
    )

  return program
}

/** Arguments before `--` that ask for the JSON envelope. */
const wantsJson = (args: string[]) => {
  const end = args.indexOf('--')
  return (end === -1 ? args : args.slice(0, end)).includes('--json')
}

const informational = new Set(['commander.helpDisplayed', 'commander.version'])

/**
 * Run the CLI and return its exit code. In JSON mode stdout carries one
 * envelope, success or failure; the same failure is always on stderr as text.
 */
export async function runCli(
  args: string[],
  io: { stdout: Writer; stderr: Writer },
  deps: ProgramDeps = {},
): Promise<number> {
  const program = createProgram(io.stdout, { ...deps, stderr: io.stderr })
  try {
    await program.parseAsync(args, { from: 'user' })
    return exitCodes.ok
  } catch (error) {
    if (error instanceof CommanderError && informational.has(error.code))
      return exitCodes.ok
    // Help for a missing command is already on stderr.
    if (error instanceof CommanderError && error.code === 'commander.help')
      return exitCodes.invalidInput
    const failure: CliError = toCliError(error)
    if (wantsJson(args)) writeJson(io.stdout, errorEnvelope(failure))
    io.stderr(`error: ${failure.message}\n`)
    return failure.exitCode
  }
}
