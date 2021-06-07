#!/usr/bin/python3
""" Square Model """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for Square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self._Rectangle__x, self._Rectangle__y,
                        self._Rectangle__width))

    @property
    def size(self):
        """ size setter """
        return self.size

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
