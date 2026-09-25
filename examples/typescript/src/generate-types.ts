/**
 * Generate TypeScript types from the live tool schemas.
 *
 * The schemas the server publishes are what every request is validated
 * against. Generating from them lets `tsc` surface incompatible type or enum
 * changes and newly required fields. These are static projections, not runtime
 * validators: review the generated diff and keep server validation in place.
 *
 * Read the schema before writing the call. This makes that the default.
 */

/** One entry of a `tools/list` response, narrowed to what codegen needs. */
export interface ToolSchema {
  name: string;
  description?: string;
  inputSchema: JsonSchema;
}

export interface JsonSchema {
  type?: string | string[];
  description?: string;
  properties?: Record<string, JsonSchema>;
  required?: string[];
  items?: JsonSchema;
  enum?: unknown[];
  const?: unknown;
  oneOf?: JsonSchema[];
  anyOf?: JsonSchema[];
  allOf?: JsonSchema[];
  $ref?: string;
  $defs?: Record<string, JsonSchema>;
  additionalProperties?: boolean | JsonSchema;
}

export interface ToolCatalogClient {
  listTools(params?: { cursor?: string }): Promise<{
    tools: unknown[];
    nextCursor?: string;
  }>;
}

interface RenderContext {
  toolName: string;
  refs: ReadonlyMap<string, string>;
}

/**
 * Render one module declaring an input type per tool.
 *
 * Each tool's `$defs` become namespaced types. JSON Schema references are local
 * to one tool document, so definitions from different tools must never share a
 * name merely because their `$defs` keys match.
 */
export function renderTypes(tools: readonly ToolSchema[]): string {
  const blocks: string[] = [
    "// Generated from the live tool schemas. Do not edit by hand.",
    "// Regenerate with: npm run types:generate",
    "// Static projection only: server schema validation remains authoritative.",
    "// Runtime-only rules can include values, keys, dependencies, conditionals, exclusions, tuple bounds, and oneOf exclusivity.",
  ];

  const emittedNames = new Map<string, string>();
  const claimName = (name: string, owner: string): string => {
    const existing = emittedNames.get(name);
    if (existing) {
      throw new Error(
        `Generated type name ${JSON.stringify(name)} collides between ${existing} and ${owner}`,
      );
    }
    emittedNames.set(name, owner);
    return name;
  };

  const contexts = tools.map((tool) => {
    const toolTypeName = typeName(tool.name);
    const inputName = claimName(
      `${toolTypeName}Input`,
      `tool ${JSON.stringify(tool.name)}`,
    );
    const refs = new Map(
      Object.keys(tool.inputSchema.$defs ?? {}).map((name) => [
        definitionRef(name),
        claimName(
          `${toolTypeName}${typeName(name)}`,
          `definition ${JSON.stringify(name)} in tool ${JSON.stringify(tool.name)}`,
        ),
      ]),
    );
    return { tool, inputName, refs };
  });

  for (const { tool, refs } of contexts) {
    const context = { toolName: tool.name, refs };
    const definitions = Object.entries(tool.inputSchema.$defs ?? {}).sort(
      ([a], [b]) => a.localeCompare(b),
    );
    for (const [name, schema] of definitions) {
      blocks.push(
        `${docComment(schema.description, "")}export type ${refs.get(definitionRef(name))} = ${render(schema, 0, context, definitionRef(name))};`,
      );
    }
  }

  for (const { tool, inputName, refs } of contexts) {
    const context = { toolName: tool.name, refs };
    blocks.push(
      `${docComment(tool.description, "")}export type ${inputName} = ${render(tool.inputSchema, 0, context, "#")};`,
    );
  }

  return `${blocks.join("\n\n")}\n`;
}

function render(
  schema: JsonSchema,
  depth: number,
  context: RenderContext,
  path: string,
): string {
  if (schema.allOf !== undefined) {
    const { allOf, ...base } = schema;
    return [base, ...allOf]
      .map(
        (member, index) =>
          `(${render(member, depth, context, index === 0 ? path : `${path}/allOf/${index - 1}`)})`,
      )
      .join(" & ");
  }
  if (schema.$ref) {
    const resolved = context.refs.get(schema.$ref);
    if (!resolved) {
      throw new Error(
        `Tool ${JSON.stringify(context.toolName)} has an unsupported or unresolved schema reference at ${path}: ${schema.$ref}`,
      );
    }
    const siblings = { ...schema };
    delete siblings.$ref;
    return hasTypeProjection(siblings)
      ? `(${resolved}) & (${render(siblings, depth, context, path)})`
      : resolved;
  }
  if (schema.const !== undefined) {
    const siblings = { ...schema };
    delete siblings.const;
    const constant = JSON.stringify(schema.const);
    return hasTypeProjection(siblings)
      ? `(${constant}) & (${render(siblings, depth, context, path)})`
      : constant;
  }
  if (schema.enum) {
    const siblings = { ...schema };
    delete siblings.enum;
    const values =
      schema.enum.length === 0
        ? "never"
        : schema.enum.map((value) => JSON.stringify(value)).join(" | ");
    return hasTypeProjection(siblings)
      ? `(${values}) & (${render(siblings, depth, context, path)})`
      : values;
  }

  if (schema.oneOf !== undefined || schema.anyOf !== undefined) {
    const intersections: string[] = [];
    for (const [keyword, union] of [
      ["oneOf", schema.oneOf],
      ["anyOf", schema.anyOf],
    ] as const) {
      if (union === undefined) continue;
      const renderedUnion =
        union.length === 0
          ? "never"
          : union
              .map((member, index) =>
                render(member, depth, context, `${path}/${keyword}/${index}`),
              )
              .join(" | ");
      intersections.push(`(${renderedUnion})`);
    }
    const siblings = { ...schema };
    delete siblings.oneOf;
    delete siblings.anyOf;
    if (hasTypeProjection(siblings)) {
      intersections.unshift(`(${render(siblings, depth, context, path)})`);
    }
    return intersections.join(" & ");
  }

  if (Array.isArray(schema.type)) {
    return schema.type
      .map((type) => render({ ...schema, type }, depth, context, path))
      .join(" | ");
  }

  switch (schema.type) {
    case "string":
      return "string";
    case "number":
    case "integer":
      return "number";
    case "boolean":
      return "boolean";
    case "null":
      return "null";
    case "array":
      return schema.items
        ? `Array<${render(schema.items, depth, context, `${path}/items`)}>`
        : "unknown[]";
    case "object":
      return renderObject(schema, depth, context, path);
    default:
      // An unconstrained schema is `unknown`, never `any`: the caller must
      // narrow it rather than inherit a hole in the contract.
      return schema.properties
        ? renderObject(schema, depth, context, path)
        : "unknown";
  }
}

