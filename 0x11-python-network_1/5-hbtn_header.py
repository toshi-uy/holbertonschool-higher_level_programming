#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
variable found in the header of the response using Requests
"""

if __name__ == "__main__":
    import requests
    import sys

    if sys.argv[1]:
        req = requests.get(sys.argv[1])
        info = req.headers
        print(info['X-Request-Id'])
