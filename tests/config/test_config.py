import os
from unittest import TestCase
from unittest.mock import patch

from ghibli.config.config import Configuration


class TestConfig(TestCase):
    @patch.dict(os.environ, {"GHIBLI_API_URL": "http://some_url"})
    def test_get_api_url(self):
        """Should properly return API url."""
        result = Configuration.get_api_url()
        self.assertEqual(result, "http://some_url")
