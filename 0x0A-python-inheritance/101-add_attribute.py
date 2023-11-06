#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.
    Args:
        obj: The object to add an attribute to.
        att: The name of the attribute to add to obj.
        value: The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
