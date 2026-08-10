class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distance = []
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(y2 - y1) + abs(x2 - x1)
                distance.append((cost, i, j))
        distance.sort()
        parent = list(range(n))
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py
        count = 0
        for cost, u, v in distance:
            if find(u) != find(v):
                union(u, v)
                count += cost
            else:
                continue
        return count