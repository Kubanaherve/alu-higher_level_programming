#!/usr/bin/python3
"""Unittests for Rectangle class."""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_constructor_defaults(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_constructor_with_x(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_constructor_with_xy(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_constructor_full(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_value_error_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_value_error_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_width_value_error_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_value_error_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_xy(self):
        r = Rectangle(2, 2)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        r = Rectangle(2, 2, 1)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display(self):
        r = Rectangle(2, 2, 1, 1)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertIn("id", d)
        self.assertIn("width", d)
        self.assertIn("height", d)
        self.assertIn("x", d)
        self.assertIn("y", d)

    def test_update_empty(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.id, 5)

    def test_update_id(self):
        r = Rectangle(1, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        r = Rectangle(1, 2)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_id_width_height(self):
        r = Rectangle(1, 2)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_id_width_height_x(self):
        r = Rectangle(1, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_all(self):
        r = Rectangle(1, 2)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_id(self):
        r = Rectangle(1, 2)
        r.update(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        r = Rectangle(1, 2)
        r.update(**{"id": 89, "width": 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(1, 2)
        r.update(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(1, 2)
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_all(self):
        r = Rectangle(1, 2)
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        r = Rectangle.create(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(r.x, 3)

    def test_create_all(self):
        d = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Rectangle.json")

    def test_save_to_file_with_data(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            data = json.loads(f.read())
        self.assertEqual(len(data), 1)
        import os
        os.remove("Rectangle.json")

    def test_load_from_file_nonexistent(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        import os
        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
