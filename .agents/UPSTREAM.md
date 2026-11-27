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
- 2026-11-25T14:49Z: `origin/main` em `73c360d92` (tag `v0.78.0`); 329 commits novos desde a nossa base. Nenhum commit toca `src/backend/home-skills.ts` nem `src/main/skill-folder-discovery.ts` (upstream segue 200/200; os nossos 2000/5000 intactos). `packages/ui/src/features/conversation/` recebeu 13 commits (ex.: `903118bdb` progresso de anexo, `a680e9f59` Mermaid alto, `c2393cfe0` Delete agent); o nosso fix do picker nao toca esse diretorio — sem sobreposicao.
- 2026-11-25 (rebase + build): `main` rebaseada sobre `73c360d92` sem conflito (12 commits da casa, 0 atras). Instalador `dist/OpenBot-0.78.0-x64.exe`, 238.125.003 bytes, sha256 `1286398dfe3033b90f6cac956b181424bc54c8d1c2d065baf9ee6529908d807d`; updater em `dex-agent` e tetos 2000/5000 confirmados no asar. Testado executando `dist/win-unpacked/OpenBot.exe` (0.78.0) com perfil temporario: janela `openbot-app://app/index.html` abriu com titulo OpenBot. Publicado no fork (`30c52e199`).
- 2026-11-26T11:10Z: `origin/main` em `25661054e99e` (mobile-announced/v1.4.14/android); 84 commits novos absorvidos e 14 commits da casa preservados, rebase sem conflito. Instalador `dist/OpenBot-0.79.0-x64.exe`, 240.169.000 bytes, sha256 `ecc7707e23c8e03aee95505b009a92bca215affe57134299fec6fa924be90662`; updater em `dex-agent` e tetos 2000 (home) / 5000 (por pasta) confirmados; listagem 724 de 724. Teste com o perfil real: `openbot-app://app/index.html`, loggedIn=true, 5 agentes, print em `.openbot-build/openbot-079-real-profile.png`. Publicado no fork logo apos este commit.
- 2026-11-26T12:00Z: `origin/main` em `1b88faff35d6be98b362dc3cf28d340fccedca19`; 14 commits novos desde o HEAD local (`7324c9e6b`). Nenhum toca `src/backend/home-skills.ts` nem `src/main/skill-folder-discovery.ts`. `packages/ui/src/features/conversation/` recebeu `440373e24` (`ImageGeneration.tsx`, `MessageRendering.tsx`); o fix do picker nao toca esse diretorio. Sem merge, rebase, commit ou push nesta verificacao.
- 2026-11-27T12:00Z: `origin/main` em `ac6e70cd937a54795e0b5e3a6f77c07a6aa62980`; 110 commits novos desde o HEAD local (`7324c9e6b`). A tag `v0.80.0` aponta para `53ded5570`, 35 commits atras do topo. Nenhum toca `src/backend/home-skills.ts` nem `src/main/skill-folder-discovery.ts`. `packages/ui/src/features/conversation/` recebeu 4 commits: `b558bbe91` (`MediaApprovalCard.tsx`), `5bf7b384f` (`AgentThreadView.tsx`, `UiBlockCard.tsx`), `4892513fe` (`MarkdownMessageText.tsx`, `message-content.css`) e `440373e24` (`ImageGeneration.tsx`, `MessageRendering.tsx`); o fix do picker nao toca esse diretorio. Sem merge, rebase, commit ou push nesta verificacao.
- 2026-11-27T17:16Z: `origin/main` em `ee8c9a1cc7e0db979f9ad934aba4be2490bb35b2` (tag `v0.80.0`); 134 commits novos absorvidos e 17 commits da casa preservados, rebase sem conflito. Instalador `dist-0.80.0/OpenBot-0.80.0-x64.exe`, 240273018 bytes, sha256 `ee829c3c3415892bea1449c79981021506eea1de8b09204282f58224584b68e8`; updater em `dex-agent` e tetos 2000 (home) / 5000 (por pasta) confirmados; listagem 729 de 729. Teste com o perfil real default: `openbot-app://app/index.html`, loggedIn=true, 25 agentes, print em `.openbot-build/openbot-0.80.0-real-profile.png`. Instalacao: ok=true, versao instalada 0.80.0, removidos `OpenBot-0.79.0-x64.exe` e `OpenBot-0.79.0-x64.exe.blockmap`. Publicado no fork logo apos este commit.

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
