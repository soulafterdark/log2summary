import sys

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 -m log2summary <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    try:
        with open(log_file, "r") as f:
            lines = f.readlines()

        levels = []

        for line in lines:
            parts = line.strip().split("|")
            if len(parts) >= 2:
                level = parts[1].strip()
                levels.append(level)

        counts = {}

        for level in levels:
            if level in counts:
                counts[level] += 1
            else:
                counts[level] = 1

        print("Summary:")
        for level, count in counts.items():
            print(f"{level}: {count}")

    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
