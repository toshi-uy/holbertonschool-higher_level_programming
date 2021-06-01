#!/usr/bin/python3
"""class Square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(BaseGeometry, Rectangle):
    """
    Square class that inherits from Rectangle, that inherits
    from BaseGeometry
    """
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method"""
        return self.__size ** 2

    def __str__(self):
        return super().__str__()