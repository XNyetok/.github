<!-- The banner and the buttons are SVGs in profile/assets, each with a light and a dark variant. To change their
     text or colors, edit scripts/build-profile-assets.py and run: python3 scripts/build-profile-assets.py -->

<div><a href="https://nyetok.id"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"><img src="assets/banner-light.svg" width="100%" alt="Nyetok: stocking up on small apps that are actually useful. Light, tidy and private apps for your Mac, free and open source, made in Indonesia. The same recipe in every app: native Swift, MIT license, free, no account, no telemetry. nyetok.id"></picture></a></div>

<div align="center"><a href="https://havus.web.id"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-havus-dark.svg"><img src="assets/btn-havus-light.svg" align="top" alt="Try Havus at havus.web.id"></picture></a> <a href="https://korupsi.web.id"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-korupsi-dark.svg"><img src="assets/btn-korupsi-light.svg" align="top" alt="Play Korupsi at korupsi.web.id"></picture></a> <a href="https://saweria.co/nyetok"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-support-dark.svg"><img src="assets/btn-support-light.svg" align="top" alt="Support Nyetok on Saweria"></picture></a></div>

Nyetok is the home of [Debi Kurnia](https://github.com/debikurnia)'s small open-source software: native apps for
macOS, a browser game, and a tool for coding agents. In Indonesian, *nyetok* means stocking up.

## Mac apps

Each one is written in Swift on Apple's own frameworks, with no Electron, no account and no telemetry.

| App | What it does | Requires | Download |
| --- | --- | --- | --- |
| [Havus](https://github.com/XNyetok/Havus)<br><sub>[havus.web.id](https://havus.web.id)</sub> | A Mac cleaner that minds its own business: caches, logs and developer junk, apps with their leftovers, large files you rarely open, a map of what fills your disk, and programs that start on their own. Everything goes to the Trash first | macOS&nbsp;14+ | [Latest&nbsp;release](https://github.com/XNyetok/Havus/releases/latest) |
| [XSpace](https://github.com/XNyetok/XSpace) | Several isolated browser profiles in one window, each with its own cookies and logins | macOS&nbsp;26+ | [Latest&nbsp;release](https://github.com/XNyetok/XSpace/releases/latest) |
| [Jambul](https://github.com/XNyetok/Jambul) | A Dynamic Island for the MacBook notch, with a timer, Keep Awake, battery peeks and your AI usage limits | macOS&nbsp;14+ | [Latest&nbsp;release](https://github.com/XNyetok/Jambul/releases/latest) |

These releases aren't notarized by Apple yet, so macOS blocks each app the first time it opens. Open the app once,
then go to System Settings → Privacy & Security and choose **Open Anyway**. Each app's README has the details.

Notarizing takes a paid Apple Developer Program membership (US$99 a year). If an app helps you, you can chip in on
[Saweria](https://saweria.co/nyetok). It's voluntary: the apps are free to use either way.

## Also in stock

| Project | What it is | Status | Get it |
| --- | --- | --- | --- |
| [Korupsi](https://github.com/XNyetok/korupsi)<br><sub>[korupsi.web.id](https://korupsi.web.id)</sub> | A pixel-art browser platformer about climbing a bureaucracy, one office at a time, with the audit team already in the lobby. About 28&nbsp;KB gzipped, in TypeScript and Canvas&nbsp;2D; the game's copy is Indonesian | The first floor is playable | [Play&nbsp;it](https://korupsi.web.id) |
| [Namvan](https://github.com/XNyetok/Namvan) | A lightweight runtime and workspace for terminal coding agents. Run Claude Code, Codex or any terminal program, close the window and they keep running, and see at a glance which agent is working, done or waiting for you | Pre-alpha, for macOS on Apple silicon | [Build&nbsp;from&nbsp;source](https://github.com/XNyetok/Namvan#build) |

Korupsi counts visits and runs anonymously, with no cookies and no identifiers; its
[telemetry notes](https://github.com/XNyetok/korupsi/blob/main/docs/telemetry.md) list every field. Namvan has no
telemetry.

Everything here is MIT-licensed, except Namvan, which is Apache-2.0. Bug reports, ideas and pull requests are
welcome; a repository's CONTRIBUTING.md, where it has one, explains how.

<sub>**Bahasa Indonesia:** Nyetok bikin aplikasi kecil yang ringan, rapi, dan nggak kepo. Semuanya gratis dan open source, tanpa akun dan tanpa telemetri. Kenalan lebih jauh di [nyetok.id](https://nyetok.id).</sub>
