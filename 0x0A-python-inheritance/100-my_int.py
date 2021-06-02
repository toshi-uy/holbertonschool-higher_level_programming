#!/usr/bin/python3
"""my own int"""


class MyInt(int):
    """my own class int"""

    def __init__(self, integer):
        """instalation of class"""
        self.__integer = integer

    def __eq__(self, integer):
        """equality method"""
        return self.__integer != self.__integer

    def __ne__(self, integer):
        """unequality method"""
        return self.__integer == self.__integer
