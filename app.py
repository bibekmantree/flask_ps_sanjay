from flask import Flask, jsonify, request, Response
from libs import validate_book_obj

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


# POST /books

@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    flag = validate_book_obj(request_data)
    if flag:
        new_book = {
            "name": request_data["name"],
            "price": request_data["price"],
            "bid": request_data["bid"]
        }
        books.insert(0, new_book)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(new_book["bid"])
        return response
    else:
        response = Response("Invalid input", status=400, mimetype='application/json')
        return response


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
