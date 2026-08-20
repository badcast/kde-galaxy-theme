#!/usr/bin/env python3
"""
Galaxy Theme KDE - Asset Generator for KDE Plasma 6
Author:  badcast <lmecomposer@gmail.com>
Project: Galaxy Theme KDE

Generates high quality SVG assets for:
- Plasma 6 Desktop Theme (widgets, dialogs, icons, bar_meters, sliders, full-height tasks with distinct open/active states)
- Aurorae Window Decorations
- FreeDesktop/KDE SVG Icons (places, apps, actions, categories, devices, mimetypes, status)
- Xcursor SVG sources (with rich drop shadows and high-contrast dark contours)
- Splash screen graphics
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLASMA_DIR = os.path.join(BASE_DIR, "plasma", "desktoptheme", "Galaxy-Dark")
AURORAE_DIR = os.path.join(BASE_DIR, "aurorae", "themes", "Galaxy-Dark-Aurorae")
ICONS_DIR = os.path.join(BASE_DIR, "icons", "Galaxy-Icons", "scalable")
CURSORS_DIR = os.path.join(BASE_DIR, "cursors", "Galaxy-Cursors", "src")
SPLASH_DIR = os.path.join(BASE_DIR, "look-and-feel", "org.galaxy.desktop", "contents", "splash", "images")

# Cosmic Palette
C_VOID_DARK   = "#0B0E17"
C_VOID_MID    = "#0F1426"
C_VOID_CARD   = "#1A2238"
C_VOID_BORDER = "#2A3558"
C_PULSAR_VIO  = "#00F0FF"
C_NEBULA_MAG  = "#00F0FF"
C_STELLAR_CYAN= "#00F0FF"
C_SUPERNOVA_GOLD = "#FBBF24"
C_AURORA_EMERALD = "#10B981"
C_STAR_WHITE  = "#F8FAFC"
C_STARDUST    = "#94A3B8"
C_DANGER_RED  = "#FF4565"

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {os.path.relpath(path, BASE_DIR)}")

# ==========================================
# 1. PLASMA 6 DESKTOP THEME WIDGETS
# ==========================================

def gen_plasma_panel_background():
    # Seamless 9-slice Plasma 6 Panel Background with uniform solid obsidian glass and crisp 1px borders
    # Zero diagonal gradient seams, zero corner distortion on resize
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 80 80">
  <defs>
    <linearGradient id="topGlowLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="{C_STELLAR_CYAN}" stop-opacity="0.8"/>
    </linearGradient>
  </defs>

  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>
  <rect id="hint-tile-center" x="6" y="6" width="68" height="68" fill="none"/>
  <rect id="hint-top-margin" x="0" y="0" width="80" height="6" fill="none"/>
  <rect id="hint-bottom-margin" x="0" y="74" width="80" height="6" fill="none"/>
  <rect id="hint-left-margin" x="0" y="0" width="6" height="80" fill="none"/>
  <rect id="hint-right-margin" x="74" y="0" width="6" height="80" fill="none"/>

  <!-- Center Tile (Uniform Solid Obsidian Dark) -->
  <g id="center">
    <rect x="6" y="6" width="68" height="68" fill="{C_VOID_MID}" fill-opacity="0.94"/>
  </g>

  <!-- Top-Left Corner (Rounded 6px) -->
  <g id="topleft">
    <path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_MID}" fill-opacity="0.94"/>
    <path d="M 0 6 A 6 6 0 0 1 6 0" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.0" stroke-opacity="0.8"/>
  </g>

  <!-- Top Border with Starlight Highlight Line -->
  <g id="top">
    <rect x="6" y="0" width="68" height="6" fill="{C_VOID_MID}" fill-opacity="0.94"/>
    <line x1="6" y1="0.5" x2="74" y2="0.5" stroke="url(#topGlowLine)" stroke-width="1.0"/>
  </g>

  <!-- Top-Right Corner (Rounded 6px) -->
  <g id="topright">
    <path d="M 74 0 A 6 6 0 0 1 80 6 L 74 6 Z" fill="{C_VOID_MID}" fill-opacity="0.94"/>
    <path d="M 74 0 A 6 6 0 0 1 80 6" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.0" stroke-opacity="0.8"/>
  </g>

  <!-- Left 1px Border -->
  <g id="left">
    <rect x="0" y="6" width="6" height="68" fill="{C_VOID_MID}" fill-opacity="0.94"/>
    <line x1="0.5" y1="6" x2="0.5" y2="74" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>

  <!-- Right 1px Border -->
  <g id="right">
    <rect x="74" y="6" width="6" height="68" fill="{C_VOID_MID}" fill-opacity="0.94"/>
    <line x1="79.5" y1="6" x2="79.5" y2="74" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>

  <!-- Bottom-Left Corner -->
  <g id="bottomleft">
    <path d="M 6 80 A 6 6 0 0 1 0 74 L 6 74 Z" fill="{C_VOID_MID}" fill-opacity="0.94"/>
    <path d="M 6 80 A 6 6 0 0 1 0 74" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>

  <!-- Bottom 1px Border -->
  <g id="bottom">
    <rect x="6" y="74" width="68" height="6" fill="{C_VOID_MID}" fill-opacity="0.94"/>
    <line x1="6" y1="79.5" x2="74" y2="79.5" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>

  <!-- Bottom-Right Corner -->
  <g id="bottomright">
    <path d="M 80 74 A 6 6 0 0 1 74 80 L 74 74 Z" fill="{C_VOID_MID}" fill-opacity="0.94"/>
    <path d="M 80 74 A 6 6 0 0 1 74 80" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>

  <!-- Shadow Group (Subtle outer drop-shadow) -->
  <rect id="shadow-center" x="6" y="6" width="68" height="68" fill="none"/>
  <rect id="shadow-top" x="6" y="0" width="68" height="6" fill="none"/>
  <rect id="shadow-bottom" x="6" y="74" width="68" height="6" fill="none"/>
  <rect id="shadow-left" x="0" y="6" width="6" height="68" fill="none"/>
  <rect id="shadow-right" x="74" y="6" width="6" height="68" fill="none"/>
  <rect id="shadow-topleft" x="0" y="0" width="6" height="6" fill="none"/>
  <rect id="shadow-topright" x="74" y="0" width="6" height="6" fill="none"/>
  <rect id="shadow-bottomleft" x="0" y="74" width="6" height="6" fill="none"/>
  <rect id="shadow-bottomright" x="74" y="74" width="6" height="6" fill="none"/>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "panel-background.svg"), svg)
    write_file(os.path.join(PLASMA_DIR, "widgets", "background.svg"), svg)
    write_file(os.path.join(PLASMA_DIR, "dialogs", "background.svg"), svg)

def gen_plasma_tasks():
    # Plasma 6 Task Manager widget - Clean, stretch-proof 9-slice cards
    # Full-width indicator lines that never distort into ovals when task buttons stretch horizontally
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="360" height="240" viewBox="0 0 360 240">
  <defs>
    <!-- Starlight Focus LED Bar -->
    <linearGradient id="focusLed" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}"/>
      <stop offset="100%" stop-color="{C_STELLAR_CYAN}"/>
    </linearGradient>
  </defs>

  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>

  <!-- MARGIN HINTS (Uniform 6px on all 4 sides) -->
  <rect id="normal-hint-top-margin" x="0" y="0" width="60" height="6" fill="none"/>
  <rect id="normal-hint-bottom-margin" x="0" y="54" width="60" height="6" fill="none"/>
  <rect id="normal-hint-left-margin" x="0" y="0" width="6" height="60" fill="none"/>
  <rect id="normal-hint-right-margin" x="54" y="0" width="6" height="60" fill="none"/>

  <rect id="focus-hint-top-margin" x="60" y="0" width="60" height="6" fill="none"/>
  <rect id="focus-hint-bottom-margin" x="60" y="54" width="60" height="6" fill="none"/>
  <rect id="focus-hint-left-margin" x="60" y="0" width="6" height="60" fill="none"/>
  <rect id="focus-hint-right-margin" x="114" y="0" width="6" height="60" fill="none"/>

  <rect id="hover-hint-top-margin" x="120" y="0" width="60" height="6" fill="none"/>
  <rect id="hover-hint-bottom-margin" x="120" y="54" width="60" height="6" fill="none"/>
  <rect id="hover-hint-left-margin" x="120" y="0" width="6" height="60" fill="none"/>
  <rect id="hover-hint-right-margin" x="174" y="0" width="6" height="60" fill="none"/>

  <rect id="minimized-hint-top-margin" x="180" y="0" width="60" height="6" fill="none"/>
  <rect id="minimized-hint-bottom-margin" x="180" y="54" width="60" height="6" fill="none"/>
  <rect id="minimized-hint-left-margin" x="180" y="0" width="6" height="60" fill="none"/>
  <rect id="minimized-hint-right-margin" x="234" y="0" width="6" height="60" fill="none"/>

  <!-- ========================================== -->
  <!-- 1. NORMAL STATE (Open Inactive Running App)-->
  <!-- ========================================== -->
  <g id="normal-center"><rect x="6" y="6" width="48" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="normal-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/><path d="M 0 6 A 6 6 0 0 1 6 0" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0" stroke-opacity="0.3"/></g>
  <g id="normal-top"><rect x="6" y="0" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.25"/><line x1="6" y1="0.5" x2="54" y2="0.5" stroke="{C_VOID_BORDER}" stroke-width="1.0" stroke-opacity="0.3"/></g>
  <g id="normal-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/><path d="M 54 0 A 6 6 0 0 1 60 6" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0" stroke-opacity="0.3"/></g>
  <g id="normal-left"><rect x="0" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/><line x1="0.5" y1="6" x2="0.5" y2="54" stroke="{C_VOID_BORDER}" stroke-width="1.0" stroke-opacity="0.3"/></g>
  <g id="normal-right"><rect x="54" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/><line x1="59.5" y1="6" x2="59.5" y2="54" stroke="{C_VOID_BORDER}" stroke-width="1.0" stroke-opacity="0.3"/></g>
  <g id="normal-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/><path d="M 6 60 A 6 6 0 0 1 0 54" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0" stroke-opacity="0.3"/></g>
  <g id="normal-bottom">
    <rect x="6" y="54" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.25"/>
    <line x1="6" y1="59.5" x2="54" y2="59.5" stroke="{C_VOID_BORDER}" stroke-width="1.0" stroke-opacity="0.3"/>
    <!-- Stretch-proof LED Running Indicator Line -->
    <line x1="6" y1="58.5" x2="54" y2="58.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.5" stroke-opacity="0.5"/>
  </g>
  <g id="normal-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/><path d="M 60 54 A 6 6 0 0 1 54 60" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0" stroke-opacity="0.3"/></g>

  <!-- Directional normal states (North, West, East) -->
  <g id="north-normal-center"><rect x="6" y="6" width="48" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="north-normal-top"><rect x="6" y="0" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.25"/><line x1="6" y1="1.5" x2="54" y2="1.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.5" stroke-opacity="0.5"/></g>
  <g id="north-normal-bottom"><rect x="6" y="54" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="north-normal-left"><rect x="0" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="north-normal-right"><rect x="54" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="north-normal-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="north-normal-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="north-normal-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="north-normal-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>

  <g id="west-normal-center"><rect x="6" y="6" width="48" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="west-normal-left"><rect x="0" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/><line x1="1.5" y1="6" x2="1.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-width="1.5" stroke-opacity="0.5"/></g>
  <g id="west-normal-right"><rect x="54" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="west-normal-top"><rect x="6" y="0" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="west-normal-bottom"><rect x="6" y="54" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="west-normal-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="west-normal-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="west-normal-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="west-normal-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>

  <g id="east-normal-center"><rect x="6" y="6" width="48" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="east-normal-right"><rect x="54" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/><line x1="58.5" y1="6" x2="58.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-width="1.5" stroke-opacity="0.5"/></g>
  <g id="east-normal-left"><rect x="0" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="east-normal-top"><rect x="6" y="0" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="east-normal-bottom"><rect x="6" y="54" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="east-normal-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="east-normal-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="east-normal-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>
  <g id="east-normal-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.25"/></g>

  <!-- ========================================== -->
  <!-- 2. FOCUS STATE (Active Focused Task Card)  -->
  <!-- ========================================== -->
  <g id="focus-center"><rect x="66" y="6" width="48" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="focus-topleft"><path d="M 60 6 A 6 6 0 0 1 66 0 L 66 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/><path d="M 60 6 A 6 6 0 0 1 66 0" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="focus-top"><rect x="66" y="0" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.75"/><line x1="66" y1="0.5" x2="114" y2="0.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="focus-topright"><path d="M 114 0 A 6 6 0 0 1 120 6 L 114 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/><path d="M 114 0 A 6 6 0 0 1 120 6" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="focus-left"><rect x="60" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/><line x1="60.5" y1="6" x2="60.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="focus-right"><rect x="114" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/><line x1="119.5" y1="6" x2="119.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="focus-bottomleft"><path d="M 66 60 A 6 6 0 0 1 60 54 L 66 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/><path d="M 66 60 A 6 6 0 0 1 60 54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="focus-bottom">
    <rect x="66" y="54" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.75"/>
    <line x1="66" y1="59.5" x2="114" y2="59.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/>
    <!-- Glowing Full-Width Active LED Line -->
    <line x1="66" y1="57.5" x2="114" y2="57.5" stroke="url(#focusLed)" stroke-width="2.5"/>
  </g>
  <g id="focus-bottomright"><path d="M 120 54 A 6 6 0 0 1 114 60 L 114 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/><path d="M 120 54 A 6 6 0 0 1 114 60" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>

  <!-- Directional focus states -->
  <g id="north-focus-center"><rect x="66" y="6" width="48" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="north-focus-top"><rect x="66" y="0" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.75"/><line x1="66" y1="2.5" x2="114" y2="2.5" stroke="url(#focusLed)" stroke-width="2.5"/></g>
  <g id="north-focus-bottom"><rect x="66" y="54" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="north-focus-left"><rect x="60" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="north-focus-right"><rect x="114" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="north-focus-topleft"><path d="M 60 6 A 6 6 0 0 1 66 0 L 66 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="north-focus-topright"><path d="M 114 0 A 6 6 0 0 1 120 6 L 114 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="north-focus-bottomleft"><path d="M 66 60 A 6 6 0 0 1 60 54 L 66 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="north-focus-bottomright"><path d="M 120 54 A 6 6 0 0 1 114 60 L 114 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>

  <g id="west-focus-center"><rect x="66" y="6" width="48" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="west-focus-left"><rect x="60" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/><line x1="62.5" y1="6" x2="62.5" y2="54" stroke="url(#focusLed)" stroke-width="2.5"/></g>
  <g id="west-focus-right"><rect x="114" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="west-focus-top"><rect x="66" y="0" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="west-focus-bottom"><rect x="66" y="54" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="west-focus-topleft"><path d="M 60 6 A 6 6 0 0 1 66 0 L 66 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="west-focus-topright"><path d="M 114 0 A 6 6 0 0 1 120 6 L 114 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="west-focus-bottomleft"><path d="M 66 60 A 6 6 0 0 1 60 54 L 66 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="west-focus-bottomright"><path d="M 120 54 A 6 6 0 0 1 114 60 L 114 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>

  <g id="east-focus-center"><rect x="66" y="6" width="48" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="east-focus-right"><rect x="114" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/><line x1="117.5" y1="6" x2="117.5" y2="54" stroke="url(#focusLed)" stroke-width="2.5"/></g>
  <g id="east-focus-left"><rect x="60" y="6" width="6" height="48" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="east-focus-top"><rect x="66" y="0" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="east-focus-bottom"><rect x="66" y="54" width="48" height="6" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="east-focus-topleft"><path d="M 60 6 A 6 6 0 0 1 66 0 L 66 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="east-focus-topright"><path d="M 114 0 A 6 6 0 0 1 120 6 L 114 6 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="east-normal-bottomleft"><path d="M 66 60 A 6 6 0 0 1 60 54 L 66 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>
  <g id="east-normal-bottomright"><path d="M 120 54 A 6 6 0 0 1 114 60 L 114 54 Z" fill="{C_VOID_CARD}" fill-opacity="0.75"/></g>

  <!-- ========================================== -->
  <!-- 3. HOVER STATE                             -->
  <!-- ========================================== -->
  <g id="hover-center"><rect x="126" y="6" width="48" height="48" fill="{C_STAR_WHITE}" fill-opacity="0.10"/></g>
  <g id="hover-topleft"><path d="M 120 6 A 6 6 0 0 1 126 0 L 126 6 Z" fill="{C_STAR_WHITE}" fill-opacity="0.10"/><path d="M 120 6 A 6 6 0 0 1 126 0" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.5" stroke-width="1.0" fill="none"/></g>
  <g id="hover-top"><rect x="126" y="0" width="48" height="6" fill="{C_STAR_WHITE}" fill-opacity="0.10"/><line x1="126" y1="0.5" x2="174" y2="0.5" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.5" stroke-width="1.0"/></g>
  <g id="hover-topright"><path d="M 174 0 A 6 6 0 0 1 180 6 L 174 6 Z" fill="{C_STAR_WHITE}" fill-opacity="0.10"/><path d="M 174 0 A 6 6 0 0 1 180 6" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.5" stroke-width="1.0" fill="none"/></g>
  <g id="hover-left"><rect x="120" y="6" width="6" height="48" fill="{C_STAR_WHITE}" fill-opacity="0.10"/><line x1="120.5" y1="6" x2="120.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.5" stroke-width="1.0"/></g>
  <g id="hover-right"><rect x="174" y="6" width="6" height="48" fill="{C_STAR_WHITE}" fill-opacity="0.10"/><line x1="179.5" y1="6" x2="179.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.5" stroke-width="1.0"/></g>
  <g id="hover-bottomleft"><path d="M 126 60 A 6 6 0 0 1 120 54 L 126 54 Z" fill="{C_STAR_WHITE}" fill-opacity="0.10"/><path d="M 126 60 A 6 6 0 0 1 120 54" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.5" stroke-width="1.0" fill="none"/></g>
  <g id="hover-bottom"><rect x="126" y="54" width="48" height="6" fill="{C_STAR_WHITE}" fill-opacity="0.10"/><line x1="126" y1="59.5" x2="174" y2="59.5" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.5" stroke-width="1.0"/></g>
  <g id="hover-bottomright"><path d="M 180 54 A 6 6 0 0 1 174 60 L 174 54 Z" fill="{C_STAR_WHITE}" fill-opacity="0.10"/><path d="M 180 54 A 6 6 0 0 1 174 60" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.5" stroke-width="1.0" fill="none"/></g>

  <!-- ========================================== -->
  <!-- 4. MINIMIZED STATE (Distinct Stasis Card)  -->
  <!-- Dimmed obsidian fill, dashed stardust border, muted dashed bottom indicator -->
  <!-- ========================================== -->
  <g id="minimized-center"><rect x="186" y="6" width="48" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="minimized-topleft"><path d="M 180 6 A 6 6 0 0 1 186 0 L 186 6 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/><path d="M 180 6 A 6 6 0 0 1 186 0" stroke="{C_STARDUST}" stroke-opacity="0.45" stroke-width="1.0" stroke-dasharray="3,2" fill="none"/></g>
  <g id="minimized-top"><rect x="186" y="0" width="48" height="6" fill="{C_VOID_DARK}" fill-opacity="0.60"/><line x1="186" y1="0.5" x2="234" y2="0.5" stroke="{C_STARDUST}" stroke-opacity="0.45" stroke-width="1.0" stroke-dasharray="3,2"/></g>
  <g id="minimized-topright"><path d="M 234 0 A 6 6 0 0 1 240 6 L 234 6 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/><path d="M 234 0 A 6 6 0 0 1 240 6" stroke="{C_STARDUST}" stroke-opacity="0.45" stroke-width="1.0" stroke-dasharray="3,2" fill="none"/></g>
  <g id="minimized-left"><rect x="180" y="6" width="6" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/><line x1="180.5" y1="6" x2="180.5" y2="54" stroke="{C_STARDUST}" stroke-opacity="0.45" stroke-width="1.0" stroke-dasharray="3,2"/></g>
  <g id="minimized-right"><rect x="234" y="6" width="6" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/><line x1="239.5" y1="6" x2="239.5" y2="54" stroke="{C_STARDUST}" stroke-opacity="0.45" stroke-width="1.0" stroke-dasharray="3,2"/></g>
  <g id="minimized-bottomleft"><path d="M 186 60 A 6 6 0 0 1 180 54 L 186 54 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/><path d="M 186 60 A 6 6 0 0 1 180 54" stroke="{C_STARDUST}" stroke-opacity="0.45" stroke-width="1.0" stroke-dasharray="3,2" fill="none"/></g>
  <g id="minimized-bottom">
    <rect x="186" y="54" width="48" height="6" fill="{C_VOID_DARK}" fill-opacity="0.60"/>
    <line x1="186" y1="59.5" x2="234" y2="59.5" stroke="{C_STARDUST}" stroke-opacity="0.45" stroke-width="1.0" stroke-dasharray="3,2"/>
    <!-- Muted Stardust Dashed Running Indicator (distinguishes minimized from active) -->
    <line x1="186" y1="58.5" x2="234" y2="58.5" stroke="{C_STARDUST}" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="3,3"/>
  </g>
  <g id="minimized-bottomright"><path d="M 240 54 A 6 6 0 0 1 234 60 L 234 54 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/><path d="M 240 54 A 6 6 0 0 1 234 60" stroke="{C_STARDUST}" stroke-opacity="0.45" stroke-width="1.0" stroke-dasharray="3,2" fill="none"/></g>

  <!-- Directional minimized states (North, West, East) -->
  <g id="north-minimized-center"><rect x="186" y="6" width="48" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="north-minimized-top"><rect x="186" y="0" width="48" height="6" fill="{C_VOID_DARK}" fill-opacity="0.60"/><line x1="186" y1="1.5" x2="234" y2="1.5" stroke="{C_STARDUST}" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="3,3"/></g>
  <g id="north-minimized-bottom"><rect x="186" y="54" width="48" height="6" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="north-minimized-left"><rect x="180" y="6" width="6" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="north-minimized-right"><rect x="234" y="6" width="6" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="north-minimized-topleft"><path d="M 180 6 A 6 6 0 0 1 186 0 L 186 6 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="north-minimized-topright"><path d="M 234 0 A 6 6 0 0 1 240 6 L 234 6 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="north-minimized-bottomleft"><path d="M 186 60 A 6 6 0 0 1 180 54 L 186 54 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="north-minimized-bottomright"><path d="M 240 54 A 6 6 0 0 1 234 60 L 234 54 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>

  <g id="west-minimized-center"><rect x="186" y="6" width="48" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="west-minimized-left"><rect x="180" y="6" width="6" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/><line x1="181.5" y1="6" x2="181.5" y2="54" stroke="{C_STARDUST}" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="3,3"/></g>
  <g id="west-minimized-right"><rect x="234" y="6" width="6" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="west-minimized-top"><rect x="186" y="0" width="48" height="6" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="west-minimized-bottom"><rect x="186" y="54" width="48" height="6" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="west-minimized-topleft"><path d="M 180 6 A 6 6 0 0 1 186 0 L 186 6 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="west-minimized-topright"><path d="M 234 0 A 6 6 0 0 1 240 6 L 234 6 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="west-minimized-bottomleft"><path d="M 186 60 A 6 6 0 0 1 180 54 L 186 54 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="west-minimized-bottomright"><path d="M 240 54 A 6 6 0 0 1 234 60 L 234 54 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>

  <g id="east-minimized-center"><rect x="186" y="6" width="48" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="east-minimized-right"><rect x="234" y="6" width="6" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/><line x1="238.5" y1="6" x2="238.5" y2="54" stroke="{C_STARDUST}" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="3,3"/></g>
  <g id="east-minimized-left"><rect x="180" y="6" width="6" height="48" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="east-minimized-top"><rect x="186" y="0" width="48" height="6" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="east-minimized-bottom"><rect x="186" y="54" width="48" height="6" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="east-minimized-topleft"><path d="M 180 6 A 6 6 0 0 1 186 0 L 186 6 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="east-minimized-topright"><path d="M 234 0 A 6 6 0 0 1 240 6 L 234 6 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="east-minimized-bottomleft"><path d="M 186 60 A 6 6 0 0 1 180 54 L 186 54 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>
  <g id="east-minimized-bottomright"><path d="M 240 54 A 6 6 0 0 1 234 60 L 234 54 Z" fill="{C_VOID_DARK}" fill-opacity="0.60"/></g>

  <!-- ========================================== -->
  <!-- 5. ATTENTION STATE                         -->
  <!-- ========================================== -->
  <g id="attention-center"><rect x="246" y="6" width="48" height="48" fill="{C_DANGER_RED}" fill-opacity="0.35"/></g>
  <g id="attention-topleft"><path d="M 240 6 A 6 6 0 0 1 246 0 L 246 6 Z" fill="{C_DANGER_RED}" fill-opacity="0.35"/><path d="M 240 6 A 6 6 0 0 1 246 0" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.0" fill="none"/></g>
  <g id="attention-top"><rect x="246" y="0" width="48" height="6" fill="{C_DANGER_RED}" fill-opacity="0.35"/><line x1="246" y1="0.5" x2="294" y2="0.5" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.0"/></g>
  <g id="attention-topright"><path d="M 294 0 A 6 6 0 0 1 300 6 L 294 6 Z" fill="{C_DANGER_RED}" fill-opacity="0.35"/><path d="M 294 0 A 6 6 0 0 1 300 6" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.0" fill="none"/></g>
  <g id="attention-left"><rect x="240" y="6" width="6" height="48" fill="{C_DANGER_RED}" fill-opacity="0.35"/><line x1="240.5" y1="6" x2="240.5" y2="54" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.0"/></g>
  <g id="attention-right"><rect x="294" y="6" width="6" height="48" fill="{C_DANGER_RED}" fill-opacity="0.35"/><line x1="299.5" y1="6" x2="299.5" y2="54" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.0"/></g>
  <g id="attention-bottomleft"><path d="M 246 60 A 6 6 0 0 1 240 54 L 246 54 Z" fill="{C_DANGER_RED}" fill-opacity="0.35"/><path d="M 246 60 A 6 6 0 0 1 240 54" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.0" fill="none"/></g>
  <g id="attention-bottom"><rect x="246" y="54" width="48" height="6" fill="{C_DANGER_RED}" fill-opacity="0.35"/><line x1="246" y1="59.5" x2="294" y2="59.5" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.0"/><line x1="246" y1="57.5" x2="294" y2="57.5" stroke="{C_SUPERNOVA_GOLD}" stroke-width="2.5"/></g>
  <g id="attention-bottomright"><path d="M 300 54 A 6 6 0 0 1 294 60 L 294 54 Z" fill="{C_DANGER_RED}" fill-opacity="0.35"/><path d="M 300 54 A 6 6 0 0 1 294 60" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.0" fill="none"/></g>

  <!-- ========================================== -->
  <!-- 6. PROGRESS STATE                          -->
  <!-- ========================================== -->
  <g id="progress-center"><rect x="306" y="6" width="48" height="48" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/></g>
  <g id="progress-topleft"><path d="M 300 6 A 6 6 0 0 1 306 0 L 306 6 Z" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/><path d="M 300 6 A 6 6 0 0 1 306 0" stroke="{C_AURORA_EMERALD}" stroke-width="1.0" fill="none"/></g>
  <g id="progress-top"><rect x="306" y="0" width="48" height="6" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/><line x1="306" y1="0.5" x2="354" y2="0.5" stroke="{C_AURORA_EMERALD}" stroke-width="1.0"/></g>
  <g id="progress-topright"><path d="M 354 0 A 6 6 0 0 1 360 6 L 354 6 Z" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/><path d="M 354 0 A 6 6 0 0 1 360 6" stroke="{C_AURORA_EMERALD}" stroke-width="1.0" fill="none"/></g>
  <g id="progress-left"><rect x="300" y="6" width="6" height="48" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/><line x1="300.5" y1="6" x2="300.5" y2="54" stroke="{C_AURORA_EMERALD}" stroke-width="1.0"/></g>
  <g id="progress-right"><rect x="354" y="6" width="6" height="48" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/><line x1="359.5" y1="6" x2="359.5" y2="54" stroke="{C_AURORA_EMERALD}" stroke-width="1.0"/></g>
  <g id="progress-bottomleft"><path d="M 306 60 A 6 6 0 0 1 300 54 L 306 54 Z" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/><path d="M 306 60 A 6 6 0 0 1 300 54" stroke="{C_AURORA_EMERALD}" stroke-width="1.0" fill="none"/></g>
  <g id="progress-bottom"><rect x="306" y="54" width="48" height="6" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/><line x1="306" y1="59.5" x2="354" y2="59.5" stroke="{C_AURORA_EMERALD}" stroke-width="1.0"/><line x1="306" y1="57.5" x2="354" y2="57.5" stroke="{C_AURORA_EMERALD}" stroke-width="2.5"/></g>
  <g id="progress-bottomright"><path d="M 360 54 A 6 6 0 0 1 354 60 L 354 54 Z" fill="{C_AURORA_EMERALD}" fill-opacity="0.3"/><path d="M 360 54 A 6 6 0 0 1 354 60" stroke="{C_AURORA_EMERALD}" stroke-width="1.0" fill="none"/></g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "tasks.svg"), svg)

def gen_plasma_bar_meter():
    # Clean Plasma 6 Level Meter Bar
    svg_h = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 60 60">
  <defs>
    <linearGradient id="barActiveFill" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="100%" stop-color="{C_PULSAR_VIO}"/>
    </linearGradient>
  </defs>

  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>
  <rect id="hint-bar-size" x="0" y="0" width="6" height="6" fill="none"/>

  <!-- Inactive Groove (Smooth obsidian track) -->
  <g id="bar-inactive-center"><rect x="6" y="6" width="8" height="8" fill="{C_VOID_DARK}"/></g>
  <g id="bar-inactive-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_DARK}"/><path d="M 0 6 A 6 6 0 0 1 6 0" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="bar-inactive-top"><rect x="6" y="0" width="8" height="6" fill="{C_VOID_DARK}"/><line x1="6" y1="0.5" x2="14" y2="0.5" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="bar-inactive-topright"><path d="M 14 0 A 6 6 0 0 1 20 6 L 14 6 Z" fill="{C_VOID_DARK}"/><path d="M 14 0 A 6 6 0 0 1 20 6" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="bar-inactive-left"><rect x="0" y="6" width="6" height="8" fill="{C_VOID_DARK}"/><line x1="0.5" y1="6" x2="0.5" y2="14" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="bar-inactive-right"><rect x="14" y="6" width="6" height="8" fill="{C_VOID_DARK}"/><line x1="19.5" y1="6" x2="19.5" y2="14" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="bar-inactive-bottomleft"><path d="M 6 20 A 6 6 0 0 1 0 14 L 6 14 Z" fill="{C_VOID_DARK}"/><path d="M 6 20 A 6 6 0 0 1 0 14" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="bar-inactive-bottom"><rect x="6" y="14" width="8" height="6" fill="{C_VOID_DARK}"/><line x1="6" y1="19.5" x2="14" y2="19.5" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="bar-inactive-bottomright"><path d="M 20 14 A 6 6 0 0 1 14 20 L 14 14 Z" fill="{C_VOID_DARK}"/><path d="M 20 14 A 6 6 0 0 1 14 20" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>

  <!-- Active Level Fill -->
  <g id="bar-active-center"><rect x="36" y="6" width="8" height="8" fill="url(#barActiveFill)"/></g>
  <g id="bar-active-topleft"><path d="M 30 6 A 6 6 0 0 1 36 0 L 36 6 Z" fill="url(#barActiveFill)"/></g>
  <g id="bar-active-top"><rect x="36" y="0" width="8" height="6" fill="url(#barActiveFill)"/></g>
  <g id="bar-active-topright"><path d="M 44 0 A 6 6 0 0 1 50 6 L 44 6 Z" fill="url(#barActiveFill)"/></g>
  <g id="bar-active-left"><rect x="30" y="6" width="6" height="8" fill="url(#barActiveFill)"/></g>
  <g id="bar-active-right"><rect x="44" y="6" width="6" height="8" fill="url(#barActiveFill)"/></g>
  <g id="bar-active-bottomleft"><path d="M 36 20 A 6 6 0 0 1 30 14 L 36 14 Z" fill="url(#barActiveFill)"/></g>
  <g id="bar-active-bottom"><rect x="36" y="14" width="8" height="6" fill="url(#barActiveFill)"/></g>
  <g id="bar-active-bottomright"><path d="M 50 14 A 6 6 0 0 1 44 20 L 44 14 Z" fill="url(#barActiveFill)"/></g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "bar_meter_horizontal.svg"), svg_h)
    write_file(os.path.join(PLASMA_DIR, "widgets", "bar_meter_vertical.svg"), svg_h)

def gen_plasma_slider():
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120">
  <defs>
    <radialGradient id="handleGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{C_STAR_WHITE}"/>
      <stop offset="60%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="100%" stop-color="{C_PULSAR_VIO}"/>
    </radialGradient>
    <linearGradient id="grooveActiveFill" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="100%" stop-color="{C_PULSAR_VIO}"/>
    </linearGradient>
  </defs>

  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>
  <rect id="hint-handle-size" x="0" y="0" width="16" height="16" fill="none"/>

  <!-- Inactive Groove Track -->
  <g id="groove-center"><rect x="6" y="6" width="8" height="8" fill="{C_VOID_DARK}"/></g>
  <g id="groove-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_DARK}"/><path d="M 0 6 A 6 6 0 0 1 6 0" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="groove-top"><rect x="6" y="0" width="8" height="6" fill="{C_VOID_DARK}"/><line x1="6" y1="0.5" x2="14" y2="0.5" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="groove-topright"><path d="M 14 0 A 6 6 0 0 1 20 6 L 14 6 Z" fill="{C_VOID_DARK}"/><path d="M 14 0 A 6 6 0 0 1 20 6" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="groove-left"><rect x="0" y="6" width="6" height="8" fill="{C_VOID_DARK}"/><line x1="0.5" y1="6" x2="0.5" y2="14" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="groove-right"><rect x="14" y="6" width="6" height="8" fill="{C_VOID_DARK}"/><line x1="19.5" y1="6" x2="19.5" y2="14" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="groove-bottomleft"><path d="M 6 20 A 6 6 0 0 1 0 14 L 6 14 Z" fill="{C_VOID_DARK}"/><path d="M 6 20 A 6 6 0 0 1 0 14" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="groove-bottom"><rect x="6" y="14" width="8" height="6" fill="{C_VOID_DARK}"/><line x1="6" y1="19.5" x2="14" y2="19.5" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="groove-bottomright"><path d="M 20 14 A 6 6 0 0 1 14 20 L 14 14 Z" fill="{C_VOID_DARK}"/><path d="M 20 14 A 6 6 0 0 1 14 20" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>

  <!-- Active Groove Highlight -->
  <g id="groove-highlight-center"><rect x="36" y="6" width="8" height="8" fill="url(#grooveActiveFill)"/></g>
  <g id="groove-highlight-topleft"><path d="M 30 6 A 6 6 0 0 1 36 0 L 36 6 Z" fill="url(#grooveActiveFill)"/></g>
  <g id="groove-highlight-top"><rect x="36" y="0" width="8" height="6" fill="url(#grooveActiveFill)"/></g>
  <g id="groove-highlight-topright"><path d="M 44 0 A 6 6 0 0 1 50 6 L 44 6 Z" fill="url(#grooveActiveFill)"/></g>
  <g id="groove-highlight-left"><rect x="30" y="6" width="6" height="8" fill="url(#grooveActiveFill)"/></g>
  <g id="groove-highlight-right"><rect x="44" y="6" width="6" height="8" fill="url(#grooveActiveFill)"/></g>
  <g id="groove-highlight-bottomleft"><path d="M 36 20 A 6 6 0 0 1 30 14 L 36 14 Z" fill="url(#grooveActiveFill)"/></g>
  <g id="groove-highlight-bottom"><rect x="36" y="14" width="8" height="6" fill="url(#grooveActiveFill)"/></g>
  <g id="groove-highlight-bottomright"><path d="M 50 14 A 6 6 0 0 1 44 20 L 44 14 Z" fill="url(#grooveActiveFill)"/></g>

  <!-- Handles -->
  <g id="horizontal-slider-handle">
    <circle cx="70" cy="20" r="7" fill="url(#handleGrad)"/>
    <circle cx="70" cy="20" r="7" fill="none" stroke="{C_STAR_WHITE}" stroke-width="1.2"/>
  </g>
  <g id="horizontal-slider-hover">
    <circle cx="95" cy="20" r="8" fill="url(#handleGrad)"/>
    <circle cx="95" cy="20" r="8" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/>
  </g>
  <g id="horizontal-slider-focus">
    <circle cx="70" cy="50" r="7" fill="url(#handleGrad)"/>
    <circle cx="70" cy="50" r="7" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.8"/>
  </g>
  <g id="horizontal-slider-shadow"><circle cx="95" cy="50" r="7" fill="#000000" opacity="0.4"/></g>

  <g id="vertical-slider-handle">
    <circle cx="20" cy="70" r="7" fill="url(#handleGrad)"/>
    <circle cx="20" cy="70" r="7" fill="none" stroke="{C_STAR_WHITE}" stroke-width="1.2"/>
  </g>
  <g id="vertical-slider-hover">
    <circle cx="45" cy="70" r="8" fill="url(#handleGrad)"/>
    <circle cx="45" cy="70" r="8" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/>
  </g>
  <g id="vertical-slider-focus">
    <circle cx="20" cy="95" r="7" fill="url(#handleGrad)"/>
    <circle cx="20" cy="95" r="7" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.8"/>
  </g>
  <g id="vertical-slider-shadow"><circle cx="45" cy="95" r="7" fill="#000000" opacity="0.4"/></g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "slider.svg"), svg)

def gen_plasma_tooltip():
    # Clean 9-slice Tooltip
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 80 80">
  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>
  <rect id="hint-top-margin" x="0" y="0" width="80" height="6" fill="none"/>
  <rect id="hint-bottom-margin" x="0" y="74" width="80" height="6" fill="none"/>
  <rect id="hint-left-margin" x="0" y="0" width="6" height="80" fill="none"/>
  <rect id="hint-right-margin" x="74" y="0" width="6" height="80" fill="none"/>

  <g id="center"><rect x="6" y="6" width="68" height="68" fill="{C_VOID_MID}" fill-opacity="0.96"/></g>
  <g id="topleft">
    <path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_MID}" fill-opacity="0.96"/>
    <path d="M 0 6 A 6 6 0 0 1 6 0" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>
  <g id="top">
    <rect x="6" y="0" width="68" height="6" fill="{C_VOID_MID}" fill-opacity="0.96"/>
    <line x1="6" y1="0.5" x2="74" y2="0.5" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>
  <g id="topright">
    <path d="M 74 0 A 6 6 0 0 1 80 6 L 74 6 Z" fill="{C_VOID_MID}" fill-opacity="0.96"/>
    <path d="M 74 0 A 6 6 0 0 1 80 6" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>
  <g id="left">
    <rect x="0" y="6" width="6" height="68" fill="{C_VOID_MID}" fill-opacity="0.96"/>
    <line x1="0.5" y1="6" x2="0.5" y2="74" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>
  <g id="right">
    <rect x="74" y="6" width="6" height="68" fill="{C_VOID_MID}" fill-opacity="0.96"/>
    <line x1="79.5" y1="6" x2="79.5" y2="74" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>
  <g id="bottomleft">
    <path d="M 6 80 A 6 6 0 0 1 0 74 L 6 74 Z" fill="{C_VOID_MID}" fill-opacity="0.96"/>
    <path d="M 6 80 A 6 6 0 0 1 0 74" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>
  <g id="bottom">
    <rect x="6" y="74" width="68" height="6" fill="{C_VOID_MID}" fill-opacity="0.96"/>
    <line x1="6" y1="79.5" x2="74" y2="79.5" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>
  <g id="bottomright">
    <path d="M 80 74 A 6 6 0 0 1 74 80 L 74 74 Z" fill="{C_VOID_MID}" fill-opacity="0.96"/>
    <path d="M 80 74 A 6 6 0 0 1 74 80" fill="none" stroke="{C_VOID_BORDER}" stroke-width="1.0"/>
  </g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "tooltip.svg"), svg)

def gen_plasma_button():
    # Clean 9-slice Plasma Button with solid uniform fills
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="180" height="60" viewBox="0 0 180 60">
  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>
  <rect id="hint-top-margin" x="0" y="0" width="60" height="6" fill="none"/>
  <rect id="hint-bottom-margin" x="0" y="54" width="60" height="6" fill="none"/>
  <rect id="hint-left-margin" x="0" y="0" width="6" height="60" fill="none"/>
  <rect id="hint-right-margin" x="54" y="0" width="6" height="60" fill="none"/>

  <!-- 1. NORMAL BUTTON (x=0..60) -->
  <g id="normal-center"><rect x="6" y="6" width="48" height="48" fill="{C_VOID_CARD}"/></g>
  <g id="normal-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_CARD}"/><path d="M 0 6 A 6 6 0 0 1 6 0" stroke="{C_VOID_BORDER}" stroke-width="1.0" fill="none"/></g>
  <g id="normal-top"><rect x="6" y="0" width="48" height="6" fill="{C_VOID_CARD}"/><line x1="6" y1="0.5" x2="54" y2="0.5" stroke="{C_VOID_BORDER}" stroke-width="1.0"/></g>
  <g id="normal-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_VOID_CARD}"/><path d="M 54 0 A 6 6 0 0 1 60 6" stroke="{C_VOID_BORDER}" stroke-width="1.0" fill="none"/></g>
  <g id="normal-left"><rect x="0" y="6" width="6" height="48" fill="{C_VOID_CARD}"/><line x1="0.5" y1="6" x2="0.5" y2="54" stroke="{C_VOID_BORDER}" stroke-width="1.0"/></g>
  <g id="normal-right"><rect x="54" y="6" width="6" height="48" fill="{C_VOID_CARD}"/><line x1="59.5" y1="6" x2="59.5" y2="54" stroke="{C_VOID_BORDER}" stroke-width="1.0"/></g>
  <g id="normal-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_VOID_CARD}"/><path d="M 6 60 A 6 6 0 0 1 0 54" stroke="{C_VOID_BORDER}" stroke-width="1.0" fill="none"/></g>
  <g id="normal-bottom"><rect x="6" y="54" width="48" height="6" fill="{C_VOID_CARD}"/><line x1="6" y1="59.5" x2="54" y2="59.5" stroke="{C_VOID_BORDER}" stroke-width="1.0"/></g>
  <g id="normal-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_VOID_CARD}"/><path d="M 60 54 A 6 6 0 0 1 54 60" stroke="{C_VOID_BORDER}" stroke-width="1.0" fill="none"/></g>

  <!-- 2. HOVER BUTTON (x=60..120) -->
  <g id="hover-center"><rect x="66" y="6" width="48" height="48" fill="#202A44"/></g>
  <g id="hover-topleft"><path d="M 60 6 A 6 6 0 0 1 66 0 L 66 6 Z" fill="#202A44"/><path d="M 60 6 A 6 6 0 0 1 66 0" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="hover-top"><rect x="66" y="0" width="48" height="6" fill="#202A44"/><line x1="66" y1="0.5" x2="114" y2="0.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="hover-topright"><path d="M 114 0 A 6 6 0 0 1 120 6 L 114 6 Z" fill="#202A44"/><path d="M 114 0 A 6 6 0 0 1 120 6" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="hover-left"><rect x="60" y="6" width="6" height="48" fill="#202A44"/><line x1="60.5" y1="6" x2="60.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="hover-right"><rect x="114" y="6" width="6" height="48" fill="#202A44"/><line x1="119.5" y1="6" x2="119.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="hover-bottomleft"><path d="M 66 60 A 6 6 0 0 1 60 54 L 66 54 Z" fill="#202A44"/><path d="M 66 60 A 6 6 0 0 1 60 54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="hover-bottom"><rect x="66" y="54" width="48" height="6" fill="#202A44"/><line x1="66" y1="59.5" x2="114" y2="59.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="hover-bottomright"><path d="M 120 54 A 6 6 0 0 1 114 60 L 114 54 Z" fill="#202A44"/><path d="M 120 54 A 6 6 0 0 1 114 60" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>

  <!-- 3. PRESSED BUTTON (x=120..180) -->
  <g id="pressed-center"><rect x="126" y="6" width="48" height="48" fill="#141B30"/></g>
  <g id="pressed-topleft"><path d="M 120 6 A 6 6 0 0 1 126 0 L 126 6 Z" fill="#141B30"/><path d="M 120 6 A 6 6 0 0 1 126 0" stroke="{C_PULSAR_VIO}" stroke-width="1.2" fill="none"/></g>
  <g id="pressed-top"><rect x="126" y="0" width="48" height="6" fill="#141B30"/><line x1="126" y1="0.5" x2="174" y2="0.5" stroke="{C_PULSAR_VIO}" stroke-width="1.2"/></g>
  <g id="pressed-topright"><path d="M 174 0 A 6 6 0 0 1 180 6 L 174 6 Z" fill="#141B30"/><path d="M 174 0 A 6 6 0 0 1 180 6" stroke="{C_PULSAR_VIO}" stroke-width="1.2" fill="none"/></g>
  <g id="pressed-left"><rect x="120" y="6" width="6" height="48" fill="#141B30"/><line x1="120.5" y1="6" x2="120.5" y2="54" stroke="{C_PULSAR_VIO}" stroke-width="1.2"/></g>
  <g id="pressed-right"><rect x="174" y="6" width="6" height="48" fill="#141B30"/><line x1="179.5" y1="6" x2="179.5" y2="54" stroke="{C_PULSAR_VIO}" stroke-width="1.2"/></g>
  <g id="pressed-bottomleft"><path d="M 126 60 A 6 6 0 0 1 120 54 L 126 54 Z" fill="#141B30"/><path d="M 126 60 A 6 6 0 0 1 120 54" stroke="{C_PULSAR_VIO}" stroke-width="1.2" fill="none"/></g>
  <g id="pressed-bottom"><rect x="126" y="54" width="48" height="6" fill="#141B30"/><line x1="126" y1="59.5" x2="174" y2="59.5" stroke="{C_PULSAR_VIO}" stroke-width="1.2"/></g>
  <g id="pressed-bottomright"><path d="M 180 54 A 6 6 0 0 1 174 60 L 174 54 Z" fill="#141B30"/><path d="M 180 54 A 6 6 0 0 1 174 60" stroke="{C_PULSAR_VIO}" stroke-width="1.2" fill="none"/></g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "button.svg"), svg)

def gen_plasma_other_widgets():
    scrollbar_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="60" height="100" viewBox="0 0 60 100">
  <rect id="background-vertical-center" x="25" y="10" width="10" height="80" fill="{C_VOID_DARK}" opacity="0.6"/>
  <rect id="slider-vertical-center" x="26" y="20" width="8" height="60" rx="4" fill="{C_PULSAR_VIO}" opacity="0.8"/>
  <rect id="slider-vertical-hover" x="25" y="20" width="10" height="60" rx="5" fill="{C_STELLAR_CYAN}"/>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "scrollbar.svg"), scrollbar_svg)

    tabbar_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="60" viewBox="0 0 100 60">
  <rect id="north-tab-center" x="10" y="10" width="80" height="40" fill="none"/>
  <g id="north-active-tab-center">
    <rect x="10" y="10" width="80" height="40" fill="{C_VOID_CARD}" fill-opacity="0.4"/>
    <line x1="10" y1="48.5" x2="90" y2="48.5" stroke="{C_STELLAR_CYAN}" stroke-width="2.5"/>
  </g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "tabbar.svg"), tabbar_svg)

    viewitem_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 60 60">
  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>
  <rect id="hint-top-margin" x="0" y="0" width="60" height="6" fill="none"/>
  <rect id="hint-bottom-margin" x="0" y="54" width="60" height="6" fill="none"/>
  <rect id="hint-left-margin" x="0" y="0" width="6" height="60" fill="none"/>
  <rect id="hint-right-margin" x="54" y="0" width="6" height="60" fill="none"/>

  <g id="hover-center"><rect x="6" y="6" width="48" height="48" fill="{C_STAR_WHITE}" fill-opacity="0.08"/></g>
  <g id="hover-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_STAR_WHITE}" fill-opacity="0.08"/><path d="M 0 6 A 6 6 0 0 1 6 0" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.3" stroke-width="1" fill="none"/></g>
  <g id="hover-top"><rect x="6" y="0" width="48" height="6" fill="{C_STAR_WHITE}" fill-opacity="0.08"/><line x1="6" y1="0.5" x2="54" y2="0.5" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.3" stroke-width="1"/></g>
  <g id="hover-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_STAR_WHITE}" fill-opacity="0.08"/><path d="M 54 0 A 6 6 0 0 1 60 6" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.3" stroke-width="1" fill="none"/></g>
  <g id="hover-left"><rect x="0" y="6" width="6" height="48" fill="{C_STAR_WHITE}" fill-opacity="0.08"/><line x1="0.5" y1="6" x2="0.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.3" stroke-width="1"/></g>
  <g id="hover-right"><rect x="54" y="6" width="6" height="48" fill="{C_STAR_WHITE}" fill-opacity="0.08"/><line x1="59.5" y1="6" x2="59.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.3" stroke-width="1"/></g>
  <g id="hover-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_STAR_WHITE}" fill-opacity="0.08"/><path d="M 6 60 A 6 6 0 0 1 0 54" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.3" stroke-width="1" fill="none"/></g>
  <g id="hover-bottom"><rect x="6" y="54" width="48" height="6" fill="{C_STAR_WHITE}" fill-opacity="0.08"/><line x1="6" y1="59.5" x2="54" y2="59.5" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.3" stroke-width="1"/></g>
  <g id="hover-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_STAR_WHITE}" fill-opacity="0.08"/><path d="M 60 54 A 6 6 0 0 1 54 60" stroke="{C_STELLAR_CYAN}" stroke-opacity="0.3" stroke-width="1" fill="none"/></g>

  <g id="selected-center"><rect x="6" y="6" width="48" height="48" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/></g>
  <g id="selected-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/><path d="M 0 6 A 6 6 0 0 1 6 0" stroke="{C_PULSAR_VIO}" stroke-opacity="0.8" stroke-width="1.2" fill="none"/></g>
  <g id="selected-top"><rect x="6" y="0" width="48" height="6" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/><line x1="6" y1="0.5" x2="54" y2="0.5" stroke="{C_PULSAR_VIO}" stroke-opacity="0.8" stroke-width="1.2"/></g>
  <g id="selected-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/><path d="M 54 0 A 6 6 0 0 1 60 6" stroke="{C_PULSAR_VIO}" stroke-opacity="0.8" stroke-width="1.2" fill="none"/></g>
  <g id="selected-left"><rect x="0" y="6" width="6" height="48" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/><line x1="0.5" y1="6" x2="0.5" y2="54" stroke="{C_PULSAR_VIO}" stroke-opacity="0.8" stroke-width="1.2"/></g>
  <g id="selected-right"><rect x="54" y="6" width="6" height="48" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/><line x1="59.5" y1="6" x2="59.5" y2="54" stroke="{C_PULSAR_VIO}" stroke-opacity="0.8" stroke-width="1.2"/></g>
  <g id="selected-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/><path d="M 6 60 A 6 6 0 0 1 0 54" stroke="{C_PULSAR_VIO}" stroke-opacity="0.8" stroke-width="1.2" fill="none"/></g>
  <g id="selected-bottom"><rect x="6" y="54" width="48" height="6" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/><line x1="6" y1="59.5" x2="54" y2="59.5" stroke="{C_PULSAR_VIO}" stroke-opacity="0.8" stroke-width="1.2"/></g>
  <g id="selected-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_PULSAR_VIO}" fill-opacity="0.35"/><path d="M 60 54 A 6 6 0 0 1 54 60" stroke="{C_PULSAR_VIO}" stroke-opacity="0.8" stroke-width="1.2" fill="none"/></g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "viewitem.svg"), viewitem_svg)

    lineedit_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 60 60">
  <rect id="hint-stretch-borders" x="0" y="0" width="1" height="1" fill="none"/>
  <rect id="hint-top-margin" x="0" y="0" width="60" height="6" fill="none"/>
  <rect id="hint-bottom-margin" x="0" y="54" width="60" height="6" fill="none"/>
  <rect id="hint-left-margin" x="0" y="0" width="6" height="60" fill="none"/>
  <rect id="hint-right-margin" x="54" y="0" width="6" height="60" fill="none"/>

  <g id="base-center"><rect x="6" y="6" width="48" height="48" fill="{C_VOID_DARK}"/></g>
  <g id="base-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_DARK}"/><path d="M 0 6 A 6 6 0 0 1 6 0" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="base-top"><rect x="6" y="0" width="48" height="6" fill="{C_VOID_DARK}"/><line x1="6" y1="0.5" x2="54" y2="0.5" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="base-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_VOID_DARK}"/><path d="M 54 0 A 6 6 0 0 1 60 6" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="base-left"><rect x="0" y="6" width="6" height="48" fill="{C_VOID_DARK}"/><line x1="0.5" y1="6" x2="0.5" y2="54" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="base-right"><rect x="54" y="6" width="6" height="48" fill="{C_VOID_DARK}"/><line x1="59.5" y1="6" x2="59.5" y2="54" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="base-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_VOID_DARK}"/><path d="M 6 60 A 6 6 0 0 1 0 54" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>
  <g id="base-bottom"><rect x="6" y="54" width="48" height="6" fill="{C_VOID_DARK}"/><line x1="6" y1="59.5" x2="54" y2="59.5" stroke="{C_VOID_BORDER}" stroke-width="1"/></g>
  <g id="base-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_VOID_DARK}"/><path d="M 60 54 A 6 6 0 0 1 54 60" stroke="{C_VOID_BORDER}" stroke-width="1" fill="none"/></g>

  <g id="focus-center"><rect x="6" y="6" width="48" height="48" fill="{C_VOID_DARK}"/></g>
  <g id="focus-topleft"><path d="M 0 6 A 6 6 0 0 1 6 0 L 6 6 Z" fill="{C_VOID_DARK}"/><path d="M 0 6 A 6 6 0 0 1 6 0" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="focus-top"><rect x="6" y="0" width="48" height="6" fill="{C_VOID_DARK}"/><line x1="6" y1="0.5" x2="54" y2="0.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="focus-topright"><path d="M 54 0 A 6 6 0 0 1 60 6 L 54 6 Z" fill="{C_VOID_DARK}"/><path d="M 54 0 A 6 6 0 0 1 60 6" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="focus-left"><rect x="0" y="6" width="6" height="48" fill="{C_VOID_DARK}"/><line x1="0.5" y1="6" x2="0.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="focus-right"><rect x="54" y="6" width="6" height="48" fill="{C_VOID_DARK}"/><line x1="59.5" y1="6" x2="59.5" y2="54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="focus-bottomleft"><path d="M 6 60 A 6 6 0 0 1 0 54 L 6 54 Z" fill="{C_VOID_DARK}"/><path d="M 6 60 A 6 6 0 0 1 0 54" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
  <g id="focus-bottom"><rect x="6" y="54" width="48" height="6" fill="{C_VOID_DARK}"/><line x1="6" y1="59.5" x2="54" y2="59.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/></g>
  <g id="focus-bottomright"><path d="M 60 54 A 6 6 0 0 1 54 60 L 54 54 Z" fill="{C_VOID_DARK}"/><path d="M 60 54 A 6 6 0 0 1 54 60" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" fill="none"/></g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "lineedit.svg"), lineedit_svg)

    busy_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="vortexGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}"/>
      <stop offset="100%" stop-color="{C_NEBULA_MAG}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <g id="busywidget">
    <circle cx="32" cy="32" r="26" fill="none" stroke="url(#vortexGrad)" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="100 60"/>
    <circle cx="32" cy="6" r="3.5" fill="{C_STAR_WHITE}"/>
  </g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "busywidget.svg"), busy_svg)

    clock_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120">
  <defs>
    <radialGradient id="clockFace" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{C_VOID_CARD}"/>
      <stop offset="85%" stop-color="{C_VOID_MID}"/>
      <stop offset="100%" stop-color="{C_PULSAR_VIO}" stop-opacity="0.6"/>
    </radialGradient>
  </defs>
  <g id="ClockFace">
    <circle cx="60" cy="60" r="54" fill="url(#clockFace)" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/>
    <circle cx="60" cy="14" r="2.5" fill="{C_STAR_WHITE}"/>
    <circle cx="106" cy="60" r="2.5" fill="{C_STAR_WHITE}"/>
    <circle cx="60" cy="106" r="2.5" fill="{C_STAR_WHITE}"/>
    <circle cx="14" cy="60" r="2.5" fill="{C_STAR_WHITE}"/>
  </g>
  <g id="HourHand">
    <path d="M 58 60 L 59 28 L 61 28 L 62 60 Z" fill="{C_STAR_WHITE}"/>
  </g>
  <g id="MinuteHand">
    <path d="M 58.5 60 L 59.5 18 L 60.5 18 L 61.5 60 Z" fill="{C_STELLAR_CYAN}"/>
  </g>
  <g id="SecondHand">
    <line x1="60" y1="68" x2="60" y2="14" stroke="{C_NEBULA_MAG}" stroke-width="1.5"/>
    <circle cx="60" cy="60" r="3" fill="{C_NEBULA_MAG}"/>
  </g>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "clock.svg"), clock_svg)

    glowbar_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="20" viewBox="0 0 100 20">
  <defs>
    <linearGradient id="gbGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="{C_NEBULA_MAG}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect id="glowbar" x="0" y="8" width="100" height="4" fill="url(#gbGrad)"/>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "glowbar.svg"), glowbar_svg)

    arrows_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <path id="up-arrow" d="M 16 26 L 32 10 L 48 26" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="2.5" stroke-linecap="round"/>
  <path id="down-arrow" d="M 16 38 L 32 54 L 48 38" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="2.5" stroke-linecap="round"/>
  <path id="left-arrow" d="M 26 16 L 10 32 L 26 48" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="2.5" stroke-linecap="round"/>
  <path id="right-arrow" d="M 38 16 L 54 32 L 38 48" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="2.5" stroke-linecap="round"/>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "widgets", "arrows.svg"), arrows_svg)

    plasma_icon_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">
  <defs>
    <linearGradient id="galaxyCore" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}"/>
      <stop offset="100%" stop-color="{C_NEBULA_MAG}"/>
    </linearGradient>
  </defs>
  <circle cx="64" cy="64" r="54" fill="none" stroke="{C_PULSAR_VIO}" stroke-width="2" stroke-opacity="0.3"/>
  <path d="M 28 64 A 36 36 0 0 1 100 64 A 36 36 0 0 1 28 64" fill="none" stroke="url(#galaxyCore)" stroke-width="4" stroke-linecap="round" stroke-dasharray="140 40"/>
  <circle cx="64" cy="64" r="14" fill="url(#galaxyCore)"/>
  <circle cx="64" cy="64" r="7" fill="{C_STAR_WHITE}"/>
  <circle cx="92" cy="40" r="4" fill="{C_STELLAR_CYAN}"/>
  <circle cx="36" cy="88" r="4" fill="{C_NEBULA_MAG}"/>
  <circle cx="76" cy="98" r="3" fill="{C_SUPERNOVA_GOLD}"/>
</svg>'''
    write_file(os.path.join(PLASMA_DIR, "icons", "plasma.svg"), plasma_icon_svg)

# ==========================================
# 2. AURORAE WINDOW DECORATIONS
# ==========================================

def gen_aurorae_theme():
    import generate_aurorae
    generate_aurorae.main()


# ==========================================
# 3. CURSOR THEME VECTOR SOURCES
# ==========================================

def gen_cursor_svgs():
    index_theme = f'''[Icon Theme]
Name=Galaxy-Cursors
Comment=Galaxy Theme KDE - Luminous cosmic pointer theme by badcast <lmecomposer@gmail.com>
Inherits=breeze_cursors,Adwaita,core
'''
    write_file(os.path.join(BASE_DIR, "cursors", "Galaxy-Cursors", "index.theme"), index_theme)

    default_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <defs>
    <linearGradient id="ptrGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}"/>
      <stop offset="100%" stop-color="{C_NEBULA_MAG}"/>
    </linearGradient>
  </defs>
  <path d="M 7.5 7.5 L 17.5 35.5 L 22.5 25.5 L 33.5 23.5 Z" fill="#000000" opacity="0.6"/>
  <path d="M 7 7 L 17 35 L 22 25 L 33 23 Z" fill="#000000" opacity="0.8"/>
  <path d="M 6 6 L 16 34 L 21 24 L 32 22 Z" fill="#05070D" stroke="#000000" stroke-width="3" stroke-linejoin="round"/>
  <path d="M 6 6 L 15 32 L 20 22 L 30 20 Z" fill="url(#ptrGrad)" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linejoin="round"/>
  <circle cx="10" cy="10" r="1.5" fill="{C_STAR_WHITE}"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "default.svg"), default_svg)

    pointer_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <defs>
    <linearGradient id="handGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="100%" stop-color="{C_PULSAR_VIO}"/>
    </linearGradient>
  </defs>
  <path d="M 19 7 C 17 7 16 8.5 16 10.5 L 16 23 L 14 23 C 12 23 10.5 24.5 10.5 26.5 C 10.5 28 11.5 29 12.5 29.5 L 19 37 C 21 39.5 24 41 27 41 L 34 41 C 38 41 41 38 41 34 L 41 23 C 41 21 39.5 19.5 37.5 19.5 C 36.5 19.5 35.5 20 35 20.5 C 34.5 19 33 18 31 18 C 30 18 29 18.5 28.5 19 C 28 17.5 26.5 16.5 24.5 16.5 L 22.5 16.5 L 22.5 10.5 C 22.5 8.5 21 7 19 7 Z" fill="#000000" opacity="0.6"/>
  <path d="M 18 6 C 16 6 15 7.5 15 9.5 L 15 22 L 13 22 C 11 22 9.5 23.5 9.5 25.5 C 9.5 27 10.5 28 11.5 28.5 L 18 36 C 20 38.5 23 40 26 40 L 33 40 C 37 40 40 37 40 33 L 40 22 C 40 20 38.5 18.5 36.5 18.5 C 35.5 18.5 34.5 19 34 19.5 C 33.5 18 32 17 30 17 C 29 17 28 17.5 27.5 18 C 27 16.5 25.5 15.5 23.5 15.5 L 21.5 15.5 L 21.5 9.5 C 21.5 7.5 20 6 18 6 Z" fill="#05070D" stroke="#000000" stroke-width="3" stroke-linejoin="round"/>
  <path d="M 18 6 C 16 6 15 7.5 15 9.5 L 15 22 L 13 22 C 11 22 9.5 23.5 9.5 25.5 C 9.5 27 10.5 28 11.5 28.5 L 18 36 C 20 38.5 23 40 26 40 L 33 40 C 37 40 40 37 40 33 L 40 22 C 40 20 38.5 18.5 36.5 18.5 C 35.5 18.5 34.5 19 34 19.5 C 33.5 18 32 17 30 17 C 29 17 28 17.5 27.5 18 C 27 16.5 25.5 15.5 23.5 15.5 L 21.5 15.5 L 21.5 9.5 C 21.5 7.5 20 6 18 6 Z" fill="url(#handGrad)" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linejoin="round"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "pointer.svg"), pointer_svg)

    for i in range(8):
        angle = i * 45
        progress_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <defs>
    <linearGradient id="waitGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}"/>
      <stop offset="100%" stop-color="{C_NEBULA_MAG}" stop-opacity="0.1"/>
    </linearGradient>
  </defs>
  <circle cx="25" cy="25" r="17" fill="#000000" opacity="0.5"/>
  <circle cx="24" cy="24" r="17" fill="#05070D" stroke="#000000" stroke-width="2"/>
  <g transform="rotate({angle}, 24, 24)">
    <circle cx="24" cy="24" r="15" fill="none" stroke="url(#waitGrad)" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="65 35"/>
    <circle cx="24" cy="9" r="3.5" fill="{C_STAR_WHITE}" stroke="#000000" stroke-width="1"/>
    <circle cx="24" cy="24" r="5" fill="{C_PULSAR_VIO}" stroke="{C_STAR_WHITE}" stroke-width="1"/>
  </g>
</svg>'''
        write_file(os.path.join(CURSORS_DIR, f"progress_{i}.svg"), progress_svg)
        write_file(os.path.join(CURSORS_DIR, f"wait_{i}.svg"), progress_svg)

    text_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <path d="M 18 10 L 30 10 M 24 10 L 24 38 M 18 38 L 30 38" stroke="#000000" stroke-width="4.5" stroke-linecap="round"/>
  <path d="M 18 10 L 30 10 M 24 10 L 24 38 M 18 38 L 30 38" stroke="{C_STELLAR_CYAN}" stroke-width="2" stroke-linecap="round"/>
  <circle cx="24" cy="24" r="2.5" fill="{C_NEBULA_MAG}" stroke="{C_STAR_WHITE}" stroke-width="0.8"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "text.svg"), text_svg)

    crosshair_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <circle cx="24" cy="24" r="14" fill="none" stroke="#000000" stroke-width="3.5"/>
  <line x1="24" y1="4" x2="24" y2="44" stroke="#000000" stroke-width="3.5"/>
  <line x1="4" y1="24" x2="44" y2="24" stroke="#000000" stroke-width="3.5"/>
  <circle cx="24" cy="24" r="14" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.8"/>
  <line x1="24" y1="4" x2="24" y2="16" stroke="{C_STELLAR_CYAN}" stroke-width="2"/>
  <line x1="24" y1="32" x2="24" y2="44" stroke="{C_STELLAR_CYAN}" stroke-width="2"/>
  <line x1="4" y1="24" x2="16" y2="24" stroke="{C_STELLAR_CYAN}" stroke-width="2"/>
  <line x1="32" y1="24" x2="44" y2="24" stroke="{C_STELLAR_CYAN}" stroke-width="2"/>
  <circle cx="24" cy="24" r="2.5" fill="{C_NEBULA_MAG}" stroke="{C_STAR_WHITE}" stroke-width="0.8"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "crosshair.svg"), crosshair_svg)

    move_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <g transform="translate(1, 1)" opacity="0.6">
    <path d="M 24 6 L 19 12 L 29 12 Z M 24 42 L 19 36 L 29 36 Z M 6 24 L 12 19 L 12 29 Z M 42 24 L 36 19 L 36 29 Z" fill="#000000"/>
    <line x1="24" y1="12" x2="24" y2="36" stroke="#000000" stroke-width="3"/>
    <line x1="12" y1="24" x2="36" y2="24" stroke="#000000" stroke-width="3"/>
  </g>
  <path d="M 24 6 L 19 12 L 29 12 Z M 24 42 L 19 36 L 29 36 Z M 6 24 L 12 19 L 12 29 Z M 42 24 L 36 19 L 36 29 Z" fill="{C_STELLAR_CYAN}" stroke="#000000" stroke-width="1"/>
  <line x1="24" y1="12" x2="24" y2="36" stroke="{C_STELLAR_CYAN}" stroke-width="2"/>
  <line x1="12" y1="24" x2="36" y2="24" stroke="{C_STELLAR_CYAN}" stroke-width="2"/>
  <circle cx="24" cy="24" r="3.5" fill="{C_PULSAR_VIO}" stroke="{C_STAR_WHITE}" stroke-width="1"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "move.svg"), move_svg)

    col_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <g transform="translate(1, 1)" opacity="0.6">
    <path d="M 6 24 L 14 17 L 14 31 Z M 42 24 L 34 17 L 34 31 Z" fill="#000000"/>
    <line x1="14" y1="24" x2="34" y2="24" stroke="#000000" stroke-width="3.5"/>
    <line x1="21" y1="14" x2="21" y2="34" stroke="#000000" stroke-width="3"/>
    <line x1="27" y1="14" x2="27" y2="34" stroke="#000000" stroke-width="3"/>
  </g>
  <path d="M 6 24 L 14 17 L 14 31 Z M 42 24 L 34 17 L 34 31 Z" fill="{C_STELLAR_CYAN}" stroke="#000000" stroke-width="1"/>
  <line x1="14" y1="24" x2="34" y2="24" stroke="{C_STELLAR_CYAN}" stroke-width="2"/>
  <line x1="21" y1="14" x2="21" y2="34" stroke="{C_STAR_WHITE}" stroke-width="1.8"/>
  <line x1="27" y1="14" x2="27" y2="34" stroke="{C_STAR_WHITE}" stroke-width="1.8"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "col-resize.svg"), col_svg)

    row_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <g transform="translate(1, 1)" opacity="0.6">
    <path d="M 24 6 L 17 14 L 31 14 Z M 24 42 L 17 34 L 31 34 Z" fill="#000000"/>
    <line x1="24" y1="14" x2="24" y2="34" stroke="#000000" stroke-width="3.5"/>
    <line x1="14" y1="21" x2="34" y2="21" stroke="#000000" stroke-width="3"/>
    <line x1="14" y1="27" x2="34" y2="27" stroke="#000000" stroke-width="3"/>
  </g>
  <path d="M 24 6 L 17 14 L 31 14 Z M 24 42 L 17 34 L 31 34 Z" fill="{C_STELLAR_CYAN}" stroke="#000000" stroke-width="1"/>
  <line x1="24" y1="14" x2="24" y2="34" stroke="{C_STELLAR_CYAN}" stroke-width="2"/>
  <line x1="14" y1="21" x2="34" y2="21" stroke="{C_STAR_WHITE}" stroke-width="1.8"/>
  <line x1="14" y1="27" x2="34" y2="27" stroke="{C_STAR_WHITE}" stroke-width="1.8"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "row-resize.svg"), row_svg)

    forbidden_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <circle cx="25" cy="25" r="16" fill="#000000" opacity="0.5"/>
  <circle cx="24" cy="24" r="16" fill="#05070D" stroke="#000000" stroke-width="4"/>
  <circle cx="24" cy="24" r="15" fill="{C_DANGER_RED}" fill-opacity="0.3" stroke="{C_DANGER_RED}" stroke-width="2.5"/>
  <line x1="13" y1="13" x2="35" y2="35" stroke="{C_STAR_WHITE}" stroke-width="2.5" stroke-linecap="round"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "not-allowed.svg"), forbidden_svg)

    help_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <path d="M 7 7 L 17 35 L 22 25 L 33 23 Z" fill="#000000" opacity="0.7"/>
  <path d="M 6 6 L 16 34 L 21 24 L 32 22 Z" fill="#05070D" stroke="#000000" stroke-width="3" stroke-linejoin="round"/>
  <path d="M 6 6 L 15 32 L 20 22 L 30 20 Z" fill="{C_STELLAR_CYAN}" stroke="{C_STAR_WHITE}" stroke-width="1.2"/>
  <circle cx="34" cy="30" r="10" fill="{C_PULSAR_VIO}" stroke="#000000" stroke-width="2"/>
  <path d="M 31 27 C 31 25 37 25 37 28 C 37 30 34 30 34 32" fill="none" stroke="{C_STAR_WHITE}" stroke-width="1.8" stroke-linecap="round"/>
  <circle cx="34" cy="36" r="1.2" fill="{C_STAR_WHITE}"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "help.svg"), help_svg)

    pirate_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <defs>
    <linearGradient id="skullGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_DANGER_RED}"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}"/>
      <stop offset="100%" stop-color="{C_STELLAR_CYAN}"/>
    </linearGradient>
  </defs>
  <!-- Shadow crossbones -->
  <g stroke="#000000" stroke-width="5" stroke-linecap="round" opacity="0.7">
    <line x1="8" y1="8" x2="40" y2="40"/>
    <line x1="40" y1="8" x2="8" y2="40"/>
  </g>
  <!-- Crossbones background -->
  <g stroke="#05070D" stroke-width="4.2" stroke-linecap="round">
    <line x1="8" y1="8" x2="40" y2="40"/>
    <line x1="40" y1="8" x2="8" y2="40"/>
  </g>
  <!-- Crossbones neon lasers -->
  <g stroke="{C_DANGER_RED}" stroke-width="2.2" stroke-linecap="round">
    <line x1="8" y1="8" x2="40" y2="40"/>
    <line x1="40" y1="8" x2="8" y2="40"/>
    <circle cx="8" cy="8" r="2.5" fill="{C_STAR_WHITE}"/>
    <circle cx="40" cy="8" r="2.5" fill="{C_STAR_WHITE}"/>
    <circle cx="8" cy="40" r="2.5" fill="{C_STAR_WHITE}"/>
    <circle cx="40" cy="40" r="2.5" fill="{C_STAR_WHITE}"/>
  </g>
  <!-- Skull Drop Shadow -->
  <path d="M 24 10 C 16 10 13 16 13 22 C 13 26 15 28 17 30 L 17 35 C 17 36 18 37 19 37 L 29 37 C 30 37 31 36 31 35 L 31 30 C 33 28 35 26 35 22 C 35 16 32 10 24 10 Z" fill="#000000" opacity="0.75"/>
  <!-- Skull Base Outline -->
  <path d="M 24 9 C 15.5 9 12 15.5 12 21.5 C 12 25.5 14 27.5 16 29.5 L 16 34.5 C 16 36 17.5 37 19 37 L 29 37 C 30.5 37 32 36 32 34.5 L 32 29.5 C 34 27.5 36 25.5 36 21.5 C 36 15.5 32.5 9 24 9 Z" fill="#05070D" stroke="#000000" stroke-width="3" stroke-linejoin="round"/>
  <!-- Skull Cranium Fill & Neon Stroke -->
  <path d="M 24 9 C 15.5 9 12 15.5 12 21.5 C 12 25.5 14 27.5 16 29.5 L 16 34.5 C 16 36 17.5 37 19 37 L 29 37 C 30.5 37 32 36 32 34.5 L 32 29.5 C 34 27.5 36 25.5 36 21.5 C 36 15.5 32.5 9 24 9 Z" fill="url(#skullGrad)" stroke="{C_STAR_WHITE}" stroke-width="1.3" stroke-linejoin="round"/>
  <!-- Eye sockets (Glowing Singularity) -->
  <ellipse cx="19" cy="22" rx="3.2" ry="4" fill="{C_VOID_DARK}" stroke="{C_STAR_WHITE}" stroke-width="0.9"/>
  <ellipse cx="29" cy="22" rx="3.2" ry="4" fill="{C_VOID_DARK}" stroke="{C_STAR_WHITE}" stroke-width="0.9"/>
  <circle cx="19" cy="22" r="1.4" fill="{C_STELLAR_CYAN}"/>
  <circle cx="29" cy="22" r="1.4" fill="{C_STELLAR_CYAN}"/>
  <!-- Nose (Inverted triangle) -->
  <path d="M 24 25.5 L 22.5 28.5 L 25.5 28.5 Z" fill="{C_VOID_DARK}"/>
  <!-- Teeth / Cyber jaw grid -->
  <line x1="20" y1="32.5" x2="20" y2="36" stroke="{C_STAR_WHITE}" stroke-width="1.2"/>
  <line x1="24" y1="32.5" x2="24" y2="36" stroke="{C_STAR_WHITE}" stroke-width="1.2"/>
  <line x1="28" y1="32.5" x2="28" y2="36" stroke="{C_STAR_WHITE}" stroke-width="1.2"/>
  <line x1="17.5" y1="33" x2="30.5" y2="33" stroke="{C_STAR_WHITE}" stroke-width="1.0"/>
</svg>'''
    write_file(os.path.join(CURSORS_DIR, "pirate.svg"), pirate_svg)

# ==========================================
# 4. SPLASH SCREEN ASSETS
# ==========================================

def gen_splash_assets():
    galaxy_core_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
  <defs>
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}"/>
      <stop offset="50%" stop-color="{C_PULSAR_VIO}"/>
      <stop offset="100%" stop-color="{C_NEBULA_MAG}"/>
    </linearGradient>
    <radialGradient id="nebulaGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{C_PULSAR_VIO}" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="{C_STELLAR_CYAN}" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="{C_VOID_DARK}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="128" cy="128" r="120" fill="url(#nebulaGlow)"/>
  <path d="M 40 128 C 40 60 90 20 160 30 C 220 40 240 100 220 160 C 200 220 140 240 80 220 C 30 200 20 140 40 128" fill="none" stroke="url(#coreGrad)" stroke-width="5" stroke-linecap="round" stroke-dasharray="300 80"/>
  <path d="M 80 128 C 80 80 110 50 160 60 C 200 70 210 110 200 150 C 190 190 150 200 110 190 C 80 180 70 140 80 128" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="3" stroke-linecap="round" stroke-dasharray="180 60"/>
  <circle cx="128" cy="128" r="28" fill="url(#coreGrad)"/>
  <circle cx="128" cy="128" r="14" fill="{C_STAR_WHITE}"/>
  <circle cx="190" cy="70" r="6" fill="{C_STELLAR_CYAN}"/>
  <circle cx="65" cy="180" r="6" fill="{C_NEBULA_MAG}"/>
  <circle cx="160" cy="210" r="5" fill="{C_SUPERNOVA_GOLD}"/>
  <circle cx="70" cy="80" r="4" fill="{C_AURORA_EMERALD}"/>
</svg>'''
    write_file(os.path.join(SPLASH_DIR, "galaxy-core.svg"), galaxy_core_svg)

    star_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
  <circle cx="16" cy="16" r="4" fill="{C_STAR_WHITE}"/>
  <line x1="16" y1="2" x2="16" y2="30" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/>
  <line x1="2" y1="16" x2="30" y2="16" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/>
</svg>'''
    write_file(os.path.join(SPLASH_DIR, "star.svg"), star_svg)

def main():
    print("==========================================")
    print("Generating Galaxy Plasma 6 Assets")
    print("==========================================")
    gen_plasma_panel_background()
    gen_plasma_tasks()
    gen_plasma_bar_meter()
    gen_plasma_slider()
    gen_plasma_tooltip()
    gen_plasma_button()
    gen_plasma_other_widgets()
    import generate_aurorae
    generate_aurorae.main()
    gen_cursor_svgs()
    gen_splash_assets()
    print("==========================================")
    print("Plasma assets generated!")
    print("==========================================")

if __name__ == "__main__":
    main()
