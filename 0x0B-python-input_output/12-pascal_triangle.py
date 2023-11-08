#!/usr/bin/python3

def facto(k):
    fact = 1
    for i in range(1, k):
        fact = fact * (i + 1)
    return fact


def pascal_triangle(n):
    L = []

    if n <= 0:
        return L
    else:
        for i in range(n):
            row = []
            for j in range(i):
                c = facto(i) / (facto(j) * facto(i - j))
                row.append(int(c))
            L.append(row)
        return L
