#!/usr/bin/python3
"""
Starts a flask application
"""


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)



@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return all data in the db  """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    print(places)
    return render_template('100-hbnb.html',
                           states=states,
                           places=places,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_data(self):
    """ closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
