# Gatilhos vivos — OpenBot (fork da casa)

Hub quente de retomada. Cada gatilho tem Quem, Por que, Como, Quando, Onde e E se??.
Fonte viva vence memória.

| Gatilho | Quem | Quando lembrar | Fonte viva / ação |
| --- | --- | --- | --- |
| STALENESS-ARTEFATOS-DERIVADOS | sessão do projeto (fiscal: `dex-fechamento-projeto-atualizado`) | antes de ler ou citar CRG, Graphify, PLAYBOOK, INDEX, receipt de capacidade ou fluxo de decisão | comparação de 3 números abaixo; regenerar antes de citar |
| CRG-LOCAL-STRUCTURAL-GRAPH | sessão do projeto | review estrutural, impacto, arquitetura, antes de citação do grafo | `code-review-graph status --repo . --data-dir .agents/CODE-REVIEW-GRAPH` |

## STALENESS-ARTEFATOS-DERIVADOS

- **Quem**: a sessão do projeto que vai ler ou citar o artefato; fiscalização por `dex-fechamento-projeto-atualizado` e `guarda-plaquinhas`. O dono do artefato é a ferramenta que o gera.
- **Por que**: todo artefato derivado nasce fotografando a fonte num instante. Fonte que mudou sem regeneração transforma foto velha em ruído confiável — falso verde. Exemplo medido nesta casa: CRG construído em `eed928df8` (2026-11-20) e repositório avançando 187 commits até `762b24085` (2026-11-21); citar o grafo velho seria citar um código que não existe mais.
- **Como**: comparar SEMPRE três números: (a) quando a FONTE mudou — `git log -1 --format=%cI` no repo (ou `stat -c %y` dos arquivos-fonte); (b) quando o ARTEFATO foi gerado — o timestamp do próprio artefato (comando de status ou `stat` do arquivo); (c) se fonte > artefato então STALE: rodar o comando de regeneração do artefato e só depois citar o conteúdo. Staleness é medido em segundos, nunca "parece atual".
- **Quando**: antes de qualquer leitura ou citação de artefato derivado — janela fria, re-arqueologia, review estrutural, decisão que diz "o grafo diz X", relatório que cita PLAYBOOK, INDEX ou receipt de capacidade.
- **Onde**: este hub, mais os comandos por artefato inventariados neste repo:
  - CRG estrutural — artefato `.agents/CODE-REVIEW-GRAPH/graph.db` (campo "Last updated" e "Built at commit"); leitura `code-review-graph status --repo . --data-dir .agents/CODE-REVIEW-GRAPH`; regeneração `code-review-graph build --repo . --data-dir .agents/CODE-REVIEW-GRAPH` (completa) ou `code-review-graph update --repo . --data-dir .agents/CODE-REVIEW-GRAPH` (incremental).
  - Graphify semântico — artefatos `.agents/GRAPHIFY/graphify-out/graph.json` e `.agents/GRAPHIFY-PARTS/*/graphify-out/graph.json` (existe `graphify` no PATH); staleness por `stat -c %y` do `graph.json` contra `git log -1 --format=%cI`; regeneração pela skill `graphify` (extract) com o corpus atual.
  - PLAYBOOK — ausente neste repo (`PLAYBOOK.md` e `PLAYBOOK.index.json` não existem); nada a citar.
  - INDEX.md de raiz e subpastas — ausente neste repo; se um dia existir, drift é linha morta ou ponta solta e o fiscal é `dex-fechamento-projeto-atualizado`.
  - Receipts de capacidade e mapas — `.agents/MAPAS/` ausente; recibos de arqueologia em `.agents/ARQUEOLOGIA/` (datas no nome e no conteúdo) só valem para o commit que os gerou.
- **E se?? o repo não tem git (sem `git log`)?** → usar `stat`/mtime dos arquivos-fonte contra o timestamp do artefato; a regra dos três números continua valendo.
- **E se?? o staleness-check der STALE mas a ferramenta de regeneração não está instalada?** → declarar o artefato como "não consultável", nunca citar número dele, e estacionar a instalação com owner e quando.
- **E se?? o check passar (verde) mas o conteúdo parecer errado?** → verde de staleness não é prova de semântica; abrir a FONTE, não o artefato. Fonte viva sempre vence memória.

## CRG-LOCAL-STRUCTURAL-GRAPH

- **Quem**: sessão do projeto; dono da construção é a skill `code-review-graph`.
- **Por que**: review estrutural sem grafo atual lê relações que o código já mudou.
- **Como**: `code-review-graph status --repo . --data-dir .agents/CODE-REVIEW-GRAPH` e exigir `Built at commit` igual ao `HEAD`; se divergir, `build` (completo) ou `update` (incremental) e repetir o status. Build interrompido aparece como `Build state: INCOMPLETE` — nesse caso só `build` cura.
- **Quando**: antes de impacto, arquitetura, comunidades, review de mudança e antes de qualquer citação do grafo.
- **Onde**: `.agents/CODE-REVIEW-GRAPH/`, recibo em `.agents/CODE-REVIEW-GRAPH-INDEX.md` e ponteiro no `AGENTS.md`.
- **E se?? o status disser INCOMPLETE?** → não citar números; rodar `build` até o status mostrar o commit atual e o build completo.
- **E se?? o grafo não cobrir a linguagem?** → declarar a lacuna e usar fonte viva (rg, testes, documentação).
