import json
import os
import sys


def read_json(path):
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {}


def package_dirs(root):
    dirs = [root]
    for parent in ("packages", "apps"):
        base = os.path.join(root, parent)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            candidate = os.path.join(base, name)
            if os.path.isfile(os.path.join(candidate, "package.json")):
                dirs.append(candidate)
    remote = os.path.join(root, "remote", "api")
    if os.path.isfile(os.path.join(remote, "package.json")):
        dirs.append(remote)
    return dirs


def installed_manifest(root, name):
    candidate = os.path.join(root, "node_modules", *name.split("/"), "package.json")
    if os.path.isfile(candidate):
        return read_json(candidate)
    return None


def license_of(manifest):
    if not manifest:
        return None
    value = manifest.get("license")
    if isinstance(value, str) and value.strip():
        return value.strip()
    licenses = manifest.get("licenses")
    if isinstance(licenses, list):
        return " OR ".join(str(item.get("type", item)) if isinstance(item, dict) else str(item) for item in licenses)
    return None


def main():
    root = sys.argv[1]
    out_json = sys.argv[2]
    out_tsv = sys.argv[3]
    records = {}
    for folder in package_dirs(root):
        manifest = read_json(os.path.join(folder, "package.json"))
        rel = os.path.relpath(folder, root).replace("\\", "/")
        for field, scope in (("dependencies", "runtime"), ("devDependencies", "dev"), ("optionalDependencies", "optional")):
            for name, declared in manifest.get(field, {}).items():
                record = records.setdefault(name, {
                    "name": name,
                    "declared": set(),
                    "scopes": set(),
                    "declared_by": set(),
                })
                record["declared"].add(declared)
                record["scopes"].add(scope)
                record["declared_by"].add(rel)
    rows = []
    for name, record in sorted(records.items()):
        manifest = installed_manifest(root, name)
        rows.append({
            "name": name,
            "declared": ",".join(sorted(record["declared"])),
            "scope": "runtime" if "runtime" in record["scopes"] else ("optional" if "optional" in record["scopes"] else "dev"),
            "declared_by": ",".join(sorted(record["declared_by"])),
            "installed_version": manifest.get("version") if manifest else None,
            "license": license_of(manifest),
            "installed": manifest is not None,
        })
    with open(out_tsv, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("name\tdeclared\tscope\tdeclared_by\tinstalled_version\tlicense\tinstalled\n")
        for row in rows:
            handle.write("\t".join(str(row[key] if row[key] is not None else "") for key in (
                "name", "declared", "scope", "declared_by", "installed_version", "license", "installed",
            )) + "\n")
    summary = {
        "total": len(rows),
        "runtime": sum(1 for row in rows if row["scope"] == "runtime"),
        "dev": sum(1 for row in rows if row["scope"] == "dev"),
        "missing_install": [row["name"] for row in rows if not row["installed"]],
        "license_counts": {},
        "without_license": [row["name"] for row in rows if not row["license"]],
        "copyleft": [row for row in rows if row["license"] and any(
            token in row["license"].upper() for token in ("GPL", "AGPL", "MPL", "CDDL", "EPL")
        )],
    }
    for row in rows:
        key = row["license"] or "(unknown)"
        summary["license_counts"][key] = summary["license_counts"].get(key, 0) + 1
    with open(out_json, "w", encoding="utf-8", newline="\n") as handle:
        json.dump({"summary": summary, "rows": rows}, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
