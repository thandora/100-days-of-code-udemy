import requests
import pprint
import smtplib
from dotenv import load_dotenv
import os


"""
Check if it will rain in the following 12 hours, and send an email alert if
it will. API used slightly different, instructions used hourly weather API
which is now a paid subscription while I used was weather update every
3 hours which is free. I also used email notification because I didn't want
to register to another service with my credentials (twilio).

Read more on API used: https://openweathermap.org/forecast5#5days
"""

# .env variables
load_dotenv(".env")
api_key = os.getenv("API_KEY")
lat = float(os.getenv("LAT"))
lon = float(os.getenv("LON"))
MY_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# EMAIL
MY_EMAIL = MY_EMAIL
APP_PASSWORD = APP_PASSWORD

# API
url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()


weather_data = response.json()
data_formatted = pprint.pformat(weather_data, sort_dicts=False)
weather_slice = weather_data["list"][:4]

# Check if will rain in the following 12 hours.
will_rain = False
for time in weather_slice:
    weather_code = time["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

# Send notification if it will rain
if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        message = "Subject:Rain Alert\n\nIt's gonna rain! Don't forget"
        "to bring your umbrella"
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
        print("Rain notification sent.")
