#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for q in range(len(matrix)):
        new_matrix[q] = list(map(lambda x: x**2, matrix[q]))

    return (new_matrix)
