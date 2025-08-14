###############
# Day 13: Finding Connected Components in Undirected Graphs
###############

def find_connected_components_dfs(graph):
    """
    Finds all connected components in a undirected graph using DFS.

    Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
            Keys are nodes, and values are lists of their neighbors

    Returns:
        list: A list of lists, where each inner list is a connected component
    """
    visited = set()
    components = []

    def dfs(node, current_component):
        """Recursive DFS helper function"""
        visited.add(node)
        current_component.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, current_component)

    # Iterate through all nodes in the graph
    for node in graph:
        if node not in visited:
            # If node hasn't been visited, it's the start of a new component
            component = []
            dfs(node, component)
            components.append(component)

    return components


if __name__ == "__main__":
    # Example graph represented as adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        3: [4],
        4: [3],
        5: [],
    }

    print("Using Depth-First Search (DFS):")
    connected_components = find_connected_components_dfs(graph)
    print(f"The connected components are: {connected_components}")
