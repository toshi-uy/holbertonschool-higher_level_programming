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
        """ returns the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """prints the rectangle, taking care of the positions"""
        for a in range(self.__y):
            print("")
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """string representation of the class"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.integer_validator("width", args[1])
                self.__width = args[1]
            if len(args) > 2:
                self.integer_validator("height", args[2])
                self.__height = args[2]
            if len(args) > 3:
                self.coord_validator("x", args[3])
                self.__x = args[3]
            if len(args) > 4:
                self.coord_validator("y", args[4])
                self.__y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'width':
                        self.integer_validator("width", value)
                    if key == 'height':
                        self.integer_validator("height", value)
                    if key == 'x':
                        self.coord_validator("x", value)
                    if key == 'y':
                        self.coord_validator("y", value)
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
