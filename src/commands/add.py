import subprocess
from pathlib import Path

from rich.console import Console

console = Console()


def add_package(package: str) -> None:
    if not Path.cwd().joinpath("pyproject.toml").exists():
        console.print(
            "  [red]✗[/red] No pyproject.toml found. Are you inside a pyre project?"
        )
        return

    console.print(f"  [green]✓[/green] Adding [cyan]{package}[/cyan]")
    subprocess.run(["uv", "add", package], check=True)
