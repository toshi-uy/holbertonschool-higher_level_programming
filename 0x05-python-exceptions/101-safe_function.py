#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {0}".format(err), file=sys.stderr)
        return None
