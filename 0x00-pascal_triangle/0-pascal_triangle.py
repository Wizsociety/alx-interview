#!/usr/bin/python3
"""
Pascal's Triangle function that generates the triangle up to n levels
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n levels.
    Arguments:
    n -- number of rows in the triangle
    Returns:
    A list of lists representing Pascal's Triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row
    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])  # Compute the inner elements
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    n = 5  # Test case; modify as needed
    for row in pascal_triangle(n):
        print([int(x) for x in row])  # This ensures the correct format with no extra spaces or commas

