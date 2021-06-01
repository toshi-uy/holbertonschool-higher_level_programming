#!/usr/bin/python3
""" Write a class MyList that inherits from list """


class MyList(list):
    """
    MyList class
    Attributes:
    attr1(print_sorted): prints a sorted list
    """
    def print_sorted(self):
        """prints sorted lists"""
        print(sorted(self))
