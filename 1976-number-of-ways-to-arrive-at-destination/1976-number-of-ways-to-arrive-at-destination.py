from heapq import heappush, heappop
class Solution:
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        pq = [(0, 0)]  
        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            for v, time in graph[u]:
                newDist = d + time
                if newDist < dist[v]:
                    dist[v] = newDist
                    ways[v] = ways[u]
                    heappush(pq, (newDist, v))
                elif newDist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n - 1]