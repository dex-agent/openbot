---
implementation_version: v2
layer: L2
slug: openbot-crg-e-hooks
tags:
  - "#openbot/ferramentas"
  - "#openbot/crg"
---

# OpenBot: CRG local e hooks do projeto

O grafo estrutural vive em .agents/CODE-REVIEW-GRAPH (code-review-graph 2.4.0+dex.1, schema v15, 749 MB, ignorado pelo .gitignore interno). Build: code-review-graph build --repo . --data-dir .agents/CODE-REVIEW-GRAPH; o primeiro build encerrou antes do pos-processamento, entao rodar postprocess. O bun install ativa core.hooksPath=.githooks via prepare; o pre-commit do projeto roda check:staged, check:ui e staged-typecheck. Hooks do CRG em .git/hooks ficam inertes com esse hooksPath; os hooks de plataforma (Codex/Claude) atualizam o grafo. Indice e limites em .agents/CODE-REVIEW-GRAPH-INDEX.md.

#openbot/ferramentas #openbot/crg

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-crg-e-hooks-content
