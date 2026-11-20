---
implementation_version: v2
layer: L2
slug: openbot-grafo-hubs-e-ciclos
tags:
  - "#openbot/grafo"
  - "#openbot/impacto"
---

# OpenBot: hubs de import e ciclos medidos

Grafo de imports proprio sobre 7.701 fontes: 35.702 arestas internas, 3.950 por alias '@/', 986 relativos nao resolvidos (assets CSS/imagem/JSON) e 34 ciclos com 427 nos. Hubs de fan-in: packages/contracts/src/ipc.ts (2.036), packages/i18n/src/message.ts (1.600), packages/contracts/src/runtime-values.ts (835), packages/ui/src/text.tsx (689), src/backend/effect-boundary.ts (555). Fan-out alto: src/main/application-services.ts (290), apps/auth-api/src/routeTree.gen.ts (271), src/main/team-api-server.ts (250). O CRG (2.4.0+dex.1) confirma 89.440 nos e 714.460 arestas no mesmo HEAD.

#openbot/grafo #openbot/impacto

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-grafo-hubs-e-ciclos-content
