# Gatilhos vivos — OpenBot (fork da casa)

Hub quente de retomada. Cada gatilho tem Quem, Por que, Como, Quando, Onde e E se??.
Fonte viva vence memória.

| Gatilho | Quem | Quando lembrar | Fonte viva / ação |
| --- | --- | --- | --- |
| STALENESS-ARTEFATOS-DERIVADOS | sessão do projeto (fiscal: `dex-fechamento-projeto-atualizado`) | antes de ler ou citar CRG, Graphify, PLAYBOOK, INDEX, receipt de capacidade ou fluxo de decisão | comparação de 3 números abaixo; regenerar antes de citar |
| MERGE-CHECK-HOOK-PRE-MERGE | hook do repo `.githooks/pre-merge-commit` | todo `git merge` local neste repo | `tools/hooks/merge-check.conf` + escape `MERGE_CHECK_SKIP=1` |
| CRG-LOCAL-STRUCTURAL-GRAPH | sessão do projeto | review estrutural, impacto, arquitetura, antes de citação do grafo | `code-review-graph status --repo . --data-dir .agents/CODE-REVIEW-GRAPH` |
| OPENBOT-PERFIL-DEV-POR-WORKTREE | sessão do projeto | app "abre vazio" ou "perdeu os dados" depois de trocar o modo de launch | `scripts/dev-services.ts` `developmentInstanceIdForStart`; perfis em `%APPDATA%` |
| OPENBOT-ROTA-REDE-PRIVADA | sessão do projeto | celular/web não conecta com `webRTC/ice/failed` mesmo com o host aberto | `openbot-remote-network-route-v1.json`; Configurações → "Como os dispositivos se conectam" |
| OPENBOT-UPDATE-SOURCE-FORK | sessão do projeto / quem publica build | app baixa ou instala versão do upstream e perde o fix do picker | `electron-builder.yml` `publish.owner`; `resources/app-update.yml` |
| RITUAL-MEMORIA-BLOCO-OPENBOT | sessão do projeto | fechamento de todo bloco material; frases `APRENDIZADO-MEMORAVEL-CONTINUO` e `AUTO-MEMORY-ZCODE-GARIMPA-DEX-MEMORIA` | `~/.agents/AGENTS.md` + `~/.agents/CONTRACTS/`; `dex-memoria`; gate `dex-notas-citaveis` |
| REBASE-BUILD-RELEASE-TEST-OPENBOT | sessão do projeto | todo rebase da `main` sobre `origin/main` | `bun install` + `dist:win` + teste executando + `git push --force-with-lease fork main` |

## STALENESS-ARTEFATOS-DERIVADOS

- **Quem**: a sessão do projeto que vai ler ou citar o artefato; fiscalização por `dex-fechamento-projeto-atualizado` e `guarda-plaquinhas`. O dono do artefato é a ferramenta que o gera.
- **Por que**: todo artefato derivado nasce fotografando a fonte num instante. Fonte que mudou sem regeneração transforma foto velha em ruído confiável — falso verde. Exemplo medido nesta casa: CRG construído em `eed928df8` (2026-11-20) e repositório avançando 187 commits até `762b24085` (2026-11-21); citar o grafo velho seria citar um código que não existe mais.
- **Como**: comparar SEMPRE três números: (a) quando a FONTE mudou — `git log -1 --format=%cI` no repo (ou `stat -c %y` dos arquivos-fonte); (b) quando o ARTEFATO foi gerado — o timestamp do próprio artefato (comando de status ou `stat` do arquivo); (c) se fonte > artefato então STALE: rodar o comando de regeneração do artefato e só depois citar o conteúdo. Staleness é medido em segundos, nunca "parece atual".
- **Quando**: antes de qualquer leitura ou citação de artefato derivado — janela fria, re-arqueologia, review estrutural, decisão que diz "o grafo diz X", relatório que cita PLAYBOOK, INDEX ou receipt de capacidade.
- **Onde**: este hub, mais os comandos por artefato inventariados neste repo:
  - CRG estrutural — artefato `.agents/CODE-REVIEW-GRAPH/graph.db` (campo "Last updated" e "Built at commit"); leitura `code-review-graph status --repo . --data-dir .agents/CODE-REVIEW-GRAPH` e `code-review-graph doctor` (read-only; "built at X but HEAD is Y" = stale); regeneração `code-review-graph build --repo . --data-dir .agents/CODE-REVIEW-GRAPH` (completa) ou `code-review-graph update --repo . --data-dir .agents/CODE-REVIEW-GRAPH` (incremental).
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

