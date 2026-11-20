# GATILHOS-VIVOS — openbot

Hub quente de retomada. Cada gatilho aponta para fonte viva; nao substitui
L1/L2, Trilho, runtime ou documentacao oficial.

| Gatilho | Quem | Quando lembrar | Fonte viva / acao |
| --- | --- | --- | --- |
| `ARQ-OPENBOT-ROTAS` | sessao do projeto | antes de rodar build/teste | `AGENTS.md` secao Checks; `.agents/napkin.md` |
| `GIT-CONFIG-FLAG-ORDEM` | sessao do projeto | ao ler config git | `git config --show-origin <chave>`; `.agents/napkin.md` |
| `BUN-AUSENTE` | sessao do projeto | `bun: command not found` | `npm install -g bun@1.4.2`; `.agents/napkin.md` |
| `CRG-LOCAL-STRUCTURAL-GRAPH` | sessao do projeto | review estrutural, impacto, hotspots | `.agents/CODE-REVIEW-GRAPH-INDEX.md`; `code-review-graph --version` |
| `MSYS-PATH-CONV-RG` | sessao do projeto | busca `rg` com padrao iniciado por `@/` | `MSYS_NO_PATHCONV=1 rg ...`; `.agents/napkin.md` |
| `OPENBOT-BUILD-RUNTIME` | sessao do projeto | instalar, buildar ou testar | `.agents/memorias/openbot-build-e-runtime.md` |
| `OPENBOT-ENCODING` | sessao do projeto | antes de editar arquivo | `.agents/memorias/openbot-encoding.md` |
| `OPENBOT-TYPECHECK-RED` | sessao do projeto | `typecheck:node` vermelho | `.agents/memorias/openbot-typecheck-node-vermelho.md` |
| `OPENBOT-METRICAS` | sessao do projeto | refatorar hotspot | `.agents/memorias/openbot-metricas-podio.md` |
| `OPENBOT-DEPS-IA` | sessao do projeto | mexer em dependencia com AGENTS/CLAUDE | `.agents/ARQUEOLOGIA/DEPENDENCIES.md` |

## ARQ-OPENBOT-ROTAS

- **Quem**: sessao do projeto.
- **Por que**: rodar checagem ampla local sobrecarrega a maquina do dono.
- **Como**: usar `bun run test:desktop -- <arquivo>` e um `typecheck:*` por vez.
- **Quando**: antes de qualquer prova de build/teste.
- **Onde**: `AGENTS.md` secao Checks; `.agents/napkin.md`.
- **E se??** a prova exigir checagem ampla? -> deixar para CI e registrar a
  ressalva no receipt.

## GIT-CONFIG-FLAG-ORDEM

- **Quem**: sessao do projeto.
- **Por que**: a ordem errada SETA a chave e corrompe o config local.
- **Como**: `git config --show-origin core.autocrlf`.
- **Quando**: ao medir a camada maquina do W2.
- **Onde**: `.agents/napkin.md`.
- **E se??** a chave ja estiver com valor `--show-origin`? ->
  `git config --unset core.autocrlf` e medir de novo.

## BUN-AUSENTE

- **Quem**: sessao do projeto.
- **Por que**: sem bun nao ha instalacao fiel do `bun.lock`.
- **Como**: `npm install -g bun@1.4.2` e conferir `bun --version`.
- **Quando**: `bun` ausente do PATH.
- **Onde**: `.agents/napkin.md`.
- **E se??** o npm nao tiver a versao fixada? -> instalar a mais proxima e
  registrar a divergencia no receipt.

## CRG-LOCAL-STRUCTURAL-GRAPH

- **Quem**: sessao do projeto.
- **Por que**: o grafo estrutural e a menor consulta antes de varredura ampla.
- **Como**: `code-review-graph build --repo . --data-dir .agents/CODE-REVIEW-GRAPH`.
- **Quando**: grafo ausente, vazio ou com SHA stale.
- **Onde**: `.agents/CODE-REVIEW-GRAPH-INDEX.md`.
- **E se??** o build falhar? -> fallback `rg` e registrar a divergencia.
