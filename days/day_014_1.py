###############
# Day 14: Number of Islands - Ideal Solution
###############

"""
From Leetcode.

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


def num_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0])
    num_islands = 0

    def dfs(row, col):
        if (
                row < 0 or row >= num_rows or \
                col < 0 or col >= num_cols or \
                grid[row][col] == "0"
        ):
            return

        # Mark the current cell as visited by "sinking it"
        grid[row][col] = "0"

        # Recursively call dfs for all the adjacency cells
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for r in range(num_rows):
        for c in range(num_cols):
            # If we find a land cell, we've discovered an island
            if grid[r][c] == "1":
                num_islands += 1
                dfs(r, c)  # Explore and sink the entire island

    return num_islands


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(num_islands(grid))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(num_islands(grid))
