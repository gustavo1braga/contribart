# contribart

Transforma seu histórico de contribuições do GitHub em arte — neon, minimalista ou pixel art — direto do terminal.

![exemplo](docs/example_neon.png)

## Por que

O gráfico de contribuições padrão do GitHub é feio e igual para todo mundo. `contribart` reaproveita os mesmos dados para gerar uma imagem que você pode usar no seu README, no Twitter/LinkedIn, ou de wallpaper.

## Instalação

```bash
git clone https://github.com/seu-usuario/contribart.git
cd contribart
pip install -r requirements.txt
```

Crie um [Personal Access Token](https://github.com/settings/tokens) com escopo `read:user` e exporte:

```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
```

## Uso

```bash
python -m contribart --user octocat --style neon
python -m contribart --user octocat --style mono --out minha_arte.png
python -m contribart --user octocat --style pixel
```

## Estilos disponíveis

| Estilo  | Descrição                                   |
|---------|----------------------------------------------|
| `neon`  | Glow magenta/ciano sobre fundo escuro         |
| `mono`  | Verde GitHub clássico, minimalista            |
| `pixel` | Downscale + upscale sem suavização (pixel art)|

## Roadmap

- [ ] Exportar como GIF animado (semana surgindo progressivamente)
- [ ] Mais paletas de cor
- [ ] Modo "poster" com nome do usuário e estatísticas
- [ ] Publicar no PyPI (`pip install contribart`)

## Licença

MIT
