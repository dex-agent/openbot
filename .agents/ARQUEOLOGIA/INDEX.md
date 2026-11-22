# INDEX — .agents/ARQUEOLOGIA

Evidencias da arqueologia W-1..W10 (2026-11-20).

| Arquivo | Conteudo |
| --- | --- |
| `REPORT.md` | laudo final com inventario, Enc, grafo, podio e ressalvas |
| `DEPENDENCIES.md` | gerenciador, direcao de dependencia, licencas, DEP-IA |
| `RECEIPT.json` | recibo JSON com exits medidos e numeros |
| `W1-inventory.tsv` | inventario por arquivo: bytes, linhas, CRLF, BOM, bytes >0x80 |
| `W1-inventory.summary.json` | agregados do inventario |
| `W2-encoding-table.md` | tabela Enc por grupo |
| `W2-git-eol.txt` | `git ls-files --eol` (camada loja) |
| `W3-graph.json` | grafo de imports: arestas, hubs, ciclos, nao resolvidos |
| `W3-edges.tsv` | arestas internas por arquivo |
| `W4-dependencies.tsv` | 168 dependencias diretas com licenca |
| `W4-artifact-scan.json` | pacotes nomeados no bundle `out/` |
| `W4b-ai-guidance.txt` | diretrizes de IA no repo e em `node_modules` |
| `W4b-summary.json` | diretrizes por dependencia direta |
| `W5-secrets.json` | achados de segredo sanitizados (arquivo:linha, tipo) |
| `W6-install.log` | `bun install --frozen-lockfile` |
| `W6-build.log` | `bun run build` |
| `W6-typecheck-node.log` | `typecheck:node` (vermelho) |
| `W6-typecheck-renderer.log` | `typecheck:renderer` (verde) |
| `W6-test-redaction.log` | teste estreito (65 passed) |
| `W7-crg-build.log` | build do CRG |
| `W7-crg-postprocess.log` | flows/comunidades/FTS |
| `W7-graphify-update.log` | extracao estrutural do Graphify |
| `W7-grafo-gate.json` | resultado do gate de grafos |
| `W8-cc.json` | CC bruto (inclui `out/`) |
| `W8-cc-source.json` | CC filtrado para fontes de producao |
| `W8-metrics-crg.json` | God Class e Long Method pelo CRG |

Scripts reprodutiveis: `.agents/scripts/`.
