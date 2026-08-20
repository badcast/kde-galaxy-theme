#!/usr/bin/env bash
# ==============================================================================
# 🌌 Galaxy Theme KDE - Master Installer for KDE Plasma 6 (>= 6.7)
# Author:  badcast <lmecomposer@gmail.com>
# Project: Galaxy Theme KDE
#
# Installs & Configures:
#   1. Color Scheme: GalaxyDark.colors
#   2. Plasma Desktop Theme: Galaxy-Dark
#   3. Aurorae Window Decoration: Galaxy-Dark-Aurorae (__aurorae__svg__Galaxy-Dark-Aurorae)
#   4. SVG Icon Theme: Galaxy-Icons (380+ bespoke vector icons & symlinks)
#   5. Cursor Theme: Galaxy-Cursors (Shadowed high-contrast Xcursors)
#   6. Global Look-and-Feel Package: org.galaxy.desktop
#   7. Kvantum Application Theme: Galaxy-Dark (Adapted from KvMojave)
#
# Usage:
#   ./install.sh           Install all theme components
#   ./install.sh --apply   Install and immediately apply all components
#   ./install.sh --build   Regenerate all vector assets and install
#   ./install.sh --uninstall Remove all installed Galaxy theme files
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APPLY_NOW=false
REBUILD_FIRST=false
UNINSTALL_MODE=false

for arg in "$@"; do
    case "$arg" in
        --apply|-a)
            APPLY_NOW=true
            ;;
        --build|-b)
            REBUILD_FIRST=true
            ;;
        --uninstall|-u)
            UNINSTALL_MODE=true
            ;;
        --help|-h)
            echo "Usage: ./install.sh [OPTIONS]"
            echo "Options:"
            echo "  --apply, -a       Install and immediately apply the theme"
            echo "  --build, -b       Re-generate all vector assets before installing"
            echo "  --uninstall, -u   Remove installed Galaxy theme components"
            echo "  --help, -h        Show this help message"
            exit 0
            ;;
    esac
done

if [[ $EUID -eq 0 ]]; then
    INSTALL_DIR="/usr/share"
    KVANTUM_DIR="/usr/share/Kvantum"
    echo "⚡ Running as root: System-wide path ($INSTALL_DIR)"
else
    INSTALL_DIR="${XDG_DATA_HOME:-$HOME/.local/share}"
    KVANTUM_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/Kvantum"
    echo "🚀 Running for user: Local path ($INSTALL_DIR)"
fi

if [[ "$UNINSTALL_MODE" = true ]]; then
    echo "🗑️ Removing Galaxy theme components..."
    rm -rf "$INSTALL_DIR/color-schemes/GalaxyDark.colors"
    rm -rf "$INSTALL_DIR/plasma/desktoptheme/Galaxy-Dark"
    rm -rf "$INSTALL_DIR/aurorae/themes/Galaxy-Dark-Aurorae"
    rm -rf "$INSTALL_DIR/icons/Galaxy-Icons"
    rm -rf "$INSTALL_DIR/icons/Galaxy-Cursors"
    rm -rf "$INSTALL_DIR/plasma/look-and-feel/org.galaxy.desktop"
    rm -rf "$INSTALL_DIR/wallpapers/Galaxy-Dark"
    rm -rf "$KVANTUM_DIR/Galaxy-Dark"
    rm -f "$HOME/.cache/plasma_theme_Galaxy-Dark.kcache"
    echo "✅ Galaxy Theme successfully uninstalled."
    exit 0
fi

if [[ "$REBUILD_FIRST" = true ]]; then
    echo "⚙️ Regenerating all vector assets and icons..."
    python3 "$SCRIPT_DIR/scripts/generate_assets.py"
    python3 "$SCRIPT_DIR/scripts/generate_icons.py"
    python3 "$SCRIPT_DIR/scripts/generate_kvantum.py"
    python3 "$SCRIPT_DIR/scripts/generate_aurorae.py"
    python3 "$SCRIPT_DIR/scripts/build_cursors.py" || true
fi

echo ""
echo "=========================================="
echo "🌌 Installing Galaxy Cosmic Suite for KDE 6"
echo "=========================================="

# 1. Color Scheme
echo "-> [1/8] Installing Color Scheme: GalaxyDark..."
mkdir -p "$INSTALL_DIR/color-schemes"
cp -f "$SCRIPT_DIR/color-schemes/"*.colors "$INSTALL_DIR/color-schemes/"

# 2. Plasma Desktop Theme
echo "-> [2/8] Installing Plasma Desktop Theme: Galaxy-Dark..."
mkdir -p "$INSTALL_DIR/plasma/desktoptheme/Galaxy-Dark"
cp -a "$SCRIPT_DIR/plasma/desktoptheme/Galaxy-Dark/"* "$INSTALL_DIR/plasma/desktoptheme/Galaxy-Dark/"
rm -f "$HOME/.cache/plasma_theme_Galaxy-Dark.kcache"

# 3. Aurorae Window Decoration
echo "-> [3/8] Installing Aurorae Decoration: Galaxy-Dark-Aurorae..."
mkdir -p "$INSTALL_DIR/aurorae/themes/Galaxy-Dark-Aurorae"
cp -a "$SCRIPT_DIR/aurorae/themes/Galaxy-Dark-Aurorae/"* "$INSTALL_DIR/aurorae/themes/Galaxy-Dark-Aurorae/"

