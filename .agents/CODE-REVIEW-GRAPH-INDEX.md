# CODE-REVIEW-GRAPH-INDEX — openbot

LOCALIZADOR: `CRG-LOCAL-STRUCTURAL-GRAPH`
Tags: `#code-review-graph`, `#crg`, `#grafo-estrutural`, `#code-review`, `#impact-radius`

## Grafo estrutural local

- Repo: `C:\CodexProjetos\openbot`
- Branch: `main`
- Commit do build: `140d75f31547`
- Data dir: `.agents/CODE-REVIEW-GRAPH` (banco `graph.db` ignorado pelo `.gitignore` interno)
- Versao do CLI: `code-review-graph 2.4.0+dex.1`
- Schema SQLite: `v15`
- Arquivos indexados: `8.592`
- Nos: `89.764`
- Arestas: `715.301`
- Linguagens: bash, html, javascript, json, kotlin, nix, python, sql, swift, tsx, typescript, yaml
- Atualizado em: `2026-11-20T12:05:35`
- Pos-processamento: `7.168 flows`, `26 comunidades`, `89.440 entradas FTS` (FTS reconstruida antes do update incremental do hook)
- Tamanho do banco: `749 MB`

## Comando de refresh

```bash
code-review-graph build --repo . --data-dir .agents/CODE-REVIEW-GRAPH
code-review-graph postprocess --repo . --data-dir .agents/CODE-REVIEW-GRAPH
```

Atualizacao incremental:

```bash
code-review-graph update --repo . --data-dir .agents/CODE-REVIEW-GRAPH
```

## Consultas uteis

```bash
code-review-graph architecture --repo . --data-dir .agents/CODE-REVIEW-GRAPH
code-review-graph large-functions --repo . --data-dir .agents/CODE-REVIEW-GRAPH
code-review-graph query callers_of <simbolo> --repo . --data-dir .agents/CODE-REVIEW-GRAPH
code-review-graph detect-changes --files <paths> --repo . --data-dir .agents/CODE-REVIEW-GRAPH
code-review-graph impact --files <paths> --repo . --data-dir .agents/CODE-REVIEW-GRAPH
code-review-graph dead-code --repo . --data-dir .agents/CODE-REVIEW-GRAPH
```

## Limites

- O grafo e auxiliar: achado material so vira fato depois de confirmado na fonte.
- `out/`, `node_modules/` e `vendor/` entram no parse quando a ferramenta os enxerga;
  o podio da arqueologia filtra fontes de producao.
- O primeiro `build` encerrou antes do pos-processamento; `postprocess` manual
  completou. Repetir o `build` inteiro no proximo refresh.
- Sem embeddings: nenhum codigo foi enviado a provedor externo.