## OPENBOT-PERFIL-DEV-POR-WORKTREE

- **Quem**: sessão do projeto que inicia o app; dono da regra é `scripts/dev-services.ts`.
- **Por que**: o nome da pasta de dados depende do modo de launch, não do código. `bun run dev --shared` usa `%APPDATA%\OpenBot Dev`; `bun run dev` sem `--shared` usa `OpenBot Dev wt-<sha256 do root>`; o app empacotado usa `%APPDATA%\OpenBot`. Trocar o modo parece "perda de dados" — o banco antigo continua intacto na outra pasta, com agentes e mensagens. Desde 2026-11-26 a base da casa foi migrada para o perfil default `%APPDATA%\OpenBot`; o `OpenBot Dev` ficou como cópia/backup e o dev `--shared` abre essa cópia, não a base viva.
- **Como**: antes de diagnosticar perda, ler o `--user-data-dir` do processo (`Get-CimInstance Win32_Process -Filter "Name='electron.exe'"`) e comparar com as pastas em `%APPDATA%`: a que tem `openbot.db` grande e WAL recente é a viva. Para voltar à mesma base, repetir o mesmo modo de launch.
- **Quando**: app abre vazio, lista de agentes/threads muda, ou o usuário relata "sumiu tudo" após reiniciar.
- **Onde**: `scripts/dev-services.ts` (`developmentInstanceIdForStart`, `developmentInstanceIdForWorktree`), `src/main/development-profile.ts` (`developmentUserDataName`), `scripts/dev-stack.ts status`. Atalhos de trabalho na Área de Trabalho e no Menu Iniciar: exe instalado **sem** `--user-data-dir`; o perfil default `%APPDATA%\OpenBot` é a base da casa desde 2026-11-26.
- **E se?? duas pastas tiverem `openbot.db` parecidos?** → comparar `projection_agents` / `projection_thread_messages` por contagem e data da última mensagem; o perfil maior e mais recente é o de trabalho.
- **E se?? a pasta wt existir e o usuário quiser descartar?** → garimpar as threads (seed tem títulos fixos criados no mesmo segundo) e registrar `LIXEIRA` + `MANIFEST.md`; nunca copiar cookies, `Local State` ou credenciais.

## OPENBOT-ROTA-REDE-PRIVADA

- **Quem**: a sessão do projeto que diagnostica conexão de celular ou web; dono do comportamento é o par `src/renderer/src/features/team/team-webrtc.ts` + `src/main/ipc/app-handlers.ts`.
- **Por que**: a preferência `route: "private"` ("Rede privada", Tailscale/Wi-Fi) faz o host anunciar `iceServers: []` e filtrar candidatos para a rede local. Celular fora dessa rede falha com `webRTC/ice/failed` mesmo com o host aberto e o signal conectado. Medido em 2026-11-24: a preferência do perfil Dev estava `private` e o celular em dados móveis não conectava. A base da casa hoje é o perfil default `%APPDATA%\OpenBot`; o arquivo abaixo é o dessa base.
- **Como**: ler `%APPDATA%\OpenBot\openbot-remote-network-route-v1.json` (a cópia antiga fica em `OpenBot Dev`); no app, Configurações → "Como os dispositivos se conectam" → **"Pelo OpenBot"** (aplica na hora via `setRemoteNetworkRoute`). Conferir o host: conexão TCP estabelecida com `signal-us.openbot.run` e `logs/main/main.log` sem erro de signal.
- **Quando**: celular/web mostra "Carregando Servidor de …" e `webRTC/ice/failed`; ou a conexão só funciona no mesmo Wi-Fi.
- **Onde**: `src/renderer/src/features/team/team-webrtc.ts` (`iceServers: state.privateNetwork ? [] : iceServers`), `src/main/remote-network-route-preference-store.ts`, `packages/contracts/src/ipc-remote-sessions.ts` (`REMOTE_NETWORK_ROUTES`), arquivo JSON no perfil.
- **E se?? o usuário quiser a rota privada e conexão fora de casa?** → a rota privada exige Tailscale no celular e os dois na mesma tailnet; sem isso, usar "Pelo OpenBot".
- **E se?? o arquivo já estiver `openbot` e ainda falhar?** → medir o relay TURN e o signal antes de concluir "host offline"; abrir o log, não adivinhar.

## OPENBOT-UPDATE-SOURCE-FORK

