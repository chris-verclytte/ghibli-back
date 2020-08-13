"""Register all routes under the /api prefixes."""
from flask import Blueprint

from ghibli.api.routes import films


def create_api() -> Blueprint:
    """Return the collection of routes and other app-related functions."""
    api = Blueprint("api", __name__, url_prefix="/api")

    films.register_routes(api=api)

    return api
