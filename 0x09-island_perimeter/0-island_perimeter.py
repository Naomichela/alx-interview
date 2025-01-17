#!/usr/bin/python3
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Parameters:
    grid (list of list of int): A 2D list representing the grid where:
        - 0 represents water
        - 1 represents land

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract sides that are shared with adjacent land cells
                if row > 0 and grid[row - 1][col] == 1:  # Check above
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter

