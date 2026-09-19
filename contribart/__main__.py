"""CLI: python -m contribart --user <usuario> --style <estilo> --palette <paleta> --out <arquivo>"""

import argparse
import sys

from .fetch import fetch_contributions
from .palettes import PALETTES
from .render import render


def main():
    parser = argparse.ArgumentParser(
        prog="contribart",
        description="Transforma seu histórico de contribuições do GitHub em arte.",
    )
    parser.add_argument("--user", required=True, help="usuário do GitHub")
    parser.add_argument(
        "--style",
        default="neon",
        choices=["neon", "mono", "pixel"],
        help="estilo visual (default: neon)",
    )
    parser.add_argument(
        "--palette",
        default=None,
        choices=sorted(PALETTES),
        help="paleta de cores (default: a do estilo)",
    )
    parser.add_argument(
        "--out", default=None, help="caminho do arquivo de saída (.png)"
    )
    args = parser.parse_args()

    out_path = args.out or f"{args.user}_{args.style}.png"

    print(f"Buscando contribuições de '{args.user}'...")
    try:
        grid = fetch_contributions(args.user)
    except Exception as exc:  # noqa: BLE001
        print(f"Erro: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Renderizando estilo '{args.style}'...")
    img = render(grid, style=args.style, palette=args.palette)
    img.save(out_path)
    print(f"Pronto! Imagem salva em: {out_path}")


if __name__ == "__main__":
    main()