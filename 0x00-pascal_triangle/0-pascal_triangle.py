#!/usr/bin/python3
"""
Pascal's Triangle Module.
This module contains a function that generates Pascal's Triangle up to a given number of rows.
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.
    
    Args:
        n (int): Number of rows to generate.
        
    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
