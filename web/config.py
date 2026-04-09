import os

DEFAULT_MAX_UPLOAD_MB = 1


def get_max_content_length():
    max_upload_mb = int(os.getenv("LOG2SUMMARY_MAX_UPLOAD_MB", str(DEFAULT_MAX_UPLOAD_MB)))
    return max_upload_mb * 1024 * 1024
