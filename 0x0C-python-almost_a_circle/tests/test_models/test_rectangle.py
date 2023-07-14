#!/usr/bin/python3
"""This is the unittest for the Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_initialization(unittest.TestCase):
    """This test the initialization of a rectangle"""

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_2_args(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(2, 3)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_3_args(self):
        rect1 = Rectangle(2, 1, 3)
        rect2 = Rectangle(2, 5, 4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_4_args(self):
        rect1 = Rectangle(2, 1, 3, 3)
        rect2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_5_args(self):
        rect = Rectangle(1, 2, 4, 5, 3)
        self.assertEqual(3, rect.id)


class TestRectangleWidth(unittest.TestCase):
    """This is the test case for With"""

    def test_private(self):
        rect = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            s = rect.__width

    def test_getter(self):
        rect = Rectangle(1, 3)
        self.assertEqual(1, rect.width)

    def test_setter(self):
        rect = Rectangle(1, 3)
        rect.width = 5
        self.assertEqual(rect.width, 5)

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)

    def test_int(self):
        self.assertEqual(Rectangle(1, 2).width, 1)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)
