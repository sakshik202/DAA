from collections import defaultdict

class TopologicalSortGraph:
    def __init__(self, vertices_count):
        self.graph = defaultdict(list)
        self.vertices_count = vertices_count

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True
        stack.append(vertex)
        i = 0
        while i < len(self.graph[vertex]):
            adjacent_vertex = self.graph[vertex][i]
            if not visited[adjacent_vertex]:
                self.topological_sort_util(adjacent_vertex, visited, stack)
            i += 1

    def topological_sort(self):
        visited = [False] * self.vertices_count
        stack = []
        vertex = 0
        while vertex < self.vertices_count:
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)
            vertex += 1
        return stack[::-1]

# Example :
topo_sort_graph = TopologicalSortGraph(6)
topo_sort_graph.add_edge(5, 2)
topo_sort_graph.add_edge(5, 0)
topo_sort_graph.add_edge(4, 0)
topo_sort_graph.add_edge(4, 1)
topo_sort_graph.add_edge(2, 3)
topo_sort_graph.add_edge(3, 1)
print("Topological Sort:", topo_sort_graph.topological_sort())

# solution for 2nd question
class DFSGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')
        i = 0
        while i < len(self.graph[vertex]):
            adjacent_vertex = self.graph[vertex][i]
            if not visited[adjacent_vertex]:
                self.dfs_util(adjacent_vertex, visited)
            i += 1

    def dfs(self, start_vertex):
        visited = [False] * (max(self.graph) + 1)
        self.dfs_util(start_vertex, visited)

# Example :
dfs_graph = DFSGraph()
dfs_graph.add_edge(0, 1)
dfs_graph.add_edge(0, 2)
dfs_graph.add_edge(1, 2)
dfs_graph.add_edge(2, 0)
dfs_graph.add_edge(2, 3)
dfs_graph.add_edge(3, 3)
print("\nDFS from vertex 2:")
dfs_graph.dfs(2)

# solution for 3rd question
class KruskalGraph:
    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.edges = []

    def add_edge(self, start, end, weight):
        self.edges.append([start, end, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []
        i, edge_count = 0, 0
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = list(range(self.vertices_count))
        rank = [0] * self.vertices_count

        while edge_count < self.vertices_count - 1 and i < len(self.edges):
            u, v, weight = self.edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                edge_count += 1
                result.append([u, v, weight])
                self.union(parent, rank, x, y)

        print("Edges in the constructed MST:")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))

# Example :
kruskal_graph = KruskalGraph(4)
kruskal_graph.add_edge(0, 1, 10)
kruskal_graph.add_edge(0, 2, 6)
kruskal_graph.add_edge(0, 3, 5)
kruskal_graph.add_edge(1, 3, 15)
kruskal_graph.add_edge(2, 3, 4)
kruskal_graph.kruskal()
