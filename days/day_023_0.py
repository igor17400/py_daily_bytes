from aux.visu_graphs import visualize_graph
import heapq

def shortest_path(edges: list[list[int]], n: int, src: int) -> list[int]:
    """
    :param edges: List of edges
    :param n: The total number of nodes
    :param src: Starting node
    :return: List of shortest paths
    """
    # ---- (1) Graph Initilization ----
    adj_list = [[] for _ in range(n)]

    # Populate the adjacency list
    for s, d, w in edges:
        # Correct the indes
        adj_list[s].append((d, w)) # Forward edge s -> d
        adj_list[d].append((s, w)) # Reverse edge d -> s

    # ---- (2) Dikjstra Code Logic ----
    shortest_dict = {}

    # Priority queue
    min_heap = [(0, src)]

    # Iterative process
    while min_heap:
        # Remember the min_heap can contain multiple entries with the same destination node
        d1, n1 = heapq.heappop(min_heap)

        if n1 in shortest_dict:
            continue
        shortest_dict[n1] = d1

        # Relaxation step
        for n2, w2 in adj_list[n1]:
            if n2 not in shortest_dict:
                new_dist = d1 + w2
                heapq.heappush(min_heap, (new_dist, n2))

    # Add unreachable nodes as infinity
    shortest_paths = {i: shortest_dict.get(i, float("inf")) for i in range(n)}
    return shortest_paths

nodes = 6
edges = [(0, 1, 8), (0, 2, 5), (2, 3, 12), (1, 3, 2), (3, 4, 4), (3, 5, 9), (4, 5, 4)] # Only forward edges
# Visualization might be useful to understand the problem
visualize_graph(edges, nodes)
shortest_paths = shortest_path(edges, nodes, 0)
print(shortest_paths)
