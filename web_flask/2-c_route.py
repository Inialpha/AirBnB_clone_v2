#!/usr/bin/python3
""" module for running flask"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return ("Hello HBNB!")

@app.route('/hbnb')
def hbnb():
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace("_", " ")
    return ("C {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
