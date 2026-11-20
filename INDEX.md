# INDEX — openbot

Mapa de retomada para agentes. A autoridade do produto continua em `AGENTS.md`,
`README.md` e `docs/architecture/`.

## Autoridade e contrato

- [AGENTS.md](AGENTS.md) — regras nao negociaveis, checks, fronteiras e termos.
- [README.md](README.md) — visao do produto e comandos.
- [docs/architecture/structure.md](docs/architecture/structure.md) — mapa dos workspaces e direcao de dependencia.
- [docs/architecture/change-rules.md](docs/architecture/change-rules.md) — regras de mudanca arquitetural.

## Areas de codigo

- [src/](src/) — Electron: `main`, `preload`, `renderer`, `backend`.
- [packages/](packages/) — contratos, UI compartilhada, i18n, logging, telemetria, team-client.
- [apps/](apps/) — auth-api, mobile, mobile-updates, site-router, status e apps de mensageria.
- [scripts/](scripts/) — harnesses E2E, build, release e verificacao.
- [tools/](tools/) — regras Biome/GritQL e checagem de UI.
- [remote/](remote/) — servico Signal e scripts de deploy.
- [docs/](docs/) — documentacao do produto.

## Arqueologia e estado vivo

- [.agents/ARQUEOLOGIA/REPORT.md](.agents/ARQUEOLOGIA/REPORT.md) — laudo W0-W10 com numeros medidos.
- [.agents/ARQUEOLOGIA/DEPENDENCIES.md](.agents/ARQUEOLOGIA/DEPENDENCIES.md) — grafo, licencas e diretrizes de IA embarcadas.
- [.agents/CODE-REVIEW-GRAPH-INDEX.md](.agents/CODE-REVIEW-GRAPH-INDEX.md) — grafo estrutural CRG.
- [.agents/ACTIVE.md](.agents/ACTIVE.md) — estado do bloco atual.
- [.agents/HANDOFF.md](.agents/HANDOFF.md) — retomada de sessao.
- [.agents/GATILHOS-VIVOS.md](.agents/GATILHOS-VIVOS.md) — gatilhos quentes.
- [.agents/napkin.md](.agents/napkin.md) — runbook tatico.
- [.agents/ESTACIONAMENTO.md](.agents/ESTACIONAMENTO.md) — itens fora do corte.

## Indices de subpastas

- [.agents/ARQUEOLOGIA/INDEX.md](.agents/ARQUEOLOGIA/INDEX.md) — artefatos da arqueologia.
