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
# Adjacency Matrix
###############

nodes = ["A", "B", "C", "D"]
num_nodes = len(nodes)

# A dictionary to map node names to their index
node_to_index = {node: i for i, node in enumerate(nodes)}

# Initialize a matrix of zeros
adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

# Add the edges to the matrix
edges = [("A", "B"), ("A", "C"), ("C", "B"), ("C", "D")]

for u, v, in edges:
    u_index = node_to_index[u]
    v_index = node_to_index[v]
    adjacency_matrix[u_index][v_index] = 1

def check_edge_matrix(u, v):
    u_index = node_to_index.get(u)
    v_index = node_to_index.get(v)

    if u_index is None or v_index is None:
        return False

    return adjacency_matrix[u_index][v_index] == 1

if __name__ == "__main__":
    print("--- Adjacency Matrix Representation ---")
    print("Node to Index Map:", node_to_index)
    for row in adjacency_matrix:
        print(row)

    print("\nCheck for edges:")
    print(f"Is there an edge from A to B? {check_edge_matrix('A', 'B')}")
    print(f"Is there an edge from C to D? {check_edge_matrix('C', 'D')}")
    print(f"Is there an edge from B to A? {check_edge_matrix('B', 'A')}")
