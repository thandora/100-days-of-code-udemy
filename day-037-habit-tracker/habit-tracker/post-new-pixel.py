import requests
from datetime import datetime
from dotenv import load_dotenv
import os

"""
Create a new pixel for an existing graph.
Read more: https://docs.pixe.la/entry/post-pixel
"""

# .env
load_dotenv(".env")
username = os.getenv("USER_NAME")
user_token = os.getenv("TOKEN")
graph_id = os.getenv("GRAPH_ID")

graph_header = {
    "X-USER-TOKEN": user_token,
}

user_endpoint = "https://pixe.la/v1/users"

# Update graph by creating new pixels using POST
graph_ep = f"{user_endpoint}/{username}/graphs/{graph_id}"
some_date = datetime(year=2023, month=1, day=1)

# rawstring format is to stop highlighting %d as placeholder of a number
# Meaning that the following works just as well:
# some_date = some_date.strftime("%Y%m%d")
some_date = some_date.strftime(r"%Y%m%d")

date = some_date
hours = "1.5"
graph_pixel_params = {
    "date": some_date,
    "quantity": hours,
}

# Send request
response = requests.post(url=graph_ep, json=graph_pixel_params, headers=graph_header)
print(response.text)
