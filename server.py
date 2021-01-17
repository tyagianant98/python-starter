
from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    return f"Hello World"


@app.route("/ping")
def ping():
    return f"pong"


@app.route("/anant")
def tyagi():
    return f"tyagi"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5003"), debug=True)
