import assert from "node:assert/strict";
import test from "node:test";
import * as ts from "typescript";

import {
  listAllTools,
  renderTypes,
  typeName,
  type ToolSchema,
} from "./generate-types.js";

/** The save_campaign shape, reduced to the fields that are easy to guess wrong. */
const SAVE_CAMPAIGN: ToolSchema = {
  name: "save_campaign",
  description: "Create or update a campaign.",
  inputSchema: {
    type: "object",
    required: ["idempotencyKey"],
    properties: {
      idempotencyKey: { type: "string", description: "Stable key per call." },
      expectedRevision: {
        type: "integer",
        description: "Revision from last get.",
      },
      desiredPhase: { type: "string", enum: ["active", "canceled"] },
      confirmLaunch: { type: "boolean" },
      flight: {
        type: "object",
        required: ["startAt", "endAt"],
        properties: {
          startAt: { type: "string" },
          endAt: { type: "string" },
        },
      },
      brief: { type: ["string", "null"] },
    },
  },
};

test("a numeric revision generates as a number, not a string", () => {
  const output = renderTypes([SAVE_CAMPAIGN]);

  assert.match(output, /expectedRevision\?: number;/);
});

test("an enum generates as its literal union so an invalid phase fails to compile", () => {
  const output = renderTypes([SAVE_CAMPAIGN]);

  assert.match(
    output,
    /desiredPhase\?: \("active" \| "canceled"\) & \(string\);/,
  );
});

test("a required field is not optional", () => {
  const output = renderTypes([SAVE_CAMPAIGN]);

  assert.match(output, /idempotencyKey: string;/);
});

test("nested objects keep the schema's own field names", () => {
  const output = renderTypes([SAVE_CAMPAIGN]);

  assert.match(output, /startAt: string;/);
  assert.match(output, /endAt: string;/);
});

test("a nullable field generates as a union with null", () => {
  const output = renderTypes([SAVE_CAMPAIGN]);

  assert.match(output, /brief\?: string \| null;/);
});

test("field descriptions carry through as JSDoc", () => {
  const output = renderTypes([SAVE_CAMPAIGN]);

  assert.match(output, /\* Stable key per call\./);
});

test("schema prose cannot terminate generated JSDoc", () => {
  const output = renderTypes([
    {
      name: "save_note",
      description: "Keep */ inside the comment.",
      inputSchema: { type: "object" },
    },
  ]);

  assert.match(output, /Keep \*\\\/ inside the comment\./);
  assert.doesNotMatch(output, /Keep \*\/ inside the comment\./);
});

