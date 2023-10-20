#!/usr/bin/python3
""" module for running flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """return Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """return HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """retrn response for c routes"""
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """response to python route"""
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
