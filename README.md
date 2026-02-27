# Log2Summary

Log2Summary is a small backend-focused project built during a structured engineering training camp.

It reads a log file, extracts structured log levels (INFO, WARNING, ERROR), counts occurrences, safely 
skips malformed lines, and prints a summary.

The project is intentionally minimal and disciplined:
- No feature creep
- Clear separation of concerns
- Reusable core logic
- Multiple interfaces over the same backend



---

## Project Structure

log2summary/
  parser.py        # Core parsing + counting logic (the "brain")
  __main__.py      # CLI interface

web/
  app.py           # Thin Flask UI layer (imports backend logic)

sample_data/
tests/



---

## CLI Usage

Run via module:

python3 -m log2summary <log_file>

Example:

python3 -m log2summary sample_data/sample.log

If installed inside the virtual environment:

log2summary sample_data/sample.log



---

## Web UI (Thin Flask Layer)

This is a minimal single-page upload interface that reuses the existing backend logic.

From the project root:

source .venv/bin/activate
python web/app.py

Then open:

http://127.0.0.1:5000

Upload a log file (e.g. sample_data/sample.log) to see counts + skipped lines.



---

## Design Principle

Core logic lives in `parser.py`.

Interfaces (CLI, Web) are thin wrappers that call the same backend functions.

This keeps the system modular, testable, and reusable.
