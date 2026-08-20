#!/usr/bin/env python3
"""
Galaxy Theme KDE - Aurorae Window Decoration Generator (Seamless Cyber-Blade & Quantum Pods)
Author:  badcast <lmecomposer@gmail.com>
Project: Galaxy Theme KDE
Website: https://github.com/badcast/kde-galaxy-theme

Generates a mathematically seamless, flawless Cosmic Cyber-HUD Window Decoration for KDE Plasma 6:
- 100% continuous, zero-slit, zero-tear 1px cyber laser border geometry
- Robust 5-state Quantum Pod Buttons (active, hover, pressed, inactive, inactive-hover)
- High-contrast typography with ethereal starlight cyan title glow
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AURORAE_DEST = os.path.join(BASE_DIR, "aurorae", "themes", "Galaxy-Dark-Aurorae")

# Cosmic Master Palette
C_VOID_ABYSS    = "#060810"
C_VOID_DARK     = "#0B0E17"
C_VOID_MID      = "#0F1426"
C_VOID_CARD     = "#161D36"
C_BORDER_DIM    = "#1C243E"
C_BORDER_MID    = "#253256"
C_BORDER_GLOW   = "#3B4D82"

# Celestial Accents
C_STELLAR_CYAN  = "#00F0FF"
C_PULSAR_VIOLET = "#00F0FF"
C_NEBULA_MAGENTA= "#00F0FF"
C_SUPERNOVA_GOLD= "#FBBF24"
C_AURORA_EMERALD= "#10B981"
C_DANGER_CRIMSON= "#FF2E63"
C_STAR_WHITE    = "#F8FAFC"
C_STARDUST      = "#94A3B8"

def gen_auroraerc():
    os.makedirs(AURORAE_DEST, exist_ok=True)
    rc_content = f"""[General]
Animation=1
HaloActive=false
HaloInactive=false
ActiveFocusedTabColor=0,240,255
ActiveTextColor=248,250,252
ActiveTextShadowColor=0,240,255,100
ActiveUnfocusedTabColor=24,34,60
InactiveFocusedTabColor=15,21,36
InactiveTextColor=148,163,184
InactiveTextShadowColor=0,0,0,180
InactiveUnfocusedTabColor=10,14,24
LeftButtons=
RightButtons=IAX
Shadow=true
TextShadowOffsetX=0
TextShadowOffsetY=1
TitleAlignment=Center
TitleVerticalAlignment=Center
UseTextShadow=true

