---
implementation_version: v2
layer: L2
slug: equipe-dev-team-charter-e550b727bc59
tags:
  - "#auto-memory/project"
---

# equipe-dev-team-charter

Espelho da auto-memory do host ZCode (arquivo equipe-dev-team-charter.md, tipo project).

The dev-team charter under C:\CodexProjetos\equipe-dev maps 7 OpenBot

The owner's programming team lives in `C:\CodexProjetos\equipe-dev`, one project per subfolder. It has 7 roles: Scope Writer (Marketplace), Tech Lead (custom agent, created in Portuguese on 2026-11-20), Change Reviewer, QA Tester, Security Reviewer, Bug Fixer and Launch Coordinator. Channels are `#pedidos`, `#dev`, `#revisao`, `#qa`, `#release`; WIP is 1 per agent and the Tech Lead is the only integrator.

Each ficha in `agents/` names its PPIRTV phase and house skills. Phase owners: P🧠 `$reuniao` (+ `$chato`, `$questionador`, `$critico-cetico`, `$entrevista-me`, `$burrinha`), P🗂️ `$sprinter` + `$spt-revisor` + `$dex-ppirtv-validate-spt`, I🛠️ `$mapeador-implementacao` + `$karpathy-guidelines`, R🔎 `$revisor-codigo` + `$guarda-plaquinhas`, T🧪 `$tio-testador` + `$checklist-visual`, V✅ `$validador-pronto` + `$dex-fechamento-projeto-atualizado`. Orchestration is `$ancora-fluxo` + `$auto-fluxo-flow` with `$chato` as commander.

