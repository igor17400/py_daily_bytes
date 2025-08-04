###############
# Day 8: Representing Graphs
###############

"""
Goal:

Given a small, directed graph, demonstrate how to represent it using both an
Adjacency Matrix and an Adjacency List, and show a simple operation
(checking for an edge) on each.
"""

###############
# Adjacency Lists
###############

nodes = ["A", "B", "C", "D"]

# Initialize a dictionary with empty lists for each node
adjacency_list = {node: [] for node in nodes}

# Add the edge to the list
edges = [("A", "B"), ("A", "C"), ("C", "B"), ("C", "D")]

for u, v in edges:
    adjacency_list[u].append(v)


def check_edge_list(u, v):
    if u not in adjacency_list:
        return False
    return v in adjacency_list[u]


if __name__ == "__main__":
    print("\n--- Adjacency List Representation ---")
    print(adjacency_list)

    print("\nCheck for edges:")
    print(f"Is there an edge from A to B? {check_edge_list('A', 'B')}")
    print(f"Is there an edge from C to D? {check_edge_list('C', 'D')}")
    print(f"Is there an edge from B to A? {check_edge_list('B', 'A')}")
