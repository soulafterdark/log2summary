import io
import unittest

from web.app import app


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_upload_missing_file_returns_400(self):
        response = self.client.post("/upload", data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Missing file field 'logfile'", response.data)

    def test_upload_empty_file_returns_400(self):
        response = self.client.post(
            "/upload",
            data={"logfile": (io.BytesIO(b""), "empty.log")},
            content_type="multipart/form-data",
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Uploaded file is empty.", response.data)

    def test_upload_valid_file_returns_summary(self):
        log_content = b"""2026-02-21 | INFO | Start
2026-02-21 | WARNING | Memory high
2026-02-21 | ERROR | Database failed
"""

        response = self.client.post(
            "/upload",
            data={"logfile": (io.BytesIO(log_content), "test.log")},
            content_type="multipart/form-data",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"INFO", response.data)
        self.assertIn(b"WARNING", response.data)
        self.assertIn(b"ERROR", response.data)


    def test_upload_non_utf8_file_returns_400(self):
        response = self.client.post(
            "/upload",
            data={"logfile": (io.BytesIO(b"\xff\xfe\xfd"), "bad.log")},
            content_type="multipart/form-data",
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Uploaded file must be UTF-8 text.", response.data)



    def test_upload_shows_skipped_line_count(self):
        log_content = b"""2026-02-21 | INFO | Start
bad line here
2026-02-21 | ERROR | Database failed
"""

        response = self.client.post(
            "/upload",
            data={"logfile": (io.BytesIO(log_content), "mixed.log")},
            content_type="multipart/form-data",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Skipped lines: 1", response.data)



if __name__ == "__main__":
    unittest.main()   



