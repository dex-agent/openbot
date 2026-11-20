# ESTACIONAMENTO — openbot

Itens fora do corte atual, com owner e quando.

| Item | Severidade | Owner | Quando |
| --- | --- | --- | --- |
| `scripts/mistral-stuck-turn-e2e.ts:110`: mock `AgentBrowserHost` sem `toolCanUseTab`, que a interface exige (`src/backend/agent/attention-registry.ts:441`). Quebra `bun run typecheck:node` (exit 1) no HEAD `140d75f`. Correcao minima: `toolCanUseTab: () => false,` como nos 19 scripts irmaos. | P1 | mantenedor do repo (scripts e2e) | proxima alteracao nesse arquivo ou antes do proximo merge |
| `apps/mobile/google-services.json` versiona chave de API Firebase de cliente (publica por desenho, restrita por app). Nao e segredo de servidor; revisar restricao no console. | P3 | mantenedor mobile | proxima revisao de credenciais moveis |
| `packages/whatsapp/vendor/baileys/src/WABinary/constants.ts:601`: constante de chave publica de cliente em codigo vendorizado (Baileys). | P3 | upstream Baileys | proximo upgrade da dependencia |
| `medir_cc_engine.py` inclui `out/` no escopo projeto, inflando o podio com bundles minificados. Podium da arqueologia filtra fontes; a ferramenta nao exclui `out/`. | P2 | dono da skill `dex-complexidade-ciclomatica` | proximo corte da skill |
| CRG build nao terminou o postprocess no primeiro disparo (processo encerrado sem exit); `postprocess` manual completou. | P2 | sessao do projeto | proximo build completo do CRG |
| Graphify 0.9.105 trava apos a extracao AST (cluster, `--no-cluster` e `extract --code-only`, inclusive 1 worker), sem escrever `graph.json`. Contornado com 26 partes + `merge-graphs` (80.042 nos, 234.054 links); o run unico do repo inteiro continua travando. | P2 | dono da skill graphify | proximo corte de grafo rico |
| `grafo_gate.py` reprova por "lixo" porque `JUNK_DIRS` fixa `.agents` e `skills`; no OpenBot `skills` e dominio de produto (marketplace) e `.agents` e a superficie de agentes do repo. As outras 5 checagens passam. | P2 | dono da skill `code-review-graph-delphi-feeder` | proximo corte da skill (allowlist por projeto) |
