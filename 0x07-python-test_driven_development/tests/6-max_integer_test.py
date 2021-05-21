#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test cases for function max_integer"""

    """test for positive numbers"""
    def test_positive(self):
        self.assertEqual(max_integer([1, 3, 90, 2]), 90)
    """test for negative numbers"""
    def test_negative(self):
        self.assertEqual(max_integer([-1, -4, -90, -100]), -1)
    """test for no arguments"""
    def test_no_args(self):
        self.assertEqual(max_integer(), None)
    """test for empty list"""
    def test_no_list(self):
        self.assertEqual(max_integer([]), None)
    """test for True as argument"""
    def test_True(self):
        with self.assertRaises(TypeError):
            max_integer(True)
    """test for None"""
    def test_None(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    """test for list with None"""
    def test_list_None(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 3])
    """test for disctionary as list"""
    def test_dict(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3})
    """test for list with string"""
    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "string", 3])
    """test for list with zero as max"""
    def test_zeromax(self):
        self.assertEqual(max_integer([-1, -3, -199, 0]), 0)

if __name__ == '__main__':
    unittest.main()
