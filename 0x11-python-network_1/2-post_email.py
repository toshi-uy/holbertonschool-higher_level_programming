#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    if sys.argv[1]:
        data = urllib.parse.urlencode({'email': sys.argv[2]})
        url = sys.argv[1] + "?" + data
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
