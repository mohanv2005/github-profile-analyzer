def analyze_repositories(repositories):

    total_stars = 0

    languages = {}

    for repo in repositories:

        total_stars += repo["stargazers_count"]

        language = repo["language"]

        if language:

            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

    return {
        "total_stars": total_stars,
        "languages": languages
    }