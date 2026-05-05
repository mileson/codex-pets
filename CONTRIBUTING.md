# Contributing

Thanks for helping grow this Codex pet collection.

## Pet Pack Checklist

- Add a new folder under `pets/<pet-id>/`.
- Include `pet.json`.
- Include `spritesheet.webp`.
- Add an installable zip under `packages/<pet-id>.codex-pet.zip`.
- Add a preview image under `assets/<pet-id>/`.
- Install tooling if needed with `python3 -m pip install -r requirements.txt`.
- Run `python3 scripts/generate_pet_gallery.py` to refresh `assets/pet-gallery.png`.
- Update both `README.md` and `README_CN.md`.

For the full maintainer flow, including the gallery and package checks, see [docs/MAINTAINING.md](docs/MAINTAINING.md).

## Zip Format

The zip file should contain the pet files at the top level:

```text
pet.json
spritesheet.webp
```

Avoid this shape:

```text
my-pet/
  pet.json
  spritesheet.webp
```

## Local Test

```bash
mkdir -p "$HOME/.codex/pets/<pet-id>"
unzip -o "packages/<pet-id>.codex-pet.zip" -d "$HOME/.codex/pets/<pet-id>"
```

Then restart Codex Desktop, open **Appearance / Pets**, select the pet, and run `/pet`.
