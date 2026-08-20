#!/usr/bin/env python3
import os

PLASMA_ICONS_DIR = "/media/dev/Kde6-desktoptheme/plasma/desktoptheme/Galaxy-Dark/icons"
GALAXY_ICONS_STATUS = "/media/dev/Kde6-desktoptheme/icons/Galaxy-Icons/scalable/status"
os.makedirs(PLASMA_ICONS_DIR, exist_ok=True)
os.makedirs(GALAXY_ICONS_STATUS, exist_ok=True)

C_CYAN = "#00F0FF"
C_CYAN_GLOW = "#38BDF8"
C_CRIMSON = "#FF2E63"
C_GOLD = "#FBBF24"
C_WHITE = "#F8FAFC"
C_MUTED = "#64748B"

def gen_audio_svg():
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 110 54" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style id="current-color-scheme" type="text/css">
      .ColorScheme-Text {{ color: {C_CYAN}; }}
      .ColorScheme-Highlight {{ color: {C_CYAN_GLOW}; }}
      .ColorScheme-NeutralText {{ color: {C_GOLD}; }}
      .ColorScheme-NegativeText {{ color: {C_CRIMSON}; }}
    </style>
    <linearGradient id="speakerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{C_CYAN}"/>
      <stop offset="100%" stop-color="{C_CYAN_GLOW}"/>
    </linearGradient>
  </defs>

  <!-- 22x22 audio-volume-high (x=0..22) -->
  <g id="audio-volume-high">
    <rect x="0" y="0" width="22" height="22" fill="none"/>
    <g class="ColorScheme-Text" fill="currentColor">
      <path d="M 3 8 L 6 8 L 10 4 L 10 18 L 6 14 L 3 14 Z" fill="url(#speakerGrad)" stroke="{C_CYAN}" stroke-width="0.8" stroke-linejoin="round"/>
      <path d="M 12.5 8.5 C 13.8 9.8 13.8 12.2 12.5 13.5" fill="none" stroke="{C_CYAN}" stroke-width="1.6" stroke-linecap="round"/>
      <path d="M 15 6.5 C 17.5 9 17.5 13 15 15.5" fill="none" stroke="{C_CYAN}" stroke-width="1.6" stroke-linecap="round"/>
      <path d="M 17.5 4.5 C 21 8 21 14 17.5 17.5" fill="none" stroke="{C_CYAN}" stroke-width="1.6" stroke-linecap="round"/>
    </g>
  </g>

  <!-- 22x22 audio-volume-medium (x=22..44) -->
  <g id="audio-volume-medium">
    <rect x="22" y="0" width="22" height="22" fill="none"/>
    <g class="ColorScheme-Text" fill="currentColor">
      <path d="M 25 8 L 28 8 L 32 4 L 32 18 L 28 14 L 25 14 Z" fill="url(#speakerGrad)" stroke="{C_CYAN}" stroke-width="0.8" stroke-linejoin="round"/>
      <path d="M 34.5 8.5 C 35.8 9.8 35.8 12.2 34.5 13.5" fill="none" stroke="{C_CYAN}" stroke-width="1.6" stroke-linecap="round"/>
      <path d="M 37 6.5 C 39.5 9 39.5 13 37 15.5" fill="none" stroke="{C_CYAN}" stroke-width="1.6" stroke-linecap="round"/>
      <path d="M 39.5 4.5 C 43 8 43 14 39.5 17.5" fill="none" stroke="{C_MUTED}" stroke-width="1.2" stroke-linecap="round" opacity="0.25"/>
    </g>
  </g>

  <!-- 22x22 audio-volume-low (x=44..66) -->
  <g id="audio-volume-low">
    <rect x="44" y="0" width="22" height="22" fill="none"/>
    <g class="ColorScheme-Text" fill="currentColor">
      <path d="M 47 8 L 50 8 L 54 4 L 54 18 L 50 14 L 47 14 Z" fill="url(#speakerGrad)" stroke="{C_CYAN}" stroke-width="0.8" stroke-linejoin="round"/>
      <path d="M 56.5 8.5 C 57.8 9.8 57.8 12.2 56.5 13.5" fill="none" stroke="{C_CYAN}" stroke-width="1.6" stroke-linecap="round"/>
      <path d="M 59 6.5 C 61.5 9 61.5 13 59 15.5" fill="none" stroke="{C_MUTED}" stroke-width="1.2" stroke-linecap="round" opacity="0.25"/>
      <path d="M 61.5 4.5 C 65 8 65 14 61.5 17.5" fill="none" stroke="{C_MUTED}" stroke-width="1.2" stroke-linecap="round" opacity="0.25"/>
    </g>
  </g>

  <!-- 22x22 audio-volume-muted (x=66..88) -->
  <g id="audio-volume-muted">
    <rect x="66" y="0" width="22" height="22" fill="none"/>
    <g fill="currentColor">
      <path d="M 69 8 L 72 8 L 76 4 L 76 18 L 72 14 L 69 14 Z" fill="{C_MUTED}" opacity="0.5" stroke="{C_MUTED}" stroke-width="0.8" stroke-linejoin="round"/>
      <line x1="68" y1="4" x2="86" y2="18" stroke="{C_CRIMSON}" stroke-width="2.2" stroke-linecap="round"/>
      <line x1="68" y1="4" x2="86" y2="18" stroke="#FFFFFF" stroke-width="0.8" stroke-linecap="round" opacity="0.8"/>
    </g>
  </g>

  <!-- 16x16 icons -->
  <g id="16-16-audio-volume-high">
    <rect x="0" y="24" width="16" height="16" fill="none"/>
    <g class="ColorScheme-Text" fill="currentColor">
      <path d="M 2 30 L 4 30 L 7 27 L 7 37 L 4 34 L 2 34 Z" fill="url(#speakerGrad)" stroke="{C_CYAN}" stroke-width="0.6"/>
      <path d="M 9 29.5 C 10.2 30.7 10.2 33.3 9 34.5" fill="none" stroke="{C_CYAN}" stroke-width="1.4" stroke-linecap="round"/>
      <path d="M 11.5 27.5 C 13.8 29.8 13.8 34.2 11.5 36.5" fill="none" stroke="{C_CYAN}" stroke-width="1.4" stroke-linecap="round"/>
    </g>
  </g>

  <g id="16-16-audio-volume-medium">
    <rect x="16" y="24" width="16" height="16" fill="none"/>
    <g class="ColorScheme-Text" fill="currentColor">
      <path d="M 18 30 L 20 30 L 23 27 L 23 37 L 20 34 L 18 34 Z" fill="url(#speakerGrad)" stroke="{C_CYAN}" stroke-width="0.6"/>
      <path d="M 25 29.5 C 26.2 30.7 26.2 33.3 25 34.5" fill="none" stroke="{C_CYAN}" stroke-width="1.4" stroke-linecap="round"/>
    </g>
  </g>

  <g id="16-16-audio-volume-low">
    <rect x="32" y="24" width="16" height="16" fill="none"/>
    <g class="ColorScheme-Text" fill="currentColor">
      <path d="M 34 30 L 36 30 L 39 27 L 39 37 L 36 34 L 34 34 Z" fill="url(#speakerGrad)" stroke="{C_CYAN}" stroke-width="0.6"/>
      <path d="M 41 29.5 C 42.2 30.7 42.2 33.3 41 34.5" fill="none" stroke="{C_CYAN}" stroke-width="1.4" stroke-linecap="round"/>
    </g>
  </g>

  <g id="16-16-audio-volume-muted">
    <rect x="48" y="24" width="16" height="16" fill="none"/>
    <g fill="currentColor">
      <path d="M 50 30 L 52 30 L 55 27 L 55 37 L 52 34 L 50 34 Z" fill="{C_MUTED}" opacity="0.5"/>
      <line x1="49" y1="26" x2="63" y2="38" stroke="{C_CRIMSON}" stroke-width="1.8" stroke-linecap="round"/>
    </g>
  </g>
