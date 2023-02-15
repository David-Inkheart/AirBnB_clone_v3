#!/usr/bin/python3
""" The index module """
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns the HTTP status """
    return jsonify({"status": "OK"})
