# Upstream do OpenBot (monitoracao)

Modelo de trabalho deste repositorio:

- `origin` = https://github.com/nightly-labs/openbot — repositorio ORIGINAL, sempre recebendo atualizacoes. Somente leitura para nos: `git fetch origin` e `git log origin/main`. Nunca push, nunca PR para o origin.
- `fork` = https://github.com/dex-agent/openbot — NOSSA versao (fork criado em 2026-11-21). Recebe branches e a nossa `main` quando decidirmos consolidar.
- Base local desta maquina: `C:/CodexProjetos/openbot` (main com commits locais de arqueologia) e worktrees em `C:/CodexProjetos/openbot-fix-picker` (branch `fix/skill-picker-200-limit`, commit `9e7638b03`, publicado no fork).

## Regra de sincronizacao

1. Monitorar: `git fetch origin` e comparar `HEAD..origin/main`.
2. Portar correcoes nossas sobre a base oficial mais recente (worktree limpo a partir de `origin/main`), nunca sobre uma base velha.
3. Publicar no `fork`, nunca no `origin`.
4. Se o upstream mexer em `src/backend/home-skills.ts`, `src/main/skill-folder-discovery.ts` ou `packages/ui/src/features/conversation/`, revisar o port do limite do picker antes de rebasear.

## Alinhamento da maquina (2026-11-21)

- `main` local = `fork/main` (`4034585bb`) + 1 commit local `762b24085` (AGENTS.md da casa: escopo de seguranca ofensiva no lugar da secao Non-negotiable do upstream).
- 3 commits de arqueologia preservados na branch `house/archaeology` (`d6083e8b1`), publicada no fork.
- Publicado no fork: `main` = `762b24085` (AGENTS da casa) e `house/archaeology`.
- Pre-align guardado em `.agents-backups/` (AGENTS.md antigo + diff) e no stash `pre-align-main-to-fork`.
- App dev reaberto na base alinhada: picker com 725 opcoes (719 home + 5 sistema + 1 MCP), primeira `accelerated-computing-cudf`, ultima `zeco`.

## Ultima verificacao

- 2026-11-21: `origin/main` em `6f9c9b01c` (0.76.1). Tetos de 200 confirmados no upstream; correcao nossa `9e7638b03` publicada na branch `fix/skill-picker-200-limit` e mergeada no fork pelo PR #1 (squash `4034585bba`), que agora e a nossa `main`.