</svg>"""
    path = os.path.join(PLASMA_ICONS_DIR, "audio.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg.strip() + "\n")
    print(f"Generated: {path}")

def gen_notification_svg():
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 110 54" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style id="current-color-scheme" type="text/css">
      .ColorScheme-Text {{ color: {C_CYAN}; }}
      .ColorScheme-Highlight {{ color: {C_CYAN_GLOW}; }}
      .ColorScheme-NegativeText {{ color: {C_CRIMSON}; }}
      .ColorScheme-NeutralText {{ color: {C_GOLD}; }}
    </style>
  </defs>

  <g id="notification-inactive">
    <rect x="0" y="0" width="22" height="22" fill="none"/>
    <g class="ColorScheme-Text" fill="currentColor">
      <path d="M 11 3 C 10.4 3 10 3.4 10 4 C 8.2 4.4 7 6 7 8 L 7 13 L 5 15 L 5 16 L 17 16 L 17 15 L 15 13 L 15 8 C 15 6 13.8 4.4 12 4 C 12 3.4 11.6 3 11 3 Z M 9.5 17 C 9.5 17.8 10.2 18.5 11 18.5 C 11.8 18.5 12.5 17.8 12.5 17 Z" fill="{C_CYAN}" opacity="0.9"/>
    </g>
  </g>

  <g id="notification-active">
    <rect x="22" y="0" width="22" height="22" fill="none"/>
    <g class="ColorScheme-Text" fill="currentColor">
      <path d="M 33 3 C 32.4 3 32 3.4 32 4 C 30.2 4.4 29 6 29 8 L 29 13 L 27 15 L 27 16 L 39 16 L 39 15 L 37 13 L 37 8 C 37 6 35.8 4.4 34 4 C 34 3.4 33.6 3 33 3 Z M 31.5 17 C 31.5 17.8 32.2 18.5 33 18.5 C 33.8 18.5 34.5 17.8 34.5 17 Z" fill="{C_CYAN}"/>
      <path d="M 26 5 C 24.5 6.5 24.5 9.5 26 11" fill="none" stroke="{C_CYAN_GLOW}" stroke-width="1.4" stroke-linecap="round"/>
      <path d="M 40 5 C 41.5 6.5 41.5 9.5 40 11" fill="none" stroke="{C_CYAN_GLOW}" stroke-width="1.4" stroke-linecap="round"/>
      <circle cx="37" cy="5" r="2.5" fill="{C_CRIMSON}"/>
      <circle cx="37" cy="5" r="1.2" fill="#FFFFFF"/>
    </g>
  </g>

  <g id="notification-disabled">
    <rect x="44" y="0" width="22" height="22" fill="none"/>
    <g fill="currentColor">
      <path d="M 55 3 C 54.4 3 54 3.4 54 4 C 52.2 4.4 51 6 51 8 L 51 13 L 49 15 L 49 16 L 61 16 L 61 15 L 59 13 L 59 8 C 59 6 57.8 4.4 56 4 C 56 3.4 55.6 3 55 3 Z" fill="{C_MUTED}" opacity="0.45"/>
      <line x1="46" y1="4" x2="64" y2="18" stroke="{C_CRIMSON}" stroke-width="2.0" stroke-linecap="round"/>
    </g>
  </g>

  <g id="notification-progress-active">
    <rect x="66" y="0" width="22" height="22" fill="none"/>
    <circle cx="77" cy="11" r="7" fill="none" stroke="{C_CYAN}" stroke-width="2.0"/>
    <circle cx="77" cy="11" r="3" fill="{C_CYAN_GLOW}"/>
  </g>

  <g id="notification-progress-inactive">
    <rect x="88" y="0" width="22" height="22" fill="none"/>
    <circle cx="99" cy="11" r="7" fill="none" stroke="{C_MUTED}" stroke-width="1.5" opacity="0.4"/>
  </g>

  <path id="expander-bottom" d="M 1 28 L 5 32 L 9 28 Z" fill="{C_CYAN}"/>
  <path id="expander-top" d="M 1 36 L 5 32 L 9 36 Z" fill="{C_CYAN}"/>
  <path id="expander-right" d="M 12 28 L 16 32 L 12 36 Z" fill="{C_CYAN}"/>
  <path id="expander-left" d="M 20 28 L 16 32 L 20 36 Z" fill="{C_CYAN}"/>
</svg>"""
    path = os.path.join(PLASMA_ICONS_DIR, "notification.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg.strip() + "\n")
    print(f"Generated: {path}")

def sync_aliases():
    alias_map = {
        "audio-volume-high.svg": [
            "notification-audio-volume-high.svg",
            "volume-level-high-symbolic.svg",
            "audio-volume-high-symbolic.svg"
        ],
        "audio-volume-medium.svg": [
            "notification-audio-volume-medium.svg",
            "volume-level-medium-symbolic.svg",
            "audio-volume-medium-symbolic.svg"
        ],
        "audio-volume-low.svg": [
            "notification-audio-volume-low.svg",
            "volume-level-low-symbolic.svg",
            "audio-volume-low-symbolic.svg"
        ],
        "audio-volume-muted.svg": [
            "notification-audio-volume-muted.svg",
            "volume-level-muted-symbolic.svg",
            "audio-volume-muted-symbolic.svg",
            "audio-volume-off.svg",
            "audio-volume-off-symbolic.svg"
        ]
    }
    for src_name, aliases in alias_map.items():
        src_path = os.path.join(GALAXY_ICONS_STATUS, src_name)
        if os.path.exists(src_path):
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
            for alias in aliases:
                dest_path = os.path.join(GALAXY_ICONS_STATUS, alias)
                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Synced icon alias: {alias}")

if __name__ == "__main__":
    gen_audio_svg()
    gen_notification_svg()
    sync_aliases()
    print("Plasma desktop icons generated successfully!")
