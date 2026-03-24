import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from log2summary.__main__ import main


class TestCLI(unittest.TestCase):
    def test_main_prints_summary_for_valid_file(self):
        log_content = """2026-02-21 | INFO | Start
2026-02-21 | WARNING | Memory high
2026-02-21 | ERROR | Database failed
"""

        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            f.write(log_content)
            temp_path = f.name

        try:
            with patch("sys.argv", ["python -m log2summary", temp_path]):
                output = io.StringIO()
                with redirect_stdout(output):
                    main()

            text = output.getvalue()
            self.assertIn("Summary:", text)
            self.assertIn("INFO: 1", text)
            self.assertIn("WARNING: 1", text)
            self.assertIn("ERROR: 1", text)
            self.assertIn("Skipped malformed lines: 0", text)
        finally:
            os.remove(temp_path)


    def test_main_exits_for_missing_file(self):
        with patch("sys.argv", ["python -m log2summary", "does_not_exist.log"]):
            output = io.StringIO()
            with redirect_stdout(output):
                with self.assertRaises(SystemExit) as cm:
                    main()

        self.assertEqual(cm.exception.code, 1)
        self.assertIn("Error: File not found.", output.getvalue())




if __name__ == "__main__":
    unittest.main()
