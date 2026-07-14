# Reconductor-
# Reconductor

Offensive reconnaissance toolkit — a Python wrapper around `nmap` that automates the scan profiles I actually use during OSCP labs and CTFs, instead of retyping the same long commands every time.

> **Requires:** [nmap](https://nmap.org/) installed and available on your `PATH`. This tool does not include nmap — it calls the `nmap` binary on your system.

## Why

Recon is the first thing you do on every box, and it's almost always the same handful of nmap commands. Reconductor asks for a target once, then lets you pick a scan profile so you're not re-typing flags every time.

## Features

- Interactive CLI with a scan profile menu
- **[1] Full TCP scan** — all 65535 ports, fast (`-T4 --min-rate=5000 --max-retries=1`)
- **[2] Detailed scan** — version + default script scan (`-sC -sV`) on ports you choose
- **[3] Full UDP scan** — top 1000 UDP ports, tuned for speed (`--min-rate 1300 --max-retries 1`)
- Saves output automatically (`-oN` / `-oA`) so results are ready for reporting

## Installation

```bash
git clone https://github.com/<your-username>/Reconductor.git
cd Reconductor
pip install -r requirements.txt
```

## Usage

```bash
python reconductor.py <target-ip>
```

Example:

```bash
python reconductor.py 10.10.10.5
```

You'll be prompted to choose a scan profile:

```
[1] Full TCP scan (All Ports)
[2] Detailed scan on specific ports (Version + default scripts)
[3] Full 1000 UDP ports scan
```

For profile 2, you'll also be asked which ports to target (e.g. `80,443,22`).

## Disclaimer
For use only against systems you own or are explicitly authorized to test (labs, CTFs, engagements with permission). You are responsible for how you use this tool.

## License

MIT — see [LICENSE](LICENSE).
