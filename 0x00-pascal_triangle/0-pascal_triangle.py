#!/usr/bin/python3

def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.
                  Must be a non-negative integer.

    Returns:
        list: A list of lists, where each inner list represents a row
              of Pascal's triangle. Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []  # Return an empty list for non-positive n

    triangle = [[1]]  # The first row of Pascal's triangle

    for i in range(1, n):
        row = [1]  # Each row starts with 1
        for j in range(1, i):
            # Calculate the value as the sum of the two elements directly above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)  # Add the row to the triangle

    return triangle  # Return the complete triangle

