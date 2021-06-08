#!/usr/bin/python3
"""
Unittest for base model
"""
import unittest
from models.base import Base
from models.Rectangle import Rectangle
from models.square import Square


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

    def test_list_as_id(self):
        """testing passing list as id"""
        b = Base([12])
        self.assertEqual(b.id, [12])
        """testing long list as id"""
        b = Base([1,2,3,4])
        self.assertEqual(b.id, [1,2,3,4])
        """testing empty list as id"""
        self.assertEqual(b.id, [])

    def test_string_as_id(self):
        """testing string as id"""
        self.assertEqual(b.id, "hola")

    def test_True(self):
        """testing True"""
        self.assertEqual(b.id, True)

if __name__ == '__main__':
    unittest.main()
