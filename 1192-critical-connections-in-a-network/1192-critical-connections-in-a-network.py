class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph = [[] for _ in range(n)]

        # Build graph
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        discovery = [-1] * n
        low = [-1] * n

        time = 0
        result = []

        def dfs(node, parent):
            nonlocal time

            discovery[node] = time
            low[node] = time
            time += 1

            for neighbor in graph[node]:

                # Don't go back through the same edge
                if neighbor == parent:
                    continue

                # If neighbor is not visited
                if discovery[neighbor] == -1:
                    dfs(neighbor, node)

                    # Update low value
                    low[node] = min(low[node], low[neighbor])

                    # Critical connection
                    if low[neighbor] > discovery[node]:
                        result.append([node, neighbor])

                else:
                    # Back edge
                    low[node] = min(low[node], discovery[neighbor])

        # Start DFS
        dfs(0, -1)

        return result