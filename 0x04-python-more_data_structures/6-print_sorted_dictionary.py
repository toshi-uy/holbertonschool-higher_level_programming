#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for elem in sorted(a_dictionary.items()):
        print("{}: {}".format(elem[0], elem[1]))
