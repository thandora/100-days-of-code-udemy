import requests
from pprint import pprint
import datetime as dt

"""
Exercise on API parameters
"""
LATITUDE = 31.968599
LONGITUDE = -99.901810

# API endpoint
url = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": LATITUDE,
    "long": LONGITUDE,
    "formatted": 0,
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()
pprint(data)

# Take only the hour of sunrise and sunset
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

now = dt.datetime.now()

print(sunrise)
print(now.hour)
