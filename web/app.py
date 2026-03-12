from flask import Flask, request, render_template

from log2summary.parser import parse_levels, count_levels

app = Flask(__name__)


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

    levels, skipped = parse_levels(lines)
    counts = count_levels(levels)

    return render_template("results.html", counts=counts, skipped=skipped)


if __name__ == "__main__":
    app.run(debug=True)
