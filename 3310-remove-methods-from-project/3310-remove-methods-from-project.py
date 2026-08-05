class Solution:
    def remainingMethods(self, n: int, k: int, arr: List[List[int]]):

        graph = [[] for _ in range(n)]

        for u, v in arr:
            graph[u].append(v)

        suspicious = set([k])

        def dfs1(node):
            for nei in graph[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    dfs1(nei)

        dfs1(k)

        for u, v in arr:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        ans = []

        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans