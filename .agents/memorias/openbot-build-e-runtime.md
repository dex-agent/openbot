---
implementation_version: v2
layer: L2
slug: openbot-build-e-runtime
tags:
  - "#openbot/build"
  - "#openbot/runtime"
---

# OpenBot: build, testes e runtime medidos

O openbot e um monorepo Bun: packageManager bun@1.4.2, engines node>=24 (medido v24.19.0), lockfile bun.lock. Instalacao fiel: bun install --frozen-lockfile. Build desktop: bun run build (electron-vite build), medido exit 0 em 24,28s e out/ com 76 MB. Teste estreito: bun run test:desktop -- <arquivo> (vitest run). Tipos por projeto: bun run typecheck:node e bun run typecheck:renderer (um por vez). Lint de arquivo: biome check --write --max-diagnostics=none. Nao rodar bun run format, bun run typecheck agregado nem suite ampla local. O prepare do bun install ativa core.hooksPath=.githooks via scripts/install-git-hooks.ts.

#openbot/build #openbot/runtime

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-build-e-runtime-content
