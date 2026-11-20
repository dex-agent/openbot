# HANDOFF — openbot

## Retomada em janela nova

1. Ler `AGENTS.md` global e `AGENTS.md` do projeto (secao Archaeology status).
2. Ler `.agents/ACTIVE.md`, `.agents/HANDOFF.md`, `.agents/napkin.md`,
   `.agents/GATILHOS-VIVOS.md`, `.agents/ESTACIONAMENTO.md`,
   `.agents/PENDENTES.md`.
3. Ler `.agents/ARQUEOLOGIA/REPORT.md` e `RECEIPT.json`.
4. Nao reexecutar etapa ja medida; conferir os exits no receipt.

## Fatos de ambiente medidos (2026-11-20)

- `bun` nao existia; instalado `bun@1.4.2` via `npm install -g bun@1.4.2`
  (alinha com `packageManager`).
- `node`: `v24.19.0`; `engines.node`: `>=24.0.0`.
- `bun install --frozen-lockfile`: exit 0. O `prepare` ativou
  `core.hooksPath=.githooks`.
- `bun run build`: exit 0, 24,28 s, `out/` 76 MB.
- `typecheck:node`: exit 1 (TS2741 em `scripts/mistral-stuck-turn-e2e.ts:110`).
- `typecheck:renderer`: exit 0. Teste estreito de redaction: 65 passed.
- `core.autocrlf=true` no gitconfig de sistema; `.gitattributes` fixa
  `* text=auto eol=lf`; loja 100% `i/lf`.
- CLI do grafo: `code-review-graph 2.4.0+dex.1`.
- Graphify 0.9.105 travou apos a extracao AST em duas rotas; ver
  `PENDENTES.md`.

## Comandos canonicos

Ver `AGENTS.md` secao Checks. Nao rodar checagem ampla local; usar
`bun run test:desktop -- <arquivo>`, `bun run test:changed` e um
`typecheck:*` por vez.

## Grafo estrutural

`.agents/CODE-REVIEW-GRAPH` (749 MB, ignorado pelo Git). Refresh:
`code-review-graph build --repo . --data-dir .agents/CODE-REVIEW-GRAPH` e
depois `postprocess`. Indice em `.agents/CODE-REVIEW-GRAPH-INDEX.md`.
