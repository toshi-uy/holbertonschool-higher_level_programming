#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request, urllib.error
    import sys

    if sys.argv[1]:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            try:
                print(response.read().decode('utf-8'))
            except:
                print("Error code:",req.getcode())
