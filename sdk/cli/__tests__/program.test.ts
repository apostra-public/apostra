import { CommanderError } from 'commander'
import { describe, expect, it } from 'vitest'

import packageMetadata from '../package.json' with { type: 'json' }
import { createProgram } from '../src/program.js'

async function run(args: string[]) {
  let output = ''
  const program = createProgram((text) => {
    output += text
  })
  program.exitOverride()
  try {
    await program.parseAsync(['node', 'apostra', ...args])
  } catch (error) {
    if (
      !(error instanceof CommanderError) ||
      error.code !== 'commander.version'
    )
      throw error
  }
  return output
}

describe('operations commands', () => {
  it('reads its version from package metadata', async () => {
    expect(await run(['--version'])).toBe(`${packageMetadata.version}\n`)
  })

  it('lists generated SDK operations in a versioned JSON envelope', async () => {
    const output = await run(['operations', 'list', '--json'])
    const value = JSON.parse(output) as {
      version: number
      operations: { name: string }[]
    }
    expect(value.version).toBe(1)
    expect(value.operations.map((operation) => operation.name)).toContain(
      'get_delivery',
    )
  })

  it('describes a generated SDK operation without a second operation catalogue', async () => {
    const output = await run([
      'operations',
      'describe',
      'get_delivery',
      '--json',
    ])
    expect(JSON.parse(output)).toMatchObject({
      version: 1,
      operation: {
        name: 'get_delivery',
        method: 'POST',
        path: '/tools/get_delivery',
      },
    })
  })
})
