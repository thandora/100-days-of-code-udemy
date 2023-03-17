import requests
from dotenv import load_dotenv
import os

"""
Create a user account on pixela using POST.
Read more: https://docs.pixe.la/entry/post-user
"""

# .env
load_dotenv(".env")
username = os.getenv("USER_NAME")
# token is defined by you, and will act like as password for your account
user_token = os.getenv("TOKEN")

user_endpoint = "https://pixe.la/v1/users"

# Create pixela account
# token is defined by you, and will act like as password for your account
create_user_ep = user_endpoint
user_params = {
    "token": user_token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Send request
response = requests.post(url=user_endpoint, json=user_params)
print(response.text)
