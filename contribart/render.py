"""Renderiza o grid de contribuições como imagem, com estilos diferentes."""

from PIL import Image, ImageDraw, ImageFilter

from .palettes import PALETTES, STYLE_DEFAULTS, mix

CELL_SIZE = 14
GAP = 4
MARGIN = 20


def _intensity_levels(grid: list[list[int]]) -> list[list[float]]:
    """Normaliza as contagens para valores entre 0 e 1."""
    flat = [v for week in grid for v in week]
    max_val = max(flat) if flat and max(flat) > 0 else 1
    return [[v / max_val for v in week] for week in grid]


def render(grid: list[list[int]], style: str = "neon", palette: str | None = None) -> Image.Image:
    pal = PALETTES[palette or STYLE_DEFAULTS[style]]
    levels = _intensity_levels(grid)
    n_weeks = len(grid)

    width = MARGIN * 2 + n_weeks * (CELL_SIZE + GAP)
    height = MARGIN * 2 + 7 * (CELL_SIZE + GAP)

    if style == "neon":
        return _render_neon(levels, width, height, pal)
    elif style == "mono":
        return _render_mono(levels, width, height, pal)
    elif style == "pixel":
        return _render_pixel(levels, width, height, pal)
    else:
        raise ValueError(f"Estilo desconhecido: {style}")


def _cell_xy(week_idx: int, day_idx: int) -> tuple[int, int]:
    x = MARGIN + week_idx * (CELL_SIZE + GAP)
    y = MARGIN + day_idx * (CELL_SIZE + GAP)
    return x, y


def _render_mono(levels, width, height, pal) -> Image.Image:
    img = Image.new("RGB", (width, height), color=pal["bg"])
    draw = ImageDraw.Draw(img)

    for w, week in enumerate(levels):
        for d, level in enumerate(week):
            x, y = _cell_xy(w, d)
            shade = mix(pal["bg"], pal["high"], 0.15 + 0.85 * level)
            draw.rounded_rectangle(
                [x, y, x + CELL_SIZE, y + CELL_SIZE], radius=3, fill=shade
            )
    return img


def _render_neon(levels, width, height, pal) -> Image.Image:
    base_img = Image.new("RGB", (width, height), color=pal["bg"])
    glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(glow_layer)

    for w, week in enumerate(levels):
        for d, level in enumerate(week):
            if level <= 0:
                continue
            x, y = _cell_xy(w, d)
            color = mix(pal["low"], pal["high"], level)
            alpha = int(80 + 175 * level)
            draw.rounded_rectangle(
                [x, y, x + CELL_SIZE, y + CELL_SIZE],
                radius=3,
                fill=color + (alpha,),
            )

    glow = glow_layer.filter(ImageFilter.GaussianBlur(6))
    base_img.paste(glow, (0, 0), glow)
    base_img.paste(glow_layer, (0, 0), glow_layer)  # núcleo nítido por cima
    return base_img.convert("RGB")


def _render_pixel(levels, width, height, pal) -> Image.Image:
    small_w, small_h = len(levels) + 2, 9
    small = Image.new("RGB", (small_w, small_h), color=pal["bg"])

    palette = [pal["bg"]] + [mix(pal["low"], pal["high"], i / 3) for i in range(4)]

    for w, week in enumerate(levels):
        for d, level in enumerate(week):
            idx = min(int(level * (len(palette) - 1)), len(palette) - 1)
            color = palette[idx] if level > 0 else palette[0]
            small.putpixel((w + 1, d + 1), color)

    return small.resize((width, height), Image.Resampling.NEAREST)