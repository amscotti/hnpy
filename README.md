# hnpy

hnpy is a lightweight Python CLI tool for fetching and displaying top stories from [Hacker News](https://news.ycombinator.com/) using the [Hacker News API from Firebase](https://github.com/HackerNews/API). It uses asynchronous HTTP requests for efficiency, Rich for colorful output, and supports limiting stories and hiding URLs.

## Features
- Asynchronous fetching of top story IDs and details using httpx.
- Customizable output: Limit number of stories (default: 30), optional URL hiding.
- Modular code structure with type hints and mypy support.
- Dependency management via uv and environment setup with mise.

## Requirements
- Python 3.12+
- mise (for managing Python versions and tools)
- uv (for fast dependency installation)

## Installation
1. Install mise: `curl https://mise.run | sh` (or `brew install mise` on macOS).
2. Navigate to the project directory and run `mise install` to set up [uv](https://docs.astral.sh/uv/).
3. Sync dependencies: `uv sync` (installs aiohttp, httpx, rich, etc., from pyproject.toml).

## Usage
Run the app with uv: `uv run python main.py [options]`

- Default (top 30 stories): `uv run python main.py`
- Limit to 10 stories: `uv run python main.py --limit 10`
- Hide URLs: `uv run python main.py --hide-url`
- Combined: `uv run python main.py --limit 5 --hide-url`

For Docker: Build with `docker build -t hnpy .` and run `docker run hnpy`.

## Development
- Run all lint tasks: `mise run lint`
- Lint: `mise run lint:check`
- Type check: `mise run lint:type`
- Update deps: `mise run uv:sync`