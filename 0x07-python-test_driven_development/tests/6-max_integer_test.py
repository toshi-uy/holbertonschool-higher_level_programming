#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test for positive numbers"""

    def test_positive(self):
        self.assertEqual(max_integer([1, 3, 90, 2]), 90)
    """test for negative numbers"""
    def test_negative(self):
        self.assertEqual(max_integer([-1, -4, -90, -100]), -1)
    def test_no_args(self):
        self.assertEqual(max_integer(), None)
    def test_no_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
