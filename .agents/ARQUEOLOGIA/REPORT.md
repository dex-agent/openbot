# Arqueologia OpenBot — W-1 a W10

Data: 2026-11-20. Commit: `140d75f3154714e967b7798d1ae43c98095400d3`.
Skill: `arqueologia-warmup-base` + dialeto `arqueologia-nodejs-warmup`.
Codigo-fonte do alvo: READ-ONLY (nenhuma edicao em `src/`, `packages/`,
`apps/`, `scripts/`, `tools/`, `remote/`).

## W0 — identidade, rotas e tier

- Projeto: OpenBot (`nightly-labs/openbot`), app desktop local-first com
  clientes web e mobile, servidores Team API e servicos Cloudflare.
- Licenca: PolyForm Noncommercial 1.0.0. Versao: 0.74.0.
- Rota: monorepo UNICO e vivo; nao existe segunda rota legada a comparar.
- Gerenciador: `bun@1.4.2`; lockfile `bun.lock`; Node `>=24` (medido v24.19.0).
- Tier: COMPLETO (>10 units).
- Denominador: 7.701 fontes `.ts/.tsx/.js/.mjs/.cjs` fora de `node_modules`,
  `dist`, `build`, `out` e `coverage`.
- Subconjuntos: vendor Baileys 174 arquivos/161.712 linhas; i18n 1.620
  arquivos `.ts` em 15 locales; testes vitest 139 arquivos/25.621 linhas;
  E2E em `scripts/`.

## W1 — superficie e argv real

| Extensao | Arquivos | Linhas | Bytes |
| --- | ---: | ---: | ---: |
| `.ts` | 5.837 | 1.197.276 | 56.924.581 |
| `.tsx` | 1.838 | 348.306 | 13.066.959 |
| `.js` | 18 | 99.061 | 4.495.973 |
| `.mjs` | 6 | 970 | 38.388 |
| `.cjs` | 2 | 37 | 1.446 |
| **Total** | **7.701** | **1.645.650** | **74.527.347** |

Peso por area: `packages` 663.568 linhas; `src` 485.186; `apps` 262.400;
`scripts` 219.027; `tools` 741; `remote` 6.675; `marketplace` 6.815.

Argv real do dono (transcrito de `package.json`):

| Prova | Comando |
| --- | --- |
| Instalar | `bun install --frozen-lockfile` |
| Build | `bun run build` -> `electron-vite build` |
| Teste desktop | `bun run test:desktop` -> `vitest run` |
| Teste por mudanca | `bun run test:changed` -> `vitest run --changed origin/main --maxWorkers=1` |
| Tipos node | `bun run typecheck:node` -> `bun scripts/type-checker.ts --noEmit -p tsconfig.node.json` |
| Tipos renderer | `bun run typecheck:renderer` -> `bun scripts/type-checker.ts --noEmit -p tsconfig.web.json` |
| Tipos API | `bun run typecheck:api` -> `bun run --cwd apps/auth-api typecheck` |
| Lint | `biome check --max-diagnostics=none .` (arquivo: `biome check --write --max-diagnostics=none <paths>`) |
| Pre-commit | `.githooks/pre-commit` via `core.hooksPath=.githooks` (ativado pelo `prepare`) |

## W2 — encoding byte-a-byte (3 camadas)

