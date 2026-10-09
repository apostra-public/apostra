/** Check selected SDK release metadata and published-release compatibility. */
import { execFileSync } from 'node:child_process'
import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'

const isPublic = process.argv.includes('--public')
const targetsIndex = process.argv.indexOf('--targets')
const targets = targetsIndex < 0 ? 'both' : process.argv[targetsIndex + 1]
if (!['typescript', 'python', 'both'].includes(targets))
  throw new Error('Pass --targets typescript, python or both')
const includesTypescript = targets === 'typescript' || targets === 'both'
const includesPython = targets === 'python' || targets === 'both'
const root = resolve(isPublic ? 'sdk' : '.')
const read = (path) => readFileSync(resolve(root, path), 'utf8')
const release = JSON.parse(
  read(
    isPublic
      ? 'release/release.json'
      : 'scripts/release/apostra-sdk/release.json',
  ),
)
const typescript = includesTypescript
  ? JSON.parse(
      read(isPublic ? 'typescript/package.json' : 'packages/apostra-sdk/package.json'),
    )
  : undefined
const python = includesPython
  ? read(
      isPublic
        ? 'python/pyproject.toml'
        : 'packages/apostra-sdk-python/pyproject.toml',
    )
  : undefined
const manifest = JSON.parse(
  read(
    isPublic
      ? 'release/manifest.json'
      : 'scripts/codegen/apostra-sdk/manifest.json',
  ),
)
const generatedTypescript = includesTypescript
  ? read(
      isPublic
        ? 'typescript/src/generated/metadata.ts'
        : 'packages/apostra-sdk/src/generated/metadata.ts',
    )
  : undefined
const generatedPython = includesPython
  ? read(
      isPublic
        ? 'python/src/apostra/_version.py'
        : 'packages/apostra-sdk-python/src/apostra/_version.py',
    )
  : undefined
const typescriptVersion = generatedTypescript?.match(
  /^export const version = '([^']+)'$/mu,
)?.[1]
const pythonVersion = generatedPython?.match(/^__version__ = '([^']+)'$/mu)?.[1]

const parseVersion = (value) => {
  const match = /^(\d+)\.(\d+)\.(\d+)$/.exec(value)
  if (!match) throw new Error(`Invalid SDK version: ${value}`)
  return match.slice(1).map(Number)
}
const versionGreaterThan = (next, previous) =>
  next.some(
    (part, index) =>
      part > previous[index] &&
      next.slice(0, index).every((value, earlier) => value === previous[earlier]),
  )
const isBreakingBump = (next, previous) =>
  next[0] > previous[0] ||
  (previous[0] === 0 && next[0] === 0 && next[1] > previous[1])

if (
  !/^\d+\.\d+\.\d+$/.test(release.version) ||
  manifest.version !== release.version ||
  !release.notes.trim()
)
  throw new Error('Release manifest version and notes must agree')

if (
  (includesTypescript &&
    (typescript.version !== release.version || typescriptVersion !== release.version)) ||
  (includesPython &&
    (python.match(/^version = "([^"]+)"$/mu)?.[1] !== release.version ||
      pythonVersion !== release.version))
)
  throw new Error('Selected package versions and generated versions must agree')

const baseIndex = process.argv.indexOf('--base')
if (!isPublic) {
  // Repository PRs keep the currently selected version. The contract job
  // regenerates from the committed OpenAPI instead of relying on a digest.
  process.stdout.write(`${targets} SDK version ${release.version}\n`)
  process.exit(0)
}
if (baseIndex < 0) {
  process.stdout.write(`${targets} SDK version ${release.version}\n`)
  process.exit(0)
}

const base = process.argv[baseIndex + 1]
if (!/^[a-f0-9]{40}$/.test(base))
  throw new Error('Pass an immutable published SDK base SHA')

let previous
try {
  previous = JSON.parse(
    execFileSync('git', ['show', `${base}:sdk/release/manifest.json`], {
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'pipe'],
    }),
  )
} catch (error) {
  // A first publication has no prior manifest. An invalid base is still an
  // error so publication cannot silently skip the comparison.
  execFileSync('git', ['cat-file', '-e', `${base}^{commit}`])
  const files = execFileSync(
    'git',
    ['ls-tree', '-r', '--name-only', base, '--', 'sdk/release/manifest.json'],
    { encoding: 'utf8' },
  )
  if (files.trim()) throw error
}

if (previous) {
  const nextVersion = parseVersion(release.version)
  const previousVersion = parseVersion(previous.version)
  if (!versionGreaterThan(nextVersion, previousVersion))
    throw new Error(
      'Published SDK version must be greater than the last published version',
    )

  const removedOperations = (previous.operations ?? []).filter(
    (operation) => !(manifest.operations ?? []).includes(operation),
  )
  if (removedOperations.length > 0 && !isBreakingBump(nextVersion, previousVersion))
    throw new Error(
      `Published SDK operations were removed (${removedOperations.join(', ')}): require a major bump (minor before 1.0)`,
    )
}

process.stdout.write(`${targets} SDK version ${release.version}\n`)
