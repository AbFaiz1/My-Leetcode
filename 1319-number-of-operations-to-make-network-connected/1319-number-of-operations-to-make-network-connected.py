class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

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

        for u, v in connections:
            if find(u) == find(v):
                count += 1
            else:
                union(u, v)

        components = 0

        for i in range(n):
            if find(i) == i:
                components += 1

        if count >= components - 1:
            return components - 1

        return -1