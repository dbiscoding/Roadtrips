from flask import Blueprint

bp = Blueprint('main', __name__)

from . import auth, main, destination, dashboard
