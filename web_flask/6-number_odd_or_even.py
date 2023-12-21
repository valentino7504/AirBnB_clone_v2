#!/usr/bin/python3
'''
creates a flask app with four routes
'''
from flask import Flask, abort, render_template
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


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>")
def python_msg(text: str):
    """returns the python messages"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<n>", strict_slashes=False)
def number_msg(n):
    """prints the number message"""
    try:
        value = int(n)
    except ValueError:
        abort(404)
    else:
        return f"{value} is a number"


@app.route("/number_template/<n>", strict_slashes=False)
def number_tem(n):
    """renders the number template page"""
    try:
        int(n)
    except ValueError:
        abort(404)
    else:
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_even(n):
    """determines if a number is odd or even"""
    try:
        value = int(n)
    except ValueError:
        abort(404)
    else:
        status = "even" if value % 2 == 0 else "odd"
        return render_template("6-number_odd_or_even.html",
                               n=n, status=status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
