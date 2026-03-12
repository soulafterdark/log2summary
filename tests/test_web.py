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


if __name__ == "__main__":
    unittest.main()
