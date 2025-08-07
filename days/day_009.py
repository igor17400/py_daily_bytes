###############
# Day 9: Breadth-First Search (BFS) - Shortest Paths
###############

"""
Goal:

Using an Adjacency List representation, let's see how to implement
BFS to find the shortest path between two nodes in an unweighted graph.
"""

###############
# Adjacency Lists - BFS
###############

from collections import deque


def bfs_shortest_path(graph, start, end): 
    """
    Finds the shortest path between start and end nodes using BFS.
    Returns a list of noded representing the path, or None if
    no path exists.
    """
    if start == end:
        return [start]

    queue = deque([start])
    visited = {start}
    predecessors = {start: None}  # To reconstruct the path

    while queue:
        current_node = queue.popleft()

        if current_node == end:
            # Path found! Reconstruct and return it
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = predecessors.get(current_node)
            return path[::-1]  # Reverse the path

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                predecessors[neighbor] = current_node  # Store predecessor

    return None  # No path found


if __name__ == "__main__":
    print("--- Breadth-First Search (BFS) for Shortest Path ---")

    adjacency_list = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D", "F"],
        "F": ["E"]
    }

    # Path from A to E should be A -> B -> D -> E (or A -> C -> D -> E)
    path1 = bfs_shortest_path(adjacency_list, "A", "E")
    print(f"Shortest path from A to E: {path1}")

    # Path from B to F
    path2 = bfs_shortest_path(adjacency_list, "B", "F")
    print(f"Shortest path from B to F: {path2}")

    # Path from A to G (doesn't exist)
    path3 = bfs_shortest_path(adjacency_list, "A", "G")
    print(f"Shortest path from A to G: {path3}")

    # Self-loop path
    path4 = bfs_shortest_path(adjacency_list, "A", "A")
    print(f"Path from A to A: {path4}")
