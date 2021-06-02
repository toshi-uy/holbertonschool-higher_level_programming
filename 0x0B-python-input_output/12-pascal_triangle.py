#!/usr/bin/python3
""" Task 12 """


from typing import List


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    trow = []
    if n <= 0:
        return trow
    y = [0]
    for x in range(n):
        trow=[left + right for left,right in zip(trow + y, y + trow)]
    return trow
