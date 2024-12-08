def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
        grid (list of list of int): 2D list where 0 represents water and 1 represents land.
        
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for the land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell (shared edge)
                if row > 0 and grid[row - 1][col] == 1:  # Check the cell above
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check the cell to the left
                    perimeter -= 2

    return perimeter

