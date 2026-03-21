"""Thumbnail generation using Pillow."""

from __future__ import annotations

import logging
from pathlib import Path

from PIL import Image

from .config import get_config

logger = logging.getLogger(__name__)


def generate_thumbnail(source_path: Path, dest_path: Path) -> tuple[int, int]:
    """Generate a JPEG thumbnail from an image file.

    Returns (width, height) of the thumbnail.
    """
    cfg = get_config()
    size = cfg.thumbnail_size

    with Image.open(source_path) as img:
        # Convert RGBA/P to RGB for JPEG output
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.thumbnail((size, size), Image.Resampling.LANCZOS)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(dest_path, "JPEG", quality=85, optimize=True)
        logger.info("Generated thumbnail: %s (%dx%d)", dest_path.name, img.width, img.height)
        return img.width, img.height


def generate_thumbnail_from_bytes(
    data: bytes, dest_path: Path
) -> tuple[int, int]:
    """Generate a JPEG thumbnail from raw image bytes.

    Returns (width, height) of the thumbnail.
    """
    import io

    cfg = get_config()
    size = cfg.thumbnail_size

    with Image.open(io.BytesIO(data)) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.thumbnail((size, size), Image.Resampling.LANCZOS)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(dest_path, "JPEG", quality=85, optimize=True)
        return img.width, img.height


def get_image_dimensions(data: bytes) -> tuple[int, int]:
    """Get width and height from image bytes without fully decoding."""
    import io

    with Image.open(io.BytesIO(data)) as img:
        return img.width, img.height
