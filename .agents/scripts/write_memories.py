import json
import os

BASE = os.path.join(".agents", "ARQUEOLOGIA", "memorias")
os.makedirs(BASE, exist_ok=True)

MEMORIES = [
    {
        "slug": "openbot-build-e-runtime",
        "scope": "project",
        "title": "OpenBot: build, testes e runtime medidos",
        "trigger": "Antes de instalar, buildar ou testar o openbot; bun ausente; duvida sobre o argv real",
        "body": (
            "O openbot e um monorepo Bun: packageManager bun@1.4.2, engines node>=24 (medido v24.19.0), "
            "lockfile bun.lock. Instalacao fiel: bun install --frozen-lockfile. Build desktop: bun run build "
            "(electron-vite build), medido exit 0 em 24,28s e out/ com 76 MB. Teste estreito: "
            "bun run test:desktop -- <arquivo> (vitest run). Tipos por projeto: bun run typecheck:node e "
            "bun run typecheck:renderer (um por vez). Lint de arquivo: biome check --write --max-diagnostics=none. "
            "Nao rodar bun run format, bun run typecheck agregado nem suite ampla local. O prepare do bun install "
            "ativa core.hooksPath=.githooks via scripts/install-git-hooks.ts."
        ),
        "tags": ["#openbot/build", "#openbot/runtime"],
    },
    {
        "slug": "openbot-rotas-e-workspaces",
        "scope": "project",
        "title": "OpenBot: workspaces, denominador e direcao de dependencia",
        "trigger": "Ao navegar o repo, decidir escopo de mudanca ou medir tamanho do projeto",
        "body": (
            "OpenBot e um monorepo unico, sem rota legada separada. Workspaces: apps/* (auth-api, mobile, "
            "mobile-updates, site-router, status, apps de mensageria), packages/* (contracts, ui, i18n, logging, "
            "telemetry, team-client, user-errors, whatsapp, brand) e remote/api. O desktop mora na raiz (src/main, "
            "src/preload, src/renderer, src/backend). Denominador da arqueologia: 7.701 fontes .ts/.tsx/.js/.mjs/.cjs "
            "fora de node_modules, dist, build, out e coverage; 1.645.650 linhas; 74,5 MB. Dependencias apontam para "
            "packages/contracts; renderer nao importa main/backend; contratos nao importam Electron/SolidJS/Cloudflare."
        ),
        "tags": ["#openbot/rotas", "#openbot/arquitetura"],
    },
    {
        "slug": "openbot-encoding",
        "scope": "project",
        "title": "OpenBot: encoding UTF-8 LF sem BOM nas tres camadas",
        "trigger": "Antes de editar arquivo do openbot; suspeita de CRLF, BOM ou mojibake",
        "body": (
            "Medicao byte-a-byte nas 7.701 fontes: zero BOM, zero CRLF, zero arquivo nao-UTF8, zero NUL; 1.994 arquivos "
            "tem bytes >=0x80 e todos decodificam como UTF-8. Camada loja: git ls-files --eol mostra 9.335 arquivos i/lf "
            "w/lf e 325 binarios; blobs de amostra batem byte-a-byte com o disco. Camada maquina: core.autocrlf=true vem "
            "do gitconfig de sistema, mas .gitattributes fixa '* text=auto eol=lf', entao nao ha contaminacao. "
            "Armadilha: 'git config core.autocrlf --show-origin' SETA a chave com o literal --show-origin; ler sempre "
            "'git config --show-origin core.autocrlf' e, se corromper, 'git config --unset core.autocrlf'."
        ),
        "tags": ["#openbot/encoding", "#openbot/tropeco"],
    },
    {
        "slug": "openbot-segredos-sanitizados",
        "scope": "project",
        "title": "OpenBot: segredos versionados sao cifrados ou fixtures",
        "trigger": "Ao revisar seguranca, .env ou varredura de segredo no openbot",
        "body": (
            "Os 5 arquivos .env versionados (apps/auth-api/.env.dev, .env.production, .env.example; remote/.env.example, "
            ".env.production) usam dotenvx: chave publica + valores 'encrypted:'. O .env.keys da raiz esta ausente e e "
            "ignorado por .gitignore. A varredura sanitizada achou 167 ocorrencias: praticamente todas sao fixtures de "
            "teste ou placeholders mascarados. Dois achados reais e nao secretos: apps/mobile/google-services.json "
            "(chave de API Firebase de cliente, publica por desenho) e uma constante de chave publica em "
            "packages/whatsapp/vendor/baileys/src/WABinary/constants.ts. Nenhum segredo de servidor em texto claro."
        ),
        "tags": ["#openbot/seguranca", "#openbot/segredos"],
    },
    {
        "slug": "openbot-grafo-hubs-e-ciclos",
        "scope": "project",
        "title": "OpenBot: hubs de import e ciclos medidos",
        "trigger": "Ao avaliar impacto de mudanca, acoplamento ou blast radius no openbot",
        "body": (
            "Grafo de imports proprio sobre 7.701 fontes: 35.702 arestas internas, 3.950 por alias '@/', 986 relativos "
            "nao resolvidos (assets CSS/imagem/JSON) e 34 ciclos com 427 nos. Hubs de fan-in: packages/contracts/src/ipc.ts "
            "(2.036), packages/i18n/src/message.ts (1.600), packages/contracts/src/runtime-values.ts (835), "
            "packages/ui/src/text.tsx (689), src/backend/effect-boundary.ts (555). Fan-out alto: "
            "src/main/application-services.ts (290), apps/auth-api/src/routeTree.gen.ts (271), src/main/team-api-server.ts (250). "
            "O CRG (2.4.0+dex.1) confirma 89.440 nos e 714.460 arestas no mesmo HEAD."
        ),
        "tags": ["#openbot/grafo", "#openbot/impacto"],
    },
    {
        "slug": "openbot-metricas-podio",
        "scope": "project",
        "title": "OpenBot: podio de God Class, Long Method e CC",
        "trigger": "Ao planejar refatoracao ou revisar hotspots do openbot",
        "body": (
            "God Class (CRG, producao): AgentService 233 metodos e 6.400 linhas em src/backend/agent-service.ts; "
            "MailboxStore 103/3.378; OpenBotDatabase 88/586; ProviderRuntime 70/3.957; BrowserHost 63/4.000. "
            "Long Method: WebWorkspaceFrame 3.454 linhas; createMockOpenBot 3.418; createApplicationServices 3.303; "
            "WorkflowCanvas 3.237; createConversationViewScope 2.476. CC (medidor da casa, fontes de producao): "
            "37.815 funcoes, media 4,49, maximo 774 em packages/ui/src/features/workflows/WorkflowCanvas.tsx; "
            "2.783 funcoes acima de 10 e 232 acima de 50. O medidor inclui out/ por default e infla o ranking; "
            "filtrar fontes antes de publicar podio."
        ),
        "tags": ["#openbot/metricas", "#openbot/hotspot"],
    },
    {
        "slug": "openbot-typecheck-node-vermelho",
        "scope": "project",
        "title": "OpenBot: typecheck:node vermelho por mock sem toolCanUseTab",
        "trigger": "Ao rodar typecheck:node no openbot ou ao tocar scripts/mistral-stuck-turn-e2e.ts",
        "body": (
            "No HEAD 140d75f, bun run typecheck:node sai 1 com TS2741 em scripts/mistral-stuck-turn-e2e.ts:110: o mock "
            "AgentBrowserHost nao tem toolCanUseTab, exigido por src/backend/agent/attention-registry.ts:441. Os outros "
            "19 scripts e2e ja tem 'toolCanUseTab: () => false'. Correcao minima: acrescentar essa linha ao mock. "
            "O build, typecheck:renderer e o teste estreito estao verdes; a arqueologia registra rota vermelha com "
            "owner e quando em .agents/ESTACIONAMENTO.md."
        ),
        "tags": ["#openbot/tropeco", "#openbot/tipos"],
    },
    {
        "slug": "openbot-deps-diretrizes-ia",
        "scope": "project",
        "title": "OpenBot: quatro dependencias diretas trazem AGENTS/CLAUDE",
        "trigger": "Ao mexer em effect, elysia, react-native-keyboard-controller ou react-native-webrtc",
        "body": (
            "Quatro dependencias diretas do openbot embarcam diretrizes de IA: effect (AGENTS.md e CLAUDE.md: preferir "
            "Effect.gen/Effect.fn, sem wrapper de Promise), elysia (regras de contribuicao do repo), "
            "react-native-keyboard-controller (regras de issue e reproducao) e react-native-webrtc (visao do projeto e "
            "comandos nativos). Ponteiro em .agents/ARQUEOLOGIA/DEPENDENCIES.md; nunca copiar as skills para o registry. "
            "Transitivas com o mesmo tipo de arquivo: bun-types, cytoscape, expo-modules-macros, thread-stream. "
            "Revalidar no upgrade com a varredura --hidden --no-ignore."
        ),
        "tags": ["#openbot/dependencias", "#openbot/diretrizes-ia"],
    },
    {
        "slug": "openbot-gerados-e-ofuscacao",
        "scope": "project",
        "title": "OpenBot: superficie gerada e ausencia de ofuscacao",
        "trigger": "Ao medir tamanho, revisar bundle ou procurar codigo morto/ofuscado no openbot",
        "body": (
            "Superficie gerada: packages/whatsapp/vendor/baileys/WAProto/index.js tem 97.691 linhas; "
            "packages/i18n/src/messages tem 1.620 arquivos .ts em 15 locales; plugin-catalog.generated.ts (auth-api e "
            "mobile) e routeTree.gen.ts sao gerados. Nao ha .min.js versionado, nao ha eval/new Function reais (as 45 "
            "ocorrencias sao metodo .eval de harness/shader) e atob aparece 10 vezes em codigo legitimo de base64. "
            "O vendor Baileys responde por 174 arquivos e 161.712 linhas do total."
        ),
        "tags": ["#openbot/gerados", "#openbot/ofuscacao"],
    },
    {
        "slug": "openbot-crg-e-hooks",
        "scope": "project",
        "title": "OpenBot: CRG local e hooks do projeto",
        "trigger": "Ao consultar grafo estrutural, instalar CRG ou commitar no openbot",
        "body": (
            "O grafo estrutural vive em .agents/CODE-REVIEW-GRAPH (code-review-graph 2.4.0+dex.1, schema v15, 749 MB, "
            "ignorado pelo .gitignore interno). Build: code-review-graph build --repo . --data-dir .agents/CODE-REVIEW-GRAPH; "
            "o primeiro build encerrou antes do pos-processamento, entao rodar postprocess. O bun install ativa "
            "core.hooksPath=.githooks via prepare; o pre-commit do projeto roda check:staged, check:ui e staged-typecheck. "
            "Hooks do CRG em .git/hooks ficam inertes com esse hooksPath; os hooks de plataforma (Codex/Claude) atualizam o grafo. "
            "Indice e limites em .agents/CODE-REVIEW-GRAPH-INDEX.md."
        ),
        "tags": ["#openbot/ferramentas", "#openbot/crg"],
    },
]

for memory in MEMORIES:
    path = os.path.join(BASE, memory["slug"] + ".json")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(memory, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
print(len(MEMORIES), "payloads written to", BASE)
