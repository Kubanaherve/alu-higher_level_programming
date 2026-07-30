#!/usr/bin/python3
"""Defines the Square class which inherits from Rectangle.

This module provides the Square class with size attribute,
positioning, area calculation, display, and serialization.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a special case of Rectangle.

    Attributes:
        size: Side length of the square (positive integer).
        x: X offset for positioning (non-negative integer).
        y: Y offset for positioning (non-negative integer).
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance.

        Args:
            size: Size of square (width and height).
            x: X offset.
            y: Y offset.
            id: Optional integer id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size (width and height) with validation."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Update attributes with args/kwargs.

        Args:
            *args: No-keyword arguments (id, size, x, y).
            **kwargs: Key-worded arguments.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
