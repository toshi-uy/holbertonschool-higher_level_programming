#!/usr/bin/python3
""" Task 5 """
import json

def save_to_json_file(my_obj, filename):
    with json.dump(my_obj, filename) as f:
        return f