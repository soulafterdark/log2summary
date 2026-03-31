# Log2Summary

Log2Summary is a small backend-focused project built as part of a structured backend 
engineering training workflow.

The application reads a log file, extracts structured log levels (INFO, WARNING, ERROR), 
counts occurrences, safely skips malformed lines, and produces a summary via CLI or Web 
interface.

This project emphasizes backend engineering practices rather than feature complexity.


---

## Features

- Log parsing for INFO / WARNING / ERROR
- Skips malformed log lines safely
- CLI interface
- Web upload interface (Flask)
- UTF-8 file validation
- Empty file handling
- Upload size limit
- Logging for web requests
- Service layer separating business logic
- Full automated test suite
- Clean Git workflow
- Package versioning


---

## Architecture

The project follows a layered backend architecture:

Interfaces
    CLI (__main__.py)
    Web (web/app.py)
        ↓
Service Layer
    service.py (summarize_lines)
        ↓
Core Logic
    parser.py (parse_levels, count_levels)

Both CLI and Web interfaces call the same service layer, which calls the parser.
This keeps the system modular, testable, and reusable.


---

## Project Structure

log2summary/
│
├── README.md
├── pyproject.toml
├── setup.py
│
├── log2summary/
│   ├── __init__.py
│   ├── __main__.py
│   ├── parser.py
│   ├── service.py
│   └── version.py
│
├── web/
│   ├── app.py
│   └── templates/
│
├── tests/
│
├── sample_data/
│
└── .venv/


---

## CLI Usage

Run via module:

python -m log2summary sample_data/sample.log

Example output:

ERROR: 1
INFO: 1
WARNING: 1
Skipped malformed lines: 0

JSON output option:

python -m log2summary sample_data/sample.log --json


---

## Web Interface

Start the web app:

source .venv/bin/activate
python web/app.py

Open in browser:

http://127.0.0.1:5000

Upload a log file to see summary results.


---

## Running Tests

python -m unittest

The test suite covers:
- Parser
- Service layer
- CLI
- Web upload
- File validation
- Upload limits


---

## Version

Current version: 0.1.0


---

## Purpose of This Project

This project is not meant to be a complex application.

It is meant to demonstrate backend engineering practices:
- Separation of concerns
- Testing before changes
- Refactoring safely
- Logging
- Versioning
- Packaging
- Clean Git workflow
- Release engineering discipline
