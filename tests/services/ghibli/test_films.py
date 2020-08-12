from unittest import TestCase
from unittest.mock import patch

from ghibli.services.ghibli.films import list_films, list_films_with_people


@patch("ghibli.services.ghibli.films.requests", autospec=True)
@patch("ghibli.services.ghibli.films.Configuration", autospec=True)
class TestFilms(TestCase):
    def test_list_films(self, configuration_mock, requests_mock):
        """Should properly list films."""
        configuration_mock.get_api_url.return_value = "http://some_url"
        fake_list = [{"id": "1", "title": "film-1 "}, {"id": "1", "title": "film-1"}]
        requests_mock.get.return_value.json.return_value = fake_list

        result = list_films()

        configuration_mock.get_api_url.assert_called_once()
        requests_mock.get.assert_called_once_with(
            "http://some_url/films", {"limit": 250, "fields": "id,title"}
        )
        self.assertEqual(result, fake_list)

    @patch("ghibli.services.ghibli.films.list_people", autospec=True)
    @patch("ghibli.services.ghibli.films.list_films", autospec=True)
    def test_list_films_with_people(
        self, list_films_mock, list_people_mock, configuration_mock, _requests_mock
    ):
        """Should properly list films with people."""
        # Mocks
        configuration_mock.get_api_url.return_value = "http://some_url"
        fake_films_list = [
            {"id": "1", "title": "film-1"},
            {"id": "2", "title": "film-2"},
            {"id": "3", "title": "film-3"},
        ]
        list_films_mock.return_value = fake_films_list
        fake_people_list = [
            {"id": "1", "name": "character-1", "films": ["http://some_url/films/1"]},
            {
                "id": "2",
                "name": "character-2",
                "films": ["http://some_url/films/1", "http://some_url/films/2"],
            },
            {"id": "3", "name": "character-3", "films": []},
        ]
        list_people_mock.return_value = fake_people_list

        # Test
        result = list_films_with_people()

        # Assertions
        list_films_mock.assert_called_once()
        list_people_mock.assert_called_once()
        self.assertEqual(
            result,
            [
                {
                    "id": "1",
                    "title": "film-1",
                    "people": [
                        {"id": "1", "name": "character-1"},
                        {"id": "2", "name": "character-2"},
                    ],
                },
                {"id": "2", "title": "film-2", "people": [{"id": "2", "name": "character-2"}]},
                {"id": "3", "title": "film-3", "people": []},
            ],
        )
