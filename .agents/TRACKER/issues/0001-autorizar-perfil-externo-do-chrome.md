---
id: ISSUE-LOCAL-0001
titulo: Autorizar perfil externo do Chrome compartilhado
status: aberto
prioridade: P2
tipo: bug
tags:
  - "#tracker/issue"
  - "#tracker/openbot"
aberto_por: sessao
criado_em: 2026-11-23
atualizado_em: 2026-11-23
origem: sessao
receipt: .agents/receipts/issues/20261123-162251-chrome-compartilhado
---

# Autorizar perfil externo do Chrome compartilhado

## Problema e impacto

O OpenBot encontra a janela do Chrome compartilhado ativo, mas o controlador exige autorização específica para ler a aba do perfil externo. Na instalação afetada, o agente recebe uma instrução de parada após essa recusa. O gatilho do Gmail ficou sem configuração e a entrega do aviso segue sem teste.

## Evidências

- Retorno do controlador: `browser_consent_required` com motivo `consumer_profile_endpoint_requires_grant`, observado novamente após autorização no chat.
- Regra de parada em [developer-instructions.ts](../../../src/backend/agent/developer-instructions.ts#L508). O [contrato de perfis](../../../docs/architecture/browser.md#browser-sessions) explica que o seletor do agente usa as sessões internas do OpenBot.
- [Laudo](../../receipts/issues/20261123-162251-chrome-compartilhado/laudo.md) e [corpo publicável](../../receipts/issues/20261123-162251-chrome-compartilhado/corpo-issue.md).
- [Issue upstream](https://github.com/nightly-labs/openbot/issues/14865).

## Critérios de aceite

- O dono pode autorizar agentes selecionados a usar um perfil externo específico.
- Em Windows, o agente autorizado lê a aba existente. Um agente sem autorização recebe a recusa e o usuário vê a ação de consentimento disponível.
- Perfis fora da autorização continuam protegidos. Revogar a autorização bloqueia novas leituras, sem transferir cookies ou sessões.

## Lacunas

A correção ainda não foi implementada nem testada. O destino de publicação é `dex-agent/openbot`. O fork está com Issues ativo, mas a integração recusou a escrita. Quando o administrador conceder essa permissão, conferir duplicatas, publicar e registrar a URL somente após reabrir a issue no fork.
