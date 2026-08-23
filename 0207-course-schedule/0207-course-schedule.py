class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
        visited = set()
        visiting = set()
        def dfs(start):
            visited.add(start)
            visiting.add(start)
            for nei in graph[start]:
                if nei not in visited:
                    if dfs(nei):
                        return True
                else:
                    if nei in visiting:
                        return True
            visiting.remove(start)
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False
        return True

                     