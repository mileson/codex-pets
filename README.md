# Codex Pets

> A growing collection of custom pets for Codex Desktop.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Pets](https://img.shields.io/badge/pets-14-blue.svg)](#pets)

[中文说明](README_CN.md)

## Pets

![Codex pet gallery](assets/pet-gallery.png?v=14-refreshed)

| Pet | Description | Package |
| --- | --- | --- |
| Auruowl | An aurora owl scholar with bright brow feathers for focused review sessions. | [auruowl.codex-pet.zip](packages/auruowl.codex-pet.zip) |
| Bonsaigo | A calm bonsai stone golem companion with a sprout crown. | [bonsaigo.codex-pet.zip](packages/bonsaigo.codex-pet.zip) |
| Canglan | A gentle azure cloud qilin calf with a jade horn and soft cloud mane. | [canglan.codex-pet.zip](packages/canglan.codex-pet.zip) |
| Chadango | A tea lantern tanuki companion with a dango tail charm. | [chadango.codex-pet.zip](packages/chadango.codex-pet.zip) |
| Clockshiba | A clockwork shiba pup with a copper gear collar. | [clockshiba.codex-pet.zip](packages/clockshiba.codex-pet.zip) |
| CorgiByte | A cheerful short-legged corgi coding buddy with a tiny cyan spark charm. | [corgibyte.codex-pet.zip](packages/corgibyte.codex-pet.zip) |
| Glassbun | A glass bunny-dragon hybrid companion with tiny horn ears. | [glassbun.codex-pet.zip](packages/glassbun.codex-pet.zip) |
| Luminara | A moon lantern moth mage companion with soft wings. | [luminara.codex-pet.zip](packages/luminara.codex-pet.zip) |
| Milkbyte | A warm yellow baby dragon with a cream belly and tiny cyan code-spark accents. | [milkbyte.codex-pet.zip](packages/milkbyte.codex-pet.zip) |
| Plaidpup | A black shiba pup in a blue plaid shirt with coherent playful poses. | [plaidpup.codex-pet.zip](packages/plaidpup.codex-pet.zip) |
| Solara | A tiny solar phoenix chick with an ember crest. | [solara.codex-pet.zip](packages/solara.codex-pet.zip) |
| Curarpikt | A focused blond chain guardian with a calm, watchful presence. | [vowlet.codex-pet.zip](packages/vowlet.codex-pet.zip) |
| Yukitsune | A snowcap kitsune cub with frosted ear tips. | [yukitsune.codex-pet.zip](packages/yukitsune.codex-pet.zip) |
| Yueyao | A rare moonlit glass dragon companion for quiet deep work. | [yueyao.codex-pet.zip](packages/yueyao.codex-pet.zip) |

Full animation previews are available in each pet's `assets/<pet-id>/` folder.

## Quick Install

Pick a pet id from the table above, then run:

```bash
PET_ID="yueyao"
curl -L "https://raw.githubusercontent.com/mileson/codex-pets/main/packages/${PET_ID}.codex-pet.zip" -o "/tmp/${PET_ID}.codex-pet.zip" \
  && mkdir -p "$HOME/.codex/pets/${PET_ID}" \
  && unzip -o "/tmp/${PET_ID}.codex-pet.zip" -d "$HOME/.codex/pets/${PET_ID}"
```

If you cloned the repository locally, install from the checked-out files:

```bash
PET_ID="yueyao"
mkdir -p "$HOME/.codex/pets/${PET_ID}" \
  && cp "pets/${PET_ID}/pet.json" "pets/${PET_ID}/spritesheet.webp" "$HOME/.codex/pets/${PET_ID}/"
```

## Select The Pet

After installation:

1. Quit and reopen Codex Desktop.
2. Open Codex settings.
3. Go to **Appearance**.
4. Find **Pets**.
5. Select the pet you installed.
6. Use `/pet` or **Wake Pet** to call it onto the screen.

Use the numbered callouts in the screenshots: first open **Settings** from the lower-left menu.

![Open Codex settings](docs/codex-open-settings.png)

Then select **Appearance**, scroll to **Custom pets**, and choose your pet.

![Select a pet in Appearance / Pets](docs/codex-appearance-pets-annotated.png)

```mermaid
flowchart LR
  A["Download pet pack"] --> B["Unzip into ~/.codex/pets/<pet-id>"]
  B --> C["Restart Codex Desktop"]
  C --> D["Open Settings"]
  D --> E["Appearance"]
  E --> F["Pets"]
  F --> G["Select pet"]
  G --> H["Run /pet"]
```

## Screenshots

Annotated screenshots live in [docs](docs/).

## Contributing

Pet packs, previews, and documentation improvements are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/MAINTAINING.md](docs/MAINTAINING.md) before opening a pull request.

## Security

Please do not open a public issue for sensitive reports. See [SECURITY.md](SECURITY.md).

## License

MIT

## Author

- X: [Mileson07](https://x.com/Mileson07)
- Xiaohongshu: [超级峰](https://xhslink.com/m/4LnJ9aB1f97)
- Douyin: [超级峰](https://v.douyin.com/rH645q7trd8/)
