#!/usr/bin/python3
""" Square Model """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for Square """
        super().__init__(size, size, x, y, id)
        self.size = size
