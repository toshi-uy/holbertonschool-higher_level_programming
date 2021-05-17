#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except:
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return False
