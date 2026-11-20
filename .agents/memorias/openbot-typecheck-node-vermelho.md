---
implementation_version: v2
layer: L2
slug: openbot-typecheck-node-vermelho
tags:
  - "#openbot/tropeco"
  - "#openbot/tipos"
---

# OpenBot: typecheck:node vermelho por mock sem toolCanUseTab

No HEAD 140d75f, bun run typecheck:node sai 1 com TS2741 em scripts/mistral-stuck-turn-e2e.ts:110: o mock AgentBrowserHost nao tem toolCanUseTab, exigido por src/backend/agent/attention-registry.ts:441. Os outros 19 scripts e2e ja tem 'toolCanUseTab: () => false'. Correcao minima: acrescentar essa linha ao mock. O build, typecheck:renderer e o teste estreito estao verdes; a arqueologia registra rota vermelha com owner e quando em .agents/ESTACIONAMENTO.md.

#openbot/tropeco #openbot/tipos

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-typecheck-node-vermelho-content
