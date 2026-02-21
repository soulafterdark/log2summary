import unittest
from log2summary.parser import parse_levels, count_levels


class TestParser(unittest.TestCase):

    def test_parse_levels_counts_correctly(self):
        lines = [
            "2024-01-01 | INFO | System started\n",
            "2024-01-01 | ERROR | Something broke\n",
            "Malformed line\n"
        ]

        levels, skipped = parse_levels(lines)
        counts = count_levels(levels)

        self.assertEqual(counts["INFO"], 1)
        self.assertEqual(counts["ERROR"], 1)
        self.assertEqual(skipped, 1)


if __name__ == "__main__":
    unittest.main()
