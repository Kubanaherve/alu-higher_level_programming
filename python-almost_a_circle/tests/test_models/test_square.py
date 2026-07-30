#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_constructor(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_default_values(self):
        s = Square(3)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_size_setter(self):
        s = Square(1)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_error(self):
        s = Square(1)
        with self.assertRaises(TypeError):
            s.size = "a"

    def test_size_value_error(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_update_args(self):
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_update_args_override_kwargs(self):
        s = Square(5)
        s.update(10, 2, size=7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(d, expected)

    def test_area(self):
        self.assertEqual(Square(4).area(), 16)

    def test_inherits_rectangle(self):
        from models.rectangle import Rectangle
        self.assertTrue(issubclass(Square, Rectangle))


if __name__ == "__main__":
    unittest.main()
