#!/usr/bin/pyhon3
""" Write a class MyList that inherits from list """
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")


class MyList(list):
    """
    MyList class
    Attributes:
    attr1(print_sorted): prints a sorted list 
    """

    def print_sorted(self):
        """prints sorted lists"""
        print(sorted(self))
