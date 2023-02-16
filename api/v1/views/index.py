#!/usr/bin/python3
""" The index module for the App """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns the HTTP status """
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', strict_slashes=False)
def stats():
    """ Returns the number of each instance type """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
