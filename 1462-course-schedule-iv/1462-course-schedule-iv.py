class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        visiting = set()
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
        def dfs(start, end):
            if start == end:
                return True
            if start in visiting:
                return False
            visited.add(start)
            visiting.add(start)
            for nei in graph[start]:
                if nei not in visited:
                    if dfs(nei, end):
                        visiting.remove(start)
                        return True
            visiting.remove(start)
            return False
        ans = [False] * len(queries)
        for i in range(len(queries)):
            visited = set()
            if dfs(queries[i][0], queries[i][1]):
                ans[i] = True
            else:
                ans[i] = False
        return ans
        
