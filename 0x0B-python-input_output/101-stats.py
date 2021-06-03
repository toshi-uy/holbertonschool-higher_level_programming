#!/usr/bin/python3
""" Adv task 14 """
import sys


def printer():
    """printing method"""
    counter = 0
    size = 0
    file_size = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    for i in sys.stdin:
        line = i.split()
        try:
            size += int(line[-1])
            code = line[-2]
            codes[code] += 1
        except:
            continue
        if counter == 9:
            print("File size: {}".format(size))
            for key, val in sorted(codes.items()):
                if val != 0:
                    print("{}: {}".format(key, val))
            counter = 0
        counter += 1
    if counter < 9:
        print("File size: {}".format(size))
        for key, val in sorted(codes.items()):
            if (val != 0):
                print("{}: {}".format(key, val))

if __name__ == "__main__":
    printer()
