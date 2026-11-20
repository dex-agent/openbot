import collections
import json
import os
import re
import sys

ROOT = sys.argv[1]
INVENTORY = sys.argv[2]
OUT_JSON = sys.argv[3]
OUT_EDGES = sys.argv[4]

IMPORT_PATTERNS = [
    re.compile(r"""(?:^|\n)\s*import\s+(?:type\s+)?(?:[^'";]*?\s+from\s+)?["']([^"']+)["']"""),
    re.compile(r"""(?:^|\n)\s*export\s+(?:type\s+)?(?:\*|\{[^}]*\})\s+from\s+["']([^"']+)["']"""),
    re.compile(r"""\brequire\(\s*["']([^"']+)["']\s*\)"""),
    re.compile(r"""\bimport\(\s*["']([^"']+)["']\s*\)"""),
]
RESOLVE_SUFFIXES = ["", ".ts", ".tsx", ".js", ".mjs", ".cjs", "/index.ts", "/index.tsx", "/index.js"]
WORKSPACE_ALIASES = {}


def load_workspace_aliases():
    for folder in ("packages", "apps"):
        base = os.path.join(ROOT, folder)
        if not os.path.isdir(base):
            continue
        for name in os.listdir(base):
            package_json = os.path.join(base, name, "package.json")
            if not os.path.isfile(package_json):
                continue
            try:
                with open(package_json, encoding="utf-8") as handle:
                    data = json.load(handle)
            except (OSError, json.JSONDecodeError):
                continue
            package_name = data.get("name")
            if package_name:
                WORKSPACE_ALIASES[package_name] = f"{folder}/{name}"
    remote = os.path.join(ROOT, "remote", "api", "package.json")
    if os.path.isfile(remote):
        try:
            with open(remote, encoding="utf-8") as handle:
                data = json.load(handle)
            if data.get("name"):
                WORKSPACE_ALIASES[data["name"]] = "remote/api"
        except (OSError, json.JSONDecodeError):
            pass


def load_files():
    files = []
    with open(INVENTORY, encoding="utf-8") as handle:
        header = handle.readline()
        for line in handle:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 10:
                continue
            files.append(parts[0])
    return set(files)


def resolve_relative(source, spec):
    base = os.path.dirname(source)
    target = os.path.normpath(os.path.join(base, spec)).replace("\\", "/")
    for suffix in RESOLVE_SUFFIXES:
        candidate = target + suffix
        if candidate in FILES:
            return candidate
    if target.endswith((".js", ".mjs", ".cjs", ".jsx")):
        stem = target.rsplit(".", 1)[0]
        for suffix in (".ts", ".tsx", ".mts", ".cts"):
            if stem + suffix in FILES:
                return stem + suffix
    return None


def resolve_workspace(spec):
    for name in sorted(WORKSPACE_ALIASES, key=len, reverse=True):
        if spec == name or spec.startswith(name + "/"):
            folder = WORKSPACE_ALIASES[name]
            rest = spec[len(name):].lstrip("/")
            if not rest:
                for suffix in RESOLVE_SUFFIXES:
                    candidate = folder + "/src/index" + suffix
                    if candidate in FILES:
                        return candidate
                return folder
            for suffix in RESOLVE_SUFFIXES:
                candidate = f"{folder}/src/{rest}{suffix}"
                if candidate in FILES:
                    return candidate
            return None
    return None


def resolve_alias(source, spec):
    if not spec.startswith("@/"):
        return None
    rest = spec[2:]
    bases = []
    if source.startswith("apps/mobile/"):
        bases = ["apps/mobile/src", "apps/mobile/assets"]
    elif source.startswith("apps/auth-api/"):
        bases = ["apps/auth-api/src"]
    elif source.startswith("src/renderer/"):
        bases = ["src/renderer/src"]
    for base in bases:
        for suffix in RESOLVE_SUFFIXES:
            candidate = f"{base}/{rest}{suffix}"
            if candidate in FILES:
                return candidate
    return None


