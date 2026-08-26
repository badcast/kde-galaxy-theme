#!/usr/bin/env bash
# ==============================================================================
# Galaxy Cosmic Suite - Uninstaller for KDE Plasma 6
# ==============================================================================

set -e

if [[ $EUID -eq 0 ]]; then
    INSTALL_DIR="/usr/share"
else
    INSTALL_DIR="${XDG_DATA_HOME:-$HOME/.local/share}"
fi

echo "Removing Galaxy theme components from $INSTALL_DIR..."

rm -f "$INSTALL_DIR/color-schemes/GalaxyDark.colors"
rm -rf "$INSTALL_DIR/plasma/desktoptheme/Galaxy-Dark"
rm -rf "$INSTALL_DIR/aurorae/themes/Galaxy-Dark-Aurorae"
rm -rf "$INSTALL_DIR/icons/Galaxy-Icons"
rm -rf "$INSTALL_DIR/icons/Galaxy-Cursors"
rm -rf "$INSTALL_DIR/plasma/look-and-feel/org.galaxy.desktop"
rm -rf "$INSTALL_DIR/wallpapers/Galaxy-Dark"

echo "Galaxy Cosmic Suite removed."
