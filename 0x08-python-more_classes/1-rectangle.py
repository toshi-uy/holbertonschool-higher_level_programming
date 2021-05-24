#!/usr/bin/python3


class Rectangle:
    """ Rectangle Class
    Attributes:
        attr1 (str): Description of `attr1`.
    """
    def __init__(self, width=0, height=0):
        """docstring on the __init__ method.
        Args:
            param1 (str): Description of `param1`.
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (:obj:`list` of :obj:`str`): Description of `param3`.

        """
        self.__width = width
        self.__heigth = height
    @property
    """str: Properties should be documented in their getter method."""
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
    """str: Properties should be documented in their getter method."""
    def height(self):
        return self.__heigth

    @height.setter
    def height(self, value):
        if type(value) is int and value > 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")