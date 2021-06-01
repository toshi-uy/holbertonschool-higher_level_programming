#!/usr/bin/python3
"""class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """inicialization for class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return super().__str__("[Rectangle] {}/{}".format(self.__width, self.__height))
