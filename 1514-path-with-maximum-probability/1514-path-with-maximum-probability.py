import heapq
class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int
    ) -> float:
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))
        best = [0.0] * n
        best[start] = 1.0
        heap = []
        heapq.heappush(heap, (-1.0, start))
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob
            if node == end:
                return prob
            for nei, p in graph[node]:
                newprob = p * prob
                if newprob > best[nei]:
                    best[nei] = newprob
                    heapq.heappush(heap, (-newprob, nei))
        return 0


       