#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new = list(my_list)
        for i, v in enumerate(new):
            if v == search:
                new[i] = replace
        return new
