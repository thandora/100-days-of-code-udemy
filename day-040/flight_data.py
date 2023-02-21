from dotenv import load_dotenv
import os
from datetime import datetime

"""Class dealing with flight data"""

# env vars
load_dotenv(".env")
search_epoint = os.getenv("SEARCH_EPOINT")
currency = os.getenv("CURRENCY")
from_loc = os.getenv("FROM_LOC")


class FlightData:
    """Responsible for storing, formatting, and generating date range for flight data."""

    def __init__(self) -> None:
        self.lowest_flights = None

    def date_range(self, flights: list) -> list:
        """Returns the first and last date for flight departure.

        Args:
            flights (list): list of flights.

        Returns:
            list: [<first date>, <last date>].
        """
        dates = []
        for flight in flights:
            date = datetime.strptime(flight["departure_date"], r"%Y-%m-%d").date()
            dates.append(date)

        dates.sort()
        dates_str = [d.strftime(r"%Y-%m-%d") for d in dates]
        return [dates_str[0], dates_str[-1]]

    def low_flights(self, raw_data: dict) -> dict:
        """Create a dict of where the lowest price (and equivalent) flights are
        added to a list, how many flights of that price there are, and how much
        was the flight.

        Args:
            raw_data (dict): dict of data from search query from flight_search

        Returns:
            dict: A dict in the form of:
            {
            "flights": <list of lowest priced flights>,
            "found": <n of those flights>,
            "price": <price of flights>,
            }

        """

        if len(raw_data["data"]) == 0:
            return None

        data = raw_data["data"]
        lowest_price = data[0]["price"]
        flights = []

        # Check for
        for flight in data:
            if flight["price"] == lowest_price:
                departure_date = flight["local_departure"].split("T")[0]
                d = {
                    "city_to": flight["cityTo"],
                    "iata_to": flight["cityCodeTo"],
                    "city_from": flight["cityFrom"],
                    "iata_from": flight["cityCodeFrom"],
                    "departure_date": departure_date,
                    "price": flight["price"],
                }

                flights.append(d)
        self.lowest_flights = {
            "flights": flights,
            "found": len(flights),
            "price": lowest_price,
        }
        return self.lowest_flights
