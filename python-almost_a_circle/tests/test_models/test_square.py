#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
import json
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_constructor(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_constructor_with_x(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_constructor_with_xy(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_constructor_full(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_value_error_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_size_value_error_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_str(self):
        s = Square(4, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 4")

    def test_area(self):
        self.assertEqual(Square(3).area(), 9)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertIn("id", d)
        self.assertIn("size", d)
        self.assertIn("x", d)
        self.assertIn("y", d)

    def test_update_empty(self):
        s = Square(1)
        s.update()
        self.assertEqual(s.id, 1)

    def test_update_id(self):
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_id_size(self):
        s = Square(1)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_id_size_x(self):
        s = Square(1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_all(self):
        s = Square(1)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_id(self):
        s = Square(1)
        s.update(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        s = Square(1)
        s.update(**{"id": 89, "size": 1})
        self.assertEqual(s.size, 1)

    def test_update_kwargs_id_size_x(self):
        s = Square(1)
        s.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_all(self):
        s = Square(1)
        s.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        s = Square.create(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{"id": 89, "size": 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        s = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(s.x, 2)

    def test_create_all(self):
        s = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Square.json")

    def test_save_to_file_with_data(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            data = json.loads(f.read())
        self.assertEqual(len(data), 1)
        import os
        os.remove("Square.json")

    def test_load_from_file_nonexistent(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        s = Square(1)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        import os
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
