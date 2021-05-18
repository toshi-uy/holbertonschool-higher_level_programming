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

    """Public instance method"""
    def area(self):
        """Return value of area"""
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """Return value of size"""
        return self.__size

    @size.setter
    def size(self, number):
        """initialization method"""
        if type(number) is not int:
            raise TypeError("size must be an integer")
        if number < 0:
            raise ValueError("size must be >= 0")
        self.__size = number
