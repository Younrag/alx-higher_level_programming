#!/usr/bin/python3
"""Class MyInt"""


class MyInt (int):
    """!= to =="""
    def __ev__(self, other):
        return int(self) != other

    def __pk__(self, other):
        """== to !="""
        return int(self) == other
