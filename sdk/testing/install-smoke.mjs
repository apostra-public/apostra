/** Build and install actual archives in isolation, never through workspace links. */
import assert from 'node:assert/strict'
import { execFile } from 'node:child_process'
import { createServer } from 'node:http'
import { promisify } from 'node:util'
import { copyFileSync, mkdtempSync, readdirSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { resolve, join } from 'node:path'

const root = resolve(process.argv[2] ?? '.')
const publicTree = process.argv.includes('--public')
const ts = join(root, publicTree ? 'sdk/typescript' : 'packages/apostra-sdk')
const py = join(root, publicTree ? 'sdk/python' : 'packages/apostra-sdk-python')
const manifest = join(root, publicTree ? 'sdk/release/manifest.json' : 'scripts/codegen/apostra-sdk/manifest.json')
const verifier = join(root, publicTree ? 'sdk/testing/verify-installed.mjs' : 'scripts/testing/apostra-sdk/verify-installed.mjs')
const tmp = mkdtempSync(join(tmpdir(), 'apostra-install-'))
async function run(command, args, cwd = root, env = {}) {
  return (await promisify(execFile)(command,args,{cwd,env:{...process.env,...env},encoding:'utf8',timeout:180_000,maxBuffer:4*1024*1024})).stdout
}
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
  })
  assert.deepEqual(requests.map(r => r.path), [
    '/api/v3/tools/get_status', '/api/v3/tools/search',
    '/api/v3/tools/get_delivery', '/api/v3/tools/get_delivery',
  ])
  for (const request of requests) {
    assert.equal(request.method, 'POST')
    assert.equal(request.headers.authorization, 'Bearer install-fixture-key')
    assert.equal(request.headers['x-scope3-customer-id'], '12')
    assert.match(request.headers['user-agent'], new RegExp(`^apostra-${language}/`))
  }
  assert.deepEqual(requests[0].body, {})
  assert.deepEqual(requests[1].body, { kind: 'inventory_source', limit: 20 })
  const delivery = {
    report: 'campaign_delivery', filters: { campaignId: 'fixture-campaign' },
    range: { startDate: '2026-01-01', endDate: '2026-01-02' }, limit: 100,
  }
  assert.deepEqual(requests[2].body, delivery)
  assert.deepEqual(requests[3].body, { ...delivery, cursor: 'opaque cursor/+?' })
}
try {
  const packed = JSON.parse(await run('npm',['pack','--json','--pack-destination',tmp],ts))
  assert(packed[0].files.some(file => file.path === 'SKILL.md'), 'npm tarball is missing SKILL.md')
  assert(packed[0].files.some(file => file.path === 'llms.txt'), 'npm tarball is missing llms.txt')
  assert(packed[0].files.some(file => file.path === 'examples/first-value.ts'), 'npm tarball is missing the first-value example')
  await run('uv',['build','--project',py,'--out-dir',tmp])
  writeFileSync(join(tmp,'package.json'),'{}')
  await run('npm',['install','--ignore-scripts','--no-audit','--no-fund',join(tmp,packed[0].filename)],tmp)
  await run('node',[verifier,manifest,tmp])
  writeFileSync(join(tmp,'smoke.mjs'), `import assert from 'node:assert/strict';import {createRequire} from 'node:module';import {Apostra} from '@apostra/sdk';const require=createRequire(import.meta.url);const metadata=require('@apostra/sdk/package.json');assert.equal(metadata.name,'@apostra/sdk');assert.throws(()=>require.resolve('@adcp/sdk'),{code:'MODULE_NOT_FOUND'});let count=0;const api=new Apostra({apiKey:'test',fetch:async()=>{count++;return Response.json({data:{ok:true},error:null})}});assert.equal((await api.getStatus({})).ok,true);assert.equal(count,1);`)
  await run('node',['smoke.mjs'],tmp)
  copyFileSync(join(root, publicTree ? 'examples/sdk-typescript/journeys.ts' : 'mintlify/examples/apostra-developer/sdk-typescript/journeys.ts'), join(tmp,'journeys.mts'))
  writeFileSync(join(tmp,'subpaths.mts'), `import type {SaveRfpRequestJ} from '@apostra/sdk/models'; import {operations,version} from '@apostra/sdk/metadata'; const recursive: SaveRfpRequestJ={nested:[1,true,null]}; const release: string=version; void [recursive,release,operations];`)
  await run(join(ts,'node_modules/.bin/tsc6'),['--noEmit','--strict','--target','ES2022','--module','NodeNext','--moduleResolution','NodeNext','--types','node','--typeRoots',join(ts,'node_modules/@types'),'journeys.mts','subpaths.mts'],tmp)
  copyFileSync(join(root, publicTree ? 'examples/sdk-python/journeys.py' : 'mintlify/examples/apostra-developer/sdk-python/journeys.py'),join(tmp,'journeys.py'))
  await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',resolve)})
  await exerciseJourneys('node',['journeys.mts'],'typescript')
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
  process.stdout.write('npm tarball, wheel and source distribution installed; both shipped journeys compiled and ran against local HTTP fixtures for each archive.\n')
} finally {
  server.closeAllConnections()
  await new Promise(resolve=>server.close(resolve))
  rmSync(tmp,{recursive:true,force:true})
}
