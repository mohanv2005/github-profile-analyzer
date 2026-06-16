import requests

BASE_URL = "https://api.github.com/users"


def get_user_profile(username):

    url = f"{BASE_URL}/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None


if __name__ == "__main__":

    profile = get_user_profile("octocat")

    print(profile)