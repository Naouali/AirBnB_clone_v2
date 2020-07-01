#!/usr/bin/python3
"""
module to create a page/route
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_route():
    strict_slashes=False
    return 'Hello HBNB!'
