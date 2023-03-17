import requests

"""
Print out the current ISS location by requesting from an API
"""

# API endpoint
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=url)
response.raise_for_status()

data = response.json()
latitude = data["iss_position"]["longitude"]
longitude = data["iss_position"]["latitude"]
iss_position = (latitude, longitude)

print(iss_position)
