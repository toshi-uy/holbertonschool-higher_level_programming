#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, using requests
"""

if __name__ == "__main__":
    import requests
    import sys

    if sys.argv[1]:
        req = requests.Request('POST', sys.argv[1], headers={'email': sys.argv[2]})
        prepared = req.prepare()
        print(prepared.body)
