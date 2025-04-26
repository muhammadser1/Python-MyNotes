import os
import requests
import webbrowser
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN_PIXELA = os.getenv('TOKEN_PIXELA')


def create_new_user(username: str, agree_terms_of_service: bool = True, not_minor: bool = True) -> int:
    """Creates a new user on Pixela and returns the HTTP status code."""
    pixela_endpoint = "https://pixe.la/v1/users"

    body = {
        "token": TOKEN_PIXELA,
        "username": username,
        "agreeTermsOfService": "yes" if agree_terms_of_service else "no",
        "notMinor": "yes" if not_minor else "no"
    }

    response = requests.post(pixela_endpoint, json=body)
    return response.status_code


def create_graph(username: str, graph_id: str, name: str, unit: str, type_: str, color: str) -> int:
    """Creates a new graph for a Pixela user."""
    pixela_endpoint = f"https://pixe.la/v1/users/{username}/graphs"

    headers = {
        "X-USER-TOKEN": TOKEN_PIXELA
    }

    body = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": type_,
        "color": color,
    }

    response = requests.post(pixela_endpoint, headers=headers, json=body)
    return response.status_code


def open_graph(username: str, graph_id: str) -> None:
    """Opens the Pixela graph page in a web browser."""
    graph_url = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"
    webbrowser.open_new_tab(graph_url)
    time.sleep(2)


def post_pixel(username: str, graph_id: str, date: str, quantity: str) -> int:
    """Posts a pixel (daily record) to the user's graph on Pixela."""
    pixela_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"

    headers = {
        "X-USER-TOKEN": TOKEN_PIXELA
    }

    body = {
        "date": date,  # 'YYYYMMDD'
        "quantity": quantity
    }

    response = requests.post(pixela_endpoint, headers=headers, json=body)

    return response.status_code


# Create new user (uncomment if needed)
# status = create_new_user(username="teacher12")
# print(f"User creation Status Code: {status}")
# if status != 200:
#     print(f"Error creating user! Status code: {status}")
#
# # Create new graph (uncomment if needed)
# status = create_graph(
#     username="teacher12",
#     graph_id="test-graph2",
#     name="graph-name",
#     unit="commit",
#     type_="int",
#     color="shibafu"
# )
# print(f"Graph creation finished with Status Code: {status}")

post_pixel("teacher12", "test-graph2", "20240926", "20")

# Open graph
open_graph("teacher12", "test-graph2")
