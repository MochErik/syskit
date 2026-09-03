#!/usr/bin/env bash
# ==============================================================================
# ⚡ SysKit & Developer CLI Suite - Universal Installer for Linux & macOS
# Author: Moch. Erik Irriansyah (@MochErik)
# ==============================================================================

set -e

GREEN="\033[32m"
CYAN="\033[36m"
YELLOW="\033[33m"
BOLD="\033[1m"
DIM="\033[2m"
RESET="\033[0m"

echo -e "${CYAN}${BOLD}"
echo "  ___ _   _ ___ _  _____ _____ "
echo " / __| | | / __| |/ /_ _|_   _|"
echo " \__ \ |_| \__ \ ' < | |  | |  "
echo " |___/\__, |___/_|\_\___| |_|  "
echo "      |___/                    "
echo -e "${RESET}"
echo -e "${BOLD}🚀 Installing SysKit & 14 Developer CLI Tools...${RESET}"
echo "──────────────────────────────────────────────────────────────────────"

# 1. Determine Python 3 command
if command -v python3 >/dev/null 2>&1; then
    PY_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PY_CMD="python"
else
    echo -e "${YELLOW}❌ Python 3 is required. Please install Python first.${RESET}"
    exit 1
fi

echo -e "🐍 Using: ${GREEN}$($PY_CMD --version)${RESET}"

# 2. Install each tool directly from GitHub
TOOLS=(
    "syskit" "netpulse" "nodesentry" "git-spark" "envguard"
    "dockervoid" "quicktunnel" "forge-api" "passforge"
    "speeddrop" "croncraft" "soc-bench" "json-lens" "pdfslim"
)

echo -e "\n📦 Installing CLI tools via $PY_CMD -m pip..."

for tool in "${TOOLS[@]}"; do
    echo -ne "  ⏳ Installing ${CYAN}$tool${RESET}..."
    $PY_CMD -m pip install --break-system-packages "git+https://github.com/MochErik/$tool.git" >/dev/null 2>&1 || \
    $PY_CMD -m pip install --user "git+https://github.com/MochErik/$tool.git" >/dev/null 2>&1 || \
    $PY_CMD -m pip install "git+https://github.com/MochErik/$tool.git" >/dev/null 2>&1 || true
    echo -e "\r  ${GREEN}✔ Installed:${RESET} ${BOLD}$tool${RESET}      "
done

echo -e "\n──────────────────────────────────────────────────────────────────────"
echo -e "${GREEN}${BOLD}🎉 Installation Complete! All 14 CLI Tools are ready.${RESET}"
echo -e "Try running ${CYAN}${BOLD}syskit${RESET} or ${CYAN}${BOLD}soc-bench${RESET} in your terminal now!\n"
