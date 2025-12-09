# Git Flow (main/staging/develop) Demo

This repo is a staged snapshot of a small project after some time using a 3-branch Git Flow approach:

- **main**: production-ready releases
- **staging**: pre-prod / release candidate testing
- **develop**: day-to-day integration for features

Everything here is Markdown to keep the history easy to read.

## Visual graph

See `docs/git-graph.png` for a rendered snapshot of the branch history; regenerate with:

```
git log --graph --decorate --oneline --all > docs/git-graph.txt
python3 scripts/render-graph.py
```
