class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px
        for x, y in edges:
            px = find(x)
            py = find(y)
            if px != py:
                union(x, y)
            else:
                return [x, y]