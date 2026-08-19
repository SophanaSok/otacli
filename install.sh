#!/bin/bash
set -e

CYAN='\033[1;36m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
BLUE='\033[1;34m'
NC='\033[0m' # No Color

# Resolve the checkout this script lives in, so the clone directory can be named anything
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_DIR="$HOME/.otacli_src"

clear 2>/dev/null || true
echo -e "${CYAN}====================================================${NC}"
echo -e "${GREEN}       Starting otacli installation...      ${NC}"
echo -e "${CYAN}====================================================${NC}\n"

echo -e "${YELLOW}[1/5] Installing system packages (mpv, chafa, wget)...${NC}"
if command -v pacman >/dev/null 2>&1; then
    sudo pacman -S --needed --noconfirm mpv chafa wget python python-pip libjxl
elif command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y mpv chafa wget python3-pip python3-venv
elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y mpv chafa wget python3-pip
else
    echo -e "${RED}[!] No supported package manager found (pacman/apt-get/dnf).${NC}"
    echo -e "${RED}    Install mpv, chafa, wget and python3 (with pip and venv) yourself, then re-run.${NC}"
    exit 1
fi
echo ""

echo -e "${YELLOW}[2/5] Removing outdated yt-dlp versions...${NC}"
if command -v pacman >/dev/null 2>&1; then
    sudo pacman -Rns --noconfirm yt-dlp 2>/dev/null || true
elif command -v apt-get >/dev/null 2>&1; then
    sudo apt-get remove -y yt-dlp || true
fi
echo ""

echo -e "${YELLOW}[3/5] Downloading the latest yt-dlp...${NC}"
sudo wget -q --show-progress https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
echo ""

echo -e "${YELLOW}[4/5] Configuring program files...${NC}"
if [ -d "$DEST_DIR" ]; then
    echo -e "${YELLOW}    Existing install found, replacing $DEST_DIR${NC}"
    rm -rf "$DEST_DIR"
fi

cp -r "$SRC_DIR" "$DEST_DIR"
rm -rf "$DEST_DIR/.git" "$DEST_DIR/.venv"
find "$DEST_DIR" -name "__pycache__" -type d -prune -exec rm -rf {} +

sudo install -m 755 "$DEST_DIR/otacli" /usr/local/bin/otacli
rm -f "$DEST_DIR/otacli"

find "$DEST_DIR" -type d -exec chmod 755 {} \;
find "$DEST_DIR" -type f -exec chmod 644 {} \;
echo ""

echo -e "${YELLOW}[5/5] Configuring Python libraries (this may take a while)...${NC}"
python3 -m venv "$DEST_DIR/.venv"
"$DEST_DIR/.venv/bin/pip" install --quiet --upgrade pip
"$DEST_DIR/.venv/bin/pip" install --quiet requests inquirerpy termcolor pillow rich curl-cffi
echo ""

mkdir -p "$HOME/.config/otacli"

echo -e "${GREEN}====================================================${NC}"
echo -e "${GREEN} [+] Installation completed successfully!${NC}"
echo -e "${BLUE} [i] You can now run ${YELLOW}otacli${BLUE} in your terminal.${NC}"
echo -e "${GREEN}====================================================${NC}"
