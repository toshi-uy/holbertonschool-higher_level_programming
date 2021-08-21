#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 3:
        respond = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
        print(respond.headers.get('id'))
