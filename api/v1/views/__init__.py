#!/usr/bin/python3
import Blueprint from flask
from api.v1.views.index import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')