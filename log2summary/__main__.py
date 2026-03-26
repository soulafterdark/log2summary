import argparse
import sys
import json
from .service import summarize_lines


def main():
    parser = argparse.ArgumentParser(
        prog="python3 -m log2summary",
        description="Summarize log levels (INFO, WARNING, ERROR) in a log file."
    )
    parser.add_argument(
        "log_file",
        help="Path to the log file to summarize"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Print summary as JSON"
    )

    args = parser.parse_args()
    log_file = args.log_file

    try:
        with open(log_file, "r") as f:
            lines = f.readlines()

        counts, skipped = summarize_lines(lines)

        if args.json_output:
            payload = {
                "INFO": counts.get("INFO", 0),
                "WARNING": counts.get("WARNING", 0),
                "ERROR": counts.get("ERROR", 0),
                "skipped": skipped,
            }
            print(json.dumps(payload))
        else:
            print("Summary:")
            for level in ["INFO", "WARNING", "ERROR"]:
                print(f"{level}: {counts.get(level, 0)}")

            print(f"Skipped malformed lines: {skipped}")

    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)


if __name__ == "__main__":
    main()
