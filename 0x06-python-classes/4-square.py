#!/usr/bin/python3
"""Square"""


class Square:
    """Define Square"""
    def __init__(self, size=0):
        self.size = size

     @property
    def size(self):
        """Property for the length of a side squqre"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
