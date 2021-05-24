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

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            width (int): Rectangle width.
            heigth (int): Rectangle height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ With property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is int and value > 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is int and value > 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
