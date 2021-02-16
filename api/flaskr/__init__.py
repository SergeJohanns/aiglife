from flask import Flask
from flaskr.models import db
from flaskr.resources import api


def create_app():
    """Factory method for the actual app object."""
    app = Flask(__name__)
    db.init_app(app)
    api.init_app(app)
    return app
