#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''compute area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validating the value.'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''A subclass representing a rectangle.'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''String'''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        '''Returns area of rectangle.'''
        return self.__height * self.__width


class Square(Rectangle):
    '''A subclass representing a rectangle.'''
    def __init__(self, size):
        '''init'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''Method for area of square.'''
        return self.__size ** 2