| Grupo | Arquivos | Linhas | Arquivos >0x80 | BOM | CRLF | Nao-UTF8 | NUL | Encoding |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `src` | 2.021 | 485.186 | 185 | 0 | 0 | 0 | 0 | UTF-8 LF |
| `packages/i18n` | 1.637 | 272.381 | 1.445 | 0 | 0 | 0 | 0 | UTF-8 LF |
| `scripts` | 674 | 219.027 | 76 | 0 | 0 | 0 | 0 | UTF-8 LF |
| `packages/whatsapp` | 189 | 163.510 | 14 | 0 | 0 | 0 | 0 | UTF-8 LF |
| `apps/mobile` | 1.159 | 156.529 | 89 | 0 | 0 | 0 | 0 | UTF-8 LF |
| `packages/ui` | 622 | 149.454 | 84 | 0 | 0 | 0 | 0 | UTF-8 LF |
| `apps/auth-api` | 693 | 102.292 | 71 | 0 | 0 | 0 | 0 | UTF-8 LF |
| `packages/contracts` | 483 | 60.197 | 12 | 0 | 0 | 0 | 0 | UTF-8 LF |
| `packages/team-client` | 52 | 13.883 | 4 | 0 | 0 | 0 | 0 | UTF-8 LF |
| demais | 171 | 23.191 | 14 | 0 | 0 | 0 | 0 | UTF-8 LF |

- Disco: zero BOM, zero CRLF, zero NUL, zero arquivo nao-UTF8; 1.994 arquivos
  tem bytes >=0x80 e todos decodificam como UTF-8.
- Loja Git: `git ls-files --eol` = 9.335 arquivos `i/lf w/lf`, 325 binarios,
  1 `i/none`, 1 `i/` sem `w/`. Blobs de amostra (`src/main/main-window.ts`,
  `apps/mobile/app.config.js`) batem byte-a-byte com o disco.
- Maquina: `core.autocrlf=true` vem do gitconfig de sistema
  (`C:/Program Files/Git/etc/gitconfig`), mas `.gitattributes` fixa
  `* text=auto eol=lf`; nao ha modo ambiguo nem contaminacao.
- Tropeco pago: `git config core.autocrlf --show-origin` SETA a chave com o
  literal `--show-origin`; a leitura correta e
  `git config --show-origin core.autocrlf`.

## W3 — grafo de dependencias internas

- 7.701 fontes, **35.702 arestas internas**, 3.950 por alias `@/`.
- 986 imports relativos nao resolvidos, todos de assets (CSS, imagens,
  `package.json`, WebP) — nao sao arestas de codigo.
- 34 ciclos com 427 nos (main, backend, renderer, contracts).
- Hubs de fan-in: `packages/contracts/src/ipc.ts` 2.036;
  `packages/i18n/src/message.ts` 1.600;
  `packages/contracts/src/runtime-values.ts` 835;
  `packages/ui/src/text.tsx` 689; `src/backend/effect-boundary.ts` 555.
- Fan-out: `src/main/application-services.ts` 290;
  `apps/auth-api/src/routeTree.gen.ts` 271;
  `src/main/team-api-server.ts` 250.
- Fechamento externo: 168 dependencias diretas instaladas, zero ausente no
  `node_modules`.

## W4 — o que se esconde

- Nenhum `.min.js` versionado.
- **Zero `eval`/`new Function` reais**: as 45 ocorrencias sao metodo
  `.eval(...)` de harness E2E e de shader.
- `atob(` aparece 10 vezes em codigo legitimo de base64.
- Literais base64 longos so em vetores de teste do WhatsApp.
- Superficie gerada: `packages/whatsapp/vendor/baileys/WAProto/index.js`
  (97.691 linhas); `packages/i18n/src/messages` (1.620 `.ts`, 15 locales);
  `plugin-catalog.generated.ts` (auth-api e mobile); `routeTree.gen.ts`.
- Postinstall do projeto auditado antes do install: `electron-dist-cache.ts`,
  `install-electron.ts` (baixa o Electron com retry), `stamp-install.ts` e
  `install-git-hooks.ts`. Nenhum script de terceiro nao auditado.

### 3rd-party em duas colunas

| Coluna | Definicao | Contagem |
| --- | --- | ---: |
| Entra no artefato final | nome encontrado em `out/` (build real) | 32 |
| Presente no repo/lockfile | dependencia direta declarada | 168 |

Limite: o renderer embute dependencias sem preservar o nome; ausencia nao prova
que o pacote nao entrou. A varredura leu 343 arquivos/70,4 MB de `out/`.

