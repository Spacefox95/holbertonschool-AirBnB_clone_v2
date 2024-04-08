#!/usr/bin/python3

from flask import Flask

"""
Starts Falsk web app and display message
"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "<p>Hello HBNB</p>"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)
