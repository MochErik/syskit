"""SysKit Unified CLI Main Entrypoint."""

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


def print_banner():
    banner = f"""
{CYAN}{BOLD}⚡ SysKit{RESET} {DIM}v1.0.0 — Unified Developer & Systems Engineering CLI Suite{RESET}
{DIM}Curated & Engineered by Moch. Erik Irriansyah (@MochErik){RESET}
{DIM}100% Standalone Local CLI Utilities — Zero Cloud/Live Server Required{RESET}
═══════════════════════════════════════════════════════════════════════"""
    print(banner)


def check_doctor():
    """System health & CLI diagnostic check."""
    print(f"\n{BOLD}🩺 SysKit Environment Doctor:{RESET}\n")
    
    # 1. OS & Architecture
    print(f"  {CYAN}• OS & Kernel   :{RESET} {platform.system()} {platform.release()} ({platform.machine()})")
    
    # 2. Python Version
    py_ver = sys.version.split()[0]
    print(f"  {CYAN}• Python Version:{RESET} {GREEN}{py_ver}{RESET}")
    
    # 3. Git CLI
    git_path = shutil.which("git")
    git_status = f"{GREEN}Installed ({git_path}){RESET}" if git_path else f"{RED}Missing{RESET}"
    print(f"  {CYAN}• Git Engine    :{RESET} {git_status}")
    
    # 4. Docker CLI
    docker_path = shutil.which("docker")
    docker_status = f"{GREEN}Available ({docker_path}){RESET}" if docker_path else f"{YELLOW}Not detected (Optional){RESET}"
    print(f"  {CYAN}• Docker Daemon :{RESET} {docker_status}")

    # 5. Cloudflared
    cf_path = shutil.which("cloudflared")
    cf_status = f"{GREEN}Available ({cf_path}){RESET}" if cf_path else f"{YELLOW}Not installed (Optional for QuickTunnel){RESET}"
    print(f"  {CYAN}• Cloudflared   :{RESET} {cf_status}")

    print(f"\n{GREEN}{BOLD}✅ All core CLI components are 100% operational locally!{RESET}\n")


def interactive_menu():
    """Interactive CLI module launcher."""
    print_banner()
    print(f"""
{BOLD}Available Local CLI Tools:{RESET}
  {BOLD}[1]{RESET} {CYAN}netpulse{RESET}   - Multi-Target Latency Mesh & Wire-Format DNS Benchmark
  {BOLD}[2]{RESET} {GREEN}nodesentry{RESET} - Micro-Footprint (<15MB RAM) SBC/Linux Resource Sentinel
  {BOLD}[3]{RESET} {YELLOW}git-spark{RESET}  - Conventional Commit & Git Workflow Generator (Offline/AI)
  {BOLD}[4]{RESET} {MAGENTA}envguard{RESET}   - Secret Leak Scanner & .env.example Schema Validator
  {BOLD}[5]{RESET} {BLUE}dockervoid{RESET} - Docker Disk Reclamation & Prune Engine
  {BOLD}[6]{RESET} {CYAN}quicktunnel{RESET}- Ephemeral HTTPS Localhost Exposer & Remote Access
  {BOLD}[7]{RESET} {GREEN}forge-api{RESET}  - Clean Architecture FastAPI Microservice Scaffolder
  {BOLD}[d]{RESET} 🩺 Doctor    - Run system diagnostics
  {BOLD}[q]{RESET} ❌ Exit
""")
    try:
        choice = input(f"{BOLD}Select tool to run (1-7/d/q) [1]: {RESET}").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting SysKit.")
        sys.exit(0)

    if not choice:
        choice = "1"

    if choice == "1":
        from netpulse.cli import main as netpulse_main
        netpulse_main([])
    elif choice == "2":
        from nodesentry.cli import main as nodesentry_main
        nodesentry_main(["status"])
    elif choice == "3":
        from git_spark.cli import main as gitspark_main
        gitspark_main([])
    elif choice == "4":
        from envguard.cli import main as envguard_main
        envguard_main(["scan", "."])
    elif choice == "5":
        from dockervoid.cli import main as dockervoid_main
        dockervoid_main([])
    elif choice == "6":
        from quicktunnel.cli import main as quicktunnel_main
        port_in = input("Enter local port to expose (e.g. 3000, 8080): ").strip()
        if port_in.isdigit():
            quicktunnel_main([port_in])
    elif choice == "7":
        from forge_api.cli import main as forge_main
        name_in = input("Enter new microservice project name: ").strip()
        if name_in:
            forge_main(["new", name_in])
    elif choice == "d":
        check_doctor()
    elif choice == "q":
        sys.exit(0)
    else:
        print(f"{RED}Invalid selection.{RESET}")


def main(args=None):
    parser = argparse.ArgumentParser(
        prog="syskit",
        description="⚡ SysKit - The Ultimate Developer & Systems Engineering CLI Toolkit",
        epilog="Examples:\n"
               "  syskit                     # Launch interactive tool selector\n"
               "  syskit net                 # Run NetPulse network & DNS diagnostics\n"
               "  syskit sentry              # Run NodeSentry resource snapshot\n"
               "  syskit commit              # Run Git-Spark conventional commit picker\n"
               "  syskit env                 # Run EnvGuard secret scanner\n"
               "  syskit docker              # Run DockerVoid disk analyzer\n"
               "  syskit tunnel 3000         # Expose local port 3000 via QuickTunnel\n"
               "  syskit forge new my-api    # Scaffold new FastAPI project\n"
               "  syskit doctor              # Check local system dependencies\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command")
    
    # Subcommands mapping
    subparsers.add_parser("net", help="Run NetPulse network & DNS diagnostics")
    subparsers.add_parser("sentry", help="Run NodeSentry SBC & Linux monitor")
    subparsers.add_parser("commit", help="Run Git-Spark conventional commit assistant")
    subparsers.add_parser("env", help="Run EnvGuard secret scanner")
    subparsers.add_parser("docker", help="Run DockerVoid container disk reclamation")
    
    tunnel_p = subparsers.add_parser("tunnel", help="Run QuickTunnel localhost exposer")
    tunnel_p.add_argument("port", type=int, nargs="?", default=8080, help="Local port to expose")

    forge_p = subparsers.add_parser("forge", help="Run Forge-API microservice scaffolder")
    forge_p.add_argument("action", nargs="?", default="new", help="Action (new)")
    forge_p.add_argument("name", nargs="?", default="my-service", help="Project name")

    subparsers.add_parser("doctor", help="Run system doctor diagnostics")

    parsed, remaining = parser.parse_known_args(args)

    if parsed.command == "net":
        from netpulse.cli import main as netpulse_main
        netpulse_main(remaining)
    elif parsed.command == "sentry":
        from nodesentry.cli import main as nodesentry_main
        nodesentry_main(remaining)
    elif parsed.command == "commit":
        from git_spark.cli import main as gitspark_main
        gitspark_main(remaining)
    elif parsed.command == "env":
        from envguard.cli import main as envguard_main
        envguard_main(remaining)
    elif parsed.command == "docker":
        from dockervoid.cli import main as dockervoid_main
        dockervoid_main(remaining)
    elif parsed.command == "tunnel":
        from quicktunnel.cli import main as quicktunnel_main
        quicktunnel_main([str(parsed.port)])
    elif parsed.command == "forge":
        from forge_api.cli import main as forge_main
        forge_main([parsed.action, parsed.name])
    elif parsed.command == "doctor":
        check_doctor()
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
