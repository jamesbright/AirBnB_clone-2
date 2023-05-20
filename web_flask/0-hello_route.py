#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
# create an instance of flask app
app = Flask(__name__)

# home route that returns a text when accessed
@app.route('/', strict_slashes=False)
def hello_route():
    """Prints text
    Returns:
        text
    """

    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
