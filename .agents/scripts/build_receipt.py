import datetime
import json
import os
import re
import subprocess
import sys

ROOT = sys.argv[1]
OUT = sys.argv[2]
BASE = os.path.join(ROOT, ".agents", "ARQUEOLOGIA")


def read_json(name, default=None):
    path = os.path.join(BASE, name)
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return default


def read_text(name):
    try:
        with open(os.path.join(BASE, name), encoding="utf-8", errors="replace") as handle:
            return handle.read()
    except OSError:
        return ""


def exit_of(name, key):
    text = read_text(name)
    matches = re.findall(rf"{key}=(-?\d+)", text)
    return int(matches[-1]) if matches else None


def git(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


inventory = read_json("W1-inventory.summary.json", {})
graph3 = read_json("W3-graph.json", {})
deps = read_json("W4-dependencies.json", {}).get("summary", {})
artifact = read_json("W4-artifact-scan.json", {})
guidance = read_json("W4b-summary.json", {})
secrets = read_json("W5-secrets.json", {})
cc = read_json("W8-cc-source.json", {})
crg_metrics = read_json("W8-metrics-crg.json", {})
gate = read_json("W7-grafo-gate.json", {})
eol_text = read_text("W2-git-eol.txt")
eol_counts = {}
for line in eol_text.splitlines():
    parts = line.split()
    if len(parts) >= 2 and parts[0].startswith("i/"):
        key = f"{parts[0]} {parts[1]}"
        eol_counts[key] = eol_counts.get(key, 0) + 1

typecheck_node = exit_of("W6-typecheck-node.log", "typecheck_node_exit")
typecheck_renderer = exit_of("W6-typecheck-renderer.log", "typecheck_renderer_exit")
build = exit_of("W6-build.log", "build_exit")
install = exit_of("W6-install.log", "bun_install_exit")
test = exit_of("W6-test-redaction.log", "test_exit")
postprocess = exit_of("W7-crg-postprocess.log", "crg_postprocess_exit")
graphify = exit_of("W7-graphify-update.log", "graphify_exit")

w6_red = [name for name, value in (("install", install), ("build", build), ("test", test), ("typecheck_node", typecheck_node), ("typecheck_renderer", typecheck_renderer)) if value not in (0, None)]
payload = {
    "schema": "dex.arqueologia.receipt.v1",
    "project": "openbot",
    "root": ROOT.replace("\\", "/"),
    "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "branch": git("branch", "--show-current"),
    "head": git("rev-parse", "HEAD"),
    "tier": "completo",
    "denominator": {
        "files": inventory.get("files"),
        "lines": inventory.get("lines"),
        "bytes": inventory.get("bytes"),
        "by_ext": inventory.get("by_ext"),
    },
    "w2_encoding": {
        "disk": {
            "bom_files": len(inventory.get("bom_files", [])),
            "crlf_files": len(inventory.get("crlf_files", [])),
            "non_utf8_files": len(inventory.get("non_utf8", [])),
            "nul_files": len(inventory.get("nul_files", [])),
            "files_with_high_bytes": inventory.get("high_files"),
        },
        "store": eol_counts,
        "machine": {
            "core_autocrlf_system": "true",
            "gitattributes": "* text=auto eol=lf",
            "contamination": "none measured",
        },
    },
    "w3_graph": {
        "internal_edges": graph3.get("internal_edges"),
        "unresolved_relative": graph3.get("unresolved_relative"),
        "cycles": graph3.get("cycles"),
        "cycle_nodes": graph3.get("cycle_nodes"),
        "top_fan_in": graph3.get("top_fan_in", [])[:5],
    },
    "w4_third_party": {
        "direct_total": deps.get("total"),
        "runtime": deps.get("runtime"),
        "dev": deps.get("dev"),
        "license_counts": deps.get("license_counts"),
        "artifact_named_packages": artifact.get("found_count"),
        "artifact_files_scanned": artifact.get("files_scanned"),
        "artifact_bytes_scanned": artifact.get("bytes_scanned"),
    },
    "w4b_guidance": {
        "packages_with_guidance": guidance.get("packages_with_guidance"),
        "direct_dependencies": guidance.get("direct_dependencies_with_guidance"),
    },
    "w5_secrets": {
        "hits": secrets.get("hit_count"),
        "tracked_hits": len(secrets.get("tracked_hits", [])),
        "env_files": secrets.get("env_files"),
        "env_tracked": secrets.get("env_tracked"),
    },
    "w6_proof": {
        "install_exit": install,
        "build_exit": build,
        "test_exit": test,
        "typecheck_node_exit": typecheck_node,
        "typecheck_renderer_exit": typecheck_renderer,
        "gate": "red" if w6_red else "green",
        "red_items": w6_red,
        "finding": "scripts/mistral-stuck-turn-e2e.ts:110 missing toolCanUseTab in AgentBrowserHook mock" if typecheck_node else None,
    },
    "w7_graphs": {
        "crg_version": "2.4.0+dex.1",
        "crg_files": 8561,
        "crg_nodes": 89440,
        "crg_edges": 714460,
        "crg_postprocess_exit": postprocess,
        "graphify_exit": graphify,
        "grafo_gate": gate,
    },
    "w8_metrics": {
        "cc_functions_source": cc.get("funcoes_fonte"),
        "cc_max_source": cc.get("cc_max_fonte"),
        "cc_mean_source": cc.get("cc_media_fonte"),
        "cc_above_10": cc.get("acima_10"),
        "cc_above_50": cc.get("acima_50"),
        "god_class_top": crg_metrics.get("god_class", [])[:5],
        "long_method_top": crg_metrics.get("long_method", [])[:5],
        "cc_top": cc.get("top", [])[:5],
    },
    "w9_w10": {
        "knowledge_layer": ".agents/ARQUEOLOGIA/REPORT.md + DEPENDENCIES.md + CODE-REVIEW-GRAPH-INDEX.md",
        "memories": "pending",
    },
}
with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
    json.dump(payload, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps({"gate": payload["w6_proof"]["gate"], "w6_red": w6_red}, indent=2))
