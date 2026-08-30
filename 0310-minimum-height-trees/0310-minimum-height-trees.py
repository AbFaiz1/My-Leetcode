from collections import deque

class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]  # FIX: single-node tree has itself as the center

        graph = [[] for _ in range(n)]

        degree = [0] * n

        dq = deque()

        for u, v in edges:

            graph[u].append(v)

            graph[v].append(u)

            degree[u] += 1

            degree[v] += 1

        for i in range(len(degree)):

            if degree[i] == 1:

                dq.append(i)
        remaining = n
        while remaining > 2:
            for _ in range(len(dq)):  
                node = dq.popleft()
                remaining -= 1
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        dq.append(nei)
        ans = []
        while dq:
            val = dq.popleft()

            ans.append(val)

        return ans