#!/usr/bin/python3
"""Unittests for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_constructor(self):
        r = Rectangle(10, 20, 3, 4, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_default_values(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_setter(self):
        r = Rectangle(1, 1)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("a", 1)

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "a")

    def test_height_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "a")

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, "a")

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(5, 5).area(), 25)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1, width=2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 2)

    def test_update_args_override_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, id=99, width=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(d, expected)

    def test_display_no_offset(self):
        r = Rectangle(2, 2)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")


if __name__ == "__main__":
    unittest.main()
