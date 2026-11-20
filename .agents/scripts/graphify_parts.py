import json
import os
import subprocess
import sys
import time

ROOT = "."
OUT_BASE = ".agents/GRAPHIFY-PARTS"
MERGE_OUT = ".agents/GRAPHIFY/graphify-out/graph.json"
LOG_DIR = ".agents/ARQUEOLOGIA/graphify-parts"
PARTS = [
    "src/renderer",
    "src/backend",
    "apps/auth-api",
    "apps/mobile/src/features",
    "apps/mobile/src/app",
    "apps/mobile/src/shared",
    "apps/mobile/plugins",
    "scripts",
    "packages/ui",
    "packages/contracts",
    "packages/whatsapp",
    "packages/team-client",
    "packages/logging",
    "packages/telemetry",
    "packages/user-errors",
    "packages/brand",
    "tools",
    "remote",
    "marketplace",
    ".storybook",
    "resources",
    ".agents",
    "apps/mobile-updates",
    "apps/site-router",
    "apps/status",
]
ALREADY = {"src/main": ".agents/GRAPHIFY-PARTS/main/graphify-out/graph.json"}
TIMEOUT = 600

os.makedirs(LOG_DIR, exist_ok=True)
results = {}


def name_of(part):
    return part.replace("/", "-").replace(".", "_")


def graph_of(out_dir):
    return os.path.join(out_dir, "graphify-out", "graph.json")


for part in PARTS:
    name = name_of(part)
    out_dir = os.path.join(OUT_BASE, name)
    log_path = os.path.join(LOG_DIR, name + ".log")
    cmd = [
        "graphify", "extract", part, "--code-only", "--no-cluster",
        "--max-workers", "1", "--out", out_dir,
    ]
    started = time.time()
    with open(log_path, "w", encoding="utf-8", errors="replace") as log:
        process = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        timed_out = False
        try:
            process.wait(timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            timed_out = True
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(process.pid)])
            process.wait()
    elapsed = round(time.time() - started, 1)
    graph = graph_of(out_dir)
    ok = process.returncode == 0 and os.path.isfile(graph)
    results[part] = {
        "exit": process.returncode,
        "seconds": elapsed,
        "timeout": timed_out,
        "graph": graph if ok else None,
    }
    print(part, results[part], flush=True)

graphs = [path for path in ALREADY.values() if os.path.isfile(path)]
graphs += [row["graph"] for row in results.values() if row["graph"]]
os.makedirs(os.path.dirname(MERGE_OUT), exist_ok=True)
merge = ["graphify", "merge-graphs", *graphs, "--out", MERGE_OUT]
merge_log = os.path.join(LOG_DIR, "merge.log")
with open(merge_log, "w", encoding="utf-8", errors="replace") as log:
    merged = subprocess.run(merge, stdout=log, stderr=subprocess.STDOUT)
summary = {
    "parts": results,
    "graphs_merged": len(graphs),
    "merge_exit": merged.returncode,
    "merge_out": MERGE_OUT,
    "merge_exists": os.path.isfile(MERGE_OUT),
}
with open(os.path.join(LOG_DIR, "summary.json"), "w", encoding="utf-8", newline="\n") as handle:
    json.dump(summary, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps({"graphs_merged": len(graphs), "merge_exit": merged.returncode, "exists": summary["merge_exists"]}, indent=2))
