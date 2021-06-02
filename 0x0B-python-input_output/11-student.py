#!/usr/bin/python3
""" task 11 """


class Student:
    """
    class Student that defines a student by:
    Public instance attributes:
    - first_name
    - last_name
    - age
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__
    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for i in json:
            self.__dict__.update({i: json[i]})
