#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = [] * len(matrix)
    row_index = 0;
    for row in matrix:
        result_matrix[row_index] = [x * x for x in row]
        row_idex += 1
    return(result_matrix)
