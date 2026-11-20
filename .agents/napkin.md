# napkin — openbot (runbook tatico)

## Tropecos pagos neste projeto

- `GIT-CONFIG-FLAG-ORDEM`: `git config core.autocrlf --show-origin` SETA o valor
  literal `--show-origin` na chave. Ler sempre
  `git config --show-origin core.autocrlf` e, se a chave foi corrompida,
  `git config --unset core.autocrlf`.
- `BUN-AUSENTE`: a maquina nao tinha `bun`; o projeto usa `bun@1.4.2`.
  Instalado via npm global. Se faltar de novo: `npm install -g bun@1.4.2`.
- `RG-FILES-BACKSLASH`: `rg --files` no Windows emite `\`; inventario usa
  `find -print0` com dedup por path relativo.
- `GATE-TEXTUAL`: suites do repo podem sair 0 com FAIL textual; ler o resumo,
  nao so o exit code.
- `PIPE-EXIT`: medir exit code sem pipe, redirecionando para arquivo.
- `MSYS-PATH-CONV-RG`: no Git Bash, padrao de busca que COMECA com `@/` e
  convertido pelo MSYS antes de chegar ao `rg.exe`; a busca volta 0 sem erro.
  Workaround: `MSYS_NO_PATHCONV=1 rg ...` ou prefixar o padrao com outro
  literal (`rg -F 'from "@/features'`). Vale para qualquer argumento que
  pareca path iniciado por `@/`.

## Rotas

- Build desktop: `bun run build` (`electron-vite build`).
- Testes desktop: `bun run test:desktop -- <path>` (um arquivo).
- Testes por mudanca: `bun run test:changed`.
- Tipos: `bun run typecheck:node`, `bun run typecheck:renderer`,
  `bun run typecheck:api`.
- Lint de arquivo: `biome check --write --max-diagnostics=none <paths>`.
- Nao usar `bun run format` nem `bun run typecheck` agregado.
