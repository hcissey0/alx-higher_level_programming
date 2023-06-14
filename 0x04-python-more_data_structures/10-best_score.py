#!/usr/bin/python3
def best_score(a_dictionary):
    res = None
    if a_dictionary is not None:
        m = 0
        for k, v in a_dictionary.items():
            if v > m:
                m = v
                res = k
    return res
