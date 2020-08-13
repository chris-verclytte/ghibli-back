"""Ghibli configuration"""

import os


# Disable this linting rules because other configuration
# methods could go there in the future
# pylint: disable=too-few-public-methods
class Configuration:
    """Ghibli configuration"""

    @staticmethod
    def get_api_url():
        """Returns the URL of Ghibli API url"""
        return os.getenv("GHIBLI_API_URL")
