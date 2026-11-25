---
implementation_version: v2
layer: L2
slug: openbot-provider-integration-limits-953c9794237b
tags:
  - "#auto-memory/project"
---

# openbot-provider-integration-limits

Espelho da auto-memory do host ZCode (arquivo openbot-provider-integration-limits.md, tipo project).

OpenBot has no ZCode provider; custom providers only run on OpenCode

OpenBot has 18 native providers (`packages/contracts/src/agent-providers.ts`); ZCode is not one. The "custom provider" dialog is not a general harness picker: `custom-provider-harness-v1.ts` accepts only `oneOf("opencode","pi")`, so "Executa em" lists just those two. The ApiHub/Agnes endpoint form in that dialog is an OpenAI-compatible endpoint run by OpenCode or Pi, not by ZCode.

The "Custom ACP agent" preset needs an agent that speaks the Agent Client Protocol as a server. The ZCode CLI (0.17.1) exposes `app-server` ("ZCode Protocol"), `-p`, `tui`, `plugins` and `skills`, but no ACP command; the official ACP registry (46 agents) has no zcode entry. ZCode's bundled ACP SDK is a library, not proof of a serving mode. ZCode's upstream is an OpenAI `/chat/completions` client, so it cannot act as an endpoint either.

OpenBot's Codex provider spawns `codex app-server --listen stdio://`; ZCode has its own app-server protocol, so whether the Codex client can drive it is unconfirmed and needs an `initialize` probe before any adapter work.

**Why:** the owner asked "não tem suporte pro zcode?" and the answer is structural, not a missing setting.

**How to apply:** two real routes exist — a thin ACP bridge around the ZCode CLI registered as a *Custom ACP agent*, or a native OpenBot adapter (new provider, driver, sign-in, Team API). Pick with `$ponytail` (smallest complete path) and prove with an E2E, never by assumption. See [[openbot-remote-access-topology]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-provider-integration-limits-953c9794237b-content
