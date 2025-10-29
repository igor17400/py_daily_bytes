# Problem: Swim in Rising Water
# Link: https://leetcode.com/problems/swim-in-rising-water/description/

import heapq


def swim_in_water(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # general variables
    rows = len(grid) - 1
    cols = len(grid[0]) - 1

    # -- Dikjstra
    min_paths = {}

    # initialize min heap
    src = (0, 0)
    min_heap = [(grid[0][0], src)]

    # move directions
    up = (0, - 1)
    down = (0, 1)
    left = (- 1, 0)
    right = (1, 0)
    moves = [up, left, down, right]

    while min_heap:
        d1, (n1_x, n1_y) = heapq.heappop(min_heap)

        if (n1_x, n1_y) in min_paths:
            continue
        min_paths[(n1_x, n1_y)] = d1

        for mv in moves:
            # Check for boundaries
            n2_x = n1_x + mv[0]
            n2_y = n1_y + mv[1]
            if (
                    (n2_x < 0 or n2_y < 0) or \
                    (n2_x > rows or n2_y > rows) or \
                    (n2_x > cols or n2_y > cols)
            ):
                continue

            # Checking minimum path
            if (n2_x, n2_y) not in min_paths:
                d_after_mv = grid[n2_x][n2_y]
                new_dist = max(d1, d_after_mv)
                heapq.heappush(min_heap, (new_dist, (n2_x, n2_y)))

    # Get last element from our array
    return min_paths[(rows, cols)]


if __name__ == '__main__':
    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(swim_in_water(grid))