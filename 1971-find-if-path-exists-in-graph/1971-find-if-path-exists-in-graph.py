class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(start):
            if start in visited:
                return
            if start == destination:
                return True
            visited.add(start)
            for nei in graph[start]:
                if dfs(nei):
                    return True
        if dfs(source):
            return True
        return False
        

            
    