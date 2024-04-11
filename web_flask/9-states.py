#!/usr/bin/python3
"""
Starts Falsk web app and display message
"""

from flask import Flask, render_template, appcontext_tearing_down
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", defaults={'n': 'States'}, strict_slashes=False)
@app.route("/cities_by_states/<string:n>", strict_slashes=False)
def html_page_display(n):
    """
    Display a HTML page only if n is a string
    """
    states = storage.all(State).values()
    sortd_states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', n=n, states=sortd_states)


@app.route('/states/<id>')
def html_display_titles(id):
    """ Display HTML page customized id
    """
    state_obj = None
    for state_name in storage.all(State).values():
        if state_name.id == id:
            state_obj = state_name
    return render_template('9-states.html', state_obj=state_obj)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
