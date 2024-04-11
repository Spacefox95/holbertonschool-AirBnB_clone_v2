#!/usr/bin/python3
"""
Starts Falsk web app and display message
"""

from flask import Flask


app = Flask(__name__)


""" Specify the route"""


@app.route("/", strict_slashes=False)
def hello():
    """ Display Hello HBNB """
    return "Hello HBNB"


""" Specify the port """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
