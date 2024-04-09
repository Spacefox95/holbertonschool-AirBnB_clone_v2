#!/usr/bin/python3

from flask import Flask, render_template, appcontext_tearing_down
from models import storage
from models.state import State

"""
Starts Falsk web app and display message
"""

app = Flask(__name__)


@app.route("/states_list/", defaults={'n': 'States'}, strict_slashes=False)
@app.route("/states_list/<string:n>", strict_slashes=False)
def html_display_odd_even(n):
    """
    Display a HTML page only if n is an integer
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', n=n, states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
