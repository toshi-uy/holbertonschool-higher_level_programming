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
import os


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

    def test_too_many_args(self):
        """testing too many args"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 4, 2, 4, 2, 2, 4)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 3 to 6 positional " +
            "arguments but 8 were given")

    @classmethod
    def setUpClass(cls):
        """setup class test"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(8, 8)
        cls.r2 = Rectangle(7, 2, 4)
        cls.r3 = Rectangle(9, 6, 7, 8, 11)
        cls.r4 = Rectangle(11, 12, 13, 12)

    def test_rect_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 11)
        self.assertEqual(self.r4.id, 3)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.width, 8)
        self.assertEqual(self.r2.width, 7)
        self.assertEqual(self.r3.width, 9)
        self.assertEqual(self.r4.width, 11)

    def test_height(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.height, 8)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r3.height, 6)
        self.assertEqual(self.r4.height, 12)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 13)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 12)

    def test_no_width(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_no_height(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            r = Rectangle(8)

    def test_width_noint(self):
        """Test for width error in type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("string", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([9], 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((2, 1), 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(2.0, 1)

    def test_height_noint(self):
        """Test for height error in type"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "string")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [9])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (2, 1))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, 2.0)

    def test_x_noint(self):
        """Test for x error in type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, "string")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, True, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, [9], 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, (2, 1), 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, 2.0)

    def test_y_noint(self):
        """Test for y error in type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, "string")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, [9])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, (2, 1))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, 2.0)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """test area module"""
        self.assertEqual(self.r1.area(), 64)
        self.assertEqual(self.r2.area(), 14)
        self.assertEqual(self.r3.area(), 54)
        self.assertEqual(self.r4.area(), 132)

    def test_area_too_many_args(self):
        """testing too many args in area module"""
        with self.assertRaises(TypeError):
            r = self.r1.area(100)

    def test_display_method(self):
        """testing display method without x,y"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 3, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "###\n###\n###\n")

    def test_display_method_x(self):
        """testing display method with x"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 3, 3, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "   ###\n   ###\n   ###\n")

    def test_display_method_x_y(self):
        """testing display method with x"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 3, 3, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n   ###\n   ###\n   ###\n")

    def test___str__(self):
        """testing str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_0(self):
        """testing update with args"""
        r1 = Rectangle(10, 10, 10, 10, 8)
        r1.update(20, 100)
        self.assertEqual(self.r1.id, 20)
        self.assertEqual(self.r1.width, 100)
        r1.update(7, 100, 80)
        self.assertEqual(self.r1.id, 7)
        self.assertEqual(self.r1.width, 100)
        self.assertEqual(self.r1.height, 80)

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_update_1(self):
        """testing update with kwars"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10, 2)
        r1.update(x=1, height=2, y=3, width=30)
        self.assertEqual(self.r1.width, 30)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 3)

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_setter(self):
        """tests that the update method uses setter with **kwargs"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.update(width="hello")
        with self.assertRaises(TypeError):
            r.update(height="hello")
        with self.assertRaises(TypeError):
            r.update(x="hello")
        with self.assertRaises(TypeError):
            r.update(y="hello")
        with self.assertRaises(ValueError):
            r.update(width=-1)
        with self.assertRaises(ValueError):
            r.update(width=0)
        with self.assertRaises(ValueError):
            r.update(height=-1)
        with self.assertRaises(ValueError):
            r.update(height=0)
        with self.assertRaises(ValueError):
            r.update(x=-1)
        with self.assertRaises(ValueError):
            r.update(y=-1)

    def test_args_and_kwargs(self):
        """testing passing args and kwargs in update"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r1), "[Rectangle] (2) 2/2 - 2/2")

    def test_unknown_kwarg(self):
        """tests for random kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(hello=2)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
