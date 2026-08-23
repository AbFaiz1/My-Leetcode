class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(start, temp):
            temp.append(start)
            if start == len(graph) - 1:
                ans.append(temp.copy())
                if temp:
                    temp.pop()
                return
            for nei in graph[start]:
                dfs(nei, temp)
            if temp:
                temp.pop()
        dfs(0, [])
        return ans