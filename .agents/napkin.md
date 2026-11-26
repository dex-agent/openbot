# Napkin — OpenBot (fork da casa)

## NAPKIN-DEFENDER-SUSPEXEC-HARNESS

- Sintoma: Defender mostra `Trojan:Win32/SuspExec.SE` depois de um teste que abre o app e le a janela.
- Causa: a deteccao mira a linha de comando `node.exe -e` que usa `spawn`, PowerShell e `--remote-debugging-port`; nao ha arquivo infectado.
- Faca em vez disso: rode o harness por script em arquivo dentro do repo, nunca inline em `node -e`; confira `Get-MpThreatDetection` e nao tente `Remove-MpThreat -ThreatID` (nao existe neste Windows 10 19045).

## NAPKIN-APP-UNICO-POR-PERFIL

- Sintoma: `Start-Process` do exe com `--user-data-dir` nao cria janela nova.
- Causa: o app usa instancia unica por perfil; se aquele perfil ja esta aberto, o novo processo apenas foca a janela existente.
- Faca em vez disso: feche a instancia do perfil antes de trocar de build, ou abra com outro perfil; confira o `--user-data-dir` real dos processos antes de concluir falha de launch.

## NAPKIN-ATALHO-MENU-INICIAR-DIST

- Sintoma: o atalho OpenBot do Menu Iniciar passa a apontar para `C:\CodexProjetos\openbot\dist\win-unpacked\OpenBot.exe`, sem `--user-data-dir`; os atalhos da area de trabalho continuam no app instalado.
- Causa: o ciclo de teste do build nao fotografa/restaura os atalhos; o build fora do local instalado deixa o Menu Iniciar apontando para o caminho efemero (medido em 2026-11-26; alvo reescrito em 25/11 12:52, antes do run de 0.79).
- Faca em vez disso: antes do teste, ler alvo/args dos atalhos OpenBot do Desktop e do Menu Iniciar; depois, restaurar e conferir. Atalho estavel aponta para o app instalado; se o banco migrou acima dele, instalar o build novo primeiro.
