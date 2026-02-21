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


def count_levels(levels):
    counts = {}

    for level in levels:
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts
