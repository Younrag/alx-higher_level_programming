#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in range(len(matrix)):
        L = []
        for j in range(len(matrix[i])):
            L.append(matrix[i][j] ** 2)
        m.append(L)
    return m
