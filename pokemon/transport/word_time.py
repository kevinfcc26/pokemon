import os

import requests

from core.exepctions import ProviderException


class WorldTimeAPI:
    BASE_URL = os.environ.get("WORD_TIME_API", "")

    def get_time(self, area: str, location: str, region: str = None) -> dict:
        """makes the request to the supplier

        Args:
            area (str): Area to search
            location (str): Location to search
            region (str, optional): Region to search. Defaults to None.

        Raises:
            ProviderException: when there is a problem with the petition

        Returns:
            dict: return the response as a dictionary
        """
        if not self.BASE_URL:
            raise ProviderException("BASE_URL is not set.")
        url = f"{self.BASE_URL}/{area}/{location}/{region if region else ''}"
        response = requests.get(url)
        if response.status_code != 200:
            raise ProviderException(response.content)
        return response.json()
