class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                parent[px] = py

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)

        mp = {}

        for i in range(len(parent)):
            root = find(i)
            mp[root] = mp.get(root, 0) + 1

        return len(mp)