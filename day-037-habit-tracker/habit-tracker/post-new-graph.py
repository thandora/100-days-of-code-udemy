import requests
import webbrowser
from dotenv import load_dotenv
import os

"""
Create a new graph on pixela using POST.
Read more: https://docs.pixe.la/entry/post-graph
"""

# .env
load_dotenv(".env")
username = os.getenv("USER_NAME")
user_token = os.getenv("TOKEN")
graph_id = os.getenv("GRAPH_ID")

user_endpoint = "https://pixe.la/v1/users"
# Graph
# Create graph (with header authentication instead of passing API key)
create_graph_ep = f"{user_endpoint}/{username}/graphs"

graph_header = {
    "X-USER-TOKEN": user_token,
}

graph_id = "ttennisgraph"
graph_config = {
    "id": graph_id,
    "name": "Table Tennis Graph",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
}

# Send request
response = requests.post(url=create_graph_ep, json=graph_config, headers=graph_header)
print(response.text)

# Created graph can be viewed here:
# https://pixe.la/v1/users/<username>/graphs/<graph_id>.html
graph_ep = f"{user_endpoint}/{username}/graphs/{graph_id}.html"
webbrowser.open(graph_ep)
