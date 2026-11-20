import json
import os
import re
import subprocess
import sys

ROOT = sys.argv[1]
OUT = sys.argv[2]
EXCLUDE = {".git", "node_modules", "dist", "build", "out", ".output", "coverage", ".openbot-build", ".cache"}
TEXT_EXT = {
    ".ts", ".tsx", ".js", ".mjs", ".cjs", ".jsx", ".json", ".jsonc", ".yaml", ".yml",
    ".toml", ".ini", ".conf", ".cfg", ".env", ".properties", ".sh", ".ps1", ".bat", ".cmd",
    ".md", ".sql", ".xml", ".plist", ".entitlements",
}
PATTERNS = [
    ("private_key_block", re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("aws_access_key", re.compile(rb"AKIA[0-9A-Z]{16}")),
    ("github_token", re.compile(rb"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}")),
    ("slack_token", re.compile(rb"xox[abposr]-[A-Za-z0-9-]{10,}")),
    ("openai_style_key", re.compile(rb"sk-[A-Za-z0-9]{20,}")),
    ("google_api_key", re.compile(rb"AIza[0-9A-Za-z_-]{30,}")),
    ("assigned_secret", re.compile(rb"(?i)(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\s*[:=]\s*['\"][^'\"\r\n]{8,}['\"]")),
    ("assigned_secret_plain", re.compile(rb"(?i)^\s*(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\s*[:=]\s*[^\s#'\"]{8,}")),
]


def ignored(paths):
    result = {}
    if not paths:
        return result
    proc = subprocess.run(
        ["git", "check-ignore", "--stdin"],
        input="\n".join(paths).encode("utf-8"),
        capture_output=True,
        cwd=ROOT,
    )
    for line in proc.stdout.decode("utf-8", "replace").splitlines():
        if line.strip():
            result[line.strip()] = True
    return result


def main():
    hits = []
    env_files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE)
        for name in sorted(filenames):
            ext = os.path.splitext(name)[1].lower()
            if name.startswith(".env"):
                env_files.append(os.path.relpath(os.path.join(dirpath, name), ROOT).replace("\\", "/"))
            if ext not in TEXT_EXT and ext != "":
                continue
            if ext == "" and not name.startswith(".env"):
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, ROOT).replace("\\", "/")
            try:
                if os.path.getsize(full) > 2_000_000:
                    continue
                with open(full, "rb") as handle:
                    data = handle.read()
            except OSError:
                continue
            for kind, pattern in PATTERNS:
                for match in pattern.finditer(data):
                    line = data.count(b"\n", 0, match.start()) + 1
                    hits.append({"path": rel, "line": line, "kind": kind, "bytes": match.end() - match.start()})
    paths = sorted({hit["path"] for hit in hits})
    ignored_map = ignored(paths)
    for hit in hits:
        hit["gitignored"] = ignored_map.get(hit["path"], False)
    payload = {
        "hits": hits,
        "hit_count": len(hits),
        "tracked_hits": [hit for hit in hits if not hit["gitignored"]],
        "env_files": env_files,
        "env_tracked": [path for path in env_files if path not in ignored(env_files)],
    }
    with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({
        "hit_count": len(hits),
        "tracked_hit_count": len(payload["tracked_hits"]),
        "kinds": sorted({hit["kind"] for hit in hits}),
        "env_files": len(env_files),
        "env_tracked": len(payload["env_tracked"]),
    }, indent=2))


if __name__ == "__main__":
    main()
