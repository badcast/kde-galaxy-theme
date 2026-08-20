#!/usr/bin/env python3
"""
Galaxy Theme KDE - Master Icon Suite Generator
Author:  badcast <lmecomposer@gmail.com>
Project: Galaxy Theme KDE

Generates 500+ vector SVG icons and FreeDesktop/KDE symlinks:
- PLACES (50+ Folders, Encrypted Vaults, Disks, Home, Trash, Cloud, Git, Special)
- OFFICE & DOCUMENTS (45+ MS Office, LibreOffice, PDF, E-books, Text formats)
- ARCHIVES & PACKAGES (35+ ZIP, RAR, 7Z, TAR, GZ, XZ, ZST, ISO, DEB, RPM, APK)
- APPS (Native KDE apps [Elisa, Amarok, Haruna, Kate, Dolphin], Generic system apps, Terminals, Editors, System utilities, Printers, Settings, Vaults)
- ACTIONS (120+ Playback controls, Printers, Navigation, Window ops, File actions, Edit ops)
- STATUS & SYSTEM TRAY (100+ Battery levels, Charging, Bluetooth, Wi-Fi, Audio/Mic, Security, Vaults, Printers, Language)
- DEVICES (40+ Hardware, Printers, Drives, Audio cards, Headsets, Displays, Peripherals)
- MIMETYPES (60+ Audio, Video, Code, Config, Web, Images, Fonts)
- CATEGORIES (15+ Menu categories)
"""

import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_ROOT = os.path.join(BASE_DIR, "icons", "Galaxy-Icons")
SCALABLE_DIR = os.path.join(ICONS_ROOT, "scalable")

# Cosmic Color Palette
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

# Office & Mimetype Palette
C_OFFICE_WORD  = "#2B579A"
C_OFFICE_EXCEL = "#217346"
C_OFFICE_PPT   = "#D24726"
C_OFFICE_BASE  = "#A4373A"
C_OFFICE_DRAW  = "#E67E22"
C_OFFICE_MATH  = "#8E44AD"
C_ARCHIVE_GOLD = "#F59E0B"
C_PDF_RED      = "#EA4335"

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

def make_folder_svg(emblem_svg="", c1=C_PULSAR_VIO, c2=C_STELLAR_CYAN):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="foldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
    <linearGradient id="backGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{C_VOID_CARD}"/>
      <stop offset="100%" stop-color="{C_VOID_MID}"/>
    </linearGradient>
  </defs>
  <path d="M 6 15 C 6 12.8 7.8 11 10 11 L 24 11 L 28 15 L 54 15 C 56.2 15 58 16.8 58 19 L 58 48 C 58 50.2 56.2 52 54 52 L 10 52 C 7.8 52 6 50.2 6 48 Z" fill="url(#backGrad)" stroke="{c1}" stroke-opacity="0.5" stroke-width="1.2"/>
  <rect x="12" y="18" width="40" height="16" rx="2" fill="{C_STAR_WHITE}" fill-opacity="0.25"/>
  <path d="M 6 23 C 6 20.8 7.8 19 10 19 L 54 19 C 56.2 19 58 20.8 58 23 L 58 48 C 58 51.3 55.3 54 52 54 L 12 54 C 8.7 54 6 51.3 6 48 Z" fill="url(#foldGrad)" fill-opacity="0.92" stroke="{C_STAR_WHITE}" stroke-opacity="0.3" stroke-width="1"/>
  <line x1="12" y1="22" x2="52" y2="22" stroke="{C_STAR_WHITE}" stroke-opacity="0.75" stroke-width="1"/>
  {emblem_svg}
</svg>'''

def make_app_svg(c1, c2, glyph_svg):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
    <linearGradient id="rim" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{C_STELLAR_CYAN}" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="{C_PULSAR_VIO}" stop-opacity="0.7"/>
    </linearGradient>
  </defs>
  <rect x="6" y="6" width="52" height="52" rx="14" fill="url(#bg)" stroke="url(#rim)" stroke-width="1.2"/>
  <rect x="7.5" y="7.5" width="49" height="49" rx="12.5" fill="none" stroke="{C_STAR_WHITE}" stroke-opacity="0.18" stroke-width="1"/>
  {glyph_svg}
</svg>'''

def make_action_svg(glyph_svg, color=C_STAR_WHITE):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <g fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    {glyph_svg}
  </g>
