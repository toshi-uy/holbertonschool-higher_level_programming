#!/usr/bin/python3
"""defining a class Square"""


class Square:
    """
    Classs that defines a square
    Args:
            size (int): The size of the square.
            position (int, int): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialization method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    """Public instance method"""
    def area(self):
        """Return value of area"""
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """Return value of size"""
        return self.__size

    @property
    def position(self):
        """Return value of position"""
        return self.__position

    @size.setter
    def size(self, number):
        """initialization method"""
        if type(number) is not int:
            raise TypeError("size must be an integer")
        if number < 0:
            raise ValueError("size must be >= 0")
        self.__size = number

    @position.setter
    def position(self, value):
        """initialization method"""
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    """Public instance method"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for a in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for b in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
