#!/usr/bin/python3
"""
Starts Falsk web app and display message
"""

from flask import Flask


app = Flask(__name__)


@app.route("/c/<string:text>", strict_slashes=False)
def hello(text: str):
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