function hasTypeProjection(schema: JsonSchema): boolean {
  return (
    schema.type !== undefined ||
    schema.properties !== undefined ||
    schema.items !== undefined ||
    schema.enum !== undefined ||
    schema.const !== undefined ||
    schema.oneOf !== undefined ||
    schema.anyOf !== undefined ||
    schema.allOf !== undefined ||
    schema.$ref !== undefined
  );
}

function renderObject(
  schema: JsonSchema,
  depth: number,
  context: RenderContext,
  path: string,
): string {
  const properties = Object.entries(schema.properties ?? {});
  if (properties.length === 0) {
    const valueType =
      schema.additionalProperties === false
        ? "never"
        : typeof schema.additionalProperties === "object"
          ? render(
              schema.additionalProperties,
              depth + 1,
              context,
              `${path}/additionalProperties`,
            )
          : "unknown";
    const inner = "  ".repeat(depth + 1);
    const closing = "  ".repeat(depth);
    return `{\n${inner}[key: string]: ${valueType};\n${closing}}`;
  }
  const required = new Set(schema.required ?? []);
  const inner = "  ".repeat(depth + 1);
  const closing = "  ".repeat(depth);

  const lines = properties.map(([name, property]) => {
    const optional = required.has(name) ? "" : "?";
    const propertyPath = `${path}/properties/${jsonPointerToken(name)}`;
    return `${docComment(property.description, inner)}${inner}${propertyKey(name)}${optional}: ${render(property, depth + 1, context, propertyPath)};`;
  });
  if (
    schema.additionalProperties === undefined ||
    schema.additionalProperties
  ) {
    if (typeof schema.additionalProperties === "object") {
      lines.push(`${inner}[key: string]: unknown;`);
      return `{\n${lines.join("\n")}\n${closing}}`;
    }
    lines.push(`${inner}[key: string]: unknown;`);
  }

  return `{\n${lines.join("\n")}\n${closing}}`;
}

/** JSDoc above a member, or nothing when the schema documents nothing. */
function docComment(description: string | undefined, indent: string): string {
  if (!description) return "";
  const body = description
    .replaceAll("*/", "*\\/")
    .split("\n")
    .map((line) => `${indent} * ${line}`.trimEnd())
    .join("\n");
  return `${indent}/**\n${body}\n${indent} */\n`;
}

function propertyKey(name: string): string {
  return /^[A-Za-z_$][A-Za-z0-9_$]*$/.test(name) ? name : JSON.stringify(name);
}

function definitionRef(name: string): string {
  return `#/$defs/${jsonPointerToken(name)}`;
}

function jsonPointerToken(value: string): string {
  return value.replace(/~/g, "~0").replace(/\//g, "~1");
}

/** `save_campaign` and `__schema47` both become valid PascalCase identifiers. */
export function typeName(raw: string): string {
  const parts = raw.split(/[^A-Za-z0-9]+/).filter(Boolean);
  const pascal = parts
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join("");
  if (!pascal) return "Schema";
  return /^[0-9]/.test(pascal) ? `Schema${pascal}` : pascal;
}

/** Fetch every page from `tools/list`, preserving the server's tool order. */
export async function listAllTools(
  client: ToolCatalogClient,
): Promise<ToolSchema[]> {
  const tools: ToolSchema[] = [];
  const seenCursors = new Set<string>();
  let cursor: string | undefined;

  while (true) {
    const page = await client.listTools(cursor ? { cursor } : undefined);
    tools.push(...(page.tools as ToolSchema[]));

    const nextCursor = page.nextCursor;
    if (!nextCursor) return tools;
    if (seenCursors.has(nextCursor)) {
      throw new Error(`tools/list repeated cursor: ${nextCursor}`);
    }
    seenCursors.add(nextCursor);
    cursor = nextCursor;
  }
}

/**
 * Fetch the live tool schemas and write them as TypeScript.
 *
 * Kept separate from `renderTypes` so the rendering rules stay testable
 * without a network or an account.
 */
export async function generateTypes(
  token: string,
  outputPath: string,
): Promise<number> {
  const { writeFile, mkdir } = await import("node:fs/promises");
  const { dirname } = await import("node:path");
  const { withApostraSession } = await import("./main.js");

  const tools = await withApostraSession(token, listAllTools);

  await mkdir(dirname(outputPath), { recursive: true });
  await writeFile(outputPath, renderTypes(tools), "utf8");
  return tools.length;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const token = process.env.APOSTRA_ACCESS_TOKEN;
  if (!token) throw new Error("Set APOSTRA_ACCESS_TOKEN before running");
  const outputPath = process.argv[2] ?? "src/generated/tools.ts";
  const count = await generateTypes(token, outputPath);
  console.log(`Wrote ${count} tool input types to ${outputPath}`);
}
