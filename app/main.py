from github_api import get_user_profile, get_user_repositories
from analyzer import analyze_repositories


username = input("Enter GitHub username: ")

profile = get_user_profile(username)
repositories = get_user_repositories(username)

if profile:
    print("\nGitHub Profile")
    print("--------------------")

    print("Name:", profile["name"])
    print("Followers:", profile["followers"])
    print("Repositories:", profile["public_repos"])

    # print("\nUser Repositories")
    # print("--------------------")
    # for repo in repositories:
    #     print("Name:", repo["name"])
    #     print("Description:", repo["description"])
    #     print("Stars:", repo["stargazers_count"])
    #     print("Forks:", repo["forks_count"])
    #     print()

    print("\nRepository Analysis")
    print("--------------------")
    analysis = analyze_repositories(repositories)
    print("Total Stars:", analysis["total_stars"])

    print("\nLanguages:")

    for lang, count in analysis["languages"].items():
        print(f"{lang}: {count}")
else:
    print("User not found")