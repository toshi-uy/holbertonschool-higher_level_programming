#!/usr/bin/python3


class Rectangle:
    """
    Rectangle Class
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

    def area(self):
        """
        Area method
        Args:
            width: The first parameter.
            height: The second parameter.

        Returns:
            Area of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def perimeter(self):
        """
        Perimeter method
        Args:
            width: The first parameter.
            height: The second parameter.

        Returns:
            Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        String of the Rectangle
        Returns:
            The String of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            rect = ""
            for j in range(self.__height):
                for i in range(self.__width):
                    rect += '#'
                    if i == self.__width - 1 and j != self.__height - 1:
                        rect += '\n'
            return rect
    def __repr__(self):
        """
        Representation of the Rectangle
        Returns:
            The representation of the rectangle.
        """
        return ('Rectangle({}, {})'.format(self.__width, self.__height))