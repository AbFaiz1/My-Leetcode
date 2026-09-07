class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        ans = []
        def solve(i, temp):
            if i >= len(arr):
                ans.append(temp.copy())
                return
            solve(i+1, temp)
            temp.append(arr[i])
            solve(i+1, temp)
            temp.pop()
        solve(0, [])
        return ans