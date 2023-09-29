#!/usr/bin/python3
"""This is the algorithm to find the peak in a list"""


def find_peak(list_of_integers):
    """This function is used to find the peak"""
    if not list_of_integers:
        return None
    return sorted(list_of_integers)[-1]
