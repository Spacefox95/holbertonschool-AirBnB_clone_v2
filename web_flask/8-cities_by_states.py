#!/usr/bin/python3
"""
Starts Falsk web app and display message
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states/", strict_slashes=False)
def html_cities_in_state():
    """
    Display an HTML page listing all cities in a state
    """
    city = storage.all(State).values()
    sorted_cities = sorted(city, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_cities)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
