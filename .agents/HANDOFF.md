# HANDOFF — OpenBot (fork da casa)

Ultima atualizacao: 2026-11-27

## Estado

- `main` local em `d4bb765df`; rebaseada sobre `ee8c9a1cc` (tag `v0.80.0`), 0 atras e 17 commits da casa a frente (134 commits do upstream absorvidos, sem conflito). Publicacao no fork logo apos o commit deste registro; `fork/main` ainda em `1c18515ca`.
- Instalador `dist-0.80.0/OpenBot-0.80.0-x64.exe` (240.273.018 bytes, sha256 `ee829c3c...`) instalado em `%LOCALAPPDATA%\Programs\OpenBot` (versao 0.80.0); updater aponta para `dex-agent/openbot`, sem releases.
- Tetos do picker 2000 (home) / 5000 (por pasta) confirmados na fonte; listagem 729 de 729.
- Teste com o perfil real default: `openbot-app://app/index.html`, loggedIn=true, 25 agentes, print em `.openbot-build/openbot-0.80.0-real-profile.png`; backup do perfil em `.openbot-build/backup-080-20261127-140941`.
- Instalacao do build novo: ok=true; removidos `OpenBot-0.79.0-x64.exe` e `OpenBot-0.79.0-x64.exe.blockmap`.
- Base da casa no perfil default `%APPDATA%\OpenBot` (migrada de `OpenBot Dev` em 2026-11-26, backup `.openbot-build/backup-default-20261126-082354`); atalhos do Desktop e do Menu Iniciar apontam para o app instalado **sem** `--user-data-dir`.
- Rota remota do perfil default em `openbot`; o celular deve conectar quando o host estiver aberto.

## Proximo passo

1. Confirmar o uso diario no perfil default; se estiver estavel, decidir se a copia `OpenBot Dev` (2,2 GB) sai para a LIXEIRA.
2. O provider DeepSeek pede login no app (banner "E necessario entrar"); nao e a conta OpenBot.
3. Se quiser auto-update, publicar release no fork e resolver assinatura Windows (Azure); sem assinatura o app recusa.
4. Revisar a divida antiga do acervo global de notas citaveis (60 findings pre-existentes).

## Retomada

Ler `.agents/ACTIVE.md`, `.agents/GATILHOS-VIVOS.md` e este arquivo; abrir o Trilho `2026-11-24-base-e-build.md`.
