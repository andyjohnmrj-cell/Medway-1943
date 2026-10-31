"""
crop_sprites.py - split a sprite sheet into one transparent PNG per sprite.

Usage:
    python crop_sprites.py sheet.png out_dir [--tolerance 10] [--min-size 4]

How it works:
 1. Background colour = the top-left pixel (sheets usually use a flat
    colour like magenta or black, or are already transparent).
 2. Every pixel within --tolerance of that colour becomes fully transparent.
 3. Remaining (opaque) pixels are grouped into connected blobs
    (8-way flood fill). Each blob's bounding box is one sprite.
 4. Blobs smaller than --min-size pixels on a side are ignored (stray dots).
 5. Each box is cropped and saved as sprite_000.png, sprite_001.png, ...
    in reading order (top to bottom, left to right).

Requires Pillow:  pip install pillow

Citation (CS50 academic honesty): this helper script was written with help
from Claude (Anthropic), an AI assistant, and is cited in README.md.
"""
import argparse
import os
from collections import deque

from PIL import Image


def make_transparent(img, tolerance):
    img = img.convert("RGBA")
    px = img.load()
    bg = px[0, 0]
    w, h = img.size
    if bg[3] == 0:          # already transparent
        return img
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if (abs(r - bg[0]) <= tolerance and abs(g - bg[1]) <= tolerance
                    and abs(b - bg[2]) <= tolerance):
                px[x, y] = (0, 0, 0, 0)
    return img


def find_boxes(img, min_size):
    w, h = img.size
    alpha = img.getchannel("A").load()
    seen = [[False] * w for _ in range(h)]
    boxes = []
    for y in range(h):
        for x in range(w):
            if seen[y][x] or alpha[x, y] == 0:
                continue
            q = deque([(x, y)])
            seen[y][x] = True
            x0 = x1 = x
            y0 = y1 = y
            while q:
                cx, cy = q.popleft()
                x0, x1 = min(x0, cx), max(x1, cx)
                y0, y1 = min(y0, cy), max(y1, cy)
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if (0 <= nx < w and 0 <= ny < h and not seen[ny][nx]
                                and alpha[nx, ny] != 0):
                            seen[ny][nx] = True
                            q.append((nx, ny))
            if x1 - x0 + 1 >= min_size and y1 - y0 + 1 >= min_size:
                boxes.append((x0, y0, x1 + 1, y1 + 1))
    boxes.sort(key=lambda b: (b[1] // 8, b[0]))   # rough reading order
    return boxes


def main():
    p = argparse.ArgumentParser()
    p.add_argument("sheet")
    p.add_argument("out_dir")
    p.add_argument("--tolerance", type=int, default=10)
    p.add_argument("--min-size", type=int, default=4)
    a = p.parse_args()

    img = make_transparent(Image.open(a.sheet), a.tolerance)
    os.makedirs(a.out_dir, exist_ok=True)
    boxes = find_boxes(img, a.min_size)
    for i, box in enumerate(boxes):
        img.crop(box).save(os.path.join(a.out_dir, f"sprite_{i:03d}.png"))
    print(f"Saved {len(boxes)} sprites to {a.out_dir}")


if __name__ == "__main__":
    main()
