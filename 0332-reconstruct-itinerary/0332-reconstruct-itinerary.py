class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for u, v in tickets:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
        for key, value in graph.items():
            if len(value) > 0:
                value.sort(reverse=True)
        ans = []
        def dfs(start):
            while start in graph and graph[start]:
                visit = graph[start].pop()
                dfs(visit)
            ans.append(start)
        dfs('JFK')
        return ans[::-1]
            
