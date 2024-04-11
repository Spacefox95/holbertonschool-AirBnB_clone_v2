#!/usr/bin/python3
"""
Starts Falsk web app and display message
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def new_state():
    states = storage.all(State).values()
    return render_template('9-states.html', state=states)


@app.route("/states/<id>", strict_slashes=False)
def html_cities_by_state(id):
    """
    Display an HTML page listing all cities by state
    """
    for state_name in storage.all(State).values():
        if state_name.id == id:
            return render_template('9-states.html', item=state_name)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    """
    blabla
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
