import heapq

# Prim's Algorithm to find Minimum Spanning Tree (MST)
def prim_mst(graph):
    # Step 1: Initialize structures
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    mst_cost = 0
    mst_edges = []

    # Step 2: Process vertices
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        # Include edge in MST
        visited[u] = True
        mst_cost += weight
        mst_edges.append(u)

        # Step 3: Update the heap with adjacent edges
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return mst_cost, mst_edges
