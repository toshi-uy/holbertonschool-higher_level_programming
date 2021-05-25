#!/usr/bin/python3
"""Class that accepts only first_name variables"""

class Frozen(object):
    __List = []
    def __setattr__(self, key, value):
        setIsOK = False
        for item in self.__List:
            if key == item:
                setIsOK = True

        if setIsOK == True:
            object.__setattr__(self, key, value)
        else:
            raise AttributeError("%r object has no attribute %r" % (self.__class__.__name__, key))

class LockedClass(Frozen):
    _Frozen__List = ["first_name"]
    def __init__(self):
        self.first_name = ""
