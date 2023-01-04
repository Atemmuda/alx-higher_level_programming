#!/usr/bin/python3
"""Module containing function to generate new list (new_list) pf numbers
that are as a result of previous list (my_list) divided by a a number (div)
"""


def divide_list(matrix, div):
    """function that divides a given matrix with the given div integer.

    Args:
        matrix (list): List of integers or float forming a matrix
        div (int or float): value to divide the elements in the  list

    Returns:
        list: new elements which results from dividing each element of
        the matrix with div
    """
    error_message = 'matrix must be a matrix (list of lists)'
    'of integers/floats'
    if type(matrix) is not list:
        raise TypeError(error_message)
    row_len = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_message)
        row_len.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_message)
        row_count += 1
    if len(set(row_len)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    new_list = list(map(lambda row: list(map(lambda x:
                    round(float(x) / div, 2), row)), matrix))
    return new_list

