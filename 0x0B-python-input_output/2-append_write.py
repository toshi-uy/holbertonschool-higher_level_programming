#!/usr/bin/python3
""" Task 2 """


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'aw') as f:
        write_data = f.write(text)
    return write_data