- **Quem**: a sessão que gera ou instala build; donos são `electron-builder.yml` (bloco `publish`) e `resources/app-update.yml` do app instalado.
- **Por que**: com `publish.owner: nightly-labs`, o `electron-updater` baixa o release do upstream e instala por cima da nossa build, apagando o fix `MAX_HOME_SKILLS = 2000` / `MAX_SKILLS_PER_FOLDER = 5000`. Medido em 2026-11-24: `OpenBot-0.77.0-x64.exe` (236 MB) baixado do upstream em `%LOCALAPPDATA%\openbot-updater\pending`.
- **Como**: manter `publish.owner: dex-agent` no `electron-builder.yml` e no `app-update.yml` do app instalado; apagar `pending` quando houver download; recompilar com `bun run dist:win` e PATH com `/c/Windows/System32` (bsdtar). O fork não publica releases, então a checagem termina em `ERR_UPDATER_NO_PUBLISHED_VERSIONS` — sem update.
- **Quando**: antes de gerar ou instalar build; ao ver "Nova atualização" ou arquivo em `openbot-updater`.
- **Onde**: `electron-builder.yml`, `dist/win-unpacked/resources/app-update.yml`, `%LOCALAPPDATA%\openbot-updater`, `docs/RELEASING.md` ("updates are published through GitHub Releases").
- **E se?? quisermos auto-update de verdade?** → precisa de release no fork + assinatura Windows (Azure Artifact Signing); sem assinatura o `src/main/windows-update-signature.ts` recusa. Cloudflare não serve para update do desktop.
- **E se?? o update do upstream já instalou?** → conferir `MAX_HOME_SKILLS = 2e3` no `app.asar`; se ausente, reinstalar o nosso `dist/OpenBot-0.76.1-x64.exe`.

## RITUAL-MEMORIA-BLOCO-OPENBOT

- **Quem**: a sessão do projeto no fechamento de cada bloco material; dona global do ritual é a plaquinha `APRENDIZADO-MEMORAVEL-CONTINUO`, com espelho obrigatório `AUTO-MEMORY-ZCODE-GARIMPA-DEX-MEMORIA`.
- **Por que**: o dono não deve repetir o pedido em cada janela. Sem ficha local, uma janela fria neste repo não encontra o ritual e o ouro do bloco fica no chat.
- **Como**: investigar a sessão com as lentes `entrevista-com-docs`, `interrogador-documental` e `investigador-socratico`; manter `garimpeiro` e `estacionamento` ativos; achado forte operacional grava no `dex-memoria v2 remember` (project ou global) e valida com `consciencia-memorias` (`validate-memory-batch.py --root <root>`); achado notável de referência grava pelo gate `dex-notas-citaveis emit` e fecha com `check`; tropeço de ferramenta vira nota ou ficha tática. O fechamento informa 🧠 memoráveis, 🚧 tropeços e 🔥 gatilhos L1 usados, oferece EDIÇÃO do que já foi gravado e roda `dex-fechamento-projeto-atualizado`.
- **Quando**: todo fechamento de bloco material e sempre que o dono usar as frases `APRENDIZADO-MEMORAVEL-CONTINUO` ou `AUTO-MEMORY-ZCODE-GARIMPA-DEX-MEMORIA`; `AUTO-MEMORY` também dispara quando uma auto-memory do host ZCode for gravada ou atualizada.
- **Onde**: `~/.agents/AGENTS.md` (plaquinhas), `~/.agents/CONTRACTS/APRENDIZADO-MEMORAVEL-CONTINUO.md` e `AUTO-MEMORY-ZCODE-GARIMPA-DEX-MEMORIA.md`, `C:\CodexProjetos\dex-memoria\SKILL.md` (entrada cotidiana), gate em `~/.agents/skills/dex-notas-citaveis/scripts/gate-notas-citaveis.py`.
- **E se?? o achado já foi gravado dentro do bloco?** → o fechamento só oferece edição, nunca pede permissão para gravar de novo.
- **E se?? o destino estiver ambíguo (projeto, global, tema)?** → não inventar rota; estacionar com owner e `quando` até a decisão.
- **E se?? a validação do lote acusar dívida antiga fora do corte?** → registrar a dívida como risco restante e exigir zero achados nos arquivos tocados.

## REBASE-BUILD-RELEASE-TEST-OPENBOT

