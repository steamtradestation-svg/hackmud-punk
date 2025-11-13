import time
from typing import Callable, Optional
from pathlib import Path
from rich.console import Console

console = Console()

class LogMonitor:
    """Simple tail-like monitor. Can be swapped for watchdog-based implementation."""

    def __init__(self, config: dict):
        self.log_path = Path(config.get("log_path", "log.txt"))
        self.poll_interval = config.get("poll_interval", 0.5)

    def _tail(self, on_line: Callable[[str], None]):
        # wait for file
        while not self.log_path.exists():
            console.log(f"Waiting for log file at {self.log_path}")
            time.sleep(1)
        with self.log_path.open("r", errors="ignore") as fh:
            # go to the end
            fh.seek(0, 2)
            while True:
                line = fh.readline()
                if not line:
                    time.sleep(self.poll_interval)
                    continue
                on_line(line.rstrip("\n"))

    def run(self, on_line: Optional[Callable[[str], None]] = None):
        if on_line is None:
            on_line = lambda l: console.log(f"LINE: {l}")
        console.log("Starting LogMonitor")
        self._tail(on_line)
