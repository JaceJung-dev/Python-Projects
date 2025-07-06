import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create a user account
create_user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(create_user_response.text)

# Create a graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Running Time Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

create_graph_response = requests.post(
    url=graph_endpoint, json=graph_config, headers=headers
)
print(create_graph_response.text)

# Post a pixel
today = datetime.now().strftime("%Y%m%d")

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
post_pixel_config = {
    "date": today,
    "quantity": input("How many hours did you run?: "),
}

post_pixel_response = requests.post(
    url=post_pixel_endpoint, json=post_pixel_config, headers=headers
)
print(post_pixel_response.text)

# Update a Pixel
update_pixel_endpoint = f"{post_pixel_endpoint}/{today}"
update_pixel_config = {
    "quantity": "3",
}

update_pixel_response = requests.put(
    url=update_pixel_endpoint, json=update_pixel_config, headers=headers
)
print(update_pixel_response.text)

# # Delete a Pixel
delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{today}"

delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_pixel_response.text)
