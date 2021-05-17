#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
            return result
        else:
            print("Inside result: {}".format("None"))
            return result
