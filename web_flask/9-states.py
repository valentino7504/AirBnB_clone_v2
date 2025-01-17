#!/usr/bin/python3
'''
this diplays a HTML page
'''
from flask import Flask, abort, render_template
from models.state import State
from models import storage
from os import getenv

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states():
    """lists the states available"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>')
def state_by_id(id):
    """
    displays a html page with the state according to id
    """
    state = None
    for state_obj in storage.all(State).values():
        if state_obj.id == id:
            state = state_obj
    return render_template('9-states.html',
                           state=state)


@app.teardown_appcontext
def close_storage(var):
    """this reloads the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