def tarjan(nodes, edges):
    index = 0
    indexes = {}
    low = {}
    stack = []
    on_stack = set()
    components = []
    for start in nodes:
        if start in indexes:
            continue
        work = [(start, iter(edges.get(start, ())))]
        indexes[start] = low[start] = index
        index += 1
        stack.append(start)
        on_stack.add(start)
        while work:
            node, children = work[-1]
            advanced = False
            for child in children:
                if child not in indexes:
                    indexes[child] = low[child] = index
                    index += 1
                    stack.append(child)
                    on_stack.add(child)
                    work.append((child, iter(edges.get(child, ()))))
                    advanced = True
                    break
                if child in on_stack:
                    low[node] = min(low[node], indexes[child])
            if advanced:
                continue
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[node])
            if low[node] == indexes[node]:
                component = []
                while True:
                    item = stack.pop()
                    on_stack.discard(item)
                    component.append(item)
                    if item == node:
                        break
                components.append(component)
    return [component for component in components if len(component) > 1]


def main():
    global FILES
    load_workspace_aliases()
    FILES = load_files()
    edges = collections.defaultdict(set)
    fan_in = collections.Counter()
    fan_out = collections.Counter()
    edge_rows = []
    unresolved = []
    external = collections.Counter()
    dynamic = 0
    for source in sorted(FILES):
        full = os.path.join(ROOT, source)
        try:
            with open(full, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
        except OSError:
            continue
        specs = set()
        for pattern in IMPORT_PATTERNS:
            specs.update(pattern.findall(text))
        if re.search(r"""\bimport\(\s*["']""", text):
            dynamic += 1
        for spec in specs:
            if spec.startswith("."):
                target = resolve_relative(source, spec)
                if target is None:
                    unresolved.append({"source": source, "spec": spec})
                    continue
                kind = "internal"
            elif spec.startswith("@openbot/") or spec in WORKSPACE_ALIASES:
                target = resolve_workspace(spec)
                if target is None:
                    unresolved.append({"source": source, "spec": spec})
                    continue
                kind = "workspace"
            elif spec.startswith("@/"):
                target = resolve_alias(source, spec)
                if target is None:
                    unresolved.append({"source": source, "spec": spec})
                    continue
                kind = "alias"
            else:
                external[spec.split("/")[0] if not spec.startswith("@") else "/".join(spec.split("/")[:2])] += 1
                continue
            if target == source:
                continue
            if target in edges[source]:
                continue
            edges[source].add(target)
            fan_in[target] += 1
            fan_out[source] += 1
            edge_rows.append((source, target, kind))
    cycles = tarjan(sorted(FILES), edges)
    payload = {
        "source_files": len(FILES),
        "internal_edges": len(edge_rows),
        "internal_nodes_with_outgoing": len(edges),
        "dynamic_import_files": dynamic,
        "unresolved_relative": len(unresolved),
        "unresolved_sample": unresolved[:40],
        "cycles": len(cycles),
        "cycle_nodes": sum(len(component) for component in cycles),
        "cycle_sample": [sorted(component)[:6] for component in sorted(cycles, key=len, reverse=True)[:10]],
        "top_fan_in": fan_in.most_common(25),
        "top_fan_out": fan_out.most_common(25),
        "top_external": external.most_common(30),
        "workspace_aliases": WORKSPACE_ALIASES,
    }
    with open(OUT_JSON, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    with open(OUT_EDGES, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("source\ttarget\tkind\n")
        for source, target, kind in sorted(edge_rows):
            handle.write(f"{source}\t{target}\t{kind}\n")
    print(json.dumps({
        "source_files": payload["source_files"],
        "internal_edges": payload["internal_edges"],
        "unresolved_relative": payload["unresolved_relative"],
        "cycles": payload["cycles"],
        "cycle_nodes": payload["cycle_nodes"],
        "top_fan_in": payload["top_fan_in"][:5],
    }, indent=2))


if __name__ == "__main__":
    main()
