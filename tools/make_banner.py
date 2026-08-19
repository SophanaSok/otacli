#!/usr/bin/env python3
"""Regenerate the main-menu ASCII banner from the version in run.py.

The banner spells out the version, so it goes stale on every release unless it is
rebuilt. Run this after bumping VERSION in run.py:

    python3 -m venv /tmp/bannerenv && /tmp/bannerenv/bin/pip install pyfiglet
    /tmp/bannerenv/bin/python tools/make_banner.py

Rewrites MAIN_MENU in src/menus_decor.py in place. Pass --check to verify the
committed banner matches the current version without writing anything; it exits
non-zero on a mismatch, which is what you want in a release checklist.
"""
import pathlib
import re
import sys

import pyfiglet

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN_PY = ROOT / "run.py"
DECOR = ROOT / "src" / "menus_decor.py"


def current_version() -> str:
    match = re.search(r'^VERSION = "([^"]+)"', RUN_PY.read_text(encoding="utf-8"), re.M)
    if not match:
        sys.exit(f"could not find VERSION in {RUN_PY}")
    return match.group(1)


def render(version: str) -> str:
    art = pyfiglet.figlet_format(f"OTACLI {version}", font="big")
    lines = art.split("\n")
    # figlet pads with whitespace-only lines; trailing spaces *within* a line are
    # significant to the art and must be kept
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def main() -> int:
    version = current_version()
    banner = render(version)
    block = f"MAIN_MENU = r'''\n{banner}\n'''"

    source = DECOR.read_text(encoding="utf-8")
    pattern = re.compile(r"MAIN_MENU = r'''\n.*?\n'''", re.S)
    if not pattern.search(source):
        sys.exit(f"could not find the MAIN_MENU block in {DECOR}")

    updated = pattern.sub(lambda _: block, source, count=1)

    if "--check" in sys.argv:
        if updated == source:
            print(f"banner matches {version}")
            return 0
        print(f"banner is stale: run.py says {version} but src/menus_decor.py disagrees")
        return 1

    if updated == source:
        print(f"banner already up to date for {version}")
        return 0

    DECOR.write_text(updated, encoding="utf-8")
    print(f"banner regenerated for {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
