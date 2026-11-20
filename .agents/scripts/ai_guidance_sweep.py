import collections
import re
import subprocess
import sys

ROOT = sys.argv[1]
OUT = sys.argv[2]
PATTERN = re.compile(r"(^|/)(AGENTS|CLAUDE)\.md$|/\.agents/|/SKILL\.md$", re.I)
result = subprocess.run(
    ["rg", "--files", "--hidden", "--no-ignore", "."],
    capture_output=True,
    text=True,
    cwd=ROOT,
    encoding="utf-8",
    errors="replace",
)
rows = []
for raw in result.stdout.splitlines():
    path = raw.replace(chr(92), "/")
    if path.startswith("./"):
        path = path[2:]
    if PATTERN.search(path):
        rows.append(path)
with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
    handle.write("\n".join(rows) + "\n")
print("total", len(rows))
counts = collections.Counter("/".join(row.split("/")[:2]) for row in rows)
for key, value in counts.most_common(20):
    print(value, key)
