class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        visiting = set()
        safe = set()
        def dfs(start):

            if start in visiting:
                return False

            if start in safe:
                return True

            visiting.add(start)

            for nei in graph[start]:
                if not dfs(nei):
                    visiting.remove(start)
                    return False

            visiting.remove(start)
            safe.add(start)

            return True
        ans = []
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans
