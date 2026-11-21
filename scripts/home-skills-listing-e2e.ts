import assert from "node:assert/strict";
import { mkdirSync, readdirSync, statSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import { Effect } from "effect";
import { listHomeSkills } from "../src/backend/home-skills";

const root = join(homedir(), ".agents", "skills");
const onDisk = readdirSync(root).filter((name) => {
  if (name.startsWith(".")) return false;
  try {
    return statSync(join(root, name, "SKILL.md")).isFile();
  } catch {
    return false;
  }
}).length;
const skills = await Effect.runPromise(listHomeSkills());
const slugs = new Set(skills.map((skill) => skill.slug));
const last = [...slugs].sort().at(-1) ?? "";
const report = {
  checkedAt: new Date().toISOString(),
  root,
  onDisk,
  listed: skills.length,
  lastSlug: last,
  hasSprinter: slugs.has("sprinter"),
  command: "bun scripts/home-skills-listing-e2e.ts",
};
mkdirSync(".openbot-build/home-skills-listing-e2e", { recursive: true });
writeFileSync(".openbot-build/home-skills-listing-e2e/report.json", `${JSON.stringify(report, null, 2)}\n`);
assert.ok(onDisk > 200, `expected more than 200 skills on disk, saw ${onDisk}`);
assert.equal(skills.length, onDisk, `listed ${skills.length} of ${onDisk} skills on disk`);
assert.ok(slugs.has("sprinter"), "sprinter is missing from the listed skills");
process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
