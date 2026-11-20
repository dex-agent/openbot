# ACTIVE — openbot

Missao atual: arqueologia completa W-1..W10 (skill `arqueologia-warmup-base` +
dialeto `arqueologia-nodejs-warmup`).

## Estado

- Repo: `C:\CodexProjetos\openbot`
- Branch: `main`
- HEAD medido: `140d75f3154714e967b7798d1ae43c98095400d3`
- Gerenciador: `bun@1.4.2` (instalado nesta maquina), lockfile `bun.lock`
- Node: `v24.19.0` (engines `>=24.0.0`)
- Tier: completo; denominador 7.701 fontes TS/JS, 1.645.650 linhas
- Codigo-fonte: READ-ONLY nesta arqueologia (nenhuma edicao de `src/`,
  `packages/`, `apps/`); escritas apenas em `.agents/`, `.githooks/`,
  `AGENTS.md`, `INDEX.md` e `.gitignore`

## Gates medidos

- W1 inventario: concluido (`.agents/ARQUEOLOGIA/W1-inventory.tsv`)
- W2 encoding: UTF-8/LF, zero BOM/CRLF (tabela em `W2-encoding-table.md`)
- W3 grafo: 35.702 arestas, 34 ciclos
- W4/W4b/W5: concluidos com ressalvas sanitizadas
- W6: `bun install --frozen-lockfile` 0, `bun run build` 0, teste estreito 0,
  `typecheck:renderer` 0; `typecheck:node` 1 (achado P1 em
  `.agents/ESTACIONAMENTO.md`)
- W7: CRG completo (89.764 nos, 715.301 arestas); Graphify reconstruido em
  26 partes e unido (80.042 nos, 234.054 links); `grafo_gate.py` exit 1 por
  falso-positivo de dominio na checagem de lixo (5/6 checagens verdes);
  plano B declarado no `REPORT.md`
- W8: podio medido (God Class `AgentService` 233 metodos; CC max 774)
- W9: 10 memorias V2 `scope=project` validadas em lote (10/10)
- W10: `RECEIPT.json` gerado, plaquinhas completas, `LIXEIRA/MANIFEST.md`

## Proximo passo

Bloco fechado. Retomar por `REPORT.md` + `RECEIPT.json`. O achado P1 de
`typecheck:node` espera o mantenedor (`.agents/ESTACIONAMENTO.md`).

