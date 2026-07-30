import os

from flask import Flask, render_template, request

from compiler.compile import compile_verilog

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    uploaded_file = request.files["verilog_file"]

    if uploaded_file.filename == "":
        return "No file selected."

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.filename
    )

    uploaded_file.save(file_path)

    result = compile_verilog(file_path)

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)