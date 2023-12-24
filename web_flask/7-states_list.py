#!/usr/bin/python3
'''
this diplays a HTML page
'''
from flask import Flask, abort, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """lists the states available"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_storage(var):
    """this reloads the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
