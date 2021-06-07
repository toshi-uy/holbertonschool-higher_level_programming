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
                .format(self.id, self.x, self.y,
                        self.size))

    @property
    def size(self):
        """ size setter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method that assigns attributes"""
        if len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            elif len(args) > 2:
                self.x = args[2]
            elif len(args) > 3:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
