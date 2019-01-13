"""
application.py
    - Create a flask app instance and registers db object 
"""
from flask import Flask


def create_app(app_name='ISAAC_COMPLETIONS'):
    app = Flask(app_name)
    app.config.from_object('isaapp.config.BaseConfig')

    from isaapp.api import api

    app.register_blueprint(api, url_prefix="/api")

    return app
