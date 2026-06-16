import requests
from config import BASE_URL

def get_user_profile(username):
    url = f"{BASE_URL}/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch user profile: {response.status_code}")
    
    