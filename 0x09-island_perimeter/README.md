# Island Perimeter Calculator

## Overview

The `island_perimeter` function calculates the perimeter of an island represented in a rectangular grid. Each cell in the grid can either be land (represented by `1`) or water (represented by `0`). The function efficiently determines the total perimeter of the island by examining adjacent land cells.

## Features

- **Input**: A 2D list representing the grid.
- **Output**: An integer representing the perimeter of the island.
- Handles grids with varying dimensions up to 100x100.
- Assumes there is only one island and no lakes.

## Function Definition

```python
def island_perimeter(grid):
    """Calculates the perimeter of an island represented in a grid.

    Args:
        grid (list of list of integers): A rectangular grid where 1 represents land
                                          and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
Parameters
grid: A list of lists containing integers (0s and 1s).
1 indicates land.
0 indicates water.
Returns
An integer representing the perimeter of the island.
Example Usage
python
Copy code
grid = [
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 16
Explanation
Initialization: The function initializes a variable to track the perimeter.
Traversal: It iterates through each cell in the grid.
Land Check: For each land cell, it assumes all four sides contribute to the perimeter.
Adjacent Land Check: The function checks adjacent cells to adjust the perimeter count.
Return Result: Finally, the computed perimeter is returned.
