# tools

Development scripts. None of them is needed to run otacli.

`make_icons.py` and the `demo.tape`/`Dockerfile.demo` pair generate the repository's
assets, so those are reproducible rather than unexplained binaries.
`find_dead_imports.py` is a small static check standing in for the linter the project
does not have — run `python3 tools/find_dead_imports.py` from the repository root.

## `make_icons.py` — `icon_1.png` and `icon.ico`

Draws the terminal-window icon with Pillow at 1024px and downsamples, so the small
sizes stay clean. Run from the repository root:

```bash
python3 -m venv /tmp/iconenv && /tmp/iconenv/bin/pip install pillow
/tmp/iconenv/bin/python tools/make_icons.py
```

Writes `icon_1.png` (512px, used by the README and the Windows installer's wizard
image) and `icon.ico` (multi-size, used by the installer and shortcuts).

## `demo.tape` + `Dockerfile.demo` — `demo.gif`

Records the README demo with [vhs](https://github.com/charmbracelet/vhs) inside a
container, so nothing is installed on the host and the recording never touches your
real config or watch history.

Run from the repository root:

```bash
mkdir -p /tmp/demo-out
docker build -f tools/Dockerfile.demo -t otacli-vhs .
docker run --rm -w /out \
  -v "$PWD/tools/demo.tape:/demo.tape:ro" \
  -v /tmp/demo-out:/out otacli-vhs /demo.tape
cp /tmp/demo-out/demo.gif demo.gif
```

`Dockerfile.demo` installs mpv, chafa and the current yt-dlp so the environment check
shows green, and adds an `otacli` launcher so the recording shows the command users
actually type. Recording takes about a minute; the result is ~800 KB at 1280x720.

### Editing the tape

Key sequence notes, learned the hard way:

- The search screen (`perform_search` in `src/main_module.py`) is a **live-filtering
  fuzzy list**. Typing the query *is* the search; a single `Enter` opens the
  highlighted result. There is no separate submit step — an extra `Enter` lands on
  "Watch from episode 1" and starts playback.
- The recording deliberately **stops at the series page**. Going further reaches the
  source picker, which displays live direct links to third-party streams; those should
  not be baked into a published asset.
- Timings are wall-clock `Sleep`s against live API calls. If the recording desyncs,
  increase the sleeps rather than reordering keys.
