/** Compare installed archives with their generated release manifest, not a fixed count. */
import assert from 'node:assert/strict'
import { execFileSync } from 'node:child_process'
import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'

// The MCP Apps host package has no operation manifest. Check instead that every
// public entry point the package declares imports from the installed archive and
// that the core exports exist. The React entry point is imported only when the
// caller says react is installed, which proves the root entry does not need it.
if (process.argv[2] === '--mcp-app-host') {
  const [, , , installDirectory, expectedVersion, withReact] = process.argv
  assert(installDirectory, 'Usage: verify-installed.mjs --mcp-app-host INSTALL_DIRECTORY [VERSION] [react]')
  const hostCode = `
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import * as host from '@apostra/mcp-app-host';
import * as frameSecurity from '@apostra/mcp-app-host/frame-security';
const require = createRequire(import.meta.url);
const metadata = require('@apostra/mcp-app-host/package.json');
assert.equal(metadata.name, '@apostra/mcp-app-host');
assert.equal(metadata.private, undefined, 'The published package must not be private');
if (${JSON.stringify(expectedVersion ?? '')}) assert.equal(metadata.version, ${JSON.stringify(expectedVersion ?? '')});
for (const name of ['createAgentMcpAppBridge', 'resolveMcpAppFrame', 'widgetPageFrame', 'readWidgetPageMeta', 'buildHostedMcpAppSrcDoc', 'buildMcpAppProxyDocument', 'MCP_APP_FRAME_LINK_GUARD', 'MCP_APP_FRAME_SANDBOX', 'APOSTRA_WIDGET_PAGE_ORIGINS'])
  assert.notEqual(host[name], undefined, 'Missing root export ' + name);
for (const name of ['MCP_APP_FRAME_SANDBOX', 'WIDGET_PAGE_FRAME_SANDBOX', 'mcpAppProxyCsp'])
  assert.notEqual(host[name] ?? frameSecurity[name], undefined, 'Missing export ' + name);
assert.equal(host.HostedMcpAppFrame, undefined, 'The React frame belongs to the ./react entry point');
if (${JSON.stringify(withReact === 'react')}) {
  const react = await import('@apostra/mcp-app-host/react');
  assert.equal(typeof react.HostedMcpAppFrame, 'function');
}
process.stdout.write(metadata.version);
`
  const installedVersion = execFileSync(
    process.execPath,
    ['--input-type=module', '-e', hostCode],
    { cwd: resolve(installDirectory), encoding: 'utf8', timeout: 30_000 },
  )
  process.stdout.write(`@apostra/mcp-app-host ${installedVersion} installed; entry points import${withReact === 'react' ? ', including ./react' : ' without react'}.\n`)
  process.exit(0)
}

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
