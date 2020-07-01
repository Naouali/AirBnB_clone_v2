#!/usr/bin/python3
"""
module to create a page/route
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_route():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
