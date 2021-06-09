#!/usr/bin/python3
"""
Unittest for Square model
"""
import unittest
import pep8
import json
import inspect
from models.base import Base
from models.square import Square
import io
import contextlib
import os


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseDocs(unittest.TestCase):
    """Base document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.rect_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_inheritance(self):
        """Testing inheritance"""
        Square.__nb_objects = 0
        self.assertEqual(issubclass(Square, Base), True)

    def test_object(self):
        """Testing object inheritance"""
        Square.__nb_objects = 0
        sq = Square(1, 1)
        self.assertEqual(isinstance(sq, Square), True)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)


class Test_Square(unittest.TestCase):
    """test cases for Square"""
    def test_too_many_args(self):
        """testing too many args"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError) as e:
            sq = Square(2, 4, 2, 4, 2, 2, 4)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 2 to 5 positional " +
            "arguments but 8 were given")

    @classmethod
    def setUpClass(cls):
        """setup class test"""
        Base._Base__nb_objects = 0
        cls.sq1 = Square(8, 8)
        cls.sq2 = Square(7, 2, 4)
        cls.sq3 = Square(9, 6, 7, 8)
        cls.sq4 = Square(11, 12, 13, 12)

    def test_rect_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.sq1.id, 1)
        self.assertEqual(self.sq2.id, 2)
        self.assertEqual(self.sq3.id, 8)
        self.assertEqual(self.sq4.id, 12)

    def test_size(self):
        """Test for functioning width"""
        self.assertEqual(self.sq1.size, 8)
        self.assertEqual(self.sq2.size, 7)
        self.assertEqual(self.sq3.size, 9)
        self.assertEqual(self.sq4.size, 11)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.sq1.x, 8)
        self.assertEqual(self.sq2.x, 2)
        self.assertEqual(self.sq3.x, 6)
        self.assertEqual(self.sq4.x, 12)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.sq1.y, 0)
        self.assertEqual(self.sq2.y, 4)
        self.assertEqual(self.sq3.y, 7)
        self.assertEqual(self.sq4.y, 13)

    def test_no_size(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            sq = Square()

    def test_size_noint(self):
        """Test for width error in type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square("string", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square(True, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square([9], 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square((2, 1), 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square(2.0, 1)

    def test_x_noint(self):
        """Test for x error in type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, "string")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, True, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, [9], 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, (2, 1), 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, 2.0)

    def test_y_noint(self):
        """Test for y error in type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1, 3, "string")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1, 3, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1, 3, [9])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1, 3, (2, 1))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1, 3, 2.0)

    def test_size_valueerror(self):
        """Test ints <= 0 for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(0, 1)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(1, 1, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.sq1.area(), 64)
        self.assertEqual(self.sq2.area(), 49)
        self.assertEqual(self.sq3.area(), 81)
        self.assertEqual(self.sq4.area(), 121)

    def test_area_too_many_args(self):
        """testing too many args in area module"""
        with self.assertRaises(TypeError):
            r = self.sq1.area(100)

    def test_display_method(self):
        """testing display method without x,y"""
        Base._Base__nb_objects = 0
        sq1 = Square(3, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            sq1.display()
        self.assertEqual(f.getvalue(), "###\n###\n###\n")

    def test_display_method_x(self):
        """testing display method with x"""
        Base._Base__nb_objects = 0
        sq1 = Square(3, 3, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            sq1.display()
        self.assertEqual(f.getvalue(), "   ###\n   ###\n   ###\n")

    def test_display_method_x_y(self):
        """testing display method with x"""
        Base._Base__nb_objects = 0
        sq1 = Square(3, 3, 3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            sq1.display()
        self.assertEqual(f.getvalue(), "\n\n\n   ###\n   ###\n   ###\n")

    def test___str__(self):
        """testing str"""
        sq1 = Square(4, 6, 2, 12)
        self.assertEqual(str(sq1), "[Square] (12) 6/2 - 4")

    def test_update_0(self):
        """testing update with args"""
        sq1 = Square(10, 2, 3, 8)
        sq1.update(89)
        self.assertEqual(str(sq1), "[Square] (89) 2/3 - 10")

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        s = Square(1, 0, 0, 1)
        with self.assertRaises(TypeError):
            s.update(1, "hello")
        with self.assertRaises(TypeError):
            s.update(1, 1, "hello")
        with self.assertRaises(TypeError):
            s.update(1, 1, 1, "hello")
        with self.assertRaises(ValueError):
            s.update(1, 0)
        with self.assertRaises(ValueError):
            s.update(1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, 1, -1)

    def test_update_too_many_args(self):
        """test too many args for update"""
        s = Square(1, 0, 0, 1)
        s.update(1, 1, 1, 1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_update_no_args(self):
        """test no args for update"""
        s = Square(1, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_update_kwargs(self):
        """Testing the update method with **kwargs"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=10)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        s.update(size=11, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 11")
        s.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(s), "[Square] (89) 5/3 - 4")

    def test_update_kwargs_setter(self):
        """tests that the update method uses setter with **kwargs"""
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.update(size="hello")
        with self.assertRaises(TypeError):
            s.update(x="hello")
        with self.assertRaises(TypeError):
            s.update(y="hello")
        with self.assertRaises(ValueError):
            s.update(size=-1)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-1)
        with self.assertRaises(ValueError):
            s.update(y=-1)

    def test_extra_kwargs(self):
        """tests for random kwargs"""
        s = Square(1, 0, 0, 1)
        s.update(hello=2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_save_to_file(self):
        """test regular use of save_to_file"""
        s1 = Square(1, 1, 1, 1)
        sq2 = Square(2, 2, 2, 2)
        l = [s1, sq2]
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            ls = [s1.to_dictionary(), sq2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_stf_empty(self):
        """test save_to_file with empty list"""
        l = []
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """test normal use of create"""
        s1 = {"id": 2, "size": 3, "x": 4, "y": 0}
        s2 = {"id": 9, "size": 6, "x": 7, "y": 8}
        s1c = Square.create(**s1)
        s2c = Square.create(**s2)
        self.assertEqual("[Square] (2) 4/0 - 3", str(s1c))
        self.assertEqual("[Square] (9) 7/8 - 6", str(s2c))
        self.assertIsNot(s1, s1c)
        self.assertIsNot(s2, s2c)
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)

    def test_load_from_filqe_no_file(self):
        """Checks use of load_from_file with no file"""
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        """Checks use of load_from_file with empty file"""
        try:
            os.remove("Square.json")
        except:
            pass
        open("Square.json", 'a').close()
        self.assertEqual(Square.load_from_file(), [])
