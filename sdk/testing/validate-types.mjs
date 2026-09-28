/** Negative fixtures must fail on each expected line, not on missing imports. */
import { spawnSync } from 'node:child_process'
import { resolve } from 'node:path'
import { readFileSync } from 'node:fs'
const cwd=resolve(process.argv[2] ?? 'packages/apostra-sdk-python')
const interop=process.argv.includes('--adcp')
const file=interop?'adcp_interop_invalid.py':'types_invalid.py'
const expected = readFileSync(resolve(cwd,'tests',file),'utf8').split('\n').flatMap((line,index)=>/^\w+:/.test(line)?[index+1]:[])
if(expected.length===0)throw new Error('Expected nonempty negative type fixtures')
for(const [command,args] of [['mypy',['--strict',`tests/${file}`]],['pyright',['--outputjson',`tests/${file}`]]]) {
 const result=spawnSync('uv',['run','--frozen',...(interop?['--group','interop']:[]),command,...args],{cwd,encoding:'utf8'})
 if(result.error)throw result.error
 if(result.status!==1)throw new Error(`${command} must reject the invalid inputs: ${result.stdout}${result.stderr}`)
 if(command==='pyright') {
   const report=JSON.parse(result.stdout)
   if(report.summary.errorCount<expected.length || report.generalDiagnostics.some(d=>!expected.includes(d.range.start.line+1)) || !expected.every(line=>report.generalDiagnostics.some(d=>d.range.start.line===line-1)))throw new Error(result.stdout)
 } else if(!expected.every(line=>result.stdout.includes(`${file}:${line}: error:`)) || [...result.stdout.matchAll(/\.py:(\d+): error:/g)].some(match=>!expected.includes(Number(match[1]))))throw new Error(result.stdout)
}
process.stdout.write(`mypy and pyright rejected every fixture in ${file}.\n`)
