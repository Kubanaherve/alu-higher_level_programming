#!/usr/bin/python3
"""Defines the Base class for all project models.

This module provides the Base class that manages unique id
attributes and offers JSON serialization and deserialization
methods, file persistence, and instance creation from dictionaries.
"""
import json


class Base:
    """Base class that manages id for all subclasses.

    Serves as the foundation for Rectangle and Square classes,
    providing automatic id assignment, JSON serialization,
    file I/O, and instance creation from dictionaries.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance.

        Args:
            id: Optional integer id. If None, auto-incremented id is used.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries: List of dictionaries.

        Returns:
            str: JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string: JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of instances to a JSON file.

        Args:
            list_objs: List of instances inheriting from Base.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(Base.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """Create an instance from a dictionary.

        Args:
            **dictionary: Dictionary of attribute values.

        Returns:
            Base: Instance with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                dicts = Base.from_json_string(f.read())
            return [cls.create(**d) for d in dicts]
        except FileNotFoundError:
            return []