Licencas diretas: MIT 129, Apache-2.0 14, BSD-3-Clause 4, ISC 4,
MIT OR Apache-2.0 3, PolyForm-Noncommercial-1.0.0 2, MPL-2.0 1 (`axe-core`,
dev), OFL-1.1 1, CC0-1.0 1, BlueOak-1.0.0 1, "SEE LICENSE IN README.md" 1,
sem campo `license` 7 (workspaces `@openbot/*`). Nenhuma runtime GPL/AGPL.

## W4b — diretrizes de IA embarcadas

Varredura `--hidden --no-ignore` no repo e em `node_modules`: 124 arquivos no
repo (92 do catalogo de marketplace, 14 skills do projeto, 12 `AGENTS.md` de
subarvore, 3 de `managed-skills`, 2 de `agent-import`, 1 outro) e 11 arquivos
em 8 pacotes instalados. Quatro sao dependencias DIRETAS: `effect`, `elysia`, `react-native-keyboard-controller`,
`react-native-webrtc`. Ponteiros e simbolos confirmados em
`DEPENDENCIES.md`. Nenhuma skill copiada para o registry.

## W5 — dados, config e segredos

- 5 arquivos `.env` versionados (`apps/auth-api/.env.dev`, `.env.production`,
  `.env.example`; `remote/.env.example`, `.env.production`): todos cifrados
  com dotenvx (chave publica + valores `encrypted:`). `.env.keys` ausente e
  ignorado.
- 167 achados de varredura, todos fixtures, placeholders mascarados
  (`whsec_••••`, `••••••••`) ou chaves publicas de cliente. Dois achados
  reais e nao secretos, P3: chave Firebase de cliente em
  `apps/mobile/google-services.json`; constante de chave publica no Baileys
  vendorizado.
- Nenhum segredo de servidor em texto claro. Valores nunca foram ecoados.

## W6 — prova de build e teste (com vermelho medido)

| Prova | Exit | Evidencia |
| --- | ---: | --- |
| `bun install --frozen-lockfile` | 0 | `W6-install.log` |
| `bun run build` (`electron-vite`) | 0 | `W6-build.log`; `out/` 76 MB; 24,28 s |
| `bun run test:desktop -- packages/logging/src/redaction.test.ts` | 0 | 65 testes passed |
| `bun run typecheck:renderer` | 0 | `W6-typecheck-renderer.log` |
| `bun run typecheck:node` | **1** | TS2741 em `scripts/mistral-stuck-turn-e2e.ts:110` |

Achado P1: o mock `AgentBrowserHost` em
`scripts/mistral-stuck-turn-e2e.ts:110` nao implementa `toolCanUseTab`, que a
interface exige (`src/backend/agent/attention-registry.ts:441`). Os outros 19
scripts E2E ja tem `toolCanUseTab: () => false`. Correcao minima de uma linha;
codigo permaneceu read-only por contrato. Owner e quando em
`ESTACIONAMENTO.md`.

## W7 — grafos canonicos

- CRG `2.4.0+dex.1`, schema v15: **8.592 arquivos, 89.764 nos, 715.301
  arestas**, 7.168 flows, 26 comunidades, 89.440 entradas FTS; banco de
  751 MB em `.agents/CODE-REVIEW-GRAPH` (ignorado pelo Git).
- O primeiro `build` encerrou sem o pos-processamento; `postprocess` manual
  completou com exit 0.
- Graphify 0.9.105 travou, com CPU ociosa, depois de extrair 100% dos
  arquivos em tres rotas (cluster, `--no-cluster` e `extract --code-only`,
  inclusive 1 worker). O grafo foi construido em **26 partes** menores
  (cada uma completou) e unido com `graphify merge-graphs`:
  **80.042 nos, 234.054 links**, 88,6 MB em `.agents/GRAPHIFY`.
  Uma extracao de fumaça (45 arquivos) provou que a ferramenta funciona e
  que a falha depende do tamanho do corpus.
