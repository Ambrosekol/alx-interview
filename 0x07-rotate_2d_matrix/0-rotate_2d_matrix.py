#!/usr/bin/python3
"""
Rotating a 2d matrix in place
"""


def rotate_2d_matrix(matrix):
    length = len(matrix)

    # transpose matrix
    for x in range(length):
        for y in range(x, length):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
    # reverse the matrix
    for rows in matrix:
        rows.reverse()
