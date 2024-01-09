#!/usr/bin/python3


import numpy


def lazy_matrix_mul(m_a, m_b):
    """calculates multiplication"""
    return numpy.matmul(m_a, m_b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
