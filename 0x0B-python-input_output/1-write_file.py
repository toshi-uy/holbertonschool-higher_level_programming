#!/usr/bin/python3
""" Task 1 """


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w') as f:
        write_data = f.write(text)
    return write_data
