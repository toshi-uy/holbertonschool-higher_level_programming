#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """sub instance of a class"""
    return (issubclass(obj, a_class))
