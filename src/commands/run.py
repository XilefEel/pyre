import subprocess
from pathlib import Path

from rich.console import Console

console = Console()


def run_project() -> None:
    run_py = Path.cwd() / "run.py"
    main_py = Path.cwd() / "src" / "main.py"

    if run_py.exists():
        console.print("  [green]✓[/green] Running [#ff8c00]run.py[/#ff8c00]\n")
        subprocess.run(["uv", "run", "python", "run.py"])

    elif main_py.exists():
        console.print("  [green]✓[/green] Running [#ff8c00]src/main.py[/#ff8c00]\n")
        subprocess.run(["uv", "run", "python", "src/main.py"])

    else:
        console.print(
            "  [red]✗[/red] No run.py or src/main.py found. Are you inside a pyre project?"
        )
