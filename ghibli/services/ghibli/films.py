"""Handle Ghibli API films resource."""
from typing import List, Mapping, Union

import requests

from ghibli.config.config import Configuration
from ghibli.services.ghibli.people import list_people

Params = Mapping[str, Union[str, int]]


def list_films() -> List:
    """List all Ghibli films."""

    # Hardcode limit to its max size since we want this endpoint
    # to retrieve all films and it does not seem that films
    # endpoint allow results to be paginated
    params: Params = {"limit": 250, "fields": "id,title"}
    return requests.get(f"{Configuration.get_api_url()}/films", params=params).json()


def list_films_with_people() -> List:
    """List Ghibli films with people belonging to it."""

    # Creating hashmap to speed-up iterations on collections
    films_with_people = {}
    for film in list_films():
        hash_key = f'{Configuration.get_api_url()}/films/{film["id"]}'
        films_with_people[hash_key] = film
        films_with_people[hash_key]["people"] = []

    # List people
    people = list_people()

    # Merge people with films
    for character in people:
        for film in character["films"]:
            # Select only necessary fields
            selected_people_field = ["id", "name"]
            films_with_people[film]["people"].append(
                {key: character[key] for key in selected_people_field}
            )

    return list(films_with_people.values())
