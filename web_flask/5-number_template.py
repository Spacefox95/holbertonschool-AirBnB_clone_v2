#!/usr/bin/python3

from flask import Flask, render_template

"""
Starts Falsk web app and display message
"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text: str):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_text(text: str):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_display(n: int):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_display(n: int):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