# 4. SVG Icon Theme
echo "-> [4/8] Installing SVG Icon Theme: Galaxy-Icons..."
mkdir -p "$INSTALL_DIR/icons/Galaxy-Icons"
cp -a "$SCRIPT_DIR/icons/Galaxy-Icons/"* "$INSTALL_DIR/icons/Galaxy-Icons/"
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
    gtk-update-icon-cache -f -q "$INSTALL_DIR/icons/Galaxy-Icons" 2>/dev/null || true
fi

# 5. Cursor Theme
echo "-> [5/8] Installing Cursor Theme: Galaxy-Cursors..."
mkdir -p "$INSTALL_DIR/icons/Galaxy-Cursors"
cp -a "$SCRIPT_DIR/cursors/Galaxy-Cursors/"* "$INSTALL_DIR/icons/Galaxy-Cursors/"

# Also install to legacy ~/.icons for X11/GTK fallback
if [[ $EUID -ne 0 ]]; then
    mkdir -p "$HOME/.icons/Galaxy-Cursors"
    cp -a "$SCRIPT_DIR/cursors/Galaxy-Cursors/"* "$HOME/.icons/Galaxy-Cursors/"
    
    # Configure default cursor theme fallback
    mkdir -p "$HOME/.icons/default" "$INSTALL_DIR/icons/default"
    cat > "$HOME/.icons/default/index.theme" <<EOF
[Icon Theme]
Name=Default
Comment=Default Cursor Theme
Inherits=Galaxy-Cursors
EOF
    cp "$HOME/.icons/default/index.theme" "$INSTALL_DIR/icons/default/index.theme"
fi

# 6. Global Look-and-Feel Package
echo "-> [6/8] Installing Global Theme: org.galaxy.desktop..."
mkdir -p "$INSTALL_DIR/plasma/look-and-feel/org.galaxy.desktop"
cp -a "$SCRIPT_DIR/look-and-feel/org.galaxy.desktop/"* "$INSTALL_DIR/plasma/look-and-feel/org.galaxy.desktop/"

# 7. Kvantum Application Theme
echo "-> [7/8] Installing Kvantum Theme: Galaxy-Dark..."
mkdir -p "$KVANTUM_DIR/Galaxy-Dark"
cp -a "$SCRIPT_DIR/Kvantum/Galaxy-Dark/"* "$KVANTUM_DIR/Galaxy-Dark/"

# 8. Cosmic Wallpaper
echo "-> [8/8] Installing Cosmic Wallpaper: Galaxy-Dark..."
mkdir -p "$INSTALL_DIR/wallpapers/Galaxy-Dark"
cp -a "$SCRIPT_DIR/wallpapers/Galaxy-Dark/"* "$INSTALL_DIR/wallpapers/Galaxy-Dark/"

# Configure Kvantum selection for user
if [[ $EUID -ne 0 ]]; then
    mkdir -p "$HOME/.config/Kvantum"
    cat > "$HOME/.config/Kvantum/kvantum.kvconfig" <<EOF
[General]
theme=Galaxy-Dark
EOF
fi

# Update Sycoca
if command -v kbuildsycoca6 >/dev/null 2>&1; then
    kbuildsycoca6 --noincremental 2>/dev/null || true
fi

# Apply components if requested or if running interactively
if [[ "$APPLY_NOW" = true ]]; then
    echo ""
    echo "🚀 Applying Galaxy Cosmic Theme across KDE Plasma 6..."

    # Colors & Look and Feel
    command -v plasma-apply-colorscheme >/dev/null 2>&1 && plasma-apply-colorscheme GalaxyDark || true
    command -v plasma-apply-desktoptheme >/dev/null 2>&1 && plasma-apply-desktoptheme Galaxy-Dark || true
    command -v plasma-apply-cursortheme >/dev/null 2>&1 && plasma-apply-cursortheme Galaxy-Cursors || true
    command -v plasma-apply-wallpaperimage >/dev/null 2>&1 && plasma-apply-wallpaperimage "$INSTALL_DIR/wallpapers/Galaxy-Dark/contents/images/2752x1536.jpeg" >/dev/null 2>&1 || true

    # Kvantum Style, Cursor, & Icons
    if command -v kwriteconfig6 >/dev/null 2>&1; then
        kwriteconfig6 --file kdeglobals --group KDE --key widgetStyle kvantum
        kwriteconfig6 --file kdeglobals --group Icons --key Theme Galaxy-Icons
        kwriteconfig6 --file kdeglobals --group General --key ColorScheme GalaxyDark
        kwriteconfig6 --file kcminputrc --group Mouse --key cursorTheme Galaxy-Cursors
        kwriteconfig6 --file kcminputrc --group Mouse --key cursorSize 24

        # Aurorae Window Decoration
        kwriteconfig6 --file kwinrc --group org.kde.kdecoration2 --key library org.kde.kwin.aurorae
        kwriteconfig6 --file kwinrc --group org.kde.kdecoration2 --key theme __aurorae__svg__Galaxy-Dark-Aurorae
    fi

    # Refresh KWin & PlasmaShell live
    if command -v qdbus6 >/dev/null 2>&1; then
        qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure 2>/dev/null || true
        qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.refreshCurrentShell 2>/dev/null || true
    fi
    echo "✨ All components applied live!"
fi

echo ""
echo "=========================================="
echo "✨ Installation Completed Successfully! ✨"
echo "=========================================="
echo ""
echo "To apply theme components at any time:"
echo "  ./install.sh --apply"
echo ""
echo "Or via System Settings:"
echo "  1. System Settings -> Colors & Themes -> Global Theme -> Select 'Galaxy Dark'"
echo "  2. Window Decorations -> Select 'Galaxy Dark Aurorae'"
echo "  3. Application Style -> Select 'kvantum'"
echo ""
