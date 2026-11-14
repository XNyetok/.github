<!-- The banner and the buttons are SVGs in profile/assets, each with a light and a dark variant. To change their
     text or colors, edit scripts/build-profile-assets.py and run: python3 scripts/build-profile-assets.py -->

<div><a href="https://nyetok.id"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"><img src="assets/banner-light.svg" width="100%" alt="Nyetok: stocking up on small apps that are actually useful. Mac apps and browser games, free and open source, made in Indonesia. The same recipe in every project: open source under the MIT license, free, no account, small and light. nyetok.id"></picture></a></div>

<div align="center"><a href="https://havus.web.id"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-havus-dark.svg"><img src="assets/btn-havus-light.svg" align="top" alt="Try Havus at havus.web.id"></picture></a> <a href="https://korupsi.web.id"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-korupsi-dark.svg"><img src="assets/btn-korupsi-light.svg" align="top" alt="Play Korupsi at korupsi.web.id"></picture></a> <a href="https://kerinciku.web.id"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-kerinci-dark.svg"><img src="assets/btn-kerinci-light.svg" align="top" alt="Play Jelajah Kerinci at kerinciku.web.id"></picture></a> <a href="https://saweria.co/nyetok"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-support-dark.svg"><img src="assets/btn-support-light.svg" align="top" alt="Support Nyetok on Saweria"></picture></a></div>

Nyetok is the home of [Debi Kurnia](https://github.com/debikurnia)'s small open-source software: native apps for
macOS and two browser games. In Indonesian, *nyetok* means stocking up.

## Mac apps

Each one is written in Swift on Apple's own frameworks, with no Electron, no account and no telemetry.

| App | What it does | Requires | Download |
| --- | --- | --- | --- |
| [Havus](https://github.com/XNyetok/Havus)<br><sub>[havus.web.id](https://havus.web.id)</sub> | A Mac cleaner that minds its own business: caches, logs and developer junk, apps with their leftovers, large files you rarely open, a map of what fills your disk, and programs that start on their own. Everything goes to the Trash first | macOS&nbsp;14+ | [Latest&nbsp;release](https://github.com/XNyetok/Havus/releases/latest) |
| [Jambul](https://github.com/XNyetok/Jambul) | A Dynamic Island for the MacBook notch, with a timer, Keep Awake, battery peeks, your Claude, Antigravity and Codex usage limits, and which Claude Code sessions are working, waiting for you or done, all on one Home tab | macOS&nbsp;27+ | [Latest&nbsp;release](https://github.com/XNyetok/Jambul/releases/latest) |

These releases aren't notarized by Apple yet, so macOS blocks each app the first time it opens. Open the app once,
then go to System Settings → Privacy & Security and choose **Open Anyway**. Each app's README has the details.

Notarizing takes a paid Apple Developer Program membership (US$99 a year). If an app helps you, you can chip in on
[Saweria](https://saweria.co/nyetok). It's voluntary: the apps are free to use either way.

## Browser games

| Game | What it is | Status | Get it |
| --- | --- | --- | --- |
| [Korupsi](https://github.com/XNyetok/korupsi)<br><sub>[korupsi.web.id](https://korupsi.web.id)</sub> | A pixel-art browser platformer about climbing a bureaucracy, one office at a time, with the audit team already in the lobby. Finish a run to earn one of ten titles and share it as an official decree. About 28&nbsp;KB gzipped, in TypeScript and Canvas&nbsp;2D; the game's copy is Indonesian | The first floor is playable | [Play&nbsp;it](https://korupsi.web.id) |
| [Jelajah Kerinci](https://github.com/XNyetok/Kerinciku)<br><sub>[kerinciku.web.id](https://kerinciku.web.id)</sub> | A browser game for young children about the nature and culture of Kerinci, Sumatra. Explore the map, play a short mini-game at each place, and collect stamps that each open a fact and a word in the Kerinci language. Made for Android phones held upright, about 150&nbsp;KB, and it plays offline after one visit | Five places are playable; the summit of Mount Kerinci opens last | [Play&nbsp;it](https://kerinciku.web.id) |

The two games count visits and plays anonymously, with no cookies, no accounts and no identifiers, and Do Not Track
turns the counting off. Their telemetry notes list every field:
[Korupsi](https://github.com/XNyetok/korupsi/blob/main/docs/telemetry.md) and
[Jelajah Kerinci](https://github.com/XNyetok/Kerinciku/blob/main/docs/telemetry.md).

Everything here is MIT-licensed. Bug reports, ideas and pull requests are welcome; each repository's
CONTRIBUTING.md explains how.

<sub>**Bahasa Indonesia:** Nyetok bikin aplikasi kecil yang ringan, rapi, dan nggak kepo, dari aplikasi Mac sampai game browser. Semuanya gratis, open source, dan tanpa akun. Kenalan lebih jauh di [nyetok.id](https://nyetok.id).</sub>
