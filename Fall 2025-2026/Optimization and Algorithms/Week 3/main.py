from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)  # Adjacency list

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # For undirected graph

    # DFS Traversal
    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        print("DFS traversal:")
        visited = [False] * self.V
        self.dfs_util(start, visited)
        print()

    # BFS Traversal
    def bfs(self, start):
        print("BFS traversal:")
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

    # Connectivity check (using DFS)
    def is_connected(self):
        visited = [False] * self.V
        self.dfs_util(0, visited)
        return all(visited)

    # Shortest path using BFS (unweighted)
    def shortest_path(self, start, end):
        visited = [False] * self.V
        prev = [-1] * self.V
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            if node == end:
                break
            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    prev[neighbor] = node
                    queue.append(neighbor)

        # Reconstruct path
        path = []
        at = end
        while at != -1:
            path.append(at)
            at = prev[at]
        path.reverse()
        return path if path[0] == start else []

# Example usage:
if __name__ == "__main__":
    g = Graph(6)
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
    for u, v in edges:
        g.add_edge(u, v)

    g.dfs(0)
    g.bfs(0)

    print("Graph is connected:", g.is_connected())
    print("Shortest path from 0 to 5:", g.shortest_path(0, 5))
