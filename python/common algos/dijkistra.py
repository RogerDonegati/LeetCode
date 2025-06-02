# time complexity
# O((V+E)logV)

import heapq

def dijkstra(graph, target):
    min_heap = [(0, target)]
    distances = {node: float("inf") for node in graph}
    distances[target] = 0

    while min_heap:
        current_distance, node = heapq.heappop(min_heap)
        if current_distance > distances[node]: # this prevents the process from double checking higher values
            continue

        for sub_node, weight in graph[node].items():
            distance = weight + current_distance
            if distance < distances[sub_node]:
                distances[sub_node] = distance
                heapq.heappush(min_heap, (distance, sub_node))

    return distances


graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
    'R': {'F': 1},
}

print(dijkstra(graph, 'D'))
