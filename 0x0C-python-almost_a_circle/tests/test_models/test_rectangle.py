#!/usr/bin/python3
"""
Unittest for Rectangle model
"""
import unittest
import pep8
import json
import inspect
from models.base import Base
from models.rectangle import Rectangle
import io
import contextlib


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py',
                                        'models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseDocs(unittest.TestCase):
    """Base document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_inheritance(self):
        """Testing inheritance"""
        Rectangle.__nb_objects = 0
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_object(self):
        """Testing object inheritance"""
        Rectangle.__nb_objects = 0
        r1 = Rectangle(1, 1)
        self.assertEqual(isinstance(r1, Rectangle), True)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class Test_Rectangle(unittest.TestCase):
    """test cases for rectangle"""
