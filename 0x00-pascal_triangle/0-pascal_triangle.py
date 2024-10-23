#!/usr/bin/env python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Starting with the first row
    
    for i in range(1, n):
        row = [1]  # First element of the row is always 1
        prev_row = triangle[i - 1]
        
        # Calculate the in-between elements of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)  # Last element of the row is always 1
        triangle.append(row)
    
    return triangle

# Call the function and print the result
if __name__ == "__main__":
    from pprint import pprint  # Import to pretty-print the triangle
    pprint(pascal_triangle(5))  # Change 5 to the size of the triangle you want

