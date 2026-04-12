import subprocess
from pathlib import Path

from rich.console import Console

console = Console()


def check_project() -> None:
    if not Path.cwd().joinpath("pyproject.toml").exists():
        console.print(
            "  [red]✗[/red] No pyproject.toml found. Are you inside a pyre project?"
        )
        return

    console.print("  [green]✓[/green] Running [cyan]mypy[/cyan]")
    subprocess.run(["uv", "run", "--extra", "dev", "mypy", "src"])

    console.print("  [green]✓[/green] Running [cyan]ruff[/cyan]")
    subprocess.run(["uv", "run", "--extra", "dev", "ruff", "check", "src"])
