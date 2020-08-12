import ghibli.services.ghibli.films as films
from http import HTTPStatus


def list_films(*, with_people=False):
    """List all Ghibli films"""
    print("FILMS = ", films)
    films_list = films.list_films_with_people() if with_people else films.list_films()
    return {"films": films_list}, HTTPStatus.OK
