#!/usr/bin/python3
"""triangle pascal with combinaision"""


def facto(k):
    """
    factorial n
    """
    fact = 1
    for i in range(1, k):
        fact = fact * (i + 1)
    return fact


def pascal_triangle(n):
    """Triangle Pascal"""
    L = []

    if n <= 0:
        return L
    else:
        for i in range(n):
            row = []
            for j in range(i + 1):
                c = facto(i) / (facto(j) * facto(i - j))
                row.append(int(c))
            L.append(row)
        return L
