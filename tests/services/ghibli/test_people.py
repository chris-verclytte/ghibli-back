from unittest import TestCase
from unittest.mock import patch

from ghibli.services.ghibli.people import list_people


@patch("ghibli.services.ghibli.people.requests", autospec=True)
@patch("ghibli.services.ghibli.people.Configuration", autospec=True)
class TestPeople(TestCase):
    def test_list_people(self, configuration_mock, requests_mock):
        """Should properly list people."""
        configuration_mock.get_api_url.return_value = "http://some_url"
        fake_list = [{"id": "1", "name": "character-1 "}, {"id": "2", "name": "character-2"}]
        requests_mock.get.return_value.json.return_value = fake_list

        result = list_people()

        configuration_mock.get_api_url.assert_called_once()
        requests_mock.get.assert_called_once_with(
            "http://some_url/people", {"limit": 250, "fields": "id,name,films"}
        )
        self.assertEqual(result, fake_list)
