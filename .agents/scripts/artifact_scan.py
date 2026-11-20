import json
import os
import re
import sys

ROOT = sys.argv[1]
BUILD_DIR = sys.argv[2]
DEPS_JSON = sys.argv[3]
OUT = sys.argv[4]

with open(DEPS_JSON, encoding="utf-8") as handle:
    deps = json.load(handle)["rows"]
names = {row["name"] for row in deps}
SPEC = re.compile(r"""(?:require|import)\(\s*["']([^"']+)["']|from\s*["']([^"']+)["']""")


def package_of(spec):
    if spec.startswith(".") or spec.startswith("/"):
        return None
    parts = spec.split("/")
    return "/".join(parts[:2]) if spec.startswith("@") else parts[0]


found = {}
scanned = 0
total_bytes = 0
for dirpath, dirnames, filenames in os.walk(BUILD_DIR):
    dirnames[:] = sorted(dirnames)
    for filename in sorted(filenames):
        if not filename.endswith((".js", ".mjs", ".cjs")):
            continue
        full = os.path.join(dirpath, filename)
        try:
            data = open(full, "rb").read()
        except OSError:
            continue
        scanned += 1
        total_bytes += len(data)
        text = data.decode("utf-8", "replace")
        for match in SPEC.finditer(text):
            spec = match.group(1) or match.group(2)
            name = package_of(spec)
            if name and name in names and name not in found:
                found[name] = os.path.relpath(full, ROOT).replace("\\", "/")
payload = {
    "build_dir": BUILD_DIR,
    "files_scanned": scanned,
    "bytes_scanned": total_bytes,
    "packages_found": found,
    "found_count": len(found),
    "declared_count": len(names),
    "limitation": "A bundled package can appear without its own name; absence is not proof that it is not bundled.",
}
with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
    json.dump(payload, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps({key: payload[key] for key in ("files_scanned", "bytes_scanned", "found_count", "declared_count")}, indent=2))
