#!/usr/bin/env python3
"""Render docs/git-graph.txt to a self-contained SVG (docs/git-graph.svg).

No external dependencies; uses only Python stdlib.
"""
from pathlib import Path
import html

text_path = Path("docs/git-graph.txt")
svg_path = Path("docs/git-graph.svg")
if not text_path.exists():
    raise SystemExit("docs/git-graph.txt missing; run git log export first")

lines = text_path.read_text().splitlines() or [""]
font_size = 14
line_height = 18
margin = 16
max_chars = max(len(line) for line in lines)
width = margin * 2 + max_chars * (font_size * 0.6)
height = margin * 2 + len(lines) * line_height

def svg_text_lines():
    for i, line in enumerate(lines):
        y = margin + (i + 1) * line_height
        yield f'<text x="{margin}" y="{y}" font-family="monospace" font-size="{font_size}">{html.escape(line)}</text>'

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{int(width)}" height="{int(height)}" viewBox="0 0 {int(width)} {int(height)}">
  <rect width="100%" height="100%" fill="white"/>
  {' '.join(svg_text_lines())}
</svg>
"""
svg_path.write_text(svg)
print(f"Wrote {svg_path} ({len(lines)} lines)")
