#!/usr/bin/python3
""" Adv Task 13 """


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    text = open(filename, 'r').readlines()
    with open(filename, 'w') as f:
        for line in text:
            f.write(line)
            if search_string in line:
                f.write(new_string)
    f.close()
