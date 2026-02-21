def parse_levels(lines):
    levels = []
    skipped = 0

    for line in lines:
        parts = line.strip().split("|")
        if len(parts) >= 2:
            level = parts[1].strip()
            levels.append(level)
        else:
            skipped += 1

    return levels, skipped