[Layout]
BorderBottom=1
BorderLeft=1
BorderRight=1
BorderTop=0
PaddingBottom=0
PaddingLeft=0
PaddingRight=0
PaddingTop=0
TitleBorderLeft=8
TitleBorderRight=8
TitleEdgeBottom=0
TitleEdgeBottomMaximized=0
TitleEdgeLeft=8
TitleEdgeLeftMaximized=4
TitleEdgeRight=8
TitleEdgeRightMaximized=4
TitleEdgeTop=0
TitleEdgeTopMaximized=0
TitleHeight=32
TitleHeightMaximized=32
ButtonHeight=22
ButtonWidth=22
ButtonSpacing=6
ButtonMarginTop=5
"""
    rc_path = os.path.join(AURORAE_DEST, "Galaxy-Dark-Auroraerc")
    with open(rc_path, "w", encoding="utf-8") as f:
        f.write(rc_content.strip() + "\n")
    print(f"Generated: {rc_path}")

def gen_decoration_svg():
    """
    Generates a 100% mathematically seamless 9-slice Aurorae decoration SVG (240x130).
    Grid: Left col=16, Center col=80, Right col=16 | Top row=32, Center row=60, Bottom row=1.
    All strokes, arcs and anchors align with 0.0px error.
    """
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="240" height="130" viewBox="0 0 240 130">
  <defs>
    <!-- Active Titlebar Fill -->
    <linearGradient id="activeTitleGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#18223C"/>
      <stop offset="100%" stop-color="#0F1626"/>
    </linearGradient>

    <!-- Inactive Titlebar Fill -->
    <linearGradient id="inactiveTitleGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0F1524"/>
      <stop offset="100%" stop-color="#090C14"/>
    </linearGradient>
  </defs>

  <!-- Stretch borders hint: tells KWin to stretch top/bottom/left/right instead of repeating (tiling) -->
  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>

  <!-- ============================================================== -->
  <!-- 1. ACTIVE NORMAL WINDOW (x=0..112, y=0..93)                     -->
  <!-- ============================================================== -->
  <g id="decoration-topleft">
    <rect x="0" y="0" width="16" height="32" fill="url(#activeTitleGrad)"/>
    <path d="M 0.5 32 L 0.5 8 A 7.5 7.5 0 0 1 8 0.5 L 16 0.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>
    <line x1="0" y1="31.5" x2="16" y2="31.5" stroke="#0B0E17" stroke-width="1.0"/>
  </g>

  <g id="decoration-top">
    <rect x="16" y="0" width="80" height="32" fill="url(#activeTitleGrad)"/>
    <line x1="16" y1="0.5" x2="96" y2="0.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>
    <line x1="16" y1="31.5" x2="96" y2="31.5" stroke="#0B0E17" stroke-width="1.0"/>
  </g>

  <g id="decoration-topright">
    <rect x="96" y="0" width="16" height="32" fill="url(#activeTitleGrad)"/>
    <path d="M 96 0.5 L 104 0.5 A 7.5 7.5 0 0 1 111.5 8 L 111.5 32" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>
    <line x1="96" y1="31.5" x2="112" y2="31.5" stroke="#0B0E17" stroke-width="1.0"/>
  </g>

  <g id="decoration-left">
    <rect x="0" y="32" width="16" height="60" fill="none"/>
    <line x1="0.5" y1="32" x2="0.5" y2="92" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>
  </g>

  <g id="decoration-center">
    <rect x="16" y="32" width="80" height="60" fill="none"/>
  </g>

  <g id="decoration-right">
    <rect x="96" y="32" width="16" height="60" fill="none"/>
    <line x1="111.5" y1="32" x2="111.5" y2="92" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>
  </g>

  <g id="decoration-bottomleft">
    <rect x="0" y="92" width="16" height="1" fill="{C_STELLAR_CYAN}"/>
  </g>

  <g id="decoration-bottom">
    <rect x="16" y="92" width="80" height="1" fill="{C_STELLAR_CYAN}"/>
  </g>

  <g id="decoration-bottomright">
    <rect x="96" y="92" width="16" height="1" fill="{C_STELLAR_CYAN}"/>
  </g>

  <!-- ============================================================== -->
  <!-- 2. ACTIVE MAXIMIZED WINDOW (x=0..112, y=96..128)               -->
  <!-- ============================================================== -->
  <g id="decoration-maximized-topleft">
    <rect x="0" y="96" width="16" height="32" fill="url(#activeTitleGrad)"/>
    <line x1="0" y1="96.5" x2="16" y2="96.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>
    <line x1="0" y1="127.5" x2="16" y2="127.5" stroke="#0B0E17" stroke-width="1.0"/>
  </g>
  <g id="decoration-maximized-top">
    <rect x="16" y="96" width="80" height="32" fill="url(#activeTitleGrad)"/>
    <line x1="16" y1="96.5" x2="96" y2="96.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>
    <line x1="16" y1="127.5" x2="96" y2="127.5" stroke="#0B0E17" stroke-width="1.0"/>
  </g>
  <g id="decoration-maximized-topright">
    <rect x="96" y="96" width="16" height="32" fill="url(#activeTitleGrad)"/>
    <line x1="96" y1="96.5" x2="112" y2="96.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>
    <line x1="96" y1="127.5" x2="112" y2="127.5" stroke="#0B0E17" stroke-width="1.0"/>
  </g>

  <!-- ============================================================== -->
  <!-- 3. INACTIVE NORMAL WINDOW (x=120..232, y=0..93)               -->
  <!-- ============================================================== -->
  <g id="decoration-inactive-topleft">
    <rect x="120" y="0" width="16" height="32" fill="url(#inactiveTitleGrad)"/>
    <path d="M 120.5 32 L 120.5 8 A 7.5 7.5 0 0 1 128 0.5 L 136 0.5" fill="none" stroke="#2A3558" stroke-width="1.0"/>
    <line x1="120" y1="31.5" x2="136" y2="31.5" stroke="#05070D" stroke-width="1.0"/>
  </g>

  <g id="decoration-inactive-top">
    <rect x="136" y="0" width="80" height="32" fill="url(#inactiveTitleGrad)"/>
    <line x1="136" y1="0.5" x2="216" y2="0.5" stroke="#2A3558" stroke-width="1.0"/>
    <line x1="136" y1="31.5" x2="216" y2="31.5" stroke="#05070D" stroke-width="1.0"/>
  </g>

  <g id="decoration-inactive-topright">
    <rect x="216" y="0" width="16" height="32" fill="url(#inactiveTitleGrad)"/>
    <path d="M 216 0.5 L 224 0.5 A 7.5 7.5 0 0 1 231.5 8 L 231.5 32" fill="none" stroke="#2A3558" stroke-width="1.0"/>
    <line x1="216" y1="31.5" x2="232" y2="31.5" stroke="#05070D" stroke-width="1.0"/>
  </g>

  <g id="decoration-inactive-left">
    <rect x="120" y="32" width="16" height="60" fill="none"/>
    <line x1="120.5" y1="32" x2="120.5" y2="92" stroke="#2A3558" stroke-width="1.0"/>
  </g>

  <g id="decoration-inactive-center">
    <rect x="136" y="32" width="80" height="60" fill="none"/>
  </g>

  <g id="decoration-inactive-right">
    <rect x="216" y="32" width="16" height="60" fill="none"/>
    <line x1="231.5" y1="32" x2="231.5" y2="92" stroke="#2A3558" stroke-width="1.0"/>
  </g>

  <g id="decoration-inactive-bottomleft">
    <rect x="120" y="92" width="16" height="1" fill="#2A3558"/>
  </g>

  <g id="decoration-inactive-bottom">
    <rect x="136" y="92" width="80" height="1" fill="#2A3558"/>
  </g>

  <g id="decoration-inactive-bottomright">
    <rect x="216" y="92" width="16" height="1" fill="#2A3558"/>
  </g>

  <!-- ============================================================== -->
  <!-- 4. INACTIVE MAXIMIZED WINDOW (x=120..232, y=96..128)         -->
  <!-- ============================================================== -->
  <g id="decoration-inactive-maximized-topleft">
    <rect x="120" y="96" width="16" height="32" fill="url(#inactiveTitleGrad)"/>
    <line x1="120" y1="96.5" x2="136" y2="96.5" stroke="#2A3558" stroke-width="1.0"/>
    <line x1="120" y1="127.5" x2="136" y2="127.5" stroke="#05070D" stroke-width="1.0"/>
  </g>
  <g id="decoration-inactive-maximized-top">
    <rect x="136" y="96" width="80" height="32" fill="url(#inactiveTitleGrad)"/>
    <line x1="136" y1="96.5" x2="216" y2="96.5" stroke="#2A3558" stroke-width="1.0"/>
    <line x1="136" y1="127.5" x2="216" y2="127.5" stroke="#05070D" stroke-width="1.0"/>
  </g>
  <g id="decoration-inactive-maximized-topright">
    <rect x="216" y="96" width="16" height="32" fill="url(#inactiveTitleGrad)"/>
    <line x1="216" y1="96.5" x2="232" y2="96.5" stroke="#2A3558" stroke-width="1.0"/>
    <line x1="216" y1="127.5" x2="232" y2="127.5" stroke="#05070D" stroke-width="1.0"/>
  </g>

  <!-- ============================================================== -->
  <!-- 5. COMPOSITOR WINDOW MASKS ('mask-*')                         -->
  <!-- ============================================================== -->
  <g id="mask-topleft">
    <path d="M 0 32 L 0 8 A 8 8 0 0 1 8 0 L 16 0 L 16 32 Z" fill="#FFFFFF"/>
  </g>
  <g id="mask-top">
    <rect x="16" y="0" width="80" height="32" fill="#FFFFFF"/>
  </g>
  <g id="mask-topright">
    <path d="M 96 0 L 104 0 A 8 8 0 0 1 112 8 L 112 32 L 96 32 Z" fill="#FFFFFF"/>
  </g>
  <g id="mask-left">
    <rect x="0" y="32" width="16" height="60" fill="#FFFFFF"/>
  </g>
  <g id="mask-center">
    <rect x="16" y="32" width="80" height="60" fill="#FFFFFF"/>
  </g>
  <g id="mask-right">
    <rect x="96" y="32" width="16" height="60" fill="#FFFFFF"/>
  </g>
  <g id="mask-bottomleft">
    <rect x="0" y="92" width="16" height="1" fill="#FFFFFF"/>
  </g>
  <g id="mask-bottom">
    <rect x="16" y="92" width="80" height="1" fill="#FFFFFF"/>
  </g>
  <g id="mask-bottomright">
    <rect x="96" y="92" width="16" height="1" fill="#FFFFFF"/>
  </g>
</svg>
'''
    dest_path = os.path.join(AURORAE_DEST, "decoration.svg")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip() + "\n")
    print(f"Generated: {dest_path}")

def gen_cyber_pod_button_svg(filename, core_color, glow_color, accent_color, glyph_func):
    """
    Generates a high-tech Cyber-Squircle Quantum Pod Button (110x22, 5 states of 22x22):
    - 1. active: Sleek cosmic pod with luminous neon border and high-contrast glyph
    - 2. hover: Polished glowing glass pod with starlight sheen and bright core
    - 3. pressed: Compressed dark matter singularity pod
    - 4. inactive: Stealthed deep space stasis pod
    - 5. deactivated: Subdued starlight silhouette
    """
    name_clean = filename.replace('.svg', '').replace('-', '_')
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="110" height="22" viewBox="0 0 110 22">
  <defs>
    <!-- Cyber Pod Active Background -->
    <linearGradient id="podBg_{name_clean}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_VOID_CARD}"/>
      <stop offset="100%" stop-color="{C_VOID_DARK}"/>
    </linearGradient>

    <!-- Cyber Pod Active Border -->
    <linearGradient id="podBorder_{name_clean}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{core_color}"/>
      <stop offset="100%" stop-color="{accent_color}"/>
    </linearGradient>
  </defs>

  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>

  <!-- ========================================== -->
  <!-- 1. ACTIVE STATE (x=0..22, center=11)       -->
  <!-- ========================================== -->
  <g id="active-center">
    <rect x="0" y="0" width="22" height="22" fill="none"/>
    <!-- Deep Space Drop Shadow -->
    <rect x="1.5" y="2.5" width="19" height="19" rx="5" fill="#000000" opacity="0.4"/>
    <!-- Cosmic Squircle Pod Capsule -->
    <rect x="1.5" y="1.5" width="19" height="19" rx="5" fill="url(#podBg_{name_clean})" stroke="url(#podBorder_{name_clean})" stroke-width="1.2"/>
    <!-- Specular Inner Glass Rim -->
    <rect x="2.5" y="2.5" width="17" height="17" rx="4" fill="none" stroke="{C_STAR_WHITE}" stroke-opacity="0.14" stroke-width="0.8"/>
    <!-- Illuminated Quantum Glyph -->
    {glyph_func(11, 11, core_color, C_STAR_WHITE, 1.3, False)}
  </g>

  <!-- ========================================== -->
  <!-- 2. HOVER STATE (x=22..44, center=33)       -->
  <!-- ========================================== -->
  <g id="hover-center">
    <rect x="22" y="0" width="22" height="22" fill="none"/>
    <!-- Radiant Glowing Laser Pod -->
    <rect x="23.5" y="1.5" width="19" height="19" rx="5" fill="{glow_color}" fill-opacity="0.28" stroke="{C_STAR_WHITE}" stroke-width="1.4"/>
    <rect x="24.5" y="2.5" width="17" height="17" rx="4" fill="none" stroke="{core_color}" stroke-width="0.9" opacity="0.75"/>
    <!-- Luminous White-Hot Glyph -->
    {glyph_func(33, 11, C_STAR_WHITE, C_STAR_WHITE, 1.5, True)}
  </g>

  <!-- ========================================== -->
  <!-- 3. PRESSED STATE (x=44..66, center=55)     -->
  <!-- ========================================== -->
  <g id="pressed-center">
    <rect x="44" y="0" width="22" height="22" fill="none"/>
    <!-- Compressed Dark Matter Singularity Pod -->
    <rect x="46.0" y="2.5" width="17" height="17" rx="4" fill="{C_VOID_ABYSS}" stroke="{core_color}" stroke-width="1.4"/>
    <!-- Compressed Glyph -->
    {glyph_func(54.5, 11, glow_color, glow_color, 1.1, False)}
  </g>

  <!-- ========================================== -->
  <!-- 4. INACTIVE STATE (x=66..88, center=77)   -->
  <!-- ========================================== -->
  <g id="inactive-center">
    <rect x="66" y="0" width="22" height="22" fill="none"/>
    <!-- Stealthed Dark Stasis Pod -->
    <rect x="67.5" y="1.5" width="19" height="19" rx="5" fill="{C_VOID_ABYSS}" fill-opacity="0.6" stroke="{C_BORDER_DIM}" stroke-width="1.0"/>
    <!-- Muted Stardust Glyph -->
    {glyph_func(77, 11, C_STARDUST, C_STARDUST, 0.9, False, opacity=0.45)}
  </g>

  <!-- ========================================== -->
  <!-- 5. DEACTIVATED & INACTIVE HOVER (x=88..110) -->
  <!-- ========================================== -->
  <g id="deactivated-active-center">
    <rect x="88" y="0" width="22" height="22" fill="none"/>
    <rect x="89.5" y="1.5" width="19" height="19" rx="5" fill="{core_color}" fill-opacity="0.15" stroke="{C_BORDER_MID}" stroke-width="1.0"/>
    {glyph_func(99, 11, C_STARDUST, C_STARDUST, 0.9, False, opacity=0.6)}
  </g>
  <g id="deactivated-center">
    <rect x="88" y="0" width="22" height="22" fill="none"/>
    <rect x="89.5" y="1.5" width="19" height="19" rx="5" fill="{core_color}" fill-opacity="0.15" stroke="{C_BORDER_MID}" stroke-width="1.0"/>
    {glyph_func(99, 11, C_STARDUST, C_STARDUST, 0.9, False, opacity=0.6)}
  </g>
  <g id="inactive_hover-center">
    <rect x="88" y="0" width="22" height="22" fill="none"/>
    <rect x="89.5" y="1.5" width="19" height="19" rx="5" fill="{core_color}" fill-opacity="0.15" stroke="{C_BORDER_MID}" stroke-width="1.0"/>
    {glyph_func(99, 11, C_STARDUST, C_STARDUST, 0.9, False, opacity=0.6)}
  </g>
  <g id="hover-inactive-center">
    <rect x="88" y="0" width="22" height="22" fill="none"/>
    <rect x="89.5" y="1.5" width="19" height="19" rx="5" fill="{core_color}" fill-opacity="0.15" stroke="{C_BORDER_MID}" stroke-width="1.0"/>
    {glyph_func(99, 11, C_STARDUST, C_STARDUST, 0.9, False, opacity=0.6)}
  </g>
</svg>
'''
    dest_path = os.path.join(AURORAE_DEST, filename)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip() + "\n")
    print(f"Generated: {dest_path}")

# ==========================================
# GLYPH DEFINITIONS (Quantum Vector Art)
# ==========================================

def glyph_close(cx, cy, stroke_col, fill_col, sw, is_hover, opacity=1.0):
    dot = f'<circle cx="{cx}" cy="{cy}" r="1.3" fill="{fill_col}"/>' if is_hover else ''
    return f'''<g opacity="{opacity}">
      <line x1="{cx-3.2}" y1="{cy-3.2}" x2="{cx+3.2}" y2="{cy+3.2}" stroke="{stroke_col}" stroke-width="{sw}" stroke-linecap="round"/>
      <line x1="{cx+3.2}" y1="{cy-3.2}" x2="{cx-3.2}" y2="{cy+3.2}" stroke="{stroke_col}" stroke-width="{sw}" stroke-linecap="round"/>
      {dot}
    </g>'''

def glyph_maximize(cx, cy, stroke_col, fill_col, sw, is_hover, opacity=1.0):
    dot = f'<circle cx="{cx}" cy="{cy}" r="1.2" fill="{fill_col}"/>' if is_hover else ''
    return f'''<g opacity="{opacity}">
      <rect x="{cx-3.5}" y="{cy-3.5}" width="7" height="7" rx="1.5" fill="none" stroke="{stroke_col}" stroke-width="{sw}"/>
      {dot}
    </g>'''

def glyph_minimize(cx, cy, stroke_col, fill_col, sw, is_hover, opacity=1.0):
    dot = f'<circle cx="{cx}" cy="{cy}" r="1.5" fill="{fill_col}"/>' if is_hover else ''
    return f'''<g opacity="{opacity}">
      <line x1="{cx-3.8}" y1="{cy}" x2="{cx+3.8}" y2="{cy}" stroke="{stroke_col}" stroke-width="{sw+0.3}" stroke-linecap="round"/>
      {dot}
    </g>'''

def glyph_restore(cx, cy, stroke_col, fill_col, sw, is_hover, opacity=1.0):
    return f'''<g opacity="{opacity}">
      <rect x="{cx-1.8}" y="{cy-3.8}" width="5.4" height="5.4" rx="1.2" fill="none" stroke="{stroke_col}" stroke-width="{sw*0.9}"/>
      <rect x="{cx-3.8}" y="{cy-1.8}" width="5.4" height="5.4" rx="1.2" fill="{C_VOID_CARD}" stroke="{stroke_col}" stroke-width="{sw*0.9}"/>
    </g>'''

def glyph_alldesktops(cx, cy, stroke_col, fill_col, sw, is_hover, opacity=1.0):
    return f'''<g opacity="{opacity}">
      <ellipse cx="{cx}" cy="{cy}" rx="4.8" ry="1.8" fill="none" stroke="{stroke_col}" stroke-width="{sw*0.9}" transform="rotate(-25 {cx} {cy})"/>
      <circle cx="{cx}" cy="{cy}" r="2.0" fill="{fill_col}"/>
    </g>'''

def glyph_keepabove(cx, cy, stroke_col, fill_col, sw, is_hover, opacity=1.0):
    return f'''<g opacity="{opacity}">
      <polyline points="{cx-3.2},{cy+1.8} {cx},{cy-2.2} {cx+3.2},{cy+1.8}" fill="none" stroke="{stroke_col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''

def glyph_keepbelow(cx, cy, stroke_col, fill_col, sw, is_hover, opacity=1.0):
    return f'''<g opacity="{opacity}">
      <polyline points="{cx-3.2},{cy-1.8} {cx},{cy+2.2} {cx+3.2},{cy-1.8}" fill="none" stroke="{stroke_col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''

def glyph_help(cx, cy, stroke_col, fill_col, sw, is_hover, opacity=1.0):
    return f'''<g opacity="{opacity}">
      <text x="{cx}" y="{cy+3.2}" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="{stroke_col}" text-anchor="middle">?</text>
    </g>'''

def main():
    print("==========================================")
    print("Generating Galaxy Seamless Aurorae Window Decoration")
    print("==========================================")
    gen_auroraerc()
    gen_decoration_svg()

    # Quantum Pod Buttons (Unified Cyber-HUD Architecture):
    # 1. Close: Supernova Crimson (#FF2E63 core, #FF0055 glow, #E11D48 accent)
    gen_cyber_pod_button_svg("close.svg", C_DANGER_CRIMSON, "#FF0055", "#E11D48", glyph_close)

    # 2. Maximize: Stellar Cyan Quasar (#00F0FF core, #38BDF8 glow, #0284C7 accent)
    gen_cyber_pod_button_svg("maximize.svg", C_STELLAR_CYAN, "#38BDF8", "#0284C7", glyph_maximize)

    # 3. Minimize: Nebula Magenta Nova (#00F0FF core, #38BDF8 glow, #0F1626 accent)
    gen_cyber_pod_button_svg("minimize.svg", C_NEBULA_MAGENTA, "#38BDF8", "#0F1626", glyph_minimize)

    # 4. Restore: Stellar Cyan Binary (#00F0FF core, #38BDF8 glow, #0284C7 accent)
    gen_cyber_pod_button_svg("restore.svg", C_STELLAR_CYAN, "#38BDF8", "#0284C7", glyph_restore)

    # 5. AllDesktops: Pulsar Violet Planetary Compass (#00F0FF core, #38BDF8 glow, #18223C accent)
    gen_cyber_pod_button_svg("alldesktops.svg", C_PULSAR_VIOLET, "#38BDF8", "#18223C", glyph_alldesktops)

    # 6. KeepAbove / KeepBelow: Plasma Warp Vectors
    gen_cyber_pod_button_svg("keepabove.svg", C_STELLAR_CYAN, "#38BDF8", "#0284C7", glyph_keepabove)
    gen_cyber_pod_button_svg("keepbelow.svg", C_PULSAR_VIOLET, "#38BDF8", "#18223C", glyph_keepbelow)

    # 7. Help: Supernova Gold Star Oracle (#FBBF24 core, #FDE047 glow, #D97706 accent)
    gen_cyber_pod_button_svg("help.svg", C_SUPERNOVA_GOLD, "#FDE047", "#D97706", glyph_help)

    # metadata.json for KDE Plasma 6
    meta_json = f"""{{
    "KPlugin": {{
        "Authors": [
            {{
                "Email": "lmecomposer@gmail.com",
                "Name": "badcast"
            }}
        ],
        "Category": "Window Decoration",
        "Description": "Galaxy Theme KDE - Seamless Cosmic Quantum Pod & Astral Blade Window Decoration for KDE Plasma 6",
        "Id": "Galaxy-Dark-Aurorae",
        "License": "GPL-3.0+",
        "Name": "Galaxy Theme KDE Aurorae",
        "Version": "4.1.0",
        "Website": "https://github.com/badcast/kde-galaxy-theme"
    }}
}}"""
    with open(os.path.join(AURORAE_DEST, "metadata.json"), "w", encoding="utf-8") as f:
        f.write(meta_json.strip() + "\n")

    print("==========================================")
    print("Galaxy Seamless Aurorae Theme Generated Successfully!")
    print("==========================================")

if __name__ == "__main__":
    main()


