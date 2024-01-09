#!/usr/bin/python3
"""Module for lookup"""


def lookup(obj):
    """Looks up object.
    Args:
        obj: the object to list.

    Returns:
        list: list of attributes.
    """
    return dir(obj)
