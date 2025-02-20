#!/usr/bin/python3
"""module list all the states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """list all the cities by states in the database"""
    states = storage.all(State)
    return (render_template('8-cities_by_states.html', states=states))


@app.teardown_appcontext
def teardown(self):
    """close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
