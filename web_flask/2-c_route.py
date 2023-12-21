#!/usr/bin/python3
'''
creates a flask app with three routes
'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns the hello message"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb_msg():
    """returns the 'hbnb'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_msg(text: str):
    """returns the c messages"""
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
