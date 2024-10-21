#!/usr/bin/python3
"""
This module contains a function that returns Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of lists: A list containing lists of integers representing
        each row of Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle