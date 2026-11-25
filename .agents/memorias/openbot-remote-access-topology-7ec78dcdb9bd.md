---
implementation_version: v2
layer: L2
slug: openbot-remote-access-topology-7ec78dcdb9bd
tags:
  - "#auto-memory/project"
---

# openbot-remote-access-topology

Espelho da auto-memory do host ZCode (arquivo openbot-remote-access-topology.md, tipo project).

OpenBot remote access splits into account/signaling (Cloudflare + Signal)

Remote access has three layers. Cloudflare (account Worker, D1/R2) carries only account and configuration requests. Signal (`remote/api`) relays SDP/ICE and issues tickets; it has no database and keeps no content. Chats, files, commands and video travel over WebRTC, direct or through a TURN relay (`remote/README.md`: "Cloudflare is never on the data path"). The old Team Tunnel endpoint answers 426, so a Cloudflare tunnel is not the remote route.

A **Windows desktop can be the remote host**: *Add server → New server on this computer → Server Settings → "Publish this server"* calls `host.start()` and registers for WebRTC. Linux is only required for the headless server (`server-mode.ts` returns null unless `platform === "linux"`) and for self-hosted Signal/TURN, which need a public IPv4 and UDP 3478, 5349 and 16384–65535. The self-hosted route (`docs/self-hosting.md`) also needs a Linux Docker host; the owner has a public IPv4 but refuses Docker/WSL2.

`bun run dev` runs against a local API (`127.0.0.1:3100`), so it cannot serve a remote client. Run the production build with `OPENBOT_AUTH_API_URL=https://api.openbot.run ./node_modules/electron/dist/electron.exe .`, or install the NSIS package from `bun run dist:win`.

**Why:** the owner wants the agent panel on his own machine without his data passing through OpenBot's servers, and believed that required Linux.

**How to apply:** explain that content already stays off OpenBot's servers on the official route; reserve the Linux/Docker story for full self-hosting of the account service. See [[openbot-checks-and-toolchain]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^openbot-remote-access-topology-7ec78dcdb9bd-content
