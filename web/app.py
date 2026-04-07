import logging
from flask import Flask, jsonify, request, render_template

from log2summary.service import summarize_lines

app = Flask(__name__)
logger = logging.getLogger(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024  # 1 MB upload limit


def configure_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            "level=%(levelname)s logger=%(name)s message=%(message)s"
        )
    )

    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(handler)

    logger.propagate = False


configure_logging()


@app.errorhandler(413)
def too_large(e):
    logger.warning("Upload rejected: file too large")
    return "Uploaded file is too large.", 413


@app.get("/")
def index():
    logger.info("Index page requested")
    return render_template("upload.html")


@app.get("/health")
def health():
    logger.info("Health check requested")
    return jsonify({"status": "ok"}), 200


@app.post("/api/summary")
def api_summary():
    f = request.files.get("logfile")
    if not f:
        logger.warning("API summary failed: missing file field")
        return jsonify({"error": "Missing file field 'logfile'"}), 400

    try:
        text = f.stream.read().decode("utf-8")
    except UnicodeDecodeError:
        logger.warning("API summary failed: non UTF-8 file")
        return jsonify({"error": "Uploaded file must be UTF-8 text."}), 400

    lines = text.splitlines()

    if not lines:
        logger.warning("API summary failed: empty file")
        return jsonify({"error": "Uploaded file is empty."}), 400

    counts, skipped = summarize_lines(lines)

    logger.info(
        "API summary processed successfully: INFO=%s WARNING=%s ERROR=%s skipped=%s",
        counts.get("INFO", 0),
        counts.get("WARNING", 0),
        counts.get("ERROR", 0),
        skipped,
    )

    return jsonify({"counts": counts, "skipped": skipped}), 200


@app.post("/upload")
def upload():
    f = request.files.get("logfile")
    if not f:
        logger.warning("Upload failed: missing file field")
        return "Missing file field 'logfile'", 400

    try:
        text = f.stream.read().decode("utf-8")
    except UnicodeDecodeError:
        logger.warning("Upload failed: non UTF-8 file")
        return "Uploaded file must be UTF-8 text.", 400

    lines = text.splitlines()

    if not lines:
        logger.warning("Upload failed: empty file")
        return "Uploaded file is empty.", 400

    counts, skipped = summarize_lines(lines)

    logger.info(
        "Upload processed successfully: INFO=%s WARNING=%s ERROR=%s skipped=%s",
        counts.get("INFO", 0),
        counts.get("WARNING", 0),
        counts.get("ERROR", 0),
        skipped,
    )

    return render_template("results.html", counts=counts, skipped=skipped)


if __name__ == "__main__":
    app.run(debug=True)
