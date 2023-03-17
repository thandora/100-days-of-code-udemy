import requests
from datetime import datetime
from dotenv import load_dotenv
import os

"""
Updates an existing pixel using PUT.
Read more: https://docs.pixe.la/entry/put-pixel
"""

# .env
load_dotenv(".env")
username = os.getenv("USER_NAME")
user_token = os.getenv("TOKEN")
graph_id = os.getenv("GRAPH_ID")

user_endpoint = "https://pixe.la/v1/users"
graph_header = {
    "X-USER-TOKEN": user_token,
}

# Update graph by updating pixel value using PUT
some_date = datetime.now().strftime(r"%Y%m%d")
value = "1.5"
update_ep = f"{user_endpoint}/{username}/graphs/{graph_id}/{some_date}"
update_params = {"quantity": value}

# Send request
response = requests.put(url=update_ep, json=update_params, headers=graph_header)
print(response.text)
