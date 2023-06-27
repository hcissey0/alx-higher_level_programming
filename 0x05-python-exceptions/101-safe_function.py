#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
    return res
