---
implementation_version: v2
layer: L2
slug: openbot-rotas-e-workspaces
tags:
  - "#openbot/rotas"
  - "#openbot/arquitetura"
---

# OpenBot: workspaces, denominador e direcao de dependencia

OpenBot e um monorepo unico, sem rota legada separada. Workspaces: apps/* (auth-api, mobile, mobile-updates, site-router, status, apps de mensageria), packages/* (contracts, ui, i18n, logging, telemetry, team-client, user-errors, whatsapp, brand) e remote/api. O desktop mora na raiz (src/main, src/preload, src/renderer, src/backend). Denominador da arqueologia: 7.701 fontes .ts/.tsx/.js/.mjs/.cjs fora de node_modules, dist, build, out e coverage; 1.645.650 linhas; 74,5 MB. Dependencias apontam para packages/contracts; renderer nao importa main/backend; contratos nao importam Electron/SolidJS/Cloudflare.

#openbot/rotas #openbot/arquitetura

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-rotas-e-workspaces-content
