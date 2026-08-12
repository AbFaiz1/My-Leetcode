class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        tin = [-1] * n
        low = [-1] * n
        timer = 0
        bridges = []
        def dfs(u, parent):
            nonlocal timer
            tin[u] = low[u] = timer
            timer += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if tin[v] != -1:
                    low[u] = min(low[u], tin[v])
                else:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > tin[u]:
                        bridges.append([u, v])
        dfs(0, -1)
        return bridges
