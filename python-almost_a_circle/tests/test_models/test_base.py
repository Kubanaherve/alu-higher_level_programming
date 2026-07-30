#!/usr/bin/python3
"""Unittests for Base class."""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_data(self):
        result = Base.to_json_string([{"id": 12}])
        self.assertIn("12", result)

    def test_to_json_string_returns_string(self):
        result = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_data(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result[0]["id"], 89)

    def test_from_json_string_returns_list(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)

    def test_create_rectangle_id(self):
        r = Rectangle.create(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_create_rectangle_id_width(self):
        r = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(r.width, 1)

    def test_create_rectangle_id_width_height(self):
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(r.height, 2)

    def test_create_rectangle_id_width_height_x(self):
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(r.x, 3)

    def test_create_rectangle_all(self):
        d = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.y, 4)

    def test_save_to_file_none_rectangle(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Rectangle.json")

    def test_save_to_file_empty_rectangle(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Rectangle.json")

    def test_save_to_file_rectangle(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            data = json.loads(f.read())
        self.assertEqual(len(data), 1)
        import os
        os.remove("Rectangle.json")

    def test_load_from_file_nonexistent_rectangle(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        import os
        os.remove("Rectangle.json")

    def test_save_to_file_none_square(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Square.json")

    def test_save_to_file_empty_square(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Square.json")

    def test_save_to_file_square(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            data = json.loads(f.read())
        self.assertEqual(len(data), 1)
        import os
        os.remove("Square.json")

    def test_load_from_file_nonexistent_square(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_square(self):
        s = Square(1)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        import os
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
