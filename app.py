from flask import Flask, request, jsonify, render_template
from sql import BookReg

app = Flask(__name__, template_folder='./pages')

@app.route("/")
def home_page():
    return render_template("homepage.html")

@app.route("/get-reg", methods=["POST"])
def get_reg():
    book_reg = BookReg()
    user = request.form.get("new_user")
    books = book_reg.get_books(user)
    return jsonify({"user": user, "books": books}), 200

@app.route("/add-book", methods=["POST"])
def add_book():
    book_reg = BookReg()
    user = request.form.get("old_user")
    book = request.form.get("book")
    due = request.form.get("due")
    data = {
        "user": user,
        "book": book,
        "due": due
    }
    book_reg.add_book(user, book, due)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)