import click
import yaml
from .monitor import LogMonitor
from .sender import Sender
from rich.console import Console

console = Console()

@click.command()
@click.option("--config", "-c", default="config.yaml", help="Path to config YAML.")
def main(config):
    console.print(f"[bold cyan]punk[/] starting with config: {config}")
    with open(config, "r") as f:
        cfg = yaml.safe_load(f)
    monitor = LogMonitor(cfg)
    sender = Sender(cfg)
    try:
        monitor.run(on_line=sender.handle_line)
    except KeyboardInterrupt:
        console.print("Shutting down punk")

if __name__ == "__main__":
    main()
