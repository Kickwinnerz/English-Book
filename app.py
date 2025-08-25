from flask import Flask, render_template, send_from_directory, safe_join, abort
import os

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

# Homepage
@app.route("/")
def index():
    return render_template("index.html")

# Optional explicit PDF route (Flask already serves /static/... but this gives safe access)
@app.route("/pdfs/<path:filename>")
def serve_pdf(filename):
    pdf_dir = os.path.join(app.root_path, "static", "pdfs")
    safe_path = safe_join(pdf_dir, filename)
    if not os.path.isfile(safe_path):
        abort(404)
    return send_from_directory(pdf_dir, filename)

# Required by Vercel to find the app variable
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))