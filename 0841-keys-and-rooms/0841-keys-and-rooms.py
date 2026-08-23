class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        def dfs(start):
            if start in visited:
                return
            visited.add(start)
            for nei in rooms[start]:
                dfs(nei)
        dfs(0)
        for i in range(n):
            if i not in visited:
                return False
        return True