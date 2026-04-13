import subprocess
from pathlib import Path

from rich.console import Console

console = Console()


def install_packages() -> None:
    if not Path.cwd().joinpath("pyproject.toml").exists():
        console.print(
            "  [red]✗[/red] No pyproject.toml found. Are you inside a pyre project?"
        )
        return

    subprocess.run(["uv", "sync"])
