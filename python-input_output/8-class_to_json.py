#!/usr/bin/python3
"""Defines a JSON-to-class conversion function."""


def class_to_json(obj):
    """Return a dict description of an object for JSON serialization."""
    return obj.__dict__