- Gate de grafos (`grafo_gate.py`, exit medido sem pipe): **exit 1** em
  `.agents/ARQUEOLOGIA/W7-grafo-gate.txt`. Cinco de seis checagens verdes
  (span, ordem de linhas, faixa de funcoes, FTS vs SQL, graphify frescor vs
  HEAD). A checagem de "lixo" e falso-positivo de dominio: `JUNK_DIRS` fixa
  `.agents` e `skills`, mas OpenBot tem marketplace de skills de produto e
  uma superficie `.agents` propria. Plano B: grafo W3 (100% das fontes) +
  as cinco checagens substantivas do CRG.

## W8 — metricas e toxicidade

Cobertura do medidor de CC: 37.815 rotinas de producao medidas contra 43.411
funcoes TS/TSX que o CRG enxerga (87,1%); a lacuna e de construtos que o
parser regex nao enumera. Plano B: CRG `large-functions`/`Function` nodes
corrobora o podio.

### God Class (CRG, producao, sem vendor)

| Classe | Metodos | Linhas | Arquivo |
| --- | ---: | ---: | --- |
| `AgentService` | 233 | 6.400 | `src/backend/agent-service.ts` |
| `MailboxStore` | 103 | 3.378 | `src/backend/mailbox-store.ts` |
| `OpenBotDatabase` | 88 | 586 | `src/backend/openbot-database.ts` |
| `ProviderRuntime` | 70 | 3.957 | `src/backend/agent/provider-runtime.ts` |
| `BrowserHost` | 63 | 4.000 | `src/backend/browser-host.ts` |

### Long Method (CRG, producao)

| Funcao | Linhas | Arquivo |
| --- | ---: | --- |
| `WebWorkspaceFrame` | 3.454 | `src/renderer/src/features/web-client/WebWorkspace.tsx` |
| `createMockOpenBot` | 3.418 | `src/renderer/src/preview/mock-openbot.ts` |
| `createApplicationServices` | 3.303 | `src/main/application-services.ts` |
| `WorkflowCanvas` | 3.237 | `packages/ui/src/features/workflows/WorkflowCanvas.tsx` |
| `createConversationViewScope` | 2.476 | `src/renderer/src/features/conversation/conversation-scope.ts` |

### Maior CC (medidor da casa, fontes de producao)

| Funcao | CC | Arquivo |
| --- | ---: | --- |
| `WorkflowCanvas` | 774 | `packages/ui/src/features/workflows/WorkflowCanvas.tsx` |
| `createWebWorkspace` | 650 | `src/renderer/src/features/web-client/web-client-context.tsx` |
| `WebWorkspaceFrame` | 641 | `src/renderer/src/features/web-client/WebWorkspace.tsx` |
| `createConversationViewScope` | 495 | `src/renderer/src/features/conversation/conversation-scope.ts` |
| `createRemoteTeamPeer` | 488 | `packages/team-client/src/remote-peer.ts` |

37.815 funcoes; media 4,49; 2.783 acima de CC 10; 232 acima de CC 50.

## W9 — camada de conhecimento

- `AGENTS.md`: secao curta "Archaeology status" com ponteiros e status real.
- `INDEX.md` na raiz; `.agents/ARQUEOLOGIA/INDEX.md`;
  `.agents/PLAN-TASKS/INDEX.md`.
- `DEPENDENCIES.md`: direcao interna, hubs, licencas, DEP-IA.
- `CODE-REVIEW-GRAPH-INDEX.md`: grafo CRG, refresh e limites.
- `.agents/`: ACTIVE, HANDOFF, GATILHOS-VIVOS, napkin, ESTACIONAMENTO,
  PENDENTES, PLAN-TASKS, LIXEIRA.
- **10 memorias V2 `scope=project`** gravadas por `dex-memoria v2 remember`
  (nunca hand-write), `status=COMMITTED`, `validation_ok=true`, e lote
  `validate-memory-batch.py`: **10/10 validos**, exit 0.
