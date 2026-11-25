---
implementation_version: v2
layer: L2
slug: build-do-fork-nao-pode-herdar-o-publish-do-upstream-d3b01afa39c5
tags:
  - "#openbot/distribuicao"
---

# Build do fork nao pode herdar o publish do upstream

O bloco publish do electron-builder.yml herdado do upstream apontava owner nightly-labs. Com isso o electron-updater baixou OpenBot 0.77.0 do upstream (236 MB em LOCALAPPDATA openbot-updater pending) e instalaria por cima da build da casa, apagando a correcao do picker com MAX_HOME_SKILLS 2000 e MAX_SKILLS_PER_FOLDER 5000. Cura aplicada em 2026-11-24: owner dex-agent no electron-builder.yml e no app-update.yml do app instalado; apagar o pending; recompilar com bun run dist:win e PATH com a pasta System32 para usar bsdtar. O fork nao publica releases, entao a checagem termina em ERR_UPDATER_NO_PUBLISHED_VERSIONS, que e o estado esperado. Atualizacao do desktop usa GitHub Releases; Cloudflare serve a conta e o OTA do celular, nao o desktop. Auto-update real exige release no fork e assinatura Windows (Azure Artifact Signing); o windows-update-signature.ts recusa instalador sem assinatura aceita.

#openbot/distribuicao

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^build-do-fork-nao-pode-herdar-o-publish-do-upstream-d3b01afa39c5-content
