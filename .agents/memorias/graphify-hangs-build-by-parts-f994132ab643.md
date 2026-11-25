---
implementation_version: v2
layer: L2
slug: graphify-hangs-build-by-parts-f994132ab643
tags:
  - "#auto-memory/project"
---

# graphify-hangs-build-by-parts

Espelho da auto-memory do host ZCode (arquivo graphify-hangs-build-by-parts.md, tipo project).

Graphify 0.9.105 hangs after full AST extraction on the OpenBot

On the OpenBot repo (2026-11-20), `graphify update` and `graphify extract --code-only` both freeze after reporting 100% AST extraction, with idle CPU and no `graph.json`, in cluster, `--no-cluster` and 1-worker modes. A 45-file smoke run finished normally, so the failure depends on corpus size. The working route: run `graphify extract <subdir> --code-only --no-cluster --max-workers 1 --out <dir>` for each part (keep each part under ~800 files), then `graphify merge-graphs <graphs...> --out graph.json`. 26 parts merged into 80,042 nodes and 234,054 links.

**Why:** the owner asked for the CRG/graphify pipeline to keep running; a silent hang costs a long wait and looks like success.

**How to apply:** detect a hang by log mtime with idle CPU, kill the whole process tree, and switch to parts instead of retrying the full run. Add `graphify-out/` to `.gitignore`.

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^graphify-hangs-build-by-parts-f994132ab643-content
