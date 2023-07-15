#!/usr/bin/python3
"""This is the Square Module"""

from .rectangle import Rectangle


class Square(Rectangle):
    """This is the square class that inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the initializor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The getter and setter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This is the update method of the square class"""
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i == 4:
                    break
                setattr(self, attrs[i], arg)
        elif kwargs:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def __str__(self):
        """The string representation of the Square class"""
        name = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
        return name

    def to_dictionary(self):
        """Returns the dictionary representation of the square"""
        res = {"id": self.id,
               "size": self.id,
               "x": self.x,
               "y": self.y
               }
        return res
