import { createHash } from 'node:crypto'
/** Paired-version and conservative contract compatibility admission. */
import { execFileSync } from 'node:child_process'
import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'
const root=resolve(process.argv.includes('--public') ? 'sdk' : '.')
const read=p=>readFileSync(resolve(root,p),'utf8')
const isPublic=process.argv.includes('--public')
const release=JSON.parse(read(isPublic?'release/release.json':'scripts/release/apostra-sdk/release.json'))
const ts=JSON.parse(read(isPublic?'typescript/package.json':'packages/apostra-sdk/package.json'))
const py=read(isPublic?'python/pyproject.toml':'packages/apostra-sdk-python/pyproject.toml')
const manifest=JSON.parse(read(isPublic?'release/manifest.json':'scripts/codegen/apostra-sdk/manifest.json'))
if (!/^\d+\.\d+\.\d+$/.test(release.version) || ts.version!==release.version || py.match(/^version = "([^"]+)"/m)?.[1]!==release.version || manifest.version!==release.version || !release.notes.trim()) throw new Error('Package versions, generated version and release notes must agree')
const spec=read(isPublic?'openapi.yaml':'mintlify/v2/v3-api-3.1.yaml')
if(createHash('sha256').update(spec).digest('hex')!==manifest.sha256)throw new Error('OpenAPI digest does not match generated sources')
const baseArg=process.argv.indexOf('--base')
if (isPublic && baseArg<0) throw new Error('Public SDK validation requires an immutable base SHA')
if (baseArg>=0) {
  const base=process.argv[baseArg+1]
  if (!/^[a-f0-9]{40}$/.test(base)) throw new Error('Pass an immutable base SHA')
  const path=isPublic?'sdk/release/manifest.json':'scripts/codegen/apostra-sdk/manifest.json'
  let old
  try { old=JSON.parse(execFileSync('git',['show',`${base}:${path}`],{encoding:'utf8',stdio:['ignore','pipe','pipe']})) } catch(error) {
    // A missing first-release manifest is expected; an invalid ref is not.
    execFileSync('git',['cat-file','-e',`${base}^{commit}`])
    const files=execFileSync('git',['ls-tree','-r','--name-only',base,'--',path],{encoding:'utf8'})
    if (files.trim()) throw error
  }
  if (old) {
    const changes=execFileSync('git',['diff','--name-only',base,'--',...(isPublic?['sdk/typescript/src','sdk/python/src']:['packages/apostra-sdk/src','packages/apostra-sdk-python/src'])],{encoding:'utf8'})
    const now=release.version.split('.').map(Number), before=old.version.split('.').map(Number)
    const greater=now.some((n,i)=>n>before[i] && now.slice(0,i).every((x,j)=>x===before[j]))
    if(changes.trim() && !greater)throw new Error('SDK source changed: increase both package versions')
  }
  if (old && old.sha256!==manifest.sha256) {
    const [major,minor]=release.version.split('.').map(Number)
    const [oldMajor,oldMinor]=old.version.split('.').map(Number)
    if (!(major>oldMajor || (oldMajor===0 && major===0 && minor>oldMinor))) throw new Error('Potential breaking OpenAPI change: require a major bump (minor before 1.0) and reviewed release notes')
  }
}
process.stdout.write(`Coordinated SDK version ${release.version}\n`)
