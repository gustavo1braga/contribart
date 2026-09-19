"""Paletas de cor: bg = fundo, low = intensidade mínima, high = máxima."""

PALETTES = {
    "neon":    {"bg": (5, 5, 15),    "low": (0, 200, 255),  "high": (255, 0, 200)},
    "github":  {"bg": (13, 17, 23),  "low": (14, 68, 41),   "high": (57, 211, 83)},
    "pixel":   {"bg": (20, 20, 30),  "low": (0, 90, 60),    "high": (170, 255, 200)},
    "sunset":  {"bg": (25, 10, 30),  "low": (255, 94, 98),  "high": (255, 195, 113)},
    "ocean":   {"bg": (5, 15, 30),   "low": (0, 90, 160),   "high": (120, 240, 230)},
    "dracula": {"bg": (40, 42, 54),  "low": (98, 114, 164), "high": (255, 121, 198)},
}

# paleta usada quando o usuário não escolhe nenhuma
STYLE_DEFAULTS = {"neon": "neon", "mono": "github", "pixel": "pixel"}


def mix(a, b, t: float):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))