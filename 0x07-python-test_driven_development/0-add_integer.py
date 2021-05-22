#!/usr/bin/python3
"""
Test Driven Doc import
Don't import using __import__

"""

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")


def add_integer(a, b=98):
    """
    function that adds 2 integers
    Returns a + b
    a and b are first casted to integers if they are float
    Raises:
    TypeError: with the message a must be an integer if either
    a or b are no integreres or floats
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integrer")
    if type(b) != int:
        raise TypeError("b must be an integrer")
    else:
        return a + b
