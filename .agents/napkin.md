# Napkin — OpenBot (fork da casa)

## NAPKIN-DEFENDER-SUSPEXEC-HARNESS

- Sintoma: Defender mostra `Trojan:Win32/SuspExec.SE` depois de um teste que abre o app e le a janela.
- Causa: a deteccao mira a linha de comando `node.exe -e` que usa `spawn`, PowerShell e `--remote-debugging-port`; nao ha arquivo infectado.
- Faca em vez disso: rode o harness por script em arquivo dentro do repo, nunca inline em `node -e`; confira `Get-MpThreatDetection` e nao tente `Remove-MpThreat -ThreatID` (nao existe neste Windows 10 19045).

## NAPKIN-APP-UNICO-POR-PERFIL

- Sintoma: `Start-Process` do exe com `--user-data-dir` nao cria janela nova.
- Causa: o app usa instancia unica por perfil; se aquele perfil ja esta aberto, o novo processo apenas foca a janela existente.
- Faca em vez disso: feche a instancia do perfil antes de trocar de build, ou abra com outro perfil; confira o `--user-data-dir` real dos processos antes de concluir falha de launch.
