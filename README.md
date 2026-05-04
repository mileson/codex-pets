# Codex Pets

> A growing collection of custom pets for Codex Desktop.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Pets](https://img.shields.io/badge/pets-1-blue.svg)](#pets)

[中文说明](README_CN.md)

## Pets

### Yueyao

Yueyao is a rare moonlit glass dragon companion for quiet deep work.

![Yueyao animation contact sheet](assets/yueyao/contact-sheet.png)

## Quick Install

Install Yueyao from this repository:

```bash
curl -L "https://github.com/mileson/codex-pets/raw/main/packages/yueyao.codex-pet.zip" -o "/tmp/yueyao.codex-pet.zip" \
  && mkdir -p "$HOME/.codex/pets/yueyao" \
  && unzip -o "/tmp/yueyao.codex-pet.zip" -d "$HOME/.codex/pets/yueyao"
```

If you cloned the repository locally, install from the checked-out files:

```bash
mkdir -p "$HOME/.codex/pets/yueyao" \
  && cp pets/yueyao/pet.json pets/yueyao/spritesheet.webp "$HOME/.codex/pets/yueyao/"
```

## Select The Pet

After installation:

1. Quit and reopen Codex Desktop.
2. Open Codex settings.
3. Go to **Appearance**.
4. Find **Pets**.
5. Select **Yueyao**.
6. Use `/pet` or **Wake Pet** to call it onto the screen.

Use the numbered callouts in the screenshots: first open **Settings** from the lower-left menu.

![Open Codex settings](docs/codex-open-settings.png)

Then select **Appearance**, scroll to **Custom pets**, and choose **Yueyao**.

![Select Yueyao in Appearance / Pets](docs/codex-appearance-pets-annotated.png)

```mermaid
flowchart LR
  A["Download pet pack"] --> B["Unzip into ~/.codex/pets/yueyao"]
  B --> C["Restart Codex Desktop"]
  C --> D["Open Settings"]
  D --> E["Appearance"]
  E --> F["Pets"]
  F --> G["Select Yueyao"]
  G --> H["Run /pet"]
```

## Folder Layout

```text
codex-pets/
  assets/
    yueyao/
      contact-sheet.png
  packages/
    yueyao.codex-pet.zip
  pets/
    yueyao/
      pet.json
      spritesheet.webp
```

Each pet folder should contain:

- `pet.json`: pet metadata.
- `spritesheet.webp`: the animation spritesheet.

The installable zip should contain those two files at the top level, not inside an extra nested folder.

## Add Another Pet

1. Create `pets/<pet-id>/`.
2. Add `pet.json` and `spritesheet.webp`.
3. Zip the two files into `packages/<pet-id>.codex-pet.zip`.
4. Add a preview image under `assets/<pet-id>/`.
5. Update this README and `README_CN.md`.

Example:

```bash
cd pets/yueyao
zip -r ../../packages/yueyao.codex-pet.zip pet.json spritesheet.webp
```

## Screenshots

Annotated screenshots live in [docs](docs/).

## Contributing

Pet packs, previews, and documentation improvements are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Security

Please do not open a public issue for sensitive reports. See [SECURITY.md](SECURITY.md).

## License

MIT

## Author

- X: [Mileson07](https://x.com/Mileson07)
- Xiaohongshu: [超级峰](https://xhslink.com/m/4LnJ9aB1f97)
- Douyin: [超级峰](https://v.douyin.com/rH645q7trd8/)
