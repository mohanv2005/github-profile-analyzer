import requests
from config import BASE_URL

def get_user_profile(username):

    url = f"{BASE_URL}/{username}"

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        return response.json()

    return None


def get_user_repositories(username):

    url = f"{BASE_URL}/{username}/repos"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    if response.status_code != 200:
        return None