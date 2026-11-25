---
implementation_version: v2
layer: L2
slug: msys-converts-at-slash-rg-patterns-49a9637e5e50
tags:
  - "#auto-memory/feedback"
---

# msys-converts-at-slash-rg-patterns

Espelho da auto-memory do host ZCode (arquivo msys-converts-at-slash-rg-patterns.md, tipo feedback).

In Git Bash, an rg search pattern starting with @/ is

In Git Bash on Windows, `rg '@/features' <path>` returns no match and exit 1 even when the literal text is present. MSYS converts the pattern before ripgrep receives it. Working forms: prefix with a literal (`rg -F 'from "@/features'`) or set `MSYS_NO_PATHCONV=1`.

**Why:** a silent zero from a search tool turns into a false conclusion that the alias is unused. The OpenBot TS alias `@/` is used in 667 files, and the first count came back 0.

**How to apply:** when a search for a string that starts with `@/`, `/c/` or another path-like prefix returns nothing, rerun with `MSYS_NO_PATHCONV=1` before concluding absence.

#auto-memory/feedback

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^msys-converts-at-slash-rg-patterns-49a9637e5e50-content
