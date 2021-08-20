#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import requests

    respond = requests.get('https://intranet.hbtn.io/status')
    header = respond.headers
    print("Body response:")
    print("\t- type:", header.get('content-type'))
    print("\t- content:", respond.content)