test("definitions become tool-scoped named types instead of repeated inline blobs", () => {
  const output = renderTypes([
    {
      name: "save_media_buy",
      inputSchema: {
        type: "object",
        $defs: {
          Budget: { type: "object", properties: { total: { type: "number" } } },
        },
        properties: { budget: { $ref: "#/$defs/Budget" } },
      },
    },
  ]);

  assert.match(output, /export type SaveMediaBuyBudget = \{/);
  assert.match(output, /budget\?: SaveMediaBuyBudget;/);
});

test("same-named definitions keep their own tool's shape and reference", () => {
  const output = renderTypes([
    {
      name: "save_campaign",
      inputSchema: {
        type: "object",
        $defs: {
          Budget: {
            type: "object",
            properties: { total: { type: "number" } },
          },
        },
        properties: { budget: { $ref: "#/$defs/Budget" } },
      },
    },
    {
      name: "save_media_buy",
      inputSchema: {
        type: "object",
        $defs: {
          Budget: {
            type: "object",
            properties: { amount: { type: "string" } },
          },
        },
        properties: { budget: { $ref: "#/$defs/Budget" } },
      },
    },
  ]);

  assert.match(
    output,
    /export type SaveCampaignBudget = \{\n  total\?: number;/,
  );
  assert.match(
    output,
    /export type SaveMediaBuyBudget = \{\n  amount\?: string;/,
  );
  assert.match(
    output,
    /export type SaveCampaignInput = \{\n  budget\?: SaveCampaignBudget;/,
  );
  assert.match(
    output,
    /export type SaveMediaBuyInput = \{\n  budget\?: SaveMediaBuyBudget;/,
  );
});

test("a schema with no constraints generates unknown rather than any", () => {
  const output = renderTypes([
    {
      name: "get",
      inputSchema: { type: "object", properties: { filter: {} } },
    },
  ]);

  assert.match(output, /filter\?: unknown;/);
});

test("a closed empty object rejects every property", () => {
  const output = renderTypes([
    {
      name: "get_status",
      inputSchema: { type: "object", additionalProperties: false },
    },
  ]);

  assert.match(
    output,
    /export type GetStatusInput = \{\n  \[key: string\]: never;/,
  );
});

test("a dictionary keeps its additional property value type", () => {
  const output = renderTypes([
    {
      name: "save_scores",
      inputSchema: {
        type: "object",
        additionalProperties: { type: "number" },
      },
    },
  ]);

  assert.match(
    output,
    /export type SaveScoresInput = \{\n  \[key: string\]: number;/,
  );
});

test("an unconstrained object remains an unknown-valued dictionary", () => {
  const output = renderTypes([
    { name: "save_metadata", inputSchema: { type: "object" } },
  ]);

  assert.match(
    output,
    /export type SaveMetadataInput = \{\n  \[key: string\]: unknown;/,
  );
});

test("object schema variants produce a valid TypeScript module", () => {
  const output = renderTypes([
    {
      name: "get_status",
      inputSchema: { type: "object", additionalProperties: false },
    },
    {
      name: "save_scores",
      inputSchema: {
        type: "object",
        additionalProperties: { type: "number" },
      },
    },
    { name: "save_metadata", inputSchema: { type: "object" } },
  ]);
  const diagnostics =
    ts.transpileModule(output, {
      compilerOptions: { module: ts.ModuleKind.ESNext },
      fileName: "generated-tools.ts",
      reportDiagnostics: true,
    }).diagnostics ?? [];

  assert.deepEqual(
    diagnostics.filter(
      ({ category }) => category === ts.DiagnosticCategory.Error,
    ),
    [],
  );
});

test("a mixed named-and-dictionary object keeps named fields assignable", () => {
  const output = renderTypes([
    {
      name: "save_configuration",
      inputSchema: {
        type: "object",
        properties: {
          configuration: {
            type: "object",
            properties: { name: { type: "string" } },
            additionalProperties: { type: "number" },
          },
        },
      },
    },
  ]);

  assert.match(
    output,
    /configuration\?: \{\n    name\?: string;\n    \[key: string\]: unknown;\n  \};/,
  );
});

test("a closed object with named properties omits the open index signature", () => {
  const output = renderTypes([
    {
      name: "save_configuration",
      inputSchema: {
        type: "object",
        properties: {
          configuration: {
            type: "object",
            properties: { name: { type: "string" } },
            additionalProperties: false,
          },
        },
      },
    },
  ]);

  assert.match(output, /configuration\?: \{\n    name\?: string;\n  \};/);
  assert.doesNotMatch(
    output,
    /configuration\?: \{\n    name\?: string;\n    \[key: string\]: unknown;/,
  );
});

test("an open object with named properties accepts unknown extension fields", () => {
  for (const additionalProperties of [undefined, true]) {
    const output = renderTypes([
      {
        name: "save_configuration",
        inputSchema: {
          type: "object",
          properties: { name: { type: "string" } },
          additionalProperties,
        },
      },
    ]);

    assert.match(
      output,
      /export type SaveConfigurationInput = \{\n  name\?: string;\n  \[key: string\]: unknown;/,
    );
  }
});

test("an allOf generates as an intersection without dropping sibling constraints", () => {
  const output = renderTypes([
    {
      name: "save_configuration",
      inputSchema: {
        type: "object",
        properties: {
          configuration: {
            type: "object",
            required: ["enabled"],
            properties: { enabled: { type: "boolean" } },
            allOf: [
              {
                type: "object",
                required: ["name"],
                properties: { name: { type: "string" } },
              },
            ],
          },
        },
      },
    },
  ]);

  assert.match(
    output,
    /configuration\?: \(\{\n    enabled: boolean;[\s\S]*\}\) & \(\{\n    name: string;/,
  );
});

test("a root allOf generates a valid type alias", () => {
  const output = renderTypes([
    {
      name: "save_configuration",
      inputSchema: {
        type: "object",
        allOf: [
          {
            type: "object",
            required: ["name"],
            properties: { name: { type: "string" } },
          },
        ],
      },
    },
  ]);

  assert.match(output, /export type SaveConfigurationInput = \(\{/);
  const diagnostics =
    ts.transpileModule(output, {
      compilerOptions: { module: ts.ModuleKind.ESNext },
      fileName: "generated-tools.ts",
      reportDiagnostics: true,
    }).diagnostics ?? [];
  assert.deepEqual(
    diagnostics.filter(
      ({ category }) => category === ts.DiagnosticCategory.Error,
    ),
    [],
  );
});

test("a oneOf generates as a union of its members", () => {
  const output = renderTypes([
    {
      name: "save_ask",
      inputSchema: {
        type: "object",
        properties: {
          target: { oneOf: [{ type: "string" }, { type: "number" }] },
        },
      },
    },
  ]);

  assert.match(output, /target\?: \(string \| number\);/);
});

test("ref siblings and simultaneous unions compose as intersections", () => {
  const output = renderTypes([
    {
      name: "save_configuration",
      inputSchema: {
        type: "object",
        $defs: { Identifier: { type: "string" } },
        properties: {
          id: { $ref: "#/$defs/Identifier", type: "string" },
          value: {
            oneOf: [{ type: "string" }, { type: "number" }],
            anyOf: [{ type: "string" }],
          },
        },
      },
    },
  ]);

  assert.match(output, /id\?: \(SaveConfigurationIdentifier\) & \(string\);/);
  assert.match(output, /value\?: \(string \| number\) & \(string\);/);
});

test("a property name that is not an identifier is quoted", () => {
  const output = renderTypes([
    {
      name: "save_dimension",
      inputSchema: {
        type: "object",
        properties: { "utm-source": { type: "string" } },
      },
    },
  ]);

  assert.match(output, /"utm-source"\?: string;/);
});

test("a generated-looking schema name becomes a valid identifier", () => {
  assert.equal(typeName("__schema47"), "Schema47");
  assert.equal(typeName("save_campaign"), "SaveCampaign");
  assert.equal(typeName("---"), "Schema");
});

test("normalised generated names must remain unique", () => {
  assert.throws(
    () =>
      renderTypes([
        { name: "save-campaign", inputSchema: { type: "object" } },
        { name: "save_campaign", inputSchema: { type: "object" } },
      ]),
    /Generated type name "SaveCampaignInput" collides/,
  );
});

test("tools/list follows every cursor before returning the catalog", async () => {
  const cursors: Array<string | undefined> = [];
  const tools = await listAllTools({
    async listTools(params) {
      cursors.push(params?.cursor);
      if (!params?.cursor) {
        return { tools: [SAVE_CAMPAIGN], nextCursor: "second-page" };
      }
      return {
        tools: [
          {
            name: "get_delivery",
            inputSchema: { type: "object" },
          },
        ],
      };
    },
  });

  assert.deepEqual(cursors, [undefined, "second-page"]);
  assert.deepEqual(
    tools.map((tool) => tool.name),
    ["save_campaign", "get_delivery"],
  );
});

test("tools/list rejects a repeated cursor instead of looping forever", async () => {
  await assert.rejects(
    listAllTools({
      async listTools() {
        return { tools: [], nextCursor: "stuck" };
      },
    }),
    /tools\/list repeated cursor: stuck/,
  );
});
