# HANDOFF — OpenBot (fork da casa)

Ultima atualizacao: 2026-11-25

## Estado

- `main` local e do fork em `bf5fb4e1f`; base upstream `72f80f561`, 97 commits novos ainda nao portados (`a771a57f7`, tag `v0.77.0`).
- Instalador `dist/OpenBot-0.76.1-x64.exe` com `MAX_HOME_SKILLS = 2000` e `MAX_SKILLS_PER_FOLDER = 5000`; updater aponta para `dex-agent/openbot`, sem releases.
- Perfil de trabalho dos dados: `%APPDATA%\OpenBot Dev`; atalho `OpenBot (dados da casa).lnk` usa `--user-data-dir` desse perfil.
- Rota remota do perfil Dev corrigida para `openbot`; o celular deve conectar quando o host estiver aberto.

## Proximo passo

1. Decidir o port dos 97 commits upstream e revalidar o picker.
2. Se quiser auto-update, publicar release no fork e resolver assinatura Windows (Azure); sem assinatura o app recusa.
3. Revisar a divida antiga do acervo global de notas citaveis (60 findings pre-existentes).

## Retomada

Ler `.agents/ACTIVE.md`, `.agents/GATILHOS-VIVOS.md` e este arquivo; abrir o Trilho `2026-11-24-base-e-build.md`.
