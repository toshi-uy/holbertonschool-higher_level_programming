#!/usr/bin/python3
""" Task One """


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename) as f:
            for line in f:
                print(line, end="")
