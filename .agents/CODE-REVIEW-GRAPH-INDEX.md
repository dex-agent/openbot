# Code review graph — receipt local

LOCALIZADOR: `CRG-LOCAL-STRUCTURAL-GRAPH`
Tags: `#code-review-graph`, `#crg`, `#grafo-estrutural`, `#code-review`, `#impact-radius`

- Repo: `C:\CodexProjetos\openbot`
- Branch: `main`
- Commit: `762b240858b475c7de8df29c0aa3b5f6d3e65f0a` (`762b24085`)
- Data dir: `.agents/CODE-REVIEW-GRAPH` (banco `graph.db`, coberto pelo `.gitignore` local)
- Arquivos indexados: 11.627
- Nós: 134.364
- Arestas: 769.707
- Linguagens: bash, html, javascript, json, kotlin, nix, sql, swift, tsx, typescript, yaml
- Atualizado em: 2026-11-21T21:52:59 (CLI `code-review-graph 2.4.0+dex.1`)
- Estado do build: completo (sem aviso `Build state: INCOMPLETE`)

## Consulta

```bash
code-review-graph status --repo . --data-dir .agents/CODE-REVIEW-GRAPH
code-review-graph detect-changes --repo . --data-dir .agents/CODE-REVIEW-GRAPH --brief
code-review-graph impact --repo . --data-dir .agents/CODE-REVIEW-GRAPH --files <paths>
```

## Refresh

```bash
code-review-graph update --repo . --data-dir .agents/CODE-REVIEW-GRAPH
```

Atualização incremental cobre commit novo. Se o status disser `Build state: INCOMPLETE`, só a reconstrução completa cura:

```bash
code-review-graph build --repo . --data-dir .agents/CODE-REVIEW-GRAPH
```

Um `update` interrompido deixa o banco travado (`database is locked`) para outra execução; espere o processo terminar ou encerre-o antes de reabrir.

## Limites

- Grafo é foto do commit acima; fonte que mudou sem refresh torna o grafo stale. Regra no gatilho `STALENESS-ARTEFATOS-DERIVADOS` em `.agents/GATILHOS-VIVOS.md`.
- Achado do grafo é pista; fato só depois de abrir código, teste ou documentação viva.
- Não cobre Object Pascal nem Markdown; documentação é eixo do Graphify.
- Não foram gerados embeddings nem envio de código para provedor externo.
