#!/usr/bin/python3
def weight_average(my_list=[]):
        if my_list is None:
                return 0
        result = []
        for item in my_list:
                result.append(item[0] * item[1])
        return result
