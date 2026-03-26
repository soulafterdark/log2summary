from flask import Flask, request, render_template

from log2summary.service import summarize_lines

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024  # 1 MB upload limit


@app.errorhandler(413)
def too_large(e):
    return "Uploaded file is too large.", 413


@app.get("/")
def index():
    return render_template("upload.html")


@app.post("/upload")
def upload():
    f = request.files.get("logfile")
    if not f:
        return "Missing file field 'logfile'", 400

    try:
        text = f.stream.read().decode("utf-8")
    except UnicodeDecodeError:
        return "Uploaded file must be UTF-8 text.", 400

    lines = text.splitlines()

    if not lines:
        return "Uploaded file is empty.", 400

    counts, skipped = summarize_lines(lines)

    return render_template("results.html", counts=counts, skipped=skipped)


if __name__ == "__main__":
    app.run(debug=True)
