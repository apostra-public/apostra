/** Set selected public SDK build inputs to the reviewed release version. */
import { readFileSync, writeFileSync } from 'node:fs'

const version = process.argv[2]
const targets = process.argv[3] ?? 'both'
if (!/^\d+\.\d+\.\d+$/.test(version ?? ''))
  throw new Error('Pass the reviewed SDK version as x.y.z')
if (!['typescript', 'python', 'both'].includes(targets))
  throw new Error('Pass targets as typescript, python or both')

const readJson = (path) => JSON.parse(readFileSync(path, 'utf8'))
const writeJson = (path, value) =>
  writeFileSync(path, `${JSON.stringify(value, null, 2)}\n`)
const replace = (path, expression, replacement) => {
  const source = readFileSync(path, 'utf8')
  const next = source.replace(expression, replacement)
  if (next === source) throw new Error(`Could not update SDK version in ${path}`)
  writeFileSync(path, next)
}

const release = readJson('sdk/release/release.json')
release.version = version
writeJson('sdk/release/release.json', release)

const manifest = readJson('sdk/release/manifest.json')
manifest.version = version
writeJson('sdk/release/manifest.json', manifest)

if (targets === 'typescript' || targets === 'both') {
  const packageJson = readJson('sdk/typescript/package.json')
  packageJson.version = version
  writeJson('sdk/typescript/package.json', packageJson)
  replace(
    'sdk/typescript/src/generated/metadata.ts',
    /^export const version = '.*'$/mu,
    `export const version = '${version}'`,
  )
}

if (targets === 'python' || targets === 'both') {
  const pythonPackage = readJson('sdk/python/package.json')
  pythonPackage.version = version
  writeJson('sdk/python/package.json', pythonPackage)
  replace('sdk/python/pyproject.toml', /^version = ".*"$/mu, `version = "${version}"`)
  replace('sdk/python/src/apostra/_version.py', /^__version__ = '.*'$/mu, `__version__ = '${version}'`)
}
