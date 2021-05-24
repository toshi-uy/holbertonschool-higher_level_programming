#!/usr/bin/python3
"""
Creating class for rectangle
"""


class Rectangle:
    """
    Rectangle Class
    Args:
        width (int): Rectangle width.
        heigth (int): Rectangle height
    """

    def __init__(self, width=0, height=0):
        """
        docstring on the __init__ method.
        Args:
            width (int): Rectangle width.
            heigth (int): Rectangle height
        """
        self.__height = height
        self.__width = width

    @property
    """ With property """"
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int and value > 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    """ height property """
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int and value > 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
