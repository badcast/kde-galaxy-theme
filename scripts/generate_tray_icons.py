#!/usr/bin/env python3
"""
Galaxy Theme KDE - Master System Tray & Status Icon Suite (Cosmic Squircle Neon Tiles)
Author:  badcast <lmecomposer@gmail.com>
Project: Galaxy Theme KDE

Designs ALL Notification Panel & System Tray icons in the cosmic glassmorphic
squircle neon-tile aesthetic (24x24 squircle with cyan-pulsar gradient border,
dark obsidian void container, and glowing neon line-art symbol).
Includes 100% complete FreeDesktop & KDE 6 status naming conventions:
- Wi-Fi & Wired Networks & VPN
- Battery & Charging States (Complete battery-000-charging, battery-charging-000, symbolic, profile, ac-adapter)
- Bluetooth & Peripherals
- Audio Volume & Microphone Meters
- Notifications, Clipboard (Klipper), Night Light, KDE Connect
- Printers & Printing states (printer, printing, error, network)
- Keyboard Layout & Language / Locale
- Media Player tray playback controls
- Plasma Vault & Security / Encryption
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_ROOT = os.path.join(BASE_DIR, "icons", "Galaxy-Icons")
SCALABLE_DIR = os.path.join(ICONS_ROOT, "scalable")

# Cosmic Palette
C_VOID_ABYSS    = "#060810"
C_VOID_DARK     = "#0B0E17"
C_VOID_MID      = "#0F1426"
C_VOID_CARD     = "#1A2238"
C_VOID_BORDER   = "#2A3558"
C_PULSAR_VIO    = "#00F0FF"
C_NEBULA_MAG    = "#00F0FF"
C_STELLAR_CYAN  = "#00F0FF"
C_SUPERNOVA_GOLD= "#FBBF24"
C_AURORA_EMERALD= "#10B981"
C_STAR_WHITE    = "#F8FAFC"
C_STARDUST      = "#94A3B8"
C_DANGER_RED    = "#FF4565"

def write_svg(category, filename, svg_content):
    path = os.path.join(SCALABLE_DIR, category, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip() + "\n")

def make_symlink(category, target_filename, link_filename):
    cat_dir = os.path.join(SCALABLE_DIR, category)
    link_path = os.path.join(cat_dir, link_filename)
    target_path = os.path.join(cat_dir, target_filename)
    if os.path.exists(link_path) or os.path.islink(link_path):
        try:
            os.remove(link_path)
        except OSError:
            pass
    if os.path.exists(target_path):
        os.symlink(target_filename, link_path)

def make_tray_svg(content, border_c1=C_STELLAR_CYAN, border_c2=C_PULSAR_VIO, bg_opacity=0.92):
    """
    Creates a 24x24 Cosmic Squircle Tile:
    - Dark obsidian void background
    - Luminous neon gradient rim (Cyan -> Pulsar Violet)
    - Specular inner glass edge
    - Glowing neon line-art symbol inside
    """
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <defs>
    <linearGradient id="tileBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{border_c1}"/>
      <stop offset="100%" stop-color="{border_c2}"/>
    </linearGradient>
    <linearGradient id="tileBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{C_VOID_CARD}" stop-opacity="{bg_opacity}"/>
      <stop offset="100%" stop-color="{C_VOID_DARK}" stop-opacity="{bg_opacity}"/>
    </linearGradient>
  </defs>
  <!-- Cosmic Squircle Tile -->
  <rect x="1.5" y="1.5" width="21" height="21" rx="5.5" fill="url(#tileBg)" stroke="url(#tileBorder)" stroke-width="1.2"/>
  <rect x="2.5" y="2.5" width="19" height="19" rx="4.5" fill="none" stroke="{C_STAR_WHITE}" stroke-opacity="0.12" stroke-width="0.8"/>
  <!-- Glowing Neon Content -->
  {content}
</svg>'''

def gen_all_tray_icons():
    print("==========================================")
    print("Generating Galaxy Cosmic Squircle System Tray Icons")
    print("==========================================")

    # ----------------------------------------------------
    # 1. WI-FI & WIRELESS NETWORKS (Cosmic Squircle Style)
    # ----------------------------------------------------
    def make_wifi_svg(pct):
        r1 = f'<path d="M 5 7.5 C 9 3.5 15 3.5 19 7.5" fill="none" stroke="{C_STELLAR_CYAN if pct >= 100 else C_STARDUST}" stroke-width="1.8" stroke-linecap="round" opacity="{1.0 if pct >= 100 else 0.3}"/>'
        r2 = f'<path d="M 7.5 10.5 C 10.2 7.8 13.8 7.8 16.5 10.5" fill="none" stroke="{C_STELLAR_CYAN if pct >= 75 else C_STARDUST}" stroke-width="1.8" stroke-linecap="round" opacity="{1.0 if pct >= 75 else 0.3}"/>'
        r3 = f'<path d="M 10 13.5 C 11.2 12.3 12.8 12.3 14 13.5" fill="none" stroke="{C_STELLAR_CYAN if pct >= 50 else C_STARDUST}" stroke-width="1.8" stroke-linecap="round" opacity="{1.0 if pct >= 50 else 0.3}"/>'
        dot = f'<circle cx="12" cy="16.5" r="1.3" fill="{C_STAR_WHITE if pct >= 25 else C_STARDUST}" opacity="{1.0 if pct >= 25 else 0.4}"/>'
        return make_tray_svg(f"{r1}{r2}{r3}{dot}")

    write_svg("status", "network-wireless-connected-100.svg", make_wifi_svg(100))
    write_svg("status", "network-wireless-connected-75.svg", make_wifi_svg(75))
    write_svg("status", "network-wireless-connected-50.svg", make_wifi_svg(50))
    write_svg("status", "network-wireless-connected-25.svg", make_wifi_svg(25))
    write_svg("status", "network-wireless-connected-00.svg", make_wifi_svg(0))
    write_svg("status", "network-wireless-disconnected.svg", make_tray_svg(f'''<path d="M 5 7.5 C 9 3.5 15 3.5 19 7.5" fill="none" stroke="{C_STARDUST}" stroke-width="1.8" stroke-linecap="round" opacity="0.35"/><line x1="5" y1="5" x2="19" y2="19" stroke="{C_DANGER_RED}" stroke-width="1.8" stroke-linecap="round"/>''', border_c1=C_DANGER_RED, border_c2=C_VOID_BORDER))

    make_symlink("status", "network-wireless-connected-100.svg", "network-wireless.svg")
    make_symlink("status", "network-wireless-connected-100.svg", "network-wireless-symbolic.svg")
    make_symlink("status", "network-wireless-connected-100.svg", "network-wireless-signal-excellent.svg")
    make_symlink("status", "network-wireless-connected-75.svg", "network-wireless-signal-good.svg")
    make_symlink("status", "network-wireless-connected-50.svg", "network-wireless-signal-ok.svg")
    make_symlink("status", "network-wireless-connected-25.svg", "network-wireless-signal-weak.svg")
    make_symlink("status", "network-wireless-connected-00.svg", "network-wireless-signal-none.svg")

    # Wired Ethernet & VPN
    write_svg("status", "network-wired.svg", make_tray_svg(f'''<rect x="5.5" y="5.5" width="13" height="9" rx="2" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><line x1="8.5" y1="14.5" x2="8.5" y2="17.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/><line x1="15.5" y1="14.5" x2="15.5" y2="17.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/><line x1="5.5" y1="17.5" x2="18.5" y2="17.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/>'''))
    write_svg("status", "network-wired-activated.svg", make_tray_svg(f'''<rect x="5.5" y="5.5" width="13" height="9" rx="2" fill="{C_STELLAR_CYAN}" fill-opacity="0.2" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><circle cx="12" cy="10" r="2" fill="{C_AURORA_EMERALD}"/><line x1="8.5" y1="14.5" x2="8.5" y2="17.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/><line x1="15.5" y1="14.5" x2="15.5" y2="17.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/><line x1="5.5" y1="17.5" x2="18.5" y2="17.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/>'''))
    write_svg("status", "network-wired-disconnected.svg", make_tray_svg(f'''<rect x="5.5" y="5.5" width="13" height="9" rx="2" fill="none" stroke="{C_STARDUST}" stroke-width="1.6" opacity="0.4"/><line x1="5" y1="5" x2="19" y2="19" stroke="{C_DANGER_RED}" stroke-width="1.8" stroke-linecap="round"/>''', border_c1=C_DANGER_RED, border_c2=C_VOID_BORDER))
    write_svg("status", "network-vpn.svg", make_tray_svg(f'''<rect x="5.5" y="10" width="13" height="8" rx="2" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><path d="M 8.5 10 L 8.5 7 C 8.5 5.2 9.8 4 12 4 C 14.2 4 15.5 5.2 15.5 7 L 15.5 10" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="14" r="1.3" fill="{C_SUPERNOVA_GOLD}"/>'''))
    make_symlink("status", "network-wired-activated.svg", "network-wired-symbolic.svg")
    make_symlink("status", "network-vpn.svg", "network-vpn-symbolic.svg")
    make_symlink("status", "network-vpn.svg", "network-vpn-activated.svg")

    # ----------------------------------------------------
    # 2. BATTERY & COMPLETE CHARGING STATES (All KDE 6 Naming Specs)
    # ----------------------------------------------------
    def make_battery_svg(level_pct, charging=False, caution=False):
        fill_col = C_DANGER_RED if (caution or level_pct <= 15) else (C_SUPERNOVA_GOLD if level_pct <= 35 else (C_AURORA_EMERALD if level_pct >= 90 else C_STELLAR_CYAN))
        fill_w = max(0, min(8.5, round(8.5 * (level_pct / 100.0), 1)))
        
        # Battery body outline
        body = f'<rect x="5.5" y="7.5" width="11.5" height="9" rx="2" fill="none" stroke="{C_STAR_WHITE}" stroke-width="1.4"/>'
        # Terminal cap
        cap = f'<path d="M 17 9.5 C 18 9.5 18.2 10.2 18.2 12 C 18.2 13.8 18 14.5 17 14.5" fill="none" stroke="{C_STAR_WHITE}" stroke-width="1.4" stroke-linecap="round"/>'
        # Level fill
        fill_rect = f'<rect x="7" y="9" width="{fill_w}" height="6" rx="1" fill="{fill_col}"/>' if fill_w > 0 else ''
        
        # Luminous charging lightning bolt
        bolt = f'''<polygon points="12,4.5 8,11.5 11.2,11.5 10,19.5 16,10.5 12.8,10.5" fill="{C_SUPERNOVA_GOLD}" stroke="{C_VOID_DARK}" stroke-width="0.8"/>
<circle cx="12" cy="11.5" r="1.0" fill="{C_STAR_WHITE}"/>''' if charging else ''
        
        border_c1 = C_SUPERNOVA_GOLD if charging else (C_DANGER_RED if caution else C_STELLAR_CYAN)
        border_c2 = C_AURORA_EMERALD if charging else (C_VOID_BORDER if caution else C_PULSAR_VIO)
        
        return make_tray_svg(f"{body}{cap}{fill_rect}{bolt}", border_c1=border_c1, border_c2=border_c2)

    # Generate all percentage levels (0 to 100 in steps of 10)
    for lvl in range(0, 110, 10):
        # Normal discharge
        lvl_svg = make_battery_svg(lvl, charging=False, caution=(lvl <= 15))
        write_svg("status", f"battery-{lvl:03d}.svg", lvl_svg)
        write_svg("status", f"battery-{lvl:03d}-symbolic.svg", lvl_svg)
        write_svg("status", f"battery-level-{lvl}-symbolic.svg", lvl_svg)

        # Charging states (Both naming conventions: battery-charging-XXX and battery-XXX-charging)
        chg_svg = make_battery_svg(lvl, charging=True)
        write_svg("status", f"battery-charging-{lvl:03d}.svg", chg_svg)
        write_svg("status", f"battery-{lvl:03d}-charging.svg", chg_svg)
        write_svg("status", f"battery-charging-{lvl:03d}-symbolic.svg", chg_svg)
        write_svg("status", f"battery-{lvl:03d}-charging-symbolic.svg", chg_svg)
        write_svg("status", f"battery-level-{lvl}-charging-symbolic.svg", chg_svg)

    # General Battery States & Symlinks
    write_svg("status", "battery-charging.svg", make_battery_svg(65, charging=True))
    write_svg("status", "battery-charging-symbolic.svg", make_battery_svg(65, charging=True))
    write_svg("status", "battery-caution.svg", make_battery_svg(10, caution=True))
    write_svg("status", "battery-caution-symbolic.svg", make_battery_svg(10, caution=True))
    write_svg("status", "battery-low.svg", make_battery_svg(15, caution=True))
    write_svg("status", "battery-low-symbolic.svg", make_battery_svg(15, caution=True))
    write_svg("status", "battery-empty.svg", make_battery_svg(0, caution=True))
    write_svg("status", "battery-empty-symbolic.svg", make_battery_svg(0, caution=True))
    write_svg("status", "battery-good.svg", make_battery_svg(70))
    write_svg("status", "battery-good-symbolic.svg", make_battery_svg(70))
    write_svg("status", "battery-full.svg", make_battery_svg(100))
    write_svg("status", "battery-full-symbolic.svg", make_battery_svg(100))
    write_svg("status", "battery-full-charging.svg", make_battery_svg(100, charging=True))
    write_svg("status", "battery-full-charging-symbolic.svg", make_battery_svg(100, charging=True))
    write_svg("status", "battery-good-charging.svg", make_battery_svg(70, charging=True))
    write_svg("status", "battery-good-charging-symbolic.svg", make_battery_svg(70, charging=True))
    write_svg("status", "battery-low-charging.svg", make_battery_svg(20, charging=True))
    write_svg("status", "battery-low-charging-symbolic.svg", make_battery_svg(20, charging=True))
    write_svg("status", "battery-caution-charging.svg", make_battery_svg(10, charging=True))
    write_svg("status", "battery-caution-charging-symbolic.svg", make_battery_svg(10, charging=True))
    write_svg("status", "battery-missing.svg", make_tray_svg(f'''<rect x="5.5" y="7.5" width="11.5" height="9" rx="2" fill="none" stroke="{C_STARDUST}" stroke-width="1.4" opacity="0.5"/><text x="11.5" y="14.5" font-family="sans-serif" font-size="8" font-weight="bold" fill="{C_STARDUST}" text-anchor="middle">?</text>'''))
    
    # AC Adapter Plug
    write_svg("status", "ac-adapter.svg", make_tray_svg(f'''<rect x="6" y="8" width="8" height="8" rx="2" fill="none" stroke="{C_AURORA_EMERALD}" stroke-width="1.6"/><line x1="8" y1="5" x2="8" y2="8" stroke="{C_AURORA_EMERALD}" stroke-width="1.6" stroke-linecap="round"/><line x1="12" y1="5" x2="12" y2="8" stroke="{C_AURORA_EMERALD}" stroke-width="1.6" stroke-linecap="round"/><path d="M 10 16 L 10 19 L 17 19" fill="none" stroke="{C_AURORA_EMERALD}" stroke-width="1.6" stroke-linecap="round"/>'''))
    make_symlink("status", "ac-adapter.svg", "ac-adapter-symbolic.svg")
    make_symlink("status", "ac-adapter.svg", "battery-ac-adapter.svg")
    make_symlink("status", "ac-adapter.svg", "battery-ac-adapter-symbolic.svg")
    make_symlink("status", "battery-100.svg", "battery.svg")
    make_symlink("status", "battery-100.svg", "battery-symbolic.svg")
    make_symlink("status", "battery-missing.svg", "battery-missing-symbolic.svg")

    # ----------------------------------------------------
    # 3. BLUETOOTH (Cosmic Squircle Rune)
    # ----------------------------------------------------
    write_svg("status", "bluetooth-active.svg", make_tray_svg(f'''<path d="M 8 7 L 16 15 L 12 19 L 12 5 L 16 9 L 8 17" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'''))
    write_svg("status", "bluetooth-connected.svg", make_tray_svg(f'''<path d="M 8 7 L 16 15 L 12 19 L 12 5 L 16 9 L 8 17" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><circle cx="17.5" cy="12" r="1.6" fill="{C_AURORA_EMERALD}"/>'''))
    write_svg("status", "bluetooth-disconnected.svg", make_tray_svg(f'''<path d="M 8 7 L 16 15 L 12 19 L 12 5 L 16 9 L 8 17" fill="none" stroke="{C_STARDUST}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" opacity="0.6"/>'''))
    write_svg("status", "bluetooth-disabled.svg", make_tray_svg(f'''<path d="M 8 7 L 16 15 L 12 19 L 12 5 L 16 9 L 8 17" fill="none" stroke="{C_STARDUST}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" opacity="0.35"/><line x1="5" y1="5" x2="19" y2="19" stroke="{C_DANGER_RED}" stroke-width="1.8" stroke-linecap="round"/>''', border_c1=C_DANGER_RED, border_c2=C_VOID_BORDER))

    make_symlink("status", "bluetooth-active.svg", "bluetooth.svg")
    make_symlink("status", "bluetooth-active.svg", "bluetooth-symbolic.svg")
    make_symlink("status", "bluetooth-active.svg", "preferences-system-bluetooth.svg")
    make_symlink("status", "bluetooth-active.svg", "network-bluetooth.svg")
    make_symlink("status", "bluetooth-active.svg", "network-bluetooth-activated.svg")
    make_symlink("status", "bluetooth-active.svg", "network-bluetooth-symbolic.svg")

    # ----------------------------------------------------
    # 4. AUDIO & MICROPHONE (Large, High-Visibility Vector Suite)
    # ----------------------------------------------------
    def make_audio_svg(pct, muted=False, off=False):
        spk = f'<path d="M 2 8.5 L 6.5 8.5 L 12 3.5 L 12 20.5 L 6.5 15.5 L 2 15.5 Z" fill="{C_STELLAR_CYAN if not (muted or off) else C_STARDUST}" stroke="{C_STELLAR_CYAN if not (muted or off) else C_STARDUST}" stroke-width="1.2" stroke-linejoin="round" opacity="{0.4 if off else 1.0}"/>'
        if muted:
            cross = f'<line x1="15" y1="7" x2="22" y2="17" stroke="{C_DANGER_RED}" stroke-width="2.2" stroke-linecap="round"/><line x1="22" y1="7" x2="15" y2="17" stroke="{C_DANGER_RED}" stroke-width="2.2" stroke-linecap="round"/>'
            return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  {spk}{cross}
</svg>'''
        elif off:
            return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  {spk}
</svg>'''
        else:
            w_low = f'<path d="M 15 9 C 16.5 10.5 16.5 13.5 15 15" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="2.2" stroke-linecap="round" opacity="{1.0 if pct >= 25 else 0.25}"/>'
            w_med = f'<path d="M 18 6.5 C 20.5 9.5 20.5 14.5 18 17.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="2.2" stroke-linecap="round" opacity="{1.0 if pct >= 50 else 0.25}"/>'
            w_high= f'<path d="M 21 4 C 24.5 8.5 24.5 15.5 21 20" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="2.2" stroke-linecap="round" opacity="{1.0 if pct >= 75 else 0.25}"/>'
            return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  {spk}{w_low}{w_med}{w_high}
</svg>'''

    write_svg("status", "audio-volume-high.svg", make_audio_svg(100))
    write_svg("status", "audio-volume-medium.svg", make_audio_svg(60))
    write_svg("status", "audio-volume-low.svg", make_audio_svg(25))
    write_svg("status", "audio-volume-muted.svg", make_audio_svg(0, muted=True))
    write_svg("status", "audio-volume-off.svg", make_audio_svg(0, off=True))

    make_symlink("status", "audio-volume-high.svg", "audio-volume-high-symbolic.svg")
    make_symlink("status", "audio-volume-medium.svg", "audio-volume-medium-symbolic.svg")
    make_symlink("status", "audio-volume-low.svg", "audio-volume-low-symbolic.svg")
    make_symlink("status", "audio-volume-muted.svg", "audio-volume-muted-symbolic.svg")
    make_symlink("status", "audio-volume-high.svg", "volume-level-high-symbolic.svg")
    make_symlink("status", "audio-volume-medium.svg", "volume-level-medium-symbolic.svg")
    make_symlink("status", "audio-volume-low.svg", "volume-level-low-symbolic.svg")
    make_symlink("status", "audio-volume-muted.svg", "volume-level-muted-symbolic.svg")

    # Microphone (Large Full-Canvas Glyph)
    write_svg("status", "audio-input-microphone.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <rect x="9" y="3" width="6" height="11" rx="3" fill="{C_STELLAR_CYAN}" fill-opacity="0.2" stroke="{C_STELLAR_CYAN}" stroke-width="1.8"/>
  <path d="M 5 9.5 C 5 14 19 14 19 9.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="12" y1="14" x2="12" y2="20" stroke="{C_STELLAR_CYAN}" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="8" y1="20" x2="16" y2="20" stroke="{C_STELLAR_CYAN}" stroke-width="1.8" stroke-linecap="round"/>
</svg>''')
    write_svg("status", "microphone-sensitivity-muted.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <rect x="9" y="3" width="6" height="11" rx="3" fill="none" stroke="{C_STARDUST}" stroke-width="1.8" opacity="0.5"/>
  <path d="M 5 9.5 C 5 14 19 14 19 9.5" fill="none" stroke="{C_STARDUST}" stroke-width="1.8" stroke-linecap="round" opacity="0.5"/>
  <line x1="12" y1="14" x2="12" y2="20" stroke="{C_STARDUST}" stroke-width="1.8" stroke-linecap="round" opacity="0.5"/>
  <line x1="8" y1="20" x2="16" y2="20" stroke="{C_STARDUST}" stroke-width="1.8" stroke-linecap="round" opacity="0.5"/>
  <line x1="4" y1="4" x2="20" y2="20" stroke="{C_DANGER_RED}" stroke-width="2.2" stroke-linecap="round"/>
</svg>''')

    make_symlink("status", "audio-input-microphone.svg", "audio-input-microphone-symbolic.svg")
    make_symlink("status", "audio-input-microphone.svg", "microphone-sensitivity-high.svg")
    make_symlink("status", "audio-input-microphone.svg", "microphone-sensitivity-medium.svg")
    make_symlink("status", "audio-input-microphone.svg", "microphone-sensitivity-low.svg")

    # Audio Devices (Headphones, Speakers, Headset, Card)
    headphones_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <path d="M 10 26 C 10 16 16 8 24 8 C 32 8 38 16 38 26" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="3.5" stroke-linecap="round"/>
  <rect x="6" y="24" width="8" height="16" rx="4" fill="{C_STELLAR_CYAN}" stroke="{C_STAR_WHITE}" stroke-width="1.5"/>
  <rect x="34" y="24" width="8" height="16" rx="4" fill="{C_STELLAR_CYAN}" stroke="{C_STAR_WHITE}" stroke-width="1.5"/>
  <circle cx="10" cy="32" r="2" fill="{C_STAR_WHITE}"/>
  <circle cx="38" cy="32" r="2" fill="{C_STAR_WHITE}"/>
</svg>'''
    write_svg("devices", "audio-headphones.svg", headphones_svg)
    write_svg("status", "audio-headphones.svg", headphones_svg)
    make_symlink("devices", "audio-headphones.svg", "audio-headphones-symbolic.svg")
    make_symlink("status", "audio-headphones.svg", "audio-headphones-symbolic.svg")

    speakers_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <rect x="10" y="6" width="28" height="36" rx="5" fill="{C_VOID_CARD}" stroke="{C_STELLAR_CYAN}" stroke-width="2.5"/>
  <circle cx="24" cy="16" r="4.5" fill="{C_STELLAR_CYAN}"/>
  <circle cx="24" cy="30" r="8" fill="none" stroke="{C_PULSAR_VIO}" stroke-width="2.5"/>
  <circle cx="24" cy="30" r="3.5" fill="{C_STELLAR_CYAN}"/>
</svg>'''
    write_svg("devices", "audio-speakers.svg", speakers_svg)
    write_svg("status", "audio-speakers.svg", speakers_svg)
    make_symlink("devices", "audio-speakers.svg", "audio-speakers-symbolic.svg")
    make_symlink("status", "audio-speakers.svg", "audio-speakers-symbolic.svg")

    headset_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <path d="M 10 26 C 10 16 16 8 24 8 C 32 8 38 16 38 26" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="3.5" stroke-linecap="round"/>
  <rect x="6" y="24" width="8" height="16" rx="4" fill="{C_STELLAR_CYAN}" stroke="{C_STAR_WHITE}" stroke-width="1.5"/>
  <rect x="34" y="24" width="8" height="16" rx="4" fill="{C_STELLAR_CYAN}" stroke="{C_STAR_WHITE}" stroke-width="1.5"/>
  <path d="M 38 34 C 38 40 32 44 26 44 L 20 44" fill="none" stroke="{C_SUPERNOVA_GOLD}" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="18" cy="44" r="3" fill="{C_SUPERNOVA_GOLD}"/>
</svg>'''
    write_svg("devices", "audio-headset.svg", headset_svg)
    write_svg("status", "audio-headset.svg", headset_svg)
    make_symlink("devices", "audio-headset.svg", "audio-headset-symbolic.svg")
    make_symlink("status", "audio-headset.svg", "audio-headset-symbolic.svg")

    # ----------------------------------------------------
    # 5. PRINTERS & PRINTING STATES
    # ----------------------------------------------------
    prt = f'''<rect x="5.5" y="9.5" width="13" height="8" rx="2" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><path d="M 8 9.5 L 8 5 C 8 4.5 8.5 4 9 4 L 15 4 C 15.5 4 16 4.5 16 5 L 16 9.5" fill="none" stroke="{C_STAR_WHITE}" stroke-width="1.4"/><rect x="8" y="13.5" width="8" height="5.5" rx="1" fill="{C_VOID_CARD}" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/><line x1="9.5" y1="16" x2="14.5" y2="16" stroke="{C_STAR_WHITE}" stroke-width="1.0" stroke-linecap="round"/><circle cx="16" cy="11.5" r="0.9" fill="{C_AURORA_EMERALD}"/>'''
    write_svg("status", "printer.svg", make_tray_svg(prt))
    write_svg("status", "printer-printing.svg", make_tray_svg(f'''{prt}<line x1="8" y1="13" x2="16" y2="13" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.8" stroke-linecap="round"/>'''))
    write_svg("status", "printer-error.svg", make_tray_svg(f'''{prt}<circle cx="17.5" cy="16.5" r="3.2" fill="{C_DANGER_RED}"/><line x1="16" y1="15" x2="19" y2="18" stroke="{C_STAR_WHITE}" stroke-width="1.0"/><line x1="19" y1="15" x2="16" y2="18" stroke="{C_STAR_WHITE}" stroke-width="1.0"/>''', border_c1=C_DANGER_RED, border_c2=C_VOID_BORDER))
    write_svg("status", "printer-warning.svg", make_tray_svg(f'''{prt}<circle cx="17.5" cy="16.5" r="3.2" fill="{C_SUPERNOVA_GOLD}"/><line x1="17.5" y1="15" x2="17.5" y2="17" stroke="{C_VOID_DARK}" stroke-width="1.2" stroke-linecap="round"/><circle cx="17.5" cy="18.5" r="0.6" fill="{C_VOID_DARK}"/>'''))
    write_svg("status", "printer-pause.svg", make_tray_svg(f'''{prt}<circle cx="17.5" cy="16.5" r="3.2" fill="{C_PULSAR_VIO}"/><line x1="16.5" y1="15" x2="16.5" y2="18" stroke="{C_STAR_WHITE}" stroke-width="1.0"/><line x1="18.5" y1="15" x2="18.5" y2="18" stroke="{C_STAR_WHITE}" stroke-width="1.0"/>'''))

    make_symlink("status", "printer.svg", "printer-symbolic.svg")
    make_symlink("status", "printer.svg", "printer-network.svg")
    make_symlink("status", "printer.svg", "printer-wireless.svg")
    make_symlink("status", "printer.svg", "cups.svg")
    make_symlink("status", "printer.svg", "document-print.svg")
    make_symlink("status", "printer.svg", "document-print-preview.svg")

    # ----------------------------------------------------
    # 6. LANGUAGE & KEYBOARD
    # ----------------------------------------------------
    write_svg("status", "input-keyboard.svg", make_tray_svg(f'''<rect x="4.5" y="6.5" width="15" height="11" rx="2" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><line x1="7" y1="9.5" x2="8.5" y2="9.5" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/><line x1="10" y1="9.5" x2="11.5" y2="9.5" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/><line x1="13" y1="9.5" x2="14.5" y2="9.5" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/><line x1="16" y1="9.5" x2="17" y2="9.5" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/><line x1="7.5" y1="12" x2="9" y2="12" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/><line x1="10.5" y1="12" x2="13.5" y2="12" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/><line x1="15" y1="12" x2="16.5" y2="12" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/><line x1="8" y1="14.5" x2="16" y2="14.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.5" stroke-linecap="round"/>'''))
    write_svg("status", "language.svg", make_tray_svg(f'''<circle cx="12" cy="12" r="7" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><ellipse cx="12" cy="12" rx="3.5" ry="7" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/><line x1="5" y1="12" x2="19" y2="12" stroke="{C_STELLAR_CYAN}" stroke-width="1.2"/><path d="M 6.5 8.5 C 8.5 9.5 15.5 9.5 17.5 8.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/><path d="M 6.5 15.5 C 8.5 14.5 15.5 14.5 17.5 15.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.0"/>'''))
    write_svg("status", "keyboard-layout.svg", make_tray_svg(f'''<text x="12" y="15" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="{C_STELLAR_CYAN}" text-anchor="middle">EN</text>'''))
    write_svg("status", "fcitx.svg", make_tray_svg(f'''<circle cx="12" cy="12" r="7" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><path d="M 8 12 L 11 15 L 16 9" fill="none" stroke="{C_AURORA_EMERALD}" stroke-width="1.8" stroke-linecap="round"/>'''))

    make_symlink("status", "input-keyboard.svg", "input-keyboard-symbolic.svg")
    make_symlink("status", "input-keyboard.svg", "input-keyboard-virtual.svg")
    make_symlink("status", "input-keyboard.svg", "input-keyboard-virtual-on.svg")
    make_symlink("status", "input-keyboard.svg", "input-keyboard-virtual-off.svg")
    make_symlink("status", "input-keyboard.svg", "preferences-desktop-keyboard.svg")
    make_symlink("status", "language.svg", "language-symbolic.svg")
    make_symlink("status", "language.svg", "locale.svg")
    make_symlink("status", "language.svg", "locale-symbolic.svg")
    make_symlink("status", "language.svg", "preferences-desktop-locale.svg")
    make_symlink("status", "keyboard-layout.svg", "keyboard-layout-symbolic.svg")
    make_symlink("status", "keyboard-layout.svg", "input-method.svg")
    make_symlink("status", "keyboard-layout.svg", "ibus.svg")

    # ----------------------------------------------------
    # 7. MEDIA PLAYBACK CONTROLS
    # ----------------------------------------------------
    write_svg("status", "media-playback-start.svg", make_tray_svg(f'''<polygon points="9,6.5 18,12 9,17.5" fill="{C_STELLAR_CYAN}" stroke="{C_STELLAR_CYAN}" stroke-width="1.2" stroke-linejoin="round"/>'''))
    write_svg("status", "media-playback-pause.svg", make_tray_svg(f'''<line x1="9" y1="7" x2="9" y2="17" stroke="{C_STELLAR_CYAN}" stroke-width="2.4" stroke-linecap="round"/><line x1="15" y1="7" x2="15" y2="17" stroke="{C_STELLAR_CYAN}" stroke-width="2.4" stroke-linecap="round"/>'''))
    write_svg("status", "media-playback-stop.svg", make_tray_svg(f'''<rect x="7" y="7" width="10" height="10" rx="1.5" fill="{C_STELLAR_CYAN}"/>'''))
    write_svg("status", "media-skip-forward.svg", make_tray_svg(f'''<polygon points="6.5,7 13.5,12 6.5,17" fill="{C_STELLAR_CYAN}" stroke="{C_STELLAR_CYAN}" stroke-width="1.0" stroke-linejoin="round"/><line x1="16.5" y1="7" x2="16.5" y2="17" stroke="{C_STELLAR_CYAN}" stroke-width="2.0" stroke-linecap="round"/>'''))
    write_svg("status", "media-skip-backward.svg", make_tray_svg(f'''<polygon points="17.5,7 10.5,12 17.5,17" fill="{C_STELLAR_CYAN}" stroke="{C_STELLAR_CYAN}" stroke-width="1.0" stroke-linejoin="round"/><line x1="7.5" y1="7" x2="7.5" y2="17" stroke="{C_STELLAR_CYAN}" stroke-width="2.0" stroke-linecap="round"/>'''))
    write_svg("status", "media-seek-forward.svg", make_tray_svg(f'''<polygon points="5,7 11.5,12 5,17" fill="{C_STELLAR_CYAN}" stroke="{C_STELLAR_CYAN}" stroke-width="1.0" stroke-linejoin="round"/><polygon points="11.5,7 18,12 11.5,17" fill="{C_STELLAR_CYAN}" stroke="{C_STELLAR_CYAN}" stroke-width="1.0" stroke-linejoin="round"/>'''))
    write_svg("status", "media-seek-backward.svg", make_tray_svg(f'''<polygon points="12.5,7 6,12 12.5,17" fill="{C_STELLAR_CYAN}" stroke="{C_STELLAR_CYAN}" stroke-width="1.0" stroke-linejoin="round"/><polygon points="19,7 12.5,12 19,17" fill="{C_STELLAR_CYAN}" stroke="{C_STELLAR_CYAN}" stroke-width="1.0" stroke-linejoin="round"/>'''))
    write_svg("status", "media-record.svg", make_tray_svg(f'''<circle cx="12" cy="12" r="5.5" fill="{C_DANGER_RED}"/>''', border_c1=C_DANGER_RED, border_c2=C_VOID_BORDER))
    write_svg("status", "media-playlist-repeat.svg", make_tray_svg(f'''<path d="M 15.5 5 L 18 7 L 15.5 9 M 18 7 L 9 7 C 7 7 6 8 6 10 M 8.5 19 L 6 17 L 8.5 15 M 6 17 L 15 17 C 17 17 18 16 18 14" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'''))
    write_svg("status", "media-playlist-shuffle.svg", make_tray_svg(f'''<path d="M 15 5.5 L 18 8 L 15 10.5 M 18 8 L 14 8 C 12.5 8 11 11 9 13 C 7.5 15 6 16 4 16 M 15 13.5 L 18 16 L 15 18.5 M 18 16 L 14 16 C 12.5 16 11 13 9 11 C 7.5 9 6 8 4 8" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'''))

    make_symlink("status", "media-playback-start.svg", "media-playback-start-symbolic.svg")
    make_symlink("status", "media-playback-pause.svg", "media-playback-pause-symbolic.svg")
    make_symlink("status", "media-playback-stop.svg", "media-playback-stop-symbolic.svg")
    make_symlink("status", "media-skip-forward.svg", "media-skip-forward-symbolic.svg")
    make_symlink("status", "media-skip-backward.svg", "media-skip-backward-symbolic.svg")

    # ----------------------------------------------------
    # 8. PLASMA VAULT & SECURITY
    # ----------------------------------------------------
    write_svg("status", "plasma-vault.svg", make_tray_svg(f'''<circle cx="12" cy="12" r="7" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><circle cx="12" cy="12" r="3" fill="none" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.4"/><line x1="12" y1="5" x2="12" y2="8" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/><line x1="12" y1="16" x2="12" y2="19" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/><line x1="5" y1="12" x2="8" y2="12" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/><line x1="16" y1="12" x2="19" y2="12" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/>'''))
    write_svg("status", "folder-locked.svg", make_tray_svg(f'''<rect x="6.5" y="10.5" width="11" height="8.5" rx="2" fill="none" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.6"/><path d="M 9 10.5 L 9 7.5 C 9 5.8 10.2 4.5 12 4.5 C 13.8 4.5 15 5.8 15 7.5 L 15 10.5" fill="none" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="14" r="1.2" fill="{C_SUPERNOVA_GOLD}"/>'''))
    write_svg("status", "folder-unlocked.svg", make_tray_svg(f'''<rect x="6.5" y="10.5" width="11" height="8.5" rx="2" fill="none" stroke="{C_AURORA_EMERALD}" stroke-width="1.6"/><path d="M 9 10.5 L 9 7.5 C 9 5.8 10.2 4.5 12 4.5 C 13.8 4.5 15 5.8 15 7.5" fill="none" stroke="{C_AURORA_EMERALD}" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="14" r="1.2" fill="{C_AURORA_EMERALD}"/>''', border_c1=C_AURORA_EMERALD, border_c2=C_VOID_BORDER))
    write_svg("status", "dialog-password.svg", make_tray_svg(f'''<circle cx="9" cy="12" r="3.8" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><line x1="12.8" y1="12" x2="18.5" y2="12" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/><line x1="15.5" y1="12" x2="15.5" y2="14.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/><line x1="18" y1="12" x2="18" y2="14.5" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/>'''))

    make_symlink("status", "plasma-vault.svg", "plasma-vault-symbolic.svg")
    make_symlink("status", "folder-locked.svg", "folder-encrypted.svg")
    make_symlink("status", "folder-locked.svg", "folder-vault.svg")
    make_symlink("status", "folder-locked.svg", "folder-crypt.svg")
    make_symlink("status", "folder-locked.svg", "folder-security.svg")
    make_symlink("status", "folder-locked.svg", "folder-private.svg")
    make_symlink("status", "folder-locked.svg", "folder-secret.svg")
    make_symlink("status", "folder-locked.svg", "folder-password.svg")
    make_symlink("status", "folder-unlocked.svg", "folder-decrypted.svg")
    make_symlink("status", "dialog-password.svg", "security-high.svg")

    # ----------------------------------------------------
    # 9. NOTIFICATIONS, KLIPPER, NIGHT LIGHT, DEVICES
    # ----------------------------------------------------
    write_svg("status", "preferences-desktop-notification-bell.svg", make_tray_svg(f'''<path d="M 12 4.5 C 9.5 4.5 7.5 6.5 7.5 9 L 7.5 13 L 5.5 15 L 18.5 15 L 16.5 13 L 16.5 9 C 16.5 6.5 14.5 4.5 12 4.5 Z" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linejoin="round"/><path d="M 10.5 16.5 C 10.5 17.5 11.2 18 12 18 C 12.8 18 13.5 17.5 13.5 16.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><circle cx="17.5" cy="6.5" r="2" fill="{C_SUPERNOVA_GOLD}"/>'''))
    write_svg("status", "notification-inactive.svg", make_tray_svg(f'''<path d="M 12 4.5 C 9.5 4.5 7.5 6.5 7.5 9 L 7.5 13 L 5.5 15 L 18.5 15 L 16.5 13 L 16.5 9 C 16.5 6.5 14.5 4.5 12 4.5 Z" fill="none" stroke="{C_STARDUST}" stroke-width="1.6" stroke-linejoin="round"/><path d="M 10.5 16.5 C 10.5 17.5 11.2 18 12 18 C 12.8 18 13.5 17.5 13.5 16.5" fill="none" stroke="{C_STARDUST}" stroke-width="1.6"/>'''))
    make_symlink("status", "preferences-desktop-notification-bell.svg", "preferences-desktop-notification.svg")
    make_symlink("status", "preferences-desktop-notification-bell.svg", "notification-symbolic.svg")
    make_symlink("status", "preferences-desktop-notification-bell.svg", "notifications.svg")
    make_symlink("status", "preferences-desktop-notification-bell.svg", "notifications-disabled.svg")

    # Night Light (Crescent Moon)
    write_svg("status", "night-light.svg", make_tray_svg(f'''<path d="M 12 4.5 C 8 4.5 4.8 7.8 4.8 12 C 4.8 16.2 8 19.5 12 19.5 C 15.2 19.5 18 17.2 19 14.2 C 15.2 14.5 12 11.2 12.2 7.2 C 12.2 6.2 12 5.2 12 4.5 Z" fill="{C_SUPERNOVA_GOLD}" stroke="{C_STAR_WHITE}" stroke-width="0.8"/><circle cx="17.5" cy="7.5" r="0.8" fill="{C_STAR_WHITE}"/>'''))
    write_svg("status", "night-light-disabled.svg", make_tray_svg(f'''<path d="M 12 4.5 C 8 4.5 4.8 7.8 4.8 12 C 4.8 16.2 8 19.5 12 19.5 C 15.2 19.5 18 17.2 19 14.2 C 15.2 14.5 12 11.2 12.2 7.2 C 12.2 6.2 12 5.2 12 4.5 Z" fill="none" stroke="{C_STARDUST}" stroke-width="1.6" opacity="0.4"/><line x1="5" y1="5" x2="19" y2="19" stroke="{C_DANGER_RED}" stroke-width="1.8" stroke-linecap="round"/>''', border_c1=C_DANGER_RED, border_c2=C_VOID_BORDER))
    make_symlink("status", "night-light.svg", "night-light-symbolic.svg")
    make_symlink("status", "night-light.svg", "redshift-status-on.svg")
    make_symlink("status", "night-light-disabled.svg", "redshift-status-off.svg")

    # Klipper / Clipboard
    write_svg("status", "klipper.svg", make_tray_svg(f'''<rect x="6" y="6.5" width="12" height="12" rx="2" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><path d="M 9.5 6.5 L 9.5 5 C 9.5 4.2 10.2 3.5 11 3.5 L 13 3.5 C 13.8 3.5 14.5 4.2 14.5 5 L 14.5 6.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round"/><line x1="9" y1="10.5" x2="15" y2="10.5" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/><line x1="9" y1="14" x2="13.5" y2="14" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/>'''))
    make_symlink("status", "klipper.svg", "klipper-symbolic.svg")
    make_symlink("status", "klipper.svg", "clipboard.svg")
    make_symlink("status", "klipper.svg", "edit-paste-symbolic.svg")

    # KDE Connect / Phone
    write_svg("status", "kdeconnect.svg", make_tray_svg(f'''<rect x="7" y="3.5" width="10" height="17" rx="2.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6"/><circle cx="12" cy="17" r="0.9" fill="{C_STELLAR_CYAN}"/><line x1="10" y1="6" x2="14" y2="6" stroke="{C_STAR_WHITE}" stroke-width="1.2" stroke-linecap="round"/>'''))
    make_symlink("status", "kdeconnect.svg", "smartphone.svg")
    make_symlink("status", "kdeconnect.svg", "phone.svg")

    # Device Notifier / USB
    write_svg("status", "device-notifier.svg", make_tray_svg(f'''<path d="M 12 4.5 L 12 16.5 M 12 4.5 L 9.5 7 M 12 4.5 L 14.5 7 M 12 11.5 L 7.5 9.5 L 7.5 8 M 12 13 L 16.5 11 L 16.5 9.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="17.8" r="1.2" fill="{C_STELLAR_CYAN}"/><circle cx="7.5" cy="7" r="1.2" fill="{C_SUPERNOVA_GOLD}"/><rect x="15" y="6" width="2.6" height="2.6" fill="{C_AURORA_EMERALD}"/>'''))
    make_symlink("status", "device-notifier.svg", "drive-removable-media-symbolic.svg")

    # Software Updates
    write_svg("status", "software-update-available.svg", make_tray_svg(f'''<path d="M 12 5 L 12 13.5 M 8 9.5 L 12 13.5 L 16 9.5" fill="none" stroke="{C_STELLAR_CYAN}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 5.5 15 L 5.5 17.5 C 5.5 18 6 18.5 6.5 18.5 L 17.5 18.5 C 18 18.5 18.5 18 18.5 17.5 L 18.5 15" fill="none" stroke="{C_STAR_WHITE}" stroke-width="1.6" stroke-linecap="round"/>'''))
    write_svg("status", "software-update-urgent.svg", make_tray_svg(f'''<path d="M 12 5 L 12 13.5 M 8 9.5 L 12 13.5 L 16 9.5" fill="none" stroke="{C_SUPERNOVA_GOLD}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 5.5 15 L 5.5 17.5 C 5.5 18 6 18.5 6.5 18.5 L 17.5 18.5 C 18 18.5 18.5 18 18.5 17.5 L 18.5 15" fill="none" stroke="{C_STAR_WHITE}" stroke-width="1.6" stroke-linecap="round"/><circle cx="17.5" cy="6.5" r="2.2" fill="{C_DANGER_RED}"/>''', border_c1=C_DANGER_RED, border_c2=C_SUPERNOVA_GOLD))
    make_symlink("status", "software-update-available.svg", "update-notifier.svg")
    make_symlink("status", "software-update-available.svg", "package-supported.svg")

    print("==========================================")
    print("Galaxy Cosmic Squircle System Tray Icons Generated!")
    print("==========================================")

if __name__ == "__main__":
    gen_all_tray_icons()

