import unittest
from log2summary.service import summarize_lines


class TestService(unittest.TestCase):
    def test_summarize_lines_counts_and_skipped(self):
        lines = [
            "2026-02-21 | INFO | Start",
            "bad line",
            "2026-02-21 | ERROR | Crash"
        ]

        counts, skipped = summarize_lines(lines)

        self.assertEqual(counts["INFO"], 1)
        self.assertEqual(counts["ERROR"], 1)
        self.assertEqual(skipped, 1)


if __name__ == "__main__":
    unittest.main()
