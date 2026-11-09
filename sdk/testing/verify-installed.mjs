/** Compare installed archives with their generated release manifest, not a fixed count. */
import assert from 'node:assert/strict'
import { execFileSync, spawnSync } from 'node:child_process'
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { dirname, join, resolve } from 'node:path'

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
// program as a user would and check that it reports the expected version and
// the operations of the SDK installed beside it. With a manifest path, those
// operations must also be the generated ones. Nothing here signs in, calls the
// API, or reads real credentials: every command runs offline, with an empty
// home directory and nothing from the caller's environment but PATH.
//
// With --published, VERSION is on npm and is also installed the two ways
// developers install it, `npm i -g @apostra/cli@VERSION` and
// `npx @apostra/cli@VERSION`, each in its own clean environment, and both get
// the same checks. Those installs reach the npm registry, never Apostra. A
// failure names the command and prints its full output.
if (process.argv[2] === '--cli') {
  const published = process.argv.includes('--published')
  const [installDirectory, expectedVersion, manifestPath] = process.argv.slice(3).filter(arg => arg !== '--published')
  assert(installDirectory, 'Usage: verify-installed.mjs --cli INSTALL_DIRECTORY [VERSION] [SDK_MANIFEST] [--published]')
  assert(!published || expectedVersion, '--published needs the VERSION to install from npm')
  const scratch = mkdtempSync(join(tmpdir(), 'apostra-cli-'))
  try {
    const project = resolve(installDirectory)
    const projectEnv = cleanEnvironment(join(scratch, 'project'))
    const reports = [verifyCli(
      'Installed in a project',
      args => run(join(project, 'node_modules/.bin/apostra'), args, { cwd: project, env: projectEnv }),
      join(project, 'node_modules/@apostra/cli'), expectedVersion, manifestPath,
    )]
    if (published) {
      const spec = `@apostra/cli@${expectedVersion}`
      const globalHome = join(scratch, 'global')
      const globalEnv = cleanEnvironment(globalHome)
      const install = run('npm', ['install', '--global', spec], { cwd: join(globalHome, 'work'), env: globalEnv })
      assert.equal(install.status, 0, `npm i -g ${spec} failed\n${install.output}`)
      const prefix = globalEnv.npm_config_prefix
      reports.push(verifyCli(
        'Installed with npm i -g',
        args => run(join(prefix, 'bin/apostra'), args, { cwd: join(globalHome, 'work'), env: globalEnv }),
        join(prefix, 'lib/node_modules/@apostra/cli'), expectedVersion,
      ))
      // npx installs the package into its cache on the first run, here `--version`.
      const npxHome = join(scratch, 'npx')
      const npxEnv = cleanEnvironment(npxHome)
      reports.push(verifyCli(
        'Run with npx',
        args => run('npx', ['--yes', spec, ...args], { cwd: join(npxHome, 'work'), env: npxEnv }),
        () => {
          const installs = readdirSync(join(npxEnv.npm_config_cache, '_npx'))
          assert.equal(installs.length, 1, `npx made ${installs.length} installs in an empty cache`)
          return join(npxEnv.npm_config_cache, '_npx', installs[0], 'node_modules/@apostra/cli')
        },
        expectedVersion,
      ))
    }
    process.stdout.write(`${reports.join('\n')}\n`)
  } finally {
    rmSync(scratch, { recursive: true, force: true })
  }
  process.exit(0)
}

/**
 * An empty home, with its own npm cache and global prefix and an empty working
 * directory, and nothing from the caller's environment but PATH: no npm
 * settings, Apostra credentials or CI tokens.
 */
function cleanEnvironment(home) {
  mkdirSync(join(home, 'work'), { recursive: true })
  return {
    PATH: process.env.PATH,
    HOME: home, XDG_CONFIG_HOME: home, APPDATA: home,
    npm_config_cache: join(home, 'npm-cache'),
    npm_config_prefix: join(home, 'npm-global'),
    // Lifecycle scripts stay off, as for every install in this lane.
    npm_config_ignore_scripts: 'true',
    npm_config_update_notifier: 'false', npm_config_fund: 'false', npm_config_audit: 'false',
  }
}

