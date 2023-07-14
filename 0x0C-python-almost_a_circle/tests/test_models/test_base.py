#!/usr/bin/python3
"""This is the unittest cases for the Base class"""

import unittest
from models.base import Base


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

    def test_diff_types(self):
        """Testing different types"""
        self.assertEqual(1.1, Base(1.1).id)
        self.assertEqual("hello", Base("hello").id)
        self.assertEqual([1, 2], Base([1, 2]).id)
        self.assertEqual({1, 2}, Base({1, 2}).id)
        self.assertEqual({'h': 72, 'a': 95}, Base({'h': 72, 'a': 95}).id)


if __name__ == "__main__":
    unittest.main()
