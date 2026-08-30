from collections import deque
class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        remaining = n
        while remaining > 2:
            size = len(q)
            remaining -= size
            for _ in range(size):
                leaf = q.popleft()
                for neighbour in graph[leaf]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        q.append(neighbour)
        return list(q)