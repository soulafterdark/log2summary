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


    def test_count_levels_handles_multiple_of_same_level(self):
        levels = ["INFO", "INFO", "WARNING", "ERROR", "INFO"]

        counts = count_levels(levels)

        self.assertEqual(counts["INFO"], 3)
        self.assertEqual(counts["WARNING"], 1)
        self.assertEqual(counts["ERROR"], 1)


    def test_parse_levels_all_malformed_lines(self):
        lines = [
            "Bad line\n",
            "Another wrong format\n",
            "Still not valid\n"
        ]

        levels, skipped = parse_levels(lines)
        counts = count_levels(levels)

        self.assertEqual(levels, [])
        self.assertEqual(counts, {})
        self.assertEqual(skipped, 3)


    def test_parse_levels_skips_unknown_levels(self):
        lines = [
            "2024-01-01 | INFO | System started\n",
            "2024-01-01 | DEBUG | Extra detail\n",
            "2024-01-01 | ERROR | Something broke\n",
        ]

        levels, skipped = parse_levels(lines)
        counts = count_levels(levels)

        self.assertEqual(counts["INFO"], 1)
        self.assertEqual(counts["ERROR"], 1)
        self.assertNotIn("DEBUG", counts)
        self.assertEqual(skipped, 1)


if __name__ == "__main__":
    unittest.main()
