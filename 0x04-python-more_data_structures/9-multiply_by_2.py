#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new = dict(a_dictionary)
        for k, v in new.items():
            new[k] *= 2
        return new
