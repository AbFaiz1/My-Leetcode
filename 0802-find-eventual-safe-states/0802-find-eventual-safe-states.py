class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        visiting = set()
        safe = set()
        def dfs(start):
            visited.add(start)
            visiting.add(start)
            for nei in graph[start]:
                if nei not in visited:
                    if not dfs(nei):
                        return False
                if nei in visiting:
                    return False
            visiting.remove(start)
            return True
        ans = []
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans