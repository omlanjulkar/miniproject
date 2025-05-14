# 10. Implement the Bellman-Ford algorithm

def bellman_ford(vertices, edges, source):
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Check for negative-weight cycles
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            print("Graph contains negative weight cycle")
            return

    print("Shortest distances from source:", distance)

vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('B', 'C', 3),
    ('A', 'C', 10),
    ('C', 'D', -10)
]
source = input("Enter source node for Bellman-Ford: ")
bellman_ford(vertices, edges, source)
