#!/usr/bin/python3
"""Module for inherits_from"""


def inherits_from(obj, a_class):
    """is subclass"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
