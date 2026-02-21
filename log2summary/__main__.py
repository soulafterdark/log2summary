import sys
from .parser import parse_levels, count_levels


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 -m log2summary <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

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
