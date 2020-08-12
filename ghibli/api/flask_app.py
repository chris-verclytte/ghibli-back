"""Return an initialized Flask application with the API."""
from flask import Flask

from ghibli.api.api import create_api


def create_app() -> Flask:
    """Initialize a Flask app."""
    app = Flask(__name__)

    api = create_api()
    app.register_blueprint(api)

    return app
