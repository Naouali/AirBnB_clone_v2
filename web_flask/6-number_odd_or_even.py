#!/usr/bin/python3
"""
module to create a page/route
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    return (str(n) + ' is a number')


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    var = 'odd'
    if n % 2 != 0:
        return render_template('6-number_odd_or_even.html', n=n, k='odd')
    return render_template('6-number_odd_or_even.html', n=n, k='even')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
