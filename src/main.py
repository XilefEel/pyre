import typer

from src.commands.add import add_package
from src.commands.check import check_project
from src.commands.new import create_project
from src.commands.run import run_project

app = typer.Typer(
    name="pyre",
    help="The missing scaffolder for modern Python. Set your projects ablaze.",
    add_completion=False,
    rich_markup_mode=None,
)


@app.command()
def new(name: str = typer.Argument(..., help="Project name")):
    """Scaffold a new Pyre project."""
    create_project(name)


@app.command()
def run():
    """Run the project."""
    run_project()


@app.command()
def check():
    """Run mypy and ruff."""
    check_project()


@app.command()
def add(package: str = typer.Argument(..., help="Package to add")):
    """Add a dependency."""
    add_package(package)


def main():
    app()


if __name__ == "__main__":
    main()
