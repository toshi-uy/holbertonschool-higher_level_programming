#!/usr/bin/python3
"""
Unittest for base model
"""
import unittest
import pep8
import inspect
import json
from models.base import Base


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py',
                                        'models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseDocs(unittest.TestCase):
    """Base document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(Base.__doc__) >= 1)


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
        b = Base([1, 2, 3, 4])
        self.assertEqual(b.id, [1, 2, 3, 4])
        """testing empty list as id"""
        b = Base([])
        self.assertEqual(b.id, [])

    def test_string_as_id(self):
        """testing string as id"""
        b = Base("hola")
        self.assertEqual(b.id, "hola")

    def test_True(self):
        """testing True"""
        b = Base(True)
        self.assertEqual(b.id, True)

    def test_accesing_nb(self):
        """testing trying to access and print the nb"""
        b = Base(10)
        with self.assertRaises(AttributeError):
            print(self.nb_objects)

    def test_accesing__nb(self):
        """testing trying to access and print the __nb"""
        b = Base(10)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

class JSON_Tests(unittest.TestCase):
    """Tests of Json"""

    def test_to_json_string(self):
        """Basic test of Json string"""
        Base._Base__nb_objects = 0
        dic1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        dic2 = {'x': 5, 'width': 8, 'id': 2, 'height': 9, 'y': 9}
        json_s = Base.to_json_string([dic1, dic2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [dic1, dic2])

    def test_empty_to_json_string(self):
        """Test empty dictionary"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        """None as dictionary"""
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_fjs_None(self):
        """test None from Json string"""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string(self):
        """testing from Json string"""
        list_input = "[{'id': 89, 'width': 10, 'height': 4, 'x': 7, 'y': 9}, \
            {'id': 7, 'width': 1, 'height': 7, 'x': 4, 'y': 0}]"
        json_l = Base.from_json_string(list_input)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 89, "width": 10, "height": 4, "x": 7, "y": 9})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})       

if __name__ == '__main__':
    unittest.main()
