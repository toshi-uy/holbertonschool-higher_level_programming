#!/usr/bin/python3
"""defining a class Square"""


class Square:
    """ Classs that defines a square """
    def __init__(self, size=0):
        """initialization method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
