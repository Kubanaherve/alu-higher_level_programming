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
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_id_mixed(self):
        b1 = Base()
        b2 = Base(50)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 50)
        self.assertEqual(b3.id, 2)

    def test_id_string(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        d = [{"id": 1, "width": 10}]
        result = Base.to_json_string(d)
        self.assertIsInstance(result, str)
        self.assertIn("width", result)

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        s = '[{"id": 1, "width": 10}]'
        result = Base.from_json_string(s)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["id"], 1)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        import os
        os.remove("Rectangle.json")

    def test_save_to_file(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content[0]["width"], 1)
        import os
        os.remove("Rectangle.json")

    def test_create_rectangle(self):
        r = Rectangle.create(id=1, width=10, height=2, x=3, y=4)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_create_square(self):
        s = Square.create(id=1, size=5, x=2, y=3)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_load_from_file_missing(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        r = Rectangle(5, 5)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].width, 5)
        import os
        os.remove("Rectangle.json")

    def test_square_save_load(self):
        s = Square(3)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].size, 3)
        import os
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
