#!/usr/bin/python3
""" Task 5 """
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
