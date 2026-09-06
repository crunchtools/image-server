# Image Server — retired

**The image server lives in [`crunchtools/rotv`](https://github.com/crunchtools/rotv) under `image-server/`.**
Open changes there. Nothing in this repository is built or deployed.

## What happened

The code moved into the ROTV monorepo per spec `008-image-server-monorepo` ("Move the
image-server Python codebase (crunchtools/image-server) into the ROTV repo as a sibling
service"). This repo was never retired afterwards, and it kept building.

Both repos pushed `quay.io/crunchtools/images-rotv:latest`, both fired by the same weekly
`parent-image-updated` dispatch, so whichever build finished last won the tag. By then the
two copies had drifted **309 lines across seven files** — `api.py`, `config.py`,
`database.py`, `exif.py`, `main.py`, `thumbnails.py`, `vision.py`. A build from here would
have put months-old code behind `images.rootsofthevalley.org`. It last pushed successfully
on 2026-08-30.

The build workflow was removed in #5. The source was removed here so it cannot be mistaken
for something maintained.

## The old code

Preserved in full, two ways:

- **[Release `archive-2026-09-06`](https://github.com/crunchtools/image-server/releases/tag/archive-2026-09-06)**
  — `.tar.gz` and `.zip` of the complete tree, with `SHA256SUMS`.
- **This repository's git history**, unchanged. `git log` and `git show` still work;
  the last commit to touch `src/` was `9ad04df` on 2026-04-19.

To get it back: `gh release download archive-2026-09-06 --repo crunchtools/image-server`
