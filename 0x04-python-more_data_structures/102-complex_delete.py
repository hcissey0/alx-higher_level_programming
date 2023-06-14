#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is not None:
        for k, v in dict(a_dictionary).items():
            if v == value:
                del a_dictionary[k]
        return a_dictionary
