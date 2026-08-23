class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
        visited = set()
        visiting = set()
        def dfs(start):
            if start in visiting:
                return False
            if start in visited:
                return True
            visited.add(start)
            visiting.add(start)
            for nei in graph[start]:
                if not dfs(nei):
                    visiting.remove(start)
                    return False
            visiting.remove(start)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True