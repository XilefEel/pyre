import subprocess
from pathlib import Path

from rich.console import Console

console = Console()


def run_project() -> None:
    main_path = Path.cwd() / "src" / "main.py"

    if not main_path.exists():
        console.print(
            "  [red]✗[/red] No src/main.py found. Are you inside a pyre project?"
        )
        return

    console.print("  [green]✓[/green] Running [cyan]src/main.py[/cyan]\n")
    subprocess.run(["uv", "run", "python", "src/main.py"])
