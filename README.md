# Image Server — superseded

> **This repository is no longer the source of truth.** The image server lives in
> [`crunchtools/rotv`](https://github.com/crunchtools/rotv) under `image-server/`,
> which is where it is developed and released from.
>
> This copy last changed on 2026-04-19 and had drifted 309 lines across seven
> files from the live one. Until 2026-09-06 it also built and pushed
> `quay.io/crunchtools/images-rotv:latest` — the same tag `crunchtools/rotv`
> publishes, from the same weekly `parent-image-updated` dispatch. Whichever
> build finished last won the tag, so production could have been served this
> stale code at any point. That workflow has been removed.
>
> Do not commit here. Open changes against `crunchtools/rotv`.


Lightweight image server with AI captioning and semantic search. Purpose-built replacement for Immich in the ROTV stack.

## Features

- Image upload with automatic thumbnail generation
- EXIF metadata extraction
- AI captioning via Gemini vision
- Semantic search via fastembed + pgvector
- Full-text search via PostgreSQL tsvector
- Theme video serving
- REST API (FastAPI)

## Quick Start

```bash
podman build -t quay.io/crunchtools/image-server .

podman run -d --name image-server \
  -p 8000:8000 \
  -v image-server-pgdata:/var/lib/pgsql/data:Z \
  -v image-server-media:/data/media:Z \
  --systemd=always \
  quay.io/crunchtools/image-server
```

## API

See `src/image_server/api.py` for full endpoint documentation.

## License

AGPL-3.0-or-later
