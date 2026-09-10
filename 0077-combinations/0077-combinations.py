class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1, n+1))
        ans = []
        def solve(i, temp):
            if len(temp) == k:
                ans.append(temp.copy())
                return
            if i >= len(arr):
                return
            solve(i+1, temp)
            temp.append(arr[i])
            solve(i+1, temp)
            temp.pop()
        solve(0, [])
        ans = list(set(map(tuple, ans)))
        return ans