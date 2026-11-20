# HANDOFF — openbot

## Retomada em janela nova

1. Ler `AGENTS.md` global e `AGENTS.md` do projeto.
2. Ler `.agents/ACTIVE.md`, `.agents/HANDOFF.md`, `.agents/napkin.md`,
   `.agents/GATILHOS-VIVOS.md`, `.agents/ESTACIONAMENTO.md`.
3. Ler `.agents/ARQUEOLOGIA/RECEIPT.json` (status medido do ultimo bloco).
4. Nao reexecutar etapa ja medida: conferir receipt e datas.

## Fatos de ambiente medidos

- `bun` nao existia na maquina; instalado `bun@1.4.2` via
  `npm install -g bun@1.4.2` em 2026-11-20 (alinha com `packageManager`).
- `node_modules` ausente no inicio; instalar com
  `bun install --frozen-lockfile`.
- `core.autocrlf=true` vem do gitconfig de sistema; `.gitattributes` fixa
  `* text=auto eol=lf` e a loja mede `i/lf`.
- CLI do grafo: `code-review-graph 2.4.0+dex.1` no PATH.

## Comandos canonicos do dono

Ver `AGENTS.md` secao Checks. Nao rodar checagens amplas locais; a prova W6
usa o recorte mais estreito e registra o que ficou para CI.
