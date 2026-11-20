import collections
import json
import sys

RAW = sys.argv[1]
DEPS = sys.argv[2]
OUT = sys.argv[3]

with open(DEPS, encoding="utf-8") as handle:
    rows = json.load(handle)["rows"]
direct = {row["name"]: row for row in rows}
counts = collections.Counter()
for line in open(RAW, encoding="utf-8", errors="replace"):
    path = line.strip().replace(chr(92), "/")
    if not path:
        continue
    parts = path.split("/")
    if len(parts) < 2 or parts[0] != "node_modules":
        continue
    name = parts[1] if not parts[1].startswith("@") else "/".join(parts[1:3])
    counts[name] += 1
payload = {
    "packages_with_guidance": len(counts),
    "files": sum(counts.values()),
    "direct_dependencies_with_guidance": [
        {"name": name, "files": count, "scope": direct[name]["scope"], "license": direct[name]["license"]}
        for name, count in sorted(counts.items()) if name in direct
    ],
    "transitive_or_unknown": [
        {"name": name, "files": count}
        for name, count in sorted(counts.items()) if name not in direct
    ],
}
with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
    json.dump(payload, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps(payload, indent=2))
