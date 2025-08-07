###############
# Day 10: Depth-First Search (DFS)
###############

"""
Goal: Understand how DFS is implemented
"""


def dfs(graph, start, visited=None):
    """Finds all reachable nodes from the start node using recursive DFS traversal.
    Returns a list of the nodes in the order they were visited."""
    if visited is None:
        visited = []

    visited.append(start)

    # Recursively visit neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


if __name__ == "__main__":
    print("--- Depth-First Search (DFS) ---")

    adjacency_list = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    reachable_nodes = dfs(adjacency_list, "A")
    print(f"Nodes reachable from A: {reachable_nodes}")

    reachable_nodes = dfs(adjacency_list, "E")
    print(f"Nodes reachable from E: {reachable_nodes}")
