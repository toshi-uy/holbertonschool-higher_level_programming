#!/usr/bin/python3
""" 0x0C. Python - Almost a circle """
import json


class Base:
    """ Clase Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def coord_validator(self, name, value):
        """Public instance method that validates coordinates"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
                return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            jason = []
            if list_objs is not None:
                for a in list_objs:
                    jason.append(cls.to_dictionary(a))
                jason = Base.to_json_string(jason)
                return json.dump(str(jason), f)
            else:
                list_objs = jason
                return json.dump(str(jason), f)
