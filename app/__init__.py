from flask import Flask
from flask_cors import CORS

def create_app(config_filename):
    app = Flask(__name__, static_folder='templates/static')
    CORS(app)
    app.config.from_object(config_filename)
