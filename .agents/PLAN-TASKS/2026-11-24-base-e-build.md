# Base atualizada e build do instalador (2026-11-24)

- Tipo: SPEC-PLAN-TASKs (simples)
- Status: EM EXECUCAO
- Owner: sessao do projeto
- Origem: pedido do dono "base e compila novamente" apos o monitoramento que mediu 212 commits upstream.

## Decisao

Rebase da `main` local sobre `origin/main` (`72f80f561`), preservando os 7 commits da casa, e novo build do instalador Windows a partir da base atualizada.

## TASKs

- T1: commitar o estado vivo pendente (`.agents/UPSTREAM.md`, `.agents/GATILHOS-VIVOS.md`) para a arvore ficar limpa.
- T2: `git rebase origin/main` e resolver conflitos preservando `AGENTS.md` da casa, `.agents/` e o fix do picker.
- T3: `bun install --frozen-lockfile` na base nova.
- T4: `bun run dist:win` com bsdtar no PATH (`/c/Windows/System32` primeiro).
- T5: conferir artefato em `dist/` (tamanho + sha256) e registrar no fechamento.

## Validacao

- `git rev-list --count origin/main..HEAD` igual a 7 (commits da casa preservados).
- `git rev-list --count HEAD..origin/main` igual a 0.
- Instalador novo em `dist/` com sha256 medido.

## Riscos

- Conflito em `AGENTS.md` e `.gitignore`: resolver mantendo as secoes da casa e o conteudo upstream.
- Build pode falhar por dependencia nova: rodar `bun install --frozen-lockfile` antes.
- Sem push: a `main` do fork so muda com pedido explicito do dono.
