#!/usr/bin/python3
""" function that returns the list of available attributes and methods of an object """

def lookup(obj):
	a = [method_name for method_name in dir(object)]
	return a
