#!/usr/bin/python3
'''
this diplays a HTML page
'''
from flask import Flask, abort, render_template
from models.state import State
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """list cities belonging to a state"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def close_storage(var):
    """this reloads the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
