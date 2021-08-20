#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
