import requests
from dotenv import load_dotenv
import os
import webbrowser
import random
from datetime import datetime, timedelta
import time

"""
Exercise on HTTP requests GET, POST, PUT, and DELETE.
Also on authentication through use of headers.
Read more: https://docs.pixe.la/
"""


def gen_randvalues(n: int, max_value: float = 3) -> dict:
    """Generates a dict of date:random value pair. Date occurs from
    Jan 1, 2023 and increments by 1 day.

    Args:
        n (int): number of entries

    Returns:
        dict: _description_
    """
    values = {}
    for x in range(n):
        start_date = datetime(year=2023, month=1, day=1) + timedelta(days=x)
        start_date = start_date.strftime(r"%Y%m%d")

        # Value is in str, according to API
        values[start_date] = str(round(random.uniform(0, max_value), 1))

    return values


# .env
load_dotenv(".env")
username = os.getenv("USER_NAME")
user_token = os.getenv("TOKEN")

pixela_ep = "https://pixe.la/v1/users"
# # Create pixela account
# create_user_ep = pixela_ep
# user_params = {
#     "token": user_token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_ep, json=user_params)

# # Graph
# # Create graph (with header authentication instead of passing API key)
# create_graph_ep = f"{pixela_ep}/{username}/graphs"
graph_header = {
    "X-USER-TOKEN": user_token,
}
graph_id = "ttennisgraph"
# graph_config = {
#     "id": graph_id,
#     "name": "Table Tennis Graph",
#     "unit": "hours",
#     "type": "float",
#     "color": "kuro",
# }
# response = requests.post(url=create_graph_ep, json=graph_config, headers=graph_header)

# # Open graph page
# graph_ep = f"{pixela_ep}/{username}/graphs/ttennisgraph.html"
# webbrowser.open(graph_ep)

# # Update graph
# Update graph by creating new pixels using POST
graph_ep = f"{pixela_ep}/{username}/graphs/{graph_id}"
some_date = datetime(year=2023, month=1, day=1)
# rawstring format is to stop highlighting %d as placeholder of a number
# i.e. the following works just as well
# some_date = some_date.strftime("%Y%m%d")
some_date = some_date.strftime(r"%Y%m%d")
date = some_date
hours = "1.5"
graph_pixel_params = {
    "date": some_date,
    "quantity": hours,
}
# response = requests.post(url=graph_ep, json=graph_pixel_params, headers=graph_header)
# print(response.text)

# # Create n pixels of random values starting from Jan 1, 2023
# values = gen_randvalues(n=5, max_value=3)
# for date, hours in values.items():
#     graph_pixel_params = {
#         "date": date,
#         "quantity": hours,
#     }
#     response = requests.post(
#         url=graph_ep, json=graph_pixel_params, headers=graph_header
#     )
#     print(f"date: {date} || value: {hours}")
#     print(response.text)
#     time.sleep(3)

# Update graph by updating pixel value using PUT
date_to_edit = "20230215"
value = "1.5"
update_ep = f"{pixela_ep}/{username}/graphs/{graph_id}/{date_to_edit}"
update_params = {"quantity": value}
response = requests.put(url=update_ep, json=update_params, headers=graph_header)

print(response.text)
