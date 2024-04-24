#!/usr/bin/python3
"""
 Rotates a 2D matrix 90 degrees clockwise in-place.
"""
def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): A 2D list of integers

    Returns:
        None
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

