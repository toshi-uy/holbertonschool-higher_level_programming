#!/usr/bin/pyhon3
""" Write a class MyList that inherits from list """


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """prints sorted lists"""
        print(sorted(self))
