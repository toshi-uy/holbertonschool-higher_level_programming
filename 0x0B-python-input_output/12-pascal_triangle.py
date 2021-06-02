#!/usr/bin/python3
""" Task 12 """


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    trow = []
    if n <= 0:
        return trow
    for line in range(1, n + 1):
    c = 1
    for i in range(1, line + 1):
        trow.append(c)
        c = int(c * (line - i) / i)
    return trow
