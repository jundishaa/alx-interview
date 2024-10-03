#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.
    
    Args:
        n (int): The number of rows of Pascal's triangle to generate.
    
    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    # Check for the edge case where n is less than or equal to 0
    if n <= 0:
        return []

    triangle = []  # Initialize the triangle list

    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)
        # Each triangle element (except the first and last) is the sum of the two above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Append the current row to the triangle

    return triangle

