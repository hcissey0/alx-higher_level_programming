#!/usr/bin/python3
"""this module contains a function 'text_indentation'
that indents a text
"""


def text_indentation(text):
    """this function indents a text
    Args:
        text (str): the text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    puncts = ".!?:;"
    spaces = "\n\t "
    for i in range(len(text)):
        if text[i] in puncts and text[i + 1] in puncts:
            continue
        if text[i + 1] in spaces:
            continue
        if text[i] in puncts:
            print(text[i])
            print()
        else:
            print(text[i], end="")
