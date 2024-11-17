# Run the formatter
format: 
    uv run ruff check . --fix
    uv run ruff check --select I --fix
    uv run mamushi ./contracts