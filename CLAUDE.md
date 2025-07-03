# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based bike ride weather recommendation system that uses the OpenWeatherMap API to help users decide when to go for a bike ride based on weather conditions.

## Development Commands

**Running Code:**
```bash
uv run python src/main.py  # Run main application
uv run pytest             # Run all tests
uv run pytest tests/test_main.py::test_get_lat_lon  # Run specific test
```

**Code Quality:**
```bash
uv run ruff check          # Lint code
uv run ruff check --fix    # Auto-fix linting issues
uv run ruff format         # Format code
```

## Environment Setup

Requires `.env` file with:
```
API_KEY=your_openweathermap_api_key
```