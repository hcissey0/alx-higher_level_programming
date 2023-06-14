#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list(my_list)
    for i, v in enumerate(new):
        if v == search:
            new[i] = replace
    return new
