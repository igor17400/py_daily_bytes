###############
# Day 14: Number of Islands - My first solution
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

def grid_to_graph(grid: list[list[str]]) -> dict:
    if not grid or not grid[0]:
        return {}

    num_rows, num_cols = len(grid), len(grid[0])
    graph = {}

    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == '1':
                graph[(r, c)] = []
                neighbors = [ # Define neighbors
                    (r + 1, c),  # Down
                    (r - 1, c),  # Up
                    (r, c + 1),  # Right
                    (r, c - 1)  # Left
                ]

                for nei_row, nei_col in neighbors:
                    # Check if neighbor is within bounds and is land
                    if (
                            0 <= nei_row < num_rows and \
                            0 <= nei_col < num_cols and \
                            grid[nei_row][nei_col] == '1'
                    ):
                        graph[(r, c)].append((nei_row, nei_col))
    return graph


def find_connected_components(graph: dict[tuple[int, int], str]) -> None:
    visited = set()
    components = []

    def dfs(node, current_component):
        visited.add(node)
        current_component.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, current_component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    graph = grid_to_graph(grid)
    components = find_connected_components(graph)
    print(len(components))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    graph = grid_to_graph(grid)
    components = find_connected_components(graph)
    print(len(components))
