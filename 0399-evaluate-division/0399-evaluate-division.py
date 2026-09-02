class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for idx, eq in enumerate(equations):
            if eq[0] not in graph:
                graph[eq[0]] = []
            if eq[1] not in graph:
                graph[eq[1]] = []
            graph[eq[0]].append((eq[1], values[idx]))
            graph[eq[1]].append((eq[0], 1/values[idx]))
        ans = -1.0
        def dfs(start, end, temp):
            nonlocal ans
            if start in visited:
                return
            visited.add(start)
            for nei, val in graph[start]:
                if nei == end:
                    ans = val*temp
                    return
                dfs(nei, end, temp*val)
        realans = []
        for i in range(len(queries)):
            ans = -1.0
            visited = set()
            if queries[i][0] not in graph or queries[i][1] not in graph:
                realans.append(ans)
                continue 
            dfs(queries[i][0], queries[i][1], 1)
            realans.append(ans)
        return realans
        
        