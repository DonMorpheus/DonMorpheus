#!/usr/bin/env python3
"""Brick-and-charcoal digital rain — packets falling, Matrix cadence."""
from __future__ import annotations

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path("/home/kali/github/DonMorpheus/assets")
FONT_KATA = "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

W, H = 1280, 260
CELL_W, CELL_H = 15, 17
COLS = W // CELL_W
ROWS = H // CELL_H + 8
NFRAMES = 36
WARMUP = 24
DURATION_MS = 65

BG = (18, 14, 11)
HEAD = (250, 240, 224)
NEAR = (232, 130, 72)
MID = (196, 69, 54)
TAIL = (120, 48, 38)
FADE = (52, 32, 24)

KATA = list("アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン")
HEX = list("0123456789ABCDEF")


def lerp(a, b, t: float):
    t = max(0.0, min(1.0, t))
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def color_for(offset: int, length: int):
    if offset == 0:
        return HEAD
    if offset == 1:
        return NEAR
    t = offset / max(length, 2)
    if t < 0.4:
        return lerp(MID, TAIL, t / 0.4)
    return lerp(TAIL, FADE, (t - 0.4) / 0.6)


def make_streams(rng: random.Random):
    streams = []
    for c in range(COLS):
        if rng.random() < 0.06:
            continue
        packet = rng.random() < 0.42
        length = rng.randint(10, 22)
        alphabet = HEX if packet else KATA
        streams.append(
            {
                "col": c,
                "head": rng.uniform(-ROWS, ROWS * 0.4),
                "speed": rng.uniform(0.55, 1.7) if packet else rng.uniform(0.28, 1.05),
                "length": length,
                "packet": packet,
                "chars": [rng.choice(alphabet) for _ in range(length + ROWS)],
            }
        )
    return streams


def render_frame(streams, font_k, font_m, rng: random.Random) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    for s in streams:
        font = font_m if s["packet"] else font_k
        alphabet = HEX if s["packet"] else KATA
        head = s["head"]
        length = s["length"]
        x = s["col"] * CELL_W + 1
        for i in range(length):
            y = int((head - i) * CELL_H)
            if y < -CELL_H or y > H:
                continue
            ch = s["chars"][(int(head) - i) % len(s["chars"])]
            fill = color_for(i, length)
            if i == 0:
                draw.text((x, y + 1), ch, font=font, fill=NEAR)
            draw.text((x, y), ch, font=font, fill=fill)
        s["head"] += s["speed"]
        if s["head"] - length > ROWS:
            s["head"] = rng.uniform(-14, -3)
            s["length"] = rng.randint(10, 22)
            s["packet"] = rng.random() < 0.42
            alphabet = HEX if s["packet"] else KATA
            s["speed"] = rng.uniform(0.55, 1.7) if s["packet"] else rng.uniform(0.28, 1.05)
            s["chars"] = [rng.choice(alphabet) for _ in range(s["length"] + ROWS)]
        if rng.random() < 0.12:
            s["chars"][rng.randrange(len(s["chars"]))] = rng.choice(alphabet)
    return img


def quantize(frames: list[Image.Image]) -> list[Image.Image]:
    base = frames[0].quantize(colors=40, method=Image.Quantize.MEDIANCUT)
    out = [base]
    for f in frames[1:]:
        out.append(f.quantize(palette=base, dither=Image.Dither.NONE))
    return out


def write_gif(path: Path, seed: int) -> None:
    rng = random.Random(seed)
    font_k = ImageFont.truetype(FONT_KATA, 13)
    font_m = ImageFont.truetype(FONT_MONO, 13)
    streams = make_streams(rng)
    for _ in range(WARMUP):
        render_frame(streams, font_k, font_m, rng)
    frames = [render_frame(streams, font_k, font_m, rng) for _ in range(NFRAMES)]
    frames[0].save(path.with_suffix(".png"))
    q = quantize(frames)
    q[0].save(
        path,
        save_all=True,
        append_images=q[1:],
        duration=DURATION_MS,
        loop=0,
        optimize=True,
        disposal=2,
    )


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    write_gif(OUT / "rain-1.gif", seed=13)
    write_gif(OUT / "rain-2.gif", seed=37)
    for name in ("rain-1.gif", "rain-2.gif", "rain-1.png", "rain-2.png"):
        p = OUT / name
        print(f"{p.name:12} {p.stat().st_size / 1024:.1f} KB")
