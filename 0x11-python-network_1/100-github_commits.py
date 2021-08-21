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
        url = 'https://api.github.com/repos/' + sys.argv[1] + '/' + sys.argv[2] + '/comits'
        respond = requests.get(url)
        commits = respond.json()
        for index, commit in commits:
            if index >= 9:
                print("{}: {}".format(commit.get('sha'), commit.get('commit').get('author').get('name')))
            else:
                break
