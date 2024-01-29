#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_el = []
        for el in row:
            new_el.append(el**2)
        new_matrix.append(new_el)
    return new_matrix
