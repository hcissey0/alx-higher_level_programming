#!/usr/bin/python3
"""This is the Rectangle module"""

from .base import Base


class Rectangle(Base):
    """This is the Rectangle class and it inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The initializor function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The setter and getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter and setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter and setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This is the area function of the rectangle and returns the area"""
        return (self.width * self.height)

    def display(self):
        """Displays the rectangle with #'s"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """The update method of the Rectangle"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i == 5:
                    break
                setattr(self, attrs[i], arg)
        elif kwargs:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def __str__(self):
        """This is the string representation of the Rectangle"""
        name = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
        return name