</svg>'''

def make_doc_svg(badge_label, badge_color, emblem_svg=""):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="docBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{C_VOID_CARD}"/>
      <stop offset="100%" stop-color="{C_VOID_MID}"/>
    </linearGradient>
    <linearGradient id="cornerFold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{badge_color}"/>
      <stop offset="100%" stop-color="{C_PULSAR_VIO}"/>
    </linearGradient>
  </defs>
  <path d="M 14 8 L 38 8 L 50 20 L 50 56 C 50 58.2 48.2 60 46 60 L 14 60 C 11.8 60 10 58.2 10 56 L 10 12 C 10 9.8 11.8 8 14 8 Z" fill="url(#docBg)" stroke="{badge_color}" stroke-opacity="0.6" stroke-width="1.5"/>
  <path d="M 38 8 L 38 20 L 50 20 Z" fill="url(#cornerFold)"/>
  <rect x="14" y="40" width="36" height="12" rx="3" fill="{badge_color}" fill-opacity="0.85"/>
  <text x="32" y="49" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="{C_STAR_WHITE}" text-anchor="middle">{badge_label}</text>
  {emblem_svg}
</svg>'''

def gen_all():
    print("==========================================")
    print("Generating Comprehensive Galaxy Cosmic Icon Suite")
    print("==========================================")

    # ----------------------------------------------------
    # 1. PLACES (FOLDERS, ENCRYPTED VAULTS, DRIVES, HOME)
    # ----------------------------------------------------
    # Shield & Lock emblem for Encrypted Folders
    lock_closed_emblem = ('<rect x="25" y="32" width="14" height="11" rx="2.5" fill="' + C_VOID_DARK + '" stroke="' + C_SUPERNOVA_GOLD + '" stroke-width="1.5"/><path d="M 28 32 L 28 28 C 28 25.8 36 25.8 36 28 L 36 32" fill="none" stroke="' + C_SUPERNOVA_GOLD + '" stroke-width="1.5"/><circle cx="32" cy="36.5" r="1.5" fill="' + C_SUPERNOVA_GOLD + '"/>')
    lock_open_emblem = ('<rect x="25" y="33" width="14" height="11" rx="2.5" fill="' + C_VOID_DARK + '" stroke="' + C_AURORA_EMERALD + '" stroke-width="1.5"/><path d="M 28 33 L 28 28 C 28 25.8 36 25.8 36 28" fill="none" stroke="' + C_AURORA_EMERALD + '" stroke-width="1.5"/><circle cx="32" cy="37.5" r="1.5" fill="' + C_AURORA_EMERALD + '"/>')
    vault_emblem = ('<circle cx="32" cy="37" r="8" fill="' + C_VOID_DARK + '" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.8"/><circle cx="32" cy="37" r="3.5" fill="none" stroke="' + C_SUPERNOVA_GOLD + '" stroke-width="1.5"/><line x1="32" y1="29" x2="32" y2="32" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.5"/><line x1="32" y1="42" x2="32" y2="45" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.5"/><line x1="24" y1="37" x2="27" y2="37" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.5"/><line x1="37" y1="37" x2="40" y2="37" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.5"/>')

    folder_definitions = {
        "folder.svg": ("", C_PULSAR_VIO, C_STELLAR_CYAN),
        "folder-open.svg": ('<path d="M 6 27 L 12 54 L 56 54 L 60 27 Z" fill="' + C_STELLAR_CYAN + '" fill-opacity="0.4"/>', C_PULSAR_VIO, C_STELLAR_CYAN),
        "folder-documents.svg": ('<path d="M 28 32 L 36 32 M 28 36 L 36 36 M 28 40 L 33 40" stroke="' + C_STAR_WHITE + '" stroke-width="1.5" stroke-linecap="round"/><rect x="25" y="28" width="14" height="18" rx="1.5" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>', C_PULSAR_VIO, C_STELLAR_CYAN),
        "folder-download.svg": ('<path d="M 32 30 L 32 44 M 26 38 L 32 44 L 38 38" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>', C_PULSAR_VIO, C_STELLAR_CYAN),
        "folder-music.svg": ('<path d="M 28 42 A 3 3 0 1 1 25 39 L 25 30 L 39 27 L 39 39 A 3 3 0 1 1 36 36 L 36 30" fill="' + C_STAR_WHITE + '" stroke="' + C_STAR_WHITE + '" stroke-width="1"/>', C_PULSAR_VIO, C_NEBULA_MAG),
        "folder-pictures.svg": ('<rect x="24" y="30" width="16" height="14" rx="2" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><circle cx="28" cy="34" r="1.5" fill="' + C_STAR_WHITE + '"/><path d="M 25 42 L 30 37 L 34 40 L 37 36 L 39 42" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>', C_SUPERNOVA_GOLD, C_PULSAR_VIO),
        "folder-videos.svg": ('<rect x="24" y="30" width="16" height="14" rx="2" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><polygon points="30,34 36,37 30,40" fill="' + C_STAR_WHITE + '"/>', C_DANGER_RED, C_PULSAR_VIO),
        "folder-code.svg": ('<path d="M 29 33 L 24 37 L 29 41 M 35 33 L 40 37 L 35 41" stroke="' + C_STAR_WHITE + '" stroke-width="1.8" stroke-linecap="round"/>', C_STELLAR_CYAN, C_AURORA_EMERALD),
        "folder-git.svg": ('<circle cx="26" cy="34" r="2.5" fill="' + C_STAR_WHITE + '"/><circle cx="38" cy="32" r="2.5" fill="' + C_STAR_WHITE + '"/><circle cx="38" cy="42" r="2.5" fill="' + C_STAR_WHITE + '"/><path d="M 26 34 L 38 32 M 38 32 L 38 42" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/>', C_DANGER_RED, C_SUPERNOVA_GOLD),
        "folder-games.svg": ('<rect x="24" y="32" width="16" height="10" rx="4" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><line x1="28" y1="35" x2="28" y2="39" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/><line x1="26" y1="37" x2="30" y2="37" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/><circle cx="36" cy="37" r="1" fill="' + C_STAR_WHITE + '"/>', C_NEBULA_MAG, C_PULSAR_VIO),
        "folder-cloud.svg": ('<path d="M 26 40 C 24 40 23 38 24 36 C 24 34 26 33 28 33 C 29 30 33 29 36 31 C 38 31 40 33 40 35 C 41 35 42 37 41 39 C 40 40 39 40 38 40 Z" fill="' + C_STAR_WHITE + '"/>', C_STELLAR_CYAN, C_VOID_CARD),
        "folder-remote.svg": ('<circle cx="32" cy="37" r="7" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><ellipse cx="32" cy="37" rx="3.5" ry="7" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/><line x1="25" y1="37" x2="39" y2="37" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>', C_STELLAR_CYAN, C_PULSAR_VIO),
        "folder-starred.svg": ('<polygon points="32,29 34,34 39,34 35,37 36,42 32,39 28,42 29,37 25,34 30,34" fill="' + C_SUPERNOVA_GOLD + '" stroke="' + C_STAR_WHITE + '" stroke-width="0.8"/>', C_PULSAR_VIO, C_SUPERNOVA_GOLD),
        "folder-temp.svg": ('<path d="M 32 30 L 32 38 M 30 40 A 2.5 2.5 0 1 1 34 40" stroke="' + C_SUPERNOVA_GOLD + '" stroke-width="1.5"/>', C_SUPERNOVA_GOLD, C_VOID_CARD),
        "folder-public.svg": ('<circle cx="32" cy="33" r="3" fill="' + C_STAR_WHITE + '"/><path d="M 26 42 C 26 38 38 38 38 42" fill="' + C_STAR_WHITE + '"/>', C_AURORA_EMERALD, C_STELLAR_CYAN),
        "folder-root.svg": ('<rect x="25" y="32" width="14" height="10" rx="2" fill="none" stroke="' + C_DANGER_RED + '" stroke-width="1.5"/><path d="M 28 32 L 28 29 C 28 27 36 27 36 29 L 36 32" stroke="' + C_DANGER_RED + '" stroke-width="1.5"/>', C_DANGER_RED, C_VOID_DARK),
        
        # Encrypted Folders & Vaults
        "folder-locked.svg": (lock_closed_emblem, C_VOID_CARD, C_PULSAR_VIO),
        "folder-unlocked.svg": (lock_open_emblem, C_VOID_CARD, C_AURORA_EMERALD),
        "folder-vault.svg": (vault_emblem, C_VOID_DARK, C_STELLAR_CYAN),
        
        "folder-system.svg": ('<circle cx="32" cy="37" r="5" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-dasharray="3 2"/><circle cx="32" cy="37" r="2" fill="' + C_STAR_WHITE + '"/>', C_PULSAR_VIO, C_VOID_DARK),
        "folder-network.svg": ('<circle cx="32" cy="33" r="3" fill="' + C_STAR_WHITE + '"/><circle cx="26" cy="42" r="2.5" fill="' + C_STAR_WHITE + '"/><circle cx="38" cy="42" r="2.5" fill="' + C_STAR_WHITE + '"/><line x1="32" y1="36" x2="26" y2="40" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/><line x1="32" y1="36" x2="38" y2="40" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>', C_STELLAR_CYAN, C_VOID_MID),
        "folder-templates.svg": ('<rect x="26" y="30" width="12" height="14" rx="1.5" stroke="' + C_STAR_WHITE + '" stroke-width="1.5" stroke-dasharray="2 2" fill="none"/>', C_STARDUST, C_VOID_CARD),
        "folder-recent.svg": ('<circle cx="32" cy="37" r="6" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><polyline points="32,34 32,37 35,37" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>', C_STELLAR_CYAN, C_PULSAR_VIO),
        "folder-database.svg": ('<ellipse cx="32" cy="32" rx="7" ry="2.5" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><path d="M 25 32 L 25 42 C 25 44 39 44 39 42 L 39 32" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><path d="M 25 37 C 25 39 39 39 39 37" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>', C_PULSAR_VIO, C_STELLAR_CYAN),
        "folder-mail.svg": ('<rect x="24" y="31" width="16" height="11" rx="1.5" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><path d="M 24 31 L 32 37 L 40 31" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>', C_STELLAR_CYAN, C_PULSAR_VIO),
    }

    for name, (emblem, c1, c2) in folder_definitions.items():
        write_svg("places", name, make_folder_svg(emblem, c1, c2))

    # Places Symlinks
    places_symlinks = {
        "inode-directory.svg": "folder.svg",
        "folder-symbolic.svg": "folder.svg",
        "folder-downloads.svg": "folder-download.svg",
        "folder-download-symbolic.svg": "folder-download.svg",
        "folder-documents-symbolic.svg": "folder-documents.svg",
        "folder-audio.svg": "folder-music.svg",
        "folder-sound.svg": "folder-music.svg",
        "folder-music-symbolic.svg": "folder-music.svg",
        "folder-images.svg": "folder-pictures.svg",
        "folder-photo.svg": "folder-pictures.svg",
        "folder-camera.svg": "folder-pictures.svg",
        "folder-pictures-symbolic.svg": "folder-pictures.svg",
        "folder-video.svg": "folder-videos.svg",
        "folder-movies.svg": "folder-videos.svg",
        "folder-videos-symbolic.svg": "folder-videos.svg",
        "folder-development.svg": "folder-code.svg",
        "folder-script.svg": "folder-code.svg",
        "folder-github.svg": "folder-git.svg",
        "folder-gitlab.svg": "folder-git.svg",
        "folder-dropbox.svg": "folder-cloud.svg",
        "folder-gdrive.svg": "folder-cloud.svg",
        "folder-google-drive.svg": "folder-cloud.svg",
        "folder-nextcloud.svg": "folder-cloud.svg",
        "folder-favorites.svg": "folder-starred.svg",
        "folder-important.svg": "folder-starred.svg",
        "folder-bookmark.svg": "folder-starred.svg",
        "folder-bookmarks.svg": "folder-starred.svg",
        "folder-tmp.svg": "folder-temp.svg",
        "folder-publicshare.svg": "folder-public.svg",
        
        # Encrypted folder symlinks
        "folder-encrypted.svg": "folder-locked.svg",
        "folder-crypt.svg": "folder-locked.svg",
        "folder-security.svg": "folder-locked.svg",
        "folder-private.svg": "folder-locked.svg",
        "folder-secret.svg": "folder-locked.svg",
        "folder-password.svg": "folder-locked.svg",
        "folder-plasma-vault.svg": "folder-vault.svg",
        "folder-decrypted.svg": "folder-unlocked.svg",
    }
    for link, target in places_symlinks.items():
        make_symlink("places", target, link)

    write_svg("places", "user-home.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><defs><linearGradient id="hg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C_STELLAR_CYAN}"/><stop offset="100%" stop-color="{C_PULSAR_VIO}"/></linearGradient></defs><circle cx="32" cy="32" r="26" fill="url(#hg)" fill-opacity="0.2" stroke="url(#hg)" stroke-width="2"/><path d="M 18 32 L 32 18 L 46 32 L 46 48 C 46 49 45 50 44 50 L 20 50 C 19 50 18 49 18 48 Z" fill="url(#hg)" stroke="{C_STAR_WHITE}" stroke-width="1.2"/><path d="M 28 50 L 28 36 L 36 36 L 36 50" fill="{C_VOID_DARK}"/></svg>''')
    write_svg("places", "user-desktop.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><rect x="10" y="14" width="44" height="30" rx="4" fill="{C_PULSAR_VIO}" fill-opacity="0.8" stroke="{C_STELLAR_CYAN}" stroke-width="1.5"/><rect x="14" y="18" width="36" height="22" fill="{C_VOID_DARK}"/><line x1="32" y1="44" x2="32" y2="52" stroke="{C_STELLAR_CYAN}" stroke-width="3.5"/><line x1="20" y1="52" x2="44" y2="52" stroke="{C_STELLAR_CYAN}" stroke-width="2.5" stroke-linecap="round"/><circle cx="32" cy="29" r="4" fill="{C_STELLAR_CYAN}"/></svg>''')
    write_svg("places", "user-trash.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><path d="M 22 18 L 42 18 M 28 14 L 36 14" stroke="{C_STARDUST}" stroke-width="2.5" stroke-linecap="round"/><path d="M 20 22 L 24 52 C 24.3 54 26 55.5 28 55.5 L 36 55.5 C 38 55.5 39.7 54 40 52 L 44 22 Z" fill="{C_VOID_CARD}" stroke="{C_STARDUST}" stroke-width="1.8"/><line x1="28" y1="28" x2="29" y2="48" stroke="{C_STAR_WHITE}" stroke-width="1.2"/><line x1="32" y1="28" x2="32" y2="48" stroke="{C_STAR_WHITE}" stroke-width="1.2"/><line x1="36" y1="28" x2="35" y2="48" stroke="{C_STAR_WHITE}" stroke-width="1.2"/></svg>''')
    write_svg("places", "user-trash-full.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><path d="M 22 18 L 42 18 M 28 14 L 36 14" stroke="{C_NEBULA_MAG}" stroke-width="2.5" stroke-linecap="round"/><path d="M 20 22 L 24 52 C 24.3 54 26 55.5 28 55.5 L 36 55.5 C 38 55.5 39.7 54 40 52 L 44 22 Z" fill="{C_PULSAR_VIO}" fill-opacity="0.7" stroke="{C_NEBULA_MAG}" stroke-width="1.8"/><line x1="28" y1="28" x2="29" y2="48" stroke="{C_STAR_WHITE}" stroke-width="1.2"/><line x1="32" y1="28" x2="32" y2="48" stroke="{C_STAR_WHITE}" stroke-width="1.2"/><line x1="36" y1="28" x2="35" y2="48" stroke="{C_STAR_WHITE}" stroke-width="1.2"/><circle cx="32" cy="30" r="3" fill="{C_SUPERNOVA_GOLD}"/></svg>''')
    make_symlink("places", "user-home.svg", "user-home-symbolic.svg")
    make_symlink("places", "user-trash.svg", "user-trash-symbolic.svg")
    make_symlink("places", "user-desktop.svg", "user-desktop-symbolic.svg")

    # ----------------------------------------------------
    # 2. MEDIA PLAYERS, PRINTERS & APPS
    # ----------------------------------------------------
    # Media Players (Native KDE & Generic FreeDesktop)
    write_svg("apps", "multimedia-player.svg", make_app_svg(C_PULSAR_VIO, C_STELLAR_CYAN, '<circle cx="32" cy="32" r="18" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="2"/><polygon points="28,24 40,32 28,40" fill="' + C_STELLAR_CYAN + '"/><circle cx="32" cy="32" r="5" fill="none" stroke="' + C_SUPERNOVA_GOLD + '" stroke-width="1.5"/>'))
    write_svg("apps", "elisa.svg", make_app_svg(C_STELLAR_CYAN, C_PULSAR_VIO, '<circle cx="32" cy="32" r="16" fill="' + C_VOID_DARK + '" stroke="' + C_STELLAR_CYAN + '" stroke-width="2"/><path d="M 28 42 A 4 4 0 1 1 24 38 L 24 24 L 38 20 L 38 38 A 4 4 0 1 1 34 34 L 34 24" fill="' + C_STAR_WHITE + '" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>'))

    make_symlink("apps", "multimedia-player.svg", "media-player.svg")
    make_symlink("apps", "multimedia-player.svg", "player.svg")
    make_symlink("apps", "multimedia-player.svg", "applications-multimedia.svg")
    make_symlink("apps", "multimedia-player.svg", "amarok.svg")
    make_symlink("apps", "multimedia-player.svg", "haruna.svg")
    make_symlink("apps", "elisa.svg", "org.kde.elisa.svg")

    # Printers & Printing Apps / Devices
    printer_glyph = '<rect x="14" y="24" width="36" height="22" rx="4" fill="' + C_VOID_DARK + '" stroke="' + C_STELLAR_CYAN + '" stroke-width="2"/><path d="M 20 24 L 20 14 C 20 12.8 21 12 22 12 L 42 12 C 43 12 44 12.8 44 14 L 44 24" fill="' + C_STAR_WHITE + '" fill-opacity="0.3" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/><rect x="20" y="34" width="24" height="16" rx="2" fill="' + C_VOID_CARD + '" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.5"/><line x1="24" y1="40" x2="40" y2="40" stroke="' + C_STAR_WHITE + '" stroke-width="1.5" stroke-linecap="round"/><circle cx="44" cy="29" r="2" fill="' + C_AURORA_EMERALD + '"/>'
    write_svg("apps", "cups.svg", make_app_svg(C_VOID_CARD, C_STELLAR_CYAN, printer_glyph))
    write_svg("apps", "system-config-printer.svg", make_app_svg(C_VOID_CARD, C_STELLAR_CYAN, printer_glyph))
    write_svg("devices", "printer.svg", make_app_svg(C_VOID_CARD, C_STELLAR_CYAN, printer_glyph))

    # Keyboard & Language Settings Apps
    lang_glyph = '<circle cx="32" cy="32" r="18" fill="none" stroke="' + C_STELLAR_CYAN + '" stroke-width="2"/><ellipse cx="32" cy="32" rx="9" ry="18" fill="none" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.5"/><line x1="14" y1="32" x2="50" y2="32" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.5"/><path d="M 17 23 C 22 26 42 26 47 23" fill="none" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.2"/><path d="M 17 41 C 22 38 42 38 47 41" fill="none" stroke="' + C_STELLAR_CYAN + '" stroke-width="1.2"/>'
    write_svg("apps", "preferences-desktop-keyboard.svg", make_app_svg(C_VOID_CARD, C_PULSAR_VIO, '<rect x="12" y="18" width="40" height="28" rx="5" fill="' + C_VOID_DARK + '" stroke="' + C_PULSAR_VIO + '" stroke-width="2"/><line x1="18" y1="26" x2="22" y2="26" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/><line x1="26" y1="26" x2="30" y2="26" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/><line x1="34" y1="26" x2="38" y2="26" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/><line x1="42" y1="26" x2="46" y2="26" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/><line x1="20" y1="32" x2="24" y2="32" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/><line x1="28" y1="32" x2="36" y2="32" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/><line x1="40" y1="32" x2="44" y2="32" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/><line x1="22" y1="38" x2="42" y2="38" stroke="' + C_STELLAR_CYAN + '" stroke-width="2.5" stroke-linecap="round"/>'))
    write_svg("apps", "preferences-desktop-locale.svg", make_app_svg(C_VOID_CARD, C_STELLAR_CYAN, lang_glyph))

    # Plasma Vault App Icon
    write_svg("apps", "plasma-vault.svg", make_app_svg(C_VOID_DARK, C_PULSAR_VIO, vault_emblem))

    # ----------------------------------------------------
    # 3. OFFICE DOCUMENTS & MIMETYPES (MS OFFICE & LIBREOFFICE)
    # ----------------------------------------------------
    office_mimetypes = {
        # Word / Writer
        "application-msword.svg": ("DOC", C_OFFICE_WORD, '<path d="M 20 20 L 26 36 L 32 23 L 38 36 L 44 20" stroke="' + C_STAR_WHITE + '" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'),
        "application-vnd.openxmlformats-officedocument.wordprocessingml.document.svg": ("DOCX", C_OFFICE_WORD, '<path d="M 20 20 L 26 36 L 32 23 L 38 36 L 44 20" stroke="' + C_STAR_WHITE + '" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'),
        "application-vnd.oasis.opendocument.text.svg": ("ODT", C_OFFICE_WORD, '<path d="M 22 22 L 42 22 M 22 27 L 42 27 M 22 32 L 36 32" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/>'),
        "application-rtf.svg": ("RTF", C_OFFICE_WORD, '<text x="32" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">RTF</text>'),
        "x-office-document.svg": ("DOC", C_OFFICE_WORD, '<path d="M 22 22 L 42 22 M 22 27 L 42 27 M 22 32 L 34 32" stroke="' + C_STAR_WHITE + '" stroke-width="2" stroke-linecap="round"/>'),

        # Excel / Calc
        "application-vnd.ms-excel.svg": ("XLS", C_OFFICE_EXCEL, '<path d="M 22 20 L 42 36 M 42 20 L 22 36" stroke="' + C_STAR_WHITE + '" stroke-width="3" stroke-linecap="round"/>'),
        "application-vnd.openxmlformats-officedocument.spreadsheetml.sheet.svg": ("XLSX", C_OFFICE_EXCEL, '<path d="M 22 20 L 42 36 M 42 20 L 22 36" stroke="' + C_STAR_WHITE + '" stroke-width="3" stroke-linecap="round"/>'),
        "application-vnd.oasis.opendocument.spreadsheet.svg": ("ODS", C_OFFICE_EXCEL, '<rect x="20" y="20" width="24" height="16" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/><line x1="32" y1="20" x2="32" y2="36" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><line x1="20" y1="28" x2="44" y2="28" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/>'),
        "text-csv.svg": ("CSV", C_OFFICE_EXCEL, '<text x="32" y="32" font-family="sans-serif" font-size="13" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">CSV</text>'),
        "x-office-spreadsheet.svg": ("CALC", C_OFFICE_EXCEL, '<rect x="20" y="20" width="24" height="16" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/><line x1="32" y1="20" x2="32" y2="36" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/><line x1="20" y1="28" x2="44" y2="28" stroke="' + C_STAR_WHITE + '" stroke-width="1.5"/>'),

        # PowerPoint / Impress
        "application-vnd.ms-powerpoint.svg": ("PPT", C_OFFICE_PPT, '<path d="M 24 36 L 24 20 L 36 20 C 40 20 40 28 36 28 L 24 28" stroke="' + C_STAR_WHITE + '" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'),
        "application-vnd.openxmlformats-officedocument.presentationml.presentation.svg": ("PPTX", C_OFFICE_PPT, '<path d="M 24 36 L 24 20 L 36 20 C 40 20 40 28 36 28 L 24 28" stroke="' + C_STAR_WHITE + '" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'),
        "application-vnd.oasis.opendocument.presentation.svg": ("ODP", C_OFFICE_PPT, '<rect x="20" y="20" width="24" height="16" rx="2" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/><polygon points="28,24 38,28 28,32" fill="' + C_STAR_WHITE + '"/>'),
        "x-office-presentation.svg": ("PRES", C_OFFICE_PPT, '<polygon points="28,24 38,28 28,32" fill="' + C_STAR_WHITE + '"/>'),

        # Access / Base & Drawings & Math
        "application-vnd.oasis.opendocument.database.svg": ("ODB", C_OFFICE_BASE, '<ellipse cx="32" cy="22" rx="10" ry="3.5" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/><path d="M 22 22 L 22 34 C 22 37 42 37 42 34 L 42 22" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/>'),
        "application-vnd.oasis.opendocument.graphics.svg": ("ODG", C_OFFICE_DRAW, '<circle cx="27" cy="25" r="5" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/><rect x="33" y="25" width="9" height="9" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/>'),
        "application-vnd.oasis.opendocument.formula.svg": ("ODF", C_OFFICE_MATH, '<path d="M 20 28 L 24 28 L 28 36 L 36 18 L 44 18" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'),
        "x-office-drawing.svg": ("DRAW", C_OFFICE_DRAW, '<polygon points="32,18 42,34 22,34" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="2"/>'),

        # PDF, E-books & Text
        "application-pdf.svg": ("PDF", C_PDF_RED, '<path d="M 22 34 C 22 26 28 20 34 20 C 38 20 42 24 42 28 C 42 34 32 36 22 34 Z" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="2"/>'),
        "application-epub+zip.svg": ("EPUB", C_PULSAR_VIO, '<path d="M 20 20 L 32 24 L 44 20 L 44 36 L 32 40 L 20 36 Z" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/><line x1="32" y1="24" x2="32" y2="40" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/>'),
    }

    for name, (label, color, glyph) in office_mimetypes.items():
        write_svg("mimetypes", name, make_doc_svg(label, color, glyph))

    # Office Symlinks
    office_symlinks = {
        "word.svg": "application-msword.svg",
        "excel.svg": "application-vnd.ms-excel.svg",
        "powerpoint.svg": "application-vnd.ms-powerpoint.svg",
        "ms-word.svg": "application-msword.svg",
        "ms-excel.svg": "application-vnd.ms-excel.svg",
        "ms-powerpoint.svg": "application-vnd.ms-powerpoint.svg",
        "application-vnd.oasis.opendocument.text-template.svg": "application-vnd.oasis.opendocument.text.svg",
        "application-vnd.oasis.opendocument.spreadsheet-template.svg": "application-vnd.oasis.opendocument.spreadsheet.svg",
        "application-vnd.oasis.opendocument.presentation-template.svg": "application-vnd.oasis.opendocument.presentation.svg",
    }
    for link, target in office_symlinks.items():
        make_symlink("mimetypes", target, link)

    # ----------------------------------------------------
    # 4. ARCHIVES & COMPRESSED PACKAGES
    # ----------------------------------------------------
    archive_definitions = {
        "application-zip.svg": ("ZIP", C_ARCHIVE_GOLD, '<rect x="22" y="16" width="20" height="20" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/><line x1="32" y1="16" x2="32" y2="36" stroke="' + C_SUPERNOVA_GOLD + '" stroke-width="2.5" stroke-dasharray="3 2"/>'),
        "application-x-7z-compressed.svg": ("7Z", C_ARCHIVE_GOLD, '<text x="32" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">7Z</text>'),
        "application-x-rar.svg": ("RAR", C_ARCHIVE_GOLD, '<rect x="20" y="18" width="8" height="18" fill="' + C_DANGER_RED + '" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/><rect x="28" y="18" width="8" height="18" fill="' + C_STELLAR_CYAN + '" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/><rect x="36" y="18" width="8" height="18" fill="' + C_SUPERNOVA_GOLD + '" stroke="' + C_STAR_WHITE + '" stroke-width="1.2"/>'),
        "application-x-tar.svg": ("TAR", C_ARCHIVE_GOLD, '<text x="32" y="32" font-family="sans-serif" font-size="13" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">TAR</text>'),
        "application-x-gzip.svg": ("GZ", C_ARCHIVE_GOLD, '<text x="32" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">GZ</text>'),
        "application-x-bzip2.svg": ("BZ2", C_ARCHIVE_GOLD, '<text x="32" y="32" font-family="sans-serif" font-size="13" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">BZ2</text>'),
        "application-x-xz.svg": ("XZ", C_ARCHIVE_GOLD, '<text x="32" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">XZ</text>'),
        "application-x-zstd.svg": ("ZST", C_ARCHIVE_GOLD, '<text x="32" y="32" font-family="sans-serif" font-size="13" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">ZST</text>'),
        "application-x-cd-image.svg": ("ISO", C_STELLAR_CYAN, '<circle cx="32" cy="27" r="10" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="2"/><circle cx="32" cy="27" r="3" fill="' + C_STELLAR_CYAN + '"/>'),
        "application-vnd.debian.binary-package.svg": ("DEB", C_DANGER_RED, '<circle cx="32" cy="27" r="8" fill="none" stroke="' + C_DANGER_RED + '" stroke-width="2.5"/><path d="M 32 23 C 34 23 36 25 36 27 C 36 30 30 31 30 34" fill="none" stroke="' + C_STAR_WHITE + '" stroke-width="1.8"/>'),
        "application-x-rpm.svg": ("RPM", C_STELLAR_CYAN, '<text x="32" y="32" font-family="sans-serif" font-size="13" font-weight="bold" fill="' + C_STAR_WHITE + '" text-anchor="middle">RPM</text>'),
        "application-vnd.android.package-archive.svg": ("APK", C_AURORA_EMERALD, '<path d="M 24 28 C 24 22 40 22 40 28 Z" fill="' + C_AURORA_EMERALD + '"/><circle cx="28" cy="25" r="1" fill="' + C_VOID_DARK + '"/><circle cx="36" cy="25" r="1" fill="' + C_VOID_DARK + '"/>'),
    }

    for name, (label, color, glyph) in archive_definitions.items():
        write_svg("mimetypes", name, make_doc_svg(label, color, glyph))

    archive_symlinks = {
        "archive-zip.svg": "application-zip.svg",
        "application-x-zip.svg": "application-zip.svg",
        "application-x-zip-compressed.svg": "application-zip.svg",
        "application-x-7zip.svg": "application-x-7z-compressed.svg",
        "application-x-rar-compressed.svg": "application-x-rar.svg",
        "application-x-compressed-tar.svg": "application-x-gzip.svg",
        "application-x-bzip-compressed-tar.svg": "application-x-bzip2.svg",
        "application-x-xz-compressed-tar.svg": "application-x-xz.svg",
        "application-x-zstd-compressed-tar.svg": "application-x-zstd.svg",
        "application-x-iso9660-image.svg": "application-x-cd-image.svg",
        "application-x-raw-disk-image.svg": "application-x-cd-image.svg",
        "package-x-generic.svg": "application-vnd.debian.binary-package.svg",
    }
    for link, target in archive_symlinks.items():
        make_symlink("mimetypes", target, link)

    # ----------------------------------------------------
    # 5. STATUS & SYSTEM TRAY (Unified Wi-Fi Line-Art Style)
    # ----------------------------------------------------
    import generate_tray_icons
    generate_tray_icons.gen_all_tray_icons()

    print("==========================================")
    print("Galaxy Universal Master Icon Suite Generated!")
    print("==========================================")

if __name__ == "__main__":
    gen_all()
