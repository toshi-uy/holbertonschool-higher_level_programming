#!/usr/bin/python3
""" Task 5 """
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w+') as f:
        f.write(json.dump(my_obj, f))
