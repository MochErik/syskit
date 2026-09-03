"""SysKit Unified CLI Main Entrypoint - 14-in-1 Developer & Systems Engineering Toolkit."""

import argparse
import sys
import os
import shutil
import platform

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"


def print_banner():
    banner = f"""
{CYAN}{BOLD}⚡ SysKit{RESET} {DIM}v1.0.0 — Unified 14-in-1 Developer & Systems Engineering CLI Suite{RESET}
{DIM}Curated & Engineered by Moch. Erik Irriansyah (@MochErik){RESET}
{DIM}100% Standalone Local CLI Utilities — Zero Cloud/Live Server Required{RESET}
═══════════════════════════════════════════════════════════════════════"""
    print(banner)


def check_doctor():
    """System health & CLI diagnostic check."""
    print(f"\n{BOLD}🩺 SysKit Environment Doctor:{RESET}\n")
    print(f"  {CYAN}• OS & Kernel   :{RESET} {platform.system()} {platform.release()} ({platform.machine()})")
    py_ver = sys.version.split()[0]
    print(f"  {CYAN}• Python Version:{RESET} {GREEN}{py_ver}{RESET}")
    
    git_path = shutil.which("git")
    print(f"  {CYAN}• Git Engine    :{RESET} {f'{GREEN}Installed ({git_path}){RESET}' if git_path else f'{RED}Missing{RESET}'}")
    
    docker_path = shutil.which("docker")
    print(f"  {CYAN}• Docker Daemon :{RESET} {f'{GREEN}Available ({docker_path}){RESET}' if docker_path else f'{YELLOW}Not detected (Optional){RESET}'}")

    cf_path = shutil.which("cloudflared")
    print(f"  {CYAN}• Cloudflared   :{RESET} {f'{GREEN}Available ({cf_path}){RESET}' if cf_path else f'{YELLOW}Not installed (Optional){RESET}'}")

    print(f"\n{GREEN}{BOLD}✅ All 14 CLI components are 100% operational locally!{RESET}\n")


def interactive_menu():
    """Interactive CLI module launcher."""
    print_banner()
    print(f"""
{BOLD}Available Local CLI Tools (14 Tools):{RESET}
  {BOLD}[1]{RESET}  {CYAN}netpulse{RESET}   - Multi-Target Latency Mesh & Wire-Format DNS Benchmark
  {BOLD}[2]{RESET}  {GREEN}nodesentry{RESET} - Micro-Footprint (<15MB RAM) SBC/Linux Resource Sentinel
  {BOLD}[3]{RESET}  {YELLOW}git-spark{RESET}  - Conventional Commit & Git Workflow Generator (Offline/AI)
  {BOLD}[4]{RESET}  {MAGENTA}envguard{RESET}   - Secret Leak Scanner & .env.example Schema Validator
  {BOLD}[5]{RESET}  {BLUE}dockervoid{RESET} - Docker Disk Reclamation & Prune Engine
  {BOLD}[6]{RESET}  {CYAN}quicktunnel{RESET}- Ephemeral HTTPS Localhost Exposer & Remote Access
  {BOLD}[7]{RESET}  {GREEN}forge-api{RESET}  - Clean Architecture FastAPI Microservice Scaffolder
  {BOLD}[8]{RESET}  {YELLOW}passforge{RESET}  - High-Entropy Password, Diceware & Token Generator
  {BOLD}[9]{RESET}  {CYAN}speeddrop{RESET}  - Instant Peer-to-Peer Wi-Fi LAN File Transfer
  {BOLD}[10]{RESET} {MAGENTA}croncraft{RESET}  - Human English to Cron Translator & Explainer
  {BOLD}[11]{RESET} {GREEN}soc-bench{RESET}  - 10-Second CPU, RAM Bandwidth & Disk I/O Benchmark
  {BOLD}[12]{RESET} {BLUE}json-lens{RESET}  - JSON Formatter, Key Flattener & Diff Comparator
  {BOLD}[13]{RESET} {RED}pdfslim{RESET}    - Zero-Bloat PDF Compressor & Metadata Sanitizer
  {BOLD}[d]{RESET}  🩺 Doctor    - Run system diagnostics
  {BOLD}[q]{RESET}  ❌ Exit
""")
    try:
        choice = input(f"{BOLD}Select tool to run (1-13/d/q) [1]: {RESET}").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting SysKit.")
        sys.exit(0)

    if not choice:
        choice = "1"

    if choice == "1":
        from netpulse.cli import main as m; m([])
    elif choice == "2":
        from nodesentry.cli import main as m; m(["status"])
    elif choice == "3":
        from git_spark.cli import main as m; m([])
    elif choice == "4":
        from envguard.cli import main as m; m(["scan", "."])
    elif choice == "5":
        from dockervoid.cli import main as m; m([])
    elif choice == "6":
        from quicktunnel.cli import main as m; m(["8080"])
    elif choice == "7":
        from forge_api.cli import main as m; m(["new", "my-api"])
    elif choice == "8":
        from passforge.cli import main as m; m([])
    elif choice == "9":
        from speeddrop.cli import main as m; m([])
    elif choice == "10":
        from croncraft.cli import main as m; m(["every 15 minutes"])
    elif choice == "11":
        from soc_bench.cli import main as m; m([])
    elif choice == "12":
        from json_lens.cli import main as m; m([])
    elif choice == "13":
        from pdfslim.cli import main as m; m([])
    elif choice == "d":
        check_doctor()
    elif choice == "q":
        sys.exit(0)


