#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
    -The letter must be sent in the variable q
    -If no argument is given, set q=""
    -If the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>
    Otherwise:
        -Display Not a valid JSON if the JSON is invalid
        -Display No result if the JSON is empty
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) is 1:
        data = {'q' : ""}
    else:
        data = {'q' : sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        if(len(req.json) is 0):
            print("No result")
        else:
            jeison = req.json()
            print("[{}] {}".format(jeison.get('id'),jeison.get('name')))
    except:
        print("Not a valid JSON")
