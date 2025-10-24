import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(edges: list[tuple], n: int):
    """
    Creates and displays a visualization of the undirected graph.
    """

    G = nx.Graph()  # Undirected Graph
    G.add_nodes_from(range(n))

    # Add edges with weights
    for s, d, w in edges:
        G.add_edge(s, d, weight=w)

    # Use a fixed layout for consistent drawing
    pos = nx.spring_layout(G, seed=42)

    # 1. Correct way to draw nodes: Use nx.draw_networkx_nodes
    nx.draw_networkx_nodes(
        G, pos,
        node_color='lightblue',
        node_size=1000,
        alpha=0.9
    )

    # 2. Correct way to draw edges: Use nx.draw_networkx_edges
    nx.draw_networkx_edges(G, pos, edge_color='gray')

    # 3. Draw labels (Node IDs and Edge Weights)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title(f"Undirected Graph with {n} Nodes")
    plt.axis('off')  # Hide the axis for a cleaner look
    plt.show()

