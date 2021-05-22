#!/usr/bin/python3
"""
Test Driven Doc import
Don't import using __import__
"""

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")

def print_square(size):
    """
    function that prints a square with the character #.
    Args:
    size: is the size length of the square
    size must be a positive integrer
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
