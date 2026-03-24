from .parser import parse_levels, count_levels


def summarize_lines(lines):
    levels, skipped = parse_levels(lines)
    counts = count_levels(levels)
    return counts, skipped
