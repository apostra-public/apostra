import { readFileSync } from 'node:fs'

import {
  Apostra,
  paginate,
  type RequestOptions,
  type ResponseDetails,
} from '@apostra/sdk'
import { readCliLogin } from '@apostra/sdk/cli-login'
import { operations } from '@apostra/sdk/metadata'

import { describeOperation, type OperationName } from './operations.js'
import {
  CliError,
  exitCodes,
  invalidInput,
  type Meta,
  toCliError,
} from './output.js'
import { freshLogin, notSignedIn } from './session.js'

type Fetch = typeof globalThis.fetch
type Dispatch = (
  operation: OperationName,
  input: object,
  options: RequestOptions,
) => Promise<ResponseDetails<unknown>>
type JsonObject = Record<string, unknown>

export type CallOptions = {
  input?: string
  set?: string[]
  account?: string
  idempotencyKey?: string
  all?: boolean
  maxPages: number
}
export type CallContext = {
  resource: string
  fetch?: Fetch
  env: NodeJS.ProcessEnv
  readStdin: () => Promise<string>
  /** Diagnostics for the person at the terminal. Never stdout. */
  note: (text: string) => void
}

const isObject = (value: unknown): value is JsonObject =>
  typeof value === 'object' && value !== null && !Array.isArray(value)

const unsafeKeys = new Set(['__proto__', 'constructor', 'prototype'])

function parseJsonObject(text: string, source: string): JsonObject {
  let value: unknown
  try {
    value = JSON.parse(text)
  } catch {
    throw invalidInput(`${source} is not valid JSON`)
  }
  if (!isObject(value))
    throw invalidInput(`${source} must be a JSON object, not ${typeof value}`)
  return value
}

/** `--input @file.json`, `--input -` (stdin) or `--input '{"a":1}'`. */
async function readInput(
  input: string | undefined,
  readStdin: () => Promise<string>,
): Promise<JsonObject> {
  if (input === undefined) return {}
  if (input === '-') return parseJsonObject(await readStdin(), 'Input on stdin')
  if (!input.startsWith('@')) return parseJsonObject(input, '--input')
  const path = input.slice(1)
  let text: string
  try {
    text = readFileSync(path, 'utf8')
  } catch {
    throw invalidInput(`Cannot read the --input file ${path}`)
  }
  return parseJsonObject(text, path)
}

/** `--set a.b=value`: the value is JSON when it parses as JSON, otherwise a string. */
function applySet(target: JsonObject, pair: string): void {
  const equals = pair.indexOf('=')
  if (equals < 1) throw invalidInput(`--set expects path=value, got "${pair}"`)
  const keys = pair.slice(0, equals).split('.')
  if (keys.some((key) => !key || unsafeKeys.has(key)))
    throw invalidInput(`--set path "${pair.slice(0, equals)}" is not allowed`)
  const text = pair.slice(equals + 1)
  let value: unknown = text
  try {
    value = JSON.parse(text)
  } catch {}
  let node = target
  for (const key of keys.slice(0, -1)) {
    const next = Object.hasOwn(node, key) ? node[key] : undefined
    if (next === undefined) node = node[key] = {} as JsonObject
    else if (isObject(next)) node = next
    else
      throw invalidInput(
        `--set ${pair.slice(0, equals)}: ${key} is not an object`,
      )
  }
  node[keys[keys.length - 1] as string] = value
}

type Resolved = { account: string; source: string }

/** Every call names its account: --account, APOSTRA_ACCOUNT_ID, or the signed-in account. */
function resolveAccount(
  options: CallOptions,
  env: NodeJS.ProcessEnv,
  signedInAccount: string | undefined,
): Resolved {
  const named =
    options.account !== undefined
      ? { account: options.account, source: '--account' }
      : env.APOSTRA_ACCOUNT_ID
        ? { account: env.APOSTRA_ACCOUNT_ID, source: 'APOSTRA_ACCOUNT_ID' }
        : undefined
  if (named && !/^[1-9][0-9]*$/.test(named.account))
    throw invalidInput(`${named.source} must be a positive integer`)
  if (signedInAccount === undefined) {
    if (!named)
      throw invalidInput(
        'Name the account with --account <id> or APOSTRA_ACCOUNT_ID. API-key calls have no signed-in account.',
        'ACCOUNT_REQUIRED',
      )
    return named
  }
  if (named && named.account !== signedInAccount)
    throw new CliError(
      `${named.source} ${named.account} is not the account you signed in to (${signedInAccount}). A sign-in reaches one account; run \`apostra login --account ${named.account}\`, or use an API key.`,
      'ACCOUNT_MISMATCH',
      exitCodes.permission,
    )
  return named ?? { account: signedInAccount, source: 'your sign-in' }
}

