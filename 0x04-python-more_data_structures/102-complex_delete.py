#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return a_dictionary
    for key, value in a_dictionary.items():
        if value == value:
            del a_dictionary[key]
            break
    return a_dictionary
