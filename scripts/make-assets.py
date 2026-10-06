#!/usr/bin/env python3
"""Field-manual SVG assets for the GitHub profile. Palette: charcoal / brick / cream."""
from pathlib import Path

OUT = Path("/home/kali/github/DonMorpheus/assets")
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "ui-sans-serif, system-ui, Segoe UI, Helvetica, Arial, sans-serif"
BG, PANEL, LINE = "#120e0b", "#1c1612", "#3d2e24"
SPINE, BRICK, CREAM, MUTED = "#9b2d22", "#c44536", "#ead9c4", "#8a7360"


def write(name: str, svg: str) -> None:
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")


def band(label: str, filename: str) -> None:
    write(
        filename,
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72">
  <rect width="1280" height="72" fill="{BG}"/>
  <rect x="0" y="0" width="10" height="72" fill="{SPINE}"/>
  <line x1="36" y1="36" x2="470" y2="36" stroke="{LINE}" stroke-width="1"/>
  <text x="640" y="42" fill="{CREAM}" font-family="{FONT}" font-size="15" letter-spacing="6" text-anchor="middle">{label}</text>
  <line x1="810" y1="36" x2="1244" y2="36" stroke="{LINE}" stroke-width="1"/>
</svg>''',
    )


def rule() -> None:
    write(
        "rule.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 20" width="1280" height="20">
  <rect width="1280" height="20" fill="{BG}"/>
  <line x1="0" y1="10" x2="1280" y2="10" stroke="{LINE}" stroke-width="1"/>
  <rect x="634" y="6" width="12" height="8" fill="{SPINE}"/>
</svg>''',
    )


def spectrum() -> None:
    cells = [
        ("Zero-Day Research &amp; Exploit Development", "Crash-to-exploit. Parsers, services, IPC."),
        ("Kernel Exploitation, Rootkits &amp; Post-Ex", "Ring-0, persist, operator follow-through."),
        ("Reverse Engineering &amp; Malware Analysis", "Binaries, implants, the other side of the kit."),
        ("APT Simulation", "Full-chain adversary simulation in authorized labs."),
        ("Hardware Hacking", "CAN bus, ECU, RFID, SDR / GSM interception."),
        ("Mobile &amp; Android", "Device, app, and operator access on the handset."),
        ("C2 Infrastructure &amp; Evasion", "Software, listeners, implants, OPSEC of the callback."),
        ("Network, Packets &amp; WiFi", "Traffic analysis, packet crafting, wireless pentest."),
    ]
    cards = []
    for i, (title, sub) in enumerate(cells):
        col, row = i % 2, i // 2
        x, y = 36 + col * 622, 78 + row * 112
        cards.append(
            f'''  <rect x="{x}" y="{y}" width="606" height="100" fill="{PANEL}"/>
  <rect x="{x}" y="{y}" width="5" height="100" fill="{SPINE}"/>
  <circle cx="{x + 28}" cy="{y + 34}" r="4" fill="{BRICK}"/>
  <text x="{x + 46}" y="{y + 40}" fill="{CREAM}" font-family="{FONT}" font-size="15">{title}</text>
  <text x="{x + 46}" y="{y + 68}" fill="{MUTED}" font-family="{SANS}" font-size="14">{sub}</text>'''
        )
    inner = "\n".join(cards)
    write(
        "operations.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 540" width="1280" height="540">
  <rect width="1280" height="540" fill="{BG}"/>
  <rect x="0" y="0" width="10" height="540" fill="{SPINE}"/>
  <text x="36" y="42" fill="{MUTED}" font-family="{FONT}" font-size="12" letter-spacing="5">OPERATIONS</text>
  <line x1="36" y1="58" x2="1244" y2="58" stroke="{LINE}" stroke-width="1"/>
{inner}
</svg>''',
    )


def adjacent() -> None:
    items = [
        "OSINT",
        "Social engineering",
        "Memory forensics",
        "IDS / IPS evasion",
        "Incident response",
        "ISO 27001  ·  NIST",
    ]
    cards = []
    for i, label in enumerate(items):
        col, row = i % 3, i // 3
        x, y = 36 + col * 414, 78 + row * 80
        cards.append(
            f'''  <rect x="{x}" y="{y}" width="398" height="68" fill="{PANEL}"/>
  <rect x="{x}" y="{y}" width="5" height="68" fill="{SPINE}"/>
  <text x="{x + 24}" y="{y + 42}" fill="{CREAM}" font-family="{FONT}" font-size="15">{label}</text>'''
        )
    inner = "\n".join(cards)
    write(
        "adjacent.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 246" width="1280" height="246">
  <rect width="1280" height="246" fill="{BG}"/>
  <rect x="0" y="0" width="10" height="246" fill="{SPINE}"/>
  <text x="36" y="42" fill="{MUTED}" font-family="{FONT}" font-size="12" letter-spacing="5">ALSO IN PRACTICE</text>
  <line x1="36" y1="58" x2="1244" y2="58" stroke="{LINE}" stroke-width="1"/>
{inner}
</svg>''',
    )


def traces() -> None:
    rows = [
        ("fieldnotes", "Lab manual — chain, leftovers, what blue still sees."),
        ("loaders", "Staging and persist in C. Early Bird, COM, eBPF."),
        ("havoc-hiddendesktop", "HVNC operator kit for Havoc. CoffeeLdr, inject, rportfwd."),
        ("ctf-toolkit", "Scripts and write-ups from Hack The Box machines."),
    ]
    body = []
    for i, (name, desc) in enumerate(rows):
        y = 78 + i * 56
        body.append(
            f'''  <rect x="36" y="{y}" width="1208" height="48" fill="{PANEL}"/>
  <rect x="36" y="{y}" width="5" height="48" fill="{SPINE}"/>
  <text x="60" y="{y + 31}" fill="{BRICK}" font-family="{FONT}" font-size="15">{name}</text>
  <text x="340" y="{y + 31}" fill="{CREAM}" font-family="{SANS}" font-size="15">{desc}</text>'''
        )
    inner = "\n".join(body)
    write(
        "traces.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 310" width="1280" height="310">
  <rect width="1280" height="310" fill="{BG}"/>
  <rect x="0" y="0" width="10" height="310" fill="{SPINE}"/>
  <text x="36" y="42" fill="{MUTED}" font-family="{FONT}" font-size="12" letter-spacing="5">PUBLIC TRACES</text>
  <line x1="36" y1="58" x2="1244" y2="58" stroke="{LINE}" stroke-width="1"/>
{inner}
</svg>''',
    )


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    band("OPERATIONS", "band-ops.svg")
    band("LAB NOTES", "band-lab.svg")
    rule()
    spectrum()
    adjacent()
    traces()
    print("ok")
