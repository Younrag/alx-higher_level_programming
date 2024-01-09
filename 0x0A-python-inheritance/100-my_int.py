#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """Class func"""
    def __new__(cls, *args, **kwargs):
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
