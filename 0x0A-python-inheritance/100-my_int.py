#!/usr/bin/python3
"""Class MyInt"""


class MyInt (int):
    """MyInt class"""
    def __new__(cls, *args, **kwargs):
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __ev__(self, other):
        """!= to =="""
        return int(self) != other

    def __pk__(self, other):
        """== to !="""
        return int(self) == other
