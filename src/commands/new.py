import shutil
import subprocess
from pathlib import Path

import typer
from rich.console import Console

console = Console()

TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"


def create_project(name: str) -> None:
    project_path = Path.cwd() / name
    template_path = TEMPLATES_DIR / "default"

    if project_path.exists():
        console.print(f"  [red]✗[/red] Directory '{name}' already exists")
        raise typer.Exit(1)

    shutil.copytree(
        template_path,
        project_path,
        dirs_exist_ok=False,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )

    console.print(f"  [green]✓[/green] Created project [cyan]{name}[/cyan]")

    for file in project_path.rglob("*.py"):
        content = file.read_text(encoding="utf-8")
        content = content.replace("{project_name}", name)
        file.write_text(content, encoding="utf-8")

    for file in project_path.rglob("*.toml"):
        content = file.read_text(encoding="utf-8")
        content = content.replace("{project_name}", name)
        file.write_text(content, encoding="utf-8")

    console.print("  [green]✓[/green] Scaffolded default template")

    subprocess.run(["git", "init", str(project_path)], capture_output=True)
    console.print("  [green]✓[/green] Initialized git repository")

    console.print("\n  Done!\n")
    console.print("  Get started:")
    console.print(f"     [cyan]cd {name}[/cyan]")
    console.print("     [cyan]uv sync[/cyan]")
    console.print("     [cyan]uv run python src/main.py[/cyan]")