**State measured 2026-11-20 (done):** all 6 Marketplace agents installed on host `Servidor de newstartmaximus`; `Tech Lead` custom agent created; workflow **`PPIRTV - Time de Desenvolvimento`** built in the web client canvas — manual trigger → Scope Writer → Gate P (approval) → Tech Lead → Change Reviewer → Gate R (approval) → QA Tester → Gate T (approval) → Launch Coordinator → Output, i.e. 10 nodes / 9 edges; persistence proven by reload (`[data-node-id]`=10, `[data-edge-id]`=9). Security Reviewer and Bug Fixer are conditional side-lenses, not linear nodes. Receipt: `.agents/receipts/2026-11-20-setup-workflow-ppirtv.json`; PT descriptions in `AGENTES-PT.md` (owner asked for Portuguese, which overrides the repo's ASD-STE100 English rule for that file). The Tech Lead model was read back on 2026-11-20 as `agnes/agnes-3.0-flash · Alto` (an earlier "Mistral: Codestral 2508" note was wrong), while Marketplace agents use DeepSeek V4 Pro — not standardized.

**Skills — read the catalog, do not assume:** `marketplace/production-catalog/catalog.json` lists `skills[]` per agent, and the six Marketplace agents already ship theirs — Scope Writer: project-plan + decision-quality-check; Change Reviewer: change-review + secure-code-guidance; QA Tester: acceptance-check + bug-triage; Security Reviewer: secure-code-guidance + repository-threat-model; Bug Fixer: bug-triage + change-review; Launch Coordinator: launch-notes + project-plan. `pstack` is NOT a skill: it is a **pack** (`packs[0]`, source cursor, "Installs all 52 pstack skills", category coding) — installing it into the Tech Lead produced 53 `pstack-*` dirs under `Agents/<agent>/.agents/skills` and the UI shows "pstack installed on 1 agent". So the only skill install the charter needed was pstack on the Tech Lead.

**Channels — done 2026-11-20:** `pedidos` (Tech Lead + Scope Writer), `dev` (Tech Lead only), `revisao` (+ Change Reviewer), `qa` (+ QA Tester), `release` (+ Launch Coordinator). Channel creation dialog: name input `input[placeholder="Ex: Project Falcon"]`, members are `input[id^="channel-member-<agentId>"]` checkboxes (all on by default → turn the unwanted ones off), create button labelled "Create". Channel ids map from the `id` suffix; the map was proven by opening `#qa` and reading the members panel (channel lead + QA Tester).

**Permissions — done 2026-11-20, measured 7/7:** Tech Lead and Bug Fixer on `Acesso completo` (`Full access`); Scope Writer, Change Reviewer, QA Tester, Security Reviewer and Launch Coordinator on `Perguntar antes` (`Ask first`). Receipt `.agents/receipts/2026-11-20-permissions.json`; driver script `.agents/scripts/set-agent-permissions.mjs` (CDP mouse, re-runnable, reads each value back). Desktop UI labels are Portuguese.

**Windows limit (platform, not a bug):** the third level `Espaço de trabalho` (`Workspace only`) reverts by itself and the panel shows in red "Para este provedor, o acesso Somente o espaço de trabalho existe apenas no macOS" — sources `packages/i18n/src/messages/pt/error/agent.ts:167` and `scripts/pi-workspace-only-smoke.ts:89` ("Workspace only runs only on macOS."). With `Full access`/`Ask first` the Folders screen says "Estas pastas valem em Espaço de trabalho", so per-folder sandboxing is **inert on Windows**: the working directory can only be a prompt instruction, never an OS sandbox.

**Measured agent ids on this host:** `951c3d88` Tech Lead (only custom agent), `846bde5e` Scope Writer, `37f0df9a` Change Reviewer, `99ea1d0f` QA Tester, `631ca90a` Security Reviewer, `27b17711` Bug Fixer, `14d10f62` Launch Coordinator. Each agent's workspace is `C:\Users\jumper\OpenBot\Agents\<agentId>`; shared folder is `C:\Users\jumper\OpenBot\Shared`.

**Owner decisions 2026-11-20 (after the open list was shown):** the real end-to-end run is **authorized** ("continue", full pipeline GO, pipeline runs to the verdict — a created trail or a validated SPT is not "done"); and the model decision is made — **standardize every agent on the `deepseek-v4-flash` family**, since `agnes-3.0-flash` was only a test the owner ran to see whether that model worked. In this UI the provider tab is `DeepSeek` and the option reads **"DeepSeek V4.1 Flash"** (no static `deepseek-v4-flash` id exists in `packages/contracts/src/agent-providers.ts`, which lists only `deepseek-v4-pro`; the flash entry comes from the live provider catalog). Model driver: `.agents/scripts/set-agent-models.mjs` (CDP mouse, reads each value back, receipt `2026-11-20-models.json`).

**Open on 2026-11-20:** (1) the real end-to-end run — authorized, not yet executed; (2) model standardization to the DeepSeek flash family — decided, pending execution; (3) working directory as a prompt instruction (per-folder sandbox is inert on Windows); (4) house closeout `$dex-fechamento-projeto-atualizado` + V2 memory validation, after (1). Consolidated receipt exists: `.agents/receipts/2026-11-20-setup-completo.json` (7 agents, skills, 5 channels, 7/7 permissions, platform limit, honest not-done list). Closeout style the owner expects: a short "what is missing" table with cost per item, then one-word options (`roda` / `padroniza` / `fecha`).

**Why:** the first charter was generic market advice; the owner pushed back asking whether it followed the Dex ecosystem and PPIRTV. A generic org chart can never satisfy that.

**Trail maintenance (measures that cost time on 2026-11-20):** the setup trail now has 10 tasks (A-01..A-10) covering agents, skills, channels, access, working-directory instruction, model standardization, the real run, the receipt and the verdict, and both gates are green: `preflight.mjs` → `achados=0` and the official `spt_validate` → `valid=true`, `contract_version=3`, `execution_eligible=true`, `next_step=goal_start`, `missing=[]`, `contract_errors=[]`. Two trap classes hit while editing it: (a) **writing the file with Python rewrote it as CRLF** and preflight S07 failed instantly — normalize with `p.read_bytes().replace(b"\r\n", b"\n")` before revalidating; (b) **evidence expectations must use the UI label, not the catalog slug** — the panel shows `Acceptance Check`, `Change Review`, `Secure Code Guidance`, `Bug Triage` and `DeepSeek`, so expecting `acceptance-check`/`change-review`/`secure-code-guidance`/`bug-triage`/`deepseek` would make the proof impossible to satisfy; also avoid the `#` prefix in expectations (`revisao`, not `#revisao`). There is no PPIRTV MCP tool in this session — the official validator runs through the stdio harness `.agents/scripts/mcp-call.mjs <tool> @args.json` (spawns `C:/CodexProjetos/dex-PPIRTV/dist/index.js`, JSON-RPC `initialize` + `tools/call`), and the args file is needed because inline JSON with Windows back-slash paths is rejected by the parser.

**How to apply:** reuse Marketplace agents before inventing one; keep `DEX-CONTRACT.md` as the binding rule; a fresh project starts with `$dex-bootstrap`/`$projeto-estrutura-ia`. Setup trail: `.agents/PLAN-TASKS/2026-11-20-configurar-time-7-agentes.md` (preflight `achados=0`). The web client needs a published host first (desktop *Server Settings → Publish this server*) — see [[openbot-remote-access-topology]]. Automating the canvas requires real pointer events — see [[openbot-workflow-canvas-pointer-events]]. See [[ppirtv-house-workflow-map]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^equipe-dev-team-charter-e550b727bc59-content
