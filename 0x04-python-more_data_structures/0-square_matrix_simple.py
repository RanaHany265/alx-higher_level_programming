#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to compute the square value of all integers of a matrix
#
# (C) 2023 EGYPT
# email ranahanymohamed265@gmail.com
# -----------------------------------------------------------


def square_matrix_simple(matrix=[]):
    new_matrix = [[number**2 for number in row] for row in matrix]
    return new_matrix
