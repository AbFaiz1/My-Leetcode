class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n))
        servers = set()
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px
        cables  = 0
        for x, y in connections:
            px = find(x)
            py = find(y)
            if px == py:
                cables += 1
            else:
                union(x, y)
        nc = 0
        for i in range(n):
            if parent[i] == i:
                nc += 1
        required = nc - 1
        if cables >= required:
            return required
        return -1
