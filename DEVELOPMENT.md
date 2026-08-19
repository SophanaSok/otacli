# Development notes

Working notes for otacli, written so development can be picked up after a gap without
re-deriving context. User-facing history lives in [`CHANGELOG.md`](CHANGELOG.md);
attribution and licensing in [`COPYRIGHT`](COPYRIGHT).

## Where the project stands

As of **2026-08-19**, v0.1.1:

- Forked from [doccli](https://github.com/TowarzyszFatCat/doccli) v2.40.0 (commit `eeb1aaf`).
- **Detached from the GitHub fork network** — `otacli` is a standalone repository, not a
  fork. This is permanent and cannot be undone.
- Upstream was notified as a courtesy in
  [TowarzyszFatCat/doccli#31](https://github.com/TowarzyszFatCat/doccli/issues/31).
- v0.1.0 and v0.1.1 are tagged and released. No `.exe` asset is attached to either.
- Nothing from upstream's identity remains in the code: no Discord application, no AniList
  client ID, no links to their community or donation page, and new icons and artwork.

## Running from source

```bash
python3 -m venv .venv
.venv/bin/pip install requests inquirerpy termcolor pillow rich curl-cffi
.venv/bin/python run.py
```

System dependencies: `mpv`, `yt-dlp`, `chafa`, optionally `megatools` for mega.nz sources.
Config and data live in `~/.config/otacli/` (`%APPDATA%\otacli` on Windows), which is
separate from the installed copy at `~/.otacli_src`, so running from a checkout shares
state with an installed copy. Point `HOME` somewhere disposable to test with a clean slate.

There is no test suite. The code is exercised by running it.

## Architecture

Entry point is `run.py`: it checks system dependencies, checks GitHub for a newer release,
then hands control to `m_welcome()` and never returns — the whole UI is **mutually
recursive menu functions**, not a loop. Menus call each other (and themselves) directly, so
the call stack grows as you navigate. That is upstream's design; it works, but it is why
there is no central state machine to hook into.

| Module | Responsibility |
|---|---|
| `run.py` | Dependency checks, update check, startup |
| `src/main_module.py` | Every menu screen and the navigation between them (~1100 lines) |
| `src/docchi_api_connector.py` | Source lookup: docchi.pl (`[PL]`) and anidb.app (`[EN]`) |
| `src/anilist_connector.py` | AniList GraphQL: metadata, progress sync, list sync, stats |
| `src/player.py` | Launching mpv, chapter files, recording watch history |
| `src/downloader.py` | Season and episode downloads |
| `src/local_lib.py` | The offline library built from downloaded files |
| `src/storage.py` | Config, list, history and resume state on disk; migrations |
| `src/stats.py` | The statistics screen and rank calculation |
| `src/cache.py` | In-memory caches for the series and trending lists |
| `src/ui_utils.py` | Terminal helpers: clear, centering, the menu wrapper |
| `src/menus_decor.py` | ASCII banners |
| `src/i18n.py` | UI strings, English only |

### Things that will bite you

- **`open_menu` compares by value, not index.** Menu handlers are written as
  `if ans == choices[0] … elif ans == choices[1]`, so inserting or removing a menu entry
  means renumbering every branch below it. Getting this wrong silently routes a menu
  item to the wrong screen rather than erroring.
- **`perform_search` is a live-filtering fuzzy list.** Typing the query *is* the search;
  one `Enter` opens the highlighted result. There is no submit step.
- **The watch-history format is not versioned.** Entries are dicts, except very old ones
  which are plain strings — both shapes are still handled in `src/stats.py` and
  `src/anilist_connector.py`. History written by doccli carries a `"Doccli - …"` source
  tag; readers match both prefixes so migrated history keeps counting. Do not narrow
  those checks.
- **`src/storage.py` migrates on first run**, copying `mylist`/`continue`/`history` from
  `~/.config/doccli` if present. It deliberately does **not** copy `settings.json`,
  because that holds an AniList token issued to doccli's API client.
- **Code comments and docstrings are still Polish** in places, inherited from upstream.
  Translating them is safe but noisy; do it in its own commit, never mixed with a change.

## Release process

The version appears in **four** places and they drift silently:

1. `VERSION` in `run.py` (the source of truth).
2. `MyAppVersion` in `installer.iss` — same number, without the leading `v`.
3. The version badge in `README.md`.
4. The main-menu banner in `src/menus_decor.py`, which spells the version out in ASCII
   art. Regenerate it rather than editing by hand:

   ```bash
   python3 -m venv /tmp/bannerenv && /tmp/bannerenv/bin/pip install pyfiglet
   /tmp/bannerenv/bin/python tools/make_banner.py          # rewrites the banner
   /tmp/bannerenv/bin/python tools/make_banner.py --check   # non-zero if stale
   ```

Then:

5. Move the entries out of `Unreleased` into a new section in `CHANGELOG.md`.
6. Commit, then `git tag -a vX.Y.Z` and push the tag.
7. `gh release create vX.Y.Z --title "vX.Y.Z" --notes-file <notes>`.

**The release title must exactly equal `VERSION` in `run.py`.** The update check
(`run.py:106`) compares the release's `name` field against `VERSION` as a plain string —
a title like "otacli v0.1.0" or "0.1.0" makes every launch report an update forever.
Verify after publishing:

```bash
curl -s https://api.github.com/repos/SophanaSok/otacli/releases/latest | grep '"name"'
```

If no release exists at all, the check 404s and is swallowed silently — harmless.

For Windows, attach the Inno Setup `.exe` as a release asset: `run.py` looks for the first
asset ending in `.exe` and offers an in-place update. Without one, Windows users get the
manual-update message.

## Open work

**Needs your accounts or hardware — cannot be done from a Linux checkout:**

- **AniList client ID.** `ANILIST_CLIENT_ID` in `src/main_module.py` is empty, so AniList
  sync is off and the Settings entry explains the setup instead of failing. Register at
  [AniList → Settings → Developer](https://anilist.co/settings/developer) with redirect URL
  `https://anilist.co/api/v2/oauth/pin`. Everything else works without it.
- **Windows installer.** `installer.iss` was rebranded and a stray Markdown fence that
  would not compile was removed, but it has **never been built or run** for this project.
  It needs a Windows machine with Inno Setup. Until then the README tells Windows users to
  run from source, and no `.exe` is attached to releases.

**Known rough edges inherited from upstream, none urgent:**

- `installer.iss` packs the whole directory with `Source: "*"` excluding only `*.iss`, so
  building from a working checkout would ship `.git` and `__pycache__`.
- Menu recursion means a long session grows the call stack indefinitely. Not a practical
  problem at human navigation speeds, but it rules out very long-lived sessions.
- No test suite, no CI, no linter configuration. `python3 tools/find_dead_imports.py`
  covers one narrow case and currently reports nothing.

**Ideas, not commitments:**

- **Automatic** intro/outro skipping. The markers already work: `src/player.py` writes an
  aniskip chapter file via `generate_aniskip_chapters` and passes it to mpv as
  `--chapters-file`, so chapters are visible in the player today. What is missing is
  skipping them without a keypress. Upstream listed both as planned; only the second half
  is actually outstanding.
- More sources. The `[PL]`/`[EN]` split in `w_players` (`src/main_module.py`) is the seam a
  new source would plug into.
- A `requirements.txt`. The dependency list is currently duplicated in `install.sh`,
  `setup_env.bat` and `tools/Dockerfile.demo`, and they must be kept in sync by hand.

## Regenerating assets

Both the icons and the demo GIF are generated, not hand-made. See
[`tools/README.md`](tools/README.md) for the commands. Both were verified to reproduce the
committed files byte-for-byte (icons) and equivalently (GIF).
