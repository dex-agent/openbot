---
implementation_version: v2
layer: L2
slug: git-config-flag-order-sets-key-d2c32a0aec20
tags:
  - "#auto-memory/feedback"
---

# git-config-flag-order-sets-key

Espelho da auto-memory do host ZCode (arquivo git-config-flag-order-sets-key.md, tipo feedback).

git config <key> --show-origin consumes the flag as a value; read

`git config core.autocrlf --show-origin` does not read the key. It sets `core.autocrlf` to the literal string `--show-origin` and exits 0. The read form is `git config --show-origin <key>`; to undo the damage, `git config --unset <key>`.

**Why:** the house EOL procedure for the encoding layer hit this trap at runtime and silently corrupted the repo's local config.

**How to apply:** before reading any git config value, put `--show-origin` before the key. Verify the local config after any suspicious exit 0.

#auto-memory/feedback

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^git-config-flag-order-sets-key-d2c32a0aec20-content
