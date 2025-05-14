def floyd_warshall(graph):
    dist = [[float('inf')] * len(graph) for _ in range(len(graph))]

    # Initialize the distance matrix with graph values
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Floyd-Warshall algorithm
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Print the result
    print("All-pairs shortest path matrix:")
    for row in dist:
        print(["∞" if val == float('inf') else val for val in row])

# Example graph represented as an adjacency matrix
# 0 indicates no direct edge, except for the diagonal
graph = [
    [0, 3, 0, 5],
    [2, 0, 0, 4],
    [0, 1, 0, 0],
    [0, 0, 2, 0]
]

floyd_warshall(graph)
