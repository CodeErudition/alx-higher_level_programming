#!/usr/bin/python3
"""
This module defines a TestSquare class for Square unit tests.
"""
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    """Tests the Base class."""

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_Square_class(self):
        """Tests Square class type."""
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_Square_inheritance(self):
        """Tests if Square inherits Base."""
        self.assertTrue(issubclass(Square, Base))

    def test_Square_constructor_no_args(self):
        """Tests constructor signature."""
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_Square_constructor_many_args(self):
        """Tests constructor signature."""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
                were given"
        self.assertEqual(str(e.exception), s)

    def test_Square_instantiation(self):
        """Tests instantiation."""
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        error_msg = "width must be an integer"
        self.assertEqual(str(e.exception), error_msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        error_msg = "x must be an integer"
        self.assertEqual(str(e.exception), error_msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        error_msg = "y must be an integer"
        self.assertEqual(str(e.exception), error_msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        error_msg = "width must be > 0"
        self.assertEqual(str(e.exception), error_msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        error_msg = "x must be >= 0"
        self.assertEqual(str(e.exception), error_msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        error_msg = "y must be >= 0"
        self.assertEqual(str(e.exception), error_msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        error_msg = "width must be > 0"
        self.assertEqual(str(e.exception), error_msg)

    def test_Square_instantiation_positional(self):
        """Tests positional instantiation."""
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

    def test_Square_instantiation_keyword(self):
        """Tests positional instantiation."""
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_Square_id_inherited(self):
        """Tests if id is inherited from Base."""
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_Square_properties(self):
        """Tests property getters/setters."""
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    def invalid_types(self):
        """Returns tuple of types for validation."""
        in_type = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return in_type

    def test_Square_validate_type(self):
        """Tests property validation."""
        r = Square(1)
        attrs = ["x", "y"]
        for attr in attrs:
            s = "{} must be an integer".format(attr)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attr, invalid_type)
                    self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid_type)
                self.assertEqual(str(e.exception), s)

    def test_Square_validate_value_negative_gt(self):
        """Tests property validation."""
        r = Square(1, 2)
        attrs = ["size"]
        for attr in attrs:
            s = "width must be > 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -(randrange(10) + 1))
                self.assertEqual(str(e.exception), s)

    def test_Square_validate_value_negative_ge(self):
        """Tests property validation."""
        r = Square(1, 2)
        attrs = ["x", "y"]
        for attr in attrs:
            s = "{} must be >= 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -(randrange(10) + 1))
                self.assertEqual(str(e.exception), s)

    def test_Square_validate_value_zero(self):
        """Tests property validation."""
        r = Square(1, 2)
        attrs = ["size"]
        for attr in attrs:
            s = "width must be > 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, 0)
                self.assertEqual(str(e.exception), s)

    def test_Square_property(self):
        """Tests property setting/getting."""
        r = Square(1, 2)
        attrs = ["x", "y", "width", "height"]
        for attr in attrs:
            n = randrange(10) + 1
            setattr(r, attr, n)
            self.assertEqual(getattr(r, attr), n)

    def test_Square_property_range_zero(self):
        """Tests property setting/getting."""
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_Square_area_no_args(self):
        """Tests area() method signature."""
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_Square_area(self):
        """Tests area() method compuation."""
        r = Square(6)
        self.assertEqual(r.area(), 36)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, 7, 8, 9)
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * w)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_Square_display_no_args(self):
        """Tests display() method signature."""
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_Square_display_simple(self):
        """Tests display() method output."""
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
            ###\n\
            ###\n\
            ###\n\
            "
        self.assertEqual(f.getvalue(), s)
        r = Square(5, 6, 7)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
                #####
                #####
                #####
                #####
                #####
            """
        self.assertEqual(f.getvalue(), s)
        r = Square(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
                #########
                #########
                #########
                #########
                #########
                #########
                #########
                #########
                #########
            """
        self.assertEqual(f.getvalue(), s)
        r = Square(1, 1, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
                 #
            """
        self.assertEqual(f.getvalue(), s)

        r = Square(5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
                #####
                #####
                #####
                #####
                #####
            """
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
                #####
                #####
                #####
                #####
                #####
            """
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 3)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
                #####
                #####
                #####
                #####
                #####
            """
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
                #####
                #####
                #####
                #####
                #####
            """
        self.assertEqual(f.getvalue(), s)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = """\
                #####
                #####
                #####
                #####
                #####
            """
        self.assertEqual(f.getvalue(), s)

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        s = """\
                ##
                ##
            """
        self.assertEqual(f.getvalue(), s)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        s = """\
                ###
                ###
                ###
            """
        self.assertEqual(f.getvalue(), s)

    def test_Square_str_no_args(self):
        """Tests __str__() method signature."""
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_Square_str(self):
        """Tests __str__() method return."""
        r = Square(5)
        s = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(r), s)
        r = Square(1, 1)
        s = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(r), s)
        r = Square(3, 4, 5)
        s = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(r), s)
        r = Square(10, 20, 30, 40)
        s = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(r), s)

    def test_Square_update_no_args(self):
        """Tests update() method signature."""
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_Square_update_args(self):
        """Tests update() postional args."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(10, 5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_Square_update_args_bad(self):
        """Tests update() positional arg fubars."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(ValueError) as e:
            r.update(10, -5)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, -17)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, 17, -25)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_Square_update_kwargs(self):
        """Tests update() keyword args."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(size=17)
        d["_Rectangle__height"] = 17
        d["_Rectangle__width"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_Square_update_kwargs_2(self):
        """Tests update() keyword args."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

        r.update(y=25, id=10, x=20, size=5)
        self.assertEqual(r.__dict__, d)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_Square_to_dictionary(self):
        """Tests to_dictionary() signature"""
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Square(1)
        d = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(r.to_dictionary(), d)

        r = Square(9, 2, 3, 4)
        d = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.size = 30
        d = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(r.to_dictionary(), d)

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

if __name__ == "__main__":
    unittest.main()
