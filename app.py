from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        "name": "MIL",
        "price": 30,
        "bid": 1
    },
    {
        "name": "SSG",
        "price": 40,
        "bid": 8

    }
]


@app.route('/')
def hello_root():
    return "Hello Root"


# GET /books
@app.route('/books')
def get_books():
    return jsonify({"books": books})


# GET /books/id
@app.route('/books/<int:bid>')
def get_book_byid(bid):
    return_book = {}
    for book in books:
        if book['bid'] == bid:
            return_book["name"] = book["name"]
            return_book["price"] = book["price"]
    return jsonify(return_book)


app.run(port=5000)
