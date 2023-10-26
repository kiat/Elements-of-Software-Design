from collections import defaultdict

def bellman_ford(graph, source):
    # Step 1: Initialize distances to all vertices as infinity and the source vertex to 0
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Step 2: Relax all edges |V| - 1 times, where |V| is the number of vertices
    vertices = list(graph.keys())
    num_vertices = len(vertices)

    for _ in range(num_vertices - 1):
        for vertex in vertices:
            for neighbor, weight in graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Step 3: Check for negative weight cycles
    for vertex in vertices:
        for neighbor, weight in graph[vertex]:
            if distances[vertex] + weight < distances[neighbor]:
                print("Graph contains negative weight cycle")
                return

    return distances

# Your graph representation
graph = defaultdict(list)
graph[0] = [(1, 11), (2, 5)]
graph[1] = [(3, 2)]
graph[2] = [(1, 4), (3, 6)]
graph[3] = []

source_vertex = 0
shortest_distances = bellman_ford(graph, source_vertex)

# Print the shortest distances from the source vertex to all other vertices
for vertex, distance in shortest_distances.items():
    print(f"Shortest distance from {source_vertex} to {vertex} is {distance}")
