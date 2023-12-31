#!/usr/bin/python3
'''
this diplays a HTML page
'''
from flask import Flask, abort, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def list_cities():
    """list cities belonging to a state"""
    states = [state_obj for state_obj in storage.all(State).values()]
    return render_template('8-cities_by_states.html',
                           states=states)

@app.teardown_appcontext
def close_storage(var):
    """this reloads the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
