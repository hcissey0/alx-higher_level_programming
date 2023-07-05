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
    text = text.strip()
    puncts = ".?:"
    spaces = "\t "
    for c in puncts:
        text = text.replace(c, c + "\n\n")
    for c in range(len(text)):
        if c < len(text) and text[c] in spaces and text[c + 1] in spaces:
            text = text.replace(text[c:c + 2], text[c])
    for i, l in enumerate(text.split('\n')):
        if i == len(text.split("\n")) - 1:
            print(l.strip(), end="")
        else:
            print(l.strip())
