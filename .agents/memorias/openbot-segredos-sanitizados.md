---
implementation_version: v2
layer: L2
slug: openbot-segredos-sanitizados
tags:
  - "#openbot/seguranca"
  - "#openbot/segredos"
---

# OpenBot: segredos versionados sao cifrados ou fixtures

Os 5 arquivos .env versionados (apps/auth-api/.env.dev, .env.production, .env.example; remote/.env.example, .env.production) usam dotenvx: chave publica + valores 'encrypted:'. O .env.keys da raiz esta ausente e e ignorado por .gitignore. A varredura sanitizada achou 167 ocorrencias: praticamente todas sao fixtures de teste ou placeholders mascarados. Dois achados reais e nao secretos: apps/mobile/google-services.json (chave de API Firebase de cliente, publica por desenho) e uma constante de chave publica em packages/whatsapp/vendor/baileys/src/WABinary/constants.ts. Nenhum segredo de servidor em texto claro.

#openbot/seguranca #openbot/segredos

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-segredos-sanitizados-content
