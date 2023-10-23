from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)

notebook_entry = ("sqlite///notebook.db")

@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("notebook.html")

@app.route("/notebook")
def write_note():
    note = request.form.get("notes")
    notebook_entry.execute("INSERT INTO notes (notes) VALUES(?)", note)

if __name__ == "__main__":
    app.run(debug=True)