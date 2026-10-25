import { operations, version } from '@apostra/sdk/metadata'

export type OperationName = keyof typeof operations
export type OperationSummary = {
  name: OperationName
  method: string
  path: string
  summary: string
}

export const cliEnvelopeVersion = 1

export function listOperations(): OperationSummary[] {
  return (
    Object.entries(operations) as [
      OperationName,
      (typeof operations)[OperationName],
    ][]
  )
    .map(([name, operation]) => ({
      name,
      method: operation.method,
      path: operation.path,
      summary: operation.summary,
    }))
    .sort((left, right) => left.name.localeCompare(right.name))
}

export function describeOperation(name: string): OperationSummary | undefined {
  return listOperations().find((operation) => operation.name === name)
}

export function operationsEnvelope() {
  return {
    version: cliEnvelopeVersion,
    sdkVersion: version,
    operations: listOperations(),
  }
}
