#!/usr/bin/python3
""" Task 12 """


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    triangle = []
    if n <= 0:
        return []
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            triangle.append(c)
            c = int(c * (line - i) / i)
    return triangle[1:]
