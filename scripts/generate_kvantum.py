#!/usr/bin/env python3
"""
Galaxy Theme KDE - Kvantum Theme Generator
Author:  badcast <lmecomposer@gmail.com>
Project: Galaxy Theme KDE

Adapts the KvMojave layout, translucency, frame metrics, and components
into the Galaxy Cosmic Dark design aesthetic.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KVANTUM_DIR = os.path.join(BASE_DIR, "Kvantum", "Galaxy-Dark")

# Base template paths
SRC_KVCONFIG = "/usr/share/Kvantum/KvMojave/KvMojave.kvconfig"
SRC_SVG = "/usr/share/Kvantum/KvMojave/KvMojave.svg"

# Galaxy Cosmic Palette
C_VOID_DARK   = "#0B0E17"
C_VOID_MID    = "#0F1426"
C_VOID_CARD   = "#1A2238"
C_VOID_BORDER = "#2A3558"
C_VOID_BORDER_HI = "#3B4A78"
C_PULSAR_VIO  = "#00F0FF"
C_NEBULA_MAG  = "#00F0FF"
C_STELLAR_CYAN= "#00F0FF"
C_SUPERNOVA_GOLD = "#FBBF24"
C_AURORA_EMERALD = "#10B981"
C_STAR_WHITE  = "#F8FAFC"
C_STARDUST    = "#94A3B8"
C_DANGER_RED  = "#FF4565"

def adapt_kvconfig():
    if not os.path.exists(SRC_KVCONFIG):
        print(f"Error: {SRC_KVCONFIG} not found!")
        return

    with open(SRC_KVCONFIG, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update metadata
    content = re.sub(r'author=.*', 'author=badcast <lmecomposer@gmail.com>', content)
    content = re.sub(r'comment=.*', 'comment=Galaxy Theme KDE - Cosmic dark translucent Kvantum theme for KDE Plasma 6', content)

    # 2. Update [GeneralColors] section
    galaxy_colors = f"""[GeneralColors]
window.color={C_VOID_MID}
inactive.window.color={C_VOID_DARK}
base.color={C_VOID_DARK}f0
inactive.base.color={C_VOID_DARK}fa
alt.base.color={C_VOID_MID}
inactive.alt.base.color={C_VOID_DARK}
button.color={C_VOID_CARD}
light.color={C_VOID_BORDER_HI}
mid.light.color={C_VOID_BORDER}
dark.color={C_VOID_DARK}
mid.color={C_VOID_CARD}
highlight.color={C_PULSAR_VIO}
inactive.highlight.color=#18223C
tooltip.base.color={C_VOID_MID}
text.color={C_STAR_WHITE}
inactive.text.color={C_STARDUST}
window.text.color={C_STAR_WHITE}
inactive.window.text.color={C_STARDUST}
button.text.color={C_STAR_WHITE}
disabled.text.color=#64748B
tooltip.text.color={C_STAR_WHITE}
highlight.text.color=#FFFFFF
inactive.highlight.text.color=#E2E8F0
link.color={C_STELLAR_CYAN}
link.visited.color={C_NEBULA_MAG}
progress.indicator.text.color=#FFFFFF"""

    content = re.sub(r'\[GeneralColors\][\s\S]*?(?=\n\[)', galaxy_colors, content)

    out_path = os.path.join(KVANTUM_DIR, "Galaxy-Dark.kvconfig")
    os.makedirs(KVANTUM_DIR, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {out_path}")

def adapt_svg():
    if not os.path.exists(SRC_SVG):
        print(f"Error: {SRC_SVG} not found!")
        return

    with open(SRC_SVG, "r", encoding="utf-8") as f:
        svg = f.read()

    # Mapping Mojave colors to Galaxy Cosmic palette
    # Case-insensitive replacement dictionary
    color_map = {
        # Deep backgrounds & darks
        "#000356": "#05070D",
        "#141414": "#0B0E17",
        "#1b1b1d": "#0B0E17",
        "#1e1e1e": "#0B0E17",
        "#222224": "#0F1426",
        "#232323": "#0F1426",
        "#262626": "#0F1426",
        "#282828": "#151B2E",
        "#2c2b2a": "#0B0E17",
        "#302f2e": "#0F1426",
        "#303030": "#151B2E",
        "#313237": "#0F1426",
        "#323232": "#151B2E",
        "#333230": "#151B2E",
        "#373739": "#1A2238",
        "#383838": "#1A2238",
        "#393939": "#1A2238",
        "#3c3c3c": "#1A2238",
        "#3d3e43": "#1A2238",
        "#434345": "#242E4C",
        "#454547": "#242E4C",
        "#464646": "#242E4C",
        "#4b4a48": "#242E4C",
        "#4f4e4b": "#242E4C",
        "#505050": "#2A3558",
        "#565c5e": "#2A3558",
        "#575757": "#2A3558",
        "#58585c": "#2A3558",
        "#5a5a5a": "#2A3558",
        "#5b5b5b": "#2A3558",
        "#5f5f5f": "#2A3558",

        # Borders & Outlines
        "#626264": "#2A3558",
        "#646464": "#2A3558",
        "#67676a": "#3B4A78",
        "#6c6c70": "#3B4A78",
        "#6e6e70": "#3B4A78",
        "#727677": "#3B4A78",
        "#737373": "#3B4A78",
        "#76767a": "#3B4A78",
        "#7b7b7b": "#4A5D96",
        "#7d7d7d": "#4A5D96",
        "#828282": "#4A5D96",
        "#8c8c8c": "#64748B",
        "#919191": "#64748B",
        "#969696": "#94A3B8",
        "#9e9ea0": "#94A3B8",
        "#a0a0a0": "#94A3B8",
        "#b1b1b3": "#CBD5E1",
        "#b4b4b4": "#CBD5E1",
        "#c3c3c6": "#E2E8F0",
        "#c8c8c8": "#F1F5F9",

        # macOS Blue Highlights -> Galaxy Pulsar Violet & Stellar Cyan
        "#245fc4": "#1E293B",
        "#2664d0": "#00F0FF",
        "#286adc": "#00F0FF",
        "#295e9f": "#18223C",
        "#31a7e8": "#00F0FF",
        "#3273c3": "#00F0FF",
        "#3daee9": "#00F0FF",
        "#436e99": "#00F0FF",
        "#4478ac": "#00F0FF",
        "#81c0ff": "#00F0FF",
        "#b74aff": "#00F0FF",

        # Status accents
        "#f35059": "#FF4565",
        "#fa2300": "#FF4565",
        "#f8c636": "#FBBF24",
        "#31e84c": "#10B981",
    }

    # Perform accurate regex substitution
    for old_hex, new_hex in color_map.items():
        # Replace case insensitive
        svg = re.sub(re.escape(old_hex), new_hex, svg, flags=re.IGNORECASE)

    out_path = os.path.join(KVANTUM_DIR, "Galaxy-Dark.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {out_path}")

def main():
    print("==========================================")
    print("Adapting KvMojave into Galaxy Cosmic Kvantum Theme")
    print("==========================================")
    adapt_kvconfig()
    adapt_svg()
    print("==========================================")
    print("Galaxy Kvantum Theme successfully created!")
    print("==========================================")

if __name__ == "__main__":
    main()
