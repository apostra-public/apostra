import { operations, version } from '@apostra/sdk/metadata'

export type OperationName = keyof typeof operations
export type OperationSummary = {
  name: OperationName
  method: string
  path: string
  summary: string
}
export type OperationDetail = OperationSummary & {
  /** True for a write: `call` then requires `--idempotency-key`. */
  idempotencyKey: boolean
  parameters: { name: string; location: string; required: boolean }[]
}

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

export function operationDetail(summary: OperationSummary): OperationDetail {
  const { idempotencyKey, parameters } = operations[summary.name]
  return {
    ...summary,
    idempotencyKey,
    parameters: parameters.map(({ name, location, required }) => ({
      name,
      location,
      required,
    })),
  }
}

export const operationsData = () => ({
  sdkVersion: version,
  operations: listOperations(),
})
