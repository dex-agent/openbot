import json
import os
import sys

EXCLUDE_DIRS = {
    ".git", "node_modules", "dist", "build", "out", ".output", "coverage",
    ".openbot-build", ".cache", ".turbo", ".next", "__history", "__recovery",
}
EXTS = {".ts", ".tsx", ".js", ".mjs", ".cjs", ".jsx", ".mts", ".cts"}


def scan(root):
    rows = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIRS)
        for name in sorted(filenames):
            ext = os.path.splitext(name)[1].lower()
            if ext not in EXTS:
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root).replace("\\", "/")
            try:
                with open(full, "rb") as handle:
                    data = handle.read()
            except OSError as error:
                rows.append({"path": rel, "error": str(error)})
                continue
            lines = data.count(b"\n")
            if data and not data.endswith(b"\n"):
                lines += 1
            rows.append({
                "path": rel,
                "ext": ext,
                "bytes": len(data),
                "lines": lines,
                "crlf": data.count(b"\r\n"),
                "lf": data.count(b"\n"),
                "bom": data.startswith(b"\xef\xbb\xbf"),
                "high": sum(1 for byte in data if byte >= 0x80),
                "nul": data.count(b"\x00"),
                "utf8": is_utf8(data),
            })
    return rows


def is_utf8(data):
    try:
        data.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


def main():
    root = sys.argv[1]
    out = sys.argv[2]
    rows = scan(root)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    columns = ["path", "ext", "bytes", "lines", "crlf", "lf", "bom", "high", "nul", "utf8"]
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(columns) + "\n")
        for row in rows:
            if "error" in row:
                handle.write(row["path"] + "\tERROR\t" + row["error"] + "\n")
                continue
            handle.write("\t".join(str(row[column]) for column in columns) + "\n")
    summary = {
        "files": len(rows),
        "bytes": sum(row.get("bytes", 0) for row in rows),
        "lines": sum(row.get("lines", 0) for row in rows),
        "by_ext": {},
        "bom_files": [row["path"] for row in rows if row.get("bom")],
        "crlf_files": [row["path"] for row in rows if row.get("crlf", 0)],
        "non_utf8": [row["path"] for row in rows if row.get("utf8") is False],
        "nul_files": [row["path"] for row in rows if row.get("nul", 0)],
        "high_files": sum(1 for row in rows if row.get("high", 0) > 0),
        "errors": [row for row in rows if "error" in row],
    }
    for row in rows:
        if "error" in row:
            continue
        item = summary["by_ext"].setdefault(row["ext"], {"files": 0, "lines": 0, "bytes": 0})
        item["files"] += 1
        item["lines"] += row["lines"]
        item["bytes"] += row["bytes"]
    with open(os.path.splitext(out)[0] + ".summary.json", "w", encoding="utf-8", newline="\n") as handle:
        json.dump(summary, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({
        "files": summary["files"],
        "lines": summary["lines"],
        "bytes": summary["bytes"],
        "by_ext": summary["by_ext"],
        "bom": len(summary["bom_files"]),
        "crlf": len(summary["crlf_files"]),
        "non_utf8": len(summary["non_utf8"]),
        "nul": len(summary["nul_files"]),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
