def island_perimeter(grid):
    """Calculates the perimeter of an island represented in a grid.

    Args:
        grid (list of list of integers): A rectangular grid where 1 represents land
                                          and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0
    
    perimeter = 0
  
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:  
                perimeter += 4
                
                if r > 0 and grid[r - 1][c] == 1: 
                    perimeter -= 1
                if r < len(grid) - 1 and grid[r + 1][c] == 1: 
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1: 
                    perimeter -= 1
                if c < len(grid[0]) - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1

    return perimeter