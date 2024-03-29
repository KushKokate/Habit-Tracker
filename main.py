import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "kushkokat"
token = "thisissecret"
graph_id = "gpa123"

# Create a new user
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Uncomment the following lines to create a new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Define the endpoint for creating a new graph
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

# Parameters for creating a new graph
graph_params = {
    "id": graph_id,  # Unique identifier for the graph
    "name": "Coding Graph",  # Name of the graph
    "unit": "commit",  # Unit of the data (e.g., commits)
    "type": "int",  # Type of data (int for integer values)
    "color": "sora",  # Color of the graph (sora is a predefined color)
}

now = datetime.now()
date = now.strftime("%Y%m%d")
# Headers containing the user token
headers = {
    "X-USER-TOKEN": token,
}

# Send a POST request to create the new graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
pixel_config = {
    "date": date,
    "quantity": input("How many commits did you make today? "),
}

responses = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(responses.text)
thing_endpoint =  f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"
thing_config = {
    "quantity": "15"
}
#response = requests.put(url=thing_endpoint, json=thing_config, headers=headers)
#print(response.text)
delete_endpoint =  f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)
