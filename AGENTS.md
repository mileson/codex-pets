# Repository Agent Instructions

These instructions apply to the whole `codex-pets` repository.

## Pet Maintenance Rules

- Do not remove or rename existing pets unless the user explicitly asks for that.
- Keep each pet id stable after publication. For a new pet such as "Context Pad", use a lowercase stable folder id such as `context-pad` unless the user gives a different id.
- A pet folder must contain exactly the installable pet files:
  - `pets/<pet-id>/pet.json`
  - `pets/<pet-id>/spritesheet.webp`
- `pet.json` must use clean user-facing copy. Do not leave image prompts, generation notes, Chinese wrapper text, or internal process wording in `description`.
- The installable package must contain `pet.json` and `spritesheet.webp` at the zip root, not inside a nested folder.
- Keep detailed contact sheets under `assets/<pet-id>/contact-sheet.png` when available, but do not add full contact sheets to the main README pet gallery.
- After adding, removing, renaming, or visually changing any pet, run `python3 scripts/generate_pet_gallery.py` and commit the refreshed `assets/pet-gallery.png`.
- If gallery generation fails because Pillow is missing, install repository tooling with `python3 -m pip install -r requirements.txt` or use an existing Python runtime that already has Pillow.
- The main README pet table is compact and manual. When adding a pet, update both `README.md` and `README_CN.md` with the new pet name, short description, and package link.
- Keep the pet-count badge in both READMEs in sync with the number of folders under `pets/`.

## Standard Add-Pet Checklist

1. Create `pets/<pet-id>/pet.json` and `pets/<pet-id>/spritesheet.webp`.
2. Create or refresh `packages/<pet-id>.codex-pet.zip` from inside `pets/<pet-id>/`:

   ```bash
   zip -r ../../packages/<pet-id>.codex-pet.zip pet.json spritesheet.webp
   ```

3. Add or refresh `assets/<pet-id>/contact-sheet.png` if a detailed preview is available.
4. Install tooling once if needed with `python3 -m pip install -r requirements.txt`.
5. Run `python3 scripts/generate_pet_gallery.py`.
6. Update `README.md`, `README_CN.md`, and `CONTRIBUTING.md` only if their visible instructions need to change.
7. Verify:

   ```bash
   unzip -t packages/<pet-id>.codex-pet.zip
   unzip -p packages/<pet-id>.codex-pet.zip pet.json
   git diff --check
   ```

8. Stage only the files related to the requested pet or documentation change. Leave unrelated local drafts untouched.

## Documentation

For the full maintainer flow, see `docs/MAINTAINING.md`.
