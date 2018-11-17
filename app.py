from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_root():
    return "Hello Root"


app.run(port=5000)
