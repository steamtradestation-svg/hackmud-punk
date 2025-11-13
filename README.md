# hackmud-punk

A repository for a collection of hackmud user scripts and a supporting Python terminal application called "punk".

Purpose
- source/: hackmud user scripts you can upload to the game.
- punk/: a Python terminal app that monitors the game's log file, acts on output (via pluggable handlers, optionally AI-assisted), and sends messages/commands to the game window on Ubuntu (using tmux or xdotool).

Quickstart
1. Clone the repo:
   git clone https://github.com/steamtradestation-svg/hackmud-punk.git
2. Create and activate a virtual environment (recommended):
   python3 -m venv .venv && source .venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Copy the example config and edit paths:
   cp config.yaml.example config.yaml
   # edit config.yaml to point log_path and send_method
5. Run the punk app in a terminal:
   python -m punk.cli --config config.yaml

Layout
- source/: hackmud user scripts and examples
- punk/: Python package with CLI, monitor, and sender modules
- config.yaml.example: example configuration
- requirements.txt: Python dependencies

Notes
- The punk app is a starting point and contains stubs for AI/tool integrations. It attempts tmux first, then xdotool, to send keys to the game window.
