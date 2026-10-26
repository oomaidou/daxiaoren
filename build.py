#!/usr/bin/env python3
"""Build the single-file game from the maintainable source in source/."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source"

html = (SOURCE / "index.html").read_text(encoding="utf-8")
css = (SOURCE / "style.css").read_text(encoding="utf-8")
js = (SOURCE / "game.js").read_text(encoding="utf-8")

built = html.replace(
    '<link rel="stylesheet" href="style.css">',
    "<style>\n" + css + "\n</style>",
)
built = built.replace(
    '<script src="game.js"></script>',
    "<script>\n" + js + "\n</script>",
)

# index.html is the version served by GitHub Pages.
(ROOT / "index.html").write_text(built, encoding="utf-8")

# A local, friendly double-click copy. Ignored by git.
(ROOT / "打小人.html").write_text(built, encoding="utf-8")

print(f"built index.html ({len(built):,} chars)")
print(f"built 打小人.html (local copy, ignored by git)")
