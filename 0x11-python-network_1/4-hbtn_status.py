#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
using requests package
"""

if __name__ == "__main__":
    import requests

    respond = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(respond.text))
    print("\t- content:", respond.content)
