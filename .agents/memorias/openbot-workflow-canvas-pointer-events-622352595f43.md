---
implementation_version: v2
layer: L2
slug: openbot-workflow-canvas-pointer-events-622352595f43
tags:
  - "#auto-memory/project"
---

# openbot-workflow-canvas-pointer-events

Espelho da auto-memory do host ZCode (arquivo openbot-workflow-canvas-pointer-events.md, tipo project).

OpenBot's Workflows canvas ignores element.click(); chips, menus and node links need synthesized pointer sequences, graph state is verified via data-node-id/data-edge-id, and Kobalte selects only accept real CDP mouse input.

Automating the OpenBot web client's Workflows canvas (measured 2026-11-20):

- `element.click()`, Playwright `getByRole(...).click()` and label clicks fail silently — no error, no state change.
- Working recipe: dispatch in order on the element, with `bubbles: true`, `cancelable: true`, `view: window`, `clientX/clientY` at the element centre, `pointerId: 1`, `isPrimary: true`: `pointerdown` → `mousedown` → `pointerup` → `mouseup` → `click`.
- Canvas menus are `div[role="menuitemradio"]` / `[role="menuitem"]`, not buttons. "Add node" offers Trigger, Prompt, Asset, LLM, Agent, Image, Video, Condition, Approval, Output.
- Trigger type chip: `button[aria-label^="Type:"]` (types: schedule, manual, webhook, message, github, discord, telegram, slack).
- Agent on a node: `.wfn-agent-pill`; task text: `textarea` inside `[data-node-id]` (set via the native value setter + `input`/`change`).
- To connect: `pointerdown` on `.wfn-port[data-wfn-port-side="out"]`, ~8 `pointermove` on `document.body`, then `pointerup` on `document.elementFromPoint(targetX, targetY)`.
- Verify the graph by counting `[data-node-id]` and `[data-edge-id]`, then `location.reload()` and recount. `tab.playwright.screenshot` does not exist in this harness and `tab.execute` accepts only its command union, so DOM counts are the proof.

**Kobalte selects need real input — RESOLVED by CDP (2026-11-20).** The agent-settings **Access** select (Kobalte `SelectPrimitive.Item`, `packages/ui/src/select.tsx`) ignores every in-page synthetic path: DOM click, the pointer sequence above, label click, keyboard (`Enter`, `ArrowDown`+`Enter`, digit typeahead). It opens (`aria-expanded="true"`, `ul[role="listbox"]` present) but the value never changes. Working route: connect Playwright over CDP to the **desktop app** (`chromium.connectOverCDP("http://127.0.0.1:9333")`, page `openbot-app://app/index.html`), then `locator.scrollIntoViewIfNeeded()` + `page.mouse.click(...)` on the trigger and on the `[role="option"]`. The full 7-agent matrix was then applied with `.agents/scripts/set-agent-permissions.mjs` and read back 7/7. Two navigation details matter more than the click itself: the panel opens a sub-page, so the next agent needs the **"Voltar às configurações"** (`Back to settings`) control pressed first (else "Permissions row not found"), and the current value must be read from the button whose text starts with `Acesso` (`Access`). Agent rows match both `button[aria-label^="<Name>."]` and `button[aria-label^="<Name>,"]`.

**Why:** three separate chips ("Type", node menu, agent pill) looked broken; the real cause was the pointer-event sequence, not a disabled control. The exact opposite mistake is also costly — assuming the sequence works everywhere and reporting a permission as changed when it did not. Injecting input from the page cannot satisfy a control that needs trusted input; only the CDP `Input` domain can.

**Model picker (measured 2026-11-20):** the agent settings model row is a `provider-model-popover` with one tab per provider (`button[aria-label^="DeepSeek:"]`, `OpenCode:`, `Pi:`, `Personalizado:`) and the names as `[role="option"]` inside `.provider-model-list`. It also stays open after a change and reports the new name immediately (e.g. `DeepSeek V4.1 Flash`), so read the row back to prove the swap.

**How to apply:** never conclude the canvas is broken from a failed `.click()`; use the sequence above and prove persistence with a reload count. When a control opens but refuses to change value, stop retrying synthetic variants — switch to CDP mouse on the desktop app. Used to build the equipe-dev PPIRTV workflow — see [[equipe-dev-team-charter]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-workflow-canvas-pointer-events-622352595f43-content
