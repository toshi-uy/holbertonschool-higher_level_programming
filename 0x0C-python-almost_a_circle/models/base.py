#!/usr/bin/python3
""" 0x0C. Python - Almost a circle """
import json
from json import encoder
from os import stat
import csv
from sys import argv


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
        with open(filename, 'w', encoding='utf-8') as f:
            jason = []
            if list_objs is not None:
                for a in list_objs:
                    jason.append(cls.to_dictionary(a))
                f.write(cls.to_json_string(jason))
            else:
                json.dump(jason, f)

    @staticmethod
    def from_json_string(json_string):
        """returns an instance with all attributes already set"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            dummy = cls(5)
        elif cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances """
        jason = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename) as f:
                for objs in cls.from_json_string(f.read()):
                    jason.append(cls.create(**objs))
                return jason
        except:
            return jason

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    listr = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    writer.writerow(listr)
                elif cls.__name__ == "Square":
                    lists = [obj.id, obj.size, obj.x, obj.y]
                    writer.writerow(lists)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        csv_list = []
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename) as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == "Rectangle":
                    for row in reader:
                        dict_cvs = {
                            "id": int(row[0]), "width": int(row[1]),
                            "height": int(row[2]), "x": int(row[3]),
                            "y": int(row[4])
                        }
                        obj = cls.create(**dict_cvs)
                        csv_list.append(obj)
                    return csv_list
                elif cls.__name__ == "Square":
                    for row in reader:
                        dict_cvs = {
                            "id": row[0], "size": row[1],
                            "x": row[2], "y": row[3]
                        }
                        obj = cls.create(**dict_cvs)
                        csv_list.append(obj)
                    return csv_list
        except:
            return csv_list
