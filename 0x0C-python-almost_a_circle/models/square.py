#!/usr/bin/python3
""" Square Model """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for Square """
        super().Rectangle.__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] (<{}>) <{}>/<{}> - <{}>".format(self.id, self._Rectangle.__x,
                                                          self._Rectangle.__y,
                                                          self._Rectangle.__width))
