class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        ans = []
        def solve(i, temp):
            if i >= len(arr):
                ans.append(temp.copy())
                return
            temp.append(arr[i])
            solve(i+1, temp)
            temp.pop()
            solve(i+1, temp)
        solve(0, [])
        return ans