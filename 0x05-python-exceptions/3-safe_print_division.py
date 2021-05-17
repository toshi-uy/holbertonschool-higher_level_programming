#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except:
        return None
    finally:
        if c is not None:
            print("Inside result: {}".format(result))