- Gatilhos L1 quentes: `OPENBOT-BUILD-RUNTIME`, `OPENBOT-ENCODING`,
  `OPENBOT-TYPECHECK-RED`, `OPENBOT-METRICAS`, `OPENBOT-DEPS-IA`,
  `GIT-CONFIG-FLAG-ORDEM`, `MSYS-PATH-CONV-RG`, `CRG-LOCAL-STRUCTURAL-GRAPH`.

## W10 — integracao, contagens e residuo

- Memoraveis gravados: **10**.
- Tropecos novos catalogados: **7** — ordem do `git config` que SETA a chave;
  `bun` ausente da maquina; MSYS converte padrao `rg` iniciado por `@/`;
  primeiro build do CRG sem postprocess; Graphify travado pos-extracao;
  medidor de CC inclui `out/`; mock E2E sem `toolCanUseTab` (P1).
- Residuo: um lock de rebuild do Graphify, preservado em
  `.agents/LIXEIRA/MANIFEST.md` (metadados sanitizados). Nada apagado sem
  garimpo.
- `RECEIPT.json` gerado no commit `63f229b` e commitado em `eed928df8`.

## Delta do quadro de ferramentas

O que o projeto passa a ter depois deste bloco:

| Capacidade | Superficie |
| --- | --- |
| Estado vivo de retomada | `.agents/ACTIVE.md`, `HANDOFF.md`, `GATILHOS-VIVOS.md`, `napkin.md`, `ESTACIONAMENTO.md`, `PENDENTES.md`, `PLAN-TASKS/INDEX.md` |
| Memoria local V2 | `.agents/lembranca.md` + 10 arquivos em `.agents/memorias/` |
| Grafo estrutural | `.agents/CODE-REVIEW-GRAPH` + `CODE-REVIEW-GRAPH-INDEX.md` |
| Grafo semantico por partes | `.agents/GRAPHIFY` (80.042 nos, 234.054 links) |
| Hooks de grafo | `.githooks/pre-commit` (bloco CRG) + `post-checkout`/`post-merge`/`post-rewrite`; hooks de plataforma Codex/Claude |
| Harness reproduzivel | 13 scripts em `.agents/scripts/` |
| Mapa do repo | `INDEX.md` na raiz + `.agents/ARQUEOLOGIA/INDEX.md` |
| Dependencias e DEP-IA | `.agents/ARQUEOLOGIA/DEPENDENCIES.md` |
| Evidencia bruta | `.agents/ARQUEOLOGIA/W1..W8` + logs W6/W7 |
| Descarte governado | `.agents/LIXEIRA/MANIFEST.md` |

Ficam fora do Git, por serem configuracao local de ferramenta: `.mcp.json` e
`.claude/settings.json` (criados pelo `code-review-graph install`).

## Creditos

- `$chato`: pressao adversarial que impediu fechar W6 como verde com
  `typecheck:node` vermelho e que cobrou prova de vida do Graphify.
- `$burrinha`: premissa pelo avesso que expos o trap do MSYS no `rg`.
- `$critico-cetico`: obrigou tratar 167 achados de segredo como suspeitos ate
  a classificacao sanitizada.
- `$entrevista-me` + `$questionador`: perguntaram, antes do install do CRG, se
  os hooks iriam atropelar o pre-commit do projeto; a resposta mudou a ordem
  da operacao.
- `$interrogador-documental`: leitura da fonte da skill e do `--help` antes de
  cada conclusao (ordem do `git config`, contrato do `dex-memoria`, rotas do
  Graphify).

## Ressalvas

- W6 tem rota vermelha real (typecheck:node); build e testes medidos verdes.
- W7 tem plano B no eixo Graphify; o eixo CRG esta completo.
- A cobertura do medidor de CC e 87,1% das funcoes TS/TSX do CRG.
- Nenhuma suite ampla, build mobile ou deploy foi executado (regra do repo).
- O SPT formal v3 nao foi criado antes da execucao; a trilha ficou em
  `TASKS.md` e `.agents/PLAN-TASKS/INDEX.md` (desvio registrado).
