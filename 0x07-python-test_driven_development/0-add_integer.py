#!/usr/bin/python3
"""
Test Driven Doc import
Don't import using __import__

"""

import doctest
doctest.testfile("tests/0-add_integer.txt")


def add_integer(a, b=98):
    """
    function that adds 2 integers
    Returns a + b
    a and b are first casted to integers if they are float
    Raises:
    TypeError: with the message a must be an integer if either
    a or b are no integers or floats
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return a + b}
