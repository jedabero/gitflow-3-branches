#!/usr/bin/env python3
"""Render docs/git-graph.txt to docs/git-graph.png via dummyimage.com.
Relies only on stdlib and network access.
"""
import urllib.parse
import urllib.request
from pathlib import Path

text_path = Path("docs/git-graph.txt")
png_path = Path("docs/git-graph.png")
size = "1400x2000"
if not text_path.exists():
    raise SystemExit("docs/git-graph.txt missing; run git log export first")

text = text_path.read_text()
encoded = urllib.parse.quote(text)
url = f"https://dummyimage.com/{size}/ffffff/000000.png&text={encoded}"

print(f"Downloading graph image from dummyimage.com to {png_path}")
with urllib.request.urlopen(url) as resp:
    png_path.write_bytes(resp.read())
print("Done.")
