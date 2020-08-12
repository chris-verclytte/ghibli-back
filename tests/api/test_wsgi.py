from unittest import TestCase
from unittest.mock import patch


class TestWsgi(TestCase):
    @patch("ghibli.api.flask_app.create_app", autospec=True)
    def test_api_instance(self, create_app_mock):
        import ghibli.api.wsgi  # pylint: disable=import-outside-toplevel,unused-import

        create_app_mock.assert_called()
