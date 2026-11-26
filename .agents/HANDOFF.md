# HANDOFF — OpenBot (fork da casa)

Ultima atualizacao: 2026-11-26

## Estado

- `main` local e do fork em `1c18515ca`; base upstream `25661054e`, 0 atras e 15 commits da casa a frente.
- Instalador `dist/OpenBot-0.79.0-x64.exe` (240.169.000 bytes, sha256 `ecc7707e...`) instalado em `%LOCALAPPDATA%\Programs\OpenBot`; updater aponta para `dex-agent/openbot`, sem releases.
- Base da casa migrada para o perfil default `%APPDATA%\OpenBot`: 19 agentes e 1.003 mensagens copiados de `OpenBot Dev`, com backup do default em `.openbot-build/backup-default-20261126-082354`; a copia antiga em `OpenBot Dev` ficou como backup.
- Atalhos do Desktop e do Menu Iniciar apontam para o app instalado **sem** `--user-data-dir`; o login da conta da casa foi refeito no perfil default e o app abriu com 26 linhas de agentes.
- Rota remota do perfil default em `openbot`; o celular deve conectar quando o host estiver aberto.

## Proximo passo

1. Confirmar o uso diario no perfil default; se estiver estavel, decidir se a copia `OpenBot Dev` (2,2 GB) sai para a LIXEIRA.
2. O provider DeepSeek pede login no app (banner "E necessario entrar"); nao e a conta OpenBot.
3. Se quiser auto-update, publicar release no fork e resolver assinatura Windows (Azure); sem assinatura o app recusa.
4. Revisar a divida antiga do acervo global de notas citaveis (60 findings pre-existentes).

## Retomada

Ler `.agents/ACTIVE.md`, `.agents/GATILHOS-VIVOS.md` e este arquivo; abrir o Trilho `2026-11-24-base-e-build.md`.
