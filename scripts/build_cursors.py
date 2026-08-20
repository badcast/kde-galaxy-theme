#!/usr/bin/env python3
"""
Galaxy Theme KDE - Cursor Theme Compiler
Author:  badcast <lmecomposer@gmail.com>
Project: Galaxy Theme KDE

Converts SVG cursor sources to multi-size Xcursor binaries (24, 32, 48, 64px) with full symlinks.
"""

import os
import struct
import subprocess
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "cursors", "Galaxy-Cursors", "src")
OUT_DIR = os.path.join(BASE_DIR, "cursors", "Galaxy-Cursors", "cursors")

SIZES = [24, 32, 48, 64]
XCUR_MAGIC = b'Xcur'
XCUR_TYPE_IMAGE = 0xfffd0002

CURSOR_DEFS = {
    "default": {
        "frames": ["default.svg"],
        "hotspot": (0.12, 0.12),
        "delay": 0,
        "aliases": ["left_ptr", "top_left_arrow", "arrow", "top_left_corner"]
    },
    "pointer": {
        "frames": ["pointer.svg"],
        "hotspot": (0.37, 0.12),
        "delay": 0,
        "aliases": ["hand1", "hand2", "hand", "pointing_hand", "e29285e634086352946a0e7090d73106", "9d800788f1b08800ae810202380a0822"]
    },
    "progress": {
        "frames": [f"progress_{i}.svg" for i in range(8)],
        "hotspot": (0.5, 0.5),
        "delay": 60,
        "aliases": ["left_ptr_watch", "half-busy", "00000000000000020006000e7e9ffc3f", "08e8e1c95fe2fc01f976f1e063a24ccd", "3ecb610c1bf2410f44200f48c40d3599"]
    },
    "wait": {
        "frames": [f"wait_{i}.svg" for i in range(8)],
        "hotspot": (0.5, 0.5),
        "delay": 60,
        "aliases": ["watch", "busy", "spinning"]
    },
    "text": {
        "frames": ["text.svg"],
        "hotspot": (0.5, 0.5),
        "delay": 0,
        "aliases": ["xterm", "ibeam"]
    },
    "crosshair": {
        "frames": ["crosshair.svg"],
        "hotspot": (0.5, 0.5),
        "delay": 0,
        "aliases": ["cross", "tcross"]
    },
    "move": {
        "frames": ["move.svg"],
        "hotspot": (0.5, 0.5),
        "delay": 0,
        "aliases": ["fleur", "all-scroll", "size_all", "4498f0e0c1937ffe01fd06f973665830", "9081237383d90e509aa00f00170e968f"]
    },
    "col-resize": {
        "frames": ["col-resize.svg"],
        "hotspot": (0.5, 0.5),
        "delay": 0,
        "aliases": ["h_double_arrow", "size_hor", "ew-resize", "e-resize", "w-resize", "028006030e0e7ebff47f21fde1c50394"]
    },
    "row-resize": {
        "frames": ["row-resize.svg"],
        "hotspot": (0.5, 0.5),
        "delay": 0,
        "aliases": ["v_double_arrow", "size_ver", "ns-resize", "n-resize", "s-resize", "00008160000006810000408080010102"]
    },
    "not-allowed": {
        "frames": ["not-allowed.svg"],
        "hotspot": (0.5, 0.5),
        "delay": 0,
        "aliases": ["circle", "forbidden", "crossed_circle", "03b6e0fcb3499374a867c041f52298f0"]
    },
    "help": {
        "frames": ["help.svg"],
        "hotspot": (0.12, 0.12),
        "delay": 0,
        "aliases": ["whats_this", "question_arrow", "5c6cd98b3f3ebcb1f9c7f1c204630408", "d9ce0ab605698f320427677b45020460"]
    },
    "pirate": {
        "frames": ["pirate.svg"],
        "hotspot": (0.5, 0.5),
        "delay": 0,
        "aliases": ["cross_reverse", "kill", "xkill", "skull", "pirate_arrow", "X_cursor", "x-cursor", "dnd-no-drop", "d9ce0ab605698f320427677b45020461", "e29285e634086352946a0e7090d73107"]
    }
}

