class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        ans = []
        def solve(i, temp):
            if sum(temp) == target:
                ans.append(temp[:])
                return
            if sum(temp) > target:
                return
            for start in range(i, len(arr)):
                temp.append(arr[start])
                solve(start, temp)
                temp.pop()
        solve(0, [])
        return ans
    