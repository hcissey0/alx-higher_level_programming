#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The unit test for max_integer()"""

    def test_max_integer(self):
        self.assertTrue(len(max_integer.__doc__) > 1)
        self.assertEqual(max_integer([2, 4, 5, 6]), 6)
        self.assertEqual(max_integer([-2, -4, -1]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([i for i in range(300)]), 299)
        self.assertRaises(KeyError, max_integer, {'hi': 3})
        self.assertEqual(max_integer("abc"), 'c')
        self.assertRaises(TypeError, max_integer, 4)
        self.assertEqual(max_integer([4, 3, 2]), 4)
        self.assertEqual(max_integer([2, 5, 3]), 5)
        self.assertEqual(max_integer([5,]), 5)



if __name__ == '__main__':
    unittest.main()
