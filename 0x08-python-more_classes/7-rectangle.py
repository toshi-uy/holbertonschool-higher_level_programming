#!/usr/bin/python3


class Rectangle:
    """
    Rectangle Class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        docstring on the __init__ method.
        Args:
            width (int): Rectangle width.
            heigth (int): Rectangle height
        """
        Rectangle.number_of_instances += 1
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
        rect = ""
        if self.__height != 0 and self.__width != 0:
            rect += "\n".join((str(Rectangle.print_symbol) * self.__width) for j in range(self.__height))
        return rect

    def __repr__(self):
        """
        Representation of the Rectangle
        Returns:
            The representation of the rectangle.
        """
        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
