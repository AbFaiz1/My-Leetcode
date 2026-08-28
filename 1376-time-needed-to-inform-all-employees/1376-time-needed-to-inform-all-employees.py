class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        mp = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                mp[manager[i]].append(i) 
        
        def dfs(start):
            ans = 0      
            for nei in mp[start]:
                c = informTime[start] + dfs(nei)
                ans = max(ans, c)
            return ans
        return dfs(headID)
                

                