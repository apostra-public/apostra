/** Refuse mismatched existing releases; allow byte-identical partial-run recovery. */
import { createHash } from 'node:crypto'
import { readFileSync, readdirSync, appendFileSync } from 'node:fs'
const release=JSON.parse(readFileSync('sdk/release/release.json','utf8'))
const files=readdirSync('artifacts')
async function get(url) { const response=await fetch(url,{signal:AbortSignal.timeout(10_000)});if(response.status===404)return null;if(!response.ok)throw new Error(`Registry lookup failed: ${response.status}`);return response.json() }
const npm=await get(`https://registry.npmjs.org/@apostra%2fsdk/${release.version}`)
const npmPackage=npm ?? await get('https://registry.npmjs.org/@apostra%2fsdk')
const tar=files.find(x=>x.endsWith('.tgz'))
if (!tar) throw new Error('Missing npm archive')
if(npm && npm.dist.integrity!==`sha512-${createHash('sha512').update(readFileSync(`artifacts/${tar}`)).digest('base64')}`)throw new Error('Existing npm version differs from release artifact')
const pypi=await get(`https://pypi.org/pypi/apostra/${release.version}/json`)
const python=files.filter(x=>x.endsWith('.whl')||x.endsWith('.tar.gz'))
if(python.length!==2)throw new Error('Expected two Python archives')
if(pypi && (pypi.urls.length!==python.length || python.some(name=>!pypi.urls.some(file=>file.filename===name && file.digests.sha256===createHash('sha256').update(readFileSync(`artifacts/${name}`)).digest('hex')))))throw new Error('Existing PyPI version differs, is incomplete or has unexpected distributions; reconcile the partial upload manually')
appendFileSync(process.env.GITHUB_OUTPUT,`npm_version_exists=${Boolean(npm)}\nnpm_package_exists=${Boolean(npmPackage)}\npypi_version_exists=${Boolean(pypi)}\n`)
