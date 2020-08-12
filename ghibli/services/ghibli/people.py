import requests
from ghibli.config.config import Configuration


def list_people():
    """List Ghibli people"""

    # Hardcode limit to its max size since we want this endpoint
    # to retrieve all films and it does not seem that films
    # endpoint allow results to be paginated
    params = {"limit": 250, "fields": "id,name,films"}

    response = requests.get(f"{Configuration.get_api_url()}/people", params=params)
    return response.json()
