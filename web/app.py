# web/app.py
from flask import Flask, request, render_template_string

from log2summary.parser import parse_levels, count_levels

app = Flask(__name__)


UPLOAD_FORM_HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Log2Summary Web</title>
  </head>
  <body>
    <h1>Log2Summary</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
      <label>
        Upload a log file:
        <input type="file" name="logfile" required />
      </label>
      <button type="submit">Summarize</button>
    </form>
  </body>
</html>
"""

RESULTS_HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Log2Summary Results</title>
  </head>
  <body>
    <h1>Summary</h1>

    <ul>
      <li>INFO: {{ counts.get("INFO", 0) }}</li>
      <li>WARNING: {{ counts.get("WARNING", 0) }}</li>
      <li>ERROR: {{ counts.get("ERROR", 0) }}</li>
    </ul>

    <p>Skipped lines: {{ skipped }}</p>

    <p><a href="/">Upload another file</a></p>
  </body>
</html>
"""


@app.get("/")
def index():
    return render_template_string(UPLOAD_FORM_HTML)


@app.post("/upload")
def upload():
    f = request.files.get("logfile")
    if not f:
        return "Missing file field 'logfile'", 400

    # Read as text safely; replace undecodable bytes.
    text = f.stream.read().decode("utf-8", errors="replace")
    lines = text.splitlines()

    levels, skipped = parse_levels(lines)
    counts = count_levels(levels)

    return render_template_string(RESULTS_HTML, counts=counts, skipped=skipped)


if __name__ == "__main__":
    app.run(debug=True)
