#!/usr/bin/python3
"""
Starts Falsk web app and display message
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>")
def html_cities_by_state(id=None):
    """
    Display an HTML page listing all cities by state
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    if id:
        for state_name in sorted_states:
            if state_name.id == id:
                return render_template('9-states.html', item=state_name)
        return render_template('9-states.html', error="Not Found!")
    else:
        return render_template('9-states.html', new_state=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
