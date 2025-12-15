import heapq


def dijkstra(graph, start):

    distances = {v: float("inf") for v in graph}
    distances[start] = 0

    heap = [(0, start)]  # (distance, vertex)

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
    "D": [("B", 5), ("C", 8), ("E", 2)],
    "E": [("C", 10), ("D", 2)],
}

start_vertex = "A"
shortest_paths = dijkstra(graph, start_vertex)

for vertex, distance in shortest_paths.items():
    print(f"Відстань від {start_vertex} до {vertex}: {distance}")
