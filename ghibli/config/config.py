"""Ghibli configuration"""

import os


class Configuration:
    """Ghibli configuration"""

    @staticmethod
    def get_api_url():
        """Returns the URL of Ghibli API url"""
        return os.getenv("GHIBLI_API_URL")
