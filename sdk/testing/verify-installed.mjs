/** Compare installed archives with their generated release manifest, not a fixed count. */
import assert from 'node:assert/strict'
import { execFileSync, spawnSync } from 'node:child_process'
import { mkdtempSync, readFileSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'

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

// The CLI has no operation manifest of its own. Run the installed `apostra`
// program as a user would, through the bin link npm created, and check that it
// reports the expected version and the operations of the SDK installed beside
// it. With a manifest path, those operations must also be the generated ones.
// Nothing here signs in, calls the API, or reads real credentials: both
// commands run offline, with the config directory pointed at an empty one.
if (process.argv[2] === '--cli') {
  const [, , , installDirectory, expectedVersion, manifestPath] = process.argv
  assert(installDirectory, 'Usage: verify-installed.mjs --cli INSTALL_DIRECTORY [VERSION] [SDK_MANIFEST]')
  const directory = resolve(installDirectory)
  const home = mkdtempSync(join(tmpdir(), 'apostra-cli-home-'))
  try {
    const apostra = (...args) => execFileSync(join(directory, 'node_modules/.bin/apostra'), args, {
      cwd: directory, encoding: 'utf8', timeout: 30_000,
      env: { ...process.env, HOME: home, XDG_CONFIG_HOME: home, APPDATA: home },
    })
    const version = apostra('--version').trim()
    if (expectedVersion) assert.equal(version, expectedVersion, 'Installed CLI reports a different version')
    const envelope = JSON.parse(apostra('operations', 'list', '--json'))
    assert.equal(envelope.schemaVersion, 1, 'Unexpected CLI envelope version')
    assert.equal(envelope.ok, true, 'The CLI operations envelope is not a success')
    const listed = envelope.data
    const names = listed.operations.map(operation => operation.name)
    assert(names.length > 0 && names.includes('get_delivery'), 'The CLI lists no SDK operations')
    assert.equal(new Set(names).size, names.length, 'The CLI lists a duplicate operation')
    const installedSdk = JSON.parse(readFileSync(join(directory, 'node_modules/@apostra/sdk/package.json'), 'utf8'))
    assert.equal(listed.sdkVersion, installedSdk.version, 'The CLI did not read the SDK installed beside it')
    if (manifestPath) {
      const manifest = JSON.parse(readFileSync(resolve(manifestPath), 'utf8'))
      assert.equal(listed.sdkVersion, manifest.version, 'The CLI SDK version differs from the manifest')
      assert.deepEqual([...names].sort(), [...manifest.operations].sort(), 'The CLI operations differ from the manifest')
    }
    // `call` is installed and reports failures in the envelope with its exit code.
    // An unknown operation is refused before any credential is read.
    const refused = spawnSync(join(directory, 'node_modules/.bin/apostra'), ['call', 'no_such_operation', '--account', '1', '--json'], {
      cwd: directory, encoding: 'utf8', timeout: 30_000,
      env: { ...process.env, HOME: home, XDG_CONFIG_HOME: home, APPDATA: home },
    })
    assert.equal(refused.status, 2, 'apostra call must exit 2 for an unknown operation')
    const refusal = JSON.parse(refused.stdout)
    assert.equal(refusal.ok, false)
    assert.equal(refusal.error.code, 'UNKNOWN_OPERATION')
    process.stdout.write(`@apostra/cli ${version} installed; it runs and lists ${names.length} operations from @apostra/sdk ${installedSdk.version}.\n`)
  } finally {
    rmSync(home, { recursive: true, force: true })
  }
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
