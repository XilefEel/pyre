import shutil
import subprocess
import time
from pathlib import Path

import questionary
import typer
from questionary import Style
from rich.console import Console

console = Console()

TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"
TEMPLATES = ["default", "minimal", "fastapi", "numpy", "pytorch", "scraper"]

pyre_style = Style(
    [
        ("qmark", "fg:#ff4500 bold"),
        ("question", "bold"),
        ("answer", "fg:#ff8c00 bold"),
        ("pointer", "fg:#ff4500 bold"),
        ("highlighted", "fg:#ff8c00 bold"),
        ("selected", "fg:#ff8c00"),
        ("instruction", "fg:#666666"),
    ]
)


def select_template() -> str:
    template = questionary.select(
        "Select a template:",
        choices=TEMPLATES,
        style=pyre_style,
        qmark="🔥",
    ).ask()

    return template


def create_project(name: str) -> None:

    project_path = Path.cwd() / name

    template_name = select_template()

    if template_name is None:
        raise typer.Exit(0)

    start = time.time()

    template_path = TEMPLATES_DIR / template_name

    if project_path.exists():
        console.print(f"  [red]✗[/red] Directory '{name}' already exists")
        raise typer.Exit(1)

    shutil.copytree(
        template_path,
        project_path,
        dirs_exist_ok=False,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )

    console.print(f"  [green]✓[/green] Created project [#ff8c00]{name}[/#ff8c00]")

    for file in project_path.rglob("*.py"):
        content = file.read_text(encoding="utf-8")
        content = content.replace("{project_name}", name)
        file.write_text(content, encoding="utf-8")

    for file in project_path.rglob("*.toml"):
        content = file.read_text(encoding="utf-8")
        content = content.replace("{project_name}", name)
        file.write_text(content, encoding="utf-8")

    console.print(
        f"  [green]✓[/green] Scaffolded [#ff8c00]{template_name}[/#ff8c00] template"
    )

    subprocess.run(["git", "init", str(project_path)], capture_output=True)
    console.print("  [green]✓[/green] Initialized git repository")

    elapsed = time.time() - start
    console.print(
        f"\n  [bold]Done[/bold] in [bold #ff4500]{elapsed:.1f}s[/bold #ff4500]\n"
    )

    console.print("  [dim]Get started:[/dim]")
    console.print(f"    [#ff8c00]cd {name}[/#ff8c00]")
    console.print("    [#ff8c00]uv sync[/#ff8c00]")
    console.print("    [#ff8c00]uv run python src/main.py[/#ff8c00]")
