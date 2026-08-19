# Changelog

All notable changes to otacli are documented here.
Work in progress and open threads are tracked in [`DEVELOPMENT.md`](DEVELOPMENT.md).

## Unreleased

### Added

- A demo GIF in the README, showing the environment check, main menu, trending list,
  fuzzy search and a series page with cover art. Recorded with `vhs` in a container.
- `tools/` — development scripts: `make_icons.py` and `demo.tape`/`Dockerfile.demo`
  regenerate the repository's assets (both verified to reproduce the committed files), and
  `find_dead_imports.py` is a static check standing in for the absent linter.
- `DEVELOPMENT.md` — project state, architecture map, release process, and the list of
  open work.

### Fixed

- Removed 13 unused imports inherited from upstream, in `src/main_module.py` and
  `src/docchi_api_connector.py`. `subprocess.DEVNULL` is still used in `main_module`, via
  the module-level `import subprocess` — it was the separate `from subprocess import
  Popen, DEVNULL` line that was dead.
- Removed an unused `storage` import left in `src/downloader.py` after the
  interface-language settings were dropped in v0.1.0.

## v0.1.0 — 2026-08-19

Forked from [doccli](https://github.com/TowarzyszFatCat/doccli) v2.40.0 (commit `eeb1aaf`).
otacli continues as an independent project under GPL-3.0. See `COPYRIGHT` for attribution.

### Removed

- **Discord Rich Presence.** The integration was bound to the doccli project's
  registered Discord application, so it could not carry over. The `rpc_enabled`
  and `rpc_status` settings are gone with it.
- **Links to doccli's community.** The "Join our Discord" menu entry and the
  Discord/donation links in the Rich Presence buttons pointed at the upstream
  project's server and its author's donation page.
- **The Polish user interface.** `src/i18n.py` now holds English strings only,
  and the language switcher is gone. The streaming sources are unchanged and
  still serve Polish subs and dubs — this affects the interface, not the catalogue.
- **The description translation step.** AniList already serves English
  descriptions, so the round trip through Google Translate was dropped, along
  with the `deep-translator` dependency.

### Changed

- **Renamed** to `otacli`: the command, the config directory
  (`~/.config/otacli`, `%APPDATA%\otacli`), the download and chapter paths, the
  watch-history source tag, and the Windows installer.
- **AniList integration now requires your own API client.** `ANILIST_CLIENT_ID`
  in `src/main_module.py` is empty by default; until it is set, the AniList
  option in Settings explains what to do instead of failing. otacli does not
  ship with anyone else's client ID.
- **Polish sources are no longer gated on the interface language.** In doccli,
  the docchi.pl source list was only fetched when the UI was set to Polish;
  dropping the Polish UI would have made those sources unreachable. Both the
  `[PL]` and `[EN]` source lists are now always fetched.
- **New icons and main-menu artwork.**
- **Version reset** to v0.1.0. The update checker points at this project's
  releases.

### Added

- **Migration from doccli.** On first run, if `~/.config/doccli` (or the Windows
  equivalent) exists, otacli copies `mylist.json`, `continue.json` and
  `history.json` across. The files are copied rather than moved, so an existing
  doccli install keeps working. `settings.json` is deliberately not copied: it
  holds an AniList token issued to doccli's API client, which otacli should not
  reuse. Watch statistics still count history entries written by doccli.

### Fixed

- `install.sh` only ever worked on Debian-family systems despite the
  documentation listing Arch packages; it now detects `pacman`, `apt-get` or
  `dnf`, and resolves its own checkout path instead of assuming the clone
  directory is named after the project.
- Removed a stray Markdown code fence in `installer.iss` that would have failed
  to compile under Inno Setup.
