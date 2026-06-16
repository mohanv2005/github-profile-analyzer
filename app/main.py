from fastapi import FastAPI

from github_api import (
    get_user_profile,
    get_user_repositories
)

from analyzer import analyze_repositories

app = FastAPI()


@app.get("/github/{username}")
def analyze_profile(username: str):

    profile = get_user_profile(username)

    if not profile:
        return {
            "error": "User not found"
        }

    repositories = get_user_repositories(username)

    analysis = analyze_repositories(repositories)

    return {
        "name": profile["name"],
        "followers": profile["followers"],
        "public_repositories": profile["public_repos"],
        "analysis": analysis
    }