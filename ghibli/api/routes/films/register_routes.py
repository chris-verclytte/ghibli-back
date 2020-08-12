"""Defines the films routes."""
from flask import Blueprint, Response, request

from ghibli.api.routes.films.list import list_films


def register_routes(api: Blueprint) -> None:
    """Register the `/films` routes."""

    @api.route("/films", methods=["GET"])
    def _list_films() -> Response:
        return list_films(with_people=True) if request.args.get("with_people") else list_films()
