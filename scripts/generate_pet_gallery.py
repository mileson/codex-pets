#!/usr/bin/env python3
"""Generate a README gallery image from the repository pet spritesheets."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError as exc:
    raise SystemExit("Missing Pillow. Run `python3 -m pip install -r requirements.txt` before generating the gallery.") from exc

CELL_W = 192
CELL_H = 208


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            try:
                return ImageFont.truetype(str(path), size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> int:
    left, _top, right, _bottom = draw.textbbox((0, 0), text, font=font)
    return int(right - left)


def trim_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    bbox = rgba.getbbox()
    return rgba.crop(bbox) if bbox else rgba


def load_pet(pet_dir: Path) -> dict[str, object] | None:
    meta_path = pet_dir / "pet.json"
    sheet_path = pet_dir / "spritesheet.webp"
    if not meta_path.is_file() or not sheet_path.is_file():
        return None
    metadata = json.loads(meta_path.read_text(encoding="utf-8"))
    with Image.open(sheet_path) as sheet:
        sprite = trim_alpha(sheet.convert("RGBA").crop((0, 0, CELL_W, CELL_H)))
    return {
        "id": metadata.get("id", pet_dir.name),
        "displayName": metadata.get("displayName", pet_dir.name),
        "description": metadata.get("description", ""),
        "sprite": sprite,
    }


def build_gallery(pets: list[dict[str, object]], output: Path, max_columns: int) -> None:
    if not pets:
        raise SystemExit("No pets found")

    columns = min(max_columns, len(pets))
    rows = math.ceil(len(pets) / columns)
    tile_w = 230
    tile_h = 230
    padding = 28
    gap = 18
    title_h = 0
    width = padding * 2 + columns * tile_w + (columns - 1) * gap
    height = padding * 2 + title_h + rows * tile_h + (rows - 1) * gap

    image = Image.new("RGBA", (width, height), (248, 250, 252, 255))
    draw = ImageDraw.Draw(image)
    name_font = load_font(24)

    for index, pet in enumerate(pets):
        row = index // columns
        col = index % columns
        x = padding + col * (tile_w + gap)
        y = padding + title_h + row * (tile_h + gap)
        draw.rounded_rectangle((x, y, x + tile_w, y + tile_h), radius=18, fill=(255, 255, 255, 255), outline=(220, 226, 235, 255), width=2)

        sprite = pet["sprite"].copy()  # type: ignore[index, union-attr]
        sprite.thumbnail((150, 150), Image.Resampling.LANCZOS)
        sx = x + (tile_w - sprite.width) // 2
        sy = y + 26 + (150 - sprite.height) // 2
        image.alpha_composite(sprite, (sx, sy))

        name = str(pet["displayName"])
        if text_width(draw, name, name_font) > tile_w - 28:
            while name and text_width(draw, name + "...", name_font) > tile_w - 28:
                name = name[:-1]
            name = name + "..."
        tx = x + (tile_w - text_width(draw, name, name_font)) // 2
        draw.text((tx, y + 184), name, fill=(24, 31, 42, 255), font=name_font)

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("assets/pet-gallery.png"))
    parser.add_argument("--max-columns", type=int, default=7)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    pets_root = repo_root / "pets"
    pets = [pet for pet_dir in sorted(pets_root.iterdir()) if pet_dir.is_dir() for pet in [load_pet(pet_dir)] if pet]
    pets.sort(key=lambda pet: str(pet["displayName"]).casefold())
    build_gallery(pets, repo_root / args.output, max(1, args.max_columns))
    print(f"Generated {args.output} with {len(pets)} pets")


if __name__ == "__main__":
    main()
