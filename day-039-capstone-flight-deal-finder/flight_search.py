import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# env vars
load_dotenv(".env")
search_epoint = os.getenv("SEARCH_EPOINT")
api_key = os.getenv("KIWI_API")
currency = os.getenv("CURRENCY")
from_loc = os.getenv("FROM_LOC")

# Dates and formatting
today = datetime.now().date()
tomorrow = today + timedelta(days=1)
end_date = today + relativedelta(month=6)
today = today.strftime(r"%d/%m/%Y")
tomorrow = tomorrow.strftime(r"%d/%m/%Y")
end_date = end_date.strftime(r"%d/%m/%Y")

search_params = {
    "fly_from": from_loc,
    "dateFrom": tomorrow,
    "dateTo": end_date,
    "curr": currency,
    "limit": 50,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.flight_params = search_params

    def search(self, location: str) -> dict:
        """Search for flights bound to <location> using kiwi API.

        Args:
            location (str): code for destination

        Returns:
            dict: flights matching query
        """
        # API
        url = "https://api.tequila.kiwi.com/v2/search"
        header = {"apikey": api_key}
        self.flight_params["fly_to"] = location.upper()

        # Request from API
        r = requests.get(url=url, params=self.flight_params, headers=header)
        return r.json()
