#!/usr/bin/python3
"""module list all the states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_city(id=None):
    """list all the states or cities by states in the database"""
    states = storage.all(State)
    if id:
        for state in states.values():
            if state.id == id:
                return (render_template('9-states.html', state=state, mode=1))
        return (render_template('9-states.html', states=None, mode=0))
    states = storage.all(State)
    return (render_template('9-states.html', states=states, mode=2))

    return (render_template('8-cities_by_states.html', states=states))


@app.teardown_appcontext
def teardown(self):
    """close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
