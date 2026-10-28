import {
  type CliLoginEntry,
  readCliLogin,
  refreshCliLogin,
} from '@apostra/sdk/cli-login'

import { CliError, exitCodes } from './output.js'

type Fetch = typeof globalThis.fetch

export const notSignedIn = (resource: string) =>
  new CliError(
    `Not signed in to ${resource}. Run \`apostra login\`.`,
    'NOT_SIGNED_IN',
    exitCodes.authentication,
  )

/** The stored login for `resource`, refreshed when its access token is about to expire. */
export async function freshLogin(
  resource: string,
  fetch?: Fetch,
): Promise<CliLoginEntry> {
  if (!readCliLogin(resource)) throw notSignedIn(resource)
  try {
    return await refreshCliLogin(resource, { fetch })
  } catch (error) {
    if (error instanceof Error && /\(HTTP 4\d\d\)/.test(error.message))
      throw new CliError(
        `${error.message}. Run \`apostra login\` again.`,
        'AUTHENTICATION_FAILED',
        exitCodes.authentication,
      )
    throw error
  }
}
