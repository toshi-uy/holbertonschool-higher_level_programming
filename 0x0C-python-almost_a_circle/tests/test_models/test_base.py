#!/usr/bin/python3
"""
Unittest for base model
"""
import unittest
from models.base import Base


class Test_Base_Model(unittest.TestCase):
    """test cases for base model"""

    def test_correctbase(self):
        """testing base with correct output"""
        b = Base(85)
        self.assertEqual(b.id, 85)
        b = Base(100)
        self.assertEqual(b.id, 100)
        """negative numbers"""
        b = Base(-45)
        self.assertEqual(b.id, -45)
        """None as id"""
        b = Base()
        self.assertEqual(b.id, 1)
        """Other None to test id increment"""
        b = Base()
        self.assertEqual(b.id, 2)
        """Other with text None to test function"""
        b = Base(None)
        self.assertEqual(b.id, 3)

    def test_too_many_args(self):
        """testing too many args"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)

if __name__ == '__main__':
    unittest.main()
