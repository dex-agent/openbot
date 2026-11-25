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
- 2026-11-22T12:00Z: `origin/main` em `d2a5ac7f7`; 5 commits novos desde a nossa base (nenhum toca `src/backend/home-skills.ts`, `src/main/skill-folder-discovery.ts` ou `packages/ui/src/features/conversation/`).
- 2026-11-23T12:00Z: `origin/main` em `72f80f561`; 212 commits novos desde a nossa base. Nenhum commit upstream toca `src/backend/home-skills.ts` nem `src/main/skill-folder-discovery.ts` (os tetos deles continuam em 200; os nossos 2000/5000 seguem intactos). `packages/ui/src/features/conversation/` recebeu 39 commits upstream, mas o nosso fix do picker (`4034585bba`) nao toca esse diretorio — sem sobreposicao com o port.
- 2026-11-24: `main` da casa rebaseada sobre `72f80f561` (8 commits preservados, 0 atras). Conflito unico em `AGENTS.md`, resolvido mantendo a secao Non-negotiable do upstream e o Escopo de seguranca ofensiva da casa. Instalador refeito: `dist/OpenBot-0.76.1-x64.exe`, 234.652.108 bytes, sha256 `3274173c53ddeb8d3bfd180261292b1a4a9fcb59ba9f54a45edcd03d39841de2`. Sem push.
- 2026-11-24 (update): `electron-builder.yml` apontava `publish.owner` para `nightly-labs`; o app instalado baixou `OpenBot-0.77.0-x64.exe` do upstream (236 MB em `%LOCALAPPDATA%\openbot-updater\pending`) e substituiria a nossa build. Cura: `owner: dex-agent` no `electron-builder.yml` e no `app-update.yml` do app instalado; pendente apagado; instalador recompilado (`234.652.035` bytes, sha256 `1a95b96e25ec061d13c08cf08336cb8005a077a249977d47e98e092dabbc6b32`). O fork nao publica releases, entao a checagem de update nao oferece versao.
- 2026-11-24T12:00Z: `origin/main` em `a771a57f7` (tag `v0.77.0`); 97 commits novos desde a nossa base. Nenhum commit toca `src/backend/home-skills.ts` nem `src/main/skill-folder-discovery.ts` (upstream segue 200/200; os nossos 2000/5000 intactos). `packages/ui/src/features/conversation/` recebeu 1 commit (`c1c43ee04`, remote sync do web client); o nosso fix do picker nao toca esse diretorio — sem sobreposicao.

## Invariantes de execucao (2026-11-22)

- App dev com a conta de producao: subir SEM `OPENBOT_AUTH_API_URL` local (ou com `https://openbot.run`). Apontar para `http://127.0.0.1:3100` cria uma conta local separada com o mesmo e-mail (ids diferentes) e o host perde presenca para web e mobile.
- Base atualizada: rodar `bun run --cwd apps/auth-api db:migrate:local` antes de subir o app. D1 desatualizado responde `D1 call failed` e todo refresh de servidores falha com 500.
- Sintoma de conta errada: `auth.getState().user.id` diferente do id que o web client usa; `servers.list()` sem o servidor esperado e web/mobile mostrando "O computador ficou offline".
- Verificacao rapida: `servers.list()` deve mostrar o servidor com `state: "online"`, `role: "owner"` e `apiUrl: wss://signal-us.openbot.run/v1/signal`.

## Recuperacao de start (2026-11-22)

- Sintoma: dialogo "O OpenBot nao conseguiu iniciar — disk I/O error" com o banco intacto (`PRAGMA quick_check` = ok).
- Causa medida: instancia anterior encerrada com `taskkill /F` deixou o perfil travado (lockfile e cache do Chromium com "Acesso negado"); o novo processo nao abriu o SQLite em WAL.
- Rota: encerrar todas as instancias do app, confirmar que nao ha `electron.exe`, e subir de novo. Nao forcar kill; fechar a janela ou usar o stop do dev.
- Higiene: manter espaco livre em C: (nesta maquina havia 7,2 GB livres com 93% de uso) — cache do Chromium falha sob pressao de disco.
