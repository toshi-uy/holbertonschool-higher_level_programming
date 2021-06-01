#!/usr/bin/pyhon3
""" Write a class MyList that inherits from list """

class MyList(list):
	def print_sorted(self):
		self.sort()
		print(self)
