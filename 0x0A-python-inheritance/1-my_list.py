#!/usr/bin/pyhon3
""" Write a class MyList that inherits from list """

class MyList(list):
	def print_sorted(self):
		list1 = self.copy()
		print(list1.sort())
