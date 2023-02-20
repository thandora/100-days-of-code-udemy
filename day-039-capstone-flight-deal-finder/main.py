# This file will need to use the DataManager, FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from dotenv import load_dotenv
import os

# env vars
load_dotenv(".env")

searcher = FlightSearch()
data = searcher.search("BER")
data_manager = FlightData(data=data)
print(data_manager.flights)