/** Runs a command. `output` names it and holds everything it printed, for failure messages. */
function run(command, args, options) {
  const result = spawnSync(command, args, { encoding: 'utf8', timeout: 180_000, ...options })
  const outcome = result.error ? `failed: ${result.error.message}` : result.signal ? `was stopped by ${result.signal}` : `exited ${result.status}`
  return { ...result, output: `$ ${[command, ...args].join(' ')}\n${outcome}\n--- stdout ---\n${result.stdout ?? ''}\n--- stderr ---\n${result.stderr ?? ''}` }
}

/**
 * Checks one installed `apostra`. `apostra(args)` runs it; `cliDirectory` (or a
 * function returning it, once the first run has installed it) is the installed
 * package, from which the SDK it loads is found as Node finds it.
 */
function verifyCli(label, apostra, cliDirectory, expectedVersion, manifestPath) {
  const check = (condition, message, result) => assert(condition, `${label}: ${message}\n${result.output}`)
  const succeed = args => {
    const result = apostra(args)
    check(result.status === 0, `apostra ${args.join(' ')} failed`, result)
    return result
  }
  const envelopeOf = result => {
    try {
      return JSON.parse(result.stdout)
    } catch {
      return check(false, 'apostra printed no JSON envelope', result)
    }
  }
  const versionRun = succeed(['--version'])
  const version = versionRun.stdout.trim()
  if (expectedVersion) check(version === expectedVersion, `reports version ${version}, expected ${expectedVersion}`, versionRun)
  const directory = typeof cliDirectory === 'function' ? cliDirectory() : cliDirectory
  const cliPackage = JSON.parse(readFileSync(join(directory, 'package.json'), 'utf8'))
  check(cliPackage.name === '@apostra/cli' && cliPackage.version === version, `${directory} holds ${cliPackage.name}@${cliPackage.version}`, versionRun)
  const listRun = succeed(['operations', 'list', '--json'])
  const envelope = envelopeOf(listRun)
  check(envelope.schemaVersion === 1, 'unexpected CLI envelope version', listRun)
  check(envelope.ok === true, 'the operations envelope is not a success', listRun)
  const listed = envelope.data
  const names = listed.operations.map(operation => operation.name)
  check(names.length > 0 && names.includes('get_delivery'), 'the CLI lists no SDK operations', listRun)
  check(new Set(names).size === names.length, 'the CLI lists a duplicate operation', listRun)
  const installedSdk = sdkBeside(directory)
  check(listed.sdkVersion === installedSdk.version, `the CLI reports SDK ${listed.sdkVersion}, but ${installedSdk.version} is installed beside it`, listRun)
  if (manifestPath) {
    const manifest = JSON.parse(readFileSync(resolve(manifestPath), 'utf8'))
    assert.equal(listed.sdkVersion, manifest.version, 'The CLI SDK version differs from the manifest')
    assert.deepEqual([...names].sort(), [...manifest.operations].sort(), 'The CLI operations differ from the manifest')
  }
  // `call` is installed and reports failures in the envelope with its exit code.
  // An unknown operation is refused before any credential is read.
  const refused = apostra(['call', 'no_such_operation', '--account', '1', '--json'])
  check(refused.status === 2, 'apostra call must exit 2 for an unknown operation', refused)
  const refusal = envelopeOf(refused)
  check(refusal.schemaVersion === 1 && refusal.ok === false && refusal.error?.code === 'UNKNOWN_OPERATION', 'apostra call did not refuse the unknown operation', refused)
  return `${label}: @apostra/cli ${version} runs and lists ${names.length} operations from @apostra/sdk ${installedSdk.version}.`
}

/** The @apostra/sdk package.json Node resolves from the installed CLI package. */
function sdkBeside(cliDirectory) {
  for (let directory = cliDirectory; ; directory = dirname(directory)) {
    const candidate = join(directory, 'node_modules/@apostra/sdk/package.json')
    if (existsSync(candidate)) return JSON.parse(readFileSync(candidate, 'utf8'))
    assert.notEqual(dirname(directory), directory, `No @apostra/sdk is installed for ${cliDirectory}`)
  }
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
