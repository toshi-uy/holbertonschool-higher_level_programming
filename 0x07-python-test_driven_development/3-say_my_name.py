#!/usr/bin/python3
"""
Test Driven Doc import
Don't import using __import__
"""

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>
    first_name and last_name must be strings
    Args:
    first_name: must add
    last_name: optional
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}" .format(first_name, last_name))
