import argparse
import sys
from .parser import parse_levels, count_levels


def main():
    parser = argparse.ArgumentParser(
        prog="python3 -m log2summary",
        description="Summarize log levels (INFO, WARNING, ERROR) in a log file."
    )
    parser.add_argument(
        "log_file",
        help="Path to the log file to summarize"
    )

    args = parser.parse_args()
    log_file = args.log_file

    try:
        with open(log_file, "r") as f:
            lines = f.readlines()

        levels, skipped = parse_levels(lines)
        counts = count_levels(levels)

        print("Summary:")
        for level, count in counts.items():
            print(f"{level}: {count}")

        print(f"Skipped malformed lines: {skipped}")

    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)


if __name__ == "__main__":
    main()
