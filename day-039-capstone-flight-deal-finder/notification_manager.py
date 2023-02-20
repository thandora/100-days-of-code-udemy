from dotenv import load_dotenv
import os
import smtplib

# EMAIL
load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
currency = os.getenv("CURRENCY")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_notification(self, to_email: str, message: str):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=message)

    def format_message(self, flights, date_range: list):
        flight = flights[0]

        city_to = flight["city_to"]
        city_from = flight["city_from"]
        iata_to = flight["iata_to"]
        iata_from = flight["iata_from"]
        price = flight["price"]

        message = (
            f"Subject: Available Cheap Flights!\n\nFlights for "
            f"{currency}{'{:,}'.format(price)} are available from "
            f"{city_from}-{iata_from} to {city_to}-{iata_to}, from "
            f"{date_range[0]} to {date_range[1]}"
        )
        return message
