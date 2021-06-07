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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.coord_validator("x", x)
        self.__x = x
        self.coord_validator("y", y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width setter """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ height setter """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ x setter """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.coord_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ y setter """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.coord_validator("y", value)
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for a in range(self.__y):
            print("")
            for i in range(self.__height):
                for b in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        return ("[Rectangle] (<{}>) <{}>/<{}> - <{}>/<{}>".format(self.id, self.__x, self.__y, self.__width, self.__height))
