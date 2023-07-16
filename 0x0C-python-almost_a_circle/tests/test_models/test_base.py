#!/usr/bin/python3
"""This is the unittest cases for the Base class"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_initialization(unittest.TestCase):
    """This is the unittest class for the base
    testing the initialization"""

    def test_one_arg_normal(self):
        """Test initialization with one argument"""
        b1 = Base(1)
        b2 = Base(5)
        self.assertEqual(1, b1.id)
        self.assertEqual(5, b2.id)

    def test_no_args(self):
        """Test without argument"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_objs(self):
        """Test to create 3 objects"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(12, b2.id)

    def test_two_args(self):
        """Passing two args"""
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_float(self):
        """Testing different types"""
        self.assertEqual(1.1, Base(1.1).id)

    def test_string(self):
        self.assertEqual("hello", Base("hello").id)

    def test_list(self):
        self.assertEqual([1, 2], Base([1, 2]).id)

    def test_set(self):
        self.assertEqual({1, 2}, Base({1, 2}).id)

    def test_dictionary(self):
        self.assertEqual({'h': 72, 'a': 95}, Base({'h': 72, 'a': 95}).id)

    def test_complex(self):
        self.assertEqual(complex(3), Base(complex(3)).id)

    def test_nan(self):
        import math
        self.assertTrue(math.isnan(Base(float('nan')).id))

    def test_infinity(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_tuple(self):
        self.assertEqual((2, 3), Base((2, 3)).id)

    def test_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_neg(self):
        self.assertEqual(-2, Base(-2).id)

    def test_byte(self):
        self.assertEqual(b'hello', Base(b'hello').id)

    def test_zero(self):
        self.assertEqual(0, Base(0).id)


class TestBaseToJSONString(unittest.TestCase):
    """The test cases for the to_json_string() function"""

    def test_normal(self):
        dct = {"a": 1, "b": 2, "c": 3}
        dct_string = '[{"a": 1, "b": 2, "c": 3}]'
        self.assertEqual(dct_string, Base.to_json_string([dct]))

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_0_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_rect_type(self):
        rect = Rectangle(2, 3)
        self.assertIsInstance(Base.to_json_string([rect.to_dictionary()]), str)

    def test_one_rect(self):
        rect = Rectangle(2, 4)
        self.assertEqual(len(Base.to_json_string([rect.to_dictionary()])), 52)

    def test_two_rect(self):
        rect1 = Rectangle(2, 4)
        rect2 = Rectangle(2, 3)
        dict_list = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(dict_list)), 106)

    def test_square_type(self):
        square = Square(4)
        self.assertIsInstance(Base.to_json_string(
            [square.to_dictionary()]), str)

    def test_square_one(self):
        square = Square(4)
        self.assertEqual(len(Base.to_json_string(
            [square.to_dictionary()])), 38)

    def test_square_two(self):
        square1 = Square(2)
        square2 = Square(3)
        list_dict = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dict)), 78)


class TestBaseSaveToFile(unittest.TestCase):
    """This is the test case class for the save_to_file() function"""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_Base_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_Rectangle_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_Square_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_Base_2_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], [])

    def test_Rectangle_2_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])

    def test_Square_2_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])

    def test_1_Square(self):
        square = Square(3)
        Square.save_to_file([square])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(),
                             Square.to_json_string([square.to_dictionary()]))

    def test_1_Rectangle(self):
        rect = Rectangle(4, 4)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(),
                             Rectangle.to_json_string([rect.to_dictionary()]))

    def test_2_square(self):
        square1 = Square(4)
        square2 = Square(5)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), Square.to_json_string(
                [square1.to_dictionary(), square2.to_dictionary()]))

    def test_2_rectangle(self):
        rect1 = Rectangle(4, 3)
        rect2 = Rectangle(3, 4)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), Rectangle.to_json_string(
                [rect1.to_dictionary(), rect2.to_dictionary()]))

    def test_none_square(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_none_Rectangle(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_none_Base(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual("[]", f.read())


if __name__ == "__main__":
    unittest.main()