def render_svg_to_png(svg_path, size, png_path):
    cmd = ["rsvg-convert", "-w", str(size), "-h", str(size), svg_path, "-o", png_path]
    subprocess.run(cmd, check=True)

def pack_xcursor(images_data):
    """
    images_data: list of dicts:
    {
        "size": nominal size (e.g. 24),
        "width": width,
        "height": height,
        "xhot": int,
        "yhot": int,
        "delay": int (ms),
        "pixels": bytes (BGRA/ARGB little endian uint32s)
    }
    """
    ntoc = len(images_data)
    header_size = 16
    toc_entry_size = 12
    toc_size = ntoc * toc_entry_size
    offset = header_size + toc_size

    # Build TOC and chunks
    toc_bytes = bytearray()
    chunks_bytes = bytearray()

    for img in images_data:
        chunk_header_size = 36
        img_chunk_size = chunk_header_size + len(img["pixels"])
        
        # TOC entry: type, subtype, position
        toc_bytes += struct.pack("<III", XCUR_TYPE_IMAGE, img["size"], offset)
        
        # Chunk header: header_size, type, subtype, version, width, height, xhot, yhot, delay
        chunk_header = struct.pack(
            "<IIIIIIIII",
            chunk_header_size,
            XCUR_TYPE_IMAGE,
            img["size"],
            1, # version
            img["width"],
            img["height"],
            img["xhot"],
            img["yhot"],
            img["delay"]
        )
        chunks_bytes += chunk_header + img["pixels"]
        offset += img_chunk_size

    header = struct.pack("<4sIII", XCUR_MAGIC, header_size, 1, ntoc)
    return header + toc_bytes + chunks_bytes

def build_cursor(cname, cinfo):
    images_data = []
    tmp_png = os.path.join(OUT_DIR, "tmp.png")

    for size in SIZES:
        for fidx, svg_fname in enumerate(cinfo["frames"]):
            svg_path = os.path.join(SRC_DIR, svg_fname)
            if not os.path.exists(svg_path):
                print(f"Warning: {svg_path} not found")
                continue
            
            render_svg_to_png(svg_path, size, tmp_png)
            im = Image.open(tmp_png).convert("RGBA")
            width, height = im.size
            
            # Convert RGBA to ARGB little-endian (B, G, R, A)
            r, g, b, a = im.split()
            bgra = Image.merge("RGBA", (b, g, r, a))
            pixels = bgra.tobytes()

            xhot = int(width * cinfo["hotspot"][0])
            yhot = int(height * cinfo["hotspot"][1])

            images_data.append({
                "size": size,
                "width": width,
                "height": height,
                "xhot": xhot,
                "yhot": yhot,
                "delay": cinfo["delay"],
                "pixels": pixels
            })

    if os.path.exists(tmp_png):
        os.remove(tmp_png)

    if not images_data:
        print(f"Error: No images generated for {cname}")
        return

    xcur_bytes = pack_xcursor(images_data)
    out_file = os.path.join(OUT_DIR, cname)
    with open(out_file, "wb") as f:
        f.write(xcur_bytes)
    print(f"Compiled Xcursor: {cname} ({len(images_data)} frames across {len(SIZES)} sizes)")

    # Create symlinks / aliases
    for alias in cinfo.get("aliases", []):
        alias_path = os.path.join(OUT_DIR, alias)
        if os.path.lexists(alias_path):
            os.remove(alias_path)
        os.symlink(cname, alias_path)

def main():
    print("==========================================")
    print("Compiling Galaxy Xcursor Theme")
    print("==========================================")
    os.makedirs(OUT_DIR, exist_ok=True)
    for cname, cinfo in CURSOR_DEFS.items():
        build_cursor(cname, cinfo)
    print("==========================================")
    print("Cursor theme successfully compiled!")
    print("==========================================")

if __name__ == "__main__":
    main()
