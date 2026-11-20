---
implementation_version: v2
layer: L2
slug: openbot-gerados-e-ofuscacao
tags:
  - "#openbot/gerados"
  - "#openbot/ofuscacao"
---

# OpenBot: superficie gerada e ausencia de ofuscacao

Superficie gerada: packages/whatsapp/vendor/baileys/WAProto/index.js tem 97.691 linhas; packages/i18n/src/messages tem 1.620 arquivos .ts em 15 locales; plugin-catalog.generated.ts (auth-api e mobile) e routeTree.gen.ts sao gerados. Nao ha .min.js versionado, nao ha eval/new Function reais (as 45 ocorrencias sao metodo .eval de harness/shader) e atob aparece 10 vezes em codigo legitimo de base64. O vendor Baileys responde por 174 arquivos e 161.712 linhas do total.

#openbot/gerados #openbot/ofuscacao

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-gerados-e-ofuscacao-content
