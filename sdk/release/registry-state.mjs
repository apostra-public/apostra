/** Refuse mismatched existing releases; allow byte-identical partial-run recovery. */
import { createHash } from 'node:crypto'
import { readFileSync, readdirSync, appendFileSync } from 'node:fs'
const targetsIndex=process.argv.indexOf('--targets')
const targets=targetsIndex<0?'both':process.argv[targetsIndex+1]
if(!['typescript','python','both','mcp-app-host'].includes(targets))throw new Error('Pass --targets typescript, python, both or mcp-app-host')
// The MCP Apps host package is a separate npm package with its own version, so
// it is checked against its package.json instead of the paired SDK release.
const hostPackage=targets==='mcp-app-host'?JSON.parse(readFileSync('sdk/mcp-app-host/package.json','utf8')):undefined
const npmName=hostPackage?.name??'@apostra/sdk'
const includesTypescript=targets==='typescript'||targets==='both'||targets==='mcp-app-host'
const includesPython=targets==='python'||targets==='both'
// The publish job checks out the unversioned source, so the build job's reviewed
// version must be passed in; release.json and the package.json only reflect the
// source default.
const versionIndex=process.argv.indexOf('--version')
const sourceVersion=()=>(hostPackage??JSON.parse(readFileSync('sdk/release/release.json','utf8'))).version
const release={version:versionIndex<0?sourceVersion():process.argv[versionIndex+1]}
if(!/^\d+\.\d+\.\d+$/.test(release.version??''))throw new Error('Pass the reviewed SDK version as --version x.y.z')
const files=readdirSync('artifacts')
async function get(url) { const response=await fetch(url,{signal:AbortSignal.timeout(10_000)});if(response.status===404)return null;if(!response.ok)throw new Error(`Registry lookup failed: ${response.status}`);return response.json() }
function versionGreaterThan(next,previous) { const nextParts=next.split('.').map(Number);const previousParts=previous.split('.').map(Number);if(nextParts.length!==3||previousParts.length!==3||nextParts.some(Number.isNaN)||previousParts.some(Number.isNaN))throw new Error('Registry latest version must be x.y.z');return nextParts.some((part,index)=>part>previousParts[index]&&nextParts.slice(0,index).every((value,earlier)=>value===previousParts[earlier])) }
const output=[]
if(includesTypescript) {
  const npmPath=npmName.replace('/','%2f')
  const npm=await get(`https://registry.npmjs.org/${npmPath}/${release.version}`)
  const npmPackage=npm ?? await get(`https://registry.npmjs.org/${npmPath}`)
  const tar=files.find(x=>x.endsWith('.tgz'))
  if (!tar) throw new Error('Missing npm archive')
  if(npm && npm.dist.integrity!==`sha512-${createHash('sha512').update(readFileSync(`artifacts/${tar}`)).digest('base64')}`)throw new Error('Existing npm version differs from release artifact')
  const npmLatest=npmPackage?.['dist-tags']?.latest
  if(!npm&&npmLatest&&!versionGreaterThan(release.version,npmLatest))throw new Error('New npm SDK version must be greater than the registry latest version')
  output.push(`npm_version_exists=${Boolean(npm)}`,`npm_package_exists=${Boolean(npmPackage)}`)
}
if(includesPython) {
  const pypi=await get(`https://pypi.org/pypi/apostra/${release.version}/json`)
  const pypiPackage=pypi ?? await get('https://pypi.org/pypi/apostra/json')
  const python=files.filter(x=>x.endsWith('.whl')||x.endsWith('.tar.gz'))
  if(python.length!==2)throw new Error('Expected two Python archives')
  if(pypi && (pypi.urls.length!==python.length || python.some(name=>!pypi.urls.some(file=>file.filename===name && file.digests.sha256===createHash('sha256').update(readFileSync(`artifacts/${name}`)).digest('hex')))))throw new Error('Existing PyPI version differs, is incomplete or has unexpected distributions; reconcile the partial upload manually')
  const pypiLatest=pypiPackage?.info?.version
  if(!pypi&&pypiLatest&&!versionGreaterThan(release.version,pypiLatest))throw new Error('New PyPI SDK version must be greater than the registry latest version')
  output.push(`pypi_version_exists=${Boolean(pypi)}`)
}
appendFileSync(process.env.GITHUB_OUTPUT,`${output.join('\n')}\n`)
