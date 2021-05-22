#!/usr/bin/python3
"""
Test Driven Doc import
Don't import using __import__
"""

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of
    these characters: . ? and :
    Args:
    text: text to indent
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    space = 0
    for a in text:
        if space == 0:
            if a == ' ':
                continue
            else:
                space = 1
        if space == 1:
            if a == '?' or a == ':':
                print(a)
                print()
                space = 0
            elif a == '.':
                print(a)
                print()
                space = 0
            else:
                print(a, end="")
