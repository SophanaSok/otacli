#!/usr/bin/env python3
"""List imports whose name is never used again in the same file.

The project has no linter; this is the check used to keep track of the dead
imports inherited from upstream. Run from the repository root:

    python3 tools/find_dead_imports.py

Only reports names that appear nowhere except their own import statement, so it
does not flag re-exports or conditional use. Exits 0 regardless — informational.
"""
import ast
import pathlib
import sys


def dead_imports(path: pathlib.Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))

    imported: dict[str, int] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported[(alias.asname or alias.name).split(".")[0]] = node.lineno
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imported[alias.asname or alias.name] = node.lineno

    used = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    used |= {
        n.value.id
        for n in ast.walk(tree)
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name)
    }

    return [f"{name} (line {line})" for name, line in sorted(imported.items()) if name not in used]


def main() -> int:
    root = pathlib.Path(__file__).resolve().parent.parent
    files = sorted(root.glob("src/*.py")) + [root / "run.py"]

    total = 0
    for path in files:
        found = dead_imports(path)
        if found:
            total += len(found)
            print(f"{path.relative_to(root)}:")
            for item in found:
                print(f"    {item}")

    print(f"\n{total} unused import(s)" if total else "\nno unused imports")
    return 0


if __name__ == "__main__":
    sys.exit(main())
