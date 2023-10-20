#!/usr/bin/python3
""" module for running flask"""
from flask import Flask, render_template

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

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """check if n is a number and return <n> is a number"""
    if isinstance(n, int):
        return ("{} is a number".format(n))
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render template with number"""
    if isinstance(n, int):
        return (render_template('5-number.html', n=n))

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """check if an number is odd or even and displays the appropriate massage"""
    if isinstance(n, int):
        return (render_template('6-number_odd_or_even.html', n=n))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
