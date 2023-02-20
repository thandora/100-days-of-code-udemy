import os
from dotenv import load_dotenv
import requests

load_dotenv(".env")
sheet_epoint = os.getenv("SHEET_EPOINT")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheet_endpoint = sheet_epoint
        self.destination_data = None

    def get_destination_data(self):
        r = requests.get(url=self.sheet_endpoint)
        self.destination_data = r.json()["prices"]
        return self.destination_data

    def update_price(self, id, new_price):
        url = f"{sheet_epoint}/{id}"
        updated_data = {
            "price": {
                "lowestPrice": new_price,
            }
        }

        requests.put(url=url, json=updated_data)
