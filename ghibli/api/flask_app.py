"""Initialization module for Flask application registering the API."""
from flask import Flask
from flask_cors import CORS  # type: ignore

from ghibli.api.api import create_api


def create_app() -> Flask:
    """Initialize a Flask app."""
    app = Flask(__name__)
    CORS(app)

    api = create_api()
    app.register_blueprint(api)

    return app
