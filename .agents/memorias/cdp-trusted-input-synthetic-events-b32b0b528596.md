---
implementation_version: v2
layer: L2
slug: cdp-trusted-input-synthetic-events-b32b0b528596
tags:
  - "#auto-memory/reference"
---

# cdp-trusted-input-synthetic-events

Espelho da auto-memory do host ZCode (arquivo cdp-trusted-input-synthetic-events.md, tipo reference).

Page-injected events cannot satisfy controls that need trusted

When a web control opens but refuses to change value, the discriminator is the CDP `Input` domain, not a cleverer synthetic event (measured 2026-11-20, OpenBot agent-settings select).

Documented in the house CDP mentor (`temas/cdp/mentor-documental`, fulltext SHA-256 verified against `fulltext-manifest.json`):

- `Input.dispatchMouseEvent`: `type` ∈ `mousePressed|mouseReleased|mouseMoved|mouseWheel`; `x/y` in CSS px of the main frame viewport; `button` (default `none`); `buttons` bitfield `Left=1, Right=2, Middle=4`; `clickCount` (default **0**); `pointerType` ∈ `mouse|pen`; `modifiers` `Alt=1, Ctrl=2, Meta=4, Shift=8`.
- `Input.dispatchKeyEvent`: `keyDown|keyUp|rawKeyDown|char`; `text` is "not needed for keyUp and rawKeyDown"; plus `windowsVirtualKeyCode`, `nativeVirtualKeyCode`, `code`, `key`, `location`, `commands`.
- `Input.insertText` inserts text that "doesn't come from a key press" (e.g. IME); `DOM.focus` focuses a node; `Input.setInterceptDrags` + `Input.dispatchDragEvent` (`dragEnter|dragOver|drop|dragCancel`) drive drag-and-drop; `Page.bringToFront` activates the tab; `Page.captureScreenshot` for evidence.
- `Runtime.evaluate { userGesture: true }` is only a flag — "whether execution should be treated as initiated by user in the UI"; it does not create input.
- **Absent from the corpus:** the word `isTrusted` (0 hits). The sentence "only CDP input is trusted" is an inference corroborated live, not a documented claim — say so when citing.

Tooling route (house): `$chrome-compartilhado-cdp` owns CDP work. Its probes are `scripts/cdp_probe.js` / `cdp_probe.ps1` (not `cdp-probe.mjs`), with actions `click`, `mouse-click`, `type`, `press`, `insert-text`, `wait-selector`, `screenshot`; open/reuse with `scripts/open-verified.ps1 -Url <https url>`.

**Gotcha:** the shared Chrome profile (`~/.codex-browser-profiles/codex-shared-chrome`, port 9222) is **not signed in** to `openbot.run` — it shows the login screen, and copying cookies is against the skill. For a logged-in surface, drive the Electron desktop app over CDP instead (`connectOverCDP("http://127.0.0.1:9333")`, page `openbot-app://app/index.html`), which is authenticated and is the host anyway. A Playwright `screenshot` on that page can time out on font loading; read panel text from the DOM instead.

Complementary source — the house **OpenBot** mentor (`temas/openbot/mentor-documental`, fulltext 90.1 MB, SHA-256 `fe0d97f3…`; custody `source/original` absent on this machine, so results were cross-checked against the local repo at `C:\CodexProjetos\openbot`): the agent settings **Instructions page is the agent's `AGENTS.md`** ("shows the agent's `AGENTS.md` file as formatted"; owners/admins edit it on the server, and a second Save replaces the agent's version when the agent edits meanwhile) — that is where a working directory is declared, because the docs themselves say "Say in an agent's instructions where its work belongs". Also documented: one access picker with `Workspace only | Ask first | Full access`, the Model page warning "The Model page of a Workspace only agent now tells you when the chosen provider does not work with Workspace only on the server", the Approval step rule ("connect the step that shares the result after Approval so it runs only after you approve"), `POST /v1/workflows/decide` + `/v1/workflows/save-graph`, and `POST /v1/agents/:id/settings` `{provider, model, reasoningEffort, providerAccountId}` as the API route for a model swap (needs Local scripts on the host).

**Why:** the owner called out that the house already had a stronger browser tool while a synthetic-event dead end was being explored; later the owner asked for the same interrogation of the OpenBot mentor whenever a UI capability is in doubt.

**How to apply:** before designing any browser interaction recipe, read `$chrome-compartilhado-cdp` and ask whether in-page or CDP input is required. See [[openbot-workflow-canvas-pointer-events]] and [[raw-log-inquiry-before-inherited-conclusion]].

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^cdp-trusted-input-synthetic-events-b32b0b528596-content
