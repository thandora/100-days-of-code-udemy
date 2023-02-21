from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

"""
Sends an email notification to all users if there are available flights that
are priced lower than the historical lowest price stored in a google sheet.
"""

searcher = FlightSearch()
notifier = NotificationManager()

data_manager = DataManager()
data_manager.get_destination_data()

# Check for flights that are priced lower than current lowest price.
for data in data_manager.destination_data:
    id = data["id"]

    # Search flight prices using iata code
    iata = data["iataCode"]
    search_result = searcher.search(iata)

    # Filter flights to lowest price
    flight_data = FlightData()
    flight_data.low_flights(search_result)
    flights = flight_data.lowest_flights["flights"]
    lowest_price = flight_data.lowest_flights["price"]

    # If stored data in sheet has no lowest price yet, update
    # to lowest price of search result.
    if data.get("lowestPrice") is None:
        data_manager.update_price(id=id, new_price=lowest_price)
        data["lowestPrice"] = lowest_price

    # Check and send notification if found flights are lower than
    # existing lowest price.
    if lowest_price <= data["lowestPrice"]:
        data_manager.update_price(id=id, new_price=lowest_price)
        data_manager.update_price(id=id, new_price=lowest_price)
        date_range = flight_data.date_range(flights=flights)
        message = notifier.format_message(flights=flights, date_range=date_range)
        emails = data_manager.get_emails()
        notifier.send_notification(message=message, emails=emails)
        print("Flight notifications sent")
