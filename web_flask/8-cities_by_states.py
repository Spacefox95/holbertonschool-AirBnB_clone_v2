#!/usr/bin/python3

from flask import Flask, render_template, appcontext_tearing_down
from models import storage
from models.state import State
from models.city import City

"""
Starts Falsk web app and display message
"""

app = Flask(__name__)


@app.route("/cities_by_states/", defaults={'n': 'States'}, strict_slashes=False)
@app.route("/cities_by_states/<string:n>", strict_slashes=False)
def html_page_display(n):
    """
    Display a HTML page only if n is a string
    """
    states = storage.all(State).values()
    city = storage.all(City).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', n=n, states=sorted_states, city=city)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
