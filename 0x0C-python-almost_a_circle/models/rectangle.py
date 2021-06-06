#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    Parameters:
    width: width of the rectangle
    height: height of the rectangle
    x: x position
    y: y position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width setter """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @property
    def height(self):
        """ height setter """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @property
    def x(self):
        """ x setter """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @property
    def y(self):
        """ y setter """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.__y = value

