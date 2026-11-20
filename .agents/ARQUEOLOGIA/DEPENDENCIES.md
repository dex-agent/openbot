# DEPENDENCIES — openbot

Gerado pela arqueologia W0-W10 em 2026-11-20. Fonte primaria: `package.json`,
`bun.lock`, `node_modules` instalado com `bun install --frozen-lockfile`.

## Gerenciador e runtime

- `packageManager`: `bun@1.4.2`
- Lockfile: `bun.lock`
- `engines.node`: `>=24.0.0` (medido: `v24.19.0`)
- Workspaces: `apps/*`, `packages/*`, `remote/api`

## Direcao de dependencia (interna)

```text
renderer ──► @openbot/contracts ◄── preload ◄── main ──► backend
                        ▲                             │
                        └──────── auth-api ──────────┘
```

Regras impostas por `biome.json` (`noRestrictedImports`): renderer e UI nao
importam `main`/`backend`/`preload`; contracts nao importa Electron, SolidJS,
provider, Cloudflare nem codigo de aplicacao; auth-api nao importa codigo do
desktop.

## Hubs de fan-in (W3, import graph proprio)

| Arquivo | Fan-in |
| --- | ---: |
| `packages/contracts/src/ipc.ts` | 2.036 |
| `packages/i18n/src/message.ts` | 1.600 |
| `packages/contracts/src/runtime-values.ts` | 835 |
| `packages/ui/src/text.tsx` | 689 |
| `src/backend/effect-boundary.ts` | 555 |
| `packages/ui/src/index.ts` | 542 |
| `apps/mobile/src/shared/lib/text.ts` | 415 |
| `packages/logging/src/index.ts` | 383 |

Numeros: 7.701 fontes, 35.702 arestas internas, 3.950 arestas por alias `@/`,
34 ciclos (427 nos), 986 imports relativos nao resolvidos (assets CSS/imagem/
JSON). Detalhe em `.agents/ARQUEOLOGIA/W3-graph.json` e `W3-edges.tsv`.

## 3rd-party em duas colunas

| Coluna | Definicao | Contagem |
| --- | --- | ---: |
| Entra no artefato final | pacote encontrado no bundle `out/` por nome | 32 |
| Presente no repo/lockfile | dependencia declarada em qualquer workspace | 168 |

A coluna do artefato usa `artifact_scan.py` sobre `out/` (76 MB, 343 arquivos,
70,4 MB lidos, build `electron-vite`); os 32 nomes aparecem em `out/main/`
(`out/main/index.js` ou `out/main/agent-database-host.js`). O renderer embute
dependencias sem preservar o nome, entao ausencia de nome nao prova que o
pacote nao foi embutido. A coluna do repo usa `W4-dependencies.tsv`
(168 diretas: 132 runtime, 36 dev).

### Licencas (diretas)

| Licenca | Pacotes |
| --- | ---: |
| MIT | 129 |
| Apache-2.0 | 14 |
| BSD-3-Clause | 4 |
| ISC | 4 |
| MIT OR Apache-2.0 | 3 |
| PolyForm-Noncommercial-1.0.0 | 2 |
| MPL-2.0 | 1 (`axe-core`, dev) |
| OFL-1.1 | 1 |
| CC0-1.0 | 1 |
| BlueOak-1.0.0 | 1 |
| SEE LICENSE IN README.md | 1 |
| sem campo `license` (workspaces `@openbot/*`) | 7 |

Nenhuma dependencia runtime com GPL/AGPL. `axe-core` (MPL-2.0) e dev.

## Diretrizes de IA embarcadas (W4b)

4 dependencias diretas trazem `AGENTS.md`/`CLAUDE.md`: `effect`, `elysia`,
`react-native-keyboard-controller`, `react-native-webrtc`.

| Pacote | Fonte | Cobre | Prova (simbolo no fonte instalado) |
| --- | --- | --- | --- |
| `effect` | `node_modules/effect/AGENTS.md` + `CLAUDE.md` | estilo Effect 4 (`Effect.gen`, `Effect.fn`, sem wrapper de Promise) | `Effect.gen` em `effect/src/workflow/WorkflowProxyServer.ts`; `Schema.TaggedError` em `effect/src/sql/SqlError.ts` |
| `elysia` | `node_modules/elysia/AGENTS.md` + `CLAUDE.md` | regras de contribuicao do repo Elysia | `class Elysia` em `elysia/dist/ws/index.mjs`; `t.Object` em `elysia/dist/replace-schema.mjs` |
| `react-native-keyboard-controller` | `node_modules/react-native-keyboard-controller/AGENTS.md` | issues e reproducao do repo | `KeyboardProvider` em `src/animated.tsx`; `useKeyboardAnimation` em `src/views/KeyboardExtender/index.tsx` |
| `react-native-webrtc` | `node_modules/react-native-webrtc/CLAUDE.md` | visao do projeto e comandos de build nativo | `RTCPeerConnection` em `src/RTCTrackEvent.ts` |

Ponteiro, nunca copia: as regras de cada dependencia governam o codigo DELA.
Revalidar com:

```bash
rg --files --hidden --no-ignore node_modules/<dep> | rg -i "(AGENTS|CLAUDE)\.md$|\.agents/|SKILL\.md$"
```

Transitivas com o mesmo tipo de arquivo: `bun-types`, `cytoscape`,
`expo-modules-macros`, `thread-stream` (nao entram no painel de dependencia
direta; revalidar no upgrade).
