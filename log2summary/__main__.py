import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 -m log2summary <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    try:
        with open(log_file, "r") as f:
            lines = f.readlines()
        print(f"Successfully read {len(lines)} lines.")
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
