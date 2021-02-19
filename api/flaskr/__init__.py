from os import environ
import time
from flask import Flask
from flaskr.models import db
from flaskr.resources import api


def create_app():
    """Factory method for the actual app object."""
    app = Flask(__name__)
    app.config['MONGOALCHEMY_DATABASE'] = 'mongo'
    # localhost is already the default, but it will probably change later.
    app.config['MONGOALCHEMY_SERVER'] = 'mongo'
    app.config['MONGOALCHEMY_PORT'] = '27017'
    app.config['MONGOALCHEMY_USER'] = 'mongoadmin'
    app.config['MONGOALCHEMY_PASSWORD'] = environ.pop('MONGO_PASS')
    # wait for the mongo container to come online before connecting
    # docker-compose has a thing for this but it's too much effort
    time.sleep(10)
    db.init_app(app)
    api.init_app(app)
    return app
