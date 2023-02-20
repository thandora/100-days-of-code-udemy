import os
from dotenv import load_dotenv

load_dotenv(".env")
epoint = os.getenv("SHEET_EPOINT")
# remove above after making project
import json
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, epoint) -> None:
        self.sheet_endpoint = epoint
        self.all_data = None

    def get_all(self):
        r = requests.get(url=self.sheet_endpoint)
        return r.json()

    def get_low_prices(self) -> float:

        if self.all_data is None:
            r = requests.get(url=self.sheet_endpoint)
            low_price = r.json()["prices"]
        else:
            low_price = self.all_data["prices"]

        data = low_price
        print(data)


sheet_manager = DataManager(epoint=epoint)
sheet_manager.get_low_prices()
# with open("flightdata.json") as f:
#     data = json.load(f)

