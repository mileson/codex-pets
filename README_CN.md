# Codex Pets

> Codex Desktop 自定义宠物合集。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Pets](https://img.shields.io/badge/pets-4-blue.svg)](#宠物)

[English](README.md)

## 宠物

这张宫格由 `scripts/generate_pet_gallery.py` 根据 `pets/*/pet.json` 和每个 `spritesheet.webp` 的第一帧自动生成。新增宠物文件夹后重跑脚本，宫格会自动扩展成多行。

![Codex 宠物宫格](assets/pet-gallery.png)

| 宠物 | 说明 | 安装包 |
| --- | --- | --- |
| Milkbyte（奶黄小龙） | 温暖的黄色奶龙小伙伴，奶油色肚皮和青蓝小火花点缀，适合轻松陪伴工作。 | [milkbyte.codex-pet.zip](packages/milkbyte.codex-pet.zip) |
| Plaidpup（蓝格衬衫黑柴） | 穿蓝格衬衫的黑柴小伙伴，动作更连贯、适合轻松陪伴。 | [plaidpup.codex-pet.zip](packages/plaidpup.codex-pet.zip) |
| Vowlet（金发链环守护者） | 安静专注的金发链环守护者，适合陪你检查、思考和推进任务。 | [vowlet.codex-pet.zip](packages/vowlet.codex-pet.zip) |
| Yueyao（月曜琉璃龙） | 稀有的月光琉璃龙，适合安静陪伴你深度工作。 | [yueyao.codex-pet.zip](packages/yueyao.codex-pet.zip) |

完整动画预览仍保留在 `assets/<pet-id>/` 目录下。

## 快速安装

从仓库包下载并安装 Milkbyte：

```bash
curl -L "https://raw.githubusercontent.com/mileson/codex-pets/main/packages/milkbyte.codex-pet.zip" -o "/tmp/milkbyte.codex-pet.zip" \
  && mkdir -p "$HOME/.codex/pets/milkbyte" \
  && unzip -o "/tmp/milkbyte.codex-pet.zip" -d "$HOME/.codex/pets/milkbyte"
```

从 GitHub 下载并安装 Yueyao：

```bash
curl -L "https://github.com/mileson/codex-pets/releases/download/v0.1.0/yueyao.codex-pet.zip" -o "/tmp/yueyao.codex-pet.zip" \
  && mkdir -p "$HOME/.codex/pets/yueyao" \
  && unzip -o "/tmp/yueyao.codex-pet.zip" -d "$HOME/.codex/pets/yueyao"
```

从仓库包下载并安装 Vowlet：

```bash
curl -L "https://raw.githubusercontent.com/mileson/codex-pets/main/packages/vowlet.codex-pet.zip" -o "/tmp/vowlet.codex-pet.zip" \
  && mkdir -p "$HOME/.codex/pets/vowlet" \
  && unzip -o "/tmp/vowlet.codex-pet.zip" -d "$HOME/.codex/pets/vowlet"
```

从仓库包下载并安装 Plaidpup：

```bash
curl -L "https://raw.githubusercontent.com/mileson/codex-pets/main/packages/plaidpup.codex-pet.zip" -o "/tmp/plaidpup.codex-pet.zip" \
  && mkdir -p "$HOME/.codex/pets/plaidpup" \
  && unzip -o "/tmp/plaidpup.codex-pet.zip" -d "$HOME/.codex/pets/plaidpup"
```

如果你已经克隆了这个仓库，也可以从本地文件安装：

```bash
mkdir -p "$HOME/.codex/pets/yueyao" \
  && cp pets/yueyao/pet.json pets/yueyao/spritesheet.webp "$HOME/.codex/pets/yueyao/"
```

## 在 Codex 里选择宠物

安装后按这个流程操作：

1. 完整退出并重新打开 Codex Desktop。
2. 打开 Codex 设置。
3. 进入 **Appearance**。
4. 找到 **Pets**。
5. 选择 **Yueyao**。
6. 输入 `/pet`，或者用 **Wake Pet** 呼唤它。

按截图里的编号操作：先从左下角菜单打开 **Settings**。

![打开 Codex 设置](docs/codex-open-settings.png)

然后进入 **Appearance**，滚动到 **Custom pets**，选择 **Yueyao**。

![在 Appearance / Pets 里选择 Yueyao](docs/codex-appearance-pets-annotated.png)

```mermaid
flowchart LR
  A["下载宠物包"] --> B["解压到 ~/.codex/pets/yueyao"]
  B --> C["重启 Codex Desktop"]
  C --> D["打开设置"]
  D --> E["Appearance"]
  E --> F["Pets"]
  F --> G["选择 Yueyao"]
  G --> H["输入 /pet"]
```

## 仓库结构

```text
codex-pets/
  assets/
    pet-gallery.png
    milkbyte/
      contact-sheet.png
    yueyao/
      contact-sheet.png
    vowlet/
      contact-sheet.png
    plaidpup/
      contact-sheet.png
  scripts/
    generate_pet_gallery.py
  requirements.txt
  packages/
    milkbyte.codex-pet.zip
    yueyao.codex-pet.zip
    vowlet.codex-pet.zip
    plaidpup.codex-pet.zip
  pets/
    milkbyte/
      pet.json
      spritesheet.webp
    yueyao/
      pet.json
      spritesheet.webp
    vowlet/
      pet.json
      spritesheet.webp
    plaidpup/
      pet.json
      spritesheet.webp
```

每个宠物文件夹需要包含：

- `pet.json`：宠物信息。
- `spritesheet.webp`：动画精灵图。

可安装的 zip 包里应该直接包含这两个文件，不要再套一层文件夹。

## 添加新的宠物

1. 创建 `pets/<pet-id>/`。
2. 放入 `pet.json` 和 `spritesheet.webp`。
3. 打包成 `packages/<pet-id>.codex-pet.zip`。
4. 如有需要，在 `assets/<pet-id>/` 放一张完整预览图。
5. 如有需要，先运行 `python3 -m pip install -r requirements.txt` 安装工具依赖。
6. 运行 `python3 scripts/generate_pet_gallery.py` 刷新宫格图。
7. 如果简短说明有变化，更新 `README.md` 和 `README_CN.md`。

完整的维护流程和 Agent 操作规范见 [docs/MAINTAINING.md](docs/MAINTAINING.md)。

示例：

```bash
cd pets/yueyao
zip -r ../../packages/yueyao.codex-pet.zip pet.json spritesheet.webp
```

## 截图说明

带标注的截图放在 [docs](docs/) 目录。

## 贡献

欢迎提交新的宠物包、预览图和文档改进。提交前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [docs/MAINTAINING.md](docs/MAINTAINING.md)。

## 安全

如果要报告敏感问题，请不要发公开 issue。请查看 [SECURITY.md](SECURITY.md)。

## 许可证

MIT

## 作者

- X: [Mileson07](https://x.com/Mileson07)
- 小红书: [超级峰](https://xhslink.com/m/4LnJ9aB1f97)
- 抖音: [超级峰](https://v.douyin.com/rH645q7trd8/)
