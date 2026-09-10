class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = list(range(1,10))
        ans = []
        def solve(i, temp):
            if sum(temp) == n and len(temp) == k:
                ans.append(temp.copy())
                return 
            if i >= len(arr):
                return
            solve(i+1, temp)
            temp.append(arr[i])
            solve(i+1, temp)
            temp.pop()
        solve(0, [])
        return ans