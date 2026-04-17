# 🔥 pyre

The missing scaffolder for modern Python. Set your projects ablaze.

## What is it?

Pyre is a `cargo`-style scaffolding tool for Python 3.14+. One command gives you a fully typed, structured, and ready-to-code project, with git initialized and dependencies installed. Choose from templates for web APIs, data science, ML, and more.

It's the all-in-one tool to ignite your Python development workflow.

## Philosophy

Python is a powerful language, but out of the box, it encourages loose patterns. Pyre is an answer to that. It brings the discipline of **Rust** and the structure of **TypeScript** into Python, without sacrificing Python's simplicity.

Every project starts with a solid foundation: a clear directory structure, type annotations, strict type checking and linting with `mypy` and `ruff`, and a curated import stack: `dataclasses`, `result`, `enum`, `abc`, `functools`, `pydantic`, `pathlib`, and the full `typing` module.

Pyre isn't a new language. It's a new default.

## Requirements

- Python 3.14+
- uv

## Installation

```bash
git clone https://github.com/XilefEel/pyre.git
cd pyre
uv tool install . --editable
```

## Usage

```bash
pyre new my_project     # scaffold a new project
cd my_project
pyre install            # install dependencies
pyre run                # run the project
pyre check              # run mypy + ruff
pyre add httpx          # add a dependency
pyre --help             # show help message
```

## Templates

When creating a new project, you can choose from the following templates:

| Template  | Description                  | Stack                      |
| --------- | ---------------------------- | -------------------------- |
| `default` | Simple, structured Python    | result, pydantic           |
| `minimal` | Bare entrypoint, no opinions | none                       |
| `fastapi` | REST API with SQLite         | fastapi, sqlmodel, uvicorn |
| `scraper` | Web scraping                 | httpx, beautifulsoup4      |
| `numpy`   | Data processing              | numpy, pandas              |
| `pytorch` | ML training loop             | torch                      |
