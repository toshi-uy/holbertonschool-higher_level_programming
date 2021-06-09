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
        self.integer_validator("width", value)
        self.width = value

    def update(self, *args, **kwargs):
        """public method that assigns attributes"""
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.integer_validator("width", args[1])
                self.size = args[1]
            if len(args) > 2:
                self.coord_validator("x", args[2])
                self.x = args[2]
            if len(args) > 3:
                self.coord_validator("y", args[3])
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'size':
                        self.integer_validator("width", value)
                    if key == 'x':
                        self.coord_validator("x", value)
                    if key == 'y':
                        self.coord_validator("y", value)
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
