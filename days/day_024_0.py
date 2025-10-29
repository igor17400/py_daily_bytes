# Problem: Path With Maximum Probability
# URL: https://leetcode.com/problems/path-with-maximum-probability/description/

import heapq

def max_probability(n, edges, succ_prob, start_node, end_node):
    """
    :type n: int
    :type edges: List[List[int]]
    :type succ_prob: List[float]
    :type start_node: int
    :type end_node: int
    :rtype: float
    """
    max_prob_lst = {}

    # Build the adjacency list - aka graph
    graph = [[] for _ in range(n)]
    for i, edge in enumerate(edges):
        graph[edge[0]].append((edge[1], succ_prob[i]))  # forward edge
        graph[edge[1]].append((edge[0], succ_prob[i]))  # backward edge

    # Priority queue - we want to get the biggest element instead of the smallest
    max_heap = [(-1, start_node)]

    while max_heap:
        p1, n1 = heapq.heappop(max_heap)

        if n1 in max_prob_lst:
            continue
        max_prob_lst[n1] = p1

        # Relaxation step
        for n2, p2 in graph[n1]:
            if n2 not in max_prob_lst:
                new_prob = p1 * p2
                # making sure our prob stays negative
                news_prob = new_prob if new_prob > 0 else (-1) * new_prob
                heapq.heappush(max_heap, (new_prob, n2))

    # Now we have a list with source and respective prob to each node
    output = max_prob_lst[end_node] if end_node in max_prob_lst else 0
    return (-1) * output

if __name__ == "__main__":
    print("--- Test 1 ---")
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succ_prob = [0.5, 0.5, 0.2]
    start_node = 0
    end_node = 2
    print(max_probability(n, edges, succ_prob, start_node, end_node))