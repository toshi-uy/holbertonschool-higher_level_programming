#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except:
        return None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
            return result
