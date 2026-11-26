---
implementation_version: v2
layer: L2
slug: perfil-da-casa-no-default-openbot-20261126
tags:
  - "#openbot/perfil"
---

# Perfil da casa mora no default do OpenBot

Desde 2026-11-26 o perfil de trabalho do OpenBot e o default `%APPDATA%\OpenBot`. Os dados da casa (19 agentes, 1.003 mensagens, migracao 69, credenciais e preferencias) foram copiados de `%APPDATA%\OpenBot Dev`; o default original foi salvo em `.openbot-build/backup-default-20261126-082354`. Os atalhos do Desktop e do Menu Iniciar apontam para o app instalado 0.79.0 sem `--user-data-dir`; o login da conta foi refeito no default com o codigo do Gmail e o app abriu com 26 linhas de agentes. A copia antiga `OpenBot Dev` fica como backup; o dev `bun run dev --shared` abre essa copia, nao a base viva. O banco default esta na migracao 69: o app instalado precisa ser 0.79.0 ou mais novo.

#openbot/perfil

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^perfil-da-casa-no-default-openbot-20261126-content
