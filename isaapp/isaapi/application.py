'''
Setup API specific settings.
'''
from flask import Flask
from flask_cors import CORS


def create_app(app_name='ISAAP'):
    app = Flask(app_name)
    app.config.from_object('isaapi.config.BaseConfig')

    CORS(app)

    # Register the API blueprint object in the application object
    from isaapi.api import api
    app.register_blueprint(api, url_prefix="/api")

    # Register the database object in the application object
    from .models import db
    db.init_app(app)

    return app