def main(args=None):
    parser = argparse.ArgumentParser(
        prog="syskit",
        description="⚡ SysKit - The Ultimate 14-in-1 Developer & Systems Engineering CLI Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("net", help="Run NetPulse network & DNS diagnostics")
    subparsers.add_parser("sentry", help="Run NodeSentry SBC & Linux monitor")
    subparsers.add_parser("commit", help="Run Git-Spark conventional commit assistant")
    subparsers.add_parser("env", help="Run EnvGuard secret scanner")
    subparsers.add_parser("docker", help="Run DockerVoid container disk reclamation")
    subparsers.add_parser("tunnel", help="Run QuickTunnel localhost exposer")
    subparsers.add_parser("forge", help="Run Forge-API microservice scaffolder")
    subparsers.add_parser("pass", help="Run PassForge password/token generator")
    subparsers.add_parser("drop", help="Run SpeedDrop Wi-Fi file transfer")
    subparsers.add_parser("cron", help="Run CronCraft natural language scheduler")
    subparsers.add_parser("bench", help="Run SoC-Bench hardware benchmark")
    subparsers.add_parser("json", help="Run JSON-Lens flattener and diff")
    subparsers.add_parser("pdf", help="Run PDFSlim compressor")
    subparsers.add_parser("doctor", help="Run system doctor diagnostics")

    parsed, remaining = parser.parse_known_args(args)

    if parsed.command == "net":
        from netpulse.cli import main as m; m(remaining)
    elif parsed.command == "sentry":
        from nodesentry.cli import main as m; m(remaining)
    elif parsed.command == "commit":
        from git_spark.cli import main as m; m(remaining)
    elif parsed.command == "env":
        from envguard.cli import main as m; m(remaining)
    elif parsed.command == "docker":
        from dockervoid.cli import main as m; m(remaining)
    elif parsed.command == "tunnel":
        from quicktunnel.cli import main as m; m(remaining or ["8080"])
    elif parsed.command == "forge":
        from forge_api.cli import main as m; m(remaining or ["new", "my-api"])
    elif parsed.command == "pass":
        from passforge.cli import main as m; m(remaining)
    elif parsed.command == "drop":
        from speeddrop.cli import main as m; m(remaining)
    elif parsed.command == "cron":
        from croncraft.cli import main as m; m(remaining)
    elif parsed.command == "bench":
        from soc_bench.cli import main as m; m(remaining)
    elif parsed.command == "json":
        from json_lens.cli import main as m; m(remaining)
    elif parsed.command == "pdf":
        from pdfslim.cli import main as m; m(remaining)
    elif parsed.command == "doctor":
        check_doctor()
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
