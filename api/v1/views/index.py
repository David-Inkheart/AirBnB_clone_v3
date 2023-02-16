#!/usr/bin/python3
""" The index module for the App """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.state import Amenity
from models.state import City
from models.state import Place
from models.state import Review
from models.state import User


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns the HTTP status """
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats')
def count_all():
    """ Retrieves the number of each objects by type """
    models = [Amenity, City, Place,
              Review, State, User]
    classes = ["amenities", "cities", "places",
             "reviews", "states", "users"]

    dict = {}

    for i in range(0, 6):
        dict[classes[i]] = storage.count(models[i])

    return jsonify(dict)
