/** Compare installed archives with their generated release manifest, not a fixed count. */
import assert from 'node:assert/strict'
import { execFileSync } from 'node:child_process'
import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'

const [manifestPath, directory, python] = process.argv.slice(2)
assert(manifestPath && directory, 'Usage: verify-installed.mjs MANIFEST INSTALL_DIRECTORY [PYTHON]')
const manifest = JSON.parse(readFileSync(resolve(manifestPath), 'utf8'))
assert.equal(typeof manifest.version, 'string', 'Missing manifest version')
assert(Array.isArray(manifest.operations) && manifest.operations.length > 0, 'Missing manifest operations')
assert(manifest.operations.every(id => typeof id === 'string' && id.length > 0), 'Invalid manifest operation')
assert.equal(new Set(manifest.operations).size, manifest.operations.length, 'Duplicate manifest operation')

const javascript = `
import assert from 'node:assert/strict';
import {operations, version} from '@apostra/sdk';
import * as metadata from '@apostra/sdk/metadata';
import '@apostra/sdk/models';
assert.deepEqual(metadata.operations, operations);
assert.equal(metadata.version, version);
process.stdout.write(JSON.stringify({version, operations: Object.keys(operations)}));
`
const pythonCode = `
import json
from importlib.metadata import version
from importlib.resources import files
from apostra import __version__, models
from apostra.transport import OPERATIONS
if version('apostra') != __version__:
    raise RuntimeError('Python distribution and runtime versions differ')
if not files('apostra').joinpath('py.typed').is_file():
    raise RuntimeError('Python package is missing py.typed')
print(json.dumps({'version': __version__, 'operations': list(OPERATIONS)}))
`
const snapshot = JSON.parse(execFileSync(
  python ?? process.execPath,
  python ? ['-c', pythonCode] : ['--input-type=module', '-e', javascript],
  { cwd: resolve(directory), encoding: 'utf8', timeout: 30_000 },
))
assert.equal(snapshot.version, manifest.version, 'Installed SDK version differs from manifest')
assert.deepEqual(snapshot.operations.sort(), [...manifest.operations].sort(), 'Installed SDK operations differ from manifest')
process.stdout.write(`${python ? 'Python' : 'TypeScript'} installed version and ${manifest.operations.length} operation identities match the generated manifest.\n`)
