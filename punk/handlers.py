from typing import Dict, Any
from rich.console import Console

console = Console()

class BaseHandler:
    def __init__(self, cfg: Dict[str, Any]):
        self.cfg = cfg

    def match(self, line: str) -> bool:
        return False

    def act(self, line: str):
        console.log(f"BaseHandler received: {line}")
