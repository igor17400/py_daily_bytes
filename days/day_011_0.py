###############
# Day 11: Bipartite Graph
###############

"""
Goal: Understand the generic concept of Bipartite Graph
"""

from collections import deque


def is_bipartite(graph):
    """
    Checks if a graph is bipartite using a two-coloring BFS approach.
    Returns True if the graph is bipartite, False otherwise.
    """
    # A dictionary to share colors: 0 or 1. None for uncolored.
    color = {node: None for node in graph}

    # Iterate through all nodes to handle disconnected components
    for start_node in graph:
        if color[start_node] is None:
            # Start a new BFS from an uncolored node
            queue = deque([start_node])
            color[start_node] = 0  # Color the starting node 0

            while queue:
                u = queue.popleft()

                # Check neighbors
                for v in graph[u]:
                    if color[v] is None:
                        # Neighbor is uncolored, so color it with the opposite color
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        # A neighbor has the same color, so the graph is not bipartite
                        return False
    return True


if __name__ == "__main__":
    # Example of a bipartite graph
    bipartite_graph = {
        'U1': ['V1', 'V2'],
        'U2': ['V2', 'V3'],
        'U3': ['V1', 'V3'],
        'V1': ['U1', 'U3'],
        'V2': ['U1', 'U2'],
        'V3': ['U2', 'U3'],
    }

    # Example of a non-bipartite graph (contains a cycle of odd length)
    non_bipartite_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
    }

    print("--- Generic Bipartite Graph Example ---")
    print("Is the bipartite_graph bipartite?", is_bipartite(bipartite_graph))
    print("Is the non_bipartite_graph bipartite?", is_bipartite(non_bipartite_graph))
