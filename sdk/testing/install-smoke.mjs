/** Build and install actual archives in isolation, never through workspace links. */
import assert from 'node:assert/strict'
import { execFile } from 'node:child_process'
import { createServer } from 'node:http'
import { promisify } from 'node:util'
import { copyFileSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { resolve, join } from 'node:path'

const root = resolve(process.argv[2] ?? '.')
const publicTree = process.argv.includes('--public')
const targetsIndex = process.argv.indexOf('--targets')
const targets = targetsIndex < 0 ? 'both' : process.argv[targetsIndex + 1]
if (!['typescript', 'python', 'both', 'mcp-app-host', 'cli'].includes(targets))
  throw new Error('Pass --targets typescript, python, both, mcp-app-host or cli')
// By default the CLI is installed with the SDK from this same tree, because the
// SDK release it needs may not be on npm yet. This asks for the registry's SDK.
const publishedSdk = process.argv.includes('--published-sdk')
if (publishedSdk && targets !== 'cli') throw new Error('--published-sdk applies only to --targets cli')
const includesTypescript = targets === 'typescript' || targets === 'both'
const includesPython = targets === 'python' || targets === 'both'
const ts = join(root, publicTree ? 'sdk/typescript' : 'packages/apostra-sdk')
const py = join(root, publicTree ? 'sdk/python' : 'packages/apostra-sdk-python')
const manifest = join(root, publicTree ? 'sdk/release/manifest.json' : 'scripts/codegen/apostra-sdk/manifest.json')
const verifier = join(root, publicTree ? 'sdk/testing/verify-installed.mjs' : 'scripts/testing/apostra-sdk/verify-installed.mjs')
async function run(command, args, cwd = root, env = {}) {
  return (await promisify(execFile)(command,args,{cwd,env:{...process.env,...env},encoding:'utf8',timeout:180_000,maxBuffer:4*1024*1024})).stdout
}
// The MCP Apps host package ships no operations, so its archive is checked for
// its own contract instead: the files and package.json that reach npm, an
// install with no workspace links, entry points that import with and without
// react, and a consumer that type-checks against the shipped declarations.
async function smokeMcpAppHost() {
  const pkg = join(root, publicTree ? 'sdk/mcp-app-host' : 'packages/mcp-app-host')
  const verifier = join(root, publicTree ? 'sdk/testing/verify-installed.mjs' : 'scripts/testing/apostra-sdk/verify-installed.mjs')
  const dir = mkdtempSync(join(tmpdir(), 'apostra-mcp-app-host-'))
  try {
    // The public tree's package.json is already in its published shape. The
    // private package keeps source exports for workspace consumers, and pnpm
    // applies its publishConfig overrides when it packs.
    await run(publicTree ? 'npm' : 'pnpm', ['pack', '--pack-destination', dir], pkg)
    const archive = readdirSync(dir).find(name => name.endsWith('.tgz'))
    assert(archive, 'Packing produced no npm archive')
    const listing = (await run('tar', ['-tzf', join(dir, archive)])).split('\n').filter(Boolean)
    for (const required of ['package/LICENSE', 'package/README.md', 'package/dist/index.js', 'package/dist/index.d.ts', 'package/dist/react.js', 'package/dist/react.d.ts', 'package/dist/frame-security.js', 'package/dist/frame-security.d.ts'])
      assert(listing.includes(required), `npm tarball is missing ${required}`)
    assert(!listing.some(name => name.includes('__tests__') || name.startsWith('package/src/')), 'npm tarball must ship dist only, not sources or tests')
    const manifest = JSON.parse(await run('tar', ['-xzOf', join(dir, archive), 'package/package.json']))
    assert.equal(manifest.license, 'Apache-2.0')
    assert.equal(manifest.private, undefined, 'The published package must not be private')
    assert.equal(manifest.main, './dist/index.js')
    assert.equal(manifest.exports['.'].import, './dist/index.js')
    assert.equal(manifest.exports['./react'].import, './dist/react.js')
    assert.equal(manifest.exports['./frame-security'].import, './dist/frame-security.js')
    assert.equal(manifest.publishConfig.exports, undefined, 'publishConfig overrides must be applied, not shipped')
    assert.equal(manifest.peerDependenciesMeta.react.optional, true)
    const consumer = join(dir, 'consumer')
    mkdirSync(consumer)
    writeFileSync(join(consumer, 'package.json'), '{"type":"module"}')
    await run('npm', ['install', '--ignore-scripts', '--no-audit', '--no-fund', join(dir, archive)], consumer)
    await run('node', [verifier, '--mcp-app-host', consumer, manifest.version])
    // With react absent the root entry still has to work: react is optional.
    // The page path needs no DOM; the srcdoc path parses HTML in the browser.
    writeFileSync(join(consumer, 'smoke.mjs'), `import assert from 'node:assert/strict';import {createRequire} from 'node:module';import {APOSTRA_WIDGET_PAGE_ORIGINS,resolveMcpAppFrame} from '@apostra/mcp-app-host';assert.throws(()=>createRequire(import.meta.url).resolve('react'),{code:'MODULE_NOT_FOUND'});const frame=resolveMcpAppFrame({meta:{'scope3/widget-page':{url:'https://widgets.apostra.com/campaigns',appearanceParams:['color-scheme']}},page:{appearance:{colorScheme:'dark',productBrand:'new'},allowedOrigins:APOSTRA_WIDGET_PAGE_ORIGINS}});assert.deepEqual({kind:frame?.kind,src:frame?.src,targetOrigin:frame?.targetOrigin},{kind:'page',src:'https://widgets.apostra.com/campaigns?color-scheme=dark',targetOrigin:'https://widgets.apostra.com'});`)
    await run('node', ['smoke.mjs'], consumer)
    const { react, 'react-dom': reactDom, '@types/react': reactTypes } = JSON.parse(readFileSync(join(pkg, 'package.json'), 'utf8')).devDependencies
    await run('npm', ['install', '--ignore-scripts', '--no-audit', '--no-fund', `react@${react}`, `react-dom@${reactDom}`, `@types/react@${reactTypes}`], consumer)
    await run('node', [verifier, '--mcp-app-host', consumer, manifest.version, 'react'])
    writeFileSync(join(consumer, 'consumer.mts'), `import {APOSTRA_WIDGET_PAGE_ORIGINS, createAgentMcpAppBridge, resolveMcpAppFrame, type McpAppFrame} from '@apostra/mcp-app-host';import {HostedMcpAppFrame} from '@apostra/mcp-app-host/react';import {mcpAppProxyCsp} from '@apostra/mcp-app-host/frame-security';const frame: McpAppFrame | null = resolveMcpAppFrame({html: '<p>widget</p>', approveResourceOrigin: () => false});void [APOSTRA_WIDGET_PAGE_ORIGINS, createAgentMcpAppBridge, HostedMcpAppFrame, mcpAppProxyCsp, frame];`)
    const tsc = join(pkg, 'node_modules/.bin/tsc6')
    const consumerFlags = ['--noEmit', '--strict', '--target', 'ES2022', '--module', 'NodeNext', '--moduleResolution', 'NodeNext', '--lib', 'ES2022,DOM,DOM.Iterable', '--jsx', 'react-jsx']
    // A browser consumer as browser toolchains configure one: no Node types,
    // and library declarations not re-checked (Vite and Next set skipLibCheck).
    await run(tsc, [...consumerFlags, '--skipLibCheck', 'consumer.mts'], consumer)
    // Checking every library declaration needs Node types: an MCP SDK
    // dependency's declarations name `Buffer`. The README states this.
    await run('npm', ['install', '--ignore-scripts', '--no-audit', '--no-fund', '@types/node@22'], consumer)
    await run(tsc, [...consumerFlags, '--types', 'node', 'consumer.mts'], consumer)
    process.stdout.write(`@apostra/mcp-app-host ${manifest.version} archive installed; entry points import and its declarations type-check.\n`)
  } finally {
    rmSync(dir, { recursive: true, force: true })
  }
}
// The CLI ships no operations of its own, so its archive is checked for its own
// contract: the files and package.json that reach npm, an install into an empty
// directory with no workspace links, and the installed `apostra` program run
// under Node (see verify-installed.mjs --cli for exactly what that proves). It
// does not sign in or call the API.
async function smokeCli() {
  const pkg = join(root, publicTree ? 'sdk/cli' : 'packages/apostra-cli')
  const dir = mkdtempSync(join(tmpdir(), 'apostra-cli-'))
  try {
    // The private package names the SDK as a workspace dependency, which pnpm
    // turns into a version range when it packs. The public tree's package.json
    // already carries the published range.
    await run(publicTree ? 'npm' : 'pnpm', ['pack', '--pack-destination', dir], pkg)
    const archive = readdirSync(dir).find(name => name.endsWith('.tgz'))
    assert(archive, 'Packing produced no npm archive')
    const listing = (await run('tar', ['-tzf', join(dir, archive)])).split('\n').filter(Boolean)
    for (const required of ['package/LICENSE', 'package/README.md', 'package/package.json', 'package/dist/bin.js', 'package/dist/program.js'])
      assert(listing.includes(required), `npm tarball is missing ${required}`)
    assert(!listing.some(name => name.includes('__tests__') || name.startsWith('package/src/')), 'npm tarball must ship dist only, not sources or tests')
    const published = JSON.parse(await run('tar', ['-xzOf', join(dir, archive), 'package/package.json']))
    assert.equal(published.name, '@apostra/cli')
    assert.equal(published.license, 'Apache-2.0')
    assert.equal(published.private, undefined, 'The published package must not be private')
    assert.deepEqual(published.bin, { apostra: './dist/bin.js' })
    assert.equal(published.repository?.url, 'https://github.com/apostra-public/apostra.git', 'npm provenance needs the repository the workflow runs in')
    assert(!JSON.stringify(published).includes('workspace:'), 'The published package must not name a workspace dependency')
    assert.match(published.dependencies['@apostra/sdk'], /^\^\d+\.\d+\.\d+$/, '@apostra/sdk must be an npm range')
    const consumer = join(dir, 'consumer')
    mkdirSync(consumer)
    const consumerManifest = { type: 'module', private: true }
    if (!publishedSdk) {
      // Pack the SDK from this tree and let it stand in for the declared range
      // everywhere in the consumer's dependency tree.
      const sdkDir = join(dir, 'sdk')
      mkdirSync(sdkDir)
      const sdk = JSON.parse(await run('npm', ['pack', '--json', '--pack-destination', sdkDir], ts))[0].filename
      consumerManifest.overrides = { '@apostra/sdk': `file:${join(sdkDir, sdk)}` }
    }
    writeFileSync(join(consumer, 'package.json'), JSON.stringify(consumerManifest))
    await run('npm', ['install', '--ignore-scripts', '--no-audit', '--no-fund', join(dir, archive)], consumer)
    process.stdout.write(await run('node', [verifier, '--cli', consumer, published.version, ...(publishedSdk ? [] : [manifest])]))
    process.stdout.write(`@apostra/cli ${published.version} archive installed with ${publishedSdk ? 'the published' : 'the in-tree'} SDK.\n`)
  } finally {
    rmSync(dir, { recursive: true, force: true })
  }
}
if (targets === 'mcp-app-host') {
  await smokeMcpAppHost()
  process.exit(0)
}
if (targets === 'cli') {
  await smokeCli()
  process.exit(0)
}
const tmp = mkdtempSync(join(tmpdir(), 'apostra-install-'))
// These fixtures prove example execution and HTTP mechanics, not live seller
// behaviour, account authorisation or complete business-result schemas.
const requests = []
const server = createServer(async (request, response) => {
  try {
    const chunks = []
    for await (const chunk of request) chunks.push(chunk)
    const body = JSON.parse(Buffer.concat(chunks).toString('utf8'))
    requests.push({ path: request.url, body, headers: request.headers, method: request.method })
    let data
    switch (request.url) {
      case '/api/v3/tools/get_status': data = { account: { id: '12' } }; break
      case '/api/v3/tools/search': data = { objects: { items: [] } }; break
      case '/api/v3/tools/get_delivery':
        data = { report: 'campaign_delivery', page: { nextCursor: body.cursor ? null : 'opaque cursor/+?' } }
        break
      default: throw new Error('Unexpected fixture operation')
    }
    response.writeHead(200, { 'content-type': 'application/json' })
    response.end(JSON.stringify({ data, error: null }))
  } catch {
    response.writeHead(400, { 'content-type': 'application/json' })
    response.end(JSON.stringify({ data: null, error: { code: 'FIXTURE_ERROR', message: 'Unexpected fixture request' } }))
  }
})
async function exerciseJourneys(command, args, language) {
  requests.length = 0
  const address = server.address()
  assert(address && typeof address !== 'string')
  await run(command, args, tmp, {
    APOSTRA_API_KEY: 'install-fixture-key', APOSTRA_ACCOUNT_ID: '12',
    APOSTRA_BASE_URL: `http://127.0.0.1:${address.port}/api/v3`,
    APOSTRA_CAMPAIGN_ID: 'fixture-campaign',
    APOSTRA_START_DATE: '2026-01-01', APOSTRA_END_DATE: '2026-01-02',
    DELIVERY_DATE: '2026-01-02',
  })
  assert.deepEqual(requests.map(r => r.path), [
    '/api/v3/tools/get_status', '/api/v3/tools/search',
    '/api/v3/tools/get_delivery', '/api/v3/tools/get_delivery',
    '/api/v3/tools/get_delivery', '/api/v3/tools/get_delivery',
  ])
  for (const request of requests) {
    assert.equal(request.method, 'POST')
    assert.equal(request.headers.authorization, 'Bearer install-fixture-key')
    assert.equal(request.headers['x-scope3-customer-id'], '12')
    assert.match(request.headers['user-agent'], new RegExp(`^apostra-${language}/`))
  }
  assert.deepEqual(requests[0].body, {})
  assert.deepEqual(requests[1].body, { kind: 'campaign', limit: 20 })
  const delivery = {
    report: 'campaign_delivery', filters: { campaignId: 'fixture-campaign' },
    range: { startDate: '2026-01-01', endDate: '2026-01-02' }, limit: 100,
  }
  assert.deepEqual(requests[2].body, delivery)
  assert.deepEqual(requests[3].body, { ...delivery, cursor: 'opaque cursor/+?' })
  const simulatedDay = { ...delivery, range: { startDate: '2026-01-02', endDate: '2026-01-02' } }
  assert.deepEqual(requests[4].body, simulatedDay)
  assert.deepEqual(requests[5].body, { ...simulatedDay, cursor: 'opaque cursor/+?' })
}
try {
  if (includesTypescript) {
    const packed = JSON.parse(await run('npm',['pack','--json','--pack-destination',tmp],ts))
    assert(packed[0].files.some(file => file.path === 'SKILL.md'), 'npm tarball is missing SKILL.md')
    assert(packed[0].files.some(file => file.path === 'llms.txt'), 'npm tarball is missing llms.txt')
    assert(packed[0].files.some(file => file.path === 'examples/first-value.ts'), 'npm tarball is missing the first-value example')
    writeFileSync(join(tmp,'package.json'),'{}')
    await run('npm',['install','--ignore-scripts','--no-audit','--no-fund',join(tmp,packed[0].filename)],tmp)
    await run('node',[verifier,manifest,tmp])
    writeFileSync(join(tmp,'smoke.mjs'), `import assert from 'node:assert/strict';import {createRequire} from 'node:module';import {Apostra} from '@apostra/sdk';const require=createRequire(import.meta.url);const metadata=require('@apostra/sdk/package.json');assert.equal(metadata.name,'@apostra/sdk');assert.throws(()=>require.resolve('@adcp/sdk'),{code:'MODULE_NOT_FOUND'});let count=0;const api=new Apostra({apiKey:'test',fetch:async()=>{count++;return Response.json({data:{ok:true},error:null})}});assert.equal((await api.getStatus({})).ok,true);assert.equal(count,1);`)
    await run('node',['smoke.mjs'],tmp)
    copyFileSync(join(root, publicTree ? 'examples/sdk-typescript/journeys.ts' : 'mintlify/examples/apostra-developer/sdk-typescript/journeys.ts'), join(tmp,'journeys.mts'))
    writeFileSync(join(tmp,'subpaths.mts'), `import type {SaveRfpRequestJ} from '@apostra/sdk/models'; import {operations,version} from '@apostra/sdk/metadata'; const recursive: SaveRfpRequestJ={nested:[1,true,null]}; const release: string=version; void [recursive,release,operations];`)
    await run(join(ts,'node_modules/.bin/tsc6'),['--noEmit','--strict','--target','ES2022','--module','NodeNext','--moduleResolution','NodeNext','--types','node','--typeRoots',join(ts,'node_modules/@types'),'journeys.mts','subpaths.mts'],tmp)
  }
  if (includesPython) {
    await run('uv',['build','--project',py,'--out-dir',tmp])
    copyFileSync(join(root, publicTree ? 'examples/sdk-python/journeys.py' : 'mintlify/examples/apostra-developer/sdk-python/journeys.py'),join(tmp,'journeys.py'))
  }
  await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',resolve)})
  if (includesTypescript)
    await exerciseJourneys('node',['journeys.mts'],'typescript')
  if (includesPython) {
    const archives = readdirSync(tmp).filter(x=>x.endsWith('.whl') || x.endsWith('.tar.gz'))
    if (archives.length !== 2) throw new Error('Expected wheel and source distribution')
    for (const [index,archive] of archives.entries()) {
    const venv=join(tmp,`venv-${index}`)
    await run('uv',['venv','--python',process.env.SDK_PYTHON ?? '3.12',venv])
    const python=join(venv,'bin/python')
    await run('uv',['pip','install','--python',python,join(tmp,archive),'mypy==1.20.0','pyright==1.1.408'])
    await run(python,['-c',`import sys, tarfile, zipfile
archive = sys.argv[1]
if archive.endswith('.whl'):
    with zipfile.ZipFile(archive) as contents:
        names = contents.namelist()
    assert 'apostra/py.typed' in names
    assert 'apostra/operations.json' in names
    assert 'apostra/SKILL.md' in names
    assert 'apostra/llms.txt' in names
else:
    with tarfile.open(archive) as contents:
        names = [name.split('/', 1)[1] for name in contents.getnames() if '/' in name]
    assert 'src/apostra/py.typed' in names
    assert 'src/apostra/operations.json' in names
    assert 'SKILL.md' in names
    assert 'llms.txt' in names
    assert 'examples/first_value.py' in names
    assert 'pyproject.toml' in names
    assert 'package.json' not in names, 'Private pnpm shim leaked into Python source distribution'
assert names
`,join(tmp,archive)],tmp)
    await run('node',[verifier,manifest,tmp,python])
    await run(python,['-m','mypy','--strict','journeys.py'],tmp)
    await run(python,['-m','pyright','--pythonpath',python,'journeys.py'],tmp)
    await run(python,['-c',`from apostra import Apostra; import importlib.resources; import importlib.util; assert importlib.util.find_spec('adcp') is None; guidance = importlib.resources.files('apostra'); assert guidance.joinpath('SKILL.md').is_file(); assert guidance.joinpath('llms.txt').is_file(); from apostra.models import SaveRfpRequestJ; import httpx; api=Apostra(api_key='test',http_client=httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(200,json={'data': {'ok': True},'error': None})))); assert api.get_status({})['ok']; value: SaveRfpRequestJ={'nested': [1, True, None]}`],tmp)
      await exerciseJourneys(python,['journeys.py'],'python')
    }
  }
  process.stdout.write(`${targets} SDK archive(s) installed; selected shipped journeys compiled and ran against local HTTP fixtures.\n`)
} finally {
  server.closeAllConnections()
  await new Promise(resolve=>server.close(resolve))
  rmSync(tmp,{recursive:true,force:true})
}
