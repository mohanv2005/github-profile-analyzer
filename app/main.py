from github_api import get_user_profile

username = input("Enter GitHub username: ")

profile = get_user_profile(username)

if profile:
    print("\nGitHub Profile")
    print("--------------------")

    print("Name:", profile["name"])
    print("Followers:", profile["followers"])
    print("Repositories:", profile["public_repos"])

else:
    print("User not found")