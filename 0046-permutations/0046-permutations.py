class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        visited = set()
        ans = []
        def solve(temp):
            if len(temp) == len(arr):
                ans.append(temp.copy())
                return 
            for i in range(len(arr)):
                if i in visited:
                    continue
                visited.add(i)
                temp.append(arr[i])
                solve(temp)
                temp.pop()
                visited.remove(i)
        solve([])
        return ans