#!/usr/bin/python3
"""module list all the states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """list all the states or cities by states in the database"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return (render_template('10-hbnb_filters.html', states=states, amenities=amenities))


@app.teardown_appcontext
def teardown(self):
    """close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
