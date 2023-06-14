#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return
    if len(my_list) == 0:
        return 0
    res = 0
    div = 0
    for u, d in my_list:
        res += u * d
        div += d
    res /= div
    return res
