---
implementation_version: v2
layer: L2
slug: celular-nao-conecta-quando-a-rota-remota-esta-em-re-b429fa65589c
tags:
  - "#openbot/conexao-remota"
---

# Celular nao conecta quando a rota remota esta em Rede Privada

No OpenBot, a preferencia de rota remota em Rede Privada (Tailscale ou o mesmo Wi-Fi) faz o host anunciar iceServers vazio e filtrar candidatos para a rede local. Um celular em dados moveis falha com webRTC/ice/failed mesmo com o host aberto e o signal conectado. Evidencia medida em 2026-11-24: o perfil OpenBot Dev tinha route private em openbot-remote-network-route-v1.json e o celular nao conectava; o codigo team-webrtc.ts usa iceServers vazio quando privateNetwork e verdadeiro. Cura: Configuracoes, Como os dispositivos se conectam, escolher Pelo OpenBot; a troca aplica na hora. Conferir o host por conexao TCP com signal-us.openbot.run e pelo main.log sem erro de signal. A rota privada so serve para dispositivos na mesma tailnet ou Wi-Fi.

#openbot/conexao-remota

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^celular-nao-conecta-quando-a-rota-remota-esta-em-re-b429fa65589c-content