/** The `nextCursor` of a page, or undefined on the last one. Refuses to guess. */
function nextCursor(data: unknown): string | undefined {
  const pages: JsonObject[] = []
  const walk = (value: unknown, depth: number) => {
    if (!isObject(value) || depth > 3) return
    if ('nextCursor' in value || 'hasMore' in value) pages.push(value)
    for (const child of Object.values(value)) walk(child, depth + 1)
  }
  walk(data, 0)
  const cursors = pages.flatMap((page) =>
    typeof page.nextCursor === 'string' && page.nextCursor
      ? [page.nextCursor]
      : [],
  )
  if (cursors.length > 1)
    throw new CliError(
      'The response has more than one page cursor, so --all cannot tell which to follow. Page it explicitly with --set cursor=<value>.',
      'AMBIGUOUS_PAGINATION',
      exitCodes.unavailable,
    )
  if (cursors.length === 0 && pages.some((page) => page.hasMore === true))
    throw new CliError(
      'The response says there are more results but gives no cursor, so --all would drop them. Narrow the request instead.',
      'INCOMPLETE_PAGINATION',
      exitCodes.unavailable,
    )
  return cursors[0]
}

function binaryData(bytes: Uint8Array) {
  try {
    return {
      encoding: 'utf-8',
      content: new TextDecoder('utf-8', { fatal: true }).decode(bytes),
    }
  } catch {
    return {
      encoding: 'base64',
      content: Buffer.from(bytes).toString('base64'),
    }
  }
}

/** Call one public V3 operation by name through the SDK's generated dispatch. */
export async function callOperation(
  name: string,
  options: CallOptions,
  context: CallContext,
): Promise<{ data: unknown; meta: Meta }> {
  const summary = describeOperation(name)
  if (!summary)
    throw invalidInput(
      `Unknown public V3 operation: ${name}. Run \`apostra operations list\`.`,
      'UNKNOWN_OPERATION',
    )
  const operation = operations[summary.name]
  const write = operation.idempotencyKey
  if (write && !options.idempotencyKey)
    throw invalidInput(
      `${name} changes data, so it needs --idempotency-key <key>. Reuse a key only to retry the same call.`,
      'IDEMPOTENCY_KEY_REQUIRED',
    )
  if (!write && options.idempotencyKey)
    throw invalidInput(
      `${name} only reads, so --idempotency-key does not apply.`,
    )
  if (options.all && (write || operation.binary))
    throw invalidInput(
      `--all pages through reads that return JSON; ${name} does not.`,
    )

  const input = await readInput(options.input, context.readStdin)
  for (const pair of options.set ?? []) applySet(input, pair)

  const apiKey = context.env.APOSTRA_API_KEY || undefined
  const login = apiKey ? undefined : readCliLogin(context.resource)
  if (!apiKey && !login) throw notSignedIn(context.resource)
  const { account, source } = resolveAccount(
    options,
    context.env,
    login?.accountId,
  )
  if (input.accountId !== undefined && String(input.accountId) !== account)
    throw new CliError(
      `The input names account ${String(input.accountId)}, but this call runs in account ${account} (${source}). Remove accountId from the input or change --account.`,
      'ACCOUNT_MISMATCH',
      exitCodes.permission,
    )
  context.note(`Using account ${account} (${source}).\n`)

  const client = new Apostra({
    baseUrl: context.resource,
    accountId: account,
    fetch: context.fetch,
    ...(apiKey
      ? { apiKey }
      : {
          tokenProvider: async () =>
            (await freshLogin(context.resource, context.fetch)).accessToken,
        }),
  })
  const dispatch = client.requestDetailed.bind(client) as unknown as Dispatch
  const send = async (body: object, signal?: AbortSignal) => {
    try {
      return await dispatch(summary.name, body, {
        accountId: account,
        idempotencyKey: options.idempotencyKey,
        signal,
      })
    } catch (error) {
      if (error instanceof TypeError) throw invalidInput(error.message)
      throw toCliError(error)
    }
  }
  const present = (data: unknown) =>
    data instanceof Uint8Array ? binaryData(data) : data

  if (!options.all) {
    const response = await send(input)
    return {
      data: present(response.data),
      meta: {
        operation: name,
        accountId: account,
        requestId: response.requestId,
      },
    }
  }

  const pages: unknown[] = []
  const requestIds: (string | null)[] = []
  for await (const page of paginate(
    (cursor, signal) => send(cursor ? { ...input, cursor } : input, signal),
    (page) => {
      const cursor = nextCursor(page.data)
      if (cursor && pages.length + 1 >= options.maxPages)
        throw new CliError(
          `Stopped after ${options.maxPages} pages and more remain. Raise --max-pages, or narrow the request.`,
          'PAGE_LIMIT',
          exitCodes.invalidInput,
        )
      return cursor
    },
  )) {
    pages.push(page.data)
    requestIds.push(page.requestId)
  }
  return {
    data: pages,
    meta: {
      operation: name,
      accountId: account,
      pages: pages.length,
      requestIds,
    },
  }
}
