# contribart

Transforma seu histórico de contribuições do GitHub em arte — neon, minimalista ou pixel art — direto do terminal.

![exemplo](docs/example_neon.png)

## Por que

O gráfico de contribuições padrão do GitHub é feio e igual para todo mundo. `contribart` reaproveita os mesmos dados para gerar uma imagem que você pode usar no seu README, no Twitter/LinkedIn, ou de wallpaper.

## Instalação

```bash
git clone https://github.com/gustavo1braga/contribart.git
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
python -m contribart --user octocat --style neon --palette sunset
```
| Opção | Descrição | Padrão |
|-------|-----------|--------|
| `--user` | Usuário do GitHub (obrigatório) | - |
| `--style` | Estilo visual: `neon`, `mono`, `pixel` | `neon` |
| `--palette` | Paleta de cores (veja abaixo) | paleta padrão do estilo |
| `--out` | Caminho do arquivo de saída (`.png`) | `<usuario>_<estilo>.png` |

## Estilos disponíveis

| Estilo  | Descrição                                        | Paleta padrão |
|---------|--------------------------------------------------|---------------|
| `neon`  | Efeito glow sobre fundo escuro                   | `neon`        |
| `mono`  | Células lisas, minimalista                       | `github`      |
| `pixel` | Downscale + upscale sem suavização (pixel art)   | `pixel`       |


## Paletas de cores

Qualquer paleta pode ser combinada com qualquer estilo usando `--palette`.

| Paleta    | Descrição                                            |
|-----------|------------------------------------------------------|
| `neon`    | Ciano para magenta sobre fundo quase preto           |
| `github`  | Verde clássico do GitHub sobre fundo escuro          |
| `pixel`   | Verde escuro para menta sobre fundo escuro           |
| `sunset`  | Coral para amarelo quente sobre fundo roxo escuro    |
| `ocean`   | Azul profundo para água-marinha sobre fundo marinho  |
| `dracula` | Azul acinzentado para rosa sobre o cinza do Dracula  |

## Roadmap

- [x] Mais paletas de cor (`--palette`)
- [ ] Modo "poster" com nome do usuário e estatísticas (`--poster`)
- [ ] Exportar como GIF animado (semana surgindo progressivamente) (`--gif`)
- [ ] Publicar no PyPI (`pip install contribart`)

## Licença

MIT Licensw.
