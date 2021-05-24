#!/usr/bin/python3
"""defining a class Square"""


class Rectangle:
    """
    Rectangle Class
    Args:
        width (int): Rectangle width.
        heigth (int): Rectangle height
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
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

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
        r = ""
        if self.__height != 0 and self.__width != 0:
            r += '\n'.join((str(self.print_symbol) *
                            self.__width) for j in range(self.__height))
        return r

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """staticmethod that return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2

    @classmethod
    def square(cls, size=0):
        """classmethod that returns a new Rectangle instance == size"""
        Rectangle.width = size
        Rectangle.height = size
        return cls(size, size)
