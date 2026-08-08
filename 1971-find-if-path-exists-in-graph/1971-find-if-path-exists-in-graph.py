from collections import deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        graph = [[] for _ in range(n)]

        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        queue = deque([source])
        visited = [False] * n
        visited[source] = True

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False