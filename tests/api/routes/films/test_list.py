from unittest import TestCase
from unittest.mock import patch

from ghibli.api.flask_app import create_app
from http import HTTPStatus


class TestFilmsList(TestCase):
    def setUp(self):
        app = create_app()
        app.config["TESTING"] = True
        self.app_client = app.test_client()

    @patch("ghibli.api.routes.films.list.films", autospec=True)
    def test_list_films(self, films_mock):
        """Should properly return films list."""
        # Mock
        films_mock.list_films.return_value = [
            {"id": "1", "title": "film-1"},
        ]

        # Tests
        response = self.app_client.get("/api/films")
        data = response.get_json()
        print("DATA =", data)
        # Assertions
        films_mock.list_films.assert_called_once()
        films_mock.list_films_with_people.assert_not_called()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            data, {"films": [{"id": "1", "title": "film-1"}]},
        )

    @patch("ghibli.api.routes.films.list.films", autospec=True)
    def test_list_films_with_people(self, films_mock):
        """Should properly return films list."""
        # Mock
        films_mock.list_films_with_people.return_value = [
            {
                "id": "1",
                "title": "film-1",
                "people": [{"id": "1", "name": "character-1"}, {"id": "2", "name": "character-2"}],
            },
        ]

        # Tests
        response = self.app_client.get("/api/films?with_people=true")
        data = response.get_json()

        # Assertions
        films_mock.list_films_with_people.assert_called_once()
        films_mock.list_films.assert_not_called()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            data,
            {
                "films": [
                    {
                        "id": "1",
                        "title": "film-1",
                        "people": [
                            {"id": "1", "name": "character-1"},
                            {"id": "2", "name": "character-2"},
                        ],
                    },
                ]
            },
        )
