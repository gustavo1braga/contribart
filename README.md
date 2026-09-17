[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/gustavo1braga/contribart/blob/master/README.pt-br.md)

# contribart

Transform your GitHub commit history into art: **neon**, **minimalist**, or **pixel art**, straight from your terminal.

![example](docs/example_neon.png)

## Why

GitHub's default contribution graph is plain and looks the same for everyone. `contribart` reuses the exact same data to generate an image you can showcase in your README, share on Twitter/LinkedIn, or use as a wallpaper.

## Installation

```bash
git clone https://github.com/gustavo1braga/contribart.git
cd contribart
pip install -r requirements.txt
```

Create a [Personal Access Token](https://github.com/settings/tokens?utm_source=gemini) with the `read:user` scope and export it:

```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
```

## Usage

```bash
python -m contribart --user octocat --style neon
python -m contribart --user octocat --style mono --out my_art.png
python -m contribart --user octocat --style pixel
```

## Available Styles

| Style | Description |
| --- | --- |
| `neon` | Magenta/cyan glow on a dark background |
| `mono` | Classic GitHub green, minimalist |
| `pixel` | Downscale + upscale without smoothing (pixel art) |

## Roadmap

* [ ] Export as animated GIF (weeks appearing progressively)
* [ ] More color palettes
* [ ] "Poster" mode with username and statistics
* [ ] Publish to PyPI (`pip install contribart`)

## License

MIT
