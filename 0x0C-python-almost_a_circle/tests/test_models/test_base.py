#!/usr/bin/python3
"""This is the unittest cases for the Base class"""

import unittest
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
        self.assertEqual(len(Base.to_json_string(dict_list)), 104)

    def test_square_type(self):
        square = Square(4)
        self.assertIsInstance(Base.to_json_string([square.to_dictionary()]), str)

    def test_square_one(self):
        square = Square(4)
        self.assertEqual(len(Base.to_json_string([square.to_dictionary()])), 38)

    def test_square_two(self):
        square1 = Square(2)
        square2 = Square(3)
        list_dict = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dict)), 76)


if __name__ == "__main__":
    unittest.main()
