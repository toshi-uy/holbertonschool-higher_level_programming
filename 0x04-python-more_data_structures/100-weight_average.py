#!/usr/bin/python3
def weight_average(my_list=[]):
        if not my_list:
                return 0
        result = []
        div = 0
        final = 1.0
        for item in my_list:
                result.append(item[0] * item[1])
                div += item[1]
        final = sum(result) / div
        return final
