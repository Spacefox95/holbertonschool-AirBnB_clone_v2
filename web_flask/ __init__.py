#!/usr/bin/python3
from flask import Flask
"""
Flask listening port for web application
"""

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
