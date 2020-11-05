from flask import Flask
from flask_cors import CORS

from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)
    app.config["CORS_HEADERS"] = 'application/json'
    return app
