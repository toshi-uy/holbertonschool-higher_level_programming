#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    new.update({n: 2 * new[n] for n in new.keys()})
    return new