- **Quem**: a sessão do projeto que executa o rebase; o dono autorizou este fluxo como padrão para todo rebase.
- **Por que**: rebase sem build deixa o instalador velho e a regressão fica invisível. Medido em 2026-11-25: a base ja estava em 0.78.0 e o app instalado seguia 0.76.1; sem executar o build novo ninguém prova que ele abre.
- **Como**: depois do rebase limpo, rodar `bun install --frozen-lockfile`; compilar com `PATH="/c/Windows/System32:$PATH" bun run dist:win`; rodar o gate de listagem `bun scripts/home-skills-listing-e2e.ts` e exigir listadas = no disco (724/724); no asar, conferir `MAX_SKILLS_PER_FOLDER = 5e3`, `owner: dex-agent` no `app-update.yml` e hash de `out/main/index.js` igual ao do build (o literal `MAX_HOME_SKILLS = 2e3` pode ser inlinado); fotografar alvo/argumentos dos atalhos OpenBot do Desktop e do Menu Iniciar; executar `dist/win-unpacked/OpenBot.exe` com o perfil real (nesta máquina o default `%APPDATA%\OpenBot`, sem `--user-data-dir`; use `--user-data-dir` só para perfil nomeado) e `--remote-debugging-port`, exigir a pagina `openbot-app://app/index.html` com titulo OpenBot e ler o print; restaurar os atalhos e conferir que nenhum aponta para `dist/win-unpacked`; registrar tamanho e sha256 no `UPSTREAM.md`; publicar com `git push --force-with-lease fork main`.
- **Quando**: todo rebase da `main` sobre `origin/main`, antes de declarar o bloco concluido.
- **Onde**: receita completa em `~/.agents/workflow/rebase-repo-build-release/WORKFLOW.md`; artefatos em `dist/win-unpacked/OpenBot.exe` e `dist/OpenBot-<versao>-x64.exe`; registro em `.agents/UPSTREAM.md`; remote `fork`.
- **E se?? o build falhar?** → nao publicar; corrigir a causa e repetir o ciclo inteiro.
- **E se?? o teste nao abrir a janela principal?** → inspecionar CDP e log; nao declarar pronto com so a dynamic island.
- **E se?? o dono pedir GitHub Release?** → push de codigo nao cria release; release exige `gh` autenticado e assinatura Windows, senao o updater recusa.
- **E se?? o atalho do Menu Iniciar ficar apontando para `dist/win-unpacked`?** → restaurar o alvo anterior (atalho estavel = app instalado) e conferir; caminho em `dist` e efemero. O perfil default `%APPDATA%\OpenBot` e a base da casa, entao atalho sem `--user-data-dir` e o correto.
- **E se?? o banco ja tiver migrado acima do app instalado?** → nao restaurar atalho para o app velho; instalar o build novo ou apontar o atalho para o build atual com o perfil da casa.

## MERGE-CHECK-HOOK-PRE-MERGE

- **Quem**: o hook do repositório (`core.hooksPath = .githooks`), instalação e manutenção pela sessão do projeto.
- **Por que**: sem gate, merge que quebra nasce. O hook roda o merge-check de três vias antes de o commit de merge existir, então conflito semântico não entra na `main`.
- **Como**: `.githooks/pre-merge-commit` lê `tools/hooks/merge-check.conf` (`SUITE="bun run test:desktop"`). Sem merge em curso, sai em silêncio. `MERGE_CHECK_SKIP=1` ou `git merge --no-verify` passam com uma linha de aviso. Merge sem resolução manual roda `code-review-graph merge-check --repo . --base BASE --ours OURS --theirs THEIRS --test-failure-exit 1 -- <SUITE>`: exit 0 libera, exit 1 bloqueia com inspeção, exit 2 (execution_error) reporta e não bloqueia. Merge já resolvido à mão roda a suíte direto no worktree.
- **Quando**: todo `git merge` local neste repositório; antes de qualquer merge que precise nascer verde.
- **Onde**: `.githooks/pre-merge-commit`, `tools/hooks/merge-check.conf`, `core.hooksPath` vigente.
- **E se?? o merge vier por PR remoto?** → o hook local não roda; o agente executa o `merge-check` completo antes de aprovar o merge.
- **E se?? o índice CRG estiver stale?** → não invalida o gate: o `merge-check` constrói laboratório próprio; a citação do grafo é que segue a regra `STALENESS-ARTEFATOS-DERIVADOS`.
- **E se?? a suíte não estiver instalada no checkout do merge?** → o merge-check devolve execution_error (exit 2) e o merge não é bloqueado por suíte doente.

