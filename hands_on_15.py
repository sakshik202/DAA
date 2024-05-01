import heapq

# solution for 1
def custom_dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        neighbor_edges = graph[current_node].items()
        neighbor_edges_iter = iter(neighbor_edges)
        while True:
            try:
                neighbor, weight = next(neighbor_edges_iter)
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
            except StopIteration:
                break
    
    return distances

# Example graph
custom_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1, 'E': 7},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'C': 7, 'D': 3}
}

start_node = 'A'
print("Shortest distances from node", start_node, ":", custom_dijkstra(custom_graph, start_node))

# solution for 2
def custom_bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    num_nodes = len(graph)
    i = 0
    while i < num_nodes - 1:
        i += 1
        for node in graph:
            neighbor_edges = graph[node].items()
            for neighbor, weight in neighbor_edges:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
   
    for node in graph:
        neighbor_edges = graph[node].items()
        for neighbor, weight in neighbor_edges:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative cycle")
    
    return distances

# Example graph
custom_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': -1, 'D': 5},
    'C': {'A': 2, 'D': 1, 'E': 7},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'C': 7, 'D': 3}
}

start_node = 'A'
print("Shortest distances from node", start_node, ":", custom_bellman_ford(custom_graph, start_node))

# solution for 3
def custom_floyd_warshall(graph):
    distances = {node: {v: float('inf') for v in graph} for node in graph}
    for node in graph:
        distances[node][node] = 0
    
    for u in graph:
        for v in graph[u]:
            distances[u][v] = graph[u][v]
    
    k = 0
    while k < len(graph):
        k += 1
        for i in graph:
            for j in graph:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    return distances

# Example graph
custom_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1, 'E': 7},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'C': 7, 'D': 3}
}

print("Shortest distances between all pairs:")
source_iter = iter(custom_graph)
while True:
    try:
        source = next(source_iter)
        distances = custom_floyd_warshall(custom_graph)
        print(f"From node {source}: {distances[source]}")
    except StopIteration:
        break
