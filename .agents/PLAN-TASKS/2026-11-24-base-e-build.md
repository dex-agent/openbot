# Base atualizada e build do instalador (2026-11-24)

- Tipo: SPEC-PLAN-TASKs (simples)
- Status: CONCLUIDO
- Owner: sessao do projeto
- Origem: pedido do dono "base e compila novamente" apos o monitoramento que mediu 212 commits upstream.

## Decisao

Rebase da `main` local sobre `origin/main` (`72f80f561`), preservando os 7 commits da casa, e novo build do instalador Windows a partir da base atualizada.

## TASKs

- [x] T1: commitar o estado vivo pendente (`.agents/UPSTREAM.md`, `.agents/GATILHOS-VIVOS.md`) para a arvore ficar limpa — `a4ca95dd7`.
- [x] T2: `git rebase origin/main` e resolver conflitos preservando `AGENTS.md` da casa, `.agents/` e o fix do picker — unico conflito em `AGENTS.md`, resolvido com as duas secoes; 8 commits da casa sobre `72f80f561`.
- [x] T3: `bun install --frozen-lockfile` na base nova — 8 pacotes, exit 0.
- [x] T4: `bun run dist:win` com bsdtar no PATH (`/c/Windows/System32` primeiro) — exit 0.
- [x] T5: conferir artefato em `dist/` — `OpenBot-0.76.1-x64.exe`, 234.652.108 bytes, sha256 `3274173c53ddeb8d3bfd180261292b1a4a9fcb59ba9f54a45edcd03d39841de2`.

## Validacao

- `git rev-list --count origin/main..HEAD` igual a 7 (commits da casa preservados).
- `git rev-list --count HEAD..origin/main` igual a 0.
- Instalador novo em `dist/` com sha256 medido.

## Riscos

- Conflito em `AGENTS.md` e `.gitignore`: resolver mantendo as secoes da casa e o conteudo upstream.
- Build pode falhar por dependencia nova: rodar `bun install --frozen-lockfile` antes.
- Sem push: a `main` do fork so muda com pedido explicito do dono.
