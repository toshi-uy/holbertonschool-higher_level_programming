#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, Print all commits by: `<sha>: <author name>`
(one by line)
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 3:
        respond = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))
        commits = respond.json()
        print(commits)
        i = 0
        for commit in commits:
            print(commit)
            if i <= 9:
                print("{}: {}".format(
                    commit.get('sha'),
                    commit.get('commit').get('author').get('name')))
                i += 1
            else:
                break
