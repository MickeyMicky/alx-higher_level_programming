#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of
    all integers of a matrix.
    """
    newMatrix = matrix.copy()
    
    for i in range(len(matrix)):
        newMatrix[i] = list(map(lambda x: x**2, matrix[i]))
        
    return newMatrix
