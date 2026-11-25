---
implementation_version: v2
layer: L2
slug: openbot-checks-and-toolchain-4feeafa3c0fa
tags:
  - "#auto-memory/project"
---

# openbot-checks-and-toolchain

Espelho da auto-memory do host ZCode (arquivo openbot-checks-and-toolchain.md, tipo project).

OpenBot needs bun@1.4.2 and has narrow-check rules; typecheck:node

OpenBot pins `packageManager: bun@1.4.2` (not installed on this machine by default; `npm install -g bun@1.4.2`). Install with `bun install --frozen-lockfile`; its `prepare` sets `core.hooksPath=.githooks`, so the project pre-commit runs and CRG hooks must not clobber it. Build is `bun run build`; tests are `bun run test:desktop -- <file>`; type checks run one project at a time (`typecheck:node`, `typecheck:renderer`). The repo forbids broad local checks.

**Why:** the owner's explicit preference is to keep the machine free and leave wide checks to CI.

`bun run dev` works on Windows but needs retries on a loaded machine: the Auth API readiness window is 30 s, and `dev:status`/`dev:stop` fail with "Could not read the permissions of ...openbot-dev-instances" when its 5 s PowerShell ACL read times out — the stack itself is fine and `bun run dev:stop` still stops it. On first run it seeds a per-worktree `OpenBot Dev` profile.

**How to apply:** never run `bun run typecheck`, `bun run format` or the full suite locally. As of 2026-11-20, `typecheck:node` exits 1 at `scripts/mistral-stuck-turn-e2e.ts:110` (mock lacks `toolCanUseTab`); treat that file as the known red, not as a new regression.

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-checks-and-toolchain-4feeafa3c0fa-content
