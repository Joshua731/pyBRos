from flask import Blueprint

user_blueprint = Blueprint(
    "character_blueprint", __name__, url_prefix="/user")

from .routes import *
