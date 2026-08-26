from heapq import heappush, heappop
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], end: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, cost))
        def bfs(start, end):
            connection = [float("inf")] * n
            pq = []
            connection[start] = 0
            heappush(pq, (0, start))
            while pq:
                dis, node = heappop(pq)
                dis = -dis
                if dis > connection[node]:
                    continue
                for nei, cost in graph[node]:
                    newdis = cost + dis
                    if newdis <= end and newdis <= connection[nei]:
                        connection[nei] = newdis
                        heappush(pq, (-newdis, nei))
            count = 0
            for i in range(n):
                if i != start and connection[i] <= end:
                    count += 1
            return count
        mini = float(inf)
        for i in range(n):
            count = bfs(i, end)
            if count <= mini:
                mini = count
                idx = i
        return idx
            