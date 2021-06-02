#!/usr/bin/python3
""" Task 3 """
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    f = ""
    json.dump(my_obj, f)
    return f
