#!/usr/bin/python3
""" The index module for the App """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns the HTTP status """
    return jsonify({"status": "OK"})
