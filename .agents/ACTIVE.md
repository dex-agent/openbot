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
- W7: CRG completo (89.440 nos, 714.460 arestas); Graphify em rota de
  diagnostico (trava apos a extracao)
- W8: podio medido (God Class `AgentService` 233 metodos; CC max 774)
- W9: 10 memorias V2 `scope=project` validadas em lote (10/10)
- W10: em fechamento

## Proximo passo

Fechar W7 (gate ou plano B declarado), gerar `RECEIPT.json`, atualizar
`REPORT.md` e commitar o bloco.
