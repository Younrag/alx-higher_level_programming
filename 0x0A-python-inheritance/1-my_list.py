#!/usr/bin/python3
"""Module for stored list"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """Method for print stored"""
        print(sorted(self))
