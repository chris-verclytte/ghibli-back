"""Films list routes."""
from http import HTTPStatus

import ghibli.services.ghibli.films as films


def list_films(*, with_people=False):
    """List all Ghibli films"""
    films_list = films.list_films_with_people() if with_people else films.list_films()
    return {"films": films_list}, HTTPStatus.OK
