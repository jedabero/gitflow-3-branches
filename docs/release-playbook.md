# Release Playbook (Condensed)

1) Cut release branch from `develop` to `staging`.
2) Tag RC on `staging` (e.g., `v1.1-rc1`).
3) Fixes land in `develop` and are cherry-picked or merged into `staging`.
4) When stable, fast-forward or merge `staging` to `main` and tag the release.
5) Back-merge `main` to `develop` if it diverged.
