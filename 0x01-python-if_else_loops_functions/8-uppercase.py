#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("")
