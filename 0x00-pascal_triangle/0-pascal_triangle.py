def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Build each row
    for i in range(1, n):
        # Start each row with '1'
        row = [1]
        
        # Fill in the middle elements by summing the two above elements
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End each row with '1'
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)

    return triangle

