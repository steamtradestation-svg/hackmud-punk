import subprocess
import shlex
from typing import Callable
from rich.console import Console

console = Console()

class Sender:
    """Send commands/messages to the game window using tmux or xdotool."""

    def __init__(self, config: dict):
        self.config = config
        self.method = config.get("send_method", "tmux")
        self.tmux_cfg = config.get("tmux", {})
        self.xdotool_cfg = config.get("xdotool", {})

    def handle_line(self, line: str):
        # Basic line handler: this is where you'd add parsing and handler dispatch.
        console.log(f"Received line: {line}")
        # Example: respond to a trigger
        if "punk: hello" in line.lower():
            self.send("say punk responding")

    def send(self, text: str):
        if self.method == "tmux":
            return self._send_tmux(text)
        elif self.method == "xdotool":
            return self._send_xdotool(text)
        else:
            console.log(f"[yellow]dry-run[/] -> {text}")
            return True

    def _send_tmux(self, text: str):
        session = self.tmux_cfg.get("session", "")
        window = self.tmux_cfg.get("window", "")
        pane = self.tmux_cfg.get("pane", "")
        target = f"{session}:{window}.{pane}" if session else ""
        cmd = f"tmux send-keys -t {shlex.quote(target)} {shlex.quote(text)} Enter"
        console.log(f"tmux command: {cmd}")
        try:
            subprocess.run(cmd, shell=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            console.log(f"[red]tmux send failed[/]: {e}")
            return False

    def _send_xdotool(self, text: str):
        window_name = self.xdotool_cfg.get("window_name", "")
        if not window_name:
            console.log("[red]xdotool: no window_name configured")
            return False
        # Find window id then type
        try:
            # gets first matching window
            cmd_find = f"xdotool search --name {shlex.quote(window_name)} | head -n1"
            win = subprocess.check_output(cmd_find, shell=True).decode().strip()
            cmd_type = f"xdotool type --window {shlex.quote(win)} {shlex.quote(text)}; xdotool key --window {shlex.quote(win)} Return"
            subprocess.run(cmd_type, shell=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            console.log(f"[red]xdotool send failed[/]: {e}")
            return False
